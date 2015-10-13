sentence = "the quick brown fox jumps over the lazy dag"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))

print word_lengths

word_lengths = [len(word) for word in words if word != "the"]
print word_lengths
