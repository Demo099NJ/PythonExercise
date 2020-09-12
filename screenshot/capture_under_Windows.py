# filename: shot_under_windows.py

# codes are from https://www.cnblogs.com/wutaotaosin/p/9719292.html

import time
import win32gui, win32ui, win32con, win32api

def window_capture(filename):
  hwnd = 0 # the number of the window, 0 indicates the current active window
  # get the device context DC (deviation context) of the window according to the window handle
  hwndDC = win32gui.GetWindowDC(hwnd)
  # get the mfcdc according to the DC of the window
  mfcDC = win32ui.CreateDCFromHandle(hwndDC)
  # mfcdcs create compatible DCS
  saveDC = mfcDC.CreateCompatibleDC()
  # create a bigmap to save the picture
  saveBitMap = win32ui.CreateBitmap()
  # get monitor information
  MoniterDev = win32api.EnumDisplayMonitors(None, None)
  w = MoniterDev[0][2][2]
  h = MoniterDev[0][2][3]
  # print w,h　　　# picture size
  # opening up space for bitmap
  saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
  # save the screenshot to savebitmap
  saveDC.SelectObject(saveBitMap)
  # cut the image with length and width (W, H) from the upper left corner (0, 0)
  saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
  saveBitMap.SaveBitmapFile(saveDC, filename)

beg = time.time()
for i in range(10):
  window_capture("haha.jpg")
end = time.time()
print(end - beg)
