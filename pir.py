import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pir = 8
ser = 11
GPIO.setup(pir, GPIO.IN)
GPIO.setup(ser, GPIO.OUT)
print("Calibrating...")
time.sleep(2)
print("Active")
n = 0
p = GPIO.PWM(ser, 200)
V = 0
p.start(V)

try:
    while True:
        if GPIO.input(pir) == True:
            n= n + 1
            print ("Motion detected: Instance= ",n)
            p.ChangeDutyCycle(20)
            for V in range(0, 101, 5):
                p.ChangeDutyCycle(V)
                time.sleep(0.05)
            for V in range(95, 0, -5):
                p.ChangeDutyCycle(V)
                time.sleep(0.05)
            time.sleep(0.1)
            p.ChangeDutyCycle(0)
            time.sleep(0.1)
        
except KeyboardInterrupt:
            pass
finally:
    p.stop()
    GPIO.cleanup()
    print("program ended")