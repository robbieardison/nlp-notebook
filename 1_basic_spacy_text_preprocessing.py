# !pip install spacy
# !python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("OMG I CAN'T believe this!!! 😤🔥🔥 #fail http://bit.ly/blah")
clean_tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
print("spaCy Cleaned Text:")
print(clean_tokens)