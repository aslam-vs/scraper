import urllib
from urlparse import urlparse

from django.core.files import File
from .models import Images, Page

import logging
logger = logging.getLogger(__name__)


def save_images(image_list, page):
    """
     save all images in database
     args: image_list,page
     """
    for image in image_list:
        try:
            img_url = image['image_src']
            name = urlparse(img_url).path.split('/')[-1]
            content = urllib.urlretrieve(img_url)

            image_obj = Images()
            image_obj.width = image['width']
            image_obj.height = image['height']
            image_obj.page = page
            image_obj.save()
            image_obj.image.save(name, File(open(content[0])), save=True)
        except Exception as e:
            logger.error(e)


def save_meta_data(meta_data, input_url):
    """
    save html meta data in database
    args: meta_data,input_url
    """
    try:
        page = Page()
        page.link_url = input_url
        page.og_title = meta_data['og_title']
        page.twitter_title = meta_data['twitter_title']
        page.title = meta_data['title']
        page.save()

        return page

    except Exception as e:
            logger.error(e)