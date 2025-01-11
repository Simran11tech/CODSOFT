#TASK 2
#Random Password Generator
import tkinter as tk
from tkinter import messagebox
import random
import string
class PasswordGenerator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("Password Generator")
        self.input_frame=tk.Frame(self.window)
        self.input_frame.pack(padx=15,pady=15)
        self.button_frame=tk.Frame(self.window)
        self.button_frame.pack(padx=15,pady=15)
        self.result_frame=tk.Frame(self.window)
        self.result_frame.pack(padx=15,pady=15)
        self.length_label=tk.Label(self.input_frame,text="Password Length:")
        self.length_label.pack(side=tk.LEFT)
        self.length_entry=tk.Entry(self.input_frame,width=8)
        self.length_entry.pack(side=tk.LEFT)
        self.generate_button=tk.Button(self.button_frame,text="Generate Password",command=self.gen_pswd)
        self.generate_button.pack(side=tk.LEFT,padx=10)
        self.copy_button=tk.Button(self.button_frame,text="Copy",command=self.copy)
        self.copy_button.pack(side=tk.LEFT,padx=10)
        self.result_label=tk.Label(self.result_frame, text="Generated Password:")
        self.result_label.pack(side=tk.LEFT)
        self.result_entry=tk.Entry(self.result_frame,width=40)
        self.result_entry.pack(side=tk.LEFT)
    def gen_pswd(self):
        try:
            length=int(self.length_entry.get())
            if length<8:
                messagebox.showerror("Error","Password length should be at least 8 characters.")
                return
            lc=string.ascii_lowercase
            uc=string.ascii_uppercase
            dg=string.digits
            sc=string.punctuation
            ac=lc+uc+dg+sc
            password=[
                random.choice(lc),
                random.choice(uc),
                random.choice(dg),
                random.choice(sc),
            ]
            for _ in range(length - 4):
                password.append(random.choice(ac))
            random.shuffle(password)
            password = "".join(password)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(tk.END, password)
        except ValueError:
            messagebox.showerror("Error", "Invalid password length.")
    def copy(self):
        password = self.result_entry.get()
        self.window.clipboard_clear()
        self.window.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
