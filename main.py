import os
from ocr_core import recognize_text

currentDirectory = os.getcwd()
activate_environment_path = currentDirectory + '/env/bin/activate_this.py'
print(activate_environment_path)
exec(open(activate_environment_path).read())

#input_path = input("Please input path(Format \\ ): ")
input_path = '/home/bakhtiyar/Desktop/apps/OCR/data/OCR/'
#search_extantion = input("Please input extantion name(Format .jpeg .png ... : ")
search_extantion = '.jpg'
for root, dirs, files in os.walk(input_path):
	for file in files:
		if file.endswith(search_extantion):
			pathToImage = os.path.join(root, file)
			#OCR module
			text = recognize_text(pathToImage)
			file = open("ExtractedText.txt","a")
			file.write(text + "\n")
			file.close()
			
		else:
			"The end"