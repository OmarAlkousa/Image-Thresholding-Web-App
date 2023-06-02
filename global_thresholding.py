# Import the required Packages
import streamlit as st
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from skimage import filters

def apply_threshold(image):

    # --- Thresholding type --- #
    thresholding_method = st.selectbox(label='Select the Method of Global Thresholding',
                                       options=['ISODATA Method (Ridler-Calvard Method)',
                                                'Li\'s Iterative Minimum Cross Entropy Method',
                                                'Mean Threshold Method',
                                                'Minimum Method',
                                                'Otsu\'s Threshold',
                                                'Triangle Method',
                                                'Yen\'s method'])

    # --- Apply Thresholding Type --- #
    # Obtain the threshold based on ISODATA method
    if thresholding_method == 'ISODATA Method (Ridler-Calvard Method)':
        threshold = filters.threshold_isodata(image=image)
    
    # Obtain the threshold based on Li's method
    elif thresholding_method == 'Li\'s Iterative Minimum Cross Entropy Method':
        threshold = filters.threshold_li(image=image)
    
    # Obtain the threshold based on Mean method
    elif thresholding_method == 'Mean Threshold Method':
        threshold = filters.threshold_mean(image=image)

    # Obtain the threshold based on Minimum method
    elif thresholding_method == 'Minimum Method':
        threshold = filters.threshold_minimum(image=image)

    # Obtain the threshold based on Otsu's method
    elif thresholding_method == 'Otsu\'s Threshold':
        threshold = filters.threshold_otsu(image=image)
    
    # Obtain the threshold based on Triangle method
    elif thresholding_method == 'Triangle Method':
        threshold = filters.threshold_triangle(image=image)
    
    # Obtain the threshold based on Yen's method
    elif thresholding_method == 'Yen\'s method':
        threshold = filters.threshold_yen(image=image)
    
    # Apply the thresholding method on the image
    binary_image = image >= threshold
    
    #####################
    # Display Histogram #
    #####################
    fig1 = make_subplots(1, 1)
    # Histogram
    fig1.add_trace(go.Histogram(x=image.ravel(), opacity=0.5), 1, 1)

    # Layout configuration
    fig1.update_layout({'title': {'text': 'Histogram',
                                  'font': {'size': 30, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': 'Intenstiy'},
                        'yaxis': {'title': 'Count'}})

    # Show the histogram plot
    st.plotly_chart(fig1, theme='streamlit', use_container_width=False)

    

    # Plot the original and the image after applying the threshold
    column1, column2 = st.columns(2)
    

    #################
    # Display Image #
    #################
    fig2 = px.imshow(img=image, color_continuous_scale='gray')

    # Layout configuration
    fig2.update_layout({'title': {'text': 'Original Image',
                                  'font': {'size': 15, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': None, 'showticklabels':False},
                        'yaxis': {'title': None, 'showticklabels':False},
                        'coloraxis_showscale':False})

    # Show the image plot
    column1.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    # Display Image after applying the specified threshold
    fig3 = px.imshow(img=binary_image, color_continuous_scale='gray')

    # Layout configuration
    fig3.update_layout({'title': {'text': f'Binary Image (Threshold={int(threshold)})',
                                  'font': {'size': 15, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': None, 'showticklabels':False},
                        'yaxis': {'title': None, 'showticklabels':False},
                        'coloraxis_showscale':False})

    # Show the image plot
    column2.plotly_chart(fig3, theme="streamlit", use_container_width=True)
