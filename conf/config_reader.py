import json
from pathlib import Path


class ReturnConfDict(object):
    """
    json_file: file name - creates Path obj
    Example: JSONReads(json_file).json_data["key1"]
    """
    def __init__(self, json_file="./conf/default.json"):
        """
        json_file: Path OBJ to (and including) json file
        """
        self.json_data = Path(json_file).resolve()

    @property
    def json_data(self):
        return self.__json_data

    @json_data.setter
    def json_data(self, json_file):
        with open(json_file, "r") as f:
            self.__json_data = json.load(f)

    def __repr__(self):
        return {"json data": self.json_data}
