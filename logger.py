import json
from datetime import datetime

class JSONLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logs = self.load_logs()

    def load_logs(self):
        try:
            with open(self.log_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def log(self, message):
        self.logs = self.load_logs()
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'message': message
        }
        self.logs.append(log_entry)

    def save_logs(self):
        with open(self.log_file, 'w') as file:
            json.dump(self.logs, file, indent=4)