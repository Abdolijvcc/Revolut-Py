import os
import fnmatch
import json

def find_and_open_json(folder_path, filename_to_find):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if fnmatch.fnmatch(file, filename_to_find):
                file_path = os.path.join(root, file)
                print(f"Found JSON file: {file_path}")
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    print("JSON content:")
                    print(json.dumps(data, indent=4))
                return data
    print("JSON file not found.")
    return None

# Example usage
def main():
    folder = 'data'
    nombre = input('Ingresar nombre: ')
    apellido = input('Ingresar apellido: ')
    filename = f"{nombre}_{apellido}.json"
    find_and_open_json(folder, filename)

if __name__ == "__main__":
    main()    
