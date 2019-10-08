import pandas as pd
import os

#run to remove first useless columns
direc=os.fsencode('.')
for File in os.listdir(direc):
    filename=os.fsdecode(File)
    if filename.endswith('.csv'):
        df=pd.read_csv(filename)
        keep_col=[i for i in df.columns if (i and 'Unnamed' not in i)]
        new_f=df[keep_col]
        new_f.to_csv(filename,index=False)
'''
#run to check number of columns
direc=os.fsencode('.')
for File in os.listdir(direc):
    filename=os.fsdecode(File)
    if filename.endswith('.csv'):
        df=pd.read_csv(filename)
        print(filename,len(df.columns))
'''
