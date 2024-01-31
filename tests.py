import random

random.randint(1,5)

print(random.randint(1,5))
import string

[''.join(random.choices(string.ascii_letters, k=random.randint(1,7))) for _ in range(2)]

random_strings_complex = [''.join(random.choices(string.ascii_letters + string.digits + '@#%&*', k=random.randint(1,15))) for _ in range(2)]

persian_words = set(read_file_as_text('/content/drive/MyDrive/TextPlainDetector/persian_words.txt', ['utf-8', 'windows-1256']).replace('غغغ', ' ').split())
