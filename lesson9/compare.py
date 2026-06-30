import time
import random
import pandas as pd


# Bạn không cần phải hiểu toàn bộ code, chỉ cần biết đoạn code này chỉ để so sánh
# cho thấy sự khác biệt về tốc độ của Pandas và Python Thuần
def compare_speed():
    # Số dòng càng lớn thì tốc độ càng cải thiện
    # Nếu số dòng quá nhỏ thì Python Thuần có thể sẽ nhanh hơn vì Pandas
    # cần 1 khoảng thời gian để sắp xếp cấu trúc dữ liệu
    num_rows = 1000000
    print(f"Đang tạo tập dữ liệu giả với {num_rows:,} dòng...")

    # 1. Khởi tạo dữ liệu
    # Dữ liệu cho Python thuần (List of Dictionaries)
    python_data = [
        {"price": random.uniform(10, 100), "quantity": random.randint(1, 20)}
        for _ in range(num_rows)
    ]

    # Dữ liệu cho Pandas (DataFrame)
    df = pd.DataFrame(python_data)

    print("-" * 50)

    # ==========================================
    # 2. Xử lý bằng Python thuần (Sử dụng Generator & Vòng lặp)
    # ==========================================
    start_time_py = time.time()

    # Tính tổng bằng cách duyệt qua từng dòng một
    total_revenue_py = sum(row["price"] * row["quantity"] for row in python_data)

    end_time_py = time.time()
    py_duration = end_time_py - start_time_py

    print(f"[Python Thuần] Tổng doanh thu : {total_revenue_py:,.2f}")
    print(f"[Python Thuần] Thời gian chạy : {py_duration:.5f} giây")

    print("-" * 50)

    # ==========================================
    # 3. Xử lý bằng Pandas (Sử dụng Vector hóa)
    # ==========================================
    start_time_pd = time.time()

    # Tính tổng bằng cách nhân hai cột với nhau và gọi hàm sum()
    total_revenue_pd = (df["price"] * df["quantity"]).sum()

    end_time_pd = time.time()
    pd_duration = end_time_pd - start_time_pd

    print(f"[Pandas]       Tổng doanh thu : {total_revenue_pd:,.2f}")
    print(f"[Pandas]       Thời gian chạy : {pd_duration:.5f} giây")

    print("-" * 50)

    # ==========================================
    # 4. Kết luận
    # ==========================================
    if pd_duration < py_duration:
        speedup = py_duration / pd_duration
        print(f"🚀 Kết luận: Pandas NHANH HƠN Python thuần khoảng {speedup:.1f} lần!")
    else:
        speedup = pd_duration / py_duration
        print(f"🐢 Kết luận: Python thuần NHANH HƠN Pandas khoảng {speedup:.1f} lần!")


# Chạy hàm đối chiếu
if __name__ == "__main__":
    compare_speed()
