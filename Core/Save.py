import json
import os
from pathlib import Path
import atexit

class Save:
    def __init__(self, _data):
        super().__init__()
        self.savePath = Path(os.getenv("APPDATA") + "\\Vrw\\UptimeTracker")
        self.savePath.mkdir(parents=True, exist_ok=True)
        self.data = _data

    def updateData(self, _data):
        self.data = _data

    def saveOnExit(self):
        atexit.unregister(self.save)
        atexit.register(self.save, "uptime", self.data)

    def save(self, key, _data):
        dataToSave = {}
        dataToSave[key] = _data

        with open(self.savePath / "save.json", "w") as f:
            json.dump(dataToSave, f)