import os
import re

def extract_affinity_from_log(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            if line.strip().startswith('1 '):
                parts = line.split()
                if len(parts) >= 2:
                    return parts[1]
    return None

def get_sort_key(filename):
    # Извлекаем числовой префикс из имени файла (часть до первого подчеркивания)
    match = re.match(r'(\d+)', filename)
    if match:
        return int(match.group(1))
    return 0

def main():
    # Получаем список всех файлов в текущей директории
    files = os.listdir()
    
    # Фильтруем только файлы логов и сортируем по числовому префиксу
    log_files = sorted(
        [f for f in files if f.endswith('_log.log')],
        key=get_sort_key
    )
    
    print("ID\tAffinity (kcal/mol)")
    print("----------------------")
    
    for log_file in log_files:
        # Извлекаем основной ID (цифры после подчеркивания)
        main_id = re.search(r'_(\d+)\.pdbqt_log', log_file)
        if main_id:
            main_id = main_id.group(1)
        else:
            main_id = "N/A"
        
        # Получаем значение аффинности
        affinity = extract_affinity_from_log(log_file)
        
        if affinity:
            print(f"{main_id}\t{affinity}")
        else:
            print(f"{main_id}\tNot found")

if __name__ == "__main__":
    main()