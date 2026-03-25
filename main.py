from Core.UptimeTracker import uptimeTracker
from Core.Storage import Save
import time

class main:
    def __init__(self):
        super().__init__()
        self.uptimeTracker = uptimeTracker()
        self.uptime = self.uptimeTracker.getUptimeData()
        self.save = Save()
        try:
            while True:
                print(f"Currently Up For {self.uptime}")
                time.sleep(10)
                self.uptimeData = self.uptimeTracker.getUptimeData()
                self.save.saveOnExit(self.uptimeData)
        except KeyboardInterrupt:
            print("Exiting... & Saving")

if __name__ == "__main__":
    app = main()