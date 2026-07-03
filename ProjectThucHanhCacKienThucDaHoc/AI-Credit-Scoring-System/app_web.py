import streamlit as st
import joblib

# 1. Đặt cấu hình trang web (Tên tab, icon)
st.set_page_config(page_title="AI Bank Approval", page_icon="🏦", layout="centered")

# 2. Tiêu đề trang web
st.title("🏦 Hệ Thống Phê Duyệt Tín Dụng Tự Động")
st.subheader("Ứng dụng AI hỗ trợ thẩm định khoản vay - Version 1.0")
st.write("---")

# 3. Tạo các ô nhập liệu đẹp mắt ở giao diện bên trái (Sidebar) hoặc chính giữa
st.sidebar.header("📋 Nhập thông tin khách hàng")

tuoi = st.sidebar.number_input(
    "Tuổi của khách hàng:", min_value=18, max_value=100, value=30, step=1
)
thu_nhap = st.sidebar.slider(
    "Thu nhập hàng tháng (Triệu VNĐ):", min_value=0, max_value=200, value=25
)
diem_td = st.sidebar.slider(
    "Điểm tín dụng CIC (300 - 850):", min_value=300, max_value=850, value=650
)
no_xau = st.sidebar.selectbox(
    "Số lần từng có nợ xấu:", options=[0, 1, 2, 3, 4, 5], index=0
)

# 4. Thiết kế nút bấm và xử lý logic khi người dùng bấm nút
if st.button("🚀 Kiểm Tra Hồ Sơ"):
    st.write("### 🔍 Kết quả thẩm định:")

    # ---------------------------------------------------
    # VÒNG 1: BỘ LỌC LUẬT CỨNG (KNOCK-OUT RULES)
    # ---------------------------------------------------
    if no_xau > 0:
        st.error("🔴 KẾT QUẢ: TỪ CHỐI NGAY LẬP TỨC (REJECTED)")
        st.warning(
            "⚠️ Lý do: Khách hàng vi phạm chính sách cốt lõi của ngân hàng (Có lịch sử nợ xấu)."
        )
    # VÒNG 2: GỌI BỘ NÃO AI (Chỉ chạy khi hồ sơ sạch nợ xấu)
    # ---------------------------------------------------
    else:
        try:
            # Load file pkl lên
            ai_bank = joblib.load("model/credit_scoring_model.pkl")
            # Chuẩn bị dữ liệu và dự đoán
            ho_so_moi = [[tuoi, thu_nhap, diem_td, no_xau]]
            ket_qua = ai_bank.predict(ho_so_moi)
            print("test kq", ket_qua)
            if ket_qua[0] == 1:
                st.success("🟢 KẾT QUẢ: PHÊ DUYỆT (APPROVED)")
                st.balloons()  # Hiệu ứng bóng bay chúc mừng cho giao diện thêm xịn!
                st.info(
                    "📝 Đánh giá: AI xác nhận hồ sơ an toàn, đạt đủ điểm uy tín để giải ngân."
                )
            else:
                st.error("🔴 KẾT QUẢ: TỪ CHỐI (REJECTED)")
                st.info(
                    "📝 Đánh giá: AI phát hiện rủi ro tiềm ẩn dựa trên mô hình hành vi tài chính."
                )

        except Exception as e:
            st.error(
                "Lỗi: Không tìm thấy file bộ não 'credit_scoring_model'. Hãy chắc chắn bạn đã đặt nó chung thư mục!"
            )
