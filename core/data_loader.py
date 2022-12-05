import os

folder_file_path = "../Data"


def load_data(file_name: str) -> str:
    data_file_path = os.path.join(folder_file_path, file_name)
    with open(data_file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data
