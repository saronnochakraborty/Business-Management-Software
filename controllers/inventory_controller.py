from db_manager import DBManager

class InventoryController:
    def __init__(self):
        self.db = DBManager()

    def get_all_items(self):
        return self.db.fetch_all("SELECT * FROM inventory ORDER BY created_at DESC")

    def add_item(self, name, description, quantity, price):
        query = "INSERT INTO inventory (name, description, quantity, price) VALUES (%s, %s, %s, %s)"
        return self.db.execute_query(query, (name, description, quantity, price))

    def update_item(self, item_id, name, description, quantity, price):
        query = "UPDATE inventory SET name=%s, description=%s, quantity=%s, price=%s WHERE id=%s"
        return self.db.execute_query(query, (name, description, quantity, price, item_id))

    def delete_item(self, item_id):
        query = "DELETE FROM inventory WHERE id=%s"
        return self.db.execute_query(query, (item_id,))
