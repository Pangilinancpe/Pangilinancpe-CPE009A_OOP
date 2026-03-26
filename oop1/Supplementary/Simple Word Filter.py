 
def word_filter(sentence, bad_words):
    words = sentence.split()
    result = []
 
    for word in words:
        if word.lower() in [b.lower() for b in bad_words]:
            result.append("*" * len(word))
        else:
            result.append(word)
 
    return " ".join(result)
 
 
# Test
sentence = "This is a stupid and dumb sentence you idiot"
bad_words = ["stupid", "dumb", "idiot"]
 
filtered = word_filter(sentence, bad_words)
print("Original :", sentence)
print("Filtered :", filtered)
 