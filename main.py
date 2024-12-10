from api_key import api_key
from system_prompt import system_prompt
import streamlit as st
from pathlib import Path
import google.generativeai as genai
import os



# set the page configuration
st.set_page_config(page_title="Vital Image Analytics",page_icon="🏥")

#set the logo
#st.image("indir.jpg",width=50)


#set the Title
st.title("🏥🩺Vital Image Analytics🩺🏥")


#set the subtitle
st.subheader("Revolutionizing healthcare through advanced visual data analysis and insights.",divider="red")


#upload file
uploaded_file = st.file_uploader("Upload a Medical Image for Analysis",type=["png","jpg","jpeg"])


#submit_button
submit_button = st.button("Generate to Analysis ")



#defining model
os.environ["GOOGLE_API_KEY"] = api_key

genai.configure(
    api_key=os.environ["GOOGLE_API_KEY"]
)

generation_config = {
    "temperature" : 0.8,
    "top_k" : 0.94,
    "top_k" : 40,
    "max_output_tokens" : 8192,
    "response_mime_type" : "text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)


#generate content
if submit_button:
    if uploaded_file is not None:  
        image_data = uploaded_file.getvalue()
        
        image_parts = [{
            "mime_type": "image/jpeg",
            "data": image_data
        }]

        prompt_parts = [
            image_parts[0],
            system_prompt
        ]
        st.image(image_data)
        st.subheader("Uploaded Medical Image")
        st.title("HERE IS THE ANALYSIS",)
        response = model.generate_content(prompt_parts)
        st.write(response.text)  # 
    else:
        st.error("Please Upload a Image File.")  
