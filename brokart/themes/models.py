from django.db import models

# models for themes.
class SitSetting(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()
