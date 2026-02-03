sentence = input("Enter a sentence: ")

print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")

count_a = sentence.lower().count('a')
print(f"The letter 'a' appears {count_a} times.")

if sentence.startswith("Hello"):
    print("Yes, the sentence starts with 'Hello'.")
else:
    print("No, the sentence does not start with 'Hello'.")

words = sentence.split()
print("\nWords in your sentence:")
for word in words:
    print(word)