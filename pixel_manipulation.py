from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size

    # Iterate over each pixel and perform encryption
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = image.getpixel((x, y))

            # Perform encryption operation using the key
            encrypted_pixel = tuple((value + key) % 256 for value in pixel)

            # Set the encrypted pixel value
            image.putpixel((x, y), encrypted_pixel)

    # Save the encrypted image
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    image.save(encrypted_image_path)
    print("Image encrypted and saved as:", encrypted_image_path)

def decrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size

    # Iterate over each pixel and perform decryption
    for x in range(width):
        for y in range(height):
            # Get the pixel value
            pixel = image.getpixel((x, y))

            # Perform decryption operation using the key
            decrypted_pixel = tuple((value - key) % 256 for value in pixel)

            # Set the decrypted pixel value
            image.putpixel((x, y), decrypted_pixel)

    # Save the decrypted image
    decrypted_image_path = image_path.split('_encrypted')[0] + '_decrypted.png'
    image.save(decrypted_image_path)
    print("Image decrypted and saved as:", decrypted_image_path)

def main():
    print("Welcome to Simple Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        image_path = input("Enter the path to the image you want to encrypt: ")
        key = int(input("Enter the encryption key (an integer): "))
        encrypt_image(image_path, key)
    elif choice == '2':
        image_path = input("Enter the path to the image you want to decrypt: ")
        key = int(input("Enter the decryption key (an integer): "))
        decrypt_image(image_path, key)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
