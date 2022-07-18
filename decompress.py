import os
import shutil
import random

from threading import Thread


# PASO 1: Cambiar los nombres de cada pagina para que tengan un numeral al principio.
def changeDefaultNamePage(path="./"):
    chapters = [dir for dir in os.listdir(path) if not(
        os.path.isfile(os.path.join(path, dir)))]

    for chapter in chapters:
        chapterPath = os.path.join(path, chapter)
        print("DIRECCION: ", chapterPath)
        pages = os.listdir(chapterPath)
        for i in range(len(pages)):
            prefixed = str(i+1) + " - "
            postfixed = pages[i]
            name = prefixed + postfixed
            nameLength = len(name) + 2
            name = name.rjust(nameLength, "0")
            oldName = os.path.join(chapterPath, pages[i])
            newName = os.path.join(chapterPath, name)
            os.rename(oldName, newName)

    print("Completed")
    return 0


def threadsChangeDefaultNamePage(path="./"):
    dirs = os.listdir(path)
    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=changeDefaultNamePage, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


# PASO 2: Llevar todas las paginas de cada capitulo al directorio raiz del manga
def rootDecompress(path="./"):
    foldiers = [dir for dir in os.listdir(
        path) if not(os.path.isfile(os.path.join(path, dir)))]

    for foldier in foldiers:
        folderPath = os.path.join(path, foldier)
        print("DIRECCION: ", folderPath)
        files = os.listdir(folderPath)
        for file in files:
            filePath = os.path.join(folderPath, file)
            fileDest = os.path.join(path, file)
            print("    ", filePath, "moved to", fileDest)
            shutil.move(filePath, fileDest)
        os.rmdir(folderPath)
    print("Completed")
    return 0


def threadsRootDecompress(path="./"):
    dirs = os.listdir(path)
    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=rootDecompress, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


# PASO 3: Seleccion de 500 paginas y su movimiento al directorio "./select"
def selectPages(path="./", select="select", mount=500):
    files = os.listdir(path)

    randomList = random.sample(range(1, len(files)), mount)
    print(len(files))
    print(randomList)
    selectPages = [files[num] for num in randomList]
    selectDir = os.path.join(path, select)
    os.mkdir(selectDir)
    for page in selectPages:
        filePath = os.path.join(path, page)
        print("    ", filePath, "moved to", selectDir)
        shutil.move(filePath, selectDir)
        print(page)
    print("Completed")
    return 0


def threadsSelectPages(path="./"):
    dirs = os.listdir(path)
    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=selectPages, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


# PASO 4: Eliminar todas las paginas del directorio raiz "./" menos el directorio "./select"
def delRePages(path="./"):
    files = [os.path.join(path, dir) for dir in os.listdir(
        path) if os.path.isfile(os.path.join(path, dir))]

    for file in files:
        os.remove(file)
    print("Completed")
    return 0


def threadsDelRePages(path="./"):
    dirs = os.listdir(path)
    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=delRePages, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


# PASO 5: Mover las 500 paginas del directorio "./select" al directorio raiz "./"
def movPagesSelected(path="./"):

    selectDir = os.path.join(path, "select")
    pages = os.listdir(selectDir)

    for page in pages:
        filePath = os.path.join(selectDir, page)
        print("    ", filePath, "moved to", path)
        shutil.move(filePath, path)
    os.rmdir(selectDir)
    print("Completed")
    return 0


def threadsMovPagesSelected(path="./"):
    dirs = os.listdir(path)
    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=movPagesSelected, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


# PASO 6: Cambiar los nombres de las paginas a numerales del 1 al 500.
def changeNamePage(path="./"):
    pages = os.listdir(path)
    for i in range(len(pages)):
        name = str(i+1)+".jpg"
        name = name.rjust(7, "0")
        oldName = os.path.join(path, pages[i])
        newName = os.path.join(path, name)
        os.rename(oldName, newName)
        print("    ", oldName, "rename to", newName)
    print("Completed")
    return 0


def threadsChangeNamePage(path="./"):
    dirs = os.listdir(path)
    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=changeNamePage, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


# threadsChangeDefaultNamePage()
# threadsRootDecompress()
# threadsSelectPages()
threadsDelRePages()
threadsMovPagesSelected()
threadsChangeNamePage()
