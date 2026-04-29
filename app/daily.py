

sentence = input("Give me your words: ")
lower_words = sentence.lower()
words = lower_words.split()
count = {}

for w in words:
    count[w] = count.get(w, 0) + 1
    
for key, value in count.items():
    print(f"{key}: {value}")

    
    


