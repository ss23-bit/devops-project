def analyze_logs(logs):
    
    level_count = {}
    error_per_day = {}

    for log in logs:

        parts = log.split()

        timestamp = parts[0]
        level = parts[1]

        date = timestamp.split("T")[0]
        
        level_count[level] = level_count.get(level, 0) + 1

        if level == "ERROR":
            error_per_day[date] = error_per_day.get(date, 0) + 1

    return level_count, error_per_day

logs = [
    "2026-05-02T10:00:01Z ERROR Disk full",
    "2026-05-02T10:01:10Z INFO User login",
    "2026-05-02T10:02:33Z ERROR Disk full",
    "2026-05-03T09:15:22Z WARNING CPU high"
]

levels, errors = analyze_logs(logs)
print(levels)
print(errors)

error_threshold = 2
warning_threshold = 2

for date, count in errors.items():
    if count >= error_threshold:
        print(f"Alert: High errors on {date} ({count})")

if levels.get("WARNING", 0) >= warning_threshold:
    print(f"WARNING spike detected")


