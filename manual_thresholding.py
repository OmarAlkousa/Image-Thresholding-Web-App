# Import the required Packages
import streamlit as st
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

def apply_threshold(image):

    # Specify the threshold
    threshold = st.slider(label='Specify the Threshold [0 ~ 255]',
                          min_value=0,
                          max_value=255,
                          value=round(image.mean()))

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
    
    

    # Plot a vertical line that represents the specified threshold
    fig1.add_vline(x=threshold, line_width=1, line_color='red')

    # Show the histogram plot
    st.plotly_chart(fig1, theme='streamlit', use_container_width=False)

    # Apply the threshold on the image
    binary_image = image >= threshold

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