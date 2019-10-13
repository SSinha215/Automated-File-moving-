from watchdog.observers import *
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self,event):
        new_name = "new_file" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists - os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src,new_destination)


folder_to_track = "Provide the folder path to track from which the files are to be moved."
folder_destination = "Provide the folder path to which the files are to be moved."
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop()
