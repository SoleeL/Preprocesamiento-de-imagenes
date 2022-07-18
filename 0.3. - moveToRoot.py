# TODO: Crear un script que mueva todas las paginas al directorio raiz de su demografia.

import os
import shutil
from threading import Thread


def rootDecompress(path="./"):
    allTitleDirs = [dir for dir in os.listdir(
        path) if not(os.path.isfile(os.path.join(path, dir)))]

    for titleDir in allTitleDirs:
        titlePath = os.path.join(path, titleDir)
        pages = os.listdir(titlePath)
        for page in pages:
            filePath = os.path.join(titlePath, page)
            fileDest = os.path.join(path, page)
            print("    ", filePath, "moved to", fileDest)
            shutil.move(filePath, fileDest)
        os.rmdir(titlePath)
    print("Completed")
    return 0


def threadsRootDecompress(path="./"):
    dirs = [dir for dir in os.listdir(path) if not(
        os.path.isfile(os.path.join(path, dir)))]

    threads = []
    for dir in dirs:
        pathDir = os.path.join(path, dir)
        threads.append(Thread(target=rootDecompress, args=(pathDir,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    return 0


threadsRootDecompress()
