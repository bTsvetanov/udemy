def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char

    return result

ceasar_text = caesar_cipher("Hello, World!", 3)
print(ceasar_text)