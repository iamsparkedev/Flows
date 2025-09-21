import customtkinter as ctk
from tkinter import messagebox
import os

# Use the imported alias 'ctk' when creating the CTk application instance
app = ctk.CTk()
app.geometry("600x500")
app.title("Flows - Easy to use video downloader")
app._set_appearance_mode("dark")

button = ctk.CTkButton(app, text="Click Me")
button.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="CTkEntry")
entry.pack(pady=20)






app.mainloop()