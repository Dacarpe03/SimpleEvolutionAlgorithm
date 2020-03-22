
import string
import random
if __name__ == "__main__":
    print("Hello")
    text = 'abcdefg'
    text = text[:6] + random.choice(string.ascii_lowercase) + text[7:]
    print(text)