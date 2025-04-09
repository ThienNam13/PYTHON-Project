import time

def shake_window(window):
    """Hiệu ứng rung màn hình."""
    x, y = window.winfo_x(), window.winfo_y()
    for _ in range(5):
        window.geometry(f"+{x+2}+{y+2}")
        time.sleep(0.05)
        window.geometry(f"+{x-2}+{y-2}")
        time.sleep(0.05)

def change_background(window, color):
    """Thay đổi màu nền khi thắng/thua."""
    window.configure(bg=color)
