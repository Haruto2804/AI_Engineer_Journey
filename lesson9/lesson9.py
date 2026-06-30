import pandas as pd

dict_users = {
    "username": ["haruto2804", "harushadow284", "ilovemanbo032", "emoidungkhoc325"],
    "is_premium": [False, True, True, False],
}
df_users = pd.DataFrame(dict_users)
# Lấy ra riêng cột Username từ bảng df_users.
print(f"Cột username có giá trị là: \n{df_users["username"]}")

# (Nâng cao một chút) Làm sao để lọc ra danh sách những người dùng có Is_Premium bằng True?
print("Danh sách cột ảo - điều kiện ")
premium_list = df_users["is_premium"]
print(premium_list)
print("Danh sách những người dùng là is_premium")
premium_names = df_users[premium_list]
print(premium_names)
print("Danh sách những người dùng là không là is_premium")
premium_names = df_users[~premium_list]
print(premium_names)
