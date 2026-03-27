import psutil
from datetime import datetime
from Core.Storage import Storage

class uptimeTracker():
    def __init__(self):
        super().__init__()
        self.Storage = Storage()
        self.getUptimeData()

    def get_uptime(self):
        lastUptimeData = self.Storage.loadData()
        boottime = self.getCurrentBootTime()
        uptime = datetime.now() - boottime
        uptime = uptime.total_seconds()

        if lastUptimeData is not None:
            lastBootTime = datetime.strptime(lastUptimeData["LastBootDate"], "%Y-%m-%d %H:%M:%S")
            lastUptime = float(lastUptimeData["UptimeTotal"])
            if lastBootTime.replace(microsecond=0) != boottime.replace(microsecond=0):
                uptime = lastUptime + uptime
        
        return uptime
    
    def getCurrentDate(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def getCurrentBootTime(self):
        uptimeF = psutil.boot_time()
        return datetime.fromtimestamp(uptimeF)

    def getUptimeData(self):
        data = {}
        CurrentBootDate = self.getCurrentBootTime().strftime("%Y-%m-%d %H:%M:%S")
        data["UptimeTotal"] = str(self.get_uptime())
        data["LastUptimeDate"] = str(self.getCurrentDate())
        data["LastBootDate"] = str(CurrentBootDate)
        return data

if __name__ == "__main__":
    app = uptimeTracker()