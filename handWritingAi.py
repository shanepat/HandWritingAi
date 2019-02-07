import os
import cv2

i = 0
j = 0
allPicture = []
label = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

for root, dirs, files in os.walk('.\\TrainingSample' , topdown=False):
    for filename in files:
        while(i <= 9):
            if (root + '\\' + filename).startswith('.\\TrainingSample' + '\\' + str(i)):
                allPicture.append(cv2.imread(root + '\\' + filename,0))
                break
            else:
                i += 1
i = 0

while(j < len(allPicture)):
    for root, dirs, files in os.walk('.\\TrainingSample' , topdown=False):
        for filename in files:
            while(i <= 9):
                if (root + '\\' + filename).startswith('.\\TrainingSample' + '\\' + str(i)):
                    label[i] = "1"
                    print("\n|" + "Label " + " ".join(label) + " |" + "Features ", end="")
                    label = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
                    for line in allPicture[j]:
                        outputLine = []
                        for num in line:
                            outputLine.append(num)
                        outputLine = str(outputLine)
                        for x in outputLine:
                            outputLine = outputLine.replace("[", "").replace("]", " ").replace(",", "")
                        print(outputLine, end="")
                        outputLine = []
                    j += 1
                    break
                else:
                    i += 1
