import customtkinter as ctk
import pygame
from game_logic import generate_secret_number, check_guess
from effects import shake_window, change_background
from sounds import play_background_music, play_sound, stop_all_sounds
from settings import modes
from treasure import show_treasure_animation

# Khởi tạo pygame
pygame.init()
play_background_music()

# Cấu hình giao diện
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("pink.json")

window = ctk.CTk()
window.title("Trò chơi đoán số xổ")
window.geometry("420x350")
window.configure(bg="#ffe6f0")

# Trạng thái trò chơi
min_value = 1
max_value = 100
secret_number = generate_secret_number()
attempts = 0
selected_mode = ctk.StringVar(value="Dễ")

# Các widget sẽ cập nhật
range_label = None
label_attempts = None

# Cập nhật phạm vi hiển thị theo chế độ
def update_range_label():
    mode = selected_mode.get()
    if mode == "Siêu Khó":
        range_text = f"Đoán số từ {min_value} đến {max_value}:"
    else:
        range_text = "Đoán số từ 1 đến 100:"
    range_label.configure(text=range_text)

# Hàm xử lý đoán
def on_check_guess():
    global attempts, secret_number, min_value, max_value
    try:
        guess = int(entry.get())
        attempts += 1
        result, new_secret, new_min, new_max = check_guess(guess, secret_number, selected_mode.get(), attempts)

        max_attempts = modes[selected_mode.get()]
        if max_attempts:
            label_attempts.configure(text=f"Lượt còn lại: {max_attempts - attempts}")
        else:
            label_attempts.configure(text=f"Đã đoán {attempts} lần")

        if result == "win":
            play_sound("win")
            change_background(window, "pink")
            result_label.configure(text="🎉 Bạn siêu giỏi luôn!", text_color="green")
            show_treasure_animation()
            entry.configure(state="disabled")
            check_button.configure(state="disabled")
            restart_button.pack(pady=5)
        elif result == "lose":
            play_sound("lose")
            change_background(window, "red")
            result_label.configure(text="😢 Thua rồi, chơi lại nha!", text_color="red")
            entry.configure(state="disabled")
            check_button.configure(state="disabled")
            restart_button.pack(pady=5)
        elif result == "low":
            result_label.configure(text="⬇️ Số quá nhỏ rồi!", text_color="pink")
        elif result == "high":
            result_label.configure(text="⬆️ Số quá lớn rồi!", text_color="pink")
        elif result == "very_close":
            result_label.configure(text="🔥 Gần trúng lắm rồi!", text_color="orange")
        elif result == "close":
            result_label.configure(text="🙂 Khá gần, cố lên!", text_color="orange")
        elif result == "changed":
            secret_number = new_secret
            min_value = new_min
            max_value = new_max
            update_range_label()
            result_label.configure(
                text=f"Sai rồi! Phạm vi mới là {min_value}-{max_value}", text_color="cyan"
            )
        elif result == "invalid":
            shake_window(window)
            result_label.configure(text="Nhập số hợp lệ nha!", text_color="red")

    except ValueError:
        shake_window(window)
        result_label.configure(text="⚠️ Chỉ được nhập số!", text_color="red")

# Khi đổi chế độ reset lại game
def on_mode_change(choice):
    global attempts, secret_number, min_value, max_value
    attempts = 0
    min_value = 1
    max_value = 100
    secret_number = generate_secret_number()
    update_range_label()
    result_label.configure(text="")
    label_attempts.configure(text="Lượt còn lại: ∞" if modes[choice] is None else f"Lượt còn lại: {modes[choice]}")
# Thua thì cho chơi lại
def restart_game():
    global secret_number, attempts
    stop_all_sounds()  # Tắt âm thanh thua cuộc nếu đang phát
    play_background_music()

    secret_number = generate_secret_number()
    attempts = 0
    entry.configure(state="normal")
    check_button.configure(state="normal")
    restart_button.pack_forget()
    result_label.configure(text="", text_color="pink")
    label_attempts.configure(text=f"Lượt còn lại: {modes[selected_mode.get()]}")
    change_background(window, "pink")  # Hoặc màu mặc định của bạn

# Giao diện
ctk.CTkLabel(window, text="Chọn chế độ:", font=("Arial", 14)).pack(pady=(10, 0))
mode_menu = ctk.CTkComboBox(window, values=list(modes.keys()), variable=selected_mode, command=on_mode_change)
mode_menu.pack(pady=5)

range_label = ctk.CTkLabel(window, text="", font=("Arial", 18))
range_label.pack(pady=(10, 5))
update_range_label()

entry = ctk.CTkEntry(window, placeholder_text="Nhập số ở đây")
entry.pack(pady=5)

check_button = ctk.CTkButton(window, text="Kiểm tra", command=on_check_guess)
check_button.pack(pady=10)
restart_button = ctk.CTkButton(window, text="🔄 Chơi lại", command=lambda: restart_game())
restart_button.pack(pady=5)
restart_button.pack_forget()  # Ẩn lúc đầu

label_attempts = ctk.CTkLabel(window, text="Lượt còn lại: ∞", font=("Arial", 12))
label_attempts.pack()

result_label = ctk.CTkLabel(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
