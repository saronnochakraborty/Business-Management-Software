import customtkinter as ctk
from controllers.inventory_controller import InventoryController

class InventoryView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = InventoryController()
        
        self.header = ctk.CTkLabel(self, text="Inventory Management", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(pady=20)

        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.pack(pady=10, padx=20, fill="x")
        

        self.form_frame.grid_columnconfigure(0, weight=3)
        self.form_frame.grid_columnconfigure(1, weight=1)
        self.form_frame.grid_columnconfigure(2, weight=1)
        self.form_frame.grid_columnconfigure(3, weight=1)

        self.name_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Item Name", height=40)
        self.name_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        self.qty_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Quantity", width=100, height=40)
        self.qty_entry.grid(row=0, column=1, padx=10, sticky="ew")
        
        self.price_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Price", width=100, height=40)
        self.price_entry.grid(row=0, column=2, padx=10, sticky="ew")
        
        self.add_btn = ctk.CTkButton(self.form_frame, text="Add Item", height=40, command=self.add_item, fg_color="#2CC985", hover_color="#229965")
        self.add_btn.grid(row=0, column=3, padx=(10, 0), sticky="ew")

        self.list_frame = ctk.CTkScrollableFrame(self)
        self.list_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
            
        headers = ["ID", "Name", "Quantity", "Price", "Actions"]
        header_frame = ctk.CTkFrame(self.list_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=5)
        
        for h in headers:
            ctk.CTkLabel(header_frame, text=h, width=100, anchor="w").pack(side="left", padx=5)

        items = self.controller.get_all_items()
        for item in items:
            row = ctk.CTkFrame(self.list_frame)
            row.pack(fill="x", pady=2)
            
            ctk.CTkLabel(row, text=str(item['id']), width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=item['name'], width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=str(item['quantity']), width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=f"₹{item['price']}", width=100, anchor="w").pack(side="left", padx=5)
            
            del_btn = ctk.CTkButton(row, text="Delete", width=60, fg_color="red", 
                                  command=lambda i=item['id']: self.delete_item(i))
            del_btn.pack(side="left", padx=5)

    def add_item(self):
        name = self.name_entry.get()
        qty = self.qty_entry.get()
        price = self.price_entry.get()
        
        if name and qty and price:
            if self.controller.add_item(name, "", int(qty), float(price)):
                self.name_entry.delete(0, 'end')
                self.qty_entry.delete(0, 'end')
                self.price_entry.delete(0, 'end')
                self.refresh_list()

    def delete_item(self, item_id):
        if self.controller.delete_item(item_id):
            self.refresh_list()
