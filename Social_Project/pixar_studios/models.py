from django.db import models
from django.contrib.auth.models import User

# Create your models here.
User._meta.get_field('email')._unique = True


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    facebook = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=5000)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class WebSites(models.Model):
    favicon = models.ImageField(upload_to='website_pics', blank=False)
    logo = models.ImageField(upload_to='website_pics', blank=False)
    short_film_page_description = models.TextField(max_length=5000)


class DisneyPlusBlogs(models.Model):
    image = models.ImageField(upload_to='dp_shorts_pics', blank=False)
    shorts_title = models.CharField(max_length=50)
    shorts_descriptions = models.TextField(max_length=5000)

    def __str__(self):
        return self.shorts_title


class TheatricalShorts(models.Model):
    image = models.ImageField(upload_to='th_shorts_pics', blank=True)
    poster = models.ImageField(upload_to='th_shorts_pics', blank=False)
    title_image = models.ImageField(upload_to='th_shorts_pics', blank=False)
    secondary_images = models.ImageField(upload_to='th_shorts_pics', blank=True)
    shorts_title = models.CharField(max_length=50)
    shorts_descriptions = models.TextField(max_length=5000)

    def __str__(self):
        return self.shorts_title
