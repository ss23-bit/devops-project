import string

def analyze_logs(logs):

    count = {}

    for log in logs:
        log = log.translate(str.maketrans("", "", string.punctuation)).lower()
        
        level = log.split()[0]

        count[level] = count.get(level, 0) + 1
        
    return count

logs = [
    "ERROR Disk full",
    "INFO User login",
    "ERROR Disk full",
    "WARNING CPU high",
    "INFO User login"
]

most_freq = analyze_logs(logs)
most_freq_level = max(most_freq, key=most_freq.get)

print(f"Most frequent: {most_freq_level} ({most_freq[most_freq_level]})")
