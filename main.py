from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("System Login")
root.geometry("400x300")
root.config(bg="#f4f4f9") 


def validate_login():
    user = txt_username.get()
    pwd = txt_password.get()
    
    
    if user == "admin" and pwd == "admin123":
        messagebox.showinfo("Success", "Login successful! Routing to dashboard...")
        
    else:
        messagebox.showerror("Error", "Invalid credentials. Please try again.")

# --- UI Layout ---

form_frame = Frame(root, bg="#f4f4f9")
form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Title 
lbl_title = Label(form_frame, text="System Login", font=("Arial", 16, "bold"), bg="#f4f4f9")
lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Username 
lbl_username = Label(form_frame, text="Username:", font=("Arial", 10), bg="#f4f4f9")
lbl_username.grid(row=1, column=0, pady=5, sticky=E)

txt_username = Entry(form_frame, width=25, font=("Arial", 10))
txt_username.grid(row=1, column=1, pady=5, padx=10)

# Password Label & Input (Using show="*" to hide characters)
lbl_password = Label(form_frame, text="Password:", font=("Arial", 10), bg="#f4f4f9")
lbl_password.grid(row=2, column=0, pady=5, sticky=E)

txt_password = Entry(form_frame, width=25, font=("Arial", 10), show="*")
txt_password.grid(row=2, column=1, pady=5, padx=10)

# Submit Button
btn_login = Button(form_frame, text="Login", command=validate_login, 
                   bg="#1A1851", fg="white", font=("Arial", 10, "bold"), width=15)
btn_login.grid(row=3, column=0, columnspan=2, pady=25)

# Run the application
root.mainloop()