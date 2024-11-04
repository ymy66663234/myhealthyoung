from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
 
load_dotenv()
 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
 
st.set_page_config(page_title="Nutrition Expert",page_icon="🗣️")
 
st.header("Nutrition Expert Web Application")
 
question = st.text_input("Write your question here...")
 
uploaded_image = st.file_uploader("Choose an Image..",type=["jpg","png","jpeg"])
 
image = ""
 
submit = st.button("Submit")
 
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image,caption="Uploaded Image",use_column_width=True)

input_prompt = """You are a nutrition expert where you need to see the food items present
in the input image and answer the question being asked , if the user don't ask any question
then calculate the total calories, also provide the details of each food items with
calorie intake in following format:
 
1. Item 1 - No of calories
2. Item 2 - No of calories
-------
-------
 
Please don't answer any question which is not related to food or the uploaded image, simply
say "I am not capable to answer this"
"""
 
if submit:
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([input_prompt,image,question])
    st.write(response.text)
