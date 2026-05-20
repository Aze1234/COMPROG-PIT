import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TradeLink")
root.geometry("1000x700")

# mock db
users_db = {
    "admin": {"password": "admin123", "role": "admin"} 
}

def render_gradient(event):
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

def login_user(u_ent, p_ent):
    username = u_ent.get().strip()
    password = p_ent.get().strip()
    
    if username in users_db and users_db[username]["password"] == password:
        messagebox.showinfo("Success", f"Welcome {username}!")
    else:
        messagebox.showwarning("Error", "Wrong username or password.")

def register_user(u_ent, p_ent):
    username = u_ent.get().strip()
    password = p_ent.get().strip()
    
    if not username or not password:
        messagebox.showwarning("Oops", "Fill out all fields!")
        return
        
    if username in users_db:
        messagebox.showerror("Error", "Username taken!")
    else:
        users_db[username] = {"password": password, "role": "user"}
        messagebox.showinfo("Success", "Account created!")
        show_login_screen()

def show_login_screen():
    clear_window() 
    bg = tk.Canvas(root, highlightthickness=0)
    bg.pack(fill=tk.BOTH, expand=True)
    bg.bind("<Configure>", render_gradient)

    card = tk.Frame(bg, bg="#FFFFFF", highlightbackground="#1F2937", highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=420, height=480)

    tk.Label(card, text="🛍️ TradeLink", font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#00AA5B").pack(pady=(40, 5))
    tk.Label(card, text="Sign In", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#333333").pack(pady=(0, 25))

    u_box = tk.Frame(card, bg="#F4F5F7")
    u_box.pack(fill=tk.X, padx=50, pady=(0, 20))
    txt_u = tk.Entry(u_box, font=("Arial", 12), bg="#F4F5F7", relief="flat")
    txt_u.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8) 

    p_box = tk.Frame(card, bg="#F4F5F7")
    p_box.pack(fill=tk.X, padx=50, pady=(0, 30))
    txt_p = tk.Entry(p_box, font=("Arial", 12), bg="#F4F5F7", relief="flat", show="*")
    txt_p.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)

    tk.Button(card, text="Login", font=("Arial", 12, "bold"), bg="#00AA5B", fg="white", relief="flat", cursor="hand2", command=lambda: login_user(txt_u, txt_p)).pack(fill=tk.X, padx=50, ipady=10)
    tk.Button(card, text="Sign Up", font=("Arial", 9), bg="#FFFFFF", fg="#00AA5B", relief="flat", cursor="hand2", command=show_signup_screen).pack(pady=(20, 0))

def show_signup_screen():
    clear_window() 
    bg = tk.Canvas(root, highlightthickness=0)
    bg.pack(fill=tk.BOTH, expand=True)
    bg.bind("<Configure>", render_gradient)

    card = tk.Frame(bg, bg="#FFFFFF", highlightbackground="#1F2937", highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=420, height=480)

    tk.Label(card, text="🛍️ TradeLink", font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#00AA5B").pack(pady=(40, 5))
    tk.Label(card, text="Create Account", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#333333").pack(pady=(0, 25))

    u_box = tk.Frame(card, bg="#F4F5F7")
    u_box.pack(fill=tk.X, padx=50, pady=(0, 20))
    txt_u = tk.Entry(u_box, font=("Arial", 12), bg="#F4F5F7", relief="flat")
    txt_u.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8) 

    p_box = tk.Frame(card, bg="#F4F5F7")
    p_box.pack(fill=tk.X, padx=50, pady=(0, 30))
    txt_p = tk.Entry(p_box, font=("Arial", 12), bg="#F4F5F7", relief="flat", show="*")
    txt_p.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)

    tk.Button(card, text="Register", font=("Arial", 12, "bold"), bg="#333333", fg="white", relief="flat", cursor="hand2", command=lambda: register_user(txt_u, txt_p)).pack(fill=tk.X, padx=50, ipady=10)
    tk.Button(card, text="Back to Login", font=("Arial", 9), bg="#FFFFFF", fg="#00AA5B", relief="flat", cursor="hand2", command=show_login_screen).pack(pady=(20, 0))

if __name__ == "__main__":
    show_login_screen()
    root.mainloop()