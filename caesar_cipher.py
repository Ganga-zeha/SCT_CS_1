def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep non-letters unchanged
    return result

# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

output = caesar_cipher(message, shift, mode)
print(f"\nResult ({mode}ed message):", output)
