
from glob import glob
import cv2
import imageio
from PIL import Image
import random
import numpy as np
import os
import shutil
import errno

root_dir = 'kitti_data'
target_dir = 'kitti_data_n/'
folders =[]

tPath = glob(root_dir + '*/*/*/*')
for i in tPath:
    folders.append(i)
    


new = [x for x in folders if "image" in x]
print(len(folders), len(new))

j =0
for i in folders:
    if i not in new:
        sub_dir = i.split("/", 1)[-1]
        src = i
        print(i)
        dest = target_dir+sub_dir
        j+=1
        if not os.path.exists(i):
            pass
        else:
            try:
                shutil.copytree(src, dest) 
            except:
                try:
                    shutil.copyfile(src, dest)
                except:
                    pass
