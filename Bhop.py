import keyboard
import time
delay = 0.02
def bhop():
    while True:
        if keyboard.is_pressed("space"):
            keyboard.press("space")
            time.sleep(delay)  # İstediğiniz gecikme değerini ayarlayabilirsiniz
            keyboard.release("space")
            time.sleep(delay)  # İstediğiniz gecikme değerini ayarlayabilirsiniz
            keyboard.press("space")

if __name__ == "__main__":
    print("Bunny hop helper runing. Press Ctrl+C for exit.")
    try:
        bhop()
    except KeyboardInterrupt:
        print("Bunny hop helper stoped.")
