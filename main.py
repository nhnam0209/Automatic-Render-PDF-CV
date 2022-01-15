import json
from a_40.a_40 import fill
import time
if __name__ == '__main__':
    s = time.time()
    with open("cv.json", encoding="utf8") as f:
        data = json.load(f)
    fill(data)
