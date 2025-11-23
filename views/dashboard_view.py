import customtkinter as ctk
from controllers.dashboard_controller import DashboardController

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = DashboardController()
        
        self.header = ctk.CTkLabel(self, text="Dashboard", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(pady=20)

        self.stats_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.stats_frame.pack(pady=20, padx=20, fill="x")

        self.refresh_list()

    def refresh_list(self):
        for widget in self.stats_frame.winfo_children():
            widget.destroy()


        self.create_card("Total Sales", f"₹{self.controller.get_total_sales():.2f}", 0, 0)
        self.create_card("Low Stock Items", str(self.controller.get_low_stock_count()), 0, 1)
        self.create_card("Total Employees", str(self.controller.get_total_employees()), 0, 2)
        
        self.create_card("Total Users", str(self.controller.get_total_users()), 1, 0)
        self.create_card("Inventory Value", f"₹{self.controller.get_total_inventory_value():.2f}", 1, 1)
        self.create_card("Total Items in Stock", str(self.controller.get_total_stock_quantity()), 1, 2)

    def create_card(self, title, value, row, col):
        card = ctk.CTkFrame(self.stats_frame, corner_radius=15, fg_color=("white", "gray20"), border_width=1, border_color=("gray80", "gray30"))
        card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
        
        self.stats_frame.grid_columnconfigure(col, weight=1)
        
        title_label = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=14, weight="bold"), text_color=("gray40", "gray70"))
        title_label.pack(pady=(20, 5), padx=20, anchor="w")
        
        value_label = ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=28, weight="bold"), text_color=("blue", "#3B8ED0"))
        value_label.pack(pady=(0, 20), padx=20, anchor="w")
