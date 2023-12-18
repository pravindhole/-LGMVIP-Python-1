import streamlit as st
import nltk
from nltk.stem.lancaster import LancasterStemmer
import tensorflow as tf
import numpy as np
import json
import random


# Initialize Lancaster Stemmer for word stemming
stemmer = LancasterStemmer()

# Load intents from intents.json
with open('intents.json') as file:
    data = json.load(file)


# Preprocess the data to extract words, labels, and create training data
words = []
labels = []
x_docs = []
y_docs = []

# Iterate through intents data to gather words, labels, and create training data
for intent in data['intents']:
    for pattern in intent['patterns']:
        # Tokenize each pattern into words
        wrds = nltk.word_tokenize(pattern)
        # Extend words list with the tokenized words
        words.extend(wrds)
        # Append tokenized words and intent tag to x_docs and y_docs respectively
        x_docs.append(wrds)
        y_docs.append(intent['tag'])
        # Add unique intent tags to labels list
        if intent['tag'] not in labels:
            labels.append(intent['tag'])
            
# Stemming words, converting to lowercase, and removing duplicate elements
words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
words = sorted(list(set(words)))
labels = sorted(labels) 


# Load the trained model
model = tf.keras.models.load_model('chatbot_model.h5')



# Function to process user input and get the chatbot's response
def chatbot_response(message):
    # Perform bag-of-words transformation on the user input
    bag = bag_of_words(message, words)
    # Get the prediction from the model based on the bag-of-words
    results = model.predict(np.array([bag]))
    results_index = np.argmax(results)
    tag = labels[results_index]

    # Find the appropriate response based on the predicted tag
    for tg in data['intents']:
        if tg['tag'] == tag:
            responses = tg['responses']
            return random.choice(responses)
        
        
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for s_word in s_words:
        for i, w in enumerate(words):
            if w == s_word:
                bag[i] = 1

    return np.array(bag)



# Streamlit app
def main():
    st.title("Simple Chatbot")

    # Input text box for user input
    user_input = st.text_input("You:", "")

    # Button to submit user input
    if st.button("Send"):
        if user_input:
            # Get and display the chatbot's response
            bot_response = chatbot_response(user_input)
            st.text_area("Bot:", value=bot_response, height=100)

if __name__ == '__main__':
    main()



    
    
# Run the Streamlit app in your terminal by executing streamlit run chatbot_app.py