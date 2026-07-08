from machine import Pin, ADC
import time

# ---------------- PINS ----------------
panic = Pin(15, Pin.IN, Pin.PULL_UP)
stop = Pin(16, Pin.IN, Pin.PULL_UP)
net_switch = Pin(17, Pin.IN, Pin.PULL_UP)

led = Pin(13, Pin.OUT)
buzzer = Pin(14, Pin.OUT)

sensor = ADC(26)

locked = True
alert_active = False

last_press = 0
press_count = 0

# ---------------- FUNCTIONS ----------------

def beep(d):
    led.value(1)
    buzzer.value(1)
    time.sleep(d)
    led.value(0)
    buzzer.value(0)
    time.sleep(0.1)

def unlock():
    global locked
    print("🔓 UNLOCKED")
    for _ in range(3):
        beep(0.1)
    locked = False

def check_unlock():
    global last_press, press_count

    if panic.value() == 0:
        time.sleep(0.2)
        now = time.ticks_ms()

        if time.ticks_diff(now, last_press) < 1000:
            press_count += 1
        else:
            press_count = 1

        last_press = now

        if press_count == 2:
            unlock()
            press_count = 0

def get_gps():
    # Simulated GPS
    return "Lat: 13.0827, Lon: 80.2707 (Chennai)"

def send_sms(location):
    print("📩 Sending SMS...")
    print("Emergency! Location:", location)

def alert_loop():
    global alert_active
    alert_active = True

    while alert_active:
        if stop.value() == 0:
            alert_active = False
            break

        led.value(1)
        buzzer.value(1)
        time.sleep(0.3)

        led.value(0)
        buzzer.value(0)
        time.sleep(0.3)

def detect_fall():
    val = sensor.read_u16()

    if val > 50000:
        print("⚡ Impact detected")

        still = 0
        for _ in range(15):
            time.sleep(0.2)
            if sensor.read_u16() < 10000:
                still += 1

        if still > 10:
            return True

    return False

# ---------------- MAIN ----------------

print("🔒 LOCKED")

while True:

    check_unlock()

    # Manual alert
    if not locked and panic.value() == 0:
        location = get_gps()

        if net_switch.value() == 1:
            send_sms(location)

        alert_loop()

    # Fall detection
    if not locked and detect_fall():
        print("⚠️ FALL DETECTED")

        location = get_gps()

        if net_switch.value() == 1:
            send_sms(location)

        alert_loop()

    time.sleep(0.1)
