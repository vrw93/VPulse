from Core.UptimeTracker import uptimeTracker
from Core.Save import Save
import time

class main:
    def __init__(self):
        super().__init__()
        self.uptimeTracker = uptimeTracker()
        self.uptime = self.uptimeTracker.get_uptime()
        self.save = Save(str(self.uptime))
        try:
            while True:
                print(f"Currently Up For {self.uptime}")
                time.sleep(10)
                self.uptime = self.uptimeTracker.get_uptime()
                self.save.updateData(str(self.uptime))
                self.save.saveOnExit()
        except KeyboardInterrupt:
            print("Exiting... & Saving")

if __name__ == "__main__":
    app = main()