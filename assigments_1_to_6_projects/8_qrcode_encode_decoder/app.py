import streamlit as st
import qrcode
from PIL import Image
import io
import cv2
import numpy as np

# Set page configuration
st.set_page_config(page_title="QR Code Encoder/Decoder", page_icon="📱")

st.title("QR Code Encoder/Decoder")
st.write("Generate or decode QR codes easily!")

# Create tabs for encode and decode functionality
tab1, tab2 = st.tabs(["Generate QR Code", "Decode QR Code"])

# QR Code Generator Tab
with tab1:
    st.header("Generate QR Code")
    
    # Get user input
    qr_text = st.text_area("Enter text or URL to encode:", height=100)
    
    # QR code customization options
    st.subheader("Customize QR Code")
    col1, col2 = st.columns(2)
    
    with col1:
        qr_size = st.slider("QR Code Size", min_value=1, max_value=10, value=5)
        qr_border = st.slider("Border Size", min_value=0, max_value=5, value=4)
    
    with col2:
        qr_color = st.color_picker("QR Code Color", "#000000")
        bg_color = st.color_picker("Background Color", "#FFFFFF")
    
    # Generate QR code button
    if st.button("Generate QR Code") and qr_text:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=qr_size,
            border=qr_border,
        )
        
        # Add data to QR code
        qr.add_data(qr_text)
        qr.make(fit=True)
        
        # Create an image from the QR code
        qr_img = qr.make_image(fill_color=qr_color, back_color=bg_color)
        
        # Convert PIL image to bytes
        img_byte_arr = io.BytesIO()
        qr_img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        # Display QR code
        st.image(img_byte_arr, caption="Generated QR Code")
        
        # Download button
        st.download_button(
            label="Download QR Code",
            data=img_byte_arr,
            file_name="qrcode.png",
            mime="image/png"
        )

# QR Code Decoder Tab
with tab2:
    st.header("Decode QR Code")
    st.write("Upload a QR code image to decode its contents.")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a QR code image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        
        # Display the uploaded image
        st.image(image, caption="Uploaded QR Code", width=300)
        
        # Convert PIL Image to numpy array for OpenCV processing
        img_array = np.array(image)
        
        # Convert RGB to BGR (OpenCV format)
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        # Decode the QR code using OpenCV's QR code detector
        try:
            # Initialize QR Code detector
            qr_detector = cv2.QRCodeDetector()
            
            # Detect and decode
            data, bbox, _ = qr_detector.detectAndDecode(img_array)
            
            if data:
                st.success("QR Code successfully decoded!")
                
                # Display decoded data
                st.subheader("Decoded Content:")
                st.code(data)
                
                # If it's a URL, provide a link
                if data.startswith(('http://', 'https://')):
                    st.markdown(f"[Open URL]({data})")
            else:
                st.error("No QR code found in the image or unable to decode.")
        except Exception as e:
            st.error(f"Error decoding QR code: {e}")

# Add instructions at the bottom
st.markdown("---")
st.markdown("""
### How to use:
1. **Generate QR Code**: Enter text or a URL, customize the appearance, and click "Generate QR Code"
2. **Decode QR Code**: Upload an image containing a QR code to extract its contents
""")

# Add information about QR codes
st.sidebar.title("About QR Codes")
st.sidebar.info("""
**QR Code** (Quick Response Code) is a type of matrix barcode invented in 1994.

**Common uses:**
- Website URLs
- Contact information
- Wi-Fi network credentials
- Payment information
- Product tracking
- Event tickets
""")
