# NLP Text Preprocessing in Python

# Step 0: Install necessary libraries
# !pip install nltk
# !python -m nltk.downloader all

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Sample input text (feel free to use a tweet or real comment)
text = "OMG I CAN'T believe this!!! 😤🔥🔥 #fail http://bit.ly/blah"

print("Original Text:")
print(text)

# Step 1: Lowercasing
text = text.lower()
print("\nLowercased Text:")
print(text)

# Step 2: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))
print("\nNo Punctuation:")
print(text)

# Step 3: Tokenization
tokens = word_tokenize(text)
print("\nTokens:")
print(tokens)

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]
print("\nWithout Stopwords:")
print(filtered_tokens)

# Step 5: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
print("\nLemmatized Tokens:")
print(lemmatized_tokens)

# Optional: Rejoin tokens into cleaned text
cleaned_text = ' '.join(lemmatized_tokens)
print("\nFinal Cleaned Text:")
print(cleaned_text)
