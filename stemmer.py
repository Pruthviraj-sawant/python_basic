from nltk.stem import PorterStemmer , WordNetLemmatizer
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')  
# Create a stemmer object
stemmer = PorterStemmer()

# Example words
words = ["running", "runner", "ran", "easily", "fairly"]

# Applying stemming
stemmed_words = [stemmer.stem(word) for word in words]
print(stemmed_words)




# Create a lemmatizer object
lemmatizer = WordNetLemmatizer()

# Example words
words = ["running", "runner", "ran", "easily", "fairly"]

# Applying lemmatization
lemmatized_words = [lemmatizer.lemmatize(word, pos="v") for word in words]  # 'v' stands for verb
print(lemmatized_words)
