import os
import time

watch_dir = r"F:\bongodev-class-content\python-practice-problems\advanced-level\Problem-07"  


existing_files = set(os.listdir(watch_dir))

print(f"Watching folder: {watch_dir}")

try:
    while True:
        time.sleep(2)  
        current_files = set(os.listdir(watch_dir))
        
       
        new_files = current_files - existing_files
        
        for file in new_files:
            if file.endswith(".txt"):
                print(f"New .txt file detected: {file}")
        
        existing_files = current_files

except KeyboardInterrupt:
    print("Stopped watching folder.")
