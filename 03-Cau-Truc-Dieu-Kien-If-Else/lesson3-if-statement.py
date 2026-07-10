# 3. Thử thách thực chiến số 3: Bộ lọc kiểm duyệt nội dung của AI
# (Content Moderation)
# Hãy tưởng tượng bạn đang làm tính năng chặn các bình luận tiêu cực/toxic cho
# một mạng xã hội bằng AI. Model AI của bạn sẽ trả về một điểm số gọi là
# toxic_score từ 0.0 đến 1.0 (Điểm càng cao thì câu bình luận càng độc hại).
# Yêu cầu: Bạn hãy viết một đoạn code Python để phân loại hành động dựa trên biến
# toxic_score = 0.85:
# Nếu toxic_score >= 0.8: In ra "Xóa bình luận và khóa tài khoản!"
# Nếu toxic_score >= 0.5 (nhưng nhỏ hơn 0.8): In ra "Ẩn bình luận và gửi cảnh cáo
# cho người dùng."
# Các trường hợp còn lại (nhỏ hơn 0.5): In ra "Bình luận hợp lệ. Cho phép hiển thị."
# Bạn hãy viết đoạn code xử lý logic này nhé!
toxic_score = 0.9
if toxic_score >= 0.8:
    print("Xóa bình luận và khóa tài khoản!")
elif toxic_score >= 0.5:
    print("Ẩn bình luận và gửi cảnh cáo")
else:
    print("Bình luận hợp lệ. Cho phép hiển thị.")
