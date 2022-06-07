import os
import pandas as pd
import shutil
import glob

os.system(f"wget {'https://data.gov.sg/dataset/f6048a81-0f7b-436c-8bfa-ebe1bb42cfdc/download'} -O {'polygrad.zip'}") # download the zip file and extract
os.system(f"wget {'https://data.gov.sg/dataset/249f1149-1e04-40e2-81c6-bfab3bba5574/download'} -O {'unigrad.zip'}")
shutil.unpack_archive('polygrad.zip')
shutil.unpack_archive('unigrad.zip')

file = [] # empty list 
path = "./*.csv"
for fname in glob.glob(path): # check for filenames and store in list
    file.append(fname)

df = pd.read_csv(file[0]) # Load the CSV into a DataFrame
df.graduates = df.graduates.str.replace(',', '') # Remove commas in graduates column
df = df[(df.course == 'Information Technology') & (df.sex=="MF")] # Select all the rows in which course is Information Technology and sex is MF
df.graduates = pd.to_numeric(df.graduates) # Convert string to integer

df_uni = pd.read_csv(file[1])
df_uni.graduates = df_uni.graduates.str.replace(',', '')
df_uni = df_uni[(df_uni.course == 'Information Technology') & (df_uni.sex=="MF")]
df_uni.graduates = pd.to_numeric(df_uni.graduates)
print(df,"\n", df_uni) 

poly_sum = df['graduates'].sum()
uni_sum = df_uni['graduates'].sum()
print("Poly Grad: ", poly_sum, "\n", "Uni Grad: ", uni_sum)  
print("Total IT graduates from 2005 to 2020: ", poly_sum + uni_sum) 