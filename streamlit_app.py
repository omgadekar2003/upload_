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
