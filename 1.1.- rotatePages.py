# TODO: Crear un script que rote las pages que su ancho sea mayor que su alto, y las guarde en la carpeta "1.1.- rotatePages".

import os
from PIL import Image
import PIL

ORIGPATH = os.path.join(
    "../", "0.- Dataset_original [Recopilacion de imagenes]")

DESTPATH = os.path.join("./", "1.1.- rotatePages/")

# TODO: Cargar todas las imagenes en formato RGB


def openImage(path):
    image = Image.open(path)
    image = image.convert('RGB')
    return image


def saveImage(imageData, destPath):

    imageData.save(destPath)
    return 0


def rotateImage(imageOrig):
    image = imageOrig.rotate(270, PIL.Image.NEAREST, expand=1)
    return image


def evaluationAspectRatio(imageData):
    if (imageData.height > imageData.width):
        return True
    else:
        return False


def evaluateImage(imagesData):
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
        if not(evaluationAspectRatio(imageData)):
            print("   ", imageFileName)
            print("        ", "ROTANDO")
            imageData = rotateImage(imageData)
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


# TODO: Crear funcion para contar cuantas imagenes tienen "anchura" mayor a su "altura"


def countAspectRatio(imagesData):
    countHeight = 0
    countWidth = 0

    print(imagesData["demo"])
    origPathDemo = os.path.join(ORIGPATH, imagesData["demo"])
    for imageFileName in imagesData["data"]:
        print("   ", imageFileName)
        origPathImage = os.path.join(origPathDemo, imageFileName)
        imageData = openImage(origPathImage)
        if evaluationAspectRatio(imageData):
            countHeight += 1
        else:
            countWidth += 1

    relationAspect = [countHeight, countWidth]
    print("completed")
    return relationAspect


imagesData = threadDataImages(ORIGPATH)
# print(imagesData[0]["demo"])
# print(countAspectRatio(imagesData[0]))

print(imagesData[2]["demo"])

evaluateImage(imagesData[2])
