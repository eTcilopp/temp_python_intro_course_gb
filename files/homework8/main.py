from models import Data

def run(**kwargs):
    data = kwargs.get('data')
    
    # Добавление записей
    entry = {"first_name": "Alexander", "last_name": "Grushkin"}
    data.add_record(entry)
    data.add_record({"first_name": "Александр", "last_name": "Чушкин"})
    data.add_record({"first_name": "Александр", "last_name": "Пушкин"})
    
    # Поиск записей
    f = data.find_record({"id":2})
    
    # Изменение записей
    data.update_record(f[0], {"first_name": "Эльмар"})
    
    e = data.find_record({"first_name":"Эльмар"})
    assert e[0].get("id") == 2  # проверка: данные обновились
    
    # Удаление записей
    data.delete_record(e[0])
    e = data.find_record({"id":2})
    assert len(e) == 0  # проверка: данные удалены


if __name__ == '__main__':
    datafile_name = 'data.json'
    run(data=Data(datafile_name))