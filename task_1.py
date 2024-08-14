def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26  # Ensure shift is within the alphabet range

    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            # Determine starting point
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Would you like to encrypt or decrypt? (Type 'encrypt' or 'decrypt'): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return

    text = input("Enter the message: ").strip()
    shift = int(input("Enter the shift value: ").strip())

    # Perform encryption or decryption
    output = caesar_cipher(text, shift, mode)

    print(f"Result: {output}")

if __name__ == "__main__":
    main()