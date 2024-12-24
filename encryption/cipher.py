# encipher

_plain_text = "M$Pszi$Gshmrk"
# _known_word = "Love"
key = 3

def encipher(text: str, key) -> str:
    ecrypted_text = ""
    for letter in text:
        letter = ord(letter)
        letter += key
        letter = chr(letter)
        ecrypted_text += letter
    return ecrypted_text

with open("encryption/ciphertexts2.txt", "a", encoding="utf-8")as text:
    for key in range(1, 27):
        cipher_text = encipher(_plain_text, key)
        text.write(cipher_text+"\n")
