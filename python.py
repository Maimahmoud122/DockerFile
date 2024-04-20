import nltk
from nltk.corpus import stopwords
from collections import Counter

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to remove stop words and count word frequency
def process_text(file_path):
    # Load the list of stop words
    stop_words = set(stopwords.words('english'))
    
    # Read the contents of the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Tokenize the text and remove stop words
    words = [word for word in nltk.word_tokenize(text.lower()) if word.isalpha() and word not in stop_words]
    
    # Count the frequency of each word
    word_freq = Counter(words)
    
    # Display the frequency count
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
    
# Call the function with the path to your text file
process_text('random_paragraphs.txt')