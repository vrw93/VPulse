import json
import os
from pathlib import Path
import atexit

class Save:
    def __init__(self):
        super().__init__()
        self.savePath = Path(os.getenv("APPDATA") + "\\Vrw\\UptimeTracker")
        self.savePath.mkdir(parents=True, exist_ok=True)

    def saveOnExit(self, _data):
        atexit.unregister(self.save)
        atexit.register(self.save, _data)

    def save(self, _data):
        with open(self.savePath / "save.json", "w") as f:
            json.dump(_data, f)