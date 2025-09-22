import customtkinter as ctk
from tkinter import messagebox
import os

# Use the imported alias 'ctk' when creating the CTk application instance



app = ctk.CTk()
app.geometry("600x400")
# app.title("Flows - Easy to use video downloader")
app._set_appearance_mode("dark")
app.resizable(False, False)





# Left frame for navigation
left_frame = ctk.CTkFrame(app, width=150, height=400, corner_radius=0)
left_frame.place(x=0, y=0)

# Example navigation buttons
nav_btn1 = ctk.CTkButton(left_frame, text="Home", width=120, height=32, corner_radius=6)
nav_btn1.place(x=15, y=50)

# Right frame for main content
right_frame = ctk.CTkFrame(app, width=450, height=400, corner_radius=0)
right_frame.place(x=150, y=0)
#url rntry
entry = ctk.CTkEntry(right_frame, placeholder_text="Enter URL", width=200, height=32, corner_radius=8)

#button
button = ctk.CTkButton(right_frame, text="Download", width=80, height=32, corner_radius=8)
button.place(x=300, y=160)
#label
label = ctk.CTkLabel(right_frame, text="Flows", font=ctk.CTkFont(size=20, weight="bold"))

label2 = ctk.CTkLabel(right_frame, text="Enter Video URL :-", font=ctk.CTkFont(size=14))

# Move your widgets into right_frame instead of app
button.place(in_=right_frame, x=150, y=160)
entry.place(in_=right_frame, x=100, y=120)
label.place(in_=right_frame, x=170, y=50)
label2.place(in_=right_frame, x=100, y=90)





# Style updates
app.title("⚡ Flows - Easy to use video downloader")
label.configure(text="⚡ Flows", font=ctk.CTkFont(size=24, weight="bold"), text_color="#00FFFF")
label2.configure(font=ctk.CTkFont(size=14, weight="bold"), text_color="#AAAAFF")

app.mainloop()