# SilentSOS

An offline emergency alert system built using Raspberry Pi Pico and simulated in Wokwi.

## Features

- Double press panic button to unlock
- Manual SOS activation
- Fall detection using analog sensor
- Buzzer and LED emergency alert
- Stop button to cancel alert
- Network switch to simulate SMS sending
- Simulated GPS coordinates

---

## Components

- Raspberry Pi Pico
- Push Button (Panic)
- Push Button (Stop)
- LED
- Active Buzzer
- Slide Switch
- Potentiometer (Fall Sensor Simulation)

---

## Pin Connections

| Component | GPIO |
|----------|------|
| LED | GP13 |
| Buzzer | GP14 |
| Panic Button | GP15 |
| Stop Button | GP16 |
| Network Switch | GP17 |
| Sensor | GP26 (ADC0) |

---

## Working

### Unlock

Double press the panic button within one second to unlock the device.

### Manual SOS

After unlocking, pressing the panic button again starts the emergency alert.

### Fall Detection

The potentiometer simulates an impact sensor.

If a high analog value is detected followed by a low value for several seconds, a fall is assumed.

### SMS

When the Network switch is ON, the system prints a simulated SMS with GPS coordinates.

### Alert

The LED and buzzer blink continuously until the Stop button is pressed.

---

## File Structure

```
.
├── main.py
├── diagram.json
├── wokwi.toml
└── README.md
```

---

## Simulation

https://wokwi.com/projects/461846617350223873

---

## Future Improvements

- MPU6050 support
- GPS Module
- GSM Module
- Cloud Notification
- Mobile App
- Battery Monitoring

---

## Author

**Srikesav M**

Built using MicroPython and Wokwi.
