#!/usr/bin/python
# -*- coding:utf-8 -*-

import SSD1331
import time
import config
import traceback
import  os

from PIL import Image,ImageDraw,ImageFont

try:
    disp = SSD1331.SSD1331()

    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()

    # Create blank image for drawing.
    image1 = Image.new("RGB", (disp.width, disp.height), "black")
    draw = ImageDraw.Draw(image1)
    font = ImageFont.truetype('Font.ttf', 20)
    font10 = ImageFont.truetype('Font.ttf',13)
    print ("***draw line")
    draw.line([(0,0),(0,63)], fill = "BLUE",width = 5)
    draw.line([(0,0),(95,0)], fill = "BLUE",width = 5)
    draw.line([(0,63),(95,63)], fill = "RED",width = 5)
    draw.line([(95,0),(95,63)], fill = "BLUE",width = 5)
    print ("***draw rectangle")
    draw.rectangle([(5,5),(90,30)],fill = "BLUE")
    
    print ("***draw text")
    draw.text((8,0), u'%%%%% ', font = font, fill = "WHITE")
    draw.text((12, 40), 'URA', font = font10, fill = "BLUE")

    #image1=image1.rotate(45) 
    disp.ShowImage(image1,0,0)
    time.sleep(5)
    
    print ("***draw image")
    image = Image.open('sq.png')	
    disp.ShowImage(image,10,10)
    
except KeyboardInterrupt:
    print ('\r\ntraceback.format_exc():\n%s' % traceback.format_exc())
    config.module_exit()
    exit()

