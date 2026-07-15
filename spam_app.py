import streamlit as st
import joblib 
import re

# load model and vectorizer with cleaning
vectorizer = joblib.load('tfidf.pkl')
model = joblib.load('spam_model_train.pkl')

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📱", layout="centered")

# Title
st.title('SPAM E-MAILS DETECTOR🚨')
st.divider()

# Subheading
st.subheader("📩 Detect Spam Messages instantly using AI Model")

# Description
st.markdown("This application leverages Machine Learning and Natural Language Processing (NLP) techniques such as TF-IDF vectorization to classify SMS messages as Spam or Ham. It provides real-time predictions with high accuracy for better message filtering.")
st.divider()

# Input box
message = st.text_area("✍️ Enter your message here:")

# clean text
import re
def clean(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|https\S+', ' URL ', text)
    text = re.sub(r'\S+@\S+', ' EMAIL ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

if st.button('Predict',type='primary'):
    if message == "":
        st.warning('Please enter a message someone first')
    else:
       
        clean_message = clean(message)
        # vectorizer
        vec = vectorizer.transform([clean_message])
        #prediction
        predict = model.predict(vec)[0]
        
        if predict == 1:
            st.error(' Your message is spam')
        else :
            st.success('Your message is Not Spam')
       