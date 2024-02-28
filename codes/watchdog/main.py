# 安装

# pip install watchdog

# 基本功能 

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    logging.info(f'start watching directory {path!r}')
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
        
# 高级用法
'''
watchmedo shell-command \
    --patterns="*.py" \
    --recursive \
    --command='echo "${watch_src_path}" && python -m unittest discover path_to_your_tests' \
    .
'''