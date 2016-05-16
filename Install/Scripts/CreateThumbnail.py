#-------------------------------------------------------------------------------
# Name:        CreateThumbnail
# Purpose:     Takes an existing thumbnail image and standardizes it.
#
# Author:      Shad Campbell - Deschutes County, Oregon
#
# Created:     21/03/2014
# Copyright:   (c)ShadCampbell 2014
# Licence:     Apache
#-------------------------------------------------------------------------------

import os, arcpy
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL.ImageChops import difference

##Get input parameters
title = arcpy.GetParameterAsText(0)
private = arcpy.GetParameterAsText(1)
stype = arcpy.GetParameterAsText(2)
departement = arcpy.GetParameterAsText(3)
thumbnail = arcpy.GetParameterAsText(4)
crop = arcpy.GetParameterAsText(5)
outputFolder = arcpy.GetParameterAsText(6)


def resize_and_crop(img, size, crop_type='top'):

    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                int(round((img.size[1] + size[1]) / 2)))
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (int(round((img.size[0] - size[0]) / 2)), 0,
                int(round((img.size[0] + size[0]) / 2)), img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
            Image.ANTIALIAS)
    # If the scale is the same, we do not need to crop
    return img;

##title = "Testing 123"
##private ="False"
##stype = "Web Map"
##departement = "Community Development"
##thumbnail = r"D:/Deschutes.png"
##outputFolder = r"D:/"

## Setup
imgFolder = os.path.abspath(__file__ + "/../../Images") #UP 2 folders and into Images folder.
smfont = ImageFont.truetype("corbel.ttf",12)
bgfont = ImageFont.truetype("corbel.ttf",18)

## Create Logo
logo = Image.new("RGBA", (30,30), "rgb(0,0,0)")
logoImg = Image.open(imgFolder + "//Logo.png")
logo.paste(logoImg, (0,0), logo)

## Create Lock
lock = Image.new("RGBA", (24,24))
if (private=="True"):
    lockImg = Image.open(imgFolder + "//Lock.png")
else:
    lockImg = Image.open(imgFolder + "//Unlock.png")
lock.paste(lockImg, (0,0), lockImg)

## Create Department Area
departmentArea = Image.new("RGBA", (200,133))
draw = ImageDraw.Draw(departmentArea)
draw.rectangle((0,100,200,133),fill=(200,200,200,226))
draw.text((33, 120),departement,(50,50,50),font=smfont)
draw.text((33, 103),title,(50,50,50),font=bgfont)

## Create Service Area
serviceArea = Image.new("RGBA", (100,20), "rgb(50,50,50)")
draw = ImageDraw.Draw(serviceArea)
draw.text((10, 2),stype,(200,200,200),font=bgfont)
serviceAreaRotated = serviceArea.rotate(90)

## Create new thumbnail and add components.
newThumb = Image.open(thumbnail)
if (newThumb.size!=(200, 133)):
    newThumb = resize_and_crop(newThumb, (200, 133), crop)

newThumb.paste(serviceAreaRotated, (0,0), serviceAreaRotated)
newThumb.paste(departmentArea, mask=departmentArea)
newThumb.paste(lock, (175,104), lock)
newThumb.paste(logo, (2,102), logo)
newThumb.save(outputFolder + "/" + title.replace(" ", "_") + "_" + stype.replace(" ", "_") + ".png")

