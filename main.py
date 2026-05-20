from tkinter import *
from tkinter import messagebox

# 1. MAIN APPLICATION SETUP

root = Tk()
root.title("TradeLink - Marketplace") 
root.geometry("950x550") 
root.config(bg="#FFFFFF")
root.minsize(750, 500) 

# 2. VISUAL EFFECTS (THE GRADIENT ENGINE)

def render_gradient(event):
    #  green-to-dark bg
    
    canvas = event.widget
    width, height = event.width, event.height
    canvas.delete("gradient") 
    
    
    c1, c2 = (0, 170, 91), (17, 24, 39)
    
    
    for i in range(60):
        r = int(c1[0] + (c2[0] - c1[0]) * (i / 60))
        g = int(c1[1] + (c2[1] - c1[1]) * (i / 60))
        b = int(c1[2] + (c2[2] - c1[2]) * (i / 60))
        
        y1 = int(height * (i / 60))
        y2 = int(height * ((i + 1) / 60))
        
        hex_color = f'#{r:02x}{g:02x}{b:02x}' 
        canvas.create_rectangle(0, y1, width, y2+1, fill=hex_color, outline=hex_color, tags="gradient")
        
# 3. fAKE DATA BASE
users_db = {
    "admin": {"password": "admin123", "role": "admin"} # Hardcoded admin account
}

products_db = [
    {"title": "iPhone 13 Pro (128GB)", "price": "₱45,000", "loc": "Cagayan de Oro", "img_file": "download.png"},
    {"title": "Mechanical Keyboard", "price": "₱2,500", "loc": "Tagoloan", "img_file": ""},
    {"title": "Sony WH-1000XM4", "price": "₱12,000", "loc": "Manila", "img_file": ""},
    {"title": "Ergonomic Mesh Chair", "price": "₱3,500", "loc": "Cebu City", "img_file": ""},
    {"title": "MacBook Air M1", "price": "₱38,000", "loc": "Davao City", "img_file": ""},
    {"title": "Nintendo Switch OLED", "price": "₱14,500", "loc": "Iligan City", "img_file": ""},
    {"title": "Logitech G Pro X", "price": "₱6,500", "loc": "Makati City", "img_file": ""},
    {"title": "Secretlab Titan", "price": "₱22,000", "loc": "Quezon City", "img_file": ""},
    {"title": "iPad Air (5th Gen)", "price": "₱32,000", "loc": "Cagayan de Oro", "img_file": ""},
    {"title": "Samsung Galaxy S23", "price": "₱35,000", "loc": "Cebu City", "img_file": ""},
    {"title": "Razer DeathAdder V2", "price": "₱2,200", "loc": "Davao City", "img_file": ""},
    {"title": "AirPods Pro 2", "price": "₱13,500", "loc": "Manila", "img_file": ""}
]

# 4. SYSTEM LOGIC 


def register_user(new_user_entry, new_pass_entry):
    
    username = new_user_entry.get().strip()
    password = new_pass_entry.get().strip()
    
    if not username or not password:
        messagebox.showwarning("Oops", "Please fill out all fields!")
        return
        
    if username in users_db:
        messagebox.showerror("Error", "Username taken! Try another one.")
    else:
       
        users_db[username] = {"password": password, "role": "user"}
        messagebox.showinfo("Success", "Account created! You can sign in now.")
        show_login_screen()

def login_user(user_entry, pass_entry):
    username = user_entry.get().strip()
    password = pass_entry.get().strip()
    
    
    if username in users_db and users_db[username]["password"] == password:
        user_role = users_db[username]["role"]
        show_dashboard(username, user_role) 
    else:
        messagebox.showwarning("Access Denied", "Wrong username or password.")

def confirm_logout():
    if messagebox.askyesno("Leaving?", "Are you sure you want to log out?"):
        show_login_screen() 

def clear_window():
    
    for widget in root.winfo_children():
        widget.destroy()

def dummy_button_click(menu_name):
    
    messagebox.showinfo("Nav", f"Opening {menu_name}...")



# 5. USER INTERFACES 


def show_login_screen():
    clear_window() 
    
    # Background
    bg = Canvas(root, highlightthickness=0)
    bg.pack(fill=BOTH, expand=True)
    bg.bind("<Configure>", render_gradient)

    # The white floating login card
    card = Frame(bg, bg="#FFFFFF", highlightbackground="#1F2937", highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor=CENTER, width=420, height=480)

    # Headers
    Label(card, text="🛍️ TradeLink", font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#00AA5B").pack(pady=(40, 5))
    Label(card, text="Sign In", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#333333").pack(pady=(0, 25))

    # Username Field (with icon)
    Label(card, text="Username", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#666666").pack(anchor="w", padx=50, pady=(0, 5))
    u_box = Frame(card, bg="#F4F5F7")
    u_box.pack(fill=X, padx=50, pady=(0, 20))
    Label(u_box, text="👤", font=("Arial", 12), bg="#F4F5F7").pack(side=LEFT, padx=(10, 5))
    txt_username = Entry(u_box, font=("Arial", 12), bg="#F4F5F7", relief="flat")
    txt_username.pack(side=LEFT, fill=X, expand=True, ipady=8) 

    # Password Field (with icon)
    Label(card, text="Password", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#666666").pack(anchor="w", padx=50, pady=(0, 5))
    p_box = Frame(card, bg="#F4F5F7")
    p_box.pack(fill=X, padx=50, pady=(0, 30))
    Label(p_box, text="🔒", font=("Arial", 12), bg="#F4F5F7").pack(side=LEFT, padx=(10, 5))
    txt_password = Entry(p_box, font=("Arial", 12), bg="#F4F5F7", relief="flat", show="*")
    txt_password.pack(side=LEFT, fill=X, expand=True, ipady=8)

    # Buttons
    Button(card, text="Login to Account", font=("Arial", 12, "bold"), bg="#00AA5B", fg="white", relief="flat", cursor="hand2", command=lambda: login_user(txt_username, txt_password)).pack(fill=X, padx=50, ipady=10)
    Button(card, text="Don't have an account? Sign Up", font=("Arial", 9), bg="#FFFFFF", fg="#00AA5B", relief="flat", cursor="hand2", command=show_signup_screen).pack(pady=(20, 0))


def show_signup_screen():
    # Identical to the login screen, just with different labels and routing!
    clear_window()
    
    bg = Canvas(root, highlightthickness=0)
    bg.pack(fill=BOTH, expand=True)
    bg.bind("<Configure>", render_gradient)

    card = Frame(bg, bg="#FFFFFF", highlightbackground="#1F2937", highlightthickness=1)
    card.place(relx=0.5, rely=0.5, anchor=CENTER, width=420, height=480)

    Label(card, text="🛍️ TradeLink", font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#00AA5B").pack(pady=(40, 5))
    Label(card, text="Create Account", font=("Arial", 16, "bold"), bg="#FFFFFF", fg="#333333").pack(pady=(0, 25))

    Label(card, text="New Username", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#666666").pack(anchor="w", padx=50, pady=(0, 5))
    u_box = Frame(card, bg="#F4F5F7")
    u_box.pack(fill=X, padx=50, pady=(0, 20))
    Label(u_box, text="👤", font=("Arial", 12), bg="#F4F5F7").pack(side=LEFT, padx=(10, 5))
    txt_new_user = Entry(u_box, font=("Arial", 12), bg="#F4F5F7", relief="flat")
    txt_new_user.pack(side=LEFT, fill=X, expand=True, ipady=8) 

    Label(card, text="New Password", font=("Arial", 10, "bold"), bg="#FFFFFF", fg="#666666").pack(anchor="w", padx=50, pady=(0, 5))
    p_box = Frame(card, bg="#F4F5F7")
    p_box.pack(fill=X, padx=50, pady=(0, 30))
    Label(p_box, text="🔒", font=("Arial", 12), bg="#F4F5F7").pack(side=LEFT, padx=(10, 5))
    txt_new_pass = Entry(p_box, font=("Arial", 12), bg="#F4F5F7", relief="flat", show="*")
    txt_new_pass.pack(side=LEFT, fill=X, expand=True, ipady=8)

    Button(card, text="Sign Up", font=("Arial", 12, "bold"), bg="#333333", fg="white", relief="flat", cursor="hand2", command=lambda: register_user(txt_new_user, txt_new_pass)).pack(fill=X, padx=50, ipady=10)
    Button(card, text="Already have an account? Log In", font=("Arial", 9), bg="#FFFFFF", fg="#00AA5B", relief="flat", cursor="hand2", command=show_login_screen).pack(pady=(20, 0))


def show_dashboard(active_user, role):
    clear_window()
    root.config(bg="#F4F5F7")
    
    # --- A. LEFT SIDEBAR (SCROLLABLE) ---
    sidebar_container = Frame(root, bg="#00AA5B", width=220)
    sidebar_container.pack(side=LEFT, fill=Y)
    sidebar_container.pack_propagate(False)

    side_canvas = Canvas(sidebar_container, bg="#00AA5B", highlightthickness=0)
    side_scroll = Scrollbar(sidebar_container, orient="vertical", command=side_canvas.yview)
    side_canvas.configure(yscrollcommand=side_scroll.set)
    
    side_scroll.pack(side=RIGHT, fill=Y)
    side_canvas.pack(side=LEFT, fill=BOTH, expand=True)

    sidebar = Frame(side_canvas, bg="#00AA5B")
    sidebar.bind("<Configure>", lambda e: side_canvas.configure(scrollregion=side_canvas.bbox("all")))
    side_canvas.create_window((0, 0), window=sidebar, anchor="nw", width=205) 

    # Sidebar Menu Items
    Label(sidebar, text="TradeLink", font=("Arial", 22, "bold"), bg="#00AA5B", fg="white").pack(pady=(20, 20))
    
    Label(sidebar, text="SHOPPING", font=("Arial", 9, "bold"), bg="#00AA5B", fg="#A7F3D0", anchor="w", padx=20).pack(fill=X, pady=(10, 5))
    Button(sidebar, text="🏠 Browse", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("Browse")).pack(fill=X, pady=2, ipady=5)
    Button(sidebar, text="🛒 My Cart", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("My Cart")).pack(fill=X, pady=2, ipady=5)
    Button(sidebar, text="❤️ Saved Items", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("Saved Items")).pack(fill=X, pady=2, ipady=5)

    Label(sidebar, text="SELLING", font=("Arial", 9, "bold"), bg="#00AA5B", fg="#A7F3D0", anchor="w", padx=20).pack(fill=X, pady=(20, 5))
    Button(sidebar, text="➕ Create Listing", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("Create Listing")).pack(fill=X, pady=2, ipady=5)
    Button(sidebar, text="📦 My Store", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("My Store")).pack(fill=X, pady=2, ipady=5)

    
    if role == "admin":
        Label(sidebar, text="ADMIN CONTROLS", font=("Arial", 9, "bold"), bg="#00AA5B", fg="#FFD700", anchor="w", padx=20).pack(fill=X, pady=(20, 5))
        Button(sidebar, text="🛡️ Manage Users", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("Manage Users")).pack(fill=X, pady=2, ipady=5)

    Label(sidebar, text="ACCOUNT", font=("Arial", 9, "bold"), bg="#00AA5B", fg="#A7F3D0", anchor="w", padx=20).pack(fill=X, pady=(20, 5))
    Button(sidebar, text="⚙️ Settings", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=lambda: dummy_button_click("Settings")).pack(fill=X, pady=2, ipady=5)
    Button(sidebar, text="🚪 Logout", font=("Arial", 11), bg="#00AA5B", fg="white", relief="flat", anchor="w", padx=20, command=confirm_logout).pack(fill=X, pady=(20, 20), ipady=10)


    #  B. MAIN DASHBOARD AREA 
    main = Frame(root, bg="#F4F5F7")
    main.pack(side=RIGHT, fill=BOTH, expand=True)

    header = Frame(main, bg="#FFFFFF", height=70)
    header.pack(fill=X)
    header.pack_propagate(False)
    Label(header, text=f"Welcome back, {active_user}!", font=("Arial", 14, "bold"), bg="#FFFFFF", fg="#333333").pack(side=LEFT, padx=30, pady=20)

    #  C. RESPONSIVE PRODUCT GRID 
    feed_container = Frame(main, bg="#F4F5F7")
    feed_container.pack(fill=BOTH, expand=True, padx=30, pady=20)
    Label(feed_container, text="Today's Picks", font=("Arial", 16, "bold"), bg="#F4F5F7", fg="#333333").pack(anchor="w", pady=(0, 10))


    feed_canvas = Canvas(feed_container, bg="#F4F5F7", highlightthickness=0)
    feed_scroll = Scrollbar(feed_container, orient="vertical", command=feed_canvas.yview)
    feed_canvas.configure(yscrollcommand=feed_scroll.set)
    
    feed_scroll.pack(side=RIGHT, fill=Y)
    feed_canvas.pack(side=LEFT, fill=BOTH, expand=True)

    feed = Frame(feed_canvas, bg="#F4F5F7")
    feed.bind("<Configure>", lambda e: feed_canvas.configure(scrollregion=feed_canvas.bbox("all")))
    canvas_frame_id = feed_canvas.create_window((0, 0), window=feed, anchor="nw")
    
    #  grid stretch horizontally when window is resized
    feed_canvas.bind('<Configure>', lambda e: feed_canvas.itemconfig(canvas_frame_id, width=e.width))

    # Mousewheel scrolling 
    feed_canvas.bind_all("<MouseWheel>", lambda e: feed_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    
    for i in range(4):
        feed.grid_columnconfigure(i, weight=1)

    
    row_num, col_num = 0, 0
    
    for item in products_db:
        card = Frame(feed, bg="#FFFFFF", width=220, height=260, highlightbackground="#E5E7EB", highlightthickness=1)
        card.grid(row=row_num, column=col_num, padx=10, pady=10, sticky="n")
        card.pack_propagate(False) 
        
       
        try:
            img_path = item.get("img_file", "")
            if img_path:
                card_img = PhotoImage(file=img_path)
                lbl_img = Label(card, image=card_img, bg="#FFFFFF")
                lbl_img.image = card_img # Stop Python from deleting the image from memory!
                lbl_img.pack(fill=X, pady=(10, 0))
            else:
                raise ValueError("No image path")
        except:
            
            lbl_img = Label(card, text="📷 No Image", bg="#E5E7EB", fg="#9CA3AF", font=("Arial", 10))
            lbl_img.pack(fill=X, ipady=40)
        
        Label(card, text=item["price"], font=("Arial", 14, "bold"), bg="#FFFFFF", fg="#00AA5B", anchor="w").pack(fill=X, padx=15, pady=(15, 0))
        Label(card, text=item["title"], font=("Arial", 11), bg="#FFFFFF", fg="#333333", anchor="w").pack(fill=X, padx=15, pady=(2, 0))
        Label(card, text="📍 " + item["loc"], font=("Arial", 9), bg="#FFFFFF", fg="#888888", anchor="w").pack(fill=X, padx=15, pady=(15, 0))
        
        
        col_num += 1
        if col_num > 3:
            col_num = 0
            row_num += 1

# Start the application
show_login_screen()
root.mainloop()