import cv2
import pytesseract
img=cv2.imread("C:\Users\Randika Dilshan\Downloads\WhatsApp Image 2022-02-13 at 1.42.36 PM.jpeg")
text = pytesseract.image_to_string(img)
print(text)