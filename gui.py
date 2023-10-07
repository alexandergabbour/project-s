#!/usr/bin/python3

import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1200x800")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

menu = customtkinter.CTkFrame(master=frame)
menu.pack(padx=(0, 300))

label = customtkinter.CTkLabel(master=frame, text="hello")
label.pack(pady=10, padx=12)

root.mainloop()
