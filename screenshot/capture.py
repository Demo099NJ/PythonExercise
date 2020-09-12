# filename: capture.py

# codes are from https://www.cnblogs.com/wutaotaosin/p/9719292.html

import time
import numpy as np
from PIL import ImageGrab

beg = time.time()
debug = False
for i in range(10):
  img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
  img = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
end = time.time()
print(end - beg)
