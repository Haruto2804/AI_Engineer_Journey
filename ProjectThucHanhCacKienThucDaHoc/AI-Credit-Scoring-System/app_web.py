import joblib

# Dữ liệu khách hàng test: [Tuổi, Thu nhập (Triệu), Điểm tín dụng, Số lần nợ xấu]
customer1 = [[38, 90, 600, 5]]

model_url = "./model/credit_scoring_model.pkl"

try:
    # Tải model
    model_scoring_credit = joblib.load(model_url)

    # Dự đoán (Lấy phần tử đầu tiên [0] vì kết quả trả về là một mảng)
    ket_qua = model_scoring_credit.predict(customer1)[0]

    # Giao diện in kết quả trực quan
    print("=" * 45)
    print("      HỆ THỐNG ĐÁNH GIÁ TÍN DỤNG AI      ")
    print("=" * 45)
    print(f"📊 Dữ liệu đầu vào: {customer1[0]}")
    print("-" * 45)

    # Dựa theo bộ dữ liệu của bạn: 1 là Duyệt (Tốt), 0 là Từ chối (Xấu)
    if ket_qua == 1:
        print("🟢 KẾT QUẢ: PHÊ DUYỆT (APPROVED)")
        print("📝 Đánh giá: Khách hàng có hồ sơ an toàn, đủ điều kiện giải ngân.")
    elif ket_qua == 0:
        print("🔴 KẾT QUẢ: TỪ CHỐI (REJECTED)")
        print("📝 Đánh giá: Hồ sơ rủi ro cao hoặc có lịch sử nợ xấu.")

    print("=" * 45)

except FileNotFoundError:
    print(f"❌ Lỗi: Không tìm thấy file model tại đường dẫn '{model_url}'.")
except Exception as e:
    print(f"❌ Có lỗi xảy ra: {e}")
