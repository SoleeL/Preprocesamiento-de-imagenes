# TODO: Crear un script que renombre todas las paginas segun id_page

# id_page: {1}{01}{001} -> {4}{40}{500}
# {1 -> 4}: Demografia del manga
# {01 -> 40}: Numero del manga en la base de datos
# {001 -> 500}: Numero de la pagina en el manga

import os
from threading import Thread


def changeName(oldName, newName):
    os.rename(oldName, newName)
    return 0


def threadsChangeName(path="./"):
    allDemoDirs = [dir for dir in os.listdir(
        path) if not(os.path.isfile(os.path.join(path, dir)))]

    threads = []
    for demoDir in allDemoDirs:
        demographics = demoDir[:1]

        demoPath = os.path.join(path, demoDir)
        allTitleDirs = os.listdir(demoPath)
        for titleDir in allTitleDirs:
            title = titleDir[:2]

            titlePath = os.path.join(demoPath, titleDir)
            allPageDirs = os.listdir(titlePath)
            for pageDir in allPageDirs:
                name = demographics + title + pageDir

                oldName = os.path.join(titlePath, pageDir)
                newName = os.path.join(titlePath, name)

                threads.append(
                    Thread(target=changeName, args=(oldName, newName,)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish
    print("completed")
    return 0


threadsChangeName()
