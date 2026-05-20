import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TradeLink")
root.geometry("1000x700")

def clear_window():
    # wipe screen clean before drawing next page
    for widget in root.winfo_children():
        widget.destroy()

def show_login_screen():
    clear_window()
    # placeholder for now
    tk.Label(root, text="Login Screen Loading...", font=("Arial", 20)).pack(pady=100)

if __name__ == "__main__":
    show_login_screen()
    root.mainloop()