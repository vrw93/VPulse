import psutil
from datetime import datetime

class uptimeTracker():
    def __init__(self):
        super().__init__()
        self.uptime = self.get_uptime()

    def get_uptime(self):
        uptimeF = psutil.boot_time()
        boottime = datetime.fromtimestamp(uptimeF)
        uptime = datetime.now() - boottime
        return uptime
    
    def getUptimeData(self):
        uptime = self.get_uptime()
        data = {}
        lastUptimeDate = datetime.now().date()