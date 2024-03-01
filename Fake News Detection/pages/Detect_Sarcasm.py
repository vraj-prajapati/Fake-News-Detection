import streamlit as st
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
# import re
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# lemm = WordNetLemmatizer()
# stop_words = stopwords.words('english')
# stop_words.remove('not')

loaded_model = load_model('my_model.h5')


# Streamlit app title and description
st.title("Sarcasm Detection")
user_input = st.text_input("Enter your text:")
st.write("You entered:", user_input)
input_text = user_input
if(st.button('Detect')):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([input_text])
# Your tokenizer (fitted on training data)

# Single input string for prediction


# Tokenize and preprocess the input text
    input_sequence = tokenizer.texts_to_sequences([input_text])
    input_sequence = pad_sequences(input_sequence, maxlen=100)

# Make predictions using the loaded model
    predictions = loaded_model.predict(input_sequence)

# Assuming it's a binary classification task
# predicted_class = np.argmax(predictions[0])

# Print the predicted class
    print("Predicted Class:", predictions)
    if predictions>=0.95:
        print(user_input)
        st.subheader("Detection Output:")
        print("Sentence is not Sarcastic!!")
        st.text_area('',"This is a Correct NEWS!!")
    else:
       print(user_input)
       st.subheader("Detection Output:")
       print("Sentence is Sarcastic!!")
       st.text_area('',"This is a Fake NEWS!!")

    
# Run Colab file and capture output
    # output = subprocess.run(["python", "sgp_test.py"], capture_output=True, text=True)

# Display Colab output in Streamlit

        

