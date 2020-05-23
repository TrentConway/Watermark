from PIL import Image
from math import degrees, atan
import argparse
import os


# Global Variables used for testing

# Path to images:
TYPES = ["png", "jpeg"]

# Path to images:
FOLDER = './'
LOGOPATH = './img/star-wars.png'
IMAGEPATH = './img/yoda.jpeg'
OUTPUTPATH = "./watermark/"
SAVEPATH = 'starwars.png'

# ALPHA
TRANSPARENCY = 65   


#TODO doc strings
# Watermark image
def watermark(image, logo, alpha=50, rotate = False, scale=False): 
    
    # Rotate image
    imageWidth, imageHeight = image.size  
    logo = logo.rotate(int(degrees(atan(imageHeight/imageWidth)))) if rotate == True else logo
    
    # Resize image
    logo = logo.resize(image.size) if scale == True else logo
    
    # Apply transparency
    alpha_mask = logo.split()[3].point(lambda i: i * alpha / 100.)
    
    # Watermark
    logoWidth, logoHeight = logo.size  
    image.paste(logo, ((imageWidth - logoWidth)//2, (imageHeight - logoHeight)//2), mask=alpha_mask)
    
    # Return image
    return image


#TODO ABSTRACT INTO FUNCTION
#TODO ERROR HANDLING 
# run when script is called
if __name__ == "__main__":
	
	# Input parameters
	parser = argparse.ArgumentParser()

	#positional arguments
	parser.add_argument("imagepath", type=str, help="path to image")
	parser.add_argument("logopath", type=str, help="path to logo")	

	# Optional arguments
	parser.add_argument("-a", "--alpha", type=int,
                    help="transparency of the logo")	
	parser.add_argument("-r", "--rotate", action="store_true",
                    help="Rotate Watermark on image")
	parser.add_argument("-s", "--scale", action="store_true",
		    help="Scale logo to fix image")
	args = parser.parse_args()


	#TO DO VALIDATE INPUTS

	
	image = Image.open(args.imagepath)
	logo = Image.open(args.logopath)
	image_marked = watermark(image, logo, alpha = args.alpha, rotate= args.rotate, scale= args.scale)
	if not os.path.exists(OUTPUTPATH):
		os.makedirs(OUTPUTPATH)
	image_marked.save(OUTPUTPATH + SAVEPATH)
