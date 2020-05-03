![alt text](starwars.png "Baby Yoda")

## BRIEF:
The objective of the first activity is to interact with images and understand how they work, regardless of your prior programing experience.  
If you are new to python, don't worry, this is a great project to understand variables, loops and python basics too.

The activity is to write an application to place a logo onto an image. As you progress the application can be used to watermark a series of images. 

Before I write software, I decompose the application into a series of steps, that are simple and managable. The steps combined will then build the application. The steps I used are below and I also added hints to help you out along the way. 

At the end of the activity (end date), I will go live and program this application start to finish answering any questions along the way. I encourage you to have a go prior to the stream!

Have fun!

## STEPS:
1. User can put a logo in the center of the image  
__HINT:__ center of the image (imageLength - logoLength)/2
2. User can specify a path to the image and logo  
__HINT:__ at min PATH is a variable 
3. User can specify a list of images to logo  
__HINT:__ For Loop
4. User can specify a folder of images to logo  
__HINT:__ https://www.tutorialspoint.com/python/os_listdir.htm
5. User can specify the transparency of the logo  
__HINT:__ transparency is the alpha channel in an RGB image
6. The logo will scale to fit the image  
__HINT:__ resize & need some maths
7. User can specify if the logo is diagonal or horizontal  
__HINT:__ at min rotate 45 
8. Have fun and continue to add to this application


# HELP
Library that I used to complete this task is PIL:  
`python3 -m pip install Pillow`  
The `image` module in the Pillow library is extremely helpful to complete the task:  
https://pillow.readthedocs.io/en/stable/reference/Image.html  
This module contains functions:
* Open
* Paste
* Save  

These functions are a good starting place to begin the challenge.  
The PIL library contains a vast range of image manipulation functions that will be needed as you progress!


The python OS and SYS librarys may also come in handy - if you want to extend the program into a command line application.
https://www.pythonforbeginners.com/system/python-sys-argv


If you are using jupyter notebooks, the library  
`from IPython.display import display` and `display(image)` to show image in notebook
