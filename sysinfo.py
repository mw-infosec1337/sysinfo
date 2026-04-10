import platform
import os
import psutil
print("=======SYSTEM INFO=======")
print("Hostname:", platform.node())
print("OS Release:", platform.release())
print("Operating System", platform.system())
print("OS Version:", platform.version())
print("Architecture:", platform.machine())
print("Processor:", platform.processor())
print("CPU:", os.cpu_count())
Ram = psutil.virtual_memory()
print("Total Ram:", round(Ram.total / (1024**3), 2), "GB")
print("Ram Used:", round(Ram.used / (1024**3), 2), "GB")
print("Ram Available:", round(Ram.available / (1024**3), 2), "GB")
Disk = psutil.disk_usage('/')
print("Total Disk:", round(Disk.total / (1024**3), 2), "GB")
print("Disk Used:", round(Disk.used / (1024**3), 2), "GB")
print("Disk Free Space:", round(Disk.free / (1024**3), 2), "GB")

