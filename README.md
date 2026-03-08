# Hephaestus Heat Tracker

A smart thermal management system for the ThinkPad T480 running Ubuntu. This project doesn't just check the temperature, but uses physics logic to predict overheating before it happens.

## The Physics
This Sentinel implements Newton's Law of Cooling in reverse to calculate the Rate of Temperature Change ($dT/dt$).
- If the temperature rises > 1.5°C per second, Sentinel will sound an audible warning even if the temperature hasn't reached the critical limit.
- Helps understand the concept of derivatives in real-time programming.

## Crazy Features
- **Real-time Monitoring**: Pulls data directly from the kernel via `psutil`.
- **Predictive Warning**: Nags via `gTTS` if the temperature rises too wildly.
- **Auto-Throttle**: Automatically initiates `cool-mode` (TLP/Power management) when the temperature reaches 75°C.
- **Voice Assistant**: Google's robotic voice feedback to make your laptop feel like it has a soul.

## Tech Stack
- **OS**: Ubuntu 24.04 (ThinkPad T480)
- **Language**: Python 3.12
- **Libraries**: `psutil`, `pygame`, `gTTS`, `subprocess`

## How to Use
1. Make sure TLP is installed on Ubuntu.
2. Create a `cool-mode` file in the root folder and grant it executable permissions: `chmod +x cool-mode`.
3. Run Sentinel:
```bash
./venv/bin/python sentinel.py
