def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq


print(word_frequency("Python is great and Python is fun"))
