import customtkinter as ctk
from db_manager import DBManager
from auth import LoginWindow
import os

class BusinessApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Business Management System")
        self.geometry("1200x800")
        
        self.db = DBManager()
        if not self.db.connect():
            print("Failed to connect to database. Please check your configuration.")
        
        self.show_login()

    def show_login(self):
        self.withdraw() 
        self.login_window = LoginWindow(self)

    def show_main_dashboard(self, user_role):
        self.deiconify() 
        self.user_role = user_role
        self.setup_ui()

    def setup_ui(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="BizManager", font=ctk.CTkFont(size=26, weight="bold"))
        self.logo_label.pack(padx=20, pady=(30, 20))

        self.nav_buttons = {}
        modules = ["Dashboard", "Inventory", "Sales", "HR", "Users"]
        
        for module in modules:
            btn = ctk.CTkButton(self.sidebar, text=module, height=40, corner_radius=10,
                              font=ctk.CTkFont(size=14),
                              fg_color="transparent", text_color=("gray10", "gray90"),
                              hover_color=("gray70", "gray30"),
                              anchor="w",
                              command=lambda m=module: self.show_module(m))
            btn.pack(pady=5, padx=15, fill="x")
            self.nav_buttons[module] = btn

        self.content_area = ctk.CTkFrame(self, corner_radius=0)
        self.content_area.pack(side="right", fill="both", expand=True)
        
        self.views = {}
        
        self.show_module("Dashboard")

    def show_module(self, module_name):

        for name, btn in self.nav_buttons.items():
            if name == module_name:
                btn.configure(fg_color=("gray75", "gray25"), text_color=("black", "white"))
            else:
                btn.configure(fg_color="transparent", text_color=("gray10", "gray90"))


        for view in self.views.values():
            view.pack_forget()


        if module_name in self.views:
            view = self.views[module_name]
            view.pack(fill="both", expand=True)
            

            if hasattr(view, 'refresh_list'):
                view.refresh_list()
            elif hasattr(view, 'refresh_products'):
                view.refresh_products()

            
        else:
            if module_name == "Dashboard":
                from views.dashboard_view import DashboardView
                view = DashboardView(self.content_area)
            elif module_name == "Inventory":
                from views.inventory_view import InventoryView
                view = InventoryView(self.content_area)
            elif module_name == "Sales":
                from views.sales_view import SalesView
                view = SalesView(self.content_area)
            elif module_name == "HR":
                from views.hr_view import HRView
                view = HRView(self.content_area)
            elif module_name == "Users":
                from views.user_view import UserView
                view = UserView(self.content_area)
            else:
                return

            self.views[module_name] = view
            view.pack(fill="both", expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = BusinessApp()
    app.mainloop()
