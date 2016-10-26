from bs4 import BeautifulSoup
import time
import urllib
import cStringIO
from PIL import Image
from concurrent import futures

from .helper import save_images, save_meta_data

import logging
logger = logging.getLogger(__name__)



class Scraper(object):

    """Scraper class for scraping datas from url"""

    def __init__(self, url):
        self.url = url

    def get_soup(self):
        """ Return BeautifulSoup object of particular page"""
        page = urllib.urlopen(self.url).read()
        soup = BeautifulSoup(page, "html.parser")
        return soup

    def get_meta_data(self):
        """ Return meta data from page"""
        start = time.clock()
        soup = self.get_soup()

        og_title = self.get_og_title(soup)
        twitter_title = None
        if not og_title:
            twitter_title = self.get_twitter_title(soup)
        title = None
        if not og_title and not twitter_title:
            title = self.get_title(soup)

        end = time.clock()
        total_time = end - start

        return {'og_title': og_title, 'twitter_title': twitter_title,
                'title': title, 'total_time': total_time}

    def get_og_title(self, soup):
        """ 
        Return og title of page
        args : soup (beautifulsoup object)
        """
        og_title = soup.find("meta", property="og:title")
        try:
            return og_title['content']
        except:
            return None

    def get_twitter_title(self, soup):
        """ 
        Return twitter title of page
        args : soup (beautifulsoup object)
        """
        twitter_title = soup.find("meta", {"name": "twitter:title"})
        try:
            return twitter_title['content']
        except:
            return None

    def get_title(self, soup):
        """ 
        Return title of page
        args : soup (beautifulsoup object)
        """
        return soup.title.renderContents()

    def get_images(self):
        """ 
        Return images,image count,time for fetch of page
        """
        start = time.clock()

        soup = self.get_soup()
        image_tags = soup.find("body").findAll("img")
        image_count = len(image_tags)

        with futures.ThreadPoolExecutor(max_workers=5) as executor:
            image_list = list((executor.submit(self.get_image_list, image_tag))
                              for image_tag in image_tags)
        img_list = []
        for future in futures.as_completed(image_list):
            try:
                img_list.append(future.result())
            except Exception as exc:
                # print('generated an exception: %s' % (exc))
                logger.error('generated an exception: %s' % (exc))
            else:
                logger.info("Asynch task completed")

        end = time.clock()
        total_time = end - start

        return {'image_list': img_list, 'total_time': total_time,
                'image_count': image_count}

    def get_image_list(self, image_tag):
        """ 
        Return image src,width,height from image tag
        args : image_tag (beautifulsoup image tag object)
        """
        image_src = image_tag['src']
        width, height = self.get_dimensions(image_src)
        return {'image_src': image_src, 'width': width, 'height': height}

    def get_dimensions(self, image_url):
        """ 
        Return dimensions of image 
        args : image_url
        """
        im = self.get_image_file(image_url)
        width, height = im.size
        return width, height

    def get_image_file(self, image_url):
        """ 
        Return image url as a image file
        args : image_url
        """
        file = cStringIO.StringIO(urllib.urlopen(image_url).read())
        im = Image.open(file)
        return im


def scraper_call_fun(input_url):
    """
    all functions controlling here
    args: input_url
    """
    scraper_obj = Scraper(input_url)
    meta_data = scraper_obj.get_meta_data()
    page = save_meta_data(meta_data, input_url)

    image_dict = scraper_obj.get_images()
    image_calc_time = image_dict['total_time']
    image_list = image_dict['image_list']
    image_count = image_dict['image_count']

    save_images(image_list, page)

    return {'meta_data': meta_data, 'image_dict': image_dict}
