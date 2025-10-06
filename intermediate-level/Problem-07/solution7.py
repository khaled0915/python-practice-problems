from collections import Counter

def top_ips(log_file, top_n=3):
    ip_counter = Counter()
    
    with open(log_file, 'r') as file:
        for line in file:
            ip = line.split()[0]  # 
            ip_counter[ip] += 1
    
    return ip_counter.most_common(top_n)


top_three = top_ips('./intermediate-level/Problem-07/access.log')
print(top_three)
# output : [('127.0.0.1', 2), ('192.168.1.2', 2), ('10.0.0.5', 1)]