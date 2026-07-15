# Spam-Detector
A Machine Learning-based web application that classifies emails and SMS messages as Spam or Ham (Not Spam) using Natural Language Processing (NLP) techniques. Built with Python, Scikit-learn, and Streamlit, the application provides a simple, interactive interface for real-time spam detection.
# 🚀 Live Demo

Live Application: https://yuvraj-ml-spam-detector-spam-kef1p4.streamlit.app/

# 📖 Project Overview

Spam messages are one of the most common forms of unwanted digital communication. They often contain advertisements, phishing attempts, or fraudulent content that can compromise user security and productivity.

This project demonstrates how Machine Learning and Natural Language Processing (NLP) can be used to automatically classify a message as Spam or Ham. The application processes the user's input, converts the text into numerical features using the TF-IDF Vectorizer, and predicts the result with a trained Logistic Regression model.

The project is designed to be beginner-friendly while showcasing the complete workflow of building and deploying a text classification model.

# 🧠 How the Model Works

The application follows a standard Natural Language Processing pipeline:

Step 1: User Input

The user enters an email or SMS message into the application.

Step 2: Text Preprocessing

The input text is cleaned and prepared by:

Converting text to lowercase
Removing punctuation and unnecessary characters
Removing stop words
Tokenizing the text

Step 3: Feature Extraction

The cleaned text is transformed into numerical vectors using the TF-IDF (Term Frequency–Inverse Document Frequency) Vectorizer, allowing the machine learning model to interpret textual data.

Step 4: Prediction

The trained Logistic Regression model analyzes the generated feature vectors and predicts whether the message belongs to the 0 means Not Spam or 1 means Spam.

Step 5: Result Display

The prediction is displayed instantly on the Streamlit interface, providing a simple and user-friendly experience.

# 🛠️ Technology Stack

Python - Core programming language
Streamlit	- Web application framework
Scikit-learn - Machine learning model development
Pandas -	Data manipulation and preprocessing
NumPy	- Numerical computations
TF-IDF - Vectorizer	Text feature extraction
Pickle	- Model serialization and loading

# 📂 Project Structure
spam-detector/

├── spam_app.py              # Streamlit application

├──spam_model_train.pkl                # Trained Logistic Regression model

├── tfidf.pkl           # TF-IDF Vectorizer

├── requirements.txt         # Project dependencies

├── README.md                # Project documentation

├── email_dataset.xlsx           # Training dataset

# ⚙️ Installation Guide

Follow these steps to run the project on your local machine.

**Clone the Repository** 
git clone: https://github.com/yuvraj-ml/spam-detector.git
**Navigate to the Project Directory**
cd spam-detector
**Install the Required Dependencies**
pip install -r requirements.txt
**Launch the Streamlit Application**
streamlit run spam_app.py

Once the server starts, open the provided local URL in your browser to access the application.

# 💻 How to Use

Using the application is straightforward:

1.Launch the Streamlit application.
2.Enter an email or SMS message into the input field.
3.Click the Predict button.
4.The application preprocesses the text and sends it to the trained model.
5.Within seconds, the application displays whether the message is Spam or Not Spam.

# 👨‍💻 Author

Yuvraj

GitHub: https://github.com/yuvraj-ml

Linkdin: www.linkedin.com/in/yuvraj-k-820836416
