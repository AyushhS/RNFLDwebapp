import streamlit as st
from PIL import Image, ImageDraw
from streamlit_image_coordinates import streamlit_image_coordinates
from processing import processing
import numpy as np
from math import sqrt
import cv2

def main():
    image = Image.open('iitbbs logo.png')
    st.image(image, width=256)
    st.title('Image and Video Processing Lab')
    st.title("RNFLDapp")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # print(uploaded_image)
        image = Image.open(uploaded_image)
        original_width, original_height = image.size
        image = image.resize((original_width//3, original_height//3), Image.Resampling.LANCZOS)
        # print(image.shape)
        cv2_image = np.array(image.convert('RGB'))
        cv2_image2 = cv2_image.copy()
        # print(cv2_image.shape)

        # Capture mouse click event
        selected_point = streamlit_image_coordinates(image)

        if selected_point:
            # st.write("Selected point coordinates:", selected_point)
            cx = selected_point['x']
            cy = selected_point['y']
            cv2_image = cv2.circle(cv2_image, (cx, cy), 1, (0, 255, 0), -1)
            selected_point2 = streamlit_image_coordinates(cv2_image)
            if selected_point2:
                rx = selected_point2['x']
                ry = selected_point2['y']
                cv2_image = cv2.circle(cv2_image, (cx, cy), int(3 * sqrt((cx - rx) * (cx - rx) + (cy - ry) * (cy - ry))), (0, 255, 0), 1)
                output_image = processing(cv2_image2, selected_point, selected_point2)
                # output_image = cv2.circle(output_image, (cx, cy), int(3 * sqrt((cx - rx) * (cx - rx) + (cy - ry) * (cy - ry))), (0, 255, 0), 1)
                # output_image = cv2.circle(output_image, (cx, cy), 1, (0, 255, 0), -1)
                st.image(output_image)
            # output_image = processing(cv2_image, selected_point)
            # st.image(output_image, title='Output')

if __name__ == "__main__":
    main()