import pandas as pd

positive_result = "positive"
negative_result = "negative"
neutral_result =  "neutral"

def load_dictionaries(file_path):
    """
    Load the dictionaries from the provided Excel file.

    Args:
    - file_path (str): Path to the Excel file containing the dictionaries.

    Returns:
    - tuple: (words, part_of_speech, entity_type) lists extracted from the file.
    """
    # Load the Excel file into a DataFrame
    dict_df = pd.read_excel(file_path)

    # Extracting dictionaries based on the provided columns
    words = dict_df['Word'].tolist()
    part_of_speech = dict_df['Part of Speech'].tolist()
    entity_type = dict_df['Entity Type'].tolist()

    return words, part_of_speech, entity_type


# Load dictionaries from the provided file
words, part_of_speech, entity_type = load_dictionaries("D:/Projects/Base/dict.1.xlsx")

#print(part_of_speech[:10])


def segment_sentence(sentence):
    """
    Segment the input sentence into an array of words.

    Args:
    - sentence (str): The input sentence.

    Returns:
    - list: A list of words.
    """
    return sentence.split()


# Test the function
sample_sentence = "Kechagi restoranni ovqatlari mazali va yaxshi edi, lekin puli juda qimmat edi"
#print(segment_sentence(sample_sentence))


def determine_word_sentiment(word, words, entity_type):
    """
    Determine the sentiment of a word based on the given dictionaries.

    Args:
    - word (str): The word to determine the sentiment for.
    - words (list): List of words from the dictionary.
    - entity_type (list): List of entity types corresponding to the words.

    Returns:
    - str: "positive", "negative", or "neutral".
    """
    if word in words:
        idx = words.index(word)

        if entity_type[idx] == "PositiveOpinion":
            return positive_result
        elif entity_type[idx] == "NegativeOpinion":
            return negative_result

    return neutral_result


# Test the function with a sample positive and negative word
determine_word_sentiment("mazali", words, entity_type), determine_word_sentiment("qimmmat", words, entity_type)

def morphological_analysis(word, words, entity_type):
   # Закрытый код
    return "unidentifiable"


# Test the function with a derived word
# morphological_analysis("mazza", words, entity_type)


def determine_sentence_sentiment(sentence, words, part_of_speech, entity_type):
    """
    Determine the sentiment of a sentence based on the given dictionaries.

    Args:
    - sentence (str): The sentence to determine the sentiment for.
    - words (list): List of words from the dictionary.
    - part_of_speech (list): List of part of speech tags corresponding to the words.
    - entity_type (list): List of entity types corresponding to the words.

    Returns:
    - str: "positive", "negative", or "neutral".
    """
    # Segment the sentence into words
    sentence_words = segment_sentence(sentence)

    positive_count = 0
    negative_count = 0

    # Analyze each word in the sentence
    for word in sentence_words:
        # First, check the word against the exception dictionary
        sentiment = determine_word_sentiment(word, words, entity_type)

        # If the word is neutral, conduct a morphological analysis
        if sentiment == neutral_result:
            sentiment = morphological_analysis(word, words, entity_type)

        # Update the sentiment counts
        if sentiment == positive_result:
            positive_count += 1
        elif sentiment == negative_result:
            negative_count += 1

    # Determine the overall sentiment of the sentence
    if positive_count > negative_count:
        return positive_result
    elif negative_count > positive_count:
        return negative_result
    else:
        return neutral_result


# Test the algorithm with the sample sentence
print(determine_sentence_sentiment(sample_sentence, words, part_of_speech, entity_type))

#segment_sentence_val = segment_sentence(sample_sentence)