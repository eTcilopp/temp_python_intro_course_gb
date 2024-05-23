import csv
import os

__all__ = ['get_files_in_current_cwd', 'read_csv_file', 'copy_csv_file', 'read_csv_file_as_dict']
 

def get_files_in_current_cwd():
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    return files


def read_csv_file(file_path: str):
    with open(file_path, 'r', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            yield row


def copy_csv_file(file_path: str, new_file_path: str):
    try:
        with (
            open(file_path, 'r', newline='') as f_read,
            open(new_file_path, 'w', newline='', encoding='utf-8') as f_write
        ):
            csvreader = csv.reader(f_read)
            csvwriter = csv.writer(
                f_write, dialect='excel',
                quoting=csv.QUOTE_MINIMAL, delimiter=' ',
                quotechar='|'
            )
            all_data = []
            for row in csvreader:
                all_data.append(row)
            csvwriter.writerows(all_data)
        return True
    except Exception:
        return False


def read_csv_file_as_dict(file_path: str):
    with open(file_path, 'r', newline='') as f:
        csv_file_dict = csv.DictReader(f, fieldnames=["name", "gender", "age"], restkey="new", restval="Main office")

    return csv_file_dict
