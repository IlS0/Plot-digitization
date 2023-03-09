import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2


if __name__ == "__main__":
    # 75 433
    file = "data/US-Gini-coefficient-1967-to-2017-Source-US-Bureau-of-the-Census.png"
    img = cv2.imread(file)

    # crop
    bbox = [75, 0, 850, 433] # x, y, w, h
    img = img[bbox[1]:bbox[1]+bbox[3], bbox[0]:bbox[0]+bbox[2]]
    plt.imshow(img, cmap='gray') # gray
    # Бинаризация
    
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    plt.imshow(thresh, cmap='gray')
    plt.waitforbuttonpress()
    plt.close('all')