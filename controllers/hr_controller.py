from db_manager import DBManager

class HRController:
    def __init__(self):
        self.db = DBManager()

    def get_all_employees(self):
        return self.db.fetch_all("SELECT * FROM employees ORDER BY created_at DESC")

    def add_employee(self, name, position, salary, hire_date):
        query = "INSERT INTO employees (name, position, salary, hire_date) VALUES (%s, %s, %s, %s)"
        return self.db.execute_query(query, (name, position, salary, hire_date))

    def update_employee(self, emp_id, name, position, salary, hire_date):
        query = "UPDATE employees SET name=%s, position=%s, salary=%s, hire_date=%s WHERE id=%s"
        return self.db.execute_query(query, (name, position, salary, hire_date, emp_id))

    def delete_employee(self, emp_id):
        query = "DELETE FROM employees WHERE id=%s"
        return self.db.execute_query(query, (emp_id,))
