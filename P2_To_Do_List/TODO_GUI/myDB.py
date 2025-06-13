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
            return 0  # Email already exists
        else:
            database[email] = [name, password]
            self._save_data(self.user_data_file, database)
            return 1  # Success

    def login_search(self, email, password):
        database = self._load_data(self.user_data_file)
        if email in database and database[email][1] == password:
            return 1  # Success
        return 0  # Invalid credentials

    def add_task(self, title, priority, description):
        database = self._load_data(self.tasks_data_file)
        if title in database:
            return 0  # Task already exists
        else:
            database[title] = [priority, description]
            self._save_data(self.tasks_data_file, database)
            return 1  # Task added successfully

    def get_tasks(self):
        return [{'title': title, 'priority': details[0], 'description': details[1]}
                for title, details in self._load_data(self.tasks_data_file).items()]
