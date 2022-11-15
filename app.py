import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
from PIL import Image

st.title('KnoB4UGo!')

# text_input edit box
title = st.text_input('Restaurant', 'Chick-fil-a')
st.write('Please check into the restaurant!', title)

# button
if st.button('Join the line'):
    st.header('**Original input data**')
    st.write("load_data")
    st.header('**Calculated molecular descriptors**')
else:
    st.info('Upload input data in the sidebar to start!')

# checkbox
st.checkbox("Disable text input widget", key="disabled")
st.session_state.disabled

#radio button
st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
)
st.session_state.visibility

#Scatter plot 
x1 = [1,2,3,4,5]
x2 = [10,22,13,34,25]
y= [100,200,50,60,80]
fig = plt.figure()
plt.scatter(x1, x2,
        c=y, alpha=0.8,
        cmap='viridis')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

#plt.show()
st.pyplot(fig)

#sidebar
dataset_name = st.sidebar.selectbox(
    'Select Dataset',
    ('Iris', 'Breast Cancer', 'Wine')
)
st.write(f"## {dataset_name} Dataset")

# Show image
image = Image.open('logo.png')
st.image(image, use_column_width=True)
