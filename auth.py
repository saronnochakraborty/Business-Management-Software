import customtkinter as ctk
from db_manager import DBManager

class LoginWindow(ctk.CTkToplevel):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.title("Login")
        self.geometry("400x300")
        self.resizable(False, False)
        
        self.db = DBManager()

        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self.frame, text="Login", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(pady=20)

        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Username")
        self.username_entry.pack(pady=10, padx=20, fill="x")

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10, padx=20, fill="x")

        self.login_button = ctk.CTkButton(self.frame, text="Login", command=self.login)
        self.login_button.pack(pady=20, padx=20, fill="x")
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        query = "SELECT * FROM users WHERE username = %s AND password_hash = %s"
        user = self.db.fetch_one(query, (username, password))

        if user:
            print(f"Login successful for {username}")
            self.app.show_main_dashboard(user['role'])
            self.destroy()
        else:
            print("Login failed")
            error_label = ctk.CTkLabel(self.frame, text="Invalid credentials", text_color="red")
            error_label.pack()

    def on_close(self):
        self.app.destroy()
