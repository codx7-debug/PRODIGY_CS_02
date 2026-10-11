# 🔐 PixelCrypt — Image Encryption Tool


<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pillow-Image_Processing-46A2F1?style=for-the-badge" alt="Pillow">
  <img src="https://img.shields.io/badge/Status-Learning_Project-2EA44F?style=for-the-badge" alt="Learning Project">
</p>


## 📌 Overview

**PixelCrypt** is a command-line tool written in Python that demonstrates basic image encryption concepts through pixel manipulation.

The tool combines two operations:

- 🔑 **XOR Encryption:** Modifies pixel channel values using a numeric key.
- 🔀 **Pixel Shuffling:** Rearranges pixel positions using a reproducible pseudorandom permutation.

The program can encrypt an image, save the encryption key, and reverse both operations to reconstruct the original image.

> **Note:** This project is intended for educational purposes. The current XOR-and-shuffling algorithm is not suitable for protecting sensitive information.

## ✨ Features

- 🖼️ Image input validation
- 🔑 Automatic generation of an encryption key
- 🔐 XOR-based pixel encryption
- 🔀 Reproducible pixel shuffling using a seed
- 💾 Automatic saving of the encrypted image
- 🔓 Image decryption using the saved key
- 📂 Custom input paths for encryption and decryption
- 🖥️ Interactive command-line menu
- ✅ Informative status messages and error handling

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pillow (PIL) | Image loading, manipulation, and saving |
| `random` | Reproducible pixel shuffling |
| `secrets` | Generation of a random numeric key |
| `pathlib` | Input path validation |
| `sys` | Program exit handling |

## 📦 Installation

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

### 2. Clone or download the project

If you use Git:

```bash
git clone <your-repository-url>
cd PixelCrypt
```

Alternatively, download the project files and open the project folder in your terminal.

### 3. Install the required dependency

```bash
pip install Pillow
```

The other libraries used by the program are included with Python.

## 🚀 How to Use

Run the program from your terminal:

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it is different.

The application displays a menu similar to this:

```text
=============================================
          PIXELCRYPT IMAGE TOOL
=============================================
  1. Encrypt an image
  2. Decrypt an image
  3. Exit
=============================================
Choose an option:
```

### 🔒 1. Encrypt an Image

1. Select option `1`.
2. Enter the path to the image you want to encrypt.
3. Wait for the encryption and shuffling operations to finish.
4. Keep the generated key file safe.

Example:

```text
Choose an option: 1

Enter the image path: photo.png

[+] Opening image...
[+] Generating encryption key...
[+] Encrypting image...
[+] Saving key...
[+] Shuffling pixels...
[+] Saving encrypted image...

IMAGE ENCRYPTED SUCCESSFULLY
```

The program creates:

- `encrypted_image.png` — the encrypted image.
- `key.txt` — the numeric key required for decryption.

**Important:** The current implementation saves these files in the program's working directory. Existing files with the same names may be overwritten.

### 🔓 2. Decrypt an Image

1. Select option `2`.
2. Enter the encrypted image path, or press Enter to use the default.
3. Enter the key file path, or press Enter to use the default.
4. Enter an output filename, or press Enter to use the default.
5. Wait for the program to restore the image.

Example:

```text
Choose an option: 2

Enter encrypted image path [encrypted_image.png]:
Enter key file path [key.txt]:
Enter output image name [decrypted_image.png]:

[+] Reading encryption key...
[+] Opening encrypted image...
[+] Reversing pixel shuffle...
[+] Reversing XOR encryption...
[+] Saving decrypted image...

IMAGE DECRYPTED SUCCESSFULLY
```

The restored image is saved as `decrypted_image.png` by default.

### 🚪 3. Exit

Select option `3` to close the application.

## 🧠 How It Works

### Step 1 — Generate a Key

The program generates a number between `0` and `255`:

```python
key = secrets.randbelow(256)
```

This key is used by both the XOR operation and the reproducible shuffling process.

### Step 2 — Encrypt the Pixels

Each pixel channel is XORed with the key:

```python
new_pixel = tuple(i ^ key for i in pixel)
```

XOR is reversible: applying the same operation with the same key restores the original channel values.

### Step 3 — Shuffle the Pixels

The program creates a list of pixel coordinates and shuffles it:

```python
rng = random.Random(key)
rng.shuffle(random_list_ofPixel)
```

Using the same seed with the same initial list reproduces the same permutation.

### Step 4 — Reverse the Operations

Decryption reverses the process in the opposite order:

1. Unshuffle the pixels.
2. Apply XOR with the same key.
3. Save the reconstructed image.

## 📁 Project Structure

```text
PixelCrypt/
├── main.py
├── key.txt                 # Generated key
├── encrypted_image.png     # Encrypted output
└── decrypted_image.png     # Decrypted output
```

The generated files appear after running the relevant operations.

## ⚠️ Limitations and Security

PixelCrypt is an educational project, not a production-grade encryption system.

- XOR with a single byte does not provide strong confidentiality.
- Python's `random` module is not designed for cryptographic security.
- Pixel shuffling is reversible obfuscation, not secure encryption.
- The key file is stored as plain text.
- Some image modes, such as grayscale or palette-based images, may require additional handling.
- Image processing can consume significant memory for large images.

For applications involving sensitive images, use an established authenticated encryption algorithm such as AES-GCM or ChaCha20-Poly1305 with proper key management.

## 🎯 Learning Objectives

This project provides practical experience with:

- Python functions and modules
- Nested loops and coordinate systems
- Tuples and lists
- Bitwise XOR operations
- Pseudorandom number generation and seeds
- Image processing with Pillow
- File handling and path validation
- Command-line interfaces
- Reversible transformations and debugging

## 🔮 Future Improvements

Potential improvements include:

- [ ] Add progress bars and loading indicators.
- [ ] Support additional image modes.
- [ ] Add automated tests for encryption and decryption.
- [ ] Allow users to choose output filenames during encryption.
- [ ] Improve key storage and validation.
- [ ] Add a graphical user interface.
- [ ] Implement authenticated encryption for a security-focused version.

## 👨‍💻 Author

**Your Name**

Add your GitHub username, portfolio, or contact details here.

---

<p align="center">
  <strong>Built with Python to explore image processing, reversible transformations, and introductory cryptography.</strong>
</p>
