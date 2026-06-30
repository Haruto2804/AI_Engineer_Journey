import pandas as pd

# Giả sử ta có dữ liệu của 3 mô hình AI dưới dạng Dictionary
data = {
    "Model_Name": ["ChatGPT", "Claude", "Gemini"],
    "Accuracy": [0.95, 0.96, 0.94],
    "Release_Year": [2022, 2023, 2023],
}
df = pd.DataFrame(data)
print(df)
