import psutil
import time

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def resources_usage():
    while True:
        
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        
        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory}%")
        print(f"Disk Usage: {disk}%")
        
        if cpu > CPU_THRESHOLD:
            alert_cpu = "Alert High CPU usage"
            print(alert_cpu)
        
        if memory > MEMORY_THRESHOLD:
            alert_memory = "Alert High Memory Usage"
            print(alert_memory)
        
        if disk > DISK_THRESHOLD:
            alert_disk = "Alert High Disk Usage"
            print(alert_disk)

        with open("alert.log", "a") as f:
            f.write(alert_cpu + "\n")
        
        time.sleep(4)

resources_usage()
    