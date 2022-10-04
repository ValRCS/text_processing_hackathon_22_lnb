# text processing pipeline

# first we need to identify the text we want to process
# what language is it in?
# what is the text about?
# what is the text's genre?
# what is the text's purpose?
# what is the text's audience?
# what is the text's author's?

# next we need to identify the text's structure
# what is the text's structure?
# what is the text's form?

# next we need to clean the text
# what is the text's format?
# what is the text's encoding?
# what is the text's encoding scheme?
# what is the text's encoding scheme version?

# next we need to check the text for errors
# what is the text's encoding errors?
# what errors are in the text?
# what ocr errors are in the text?
# how do we fix the text's errors?

# to correct the text's errors we need to identify the text's errors
# this is done by comparing the text to a reference text
# we use regular expressions to identify the text's errors
# also we used dictionaries to identify the text's errors

# next we need to normalize the text
# what is the text's normalization?
# text normalization means to convert the text to a standard form
# it could be converting the text to lowercase

# next we need to tokenize the text
# what is the text's tokenization?
# tokenization means to split the text into tokens
# tokens are the smallest units of text
# tokens can be words, sentences, paragraphs, or characters

# next we need to lemmatize the text
# what is the text's lemmatization?
# lemmatization means to convert the text to its lemma
# lemmas are the base form of a word
# lemmas are the dictionary form of a word

# next we need to stem the text
# what is the text's stemming?
# stemming means to convert the text to its stem
# stems are the base form of a word

# next we need to remove stopwords from the text
# what is the text's stopwords?
# stopwords are words that are filtered out before or after processing of natural language data
# some examples of stopwords are the, is, at, which, and, and of in English

# next we need to remove punctuation from the text
# what is the text's punctuation?
# punctuation are characters that are filtered out before or after processing of natural language data
# some examples of punctuation are . , ! ? : ; " ' ( ) [ ] { } < > / \ | @ # $ % ^ & * - _ + = ~ ` in English

# next we need to remove numbers from the text
# what is the text's numbers?
# numbers are digits that are filtered out before or after processing of natural language data
# some examples of numbers are 0 1 2 3 4 5 6 7 8 9 in English

# next we need to remove whitespace from the text
# what is the text's whitespace?
# whitespace are spaces that are filtered out before or after processing of natural language data
# some examples of whitespace are \t \r \v \f \n in English

# next we need to embed the text
# what is the text's embedding?
# embedding means to convert the text to a vector of numbers
# embeddings are a representation of the semantic properties of a text
# embeddings are a representation of the syntactic properties of a text
# embeddings are a representation of the contextual properties of a text

# next we need to vectorize the text
# what is the text's vectorization?
# vectorization means to convert the text to a vector of numbers
# vectors are a representation of the semantic properties of a text
# vectors are a representation of the syntactic properties of a text
# vectors are a representation of the contextual properties of a text
# example of text vectorization is word2vec
# example of text vectorization is glove
# example of text vectorization is fasttext
# example of text vectorization is elmo
# example of text vectorization is bert
# example of text vectorization is gpt
# example of text vectorization is gpt2
# example of text vectorization is gpt3
# example of text vectorization is transformer

# next we need to convert the text to a bag of words
# what is the text's bag of words?
# bag of words means to convert the text to a vector of numbers
# bag of words are a representation of the semantic properties of a text
# bag of words are a representation of the syntactic properties of a text
# bag of words are a representation of the contextual properties of a text
# example of bag of words: the quick brown fox jumps over the lazy dog


# next we need to convert the text to a bag of ngrams
# what is the text's bag of ngrams?
# bag of ngrams means to convert the text to a vector of numbers
# bag of ngrams are a representation of the semantic properties of a text
# bag of ngrams are a representation of the syntactic properties of a text
# bag of ngrams are a representation of the contextual properties of a text
# example of ngrams are unigrams, bigrams, trigrams, quadgrams, and pentagrams
# example of bigram is the phrase "machine learning"

# next we need to convert the text to a bag of characters
# what is the text's bag of characters?
# bag of characters means to convert the text to a vector of numbers
# bag of characters are a representation of the semantic properties of a text
# bag of characters are a representation of the syntactic properties of a text
# bag of characters are a representation of the contextual properties of a text

# next we need to convert the text to a bag of phonemes
# what is the text's bag of phonemes?
# bag of phonemes means to convert the text to a vector of numbers
# bag of phonemes are a representation of the semantic properties of a text
# bag of phonemes are a representation of the syntactic properties of a text
# example of bag of phonemes are the phonemes of the word "hello" in English
# phone = h
# phone = eh
# phone = l
# phone = ow
# bag of phonemes are a representation of the contextual properties of a text

# next we need to convert the text to a bag of syllables
# what is the text's bag of syllables?
# bag of syllables means to convert the text to a vector of numbers
# bag of syllables are a representation of the semantic properties of a text
# bag of syllables are a representation of the syntactic properties of a text
# example of bag of syllables are the syllables of the word "hello" in English
# syllable = hel
# syllable = lo

# when we analyze text we can use the following methods
# we can perform topic modeling
# we can perform sentiment analysis
# we can perform named entity recognition
# we can perform part of speech tagging
# we can perform word sense disambiguation
# we can perform word sense induction

# topic modeling is a method for discovering the abstract "topics" that occur in a collection of documents
# popular topic modeling algorithms include Latent Dirichlet Allocation (LDA), Latent Semantic Analysis (LSA), and Non-negative Matrix Factorization (NMF)
# gensim is a popular python library for topic modeling
# gensim has a function called LdaModel that performs topic modeling using Latent Dirichlet Allocation (LDA)
# gensim has a function called LsiModel that performs topic modeling using Latent Semantic Analysis (LSA)
# for visualization of topic modeling results we can use pyLDAvis
# pyLDAvis is a popular python library for visualization of topic modeling results
# pyLDAvis has a function called prepare that performs visualization of topic modeling results

# sentiment analysis is a method for determining whether a piece of writing is positive, negative, or neutral
# popular sentiment analysis algorithms include VADER, TextBlob, and Stanford CoreNLP
# nltk is a popular python library for sentiment analysis
# nltk has a function called SentimentIntensityAnalyzer that performs sentiment analysis using VADER
# textblob is a popular python library for sentiment analysis
# textblob has a function called TextBlob that performs sentiment analysis using TextBlob
# stanfordcorenlp is a popular python library for sentiment analysis
# stanfordcorenlp has a function called StanfordCoreNLP that performs sentiment analysis using Stanford CoreNLP

# named entity recognition is a method for identifying named entities in text
# popular named entity recognition algorithms include spaCy, Stanford CoreNLP, and Flair
# spacy is a popular python library for named entity recognition
# spacy has a function called EntityRecognizer that performs named entity recognition using spaCy
# stanfordcorenlp is a popular python library for named entity recognition
# stanfordcorenlp has a function called StanfordCoreNLP that performs named entity recognition using Stanford CoreNLP
# for Latvian language we use tools provided by nlp.ailab.lv

# part of speech tagging is a method for identifying the part of speech of each word in a sentence
# popular part of speech tagging algorithms include spaCy, Stanford CoreNLP, and Flair
# spacy is a popular python library for part of speech tagging
# for Latviešu valoda we use tools provided by nlp.ailab.lv

# word sense disambiguation is a method for identifying the sense of each word in a sentence
# popular word sense disambiguation algorithms include WordNet, Lesk, and Lesk++
# nltk is a popular python library for word sense disambiguation
# nltk has a function called wordnet that performs word sense disambiguation using WordNet
# nltk has a function called lesk that performs word sense disambiguation using Lesk
# for Latvian language there is no simple way to perform word sense disambiguation

# word sense induction is a method for identifying the senses of words in a corpus
# popular word sense induction algorithms include WordNet, Lesk, and Lesk++
# nltk is a popular python library for word sense induction
# nltk has a function called wordnet that performs word sense induction using WordNet


# tools for text analysis
# we use Python
# we use NLTK
# we use spaCy
# we use TextBlob
# we use Gensim
# for visualization of topic modeling results we use pyLDAvis
# for Latvian language we use tools provided by nlp.ailab.lv
# for general purpose plotting we use plotly
# Jupyter Notebook is a popular tool for interactive computing
# Visual Studio Code provide a great environment for Python development
# Visual Studio Code provide a great environment for Jupyter Notebook development 
# alternative is to use web based Jupyter Notebook - https://jupyter.org/try
# Google Colab is a popular web based Jupyter Notebook - offers GPU and TPU support