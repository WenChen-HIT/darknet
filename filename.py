# coding=utf-8
import os
import os.path

rootdir = './data/00/image_0'
output = open('./00imagefile.txt', 'w')
# rootdir = './data/rgb'
# output = open('./rgbimagefile.txt', 'w')

for parent, dirnames, filenames in os.walk(rootdir):
    for dirname in dirnames:
        print("parent is" + parent)
        print("dirname is " + dirname)
    filenames.sort()
    for filename in filenames:
        print("parent is " + parent)
        print("filename is " + filename)
        print("the full name of the file is " + os.path.join(parent, filename))
        currFilePath = os.path.join(parent, filename)
        output.write(currFilePath)
        output.write('\n')
output.close()

