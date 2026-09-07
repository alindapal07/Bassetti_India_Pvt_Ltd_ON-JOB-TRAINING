 # Text Statistics Analyzer
#
# Given:
#
# text = """
# Python is powerful. Python is simple. Python is popular.
# """
#
# Create functions to calculate:
#
# 1. Number of characters
# 2. Number of words
# 3. Number of sentences
# 4. Number of unique words
# 5. Most frequently occurring word
# 6. Longest word
# 7. Shortest word





# Text Statistics Analyzer

text = """
Python is powerful.
Python is simple.
Python is popular.
"""

# 1. Number of characters
def count_characters(text):
    return len(text)


# 2. Number of words
def count_words(text):
    words = text.split()
    return len(words)

# 3. Number of sentences
def count_sentences(text):
    sentences = text.split(".")
    count = 0
    for sentence in sentences:
        if sentence.strip():
            count += 1
    return count


# 4. Number of unique words
def count_unique_words(text):
    words = text.lower().split()
    unique_words = set()
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            unique_words.add(word)
    return len(unique_words)


# 5. Most frequently occurring word
def most_frequent_word(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    if not frequency:
        return None
    most_word = max(frequency, key=frequency.get)
    return most_word


# 6. Longest word
def longest_word(text):
    words = text.lower().split()
    clean_words = []
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            clean_words.append(word)
    if not clean_words:
        return None
    return max(clean_words, key=len)


# 7. Shortest word
def shortest_word(text):
    words = text.lower().split()
    clean_words = []
    for word in words:
        word = word.strip(".,!?;:")
        if word:
            clean_words.append(word)
    if not clean_words:
        return None
    return min(clean_words, key=len)
# Main Program

try:

    if not text.strip():
        raise ValueError("Text cannot be empty")

    print("----- TEXT STATISTICS -----")
    print("Number of characters :", count_characters(text))
    print("Number of words      :", count_words(text))
    print("Number of sentences  :", count_sentences(text))
    print("Unique words         :", count_unique_words(text))
    print("Most frequent word   :", most_frequent_word(text))
    print("Longest word         :", longest_word(text))
    print("Shortest word        :", shortest_word(text))

except ValueError as e:

    print("Error:", e)