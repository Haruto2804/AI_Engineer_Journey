sentiment_result = {
    "text": "Khóa học AI này thực sự rất thực tế và dễ hiểu!",
    "label": "Positive",
    "confidence": 0.93,
}
# Yêu cầu: 1. Hãy viết lệnh in ra màn hình nhãn dự đoán (label) của câu văn trên.
print(f"Nhãn dựa đoán của câu văn trên là: {sentiment_result['label']}")
# 2. Hãy viết một câu điều kiện if: Nếu độ tự tin (confidence) lớn hơn 0.9, hãy in ra câu: "Kết quả đáng tin cậy!". Ngược lại, in ra: "Cần kiểm tra lại."

result = (
    "Kết quả đáng tin cậy!"
    if sentiment_result["confidence"] > 0.9
    else "Cần kiểm tra lại."
)
print(f"Kết quả: {result}")
