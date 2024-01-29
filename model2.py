import numpy as np
import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
from keras.models import Sequential, load_model
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os
import pefile
from capstone import *
import docx2txt
import pickle

nltk.download('punkt')
nltk.download('words')
english_words = set(words.words())

def load_dictionary(dictionary_path):
    encodings = ['utf-8', 'windows-1256']
    dictionary_words = []
    for encoding in encodings:
        try:
            with open(dictionary_path, 'r', encoding=encoding) as f:
                dictionary_words = set(word.replace('غغغ', ' ').rstrip() for word in f.read().splitlines())
            break
        except UnicodeDecodeError:
            continue
    return dictionary_words

def disassemble(file_path):
    pe = pefile.PE(file_path)
    eop = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    code_section = pe.get_section_by_rva(eop)
    code_dump = code_section.get_data(eop, pe.OPTIONAL_HEADER.SizeOfCode)
    cs = Cs(CS_ARCH_X86, CS_MODE_32)
    assembly_code = "\n".join(f"{i.mnemonic} {i.op_str}" for i in cs.disasm(code_dump, 0x1000))
    return assembly_code

def read_txt(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return text

def read_docx(file_path):
    text = docx2txt.process(file_path)
    return text

# Load Persian dictionary
persian_words = load_dictionary('persian_words.txt')  # Replace with your dictionary path

# Combine English and Persian words
all_words = english_words.union(persian_words)

# Tokenize the words
tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_words)
sequences = tokenizer.texts_to_sequences(all_words)

# Save the tokenizer
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Prepare the data for the LSTM
X = []
y = []
for i in range(1, len(sequences)):
    X.append(sequences[i-1])
    y.append(sequences[i])
X = pad_sequences(X)
y = pad_sequences(y, maxlen=1)  # Ensure all sequences in y have the same length

# Define the LSTM model
model = Sequential()
model.add(Embedding(input_dim=len(all_words)+1, output_dim=64, input_length=X.shape[1]))
model.add(LSTM(64))
model.add(Dense(len(all_words)+1, activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(X, y, epochs=10, verbose=1)

# Save the model
model.save('your_model.h5')  # Replace with your model path

# Determine the file type and read the file accordingly
file_path = "farsi-text.txt"  # Replace with your file path
file_extension = os.path.splitext(file_path)[1]
if file_extension == '.exe':
    text = disassemble(file_path)
elif file_extension == '.txt':
    text = read_txt(file_path)
elif file_extension == '.docx':
    text = read_docx(file_path)
else:
    print(f"Unsupported file type: {file_extension}")
    text = ""

# Tokenize the textg
sequences = tokenizer.texts_to_sequences([text])

# Prepare the data for the LSTM
X = []
for i in range(1, len(sequences)):
    X.append(sequences[i-1])
X = pad_sequences(X)

# Make a prediction
predictions = model.predict(X)
