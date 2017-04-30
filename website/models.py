from django.db import models
from stdimage.models import StdImageField
from ckeditor.fields import RichTextField
import re
# Create your models here.



class Author(models.Model):
    """
    represents Author of content
    """
    name = models.CharField(max_length=250,default='')
    profile_picture = StdImageField(upload_to='uploads/profiles',
                            variations={'thumbnail': {'width': 100, 'height': 75}})
    bio=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    """
    represent article in the site will be shown on article page

    """
    post = RichTextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=250,default='')
    author=models.ForeignKey('Author',related_name='articles',blank=True,null=True)
    picture= StdImageField(upload_to='uploads/images',
                          variations={'thumbnail': {'width': 264, 'height': 140,'crop':True}},blank=True,null=True)
    video_url= models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title



class Video(models.Model):
    """
    represent videos in the site will be shown on videos page
    """
    date = models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=250, default='')
    author=models.ForeignKey('Author',related_name='videos',null=True)
    video_url= models.URLField()
    video_thumbnail=models.ImageField(upload_to='uploads/thumbnails',blank=True,null=True)
    def __str__(self):
        return self.title


    @property
    def embed_url(self):
        regex = r"(?:https:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)"

        return re.sub(regex, r"https://www.youtube.com/embed/\1", self.video_url)




class ResourceCategory(models.Model):
    """
    represent Resource Category in the site will be shown  as headers in  resources page

    """

    category_name=models.CharField(max_length=250, default='')

    def __str__(self):
        return self.category_name





class Resource(models.Model):
    """
    represent Resources in the site will be shown  in resources page

    """
    title=models.CharField(max_length=250, default='')
    link=models.URLField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    category=models.ForeignKey('ResourceCategory',related_name='resources',blank=True,null=True)

    def __str__(self):
        return self.title




