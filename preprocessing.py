import os
import pandas as pd
from collections import Counter

# specify the directory you want to scan
directory = 'dictionary-files'

# initialize a counter
char_counter = Counter()

# iterate over all files in the directory
for filename in os.listdir(directory):
    # construct the full file path
    filepath = os.path.join(directory, filename)
    try:
        # open the file in binary mode and read its contents
        with open(filepath, 'rb') as file:
            contents = file.read()
        # update the counter with the bytes in this file
        char_counter.update(contents)
    except Exception as e:
        print(f"Could not read file {filepath} due to {str(e)}")

# convert the counter to a DataFrame
df = pd.DataFrame.from_dict(char_counter, orient='index').reset_index()
df.columns = ['Byte', 'Frequency']

# add a column for the character representation of each byte
df['Character'] = df['Byte'].apply(lambda x: chr(x) if 32 <= x <= 126 else '')
# def check_char(string):


# save the DataFrame to an Excel file
# df.to_excel('byte_frequencies.xlsx', index=False)
