from Core.UptimeTracker import uptimeTracker
from Core.Storage import Storage
import time

class main:
    def __init__(self):
        super().__init__()
        self.uptimeTracker = uptimeTracker()
        self.uptime = self.uptimeTracker.getUptimeData()
        self.Storage = Storage()
        try:
            while True:
                print(f"Currently Up For {self.uptime}")
                self.uptime = self.uptimeTracker.getUptimeData()
                self.Storage.saveOnExit(self.uptime)
                time.sleep(2)
        except KeyboardInterrupt:
            print("Exiting... & Saving")

if __name__ == "__main__":
    app = main()