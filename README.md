# 🖥️ sysinfo.py

A simple but useful Python tool that gives you a quick overview of any computer you're sitting in front of.
Whether it's **your own machine** or **someone else's PC**, `sysinfo.py` helps you instantly understand the system specs without digging through menus and settings.

---

## ✨ What is sysinfo.py?

`sysinfo.py` is a lightweight Python script built to display the most important hardware and operating system information in a fast, clean, and readable way.

Instead of manually checking system menus, task manager, or terminal commands one by one, this tool gives you a quick summary in one shot ⚡

---

## 🔍 What it currently shows

The script currently displays:

- 🏷️ Hostname
- 🐧 / 🪟 Operating System
- 🧱 OS Release
- 🛠️ OS Version
- 🖥️ Architecture
- ⚙️ Processor information
- 🧠 CPU core count
- 💾 Total RAM
- 📈 Used RAM
- 📉 Available RAM
- 🗄️ Total Disk size
- 📦 Used Disk space
- 🧹 Free Disk space

---

## 🤔 Why I made this

Sometimes you sit at a random computer and immediately want to know:

- What OS is this running?
- How much RAM does it have?
- How many CPU cores does it have?
- Is the disk almost full?
- What kind of machine am I dealing with?

Instead of checking everything manually, I wanted a quick script I can run anywhere and get the answer immediately 💡

This project is being built as a **personal utility** and a **portable reference tool** that I can use on different computers whenever I need a fast system overview.

---

## 🎯 Project goal

The long-term goal of `sysinfo.py` is to become a simple and reliable cross-system information tool that works smoothly on:

- 🪟 Windows
- 🐧 Linux

The idea is not to build a huge monitoring platform.
The goal is to keep it:

- simple ✅
- fast ✅
- readable ✅
- portable ✅
- practical ✅

---

## 🚧 Current status

`sysinfo.py` is still under development.

Right now, it already covers the core system basics, but I plan to keep improving it and make it more polished over time.

So this project is a **work in progress** — but a useful one 😄

---

## 🔮 Planned improvements

Future versions may include:

- 📊 CPU usage percentage
- 🧠 RAM usage percentage
- 💽 Disk usage percentage
- ⏱️ Uptime / boot time
- 👤 Current logged-in user
- 🌐 IP address
- 📡 Network information
- 🧾 JSON output
- 🎨 Better CLI formatting
- 🧩 Basic mode / Full mode

---

## 📦 Requirements

This script currently uses:

- Python 3
- `psutil`

Install `psutil` with:

```bash
pip install psutil
