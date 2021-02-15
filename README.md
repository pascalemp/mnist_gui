# Visual MNIST Classifier using PyQT5

***Note:** This network has already been trained. This is merely a small Python app to display the respective classification of a given input image from the MNIST dataset.*  

- *The entire MNIST dataset is available at http://yann.lecun.com/exdb/mnist/ if you wish to train a network of your own.*

The full MNIST database consists solely of handwritten digits. It has ```60,000``` training
samples, and ```10,000``` test samples, with each sample represented by ```28x28``` pixels. Each pixel contains a
value within the range ```[0,255]``` which represents it's grayscale value.

## Installation
There are a few package pre-requisites and I've enlisted these in the ```requirements.txt``` file in this repository. 

1. ```git clone``` this repo into a local directory.
2. I recommend creating a virtual enviroment in order to install these packages in a local environment, but you're welcome to install them globally if you like. 
3. Install the pre-requisite packages using ```pip3 install -r requirements.txt```
4. Done!

## Usage
I have included a small subset of ***64 test images*** in the ```data/test_samples``` directory. These are sampled from the larger test set in order for you use the GUI classifier. The code is very rudimentary and works solely on the MNIST image databsed - the aim for this project was just to become familiar with PyQT syntax rather than produce a flawless algorithm!  

Run ```pyqt_window.py``` and select one of the images in the ```data/test_samples``` directory and the GUI will display the network classification output for the given digit.