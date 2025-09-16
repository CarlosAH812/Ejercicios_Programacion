words = []

for i in range(5):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

long_words = [w for w in words if len(w) > 4]

print("Words with more than 4 letters:", long_words)