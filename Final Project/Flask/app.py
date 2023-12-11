from flask import Flask, request, render_template
from string import digits, ascii_letters
from random import sample

# Use this for your original alphabet string
ALL_LETTERS_DIGITS = digits + ascii_letters
# Use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))

app = Flask(__name__)

ACTION_ENCRYPT = 'encrypt'
ACTION_DECRYPT = 'decrypt'


def encrypt_message(message, key):
    """
    Encrypts the message provided by the user using a substitution cipher with a provided key.
    This function iterates over each character of the message. If the character
    exists in ALL_LETTERS_DIGITS, it gets substituted
    by the corresponding character in the key. Characters that do not exist in ALL_LETTER_DIGITS
    such as punctuation do not get encrypted but will still be accepted and printed.

    Args:
        message (str): The message provided by the user to be encrypted.
        key (str): The substitution cipher key.

    Returns:
        str: The encrypted message.
    """
    encrypted_message = ''
    for char in message:
        if char in ALL_LETTERS_DIGITS:
            position = ALL_LETTERS_DIGITS.find(char)
            if position >= 0 and position < len(key):
                encrypted_char = key[position]
                encrypted_message += encrypted_char
            else:
                # Handles an edge case where the user-provided key has fewer characters than the message
                encrypted_message += char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """
    Decrypts encrypted message using the provided key.
    This function iterates over each character of the encrypted message. If the character
    exists in the key, it gets substituted back to its original form using ALL_LETTERS_DIGITS.

    Args:
        encrypted_message (str): The encrypted message to be decrypted.
        key (str): The substitution cipher key.

    Returns:
        str: The decrypted message.
    """
    decrypted_message = ''
    for char in encrypted_message:
        if char in key:
            position = key.find(char)
            decrypted_char = ALL_LETTERS_DIGITS[position]
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def caesar_cipher(text, shift=None):
    if shift is None:
        shift = 2  # Default shift value
    decrypted_message = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message

def atbash_cipher(text):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    inverted_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    
    # Replace each character with its opposite in the alphabet
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if char in alphabet:
                index = alphabet.index(char)
                encrypted_char = inverted_alphabet[index]
                if is_upper:
                    encrypted_char = encrypted_char.upper()
                result += encrypted_char
            else:
                result += char
        else:
            result += char 
    return result


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        cipher_type = request.form.get("cipher_type")
        action = request.form.get("action")
        message = request.form.get("message")
        key = request.form.get("key")

        if cipher_type == "substitution":
            if action == "encrypt":
                if key == "":
                    key = RANDOM_KEY
                encrypted_message = encrypt_message(message, key)
                return render_template("result.html", cipher_type="Substitution Cipher", result=encrypted_message, key=key)

            elif action == "decrypt":
                if key == "":
                    return "Error: Decryption requires a key."
                decrypted_message = decrypt_message(message, key)
                return render_template("result.html", cipher_type="Substitution Cipher", result=decrypted_message, key=key)
        elif cipher_type == "caesar":
            # Caesar Cipher logic with key validation
            if not key.isdigit():
                return "Error: Caesar Cipher requires a numeric key."
            if action == "encrypt":
                encrypted_message = caesar_cipher(message, int(key))
                return render_template("result.html", cipher_type="Caesar Cipher", result=encrypted_message, key=key)
            elif action == "decrypt":
                decrypted_message = caesar_cipher(message, -int(key))
                return render_template("result.html", cipher_type="Caesar Cipher", result=decrypted_message, key=key)
        elif cipher_type == "atbash":
            if action == "encrypt":
                encrypted_message = atbash_cipher(message)
                return render_template("result.html", cipher_type="Atbash Cipher", result=encrypted_message, key="N/A")
            elif action == "decrypt":
                decrypted_message = atbash_cipher(message)  
                return render_template("result.html", cipher_type="Atbash Cipher", result=decrypted_message, key="N/A")

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
