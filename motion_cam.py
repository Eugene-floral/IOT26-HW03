import RPi.GPIO as GPIO
import time
import subprocess

PIR_PIN = 17
photo_count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Wait a second...")
time.sleep(30)
print("Start!")

try:
    while True:
        if GPIO.input(PIR_PIN):
            photo_count += 1
            filename = f"motion_{photo_count}.jpg"
            subprocess.run(["rpicam-still", "-o", filename, "--nopreview"])
            print(f"Motion detected! Photo saved: {filename}")
            while GPIO.input(PIR_PIN):
                time.sleep(0.1)
            print("Waiting...")
            time.sleep(3)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Done")
    GPIO.cleanup()
