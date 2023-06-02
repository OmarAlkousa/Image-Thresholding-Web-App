# License: MIT
# Author: Omar Alkousa
# Email: omar.ok1998@gmail.com
# LinkedIn: linkedin.com/in/omar-alkousa/
# Medium: medium.com/@omar.ok1998


# Import the required package
import streamlit as st
from skimage.io import imread
import global_thresholding
import local_thresholding
import manual_thresholding

#################
# Documentation #
#################
# Set a title of the app
st.markdown("<h1 style='text-align: center; color: grey;'>Thresholding Medical Images",
            unsafe_allow_html=True)
# Explanation of the web app
st.markdown('''
This web app is to represent how you can use streamlit to import local Grayscale images and show its histogram to specify the threshold you want to apply.
All you have to do is to upload the image file.
            ''')

# Fast Example of the app
st.markdown("### Import the image file")
st.markdown("If you want a fast try of this app and you don't have any image file, you can download an example file that is in the same \
            [**GitHub repository**](https://github.com/OmarAlkousa/Image-Thresholding-Web-App.git) of the app.")


###################
# Upload an image #
###################
uploaded_file = st.file_uploader(label="Import the file of the image")

# If the file is uploaded
if uploaded_file is not None:

    # Caching the data for faster implementation
    @st.cache_data
    def load_image():
        img = imread(fname=uploaded_file.name, as_gray=True)
        return img

    # Load the Data
    img = load_image()

    # Select the type of thresholding #
    thresholding_method = st.selectbox(label='How do you want to apply thresholding?',
                                       options=['Manual Thresholding',
                                                'Local Thresholding',
                                                'Global Thresholding'])
    
    if thresholding_method == 'Global Thresholding':
        global_thresholding.apply_threshold(img)
    
    elif thresholding_method == 'Local Thresholding':
        local_thresholding.apply_threshold(img)
    
    elif thresholding_method == 'Manual Thresholding':
        manual_thresholding.apply_threshold(img)
    
    
