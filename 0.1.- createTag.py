# TODO: Crear un script que recopile la data de la base de datos en un .csv, y lo guarde en el directorio raiz "./".

import os
import csv

from threading import Thread

# CSV DATA
fieldnames = ["id_demographics", "demographics",
              "id_title", "title", "id_page", "page"]


def getIdsPage(path, listIdsPage):
    listIdsPage.extend(os.listdir(path))
    return 0


def threadsGetIdsPage(path="./"):
    dirs = foldiers = [dir for dir in os.listdir(
        path) if not(os.path.isfile(os.path.join(path, dir)))]
    threads = []
    responses = []

    for i in range(len(dirs)):
        responses.append({
            "title": dirs[i],
            "data": []
        })

        pathDir = os.path.join(path, dirs[i])

        threads.append(
            Thread(target=getIdsPage, args=(pathDir, responses[i]["data"],)))

    [t.start() for t in threads]  # start all threads
    [t.join() for t in threads]  # block until all threads finish

    return responses


def demographicsDataPages(path="./"):
    dirs = foldiers = [dir for dir in os.listdir(
        path) if not(os.path.isfile(os.path.join(path, dir)))]
    responses = []
    for i in range(len(dirs)):
        responses.append({
            "demographics": dirs[i],
            "data": []
        })
        pathDir = os.path.join(path, dirs[i])
        responses[i]["data"] = threadsGetIdsPage(pathDir)
    return responses


def formatPagesData(allDemoData):
    responses = []
    for demoData in allDemoData:
        demographics = demoData["demographics"]
        for titleData in demoData["data"]:
            title = titleData["title"]
            if len(titleData["data"]) != 500:
                print("CUIDADO", title)
            for pageData in titleData["data"]:
                idPage = pageData
                pageDatawithFormat = {
                    "id_demographics": demographics[:1],
                    "demographics": demographics[4:],
                    "id_title": title[:2],
                    "title": title[5:],
                    "id_page": idPage[:3],
                    "page": idPage}
                responses.append(pageDatawithFormat)
    return responses


def saveCSVDatasetMangas(datasetMangas, fieldnames):
    with open('tags.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(datasetMangas)
    return None


allIdsPages = demographicsDataPages()

demoData = list(formatPagesData(allIdsPages))

saveCSVDatasetMangas(demoData, fieldnames)
