import os
import pandas as pd

allfiles = os.listdir()

num_of_lines = {}

def funca(file):
    fa = open(file, "r")
    n = len(fa.readlines())
    fa.close()
    return n


for filename in allfiles:
    if filename[-4:] == '.txt':
        num_of_lines[filename] = funca(filename)

dfa = pd.DataFrame(num_of_lines.items())
dfa.columns = ['name of file', 'num of lines']
print(dfa)

dfa.to_excel("data.xlsx", index=False)

# openpyxl
# pandas
