from django.db import models

# Models Created to store all variables for the site into sqlite3 database

# All posts may be changed/ deleted or new ones added with Post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.FileField(upload_to='post_image', blank=True)
    # landscape is a boolean field used to adjust given bos size (see 'art.html')
    landscape = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# Short Info about the artist displayed on home page
class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.CharField(max_length=100)
    profilepicture = models.FileField(upload_to='artist_image', blank=True)

    def __str__(self):
        return self.name

# All changeable data displayed buy the carousel on the home page
class MainCarousel(models.Model):
    car_title = models.CharField(max_length=200)
    car_image = models.FileField(upload_to='carousel_image', blank=True)
    car_text = models.TextField()

    def __str__(self):
        return self.car_title

# Featured work relating to the Carousel model
class Featured(models.Model):
    featured_image = models.FileField(upload_to='featured_image', blank=True)
    featured_title = models.CharField(max_length=200)
    featured_text = models.TextField()

    def __str__(self):
        return self.featured_title

# Data giving info about the nature of the website
class About(models.Model):
    about_image = models.FileField(upload_to='about_image', blank=True)
    about_title = models.CharField(max_length=200)
    about_text = models.TextField()

    def __str__(self):
        return self.about_title