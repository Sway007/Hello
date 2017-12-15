## Assignment 1

1. **Text processing model**

    ```python
    def get_words_from_msg(message, stopwords=sw):
    
    msg_words = set(wordpunct_tokenize(message.lower()))
    msg_words = msg_words.difference(stopwords)
    msg_words = [w for w in msg_words 
            if re.search('[a-zA-Z]', w) and len(w) > 1]
    
    return msg_words
    ```
    get word tokens by utilizing `nltk.tokenize.wordpunct_tokenize`

2. **Classify/train model**  

    ```python
    def feature_extractor(message):
    
    msg_words = get_words_from_msg(message)
    features = dict.fromkeys(msg_words, True)

    return features

    def get_train_sets(raw_data_path):

        features_labes = []
        with open(raw_data_path, 'r') as f:
            csvf = csv.reader(f, delimiter=',')
            next(csvf)
            for msg, label in csvf:
                features = feature_extractor(msg)
                features_labes.append((features, label))

        return features_labes

    def get_naive_bayes_classifier(train_file='Data/assignment1_data.csv'):
        
        train_set = get_train_sets('Data/assignment1_data.csv')
        classifier = NaiveBayesClassifier.train(train_set)
    ```
    train a naive bayes classifier by utilizing `nltk.NaiveBayesClassifier`

3. **test model**

    as no test data set given, so I find a test data set from [website: http://slendermeans.org/ml4h-ch3.html], below show the test accuracy:

    ```jupyter notebook
    Test Spam accuracy: 99.21%
    Test Ham accuracy: 11.00%
    Test Hard Ham accuracy: 8.06%
    ```

## Assignment 2

    