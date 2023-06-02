# Image Thresholding Web App

[![**Open in Streamlit**](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]()

Image thresholding is a process in image processing that involves converting a grayscale or color image into a binary image. The binary image contains only two pixel values, typically black and white, based on a threshold value. The threshold value is a scalar value that is used to differentiate between the pixels that belong to the foreground of the image and those that belong to the background. There are two major approaches of thresholding: global and local thresholding. The first method involves selecting a single threshold value for the entire image based on the histogram of the pixel intensities. Whereas the latter involves selecting a threshold value for each pixel based on the local intensities of neighboring pixels.

Thresholding is commonly used in image segmentation, object detection, and feature extraction in computer vision and image processing applications.

#### Instead of coding every method you might try on the image, you can upload it to the web app and try it easily with the following methods:

- **Manual Thresholding**: you can manually select the threshold [0~255]
- **Global Thresholding**: 7 methods of global thresholding methods are supported in this web app
  - ISODATA Method (Ridler-Calvard Method)
  - Li's Iterative Minimum Cross Entropy Method
  - Mean Threshold Method
  - Minimum Method
  - Otsu's Threshold
  - Triangle Method
  - Yen's Method
- **Local Thresholding**: 5 methods of adaptive (local) thresholding methods are supported in this web app
  - Niblack Method
  - Sauvola Method
  - Gaussian
  - Mean
  - Median



https://github.com/OmarAlkousa/Image-Thresholding-Web-App/assets/64659365/a112bddd-0670-40de-a888-ef859e11f684

