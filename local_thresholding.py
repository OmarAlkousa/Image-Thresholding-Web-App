# Import the required Packages
import streamlit as st
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go
from skimage import filters

def apply_threshold(image):

    # --- Select the thresholding method --- #
    thresholding_method = st.selectbox(label='Select the Method of Local Thresholding',
                                       options=['Niblack Method',
                                                'Sauvola Method',
                                                'Gaussian',
                                                'Mean',
                                                'Median'],
                                       key='local_thresholding_method')
    
    # --- Apply the thresholding method --- #
    # Niblack Method
    if thresholding_method == 'Niblack Method':
        # Specify the window size
        window_size_niblack = st.number_input(label='Specify the Window Size',
                                              value=15,
                                              min_value=3,
                                              step=2,
                                              key='niblack_window_size')
        # Specify the parameter k
        k_niblack = st.number_input(label='Specify the Parameter k',
                                    value=0.2,
                                    step=0.1,
                                    key='k_niblack',
                                    help='k is a configurable parameter that weights the effect of standard deviation.')
        # Obtain the threshold mask
        threshold = filters.threshold_niblack(image=image, window_size=window_size_niblack, k=k_niblack)
    
    # Sauvola Method
    elif thresholding_method == 'Sauvola Method':
        # Specify the window size
        window_size_sauvola = st.number_input(label='Specify the Window Size',
                                              value=15,
                                              min_value=3,
                                              step=2,
                                              key='sauvola_window_size')
        # Specify the parameter k
        k_sauvola = st.number_input(label='Specify the Parameter k',
                                    value=0.2,
                                    step=0.1,
                                    key='k_sauvola',
                                    help='k is a configurable parameter that weights the effect of standard deviation.')
        # Specify the parameter R
        r_sauvola = st.number_input(label='Specify the Parameter R',
                                    value= 0.5*(image.max()-image.min()),
                                    step=0.1,
                                    key='r_sauvola',
                                    help='Value of R, the dynamic range of standard deviation. If None, set to the half of the image dtype range.')
        # Obtain the threshold mask
        threshold = filters.threshold_sauvola(image=image, window_size=window_size_sauvola, k=k_sauvola, r=r_sauvola)

    # Local Thresholding
    elif thresholding_method in ['Gaussian', 'Mean', 'Median']:
        # Specify the window size
        window_size_local = st.number_input(label='Specify the Window Size',
                                            value=3,
                                            min_value=3,
                                            step=2,
                                            key='local_window_size')
        # Specify the mode of handling array borders
        mode_local = st.selectbox(label='Select Mode',
                                  options=['reflect', 'constant', 'nearest', 'mirror', 'wrap'],
                                  help='Determine how the array borders are handled, where cval is the value when mode is equal to \'constant\'. Default is \'reflect\'.',
                                  key='local_mode')
        # Specify the value of the constant that will be subtracted from weighted mean of neighborhood
        offset_local = st.number_input(label='Constant subtracted from weighted mean of neighborhood',
                                       value=0,
                                       key='gaussian_offset')
        
        cval_constant = st.number_input(label='Value to fill past edges of input if mode is \'constant\'.',
                                        value=0,
                                        key='local_cval')

        threshold = filters.threshold_local(image=image,
                                            block_size=window_size_local,
                                            method=thresholding_method.lower(),
                                            mode=mode_local,
                                            offset=offset_local,
                                            cval=cval_constant)
    
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
    fig3.update_layout({'title': {'text': 'Binary Image',
                                  'font': {'size': 15, 'family': 'Times New Roman, bold'},
                                  'x': 0.5,
                                  'xanchor': 'center',
                                  'yanchor': 'top'},
                        'xaxis': {'title': None, 'showticklabels':False},
                        'yaxis': {'title': None, 'showticklabels':False},
                        'coloraxis_showscale':False})

    # Show the image plot
    column2.plotly_chart(fig3, theme="streamlit", use_container_width=True)
