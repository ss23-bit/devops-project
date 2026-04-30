import string

sentence = input("Say some thing: ").lower()

sentence = sentence.translate(str.maketrans("", "", string.punctuation))

count = {}
words = sentence.split()
if not words:
    print("No valid words found")

for w in words:
    count[w] = count.get(w, 0) + 1

max_word = None
max_count = 0

for word, freq in count.items():
    if freq > max_count:
        max_word = word
        max_count = freq

print(f"{max_word}: {max_count}")


    
    


