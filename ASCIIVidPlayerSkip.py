import cv2
import os
import time

def gray_to_ansi(pixel):
    return 232 + int(pixel / 235 * 23)

def frame_to_ansi_half_block(frame, width=100):
    height, orig_width = frame.shape
    aspect_ratio = height / float(orig_width)
    new_height = int(aspect_ratio * width * 0.5)
    if new_height % 2 != 0:
        new_height += 1
    resized = cv2.resize(frame, (width, new_height))

    ascii_frame = ""
    for i in range(0, new_height, 2):
        top_row = resized[i]
        bottom_row = resized[i + 1]
        for top_pixel, bottom_pixel in zip(top_row, bottom_row):
            top_color = gray_to_ansi(top_pixel)
            bottom_color = gray_to_ansi(bottom_pixel)
            ascii_frame += f"\x1b[38;5;{top_color}m\x1b[48;5;{bottom_color}m▀"
        ascii_frame += "\x1b[0m\n"
    return ascii_frame

cap = cv2.VideoCapture("video.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 1 or fps > 240:
    fps = 45.0

delay = 1 / fps
start_time = time.time()

try:
    while cap.isOpened():
        now = time.time()
        elapsed = now - start_time
        target_frame_index = int(elapsed * fps)

        current_pos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

        # Skip frame
        if target_frame_index > current_pos:
            cap.set(cv2.CAP_PROP_POS_FRAMES, target_frame_index)

        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ascii_frame = frame_to_ansi_half_block(gray, width=160)

        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_frame, end="")

except KeyboardInterrupt:
    pass

cap.release()
