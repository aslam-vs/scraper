Scraper
=========

	1 Get meta tags from the head part in below-mentioned priority (so if a exists, forget about b and c)

	a. meta content="Why Ford is Winning on the Social Web" data-page-subject="true" property="og:title" 

	b. meta content="Why Ford is Winning on the Social Web" data-page-subject="true" name="twitter:title" 

	c. title Why Ford is Winning on the Social Web

	2 From the body part, fetch all the images. With this, also find out the width and height of the image. (can use multi-threading to save time)

	3 A function to save all of this into the database.

	4 Display the time taken to complete 1 and 2



Getting Up and Running Locally
---------------------


The steps below will get you up and running with a local development environment. Assume you have the following installed:-

	pip
	virtualenv


Then install the requirements for your local development:-

	pip install -r requirements/local.txt


Then, create database and change DATABASES settings in settings.py:


You can now run the usual Django migrate and runserver commands:
cd src
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver





