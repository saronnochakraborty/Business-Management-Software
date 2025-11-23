import customtkinter as ctk
from controllers.sales_controller import SalesController
from controllers.inventory_controller import InventoryController

class SalesView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.sales_controller = SalesController()
        self.inventory_controller = InventoryController()
        self.cart = []
        
        self.header = ctk.CTkLabel(self, text="Sales / POS", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(pady=20)

        self.main_layout = ctk.CTkFrame(self, fg_color="transparent")
        self.main_layout.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.left_panel = ctk.CTkFrame(self.main_layout)
        self.left_panel.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        ctk.CTkLabel(self.left_panel, text="Available Products", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        
        self.product_list = ctk.CTkScrollableFrame(self.left_panel)
        self.product_list.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.right_panel = ctk.CTkFrame(self.main_layout, width=300)
        self.right_panel.pack(side="right", fill="y")
        
        ctk.CTkLabel(self.right_panel, text="Cart", font=ctk.CTkFont(weight="bold")).pack(pady=10)
        
        self.cart_frame = ctk.CTkScrollableFrame(self.right_panel)
        self.cart_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.total_label = ctk.CTkLabel(self.right_panel, text="Total: ₹0.00", font=ctk.CTkFont(size=18, weight="bold"))
        self.total_label.pack(pady=10)
        
        self.checkout_btn = ctk.CTkButton(self.right_panel, text="Checkout", height=50, font=ctk.CTkFont(size=16, weight="bold"), command=self.checkout, fg_color="#2CC985", hover_color="#229965")
        self.checkout_btn.pack(pady=20, padx=10, fill="x")

        self.refresh_products()

    def refresh_products(self):
        for widget in self.product_list.winfo_children():
            widget.destroy()
            
        items = self.inventory_controller.get_all_items()
        for item in items:
            if item['quantity'] > 0:
                btn = ctk.CTkButton(self.product_list, 
                                  text=f"{item['name']} - ₹{item['price']} ({item['quantity']} in stock)",
                                  height=40,
                                  fg_color="transparent", border_width=1, border_color="gray50",
                                  text_color=("gray10", "gray90"),
                                  anchor="w",
                                  command=lambda i=item: self.add_to_cart(i))
                btn.pack(pady=5, padx=5, fill="x")

    def add_to_cart(self, item):
        found = False
        for cart_item in self.cart:
            if cart_item['product_id'] == item['id']:
                if cart_item['quantity'] < item['quantity']:
                    cart_item['quantity'] += 1
                found = True
                break
        
        if not found:
            self.cart.append({
                'product_id': item['id'],
                'name': item['name'],
                'price': float(item['price']),
                'quantity': 1,
                'max_qty': item['quantity']
            })
            
        self.update_cart_ui()

    def update_cart_ui(self):
        for widget in self.cart_frame.winfo_children():
            widget.destroy()
            
        total = 0
        for item in self.cart:
            item_total = item['price'] * item['quantity']
            total += item_total
            
            frame = ctk.CTkFrame(self.cart_frame)
            frame.pack(fill="x", pady=2)
            
            ctk.CTkLabel(frame, text=f"{item['name']} x{item['quantity']}", anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(frame, text=f"₹{item_total:.2f}", anchor="e").pack(side="right", padx=5)
            
        self.total_label.configure(text=f"Total: ₹{total:.2f}")

    def checkout(self):
        if not self.cart:
            return
            
        total = sum(item['price'] * item['quantity'] for item in self.cart)
        if self.sales_controller.create_sale(1, total, self.cart):
            self.cart = []
            self.update_cart_ui()
            self.refresh_products()
            print("Checkout successful")
