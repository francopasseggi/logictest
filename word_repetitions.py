# Find frequency of each word in a string in Python
# using dictionary.
 
def count_words(sentence):
    """Count the number of times each word occurs in words."""
    frequencies = {}  # dictionary of { <word>: <count> } pairs to return
    
    words = sentence.split()
    for word in words:
        count(word, frequencies)

    return frequencies

def count(word, frequencies):
    # Trim non alphanumeric characters
    word = word.strip(" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~").lower()

    # lowercase word
    word = word.lower()

    if word in frequencies:
        frequencies[word] += 1

    else:
        frequencies.update({word: 1})


if __name__ == "__main__":
    sentence = "Hi how are things? How are you? Are you a developer? I am also a developer"
    frequencies = count_words(sentence)

    for word in frequencies:
        print ("Frequency of ", word, end = " ")
        print (":", end = " ")
        print (frequencies[word], end = " ")
        print()