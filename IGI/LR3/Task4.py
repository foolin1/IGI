# main: Finding the words with the minimum length, the words before the comma, and the longest word ending with 'y' in a string
# Version: 1.0
# Author: Volodin I.
# Date: 01.05.2024

import string

def get_min_length_words(text):
    """
    Returns a list of words with the minimum length in the given text.
    """
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    min_length = min(len(word) for word in words)
    return [word for word in words if len(word) == min_length]

def get_words_before_comma(text):
    """
    Returns a list of words that precede a comma in the given text.
    """
    words = text.split()
    return [words[i][:-1] for i, word in enumerate(words) if word.endswith(",")]

def get_longest_word_ending_with_y(text):
    """
    Returns the longest word ending with 'y' in the given text. If no such word exists, returns None.
    """
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    words_ending_with_y = [word for word in words if word.endswith('y')]
    return max(words_ending_with_y, key=len) if words_ending_with_y else None

def main():
    """
    Executes the main.
    """
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    min_length_words = get_min_length_words(text)
    print(f"Words with minimum length ({len(min_length_words[0])}): {min_length_words}")
    words_before_comma = get_words_before_comma(text)
    print(f"Words before comma: {words_before_comma}")
    longest_word_ending_with_y = get_longest_word_ending_with_y(text)
    print(f"Longest word ending with 'y': {longest_word_ending_with_y}")