# TODO: Crear un script que recorte las pages segun la razon 3:5, y las guarde en la carpeta "1.2.- croppedPages".

import os
from PIL import Image
import PIL

ORIGPATH = os.path.join("./", "1.1.- rotatePages")
DESTPATH = os.path.join("./", "1.2.- croppedPages")


def openImage(path):
    image = Image.open(path)
    image = image.convert('RGB')
    return image


def saveImage(imageData, destPath):
    imageData.save(destPath)
    return 0


def getAspectRatio(imageData):
    return imageData[0]/imageData[1]


def calculateResize(imageData):
    aspectRatio = getAspectRatio(imageData)
    if aspectRatio > 0.6:
        ySize = int(imageData[1])
        xNewSize = int((3*ySize)/5)
        return (xNewSize, ySize)

    elif aspectRatio < 0.6:
        xSize = int(imageData[0])
        yNewSize = int((5*xSize)/3)
        return (xSize, yNewSize)
    else:
        return imageData


def calculateResizePoint(origSize, destSize):
    cropPoint = ()
    if origSize[0] == destSize[0]:
        yResize = origSize[1] - destSize[1]
        y1 = int(yResize/2)
        aPoint = (0, y1)
        y2 = int(origSize[1] - yResize/2)
        bPoint = (origSize[0], y2)
    elif origSize[1] == destSize[1]:
        xResize = origSize[0] - destSize[0]
        x1 = int(xResize/2)
        aPoint = (x1, 0)
        x2 = int(origSize[0] - xResize/2)
        bPoint = (x2, origSize[1])
    cropPoint = aPoint + bPoint
    return cropPoint


def resizePages(imagesData):
    print(imagesData["demo"])

    origPathDemo = os.path.join(ORIGPATH, imagesData["demo"])
    destPathDemo = os.path.join(DESTPATH, imagesData["demo"])

    if not(os.path.isdir(destPathDemo)):
        os.mkdir(destPathDemo)

    amountPages = len(imagesData["data"])

    for i in range(amountPages):
        print(i+1, "/", amountPages)
        imageFileName = imagesData["data"][i]
        origPathImage = os.path.join(origPathDemo, imageFileName)
        destPathImage = os.path.join(destPathDemo, imageFileName)
        imageData = openImage(origPathImage)
        if getAspectRatio(imageData.size) != 0.6:
            newSize = calculateResize(imageData.size)
            cropPoints = calculateResizePoint(imageData.size, newSize)
            newImageData = imageData.crop(cropPoints)
            saveImage(newImageData, destPathImage)
        else:
            saveImage(imageData, destPathImage)
    print("completed")
    return 0


def threadDataImages(path="./"):
    allDemoDirs = [dir for dir in os.listdir(
        path) if not(os.path.isfile(os.path.join(path, dir)))]
    responses = []

    for i in range(len(allDemoDirs)):
        demoFoldier = allDemoDirs[i]
        demoPath = os.path.join(path, allDemoDirs[i])

        responses.append({
            "demo": demoFoldier,
            "data": os.listdir(demoPath)
        })

    print("completed")
    return responses


imagesData = threadDataImages(ORIGPATH)
resizePages(imagesData[3])
