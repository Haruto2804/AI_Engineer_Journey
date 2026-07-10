import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# 1. Dữ liệu gốc: Tuổi thì nhỏ, Lương thì số rất to
data = {"Tuổi": [25, 30, 50], "Lương": [10000000, 20000000, 50000000]}
df = pd.DataFrame(data)
print("--- DỮ LIỆU GỐC ---")
print(df)

# 2. Gọi công cụ chuẩn hóa Min-Max (Ép về 0 đến 1)
scaler = MinMaxScaler()

# 3. Tiến hành ép kiểu và xem kết quả
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\n--- DỮ LIỆU SAU KHI CHUẨN HÓA ---")
print(df_scaled)
