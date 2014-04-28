import os
import arcpy
import pythonaddins

tbxfile = os.path.join(os.path.dirname(__file__), r'Scripts\AGOLThumbnails.tbx')

class thumbnail_button(object):
    """Implementation for AGOLThumbnails_addin.thumbnail_button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(tbxfile, "CreateAGOLThumbnail")