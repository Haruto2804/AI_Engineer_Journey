# p và r đều là %
def calculate_f1_score(p, r):
    if p < 0 or p > 1:
        print("Precision không hợp lệ (0->1)")
        return -1
    elif r < 0 or r > 1:
        print("Recall không hợp lệ (0->1)")
        return -1
    f1_score = float((2 * p * r) / (p + r))
    return f1_score


result = calculate_f1_score(0.8, 0.9)

print(f"F1-Score = {result}")
