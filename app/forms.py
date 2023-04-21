from django import forms
from . models import Cloud_Image,Upscaled_Image

# Cloud Image Form
class Cloud_Image_Form(forms.ModelForm):
	class Meta:
		model = Cloud_Image
		fields = ["image"]

# Upsscaled-Image Form
class Upscaled_Image_Form(forms.ModelForm):
	class Meta:
		model = Upscaled_Image
		fields = ["image"]