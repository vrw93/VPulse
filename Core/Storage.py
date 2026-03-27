import json
import os
from pathlib import Path
import atexit

class Storage:
    def __init__(self):
        super().__init__()
        self.savePath = Path(os.getenv("APPDATA") + "\\VrwDev\\UptimeTracker")
        self.savePath.mkdir(parents=True, exist_ok=True)

    def loadData(self):
        try:
            with open(self.savePath / "save.json", "r") as f:
                _data = json.load(f)
            return _data
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def saveOnExit(self, _data):
        atexit.unregister(self.save)
        atexit.register(self.save, _data)

    def save(self, _data):
        with open(self.savePath / "save.json", "w") as f:
            json.dump(_data, f, indent=4, sort_keys=True)