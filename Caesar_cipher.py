#Ceaser_Cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    print("This program can encrypt or decrypt your message.")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ").strip()
        
        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = encrypt(message, shift)
            print("\nEncrypted message:", encrypted)
        
        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted = decrypt(message, shift)
            print("\nDecrypted message:", decrypted)
        
        elif choice == "3":
            print("Exiting... bye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
