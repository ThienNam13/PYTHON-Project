import tkinter as tk
from tkinter import messagebox
import random

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Trò chơi đoán số")
window.geometry("300x200")  # Kích thước cửa sổ

# Tạo số ngẫu nhiên
secret_number = random.randint(1, 100)

# Hàm kiểm tra số đoán
def check_guess():
    try:
        guess = int(entry.get())
        if guess == secret_number:
            messagebox.showinfo("Kết quả", "Chúc mừng! Bạn đoán đúng!")
            window.quit()
        elif guess < secret_number:
            result_label.config(text="Số nhỏ quá! Thử lại.")
        else:
            result_label.config(text="Số lớn quá! Thử lại.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")

# Tạo các thành phần giao diện
instruction_label = tk.Label(window, text="Đoán số từ 1 đến 100:", font=("Arial", 18))
instruction_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)

check_button = tk.Button(window, text="Kiểm tra", command=check_guess)
check_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.config(bg="lightpink")
check_button.config(bg="green", fg="white")

# Chạy ứng dụng
window.mainloop()