from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

from watchdog.utils import WatchdogShutdown

class WatchMan(FileSystemEventHandler):
    def on_any_event(self,event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            # subprocess.call(["python","site_gen.py"])
            # print("File created")
            pass
        elif event.event_type == 'modified':
            subprocess.call(["python","site_gen.py"])
            print('File modified')
        # subprocess.call(["python","site_gen.py"])

if __name__== "__main__":
    print("Watching content folder...")
    event_handler = WatchMan()
    observer = Observer()
    observer.schedule(event_handler,path='content',recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
