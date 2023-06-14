import os
import json

class Data:
    def __init__(self, filename):
        self.path_to_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        self.data = self.get_data_from_file()
    
    @property
    def next_id(self):
        max_id=max({value.get("id") for value in self.data})
        if not max_id:
            return 1
        return max_id + 1
    
    def rewrite_data_to_file(self):
        with open(self.path_to_data_file, encoding = 'utf-8', mode = 'w') as datafile: 
            datafile.write(json.dumps(self.data))
    
    def get_data_from_file(self):
        with open(self.path_to_data_file, encoding = 'utf-8', mode = 'r') as datafile:
            return json.loads(datafile.read())
    
    def find_record(self, conditions):
        def check_search_condition(record, conditions):
            for key, value in conditions.items():
                if record.get(key)!=value:
                    return False
            return True
        return [record for record in self.data if check_search_condition(record, conditions)]
    
    def update_record(self, record, update):
        idx = self.data.index(record)
        for key, value in update.items():
            if key != "id":
                record[key] = value
        self.data[idx] = record
        self.rewrite_data_to_file()
        return record.get("id")
    
    def add_record(self, record):
        record = {"id": self.next_id, **record}
        self.data.append(record)
        self.rewrite_data_to_file()
        return record.get("id") 
    
    def delete_record(self, record):
        self.data.remove(record)
        self.rewrite_data_to_file()
        return True
        
            
        


data = Data('data.json')
a = data.add_record({"first_name": "Alexander", "last_name": "Grushkin"})
b = data.add_record({"first_name": "Александр", "last_name": "Чушкин"})
c = data.add_record({"first_name": "Александр", "last_name": "Пушкин"})
d = data.find_record({"last_name":"Grushkin"})
data.update_record(d[0], {"first_name": "Эльмар"})
e = data.find_record({"first_name":"Эльмар"})
print(e)
data.delete_record(e[0])
print(e)
pass