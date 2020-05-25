# Train log for Monodepth2 training with roll angles

## Original Monodepth2 evaluation results:

#### Mono_640x192:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 35.365 | std: 0.223

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.282  &   3.007  &   8.235  &   0.379  &   0.565  &   0.806  &   0.908  \\

-> Done!
```

#### Mono_1024x320:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 38.702 | std: 0.217

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.282  &   2.855  &   8.158  &   0.384  &   0.559  &   0.800  &   0.906  \\

-> Done!
```

## Training results with mono+stereo_640x192 KITTI without roll angles:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 6.495 | std: 0.241

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.282  &   2.897  &   8.169  &   0.383  &   0.557  &   0.801  &   0.906  \\

-> Done!
```


## Training results with roll angles:

- These are the results after epoch 20:
```
-> Computing predictions with size 640x192
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 29.070 | std: 0.156

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.337  &   4.068  &   9.099  &   0.426  &   0.490  &   0.747  &   0.873  \\

-> Done!

```
The training loss was around 0.0512.

- Thought that there could be an improvement if trained more, but there is not much. Here is the training loss pattern for 20th to 30th epoch:
```
epoch   0 | batch   1250 | examples/s:  22.0 | loss: 0.04706 | time elapsed: 00h14m40s | time left: 06h14m34s
epoch   0 | batch   1500 | examples/s:  25.4 | loss: 0.06215 | time elapsed: 00h17m31s | time left: 06h09m52s
epoch   0 | batch   1750 | examples/s:  15.8 | loss: 0.06182 | time elapsed: 00h20m23s | time left: 06h06m07s
epoch   0 | batch   2000 | examples/s:  17.8 | loss: 0.05184 | time elapsed: 00h23m14s | time left: 06h02m16s
Training
epoch   1 | batch    683 | examples/s:  13.5 | loss: 0.05280 | time elapsed: 00h45m28s | time left: 05h31m38s
epoch   1 | batch   2683 | examples/s:  17.7 | loss: 0.05847 | time elapsed: 01h07m43s | time left: 05h06m40s
Training
epoch   2 | batch   1366 | examples/s:  20.2 | loss: 0.04814 | time elapsed: 01h29m57s | time left: 04h43m01s
Training
epoch   3 | batch     49 | examples/s:  19.0 | loss: 0.04626 | time elapsed: 01h52m12s | time left: 04h19m59s
epoch   3 | batch   2049 | examples/s:  16.7 | loss: 0.04630 | time elapsed: 02h14m26s | time left: 03h57m11s
Training
epoch   4 | batch    732 | examples/s:  21.8 | loss: 0.05652 | time elapsed: 02h36m44s | time left: 03h34m37s
epoch   4 | batch   2732 | examples/s:  16.2 | loss: 0.05676 | time elapsed: 02h58m53s | time left: 03h11m58s
Training
epoch   5 | batch   1415 | examples/s:  21.8 | loss: 0.04842 | time elapsed: 03h21m10s | time left: 02h49m32s
Training
epoch   6 | batch     98 | examples/s:  15.5 | loss: 0.05048 | time elapsed: 03h43m28s | time left: 02h27m09s
epoch   6 | batch   2098 | examples/s:  23.1 | loss: 0.05468 | time elapsed: 04h05m38s | time left: 02h04m43s
Training
epoch   7 | batch    781 | examples/s:  17.2 | loss: 0.05899 | time elapsed: 04h27m56s | time left: 01h42m22s
epoch   7 | batch   2781 | examples/s:  17.3 | loss: 0.04428 | time elapsed: 04h50m10s | time left: 01h20m01s
Training
epoch   8 | batch   1464 | examples/s:  27.5 | loss: 0.04804 | time elapsed: 05h12m25s | time left: 00h57m41s
Training
epoch   9 | batch    147 | examples/s:  18.5 | loss: 0.05531 | time elapsed: 05h34m47s | time left: 00h35m22s
epoch   9 | batch   2147 | examples/s:  26.8 | loss: 0.04940 | time elapsed: 05h56m56s | time left: 00h13m03s
```

### Training:

#### Epoch 17:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 29.459 | std: 0.163

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.346  &   4.565  &   9.282  &   0.428  &   0.491  &   0.749  &   0.873  \\

-> Done!
```
#### Epoch 18:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 30.406 | std: 0.158

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.339  &   4.292  &   9.163  &   0.423  &   0.496  &   0.754  &   0.877  \\

-> Done!
```
#### Epoch 19:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 29.145 | std: 0.161

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.336  &   4.041  &   9.071  &   0.426  &   0.487  &   0.748  &   0.875  \\

-> Done!
```
#### Epoch 20:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 29.070 | std: 0.156

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.337  &   4.068  &   9.099  &   0.426  &   0.490  &   0.747  &   0.873  \\

-> Done!
```
#### Epoch 21:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 28.263 | std: 0.162

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.337  &   4.202  &   9.132  &   0.424  &   0.492  &   0.749  &   0.876  \\

-> Done!
```
#### Epoch 22:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 27.908 | std: 0.163

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.339  &   4.153  &   9.070  &   0.428  &   0.485  &   0.744  &   0.872  \\

-> Done!
```
#### Epoch 23:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 28.085 | std: 0.161

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.348  &   4.447  &   9.206  &   0.431  &   0.488  &   0.743  &   0.869  \\

-> Done!
```
#### Epoch 24:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 27.834 | std: 0.164

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.347  &   4.608  &   9.247  &   0.430  &   0.489  &   0.745  &   0.872  \\

-> Done!
```
#### Epoch 25:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 28.328 | std: 0.164

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.344  &   4.517  &   9.260  &   0.428  &   0.492  &   0.747  &   0.873  \\

-> Done!
```
#### Epoch 26:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 28.328 | std: 0.164

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.344  &   4.517  &   9.260  &   0.428  &   0.492  &   0.747  &   0.873  \\

-> Done!
```
#### Epoch 27:
```
-> Evaluating
   Mono evaluation - using median scaling
 Scaling ratios | med: 27.913 | std: 0.165

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.343  &   4.457  &   9.221  &   0.429  &   0.489  &   0.746  &   0.871  \\

-> Done!
```
#### Epoch 28:
```
-> Evaluating
 Mono evaluation - using median scaling
 Scaling ratios | med: 27.494 | std: 0.166

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.344  &   4.257  &   9.043  &   0.429  &   0.486  &   0.742  &   0.872  \\

-> Done!
```

#### Epoch 29:
```
-> Evaluating
 Mono evaluation - using median scaling
 Scaling ratios | med: 27.841 | std: 0.162

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.345  &   4.342  &   9.177  &   0.433  &   0.485  &   0.740  &   0.869  \\

-> Done!
```

#### Epoch 30:
```
-> Evaluating
 Mono evaluation - using median scaling
 Scaling ratios | med: 28.785 | std: 0.164

   abs_rel |   sq_rel |     rmse | rmse_log |       a1 |       a2 |       a3 |
&   0.343  &   4.414  &   9.246  &   0.429  &   0.487  &   0.745  &   0.872  \\

-> Done!
```
