from PIL import Image
# from os import urandom
import secrets , random 
import sys
from pathlib import Path
def Xor_encryption(im , key ):
    width , height = im.size
    new_image = Image.new(im.mode, im.size)
    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x,y))
            new_pixel  = tuple(i ^ key for i in pixel)
            new_image.putpixel((x, y), new_pixel)
    return new_image


def decrypting(im, key):
      width , height = im.size
      new_image = Image.new(im.mode, im.size)
      for y in range(height):
            for x in range(width):
                pixel = im.getpixel((x,y))
                new_pixel  = tuple(i ^ key for i in pixel)
                new_image.putpixel((x, y), new_pixel)
      return new_image
    

def shufflleing(new , key ):
    # creat a list of pixel postions 
    image = new
    width, hight = image.size
    random_list_ofPixel = []
    New_shiff = Image.new(image.mode, image.size)

    for y in range(hight):
        for x in range(width):
            random_list_ofPixel.append((x,y))

    rng = random.Random(key)
    rng.shuffle(random_list_ofPixel)

    for y in range(hight):
        for x in range(width):
            i = random_list_ofPixel[y * width + x]
            pixel = image.getpixel(i)
            New_shiff.putpixel((x, y), pixel)

    return New_shiff

def unshuffling(image, key):
    width, height = image.size
    random_list_ofPixel = [(x, y) for y in range(height) for x in range(width)]

    rng = random.Random(key) # choosing the same key gives you the same order 
    rng.shuffle(random_list_ofPixel)

    New_image = Image.new(image.mode, image.size)

    for y in range(height):
        for x in range(width):
            i = random_list_ofPixel[y * width + x]
            pixel = image.getpixel((x, y))
            New_image.putpixel(i, pixel)

    return New_image

# ==============================
# PIXELCRYPT MENU
# ==============================

print("=" * 45)
print("          PIXELCRYPT IMAGE TOOL")
print("=" * 45)
print("  1. Encrypt an image")
print("  2. Decrypt an image")
print("  3. Exit")
print("=" * 45)

choice = input("Choose an option: ").strip()

# ==============================
# ENCRYPTION OPERATION
# ==============================


if choice == "1":

    image_arg = input("Enter the image path: ").strip()
    image_path = Path(image_arg)

    if not image_path.exists():
        print("\n[ERROR] The image file does not exist.")
        sys.exit(1)

    if not image_path.is_file():
        print("\n[ERROR] The path is not a file.")
        sys.exit(1)

    if image_path.suffix.lower() not in [
        ".png", ".jpg", ".jpeg", ".bmp", ".webp"
    ]:
        print("\n[ERROR] Unsupported image extension.")
        sys.exit(1)

    try:
        print("\n[+] Opening image...")
        im = Image.open(image_path)
        im.load()
    except (OSError, ValueError) as error:
        print(f"\n[ERROR] Could not open image: {error}")
        sys.exit(1)

    print("[+] Generating encryption key...")
    key = secrets.randbelow(256)

    print("[+] Encrypting image...")
    new = Xor_encryption(im, key)

    print("[+] Saving key...")
    try:
        with open("key.txt", "w") as key_text:
            key_text.write("Keep the key privately\n")
            key_text.write(str(key))
    except OSError as error:
        print(f"\n[ERROR] Could not save key: {error}")
        sys.exit(1)

    print("[+] Shuffling pixels...")
    newSHuffled = shufflleing(new, key)

    print("[+] Saving encrypted image...")
    try:
        newSHuffled.save("encrypted_image.png")
    except OSError as error:
        print(f"\n[ERROR] Could not save image: {error}")
        sys.exit(1)

    print("\n" + "=" * 45)
    print("       IMAGE ENCRYPTED SUCCESSFULLY")
    print("=" * 45)
    print("[+] Output image : encrypted_image.png")
    print("[+] Key file     : key.txt")
    print("[!] Keep your key safe.")
    print("=" * 45)


# ==============================
# DECRYPTION OPERATION
# ==============================

elif choice == "2":

    encrypted_path = Path(
        input("Enter encrypted image path [encrypted_image.png]: ").strip()
        or "encrypted_image.png"
    )

    key_path = Path(
        input("Enter key file path [key.txt]: ").strip()
        or "key.txt"
    )

    output_path = Path(
        input("Enter output image name [decrypted_image.png]: ").strip()
        or "decrypted_image.png"
    )

    if not encrypted_path.is_file():
        print("\n[ERROR] Encrypted image file not found.")
        sys.exit(1)

    if not key_path.is_file():
        print("\n[ERROR] Key file not found.")
        sys.exit(1)

    try:
        print("\n[+] Reading encryption key...")
        key = int(key_path.read_text().strip().splitlines()[-1])

        if not 0 <= key <= 255:
            raise ValueError("Key must be between 0 and 255.")

        print("[+] Opening encrypted image...")
        encrypted_image = Image.open(encrypted_path)
        encrypted_image.load()

    except (OSError, ValueError, IndexError) as error:
        print(f"\n[ERROR] Could not load image or key: {error}")
        sys.exit(1)

    print("[+] Reversing pixel shuffle...")
    unshuffled_image = unshuffling(encrypted_image, key)

    print("[+] Reversing XOR encryption...")
    decrypted_image = Xor_encryption(unshuffled_image, key)

    print("[+] Saving decrypted image...")
    try:
        decrypted_image.save(output_path)
    except OSError as error:
        print(f"\n[ERROR] Could not save decrypted image: {error}")
        sys.exit(1)

    print("\n" + "=" * 45)
    print("       IMAGE DECRYPTED SUCCESSFULLY")
    print("=" * 45)
    print(f"[+] Output image : {output_path}")
    print("[+] Decryption completed.")
    print("=" * 45)


# ==============================
# EXIT
# ==============================

elif choice == "3":
    print("\nExiting PixelCrypt. Goodbye!")
    sys.exit(0)

else:
    print("\n[ERROR] Invalid option. Please choose 1, 2, or 3.")
    sys.exit(1)


