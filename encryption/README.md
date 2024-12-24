# Encrypt and Decrypt


## How it Works
### Encryption Algorithm
> The function takes in a plain text. Shifts each letter a specified steps forward using a shift key. And finally returns the new cipher text.

### Decryption Algorithm using a known word
> The function takes in a cipher text and known word present in the plain text.
> The function finds the encryption key by encrypting the known word and loops through the cipher text to find if the cipher known word exists. If does the we return the key and use it shift backwards the main cipher text.

### Decryption Algorithm without known word or key
> Suppose I'm now given only a ciphertext and now I should decrypt it.
> I know that the original text was written in English. The text was encrypted by shifting letters forward using a key.

**Procedure** \
English alphabets range between A-Z. Meaning I'll have a total of 26 key trials if I'm to use uppercase letters only.
1. Find a record of all valid english words composed of alphabets A-Z.
2. Split the ciphertext using space separator into a list.
3. Each cipherstring in the list has a fixed number of characters which are definetely same for the original text. Count the characters in the cipherstring. Call this cipherstring_character_count 
4. Find all words that match the cipherstring_character_count and store each in a file.
5. Shift each letter in the cipherstring using all 26 keys one at time. With each key shift, compare if the cipherword formed exist in the english file record of specific character count. If a matching word is found store it another file and move to the next key. If multiple words are found using one key, group those words in one line comma separated. When the keys are depleted move to the next cipherstring and repeat this step.
6. When all cipherstrings are depleted. I'll have a list of words of 26 lines and different files for each cipherstring, each line is a number key. Combine all the words of every row in each file to form sentences.
7. Read the sentences and find if they make sense. Manually delete those that don't make sense all follow english flow of grammar.   
