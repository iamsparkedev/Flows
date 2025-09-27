import customtkinter as ctk
from tkinter import messagebox
import os
import webbrowser
import downloader  # Import the downloader module
# Use the imported alias 'ctk' when creating the CTk application instance


#Github btn Logic
def GithubButton():
    webbrowser.open("https://github.com/iamsparkedev/Flows")


#About me btn logic
def AboutMeButton():
    webbrowser.open("https://github.com/iamsparkedev/")


#Main app window
app = ctk.CTk()
app.geometry("600x400")
app._set_appearance_mode("dark")
app.resizable(False, False)
ctk.set_default_color_theme("dark-blue")

# Left frame for navigation
left_frame = ctk.CTkFrame(app, width=150, height=400, corner_radius=0, fg_color="transparent")
left_frame.place(x=0, y=0)

# about me button
nav_btn1 = ctk.CTkButton(left_frame, text="About me", width=120, height=32, corner_radius=8, command=AboutMeButton)
nav_btn1.place(x=15, y=30)

#github button
nav_btn1 = ctk.CTkButton(left_frame, text="GitHub", width=120, height=32, corner_radius=8, command=GithubButton)
nav_btn1.place(x=15, y=72)

# Right frame for main content
right_frame = ctk.CTkFrame(app, width=450, height=400, corner_radius=0, fg_color="transparent")
right_frame.place(x=150, y=0)

#url rntry and variable
entry = ctk.CTkEntry(right_frame, placeholder_text="Enter URL", width=200, height=32, corner_radius=8)

#Download button and logic
def on_button_click():
    url = entry.get()
    downloader.download(url)  # Call the download function from downloader module
button = ctk.CTkButton(right_frame, text="Download", width=80, height=32, corner_radius=8,command=on_button_click,fg_color="#5DD9D9" ,hover_color="#A0F2F2", border_color="#464A4A", border_width=2, font=ctk.CTkFont(size=10, weight="bold"))

#labels
label = ctk.CTkLabel(right_frame, text="Flows", font=ctk.CTkFont(size=20, weight="bold"))
label2 = ctk.CTkLabel(right_frame, text="Enter Video URL :-", font=ctk.CTkFont(size=14))

# Move your widgets into right_frame instead of app
button.place(in_=right_frame, x=150, y=160)
entry.place(in_=right_frame, x=100, y=120)
label.place(in_=right_frame, x=170, y=50)
label2.place(in_=right_frame, x=100, y=90)



# Style updates
app.title("⚡ Flows - Easy to use video downloader")
label.configure(text="⚡ Flows", font=ctk.CTkFont(size=24, weight="bold"), text_color="#5DD9D9")
label2.configure(font=ctk.CTkFont(size=10, weight="bold"), text_color="#AAAAFF")
app.configure(bg="#1E1E1E")
left_frame.configure(fg_color="#2E2E2E", border_width=1, border_color="#3E3E3E")
app.mainloop()