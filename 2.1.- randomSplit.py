# TODO: Crear un script que distribuya de manera aleatoria el dataset resultante de "1.3.- resizedPages.py" en una proporcion de 60% en la carpeta "2.0.- train", 20% en la carpeta "2.1.- validacion" y 20% en la carpeta "2.2.- test".

import random
import shutil
import os

# Ruta de origen de las imagenes
ORIGPATH = os.path.join(
    "../",
    "1.- Etapas_preprocesamiento",
    "1.4.- crooppedPagesSame"
)

# Rutas de destino de las imagenes
TRAIPATH = os.path.join("./", "1.- train")
VALIPATH = os.path.join("./", "2.- validation")
TESTPATH = os.path.join("./", "3.- test")

# Porcentajes de distribucion de la base de datos
TRAIPERCENT = 0.6
VALIPERCENT = 0.2
TESTPERCENT = 0.2


def createFoldier(foldierPath):
    if not(os.path.isdir(foldierPath)):
        os.mkdir(foldierPath)
    return 0


def copyPages(pagesList, origPath, destPath):
    print("Ruta de origen: ", origPath)
    print("RUta de destino", destPath)
    for page in pagesList:
        origPagePath = os.path.join(origPath, page)
        destPagePath = os.path.join(destPath, page)
        shutil.copy(origPagePath, destPagePath)
    print("COPY COMPLETED")
    return 0


def removeElementList(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result


def selectPages(pagesData):
    print(pagesData["demo"])

    origPathDemo = os.path.join(ORIGPATH, pagesData["demo"])

    destPathDemoTrai = os.path.join(TRAIPATH, pagesData["demo"])
    createFoldier(destPathDemoTrai)

    destPathDemoVali = os.path.join(VALIPATH, pagesData["demo"])
    createFoldier(destPathDemoVali)

    destPathDemoTest = os.path.join(TESTPATH, pagesData["demo"])
    createFoldier(destPathDemoTest)

    pages = os.listdir(origPathDemo)
    amountPages = len(pages)

    amountTrai = int(amountPages * TRAIPERCENT)
    amountVali = int(amountPages * VALIPERCENT)
    amountTest = int(amountPages * TESTPERCENT)  # No es necesario

    # Seleccionar las paginas para ENTRENAMIENTO y copiarlas
    randomTraiList = random.sample(range(1, amountPages), amountTrai)
    selectTraiPages = [pages[num] for num in randomTraiList]
    copyPages(selectTraiPages, origPathDemo, destPathDemoTrai)

    # Descartar las paginas seleccionadas para ENTRENAMIENTO
    pages = removeElementList(pages, selectTraiPages)
    amountPages = len(pages)
    print("1: ", amountPages)

    # Seleccionar las paginas para VALIDACION y copiarlas
    randomValiList = random.sample(range(1, amountPages), amountVali)
    selectValiPages = [pages[num] for num in randomValiList]
    copyPages(selectValiPages, origPathDemo, destPathDemoVali)

    # Descartar las paginas seleccionadas para VALIDACION
    pages = removeElementList(pages, selectValiPages)
    amountPages = len(pages)
    print("2: ", amountPages)

    # Copiar las paginas para ENTRENAMIENTO
    # Seleccion por descarte (Solo quedan la cantidad respectiva de paginas dentro de "pages")
    selectTestPages = pages
    copyPages(selectTestPages, origPathDemo, destPathDemoTest)

    # Descartar las paginas seleccionadas para ENTRENAMIENTO
    pages = removeElementList(pages, selectTestPages)
    amountPages = len(pages)

    print("COMPLETED")

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
selectPages(imagesData[0])
