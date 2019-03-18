PSNR-Calculator-for-Images
===
This program written in python can calculate Peak Signal-to-noise-ratio between two images.

## Features
- Add noise to an image by performing color transfer and recovery between two images
- Calculate PSNR between two images

## Details
First let us add noise to an image by performing `color transfer and recovery` between two images. Of course you can just jump this step if already having your own images.
Last week I had already implemented `color transfer` in [another repository](https://github.com/chia56028/Color-Transfer-between-Images). After understanding the principle of color transfer, we can perform `color recovery` by changing the formula.

<img src="https://i.imgur.com/iUAMPwo.png" width="400" height="180">

After completing the above steps, it's time to calculate PSNR between two images.
Just split a color image into its 3 RGB channels then calculate their `MSE` and use it to calculate `PSNR`.

<img src="https://i.imgur.com/dUUCwOb.png" width="350" height="225">

MAX<sub>I</sub> is maximum value of pixel, actually it will be 255. 


## Install Packages
```bash
pip install numpy
pip install opencv-python
pip install python-csv
```
If you want to create `EXE file` after programming, also install this:
```bash
pip install pyinstaller
```

## Run the program
Put 6 source pictures inside `source` folder and 6 target pictures inside the `target` folder, then execute the code:
```bash
python color_transfer_and recovery.py
```
After that, your can find 6 result images inside `result` folder and 6 recovery images inside `result` folder.

Then, execute the command below to get PSNR between `source` images and `recovery` images:
```
python calculate_PSNR.py
```

Execute following instruction to create `EXE file` of this program:
```bash
pyinstaller -F color_transfer.py
```

### Example
Source / Recovery
<p float="left">
    <img src="https://i.imgur.com/TFoCa6o.png" width="200" height="300">
    <img src="https://i.imgur.com/zMVJLA0.png" width="200" height="300">
</p>

The PSNR between these two images is 43.71 :)
