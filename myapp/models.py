from django.db import models


# Create your models here.
class NewsInformation(models.Model):
    news_title = models.CharField(primary_key=True, max_length=50)
    news_details = models.TextField(max_length=200)
    cover_image = models.ImageField(default='default.jpg', upload_to='cover_image', null=True)
