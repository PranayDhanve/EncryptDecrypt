from tkinter import *
from tkinter import messagebox
import base64


def display_result(title, message, bg_color):
    result_window = Toplevel(screen)
    result_window.title(title)
    result_window.geometry("400x200")
    result_window.configure(bg=bg_color)

    Label(result_window, text=title.upper(), font=("Arial", 14), fg="white", bg=bg_color).place(x=10, y=10)
    text_result = Text(result_window, font=("Calibri", 14), bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text_result.place(x=10, y=40, width=380, height=150)
    text_result.insert(END, message)
    text_result.config(state=DISABLED)  

# Decryption 
def decrypt():
    password = code.get()

    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return
    elif password != "0000":
        messagebox.showerror("Error", "Invalid password.")
        return

    # Perform decryption
    try:
        message = text_input.get(1.0, END).strip()
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypted_message = base64_bytes.decode("ascii")
        display_result("Decryption", decrypted_message, "#00bd56")
    except Exception as e:
        messagebox.showerror("Error", "Failed to decrypt the message. Make sure it's encoded correctly.")

# Encryption function
def encrypt():
    password = code.get()

    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return
    elif password != "0000":
        messagebox.showerror("Error", "Invalid password.")
        return

    # Perform encryption
    try:
        message = text_input.get(1.0, END).strip()
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypted_message = base64_bytes.decode("ascii")
        display_result("Encryption", encrypted_message, "#ed3833")
    except Exception as e:
        messagebox.showerror("Error", "Failed to encrypt the message.")

# Reset function to clear input fields
def reset():
    code.set("")
    text_input.delete(1.0, END)

# Main UI function
def main_screen():
    global text_input
    global screen
    global code

    screen = Tk()
    screen.geometry("400x400")
    screen.title("Encryption-Decryption App")

    # Title label
    Label(text="Text Encryptor and Decryptor", fg="black", font=("Arial", 14)).place(x=10, y=10)

    # Input text box
    text_input = Text(font=("Arial", 12), bg="white", relief=GROOVE, wrap=WORD, bd=1)
    text_input.place(x=10, y=50, width=380, height=100)

    # Password entry label
    Label(text="Enter Secret Key", fg="black", font=("Calibri", 13)).place(x=10, y=170)

    
    code = StringVar()
    Entry(width=30, bd=1, textvariable=code, font=("Arial", 13), show="*").place(x=10, y=200)

    
    Button(text="ENCRYPT", height=2, width=23, bg="#ed3833", fg="white", bd=1, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=1, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#1089ff", fg="white", bd=1, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
