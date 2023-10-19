import customtkinter as ctk
import tkinter
import customtkinter
from PIL import ImageTk, Image
import re

def create_window():
    window = ctk.CTk()
    window.geometry("1400x800")
    ctk.set_appearance_mode("dark")
    window.resizable(width=0, height=0)
    center_window(window)
    window.mainloop()

def center_window(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 1400
    window_height = 800
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

if __name__ == "__main__":
    create_window()
    
