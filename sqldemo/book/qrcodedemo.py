#! /usr/bin/env python
#coding=utf-8
import qrcode
 
img = qrcode.make('http://www.tuweizhong.com')
# img <qrcode.image.pil.PilImage object at 0x1044ed9d0>
 
with open('test.png', 'wb') as f:
    img.save(f)
