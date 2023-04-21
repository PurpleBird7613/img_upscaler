from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
 
# Uploading image to Cloudinary
class Cloud_Image(models.Model):
	image = CloudinaryField("Image", resource_type = "image",null = False, blank = False)
	date = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User,on_delete = models.CASCADE)

# Uploading the Uplscaled-Image link to database
class Upscaled_Image(models.Model):
	image = models.TextField(null = False,blank = False)
	date = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User,on_delete = models.CASCADE)
	
# Developer Link
class Developer(models.Model):
	link = models.TextField(null = True,blank = True)
	date = models.DateTimeField(auto_now_add = True)
	
