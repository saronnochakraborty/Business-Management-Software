import customtkinter as ctk
from controllers.user_controller import UserController

class UserView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = UserController()
        
        self.header = ctk.CTkLabel(self, text="User Management", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(pady=20)

        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.pack(pady=10, padx=20, fill="x")
        
        self.form_frame.grid_columnconfigure(0, weight=2)
        self.form_frame.grid_columnconfigure(1, weight=2)
        self.form_frame.grid_columnconfigure(2, weight=1)
        self.form_frame.grid_columnconfigure(3, weight=1)
        
        self.username_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Username", height=40)
        self.username_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        self.password_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Password", show="*", height=40)
        self.password_entry.grid(row=0, column=1, padx=10, sticky="ew")
        
        self.role_var = ctk.StringVar(value="staff")
        self.role_menu = ctk.CTkOptionMenu(self.form_frame, values=["admin", "manager", "staff"], variable=self.role_var, height=40)
        self.role_menu.grid(row=0, column=2, padx=10, sticky="ew")
        
        self.add_btn = ctk.CTkButton(self.form_frame, text="Add User", height=40, command=self.add_user, fg_color="#2CC985", hover_color="#229965")
        self.add_btn.grid(row=0, column=3, padx=(10, 0), sticky="ew")

        self.list_frame = ctk.CTkScrollableFrame(self)
        self.list_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
            
        headers = ["ID", "Username", "Role", "Created At", "Actions"]
        header_frame = ctk.CTkFrame(self.list_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=5)
        
        for h in headers:
            ctk.CTkLabel(header_frame, text=h, width=100, anchor="w").pack(side="left", padx=5)

        users = self.controller.get_all_users()
        for user in users:
            row = ctk.CTkFrame(self.list_frame)
            row.pack(fill="x", pady=2)
            
            ctk.CTkLabel(row, text=str(user['id']), width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=user['username'], width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=user['role'], width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=str(user['created_at']), width=100, anchor="w").pack(side="left", padx=5)
            
            del_btn = ctk.CTkButton(row, text="Delete", width=60, fg_color="red", 
                                  command=lambda i=user['id']: self.delete_user(i))
            del_btn.pack(side="left", padx=5)

    def add_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        
        if username and password:
            if self.controller.add_user(username, password, role):
                self.username_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                self.refresh_list()

    def delete_user(self, user_id):
        if self.controller.delete_user(user_id):
            self.refresh_list()
