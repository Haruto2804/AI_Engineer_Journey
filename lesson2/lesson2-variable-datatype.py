# Bây giờ, bạn đang là một AI Engineer phát triển hệ thống
# Nhận diện khuôn mặt tại cửa ra vào.

# Yêu cầu: Hãy khai báo 3 biến sau bằng Python:

# Biến đặt tên là user_name chứa tên của người bước vào (ví dụ: "Nguyen Van A").
user_name = "Haruto2804"
# Biến đặt tên là confidence_score chứa độ tin cậy của AI khi nhận diện khuôn mặt
# này (ví dụ: 0.98 - tức là AI tin tưởng 98%).
confidence_score = 0.98

# Biến đặt tên là is_allowed để quyết định xem cửa có mở hay không. Bạn hãy gán
# giá trị thích hợp cho biến này dựa trên logic: nếu độ tin cậy cao
is_allowed = True if confidence_score > 0.9 else False
# (confidence_score > 0.9) thì cho phép vào (True).
if is_allowed:
    print("Bạn được phép vào!")
else:
    print("Bạn không được phép vào")
