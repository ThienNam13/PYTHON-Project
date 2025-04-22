import random
from settings import modes

def generate_secret_number(min_value=1, max_value=100):
    return random.randint(min_value, max_value)

def check_guess(guess, secret_number, mode, attempts, min_value=1, max_value=100):
    max_attempts = modes[mode]

    if guess == secret_number:
        return "win", secret_number, min_value, max_value

    # Kiểm tra lượt ở mọi chế độ (trừ "Dễ" không giới hạn)
    if max_attempts and attempts >= max_attempts:
        return "lose", secret_number, min_value, max_value
    
    # Siêu Khó: thay đổi phạm vi mỗi lần đoán sai
    if mode == "Siêu Khó":
        min_value = max(1, guess - 5)
        max_value = min(100, guess + 5)
        secret_number = random.randint(min_value, max_value)
        return "changed", secret_number, min_value, max_value

    # Dễ: thêm gợi ý khoảng cách
    if mode == "Dễ":
        distance = abs(guess - secret_number)
        if distance <= 5:
            return "very_close", secret_number, min_value, max_value
        elif distance <= 10:
            return "close", secret_number, min_value, max_value

    # check low/high
    if guess < secret_number:
        result = "low"
    else:
        result = "high"

    return result, secret_number, min_value, max_value

