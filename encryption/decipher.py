# decipher

def decipher(cipher_text: str, known_word_in_plain_text: str)-> str:
    # find the encryption key
    def _encipher_known_word(text, key: int) -> str:
        ecrypted_text = ""
        for letter in text:
            letter = ord(letter)
            letter += key
            letter = chr(letter)
            ecrypted_text += letter
        return ecrypted_text
    
    def _encryption_key_from_known_word():
        encrypted_known_word = ""
        for key in range(1, 27):
            encrypted_known_word = _encipher_known_word(known_word_in_plain_text, key)
            if encrypted_known_word in cipher_text:
                return key       
            else:
                continue
        return "Encryption was key not found."
    
    shift_key = _encryption_key_from_known_word()
    decrypted_text = ""
    for letter in cipher_text:
        letter = ord(letter)
        # shift backward
        letter -= shift_key
        letter = chr(letter)
        decrypted_text += letter

    return decrypted_text

class Decrypt():
    def __init__(self):
        self.cipher_text = "M$Pszi$Gshmrk"