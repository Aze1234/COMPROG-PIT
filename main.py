import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TradeLink")
root.geometry("1000x700")

def render_gradient(event):
    # draws smooth green to dark background fade
    canvas = event.widget
    width, height = event.width, event.height
    canvas.delete("gradient") 
    
    c1, c2 = (0, 170, 91), (17, 24, 39)
    for i in range(60):
        r = int(c1[0] + (c2[0] - c1[0]) * (i / 60))
        g = int(c1[1] + (c2[1] - c1[1]) * (i / 60))
        b = int(c1[2] + (c2[2] - c1[2]) * (i / 60))
        y1, y2 = int(height * (i / 60)), int(height * ((i + 1) / 60))
        hex_color = f'#{r:02x}{g:02x}{b:02x}' 
        canvas.create_rectangle(0, y1, width, y2+1, fill=hex_color, outline=hex_color, tags="gradient")
    canvas.tag_lower("gradient") 

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_login_screen():
    clear_window() 
    
    bg = tk.Canvas(root, highlightthickness=0)
    bg.pack(fill=tk.BOTH, expand=True)
    bg.bind("<Configure>", render_gradient)

    # white floating card
    card = tk.Frame(bg, bg="#FFFFFF", highlightbackground="#1F2937", highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=420, height=480)

    tk.Label(card, text="🛍️ TradeLink", font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#00AA5B").pack(pady=(40, 5))
    tk.Label(card, text="Sign In", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#333333").pack(pady=(0, 25))

    # user input
    tk.Label(card, text="Username", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#666666").pack(anchor="w", padx=50, pady=(0, 5))
    u_box = tk.Frame(card, bg="#F4F5F7")
    u_box.pack(fill=tk.X, padx=50, pady=(0, 20))
    tk.Label(u_box, text="👤", font=("Arial", 12), bg="#F4F5F7").pack(side=tk.LEFT, padx=(10, 5))
    txt_username = tk.Entry(u_box, font=("Arial", 12), bg="#F4F5F7", relief="flat")
    txt_username.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8) 

    # pass input
    tk.Label(card, text="Password", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#666666").pack(anchor="w", padx=50, pady=(0, 5))
    p_box = tk.Frame(card, bg="#F4F5F7")
    p_box.pack(fill=tk.X, padx=50, pady=(0, 30))
    tk.Label(p_box, text="🔒", font=("Arial", 12), bg="#F4F5F7").pack(side=tk.LEFT, padx=(10, 5))
    txt_password = tk.Entry(p_box, font=("Arial", 12), bg="#F4F5F7", relief="flat", show="*")
    txt_password.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)

    tk.Button(card, text="Login to Account", font=("Arial", 12, "bold"), bg="#00AA5B", fg="white", relief="flat", cursor="hand2").pack(fill=tk.X, padx=50, ipady=10)

if __name__ == "__main__":
    show_login_screen()
    root.mainloop()