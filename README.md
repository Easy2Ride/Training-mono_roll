
# Monodepth2 training with roll angles:

## Cloning the repository:

The entire repository can be cloned with submodules using
```
git clone https://github.com/shyam573/Training-mono_roll
git submodule init
git submodule update
```

## Executing the code:

This procedure removes the actual folder of KITTI dataset. The operations are performed on the current KITTI folder.

- KITTI like folder structure can be created without images can be created by running the command below. This creates a folder structure just like KITTI format by also copying the .bin and .txt files from velodyne and oxts folders.
```
python create_tree.py
```

- Images with roll angles with the method mentioned in section below can be created running the following command:
```
python create_images.py
```

- Training can be performed by executing the following command:
```
python monodepth2/train.py --model_name mono_model --png
```

- Results for all the models can be checked using:
```
python inference.py
```

## Method used:

- Roll angles are varied in between a range of -30 degrees and 30 degrees with a uniform distribution.

- The random degrees that are selected for increment or decrement is in between 0.08 and 0.14 with uniform distribution.

- For a sequence of images, when a random angle is generated, angles are incremented or decremented with random degrees for each image processed only once.

- Increment or decrement of angles is continued in steps of random degrees till the random angle is obtained and then vice versa is performed in steps of random degrees till zero is obtained.

- For a new image sequence, the roll angle again starts from zero.

- Random angle is generated again and the above steps are repeated for all image sequences.

- This entire procedure is offline. The zoom factor suitable for this approach is 1.75. Zoom factor is obtained based on trial and error method such that remove all black pixels at edges are removed, hence the image is corrected. The flag used of rotation is `cv2.INTER_LANCZOS4` and for resizing is `cv2.INTER_LINEAR`.

## KITTI Benchmark - Depth Results:

All the evaluations are done using median scaling on KITTI dataset.

| --model_name | abs_rel | sq_rel | rmse | rmse_log | delta<1.25 (a1)| delta<1.25<sup>2</sup> (a2) | delta<1.25<sup>3</sup> (a3) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mono_640x192_original         | 0.115 | 0.903 | 4.863 | 0.193 | 0.877 | 0.959 | 0.981 |
| mono_1024x320_original        | 0.115 | 0.882 | 4.701 | 0.190 | 0.879 | 0.961 | 0.982 |
| mono_640x192_no_roll          | 0.117 | 0.902 | 4.897 | 0.194 | 0.872 | 0.958 | 0.981 |
| mono+stereo_640x192_no_roll   | 0.108 | 0.820 | 4.693 | 0.188 | 0.884 | 0.961 | 0.981 |
| **mono_640x192_roll**         | **0.146** | **0.995** | **5.592** | **0.225** | **0.800** | **0.942** | **0.977** |
| **mono+640x192_crop_and adjusted_intrinsics** | **0.166** | **1.540** | **6.742** | **0.261** | **0.761** | **0.914** | **0.962** |
| **mono+640x192_no_crop**      | **0.120** | **0.886** | **4.860** | **0.197** | **0.869** | **0.958** | **0.981** |

## Inference results:

The results are not satisfactory.


#### No angle:

![alt text](images/out_image_angle_0.jpg)

#### +5 degrees:

![alt text](images/out_image_angle_5.jpg)

#### +10 degrees:

![alt text](images/out_image_angle_10.jpg)

#### +15 degrees:

![alt text](images/out_image_angle_15.jpg)


#### +30 degrees:

![alt text](images/out_image_angle_30.jpg)


#### -5 degrees:

![alt text](images/out_image_angle_-5.jpg)


#### -10 degrees:

![alt text](images/out_image_angle_-10.jpg)
<<<<<<< HEAD
=======


## Pose evaluation:

#### KITTI data without roll:

##### Input images:
Frame_0            |  Frame_10
:-------------------------:|:-------------------------:
![alt text](images/pose_1_no_rot.png)  |  ![alt text](images/pose_2_no_rot.png)


| --model_name                  | axis angle | translation |
| --- | --- | --- |
| mono_640x192_no_roll          | [[[[ 0.00655744 -0.00267642 -0.00119118]] [[-0.00431914  0.007259    0.00880607]]]]  | [[[[ 0.00135109  0.00106663 -0.05294015]] [[ 0.00179297  0.0003      0.00100699]]]] |
| mono_640x192_original         | [[[[ 0.00401209 -0.01463537  0.00204289]] [[ 0.00595027  0.00032399  0.00139341]]]] | [[[[ 0.00170265  0.00081443 -0.04820688]] [[ 0.00103417 -0.0022139   0.00141263]]]] |
| mono_640x192_roll             | [[[[ 0.00247418 -0.00416443 -0.00153273]] [[ 0.00149564  0.00071484  0.00152816]]]]  | [[[[ 9.9882437e-04  9.8287608e-05 -2.0081338e-02]] [[ 6.6675222e-04 -7.7092653e-04 -4.2723786e-04]]]] |
| mono_1024x320_original        | [[[[ 0.00247418 -0.00416443 -0.00153273]] [[ 0.00149564  0.00071484  0.00152816]]]]  | [[[[ 9.9882437e-04  9.8287608e-05 -2.0081338e-02]] [[ 6.6675222e-04 -7.7092653e-04 -4.2723786e-04]]]] |
| mono+640x192_crop_and adjusted_intrinsics        | [[[[ 0.00757046 -0.00610405 -0.0020394 ]] [[ 0.00601145 -0.01096405 -0.00219242]]]]  | [[[[-0.03009547 -0.00815338 -0.04944364]] [[ 0.00671122  0.00480929 -0.00732381]]]] |
| mono+640x192_no_crop | [[[[ 0.00511242  0.00064716 -0.00039573]] [[-0.00151218  0.00673385  0.00404888]]]]   | [[[[ 0.0002227   0.00096126 -0.05561864]] [[-0.00212339  0.00022645 -0.0012411 ]]]] |
| mono+stereo_640x192_no_roll      | [[[[ 0.00523074 -0.00421901  0.00272432]] [[ 0.02156832  0.01409656  0.00287587]]]] | [[[[ 0.00511361  0.00631492 -0.28275436]] [[-0.00557166  0.00051804 -0.0031521 ]]]] |


#### KITTI data with roll:
##### Initial intrinsics for four scales:
Scale 1:
[[371.19998   0.      320.        0.     ]
 [  0.      368.63998  96.        0.     ]
 [  0.        0.        1.        0.     ]
 [  0.        0.        0.        1.     ]]

Scale 2:
[[185.59999   0.      160.        0.     ]
 [  0.      184.31999  48.        0.     ]
 [  0.        0.        1.        0.     ]
 [  0.        0.        0.        1.     ]]

Scale 3:
[[92.799995  0.       80.        0.      ]
 [ 0.       92.159996 24.        0.      ]
 [ 0.        0.        1.        0.      ]
 [ 0.        0.        0.        1.      ]]

Scale 4:
[[46.399998  0.       40.        0.      ]
 [ 0.       46.079998 12.        0.      ]
 [ 0.        0.        1.        0.      ]
 [ 0.        0.        0.        1.      ]]

##### Modified intrinsics for four scales:
The initial intrinsics are modified by scaling them with a factor of 1242/710 across x-axis and 375/214 across y-axis.
 
Scale 1:
[[212.19968   0.      182.93076   0.     ]
[  0.      210.37056  54.784     0.     ]
 [  0.        0.        1.        0.     ]
 [  0.        0.        0.        1.     ]]

Scale 2:
[[106.09984   0.       91.46538   0.     ]
 [  0.      105.18528  27.392     0.     ]
 [  0.        0.        1.        0.     ]
 [  0.        0.        0.        1.     ]]

Scale 3:
[[53.04992  0.      45.73269  0.     ]
 [ 0.      52.59264 13.696    0.     ]
 [ 0.       0.       1.       0.     ]
 [ 0.       0.       0.       1.     ]]

Scale 4:
[[26.52496   0.       22.866344  0.      ]
 [ 0.       26.29632   6.848     0.      ]
 [ 0.        0.        1.        0.      ]
 [ 0.        0.        0.        1.      ]]

Frame_0            |  Frame_10
:-------------------------:|:-------------------------:
![alt text](images/pose_1_rot.png)  |  ![alt text](images/pose_2_rot.png)

| --model_name                  | axis angle | translation |
| --- | --- | --- |
| mono_640x192_no_roll          | [[[[ 0.00728744  0.00106746 -0.00520063]] [[-0.00322976  0.00740163  0.00878016]]]]  | [[[[ 0.00124007  0.00078411 -0.04481828]] [[ 0.00239687  0.00029508 -0.00011296]]]] |
| mono_640x192_original         | [[[[ 0.00445435  0.00067883 -0.00376851]] [[ 0.00281886  0.00014292  0.00143521]]]]  | [[[[ 2.0593926e-03  5.9843867e-04 -4.5199975e-02]] [[ 3.5944282e-05 -2.1570239e-03  2.1252770e-04]]]] |
| mono_640x192_roll             | [[[[ 0.00448418 -0.0342516  -0.0026397 ]] [[-0.00924    -0.02129632  0.00076043]]]]  | [[[[-0.00308903  0.00079387 -0.02370519]] [[ 0.01330386  0.00162566 -0.01314305]]]] |
| mono_1024x320_original        | [[[[ 0.00270717 -0.00431579 -0.00789273]] [[ 0.00181455  0.00062207  0.00094025]]]]  | [[[[ 9.5329963e-04 -1.9483448e-05 -1.7933989e-02]] [[ 1.0520169e-03 -6.6787860e-04 -3.4925943e-05]]]] |
| mono+640x192_crop_and adjusted_intrinsics        | [[[[ 0.00886186 -0.00788227 -0.01050381]] [[ 0.00759645 -0.01228975 -0.00436501]]]]  | [[[[-0.02475407 -0.00672459 -0.0402808 ]] [[ 0.00582408  0.00386715 -0.00672717]]]] |
| mono+640x192_no_crop | [[[[ 0.00665126  0.00229863 -0.00854432]] [[-0.00214099  0.00639689  0.00334335]]]]   | [[[[ 0.00017955  0.00054971 -0.04360052]] [[-0.00229242  0.00083296 -0.00201386]]]] |
| mono+stereo_640x192_no_roll      | [[[[ 0.00655371 -0.00302104 -0.00490357]] [[ 0.01817443  0.01174646  0.00278738]]]] | [[[[ 0.00473535  0.00483456 -0.23759145]] [[-0.00314006  0.00158418 -0.00561508]]]] |
>>>>>>> a763fff7b9fd830157bdd0a0efc567ce3f7f4873
