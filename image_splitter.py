import cv2 
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("static/img/red10.png")

img = cv2.blur(image,(6,6))
contrast = 20
brightness = 1
brightness += int(round(255*(1-contrast)/2))
img = cv2.addWeighted(img, contrast, img, 0, brightness)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray],[0],None,[256],[0,256])
colors = np.where(hist>5000)
img_number = 0
for color in colors[0]:
    print(color)
    split_image = image.copy()
    split_image[np.where(gray != color)] = 0

    src = split_image
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    cv2.imwrite(str(img_number)+".png",dst)

    # cv2.imwrite(str(img_number)+".png",split_image)
    img_number+=1

# # to show histogram levels
# plt.hist(gray.ravel(),256,[0,256])
# plt.savefig('plt')
# plt.show()