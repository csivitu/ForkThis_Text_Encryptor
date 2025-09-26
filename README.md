# ForkThis_Text_Encryptor

A simple Python application for encrypting and decrypting messages using symmetric encryption. The project features a graphical user interface (GUI) built with Tkinter and uses the `cryptography` library for secure encryption.

## Features

- Encrypt and decrypt text messages with a user-provided key
- Generate secure encryption keys
- Copy results to clipboard
- Play sound effects on button clicks
- Simple and user-friendly GUI

## Requirements

- Python 3.11+
- [cryptography](https://pypi.org/project/cryptography/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [pygame](https://pypi.org/project/pygame/)
- [Pillow](https://pypi.org/project/Pillow/) (for image handling, optional)

Install dependencies with:

```sh
pip install cryptography pyperclip pygame Pillow
```
## Usage
Run the GUI.

Enter your message and encryption key.

Click "Encrypt" to encrypt the message, or "Decrypt" to decrypt.

Use "Generate Key" to create a new secure key.

Copy results with the "Copy" button.
