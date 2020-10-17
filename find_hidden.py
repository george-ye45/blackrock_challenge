import cv2
from PIL import Image
import numpy as np


picture = Image.open("imageEmbedded.png")
r,g,b = picture.getpixel( (0,0) )
print("Red: {0}, Green: {1}, Blue: {2}".format(r,g,b))

def compare(list1, list2):
    for i in range(3):
        if list1[i] != list2[i]:
            return False
    return True



img_arr = cv2.imread('imageEmbedded.png')   # reads an image in the BGR format
img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2RGB)   # BGR -> RGB

for i in range(210):
    for j in range(600):
        if compare(img_arr[i][j], [0, 0, 0]):
            img_arr[i][j] = np.array([150, 150, 150])


img = Image.fromarray(img_arr, 'RGB')
img.show()
img.save("found.png")
