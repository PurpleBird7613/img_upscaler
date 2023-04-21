from django.shortcuts import render,redirect,HttpResponse
from . models import Cloud_Image,Upscaled_Image,Developer
from . forms import Cloud_Image_Form,Upscaled_Image_Form
import environ
from django.contrib.auth import get_user_model,login,logout,authenticate
from django.contrib.auth.models import User
import replicate
import os
from . upscale import upscale

env = environ.Env()
# reading .env file 
environ.Env.read_env()
env("REPLICATE_API_TOKEN")

# Home	
def home(request):
	context = {}
	
	developer = Developer.objects.all().order_by("-date")[0:1]
	context["developer"] = developer
	
	# Creating a user if user is not authenticated 
	if not request.user.is_authenticated:
		U = get_user_model()
		u = U.objects.all().order_by("id")[0::-1][0:1]	
		for i in u:
			username = int(i.username) # Usernames are in int form
			username += 1
		# creation of user
		user = User.objects.create_user(username, password="Password@")
		user.save()
		login(request,user)
		return redirect("home")
	
	user = request.user
	context["user"] = user

	upscaled_image = Upscaled_Image.objects.filter(author = user).order_by("-date")[0:2]
	context["image"] = upscaled_image
	
	# Uploading The Image to Cloudinary
	if request.method == "POST":
		image = request.FILES.get("image","")
		if image == "":
			return HttpResponse("Please upload an Image!!!")
		
		form = Cloud_Image_Form(data = request.POST,files = request.FILES)
		if form.is_valid():
			obj = form.save(commit = False)
			obj.image = image
			obj.author = user
			obj.save()
			
		# Upscaling the uploaded image
		cloud_image = Cloud_Image.objects.filter(author = user).order_by("-date")[0:1]
		for img in cloud_image:
			# Uploading the link of the Upscaled Image
			Obj = Upscaled_Image(image = upscale(img.image.url),author = user)
			Obj.save()							
		return redirect("home")
	
	return render(request,"home.html",context)
	