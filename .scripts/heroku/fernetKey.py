from cryptography.fernet import Fernet
import sys
import os
dir_prefix = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
filename = 'airflow_key.txt'

if filename not in os.listdir(dir_prefix + '/.config'):
    key = Fernet.generate_key()

    # Load into file
    with open(dir_prefix + f'/.config/{filename}', 'wb') as file:
        file.write(key)
else:
    with open(dir_prefix + f'/.config/{filename}', 'rb') as file:
        key = file.read()

# Return key
print(f'{key.decode()}')