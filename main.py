import language


def encrypt_text(cur_text, lan, cur_task):
    words = cur_text.split()
    if cur_task == "encrypt":
        encrypted_words = [caesar_cipher(word, len(word.strip('.,?!";:')), lan) for word in words]
        return " ".join(encrypted_words)
    elif cur_task == "decrypt":
        decrypted_words = [caesar_decipher(word, len(word.strip('.,?!";:')), lan) for word in words]
        return " ".join(decrypted_words)


def caesar_cipher(word, shift, cur_language):
    abc = language.create_alphabet(cur_language)
    encrypted_word = ""
    for i in range(len(word)):
        if word[i].upper() not in abc:
            encrypted_word += (word[i])
        if word[i].upper() in abc:
            c = abc[(abc.index(word[i].upper()) + shift) % len(abc)]
            if word[i].isupper():
                encrypted_word += c.upper()
            else:
                encrypted_word += c.lower()

    return encrypted_word


def caesar_decipher(word, shift, cur_language):
    abc = language.create_alphabet(cur_language)
    decrypted_word = ""
    for i in range(len(word)):
        if word[i].upper() not in abc:
            decrypted_word += (word[i])
        if word[i].upper() in abc:
            c = abc[(abc.index(word[i].upper()) - shift) % len(abc)]
            if word[i].isupper():
                decrypted_word += c.upper()
            else:
                decrypted_word += c.lower()

    return decrypted_word


def caesar_cipher_num(word, n, cur_lang, task1):
    abc = language.create_alphabet(cur_lang)
    new_word = " "
    for i in range(len(word)):
        if word[i].upper() not in abc:
            new_word += (word[i])
        if word[i].upper() in abc:
            if task1 == "encrypt":
                c = abc[(abc.index(word[i].upper()) + n) % len(abc)]
                if word[i].isupper():
                    new_word += c.upper()
                else:
                    new_word += c.lower()
            elif task1 == "decrypt":
                c = abc[(abc.index(word[i].upper()) - n) % len(abc)]
                if word[i].isupper():
                    new_word += c.upper()
                else:
                    new_word += c.lower()
    return new_word


if __name__ == '__main__':
    text = str(input("Enter text: "))
    current_language = input("Choose language! For example: ru  ")
    task = input("Choose task: encrypt/decrypt ")
    chars = input("Set the number of characters? n/y ")
    if chars == 'y':
        num = int(input("Enter the number of characters: "))
        encrypted_text = caesar_cipher_num(text, num, current_language, task)
    elif chars == 'n':
        encrypted_text = encrypt_text(text, current_language, task)
    print(encrypted_text)
