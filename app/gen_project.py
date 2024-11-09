from csv_handler import CsvHandler

if __name__ == "__main__":
    csvHandler = CsvHandler()
    cromsMap = csvHandler.readCromToGinFile()
    print(cromsMap)
    cromsData = csvHandler.readMorbidmapFile()
    listGenesCroms = cromsData["Croms"]
    mapResults = csvHandler.colcGenesOfDiseases(cromsData)
    mapPercentage = csvHandler.colcPercentage(cromsMap, mapResults, listGenesCroms)
    print(mapPercentage)
    cromoWithMaxGenesRelevantToDiseases = max(mapPercentage, key=mapPercentage.get)
    print("THE ANSWER : " + cromoWithMaxGenesRelevantToDiseases + " : " + str(mapPercentage[cromoWithMaxGenesRelevantToDiseases] * 100) + "%")
