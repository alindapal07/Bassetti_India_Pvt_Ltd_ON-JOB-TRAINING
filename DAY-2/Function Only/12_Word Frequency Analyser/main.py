# Word Frequency Analyzer
#
# Given:
#
# text = """
# Python is easy. Python is powerful. Python is widely used.
# """
#
# Return:
#
# {
#     "python": 3,
#     "is": 3,
#     "easy": 1,
#     "powerful": 1,
#     "widely": 1,
#     "used": 1
# }
#
# Create functions:
# get_word_frequency()
# get_most_common_word()
# get_unique_words()
#
# Handle:
# - Empty input
# - Different capitalization
# - Punctuation




text = """
Python is easy. Python is powerful. Python is widely used.
"""

def get_word_frequency(text):
    if not text.strip():
        raise ValueError("Text cannot be empty")

    words = text.lower().split()
    frequency = {}

    for word in words:
        word = word.strip(".,!?;:")

        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency

def get_most_common_word(frequency):
    if not frequency:
        raise ValueError("No words available")

    return max(frequency, key=frequency.get)

def get_unique_words(frequency):
    return list(frequency.keys())

try:
    frequency = get_word_frequency(text)

    print("Word Frequency:", frequency)
    print("Most Common Word:", get_most_common_word(frequency))
    print("Unique Words:", get_unique_words(frequency))

except ValueError as e:
    print("Error:", e)