# import streamlit as st
# import boto3
# from botocore.exceptions import NoCredentialsError

# # Access AWS credentials from Streamlit secrets
# AWS_ACCESS_KEY = st.secrets["AWS_ACCESS_KEY"]
# AWS_SECRET_KEY = st.secrets["AWS_SECRET_KEY"]
# S3_BUCKET_NAME = st.secrets["S3_BUCKET_NAME"]

# # Initialize S3 client
# s3 = boto3.client('s3',
#                   aws_access_key_id=AWS_ACCESS_KEY,
#                   aws_secret_access_key=AWS_SECRET_KEY)



# st.title('File Upload to S3')

# # File uploader widget
# uploaded_file = st.file_uploader("Choose a file")

# # Submit button
# if st.button('Submit'):
#     if uploaded_file is not None:
#         try:
#             # Upload the file to S3
#             s3.upload_fileobj(uploaded_file, S3_BUCKET_NAME, uploaded_file.name)
#             st.success(f"File '{uploaded_file.name}' uploaded successfully to S3 bucket '{S3_BUCKET_NAME}'.")
#         except NoCredentialsError:
#             st.error("AWS credentials not found. Please configure them properly.")
#     else:
#         st.warning("No file uploaded. Please upload a file first.")



import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError

# Access AWS credentials from Streamlit secrets
AWS_ACCESS_KEY = st.secrets["AWS_ACCESS_KEY"]
AWS_SECRET_KEY = st.secrets["AWS_SECRET_KEY"]
S3_BUCKET_NAME = st.secrets["S3_BUCKET_NAME"]

# Initialize S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY)

# Image URLs
image_url_left = "https://media.licdn.com/dms/image/D4E12AQF-BvR3QRs9gw/article-cover_image-shrink_720_1280/0/1656343174665?e=2147483647&v=beta&t=T3dP2OU7Tbws3Ap79YdaIIYX1st1UqSW1TeKVdH6L48"
image_url_center = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkM0Emsq4_Gz6ZqhBstMmUDwDeogsSd0zcQQ&s"
image_url_right = "https://www.uptoplay.net/imagescropped/diemsnoticesicon128.jpg.webp"

# Layout using Streamlit columns
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the proportions of the columns

# Display the left image in the first column with circular styling
with col1:
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{image_url_left}" alt="Left Image" style="width:150px; height:150px; border-radius: 50%;">
    </div>
    """, unsafe_allow_html=True)

# Display the center collab image in the second column
with col2:
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{image_url_center}" alt="Collab Logo" style="width:150px; height:150px; border-radius: 50%;">
    </div>
    """, unsafe_allow_html=True)

    # Attractive heading for B.Tech CA-II Submission
    st.title("🎓 **DIEMS B.Tech CA-II Submission** 🎓")
    st.write("Enhancing Knowledge Through Collaboration")

# Display the right image in the third column with circular styling
with col3:
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center;">
        <img src="{image_url_right}" alt="DIEMS Logo" style="width:150px; height:150px; border-radius: 50%;">
    </div>
    """, unsafe_allow_html=True)

# File upload section

st.title('File Upload to S3')

# File uploader widget
uploaded_file = st.file_uploader("Choose a file")

# Submit button
if st.button('Submit'):
    if uploaded_file is not None:
        try:
            # Upload the file to S3
            s3.upload_fileobj(uploaded_file, S3_BUCKET_NAME, uploaded_file.name)
            st.success(f"File '{uploaded_file.name}' uploaded successfully to S3 bucket '{S3_BUCKET_NAME}'.")
        except NoCredentialsError:
            st.error("AWS credentials not found. Please configure them properly.")
    else:
        st.warning("No file uploaded. Please upload a file first.")
