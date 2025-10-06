import re

def analyze_docker_log(file_path):
   
    error_patterns = re.compile(r'(ERROR|Exception)', re.IGNORECASE)
    timestamp_pattern = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?')

    error_logs = []

    with open(file_path, 'r') as log_file:
        for line in log_file:
            if error_patterns.search(line):
                
                timestamp_match = timestamp_pattern.search(line)
                timestamp = timestamp_match.group() if timestamp_match else "No Timestamp"
                error_logs.append((timestamp, line.strip()))
    
    return error_logs



if __name__ == "__main__":
    log_file_path = "f:/bongodev-class-content/python-practice-problems/advanced-level/Problem-01/docker.log" 
    errors = analyze_docker_log(log_file_path)
    
    for ts, msg in errors:
        print(f"[{ts}] {msg}")
