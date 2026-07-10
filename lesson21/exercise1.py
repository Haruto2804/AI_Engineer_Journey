import pandas as pd

data_nganhang = {"diem_tin_dung": [720, 850, 150, 610, 9999, 450]}
df_bank = pd.DataFrame(data_nganhang)
print(df_bank)
df_bank["diem_tin_dung_sach"] = df_bank["diem_tin_dung"].clip(upper=850, lower=300)
print(df_bank)
