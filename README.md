# NLP-Artificial-Intelligence-
This script demonstrates various Natural Language Processing (NLP) techniques using Python libraries such as SpaCy and NLTK. It covers fundamental tasks such as tokenization, dependency parsing, stopwords removal, stemming, lemmatization, and n-grams generation.
### Key Features:
1. **Tokenization:**
   - Splits text into tokens (words or sentences).
   - Example: Using NLTK's `sent_tokenize` for sentence tokenization.

2. **Dependency Parsing:**
   - Analyzes grammatical structure and relationships between words in a sentence.
   - Visualized using SpaCy's `displacy.render()`.

3. **Stopwords Removal:**
   - Filters out common stopwords (e.g., 'the', 'is', 'and') from text.
   - Utilizes NLTK's `stopwords.words('english')`.

4. **Stemming vs. Lemmatization:**
   - Reduces words to their base or root form.
   - Demonstrates NLTK's `PorterStemmer` for stemming and SpaCy's `lemma_` attribute for lemmatization.

5. **N-grams Generation:**
   - Extracts contiguous sequences of n items (words or characters) from text.
   - Implemented using NLTK's `ngrams` function.

6. **Named Entity Recognition (NER) and Visualization:**
   - Identifies named entities (e.g., persons, organizations) in text.
   - Visualized using SpaCy's `displacy.render()` with entity annotations.

### Usage
1. Ensure you have Python installed along with the required libraries: SpaCy and NLTK.
2. Run the provided script to see demonstrations of various NLP techniques on sample text.

### Example
```python
import spacy
from nltk import sent_tokenize, word_tokenize
from nltk.util import ngrams
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nlp=spacy.load(" en_core_web_sm")
 Doc2
