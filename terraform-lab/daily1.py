import psutil
import time
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 50
DISK_THRESHOLD = 80

def monitor_resources():
    while True:
        
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory}%")
        print(f"Disk Usage: {disk}%")

        alerts = []
        
        if cpu > CPU_THRESHOLD:
            alerts.append("Alert High CPU usage")
        
        if memory > MEMORY_THRESHOLD:
            alerts.append("Alert High Memory Usage")
           
        if disk > DISK_THRESHOLD:
            alerts.append("Alert High Disk Usage")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("alert.log", "a") as f:
            for alert in alerts:
                messege = f"{timestamp} {alert}"
                print(messege)
                f.write(messege + "\n")
        
        time.sleep(4)

monitor_resources()
    