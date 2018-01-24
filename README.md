# Image Resizer

This command line script makes it easy to resize images. You can change width or height(or both) of your image, set the resized image scale, which will be saved to a custom folder(or default original image folder). If you break image proportion script will display a warning message.

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

# Quickstart

Programm takes arguments: 
```bash
optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
  -o OUTPUT, --output OUTPUT
  -w WIDTH, --width WIDTH
  -he HEIGHT, --height HEIGHT
  -s SCALE, --scale SCALE
```

which you can explore symply by typing the following in command line:
```bash
$ python image_resize.py -h
```

Example of programm output:
```bash
$ python image_resize.py -i C:\devman\map.png -w 1500 -he 1200
Result image proportion will be changed
```
After that you will find your resized image here: C:\devman\map__1500x1200.png

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
