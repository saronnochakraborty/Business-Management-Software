from db_manager import DBManager

class UserController:
    def __init__(self):
        self.db = DBManager()

    def get_all_users(self):
        return self.db.fetch_all("SELECT * FROM users ORDER BY created_at DESC")

    def add_user(self, username, password, role):
        query = "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)"
        return self.db.execute_query(query, (username, password, role))

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id=%s"
        return self.db.execute_query(query, (user_id,))
