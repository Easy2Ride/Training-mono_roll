
from glob import glob
import cv2
import imageio
from PIL import Image
import random
import numpy as np
import os
import shutil

root_dir = 'kitti_data/'
target_dir = 'kitt/'
folders =[]

for i in glob(root_dir + '*/*/*/*'):
    folders.append(i)

    
new_fold = [x for x in folders if "image" in x and not "txt" in x]
print(len(folders), len(new_fold))


angle_min = -30
angle_max = 30
angle_inc_min = 0.08
angle_inc_max = 0.14
straight_min = 40
straight_max = 70
ang_gen = True


def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LANCZOS4)
  return result

def cv2_clipped_zoom(img, zoom_factor):
    height, width = img.shape[:2]
    new_height, new_width = int(height * zoom_factor), int(width * zoom_factor)
    y1, x1 = max(0, new_height - height) // 2, max(0, new_width - width) // 2
    y2, x2 = y1 + height, x1 + width
    bbox = np.array([y1,x1,y2,x2])
    bbox = (bbox / zoom_factor).astype(np.int)
    y1, x1, y2, x2 = bbox
    cropped_img = img[y1:y2, x1:x2]
    resize_height, resize_width = min(new_height, height), min(new_width, width)
    pad_height1, pad_width1 = (height - resize_height) // 2, (width - resize_width) //2
    pad_height2, pad_width2 = (height - resize_height) - pad_height1, (width - resize_width) - pad_width1
    pad_spec = [(pad_height1, pad_height2), (pad_width1, pad_width2)] + [(0,0)] * (img.ndim - 2)
    result = cv2.resize(cropped_img, (resize_width, resize_height))
    result = np.pad(result, pad_spec, mode='constant')
    assert result.shape[0] == height and result.shape[1] == width
    return result

def rot_ang():
    global angle_cur 
    global rand_angle
    global ang_gen 
    global flag
    global mode
    if ang_gen == True:
        rand_angle = random.uniform(angle_min, angle_max)
        angle_cur = 0
        ang_gen = False
        if rand_angle>=0: flag = True
        if rand_angle<0: flag = False
    
    if angle_cur < rand_angle and flag == True and ang_gen == False:
        mode = "inc"
        if abs(angle_cur - rand_angle) < angle_inc_max and rand_angle > 0:
            angle_cur += angle_inc_max
            flag = False
        if abs(angle_cur) < angle_inc_min and rand_angle < 0:
            flag = False
            ang_gen = True
            
    if angle_cur > rand_angle and flag == False and ang_gen == False:
        mode = "dec"
        if abs(angle_cur - rand_angle) < angle_inc_max and rand_angle < 0:
            angle_cur -= angle_inc_min
            flag = True
        if abs(angle_cur) < angle_inc_min and rand_angle > 0:
            flag = True
            ang_gen = True
            
    def rot_aug(mode):
        global angle_cur 
        global rand_angle
        global ang_gen
        ang_sel = random.uniform(angle_inc_min, angle_inc_max)
        if mode == "inc":
            angle_cur += ang_sel 
        if mode == "dec":
            angle_cur -= ang_sel 
        if abs(angle_cur) < angle_inc_min:
            ang_gen = True     
        rot_image = img    
        return angle_cur
    
    angle_cur = rot_aug(mode)
    return angle_cur

temm = 0
def last_10chars(x):
    return(x[-10:])

for imgPath in new_fold:
    ang_gen = True
    print(temm)
    temm +=1
    sub_dir = imgPath.split("/", 1)[-1] 
    t = target_dir+sub_dir

    if os.path.exists(t) and os.path.isdir(t):
        shutil.rmtree(t)
        os.makedirs(t)
    else:
        os.makedirs(t)
    img_l = glob(imgPath +'/*.jpg')
    img_list =sorted(img_l, key = last_10chars)
    for img in img_list:  
        try:
            image = cv2.imread(img)
            img_name=os.path.basename(img)
            angle = rot_ang()
            rot_and_resized = cv2_clipped_zoom(rotate_image(image, angle), 1.75)
            save_path = t+str('/')+img_name
            cv2.imwrite(save_path, rot_and_resized)
        except:
            print('image missing')
            pass
