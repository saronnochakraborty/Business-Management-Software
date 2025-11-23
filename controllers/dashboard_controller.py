from db_manager import DBManager

class DashboardController:
    def __init__(self):
        self.db = DBManager()

    def get_total_sales(self):
        result = self.db.fetch_one("SELECT SUM(total_amount) as total FROM sales")
        return result['total'] if result and result['total'] else 0.0

    def get_low_stock_count(self, threshold=5):
        result = self.db.fetch_one("SELECT COUNT(*) as count FROM inventory WHERE quantity < %s", (threshold,))
        return result['count'] if result else 0

    def get_total_employees(self):
        result = self.db.fetch_one("SELECT COUNT(*) as count FROM employees")
        return result['count'] if result else 0

    def get_total_users(self):
        result = self.db.fetch_one("SELECT COUNT(*) as count FROM users")
        return result['count'] if result else 0

    def get_total_inventory_value(self):
        result = self.db.fetch_one("SELECT SUM(quantity * price) as total_value FROM inventory")
        return result['total_value'] if result and result['total_value'] else 0.0

    def get_total_stock_quantity(self):
        result = self.db.fetch_one("SELECT SUM(quantity) as total_qty FROM inventory")
        return result['total_qty'] if result and result['total_qty'] else 0
