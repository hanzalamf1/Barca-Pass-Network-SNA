import pandas as pd
import json

# JSON dosyasının yolunu belirle
json_file_path = 'C:/Users/hanza/Desktop/16120.json'

# JSON dosyasını utf-8 kodlaması ile oku
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# JSON verisini DataFrame'e dönüştür
df = pd.json_normalize(data)

# DataFrame'i Excel dosyasına yaz
excel_file_path = 'C:/Users/hanza/Desktop/social/week1/16120.xlsx'
df.to_excel(excel_file_path, index=False)

print("JSON verisi Excel dosyasına yazdırıldı.")
