# Encrypt and Decrypt


## How it Works
### Encryption Algorithm
> The function takes in a plain text. Shifts each letter a specified steps forward using a shift key. And finally returns the new cipher text.

### Decryption Algorithm
> The function takes in a cipher text and known word present in the plain text.
> The function finds the encryption key by encrypting the known word and loops through the cipher text to find if the cipher known word exists. If does the we return the key and use it shift backwards the main cipher text.