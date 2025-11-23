from db_manager import DBManager

class SalesController:
    def __init__(self):
        self.db = DBManager()

    def create_sale(self, user_id, total_amount, items):
        sale_query = "INSERT INTO sales (user_id, total_amount) VALUES (%s, %s)"
        sale_id = self.db.execute_query(sale_query, (user_id, total_amount))
        
        if not sale_id:
            return False

        item_query = "INSERT INTO sale_items (sale_id, product_id, quantity, price_at_sale) VALUES (%s, %s, %s, %s)"
        stock_query = "UPDATE inventory SET quantity = quantity - %s WHERE id = %s"

        for item in items:
            self.db.execute_query(item_query, (sale_id, item['product_id'], item['quantity'], item['price']))
            self.db.execute_query(stock_query, (item['quantity'], item['product_id']))
            
        return True

    def get_all_sales(self):
        return self.db.fetch_all("SELECT s.id, u.username, s.total_amount, s.created_at FROM sales s LEFT JOIN users u ON s.user_id = u.id ORDER BY s.created_at DESC")
