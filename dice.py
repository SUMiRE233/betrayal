import tkinter as tk
from PIL import Image, ImageTk
import random

result_num = None

def Rolldice():
    global result_num
    root = tk.Tk()
    root.title('骰子')

    jpg_images = [ImageTk.PhotoImage(Image.open(f'图片/骰子/dice_{i}.jpg')) for i in range(3)]
    result_label = tk.Label(root)

    gif = Image.open('图片/骰子/dice_0.gif')
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))
    except EOFError:
        pass

    play_count = 0

    def update_frame(frame_index):
        nonlocal play_count
        global result_num
        if frame_index < len(frames):
            gif_label.config(image=frames[frame_index])
            root.after(50, lambda: update_frame(frame_index + 1))
        else:
            if play_count < 1:
                play_count += 1
                update_frame(0)
            else:
                gif_label.pack_forget()
                result_num = random.randint(0, 2)
                result_label.config(image=jpg_images[result_num])
                result_label.pack()

    gif_label = tk.Label(root)
    gif_label.pack()
    update_frame(0)

    root.mainloop()
    print(result_num)
    return result_num

Rolldice()