import customtkinter as ctk
from controllers.hr_controller import HRController
from datetime import date

class HRView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = HRController()
        
        self.header = ctk.CTkLabel(self, text="HR & Payroll Management", font=ctk.CTkFont(size=24, weight="bold"))
        self.header.pack(pady=20)

        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.pack(pady=10, padx=20, fill="x")
        
        self.form_frame.grid_columnconfigure(0, weight=3)
        self.form_frame.grid_columnconfigure(1, weight=2)
        self.form_frame.grid_columnconfigure(2, weight=1)
        self.form_frame.grid_columnconfigure(3, weight=1)
        
        self.name_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Employee Name", height=40)
        self.name_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        self.pos_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Position", height=40)
        self.pos_entry.grid(row=0, column=1, padx=10, sticky="ew")
        
        self.salary_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Salary", height=40)
        self.salary_entry.grid(row=0, column=2, padx=10, sticky="ew")
        
        self.add_btn = ctk.CTkButton(self.form_frame, text="Add Employee", height=40, command=self.add_employee, fg_color="#2CC985", hover_color="#229965")
        self.add_btn.grid(row=0, column=3, padx=(10, 0), sticky="ew")

        self.list_frame = ctk.CTkScrollableFrame(self)
        self.list_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
            
        headers = ["ID", "Name", "Position", "Salary", "Hire Date", "Actions"]
        header_frame = ctk.CTkFrame(self.list_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=5)
        
        for h in headers:
            ctk.CTkLabel(header_frame, text=h, width=100, anchor="w").pack(side="left", padx=5)

        employees = self.controller.get_all_employees()
        for emp in employees:
            row = ctk.CTkFrame(self.list_frame)
            row.pack(fill="x", pady=2)
            
            ctk.CTkLabel(row, text=str(emp['id']), width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=emp['name'], width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=emp['position'], width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=f"₹{emp['salary']}", width=100, anchor="w").pack(side="left", padx=5)
            ctk.CTkLabel(row, text=str(emp['hire_date']), width=100, anchor="w").pack(side="left", padx=5)
            
            del_btn = ctk.CTkButton(row, text="Delete", width=60, fg_color="red", 
                                  command=lambda i=emp['id']: self.delete_employee(i))
            del_btn.pack(side="left", padx=5)

    def add_employee(self):
        name = self.name_entry.get()
        pos = self.pos_entry.get()
        salary = self.salary_entry.get()
        
        if name and pos and salary:
            today = date.today()
            if self.controller.add_employee(name, pos, float(salary), today):
                self.name_entry.delete(0, 'end')
                self.pos_entry.delete(0, 'end')
                self.salary_entry.delete(0, 'end')
                self.refresh_list()

    def delete_employee(self, emp_id):
        if self.controller.delete_employee(emp_id):
            self.refresh_list()
