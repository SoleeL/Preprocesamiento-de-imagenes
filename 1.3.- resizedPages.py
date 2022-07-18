# TODO: Crear un script que redimensione las pages a 135x225 pixeles, y las guarde en la carpeta "1.3.- resizedPages".

import os
from PIL import Image
import PIL

ORIGPATH = os.path.join("./", "1.2.- croppedPages")
DESTPATH = os.path.join("./", "1.3.- resizedPages")
FIXESHEIGHT = 225


def openImage(path):
    image = Image.open(path)
    image = image.convert('RGB')
    return image


def saveImage(imageData, destPath):
    imageData.save(destPath)
    return 0


def calculateHeightPercent(heigtImage, fixedHeight):
    heightPercent = (fixedHeight / float(heigtImage))
    return heightPercent


def calculateWidthSize(widthImage, heightPercent):
    widthSize = int(float(widthImage * float(heightPercent)))
    return widthSize


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
        heightPercent = calculateHeightPercent(imageData.size[1], FIXESHEIGHT)
        widthSize = calculateWidthSize(imageData.size[0], heightPercent)
        newImageData = imageData.resize(
            (
                widthSize,
                FIXESHEIGHT
            ),
            PIL.Image.NEAREST
        )
        saveImage(newImageData, destPathImage)

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
