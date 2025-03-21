import time
import sys

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_song():
    lyrics = [
        ("แค่ห่างกับเธอนิดเดียวก็จะตายแล้ว", 0.13),
        ("แค่ห่างกับเธอแป๊ปเดียวฉันก็ทนไม่ไหว", 0.13),
        ("ช่วยอยู่ตรงนี้นานหน่อยได้ไหม", 0.18),
        ("ไม่มีเธอไม่ได้จริงๆ", 0.2),
        ("My heart skip a beat", 0.1),
        ("Heart skip a beat", 0.1),
    ]

    delays = [0.4, 0.85, 1.5, 1.5, 5.0, 0.7]

    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        time.sleep(delays[i])
        animate_text(lyric, speed)

if __name__ == "__main__":
    sing_song()
