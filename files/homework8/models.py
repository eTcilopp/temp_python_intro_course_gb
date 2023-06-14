import os
import json

class Data:
    def __init__(self, filename):
        self.data = self.get_data_from_file(filename)
    
    def get_data_from_file(self, filename):
        filename_with_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        with open(filename_with_path, encoding = 'utf-8', mode = 'r') as datafile:
            return json.loads(datafile.read())
    
    def get_record(self, conditions: dict):
        def check_condition(record, conditions):
            for key, value in conditions.items():
                if record.get(key)!=value:
                    return False
            return True
        
        return [record for record in self.data if check_condition(record, conditions)]


data = Data('data.json')
a = data.get_record({"first_name": "Александр"})
b = data.get_record({"first_name": "Александр", "last_name": "Чушкин"})
c = data.get_record({"first_name": "Александр", "last_name": "Пушкин"})
pass