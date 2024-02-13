import os
import pandas as pd

def remodel(df: pd.DataFrame):
    _2M, _2A, _3M, _3A, _1M, _1A = [], [], [], [], [], []
    for index, row in df.iterrows():
        if '2M-2A' in row and isinstance(row['2M-2A'], str):
            _2M.append(int(row['2M-2A'].split('-')[0]))
            _2A.append(int(row['2M-2A'].split('-')[1]))
        if '3M-3A' in row and isinstance(row['3M-3A'], str):
            _3M.append(int(row['3M-3A'].split('-')[0]))
            _3A.append(int(row['3M-3A'].split('-')[1]))
        if '1M-1A' in row and isinstance(row['1M-1A'], str):
            _1M.append(int(row['1M-1A'].split('-')[0]))
            _1A.append(int(row['1M-1A'].split('-')[1]))
        try:
            if 'FG%' in row:
                df.at[index, 'FG%'] = float(row['FG%'].rstrip('%'))
            else:
                df.at[index, 'FG%'] = 0
        except:
            df.at[index, 'FG%'] = 0
        try:
            if '1%' in row:
                df.at[index, '1%'] = float(row['1%'].rstrip('%'))
            else:
                df.at[index, '1%'] = 0
        except:
            df.at[index, '1%'] = 0
    df.insert(3, '2M', _2M)
    df.insert(4, '2A', _2A)
    df.insert(5, '3M', _3M)
    df.insert(6, '3A', _3A)
    df.insert(7, '1M', _1M)
    df.insert(8, '1A', _1A) 



# Load data and preprocess
dir = "./1_Data_Collection/datasets/game_data/"
directory = os.fsencode(dir)
print(os.listdir(directory))

for file in os.listdir(directory)[1:-1]:
    filename = os.fsdecode(file)
    if filename.endswith(".csv"):
        print(filename)
        data = pd.read_csv(dir+filename)
        remodel(data)
        data = data.drop(columns=["1M-1A", "2M-2A", "3M-3A"], axis=1)
        data.to_csv(dir+filename, index=False)
        print("Preprocessing complete for file " + filename + "." + "\n")
    else:
        continue