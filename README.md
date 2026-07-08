# 🚨 SilentSOS Advanced Pro

A Raspberry Pi Pico-based emergency alert system built with **MicroPython** and simulated using **Wokwi**. The system provides manual SOS activation, fall detection, simulated GPS location, and SMS notification for emergency situations.

## ✨ Features

- 🔒 Double-press security unlock
- 🚨 Manual SOS button
- 🤕 Fall detection using analog sensor
- 📍 Simulated GPS location
- 📩 Simulated SMS notification
- 🔊 LED and buzzer emergency alarm
- 🛑 Stop button to cancel alarm
- 🌐 Network switch to enable/disable SMS

## 🛠 Components

- Raspberry Pi Pico
- LED
- Active Buzzer
- Push Button (Panic)
- Push Button (Stop)
- Slide Switch
- Potentiometer (Sensor Simulation)

## GPIO Connections

| Component | GPIO |
|-----------|------|
| LED | GP13 |
| Buzzer | GP14 |
| Panic Button | GP15 |
| Stop Button | GP16 |
| Network Switch | GP17 |
| Potentiometer | GP26 |

## How It Works

1. Device starts in a locked state.
2. Double-press the panic button within one second to unlock.
3. Press the panic button again to activate SOS.
4. GPS coordinates are generated.
5. If the network switch is ON, an SMS containing the GPS location is simulated.
6. LED and buzzer flash continuously until the stop button is pressed.
7. Fall detection automatically triggers the same emergency procedure.

## Project Structure

```
SilentSOS-Advanced-Pro/
├── main.py
├── diagram.json
├── README.md
├── .gitignore
└── LICENSE
```

## Simulation

https://wokwi.com/projects/461846617350223873

## Technologies

- MicroPython
- Raspberry Pi Pico
- Wokwi Simulator
- Embedded Systems
- IoT

## Future Improvements

- MPU6050 Accelerometer
- GPS Module
- GSM Module
- OLED Display
- Mobile App Integration
- Cloud Notifications

## Author

**Srikesav M**

B.Tech Information Technology  
PSG College of Technology

## License

MIT License
