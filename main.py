import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TradeLink")
root.geometry("1000x700")

users_db = { "admin": {"password": "admin123", "role": "admin"} }

# product inventory list
products_db = [
    {"title": "iPhone 13 Pro", "price": "₱45,000", "loc": "CDO"},
    {"title": "Mechanical Keyboard", "price": "₱2,500", "loc": "Tagoloan"},
    {"title": "Sony Headphones", "price": "₱12,000", "loc": "Manila"},
    {"title": "Ergonomic Chair", "price": "₱3,500", "loc": "Cebu"}
]

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
    for widget in root.winfo_children(): widget.destroy()

def dummy_nav(menu):
    # prove buttons work
    messagebox.showinfo("Nav", f"Opening {menu}...")

def logout():
    if messagebox.askyesno("Exit", "Log out?"):
        show_login_screen()

def login_user(u_ent, p_ent):
    username = u_ent.get().strip()
    password = p_ent.get().strip()
    if username in users_db and users_db[username]["password"] == password:
        show_dashboard(username) 
    else:
        messagebox.showwarning("Error", "Wrong username or password.")

def show_dashboard(user):
    clear_window()
    root.config(bg="#F4F5F7")
    
    # sidebar
    sidebar = tk.Frame(root, bg="#111827", width=200)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)
    
    tk.Label(sidebar, text="🛍️ TradeLink", font=("Arial", 16, "bold"), fg="#00AA5B", bg="#111827").pack(pady=20)
    tk.Button(sidebar, text="My Cart", bg="#1F2937", fg="white", relief="flat", command=lambda: dummy_nav("Cart")).pack(fill=tk.X, padx=10, pady=5, ipady=5)
    tk.Button(sidebar, text="Logout", bg="#ef4444", fg="white", relief="flat", command=logout).pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=20, ipady=5)

    # main area
    main = tk.Frame(root, bg="#F4F5F7")
    main.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    header = tk.Frame(main, bg="#FFFFFF", height=60)
    header.pack(fill=tk.X)
    tk.Label(header, text=f"Welcome back, {user}", font=("Arial", 14), bg="#FFFFFF").pack(side=tk.LEFT, padx=20, pady=15)

def show_login_screen():
    clear_window()
    bg = tk.Canvas(root, highlightthickness=0)
    bg.pack(fill=tk.BOTH, expand=True)
    bg.bind("<Configure>", render_gradient)

    card = tk.Frame(bg, bg="#FFFFFF")
    card.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=400, height=400)
    
    txt_u = tk.Entry(card, bg="#eee"); txt_u.pack(pady=10)
    txt_p = tk.Entry(card, bg="#eee", show="*"); txt_p.pack(pady=10)
    tk.Button(card, text="Login", command=lambda: login_user(txt_u, txt_p)).pack()

if __name__ == "__main__":
    show_login_screen()
    root.mainloop()