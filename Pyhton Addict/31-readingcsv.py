# ####################PANDAS İLE OKUNUŞU ########
import pandas as pd

df = pd.read_csv('filled_jobs.csv')

print(df, "\n")
#İlk 10 kaydı getiriniz.
print(df.head(10),"\n")

# 2- Toplam kaç kayıt vardır ?
print(len(df.index))
# 3 - colum isimlerini yazdırınız
print("*******************")
print(df.columns)

# ####################NORMAL PYTHON KOMUTLARI İLE ########

with open("filled_jobs.csv", "r", encoding="utf-8" ) as file:
    print(file.read())

# #################### CSV MODÜLÜ İMPORT EDEREK ########

import csv  # loads csv module
with open("filled_jobs.csv", 'r', newline = '', encoding = 'utf-8') as file:
    csv_rows = csv.reader(file, delimiter=',')  # reader() function takes each
                                 # row (lines) into a list
    for row in csv_rows: # altalta çıktı almak için for döngüsüne soktuk.
        print(row) 

import csv
spaces = ("30","10","10","10","10","12","14")
with open('filled_jobs.csv', newline='') as mycsv:
    data = csv.reader(mycsv, delimiter=',')
    for line in data:
        for i in range(len(line)):
            print(f"{line[i]:^{spaces[i]}}",end = "")
        print()
