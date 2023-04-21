import replicate
import os
	
def upscale(image):
	os.environ["REPLICATE_API_TOKEN"]

	output = replicate.run(
    "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3",
    	input = {
    		"img": image,
    		"scale" : 3,
    		"version" : "v1.4"
  	  }, 
	  )
	print(output)
	
	return output