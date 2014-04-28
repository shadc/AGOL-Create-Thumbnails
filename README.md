AGOL Create Thumbnails
===========

This is an ArcCatalog addin that allows users to generate standardized thumbnails for ArcGIS Online.  With this addin you don't have to have Photoshop
or some other image manipulation software to brand and annotate your thumbnails for your organization. Simply crop a base image to 200 x 133 pixels 
and use this addin to do the rest. 

NOTE: This toolbar requires the python library Pillow be installed. The windows version (Pillow-2.3.0.win32-py2.7.exe) is included in this repository.
Install this before installing the toolbar. 

Start with this...

![alt tag](https://dl.dropboxusercontent.com/u/25277330/DSC_3229.JPG)
 
and end up with this...

![alt tag](https://dl.dropboxusercontent.com/u/25277330/Water_Levels.png)


Easily customize:

Modify the "Type" and "Department" by opening the toolbox (\install\scripts\AGOLThumbnails.tbx) in ArcCatalog and modifying the "parameters"
of the "Create AGOL Thumbnail" tool. 

Update the logo by replacing the logo file \install\images\Logo.png) with your 30 x 30 pixel logo.

Advanced:
Modify the colors, text, location, etc by modifying the CreateThumbnail.py file in the \install\Scripts\ folder.

After you have customized the add-in recompile it by double clicking the makeaddin.py file.  Then double click the 
AGOL Create Thumbnails.esriaddin to install the addin.  


Created By [shadcampbell](https://github.com/shadcampbell) [@shadc](https://twitter.com/shadc)

## Known Issues:
* Does not crop or resize an input image to 200 x 133 pixels.
* Long titles can run off the image.  

