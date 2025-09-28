import tkinter as tk
from tkinter import messagebox
from tkinter import Button
import logic
import pyperclip
import pygame as pg
from tkinter import filedialog
import time


pg.mixer.init()
pg.mixer.music.load("buttonClick.mp3")

hover_sound = pg.mixer.Sound("sound.mp3")

last_hover_time = 0  
def buttonSound():
    pg.mixer.music.play()

def play_hover_sound(event=None):
    global last_hover_time
    current_time = time.time()
    if current_time - last_hover_time > 0.3:
        hover_sound.play()
        last_hover_time = current_time

def handle_generate_key():
    new_key = logic.generate_key_str()
    key_entry.delete(0,tk.END)
    key_entry.insert(0,new_key)
    buttonSound()


def handle_encrypt():
    message = message_entry.get()
    key = key_entry.get()


    if not message or not key:
        messagebox.showwarning("Input Error", "Message and Key fields are required.")
        return
    
    encrypted_result = logic.encrypt_message(message=message,key=key)
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
    except:
        pass
    result_text.insert('1.0', decrypted_result)
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
            
            
            result_text.delete('1.0', tk.END)
            result_text.insert('1.0', f"--- Content from {file_path} ---\n\n{file_content}")

        except Exception as e:
            messagebox.showerror("File Error", f"Failed to read file: {e}")


    buttonSound()



window  = tk.Tk()
window.title("Password Encryptor and Decryptor")
window.geometry("500x400")
window.resizable(True,True)
buttonsColor="#799EFF"
backgroundColor="#FEFFC4"
otherFrames="#FFDE63"
frame = tk.Frame(window,background=backgroundColor)
frame.pack(expand=True,fill=tk.BOTH)
#Input Text
input_frame = tk.LabelFrame(frame,padx=5,pady=5,background=otherFrames)
input_frame.pack(fill="x",padx=10,pady=5)

message_label = tk.Label(input_frame,text="Password/Message:",background=otherFrames)
message_label.grid(row=0,column=0,sticky="w", pady=(0, 5))

key_label = tk.Label(input_frame,text="Encryption Key:",background=otherFrames)
key_label.grid(row=2,column=0, sticky="w", pady=(0, 10))

message_entry = tk.Entry(input_frame,width=68,background=backgroundColor)
message_entry.grid(row=1,column=0,sticky="w", pady=(0, 5))

key_entry = tk.Entry(input_frame,width=68,background=backgroundColor)
key_entry.grid(row=3,column=0,columnspan=2, sticky="ew", pady=(0, 10))

key_button = tk.Button(input_frame,text="Generate Key",command=handle_generate_key,bg=buttonsColor)
key_button.grid(row=4,column=0,columnspan=2,pady=(0,10))
key_button.bind("<Enter>", play_hover_sound)

#Buttons
button_frame = tk.LabelFrame(frame,padx=10,pady=5,background=otherFrames)
button_frame.pack(fill='x',padx=10,pady=10)


encrypt_button = tk.Button(button_frame, text="Encrypt",command=handle_encrypt,bg=buttonsColor)
encrypt_button.pack(side="left", padx=25)
encrypt_button.bind("<Enter>", play_hover_sound)


decrypt_button = tk.Button(button_frame, text="Decrypt",command=handle_decrypt,bg=buttonsColor)
decrypt_button.pack(side="left", padx=25)
decrypt_button.bind("<Enter>", play_hover_sound)


clear_button = tk.Button(button_frame, text="Clear",command=handle_clear,bg=buttonsColor)
clear_button.pack(side="left", padx=25)
clear_button.bind("<Enter>", play_hover_sound)

encrypt_file_button = tk.Button(button_frame, text="Encrypt File", command=handle_encrypt_file, bg=buttonsColor)
encrypt_file_button.pack(side="left", padx=25)
encrypt_file_button.bind("<Enter>", play_hover_sound)


#Result
result_frame = tk.LabelFrame(frame,padx=5,pady=5,background=otherFrames)
result_frame.pack(fill="both",padx=10,pady=5)

result_label = tk.Label(result_frame,text="Result(Encrypted/Decrypted):",background=otherFrames)
result_label.grid(row=0,column=0,columnspan=2, sticky="w", pady=(0, 10))

result_text = tk.Text(result_frame,height=4,width=58,background=backgroundColor)
result_text.grid(row=1,column=0,sticky="w",pady=(0,5))

window.mainloop()