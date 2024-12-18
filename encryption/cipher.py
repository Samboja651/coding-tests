# encipher

# _plain_text = "I Love Coding"
# _known_word = "Love"
# key = 4

def encipher(text: str, key) -> str:
    ecrypted_text = ""
    for letter in text:
        letter = ord(letter)
        letter += key
        letter = chr(letter)
        ecrypted_text += letter
    return ecrypted_text

# cipher_text = encipher(_plain_text, key)
# print(cipher_text)