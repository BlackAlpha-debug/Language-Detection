# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import re
import numpy as np

app = Flask(__name__)

# Load your trained model and vectorizer
model = joblib.load('models/language_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# Preprocessing function (same as your training code)
def preprocess_text(text):
    Upper_Case_Lang = ['German', 'Arabic', 'Hindi', 'Urdu']
    text = re.sub(r'http[s]?://\S+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.split()
    text = ' '.join(text)
    if text not in Upper_Case_Lang:
        text = text.lower()
    return text

def predict_language(text):
    # Preprocess the text
    processed_text = preprocess_text(text)
    
    # Transform using the trained vectorizer
    text_vector = vectorizer.transform([processed_text])
    
    # Get prediction and probability
    prediction = model.predict(text_vector)[0]
    probabilities = model.predict_proba(text_vector)[0]
    confidence = max(probabilities)
    
    return {
        'language': prediction,
        'confidence': float(confidence)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text.strip():
            return jsonify({'error': 'No text provided'}), 400
        
        result = predict_language(text)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)