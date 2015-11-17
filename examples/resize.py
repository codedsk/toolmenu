from PIL import Image
import sys
import os
import argparse

# parse the command line options
command_parser = argparse.ArgumentParser(usage=None)
command_parser.add_argument(
    '--maxwidth',
    help='max width of the resized image',
    action="store",
    dest="maxwidth",
    default="150",
    type=int
)
command_parser.add_argument(
    '--maxheight',
    help='max height of the resized image',
    action="store",
    dest="maxheight",
    default="80",
    type=int
)

cl_options, cl_unknown = command_parser.parse_known_args()

maxwidth = cl_options.maxwidth
maxheight = cl_options.maxheight


for ifn in cl_unknown:
    ofn = os.path.splitext(ifn)[0] + "_thumb.jpg"
    im = Image.open(ifn)
    width,height = im.size
    ratio = min(1.0*maxwidth/width,1.0*maxheight/height)
    newwidth = width*ratio
    newheight = height*ratio
    im.thumbnail((int(newwidth),int(newheight)),Image.ANTIALIAS)
    im.save(ofn,'JPEG')

