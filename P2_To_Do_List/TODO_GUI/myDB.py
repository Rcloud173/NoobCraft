import json
import os

class Database:
    def __init__(self):
        self.user_data_file = 'user_data.json'
        self.tasks_data_file = 'tasks_data.json'

    def _load_data(self, filename):
        if not os.path.exists(filename):
            return {}
        with open(filename, 'r') as file:
            return json.load(file)

    def _save_data(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def add_user_data(self, name, email, password):
        database = self._load_data(self.user_data_file)
        if email in database:
            return 0
        else:
            database[email] = [name, password]
            self._save_data(self.user_data_file, database)
            return 1

    def login_search(self, email, password):
        database = self._load_data(self.user_data_file)
        if email in database and database[email][1] == password:
            return 1
        return 0

    def add_task(self, user_email, title, priority, description):
        database = self._load_data(self.tasks_data_file)
        if user_email not in database:
            database[user_email] = []

        database[user_email].append({
            'title': title,
            'priority': priority,
            'description': description
        })

        self._save_data(self.tasks_data_file, database)
        return 1

    def get_tasks(self, user_email):
        database = self._load_data(self.tasks_data_file)
        return database.get(user_email, [])

    def update_task(self, user_email, task_index, title, priority, description):
        database = self._load_data(self.tasks_data_file)
        if user_email in database and 0 <= task_index < len(database[user_email]):
            database[user_email][task_index] = {
                'title': title,
                'priority': priority,
                'description': description
            }
            self._save_data(self.tasks_data_file, database)
            return 1
        return 0
    
    def delete_task(self, user_email, task_index):
        database = self._load_data(self.tasks_data_file)
        if user_email in database and 0 <= task_index < len(database[user_email]):
            del database[user_email][task_index]
            self._save_data(self.tasks_data_file, database)
            return 1
        return 0

    def mark_task_done(self, user_email, task_index):
        database = self._load_data(self.tasks_data_file)
        if user_email in database and 0 <= task_index < len(database[user_email]):
            database[user_email][task_index]['priority'] = 'done ✅'
            self._save_data(self.tasks_data_file, database)
            return 1
        return 0

