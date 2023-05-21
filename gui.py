# import streamlit as st

# # Read the file as bytes
# file_path = "1684673711/2023-04-02_12-03-36_UTC.mp4"
# with open(file_path, "rb") as file:
#     file_bytes = file.read()

# # Create a download button
# def download_button(file_bytes, file_name):
#     """
#     Function to create a download button.
#     """
#     download_link = f'<a href="data:application/octet-stream;base64,{file_bytes}" download="{file_name}">Download File</a>'
#     st.markdown(download_link, unsafe_allow_html=True)

# # Display the download button
# download_button(file_bytes, "2023-04-02_12-03-36_UTC.mp4")


import streamlit as st

# Read the file as bytes
file_path =  "1684673711/2023-04-02_12-03-36_UTC.mp4"
with open(file_path, "rb") as file:
    file_bytes = file.read()

# Display the download button
st.download_button("Download File", file_bytes, file_name="2023-04-02_12-03-36_UTC.mp4")
