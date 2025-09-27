import tkinter as tk
from tkinter import messagebox
import logic
import pyperclip
import pygame as pg
from tkinter import filedialog

pg.mixer.init()
pg.mixer.music.load("buttonClick.mp3")

def buttonSound():
    pg.mixer.music.stop()
    pg.mixer.music.play()

def handle_generate_key():
    new_key = logic.generate_key_str()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, new_key)
    buttonSound()

def handle_encrypt():
    message = message_entry.get()
    key = key_entry.get()

    if not message or not key:
        messagebox.showwarning("Input Error", "Message and Key fields are required.")
        return

    encrypted_result = logic.encrypt_message(message=message, key=key)
    result_text.delete('1.0', tk.END)
    result_text.insert('1.0', encrypted_result)
    buttonSound()

def handle_decrypt():
    encrypted_message = result_text.get('1.0', tk.END).strip()
    key = key_entry.get()

    if not key:
        messagebox.showwarning("Input Error", "Key field cannot be empty.")
        return

    try:
        decrypted_result = logic.decrypt_message(encrypted_message, key)
        result_text.delete('1.0', tk.END)
        result_text.insert('1.0', decrypted_result)
    except Exception as e:
        messagebox.showerror("Decryption Error", f"Failed to decrypt: {e}")
    buttonSound()

def handle_clear():
    message_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    result_text.delete('1.0', tk.END)
    buttonSound()

def handle_encrypt_file():
    file_path = filedialog.askopenfilename(
        title="Select a Text File to Encrypt",
        filetypes=[("Text Files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            key = key_entry.get()
            if not key:
                messagebox.showwarning("Input Error", "Key is required to encrypt the file.")
                return

            encrypted_content = logic.encrypt_message(file_content, key)
            result_text.delete('1.0', tk.END)
            result_text.insert('1.0', encrypted_content)

        except Exception as e:
            messagebox.showerror("File Error", f"Failed to read file: {e}")
    buttonSound()

window = tk.Tk()
window.title("Password Encryptor and Decryptor")
window.geometry("800x600")
window.resizable(True, True)

buttonsColor = "#799EFF"
backgroundColor = "#FEFFC4"
otherFrames = "#FFDE63"

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

main_frame = tk.Frame(window, background=backgroundColor)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(2, weight=1)


input_frame = tk.LabelFrame(main_frame, background=otherFrames, text="Input")
input_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
input_frame.columnconfigure(0, weight=1)

message_label = tk.Label(input_frame, text="Password/Message:", background=otherFrames)
message_label.grid(row=0, column=0, sticky="w")

message_entry = tk.Entry(input_frame, background=backgroundColor)
message_entry.grid(row=1, column=0, sticky="ew", pady=(0, 5))

key_label = tk.Label(input_frame, text="Encryption Key:", background=otherFrames)
key_label.grid(row=2, column=0, sticky="w")

key_entry = tk.Entry(input_frame, background=backgroundColor)
key_entry.grid(row=3, column=0, sticky="ew", pady=(0, 5))

key_button = tk.Button(input_frame, text="Generate Key", command=handle_generate_key, bg=buttonsColor)
key_button.grid(row=4, column=0, sticky="e", pady=(0, 5))

# ---- Button Frame ----
button_frame = tk.LabelFrame(main_frame, background=otherFrames, text="Actions")
button_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

encrypt_button = tk.Button(button_frame, text="Encrypt", command=handle_encrypt, bg=buttonsColor)
encrypt_button.grid(row=0, column=0, padx=5, sticky="ew")

decrypt_button = tk.Button(button_frame, text="Decrypt", command=handle_decrypt, bg=buttonsColor)
decrypt_button.grid(row=0, column=1, padx=5, sticky="ew")

clear_button = tk.Button(button_frame, text="Clear", command=handle_clear, bg=buttonsColor)
clear_button.grid(row=0, column=2, padx=5, sticky="ew")

encrypt_file_button = tk.Button(button_frame, text="Encrypt File", command=handle_encrypt_file, bg=buttonsColor)
encrypt_file_button.grid(row=0, column=3, padx=5, sticky="ew")

# ---- Result Frame ----
result_frame = tk.LabelFrame(main_frame, background=otherFrames, text="Result")
result_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
result_frame.columnconfigure(0, weight=1)
result_frame.rowconfigure(1, weight=1)

result_label = tk.Label(result_frame, text="Encrypted / Decrypted Output:", background=otherFrames)
result_label.grid(row=0, column=0, sticky="w")

result_text = tk.Text(result_frame, background=backgroundColor, wrap="word")
result_text.grid(row=1, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(result_frame, command=result_text.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
result_text.config(yscrollcommand=scrollbar.set)

# Run the application
window.mainloop()