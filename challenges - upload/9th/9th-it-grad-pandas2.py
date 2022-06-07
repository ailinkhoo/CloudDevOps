import os
import pandas as pd
import shutil
import glob

os.system(f"wget {'https://data.gov.sg/dataset/f6048a81-0f7b-436c-8bfa-ebe1bb42cfdc/download'} -O {'polygrad.zip'}") # download the zip file and extract
os.system(f"wget {'https://data.gov.sg/dataset/249f1149-1e04-40e2-81c6-bfab3bba5574/download'} -O {'unigrad.zip'}")
shutil.unpack_archive('polygrad.zip') # https://www.geeksforgeeks.org/python-shutil-unpack_archive-method/
shutil.unpack_archive('unigrad.zip')

file = [] # make an empty list 
path = "./*.csv" # https://stackoverflow.com/questions/14262405/loop-through-all-csv-files-in-a-folder
for fname in glob.glob(path): # check for filenames and store in list
    file.append(fname)
    
df = pd.concat(map(pd.read_csv, [file[0], file[1]]), ignore_index=True) # combine two dataframe into one (https://www.tutorialspoint.com/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe)

df.graduates = df.graduates.str.replace(',', '') # Remove commas in graduates column
df = df[df['course'] == 'Information Technology'] # Selecting all the rows in which course is Information Technology and sex is MF
df = df[df['sex'] == 'MF'] 
df.graduates = pd.to_numeric(df.graduates) # Convert string to integer

print(df)
print("Total IT graduates from 2005 to 2020: ", df['graduates'].sum()) 