# Create virtual env:
	virtualenv -p python3 env
# Activate 
	source env/bin/activate
#Install libraries
	pip3 install pillow
	pip3 install pytesseract
	pip3 install opencv-python
	pip3 install tesseract
	sudo apt-get install tesseract-ocr
# Import necessary packeges
	from PIL import image
	import pytesseract
	iport argparse
	import cv2
	import os
# Construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image to be OCR'd")
ap.add_argument("-p","-preprtcess",type=str,default="thresh", help="type of preprocessing to be done")
args=vars(ap.parse_args())
# --image: The path to the image we're sending through the OCR system.
# --preprocess: The preprocessing method. This switch is optional and can accept two values: tresh (treshold) or blur.
# load the example and convert it to grayscale.
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#check to see if we should apply tresholding to preprocess the image.
if args["preprocess"]=="thresh":
	gray = cv2.threshold(gray, 0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median bluring should be done to remove noice
elif.args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray,3)
# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imread(filename, gray)
# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

#show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)


# Add all installed library
	pip3 freeze > requirements.txt
