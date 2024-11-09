import csv
from constants import CROMTOGENE, MORBIDMAP
from collections import Counter

class CsvHandler:

    def __init__(self):
        self.filePath = None

    def readCromToGinFile(self):
        with open(CROMTOGENE, 'r+') as csvfile:
            reader = csv.reader(csvfile)
            chromosomeArray = []
            proteinCodingGeneArray = []
            cromsMap = {}

            for row in reader:
                chromosomeArray.append(row[0])
                proteinCodingGeneArray.append(row[4])

            for index in range(len(chromosomeArray)):
                if index != 0:
                    cromsMap[chromosomeArray[index]] = proteinCodingGeneArray[index]

            return cromsMap


    def readMorbidmapFile(self):
        with open(MORBIDMAP, 'r+') as csvfile:
            answer = {}
            reader = csv.reader(csvfile)
            cromsArray = []
            mapCromToDisease = {}
            for row in reader:
                cromNumber = self.__getCromNameFromCytoLocation(row[3])

                if (not cromNumber in cromsArray) & (cromNumber != 'X') & (cromNumber != 'Y'):
                    cromsArray.append(cromNumber)

                if not cromNumber in mapCromToDisease:
                    mapCromToDisease[cromNumber] = []
                    #mapCromToDisease[cromNumber].append({row[2]: row[0]})
                    mapCromToDisease[cromNumber].append(row[0])
                else:
                    #mapCromToDisease[cromNumber].append({row[2]: row[0]})
                    mapCromToDisease[cromNumber].append(row[0])

            answer["Croms"] = cromsArray
            answer["Map"] = mapCromToDisease
        return answer

    def colcGenesOfDiseases(self, answer):
        mapCromToNumOfGenes = {}

        for cromo in answer["Croms"]:
            counterList = Counter(answer["Map"][cromo])
            #print("len : " + cromo + " " + str(len(answer["Map"][cromo])))
            counter = 0
            for currAnswer in answer["Map"][cromo]:
                if counterList[currAnswer] == 1:
                    counter = counter + 1
                elif counterList[currAnswer] > 1:
                    isCounted = False
                    if not isCounted:
                        counter = counter + 1
                        isCounted = True
            mapCromToNumOfGenes[cromo] = counter
        return mapCromToNumOfGenes

    def colcPercentage(self, mapTotleGene, mapGenesLinkedToDiseases, listGenesCroms):
        percentageMap  = {}
        for crom in listGenesCroms:
            if (crom in mapGenesLinkedToDiseases) & (crom in mapTotleGene):
                #print(crom + " " + str(mapGenesLinkedToDiseases[crom]) + " " + str(mapTotleGene[crom]))
                percentage = int(mapGenesLinkedToDiseases[crom]) / int(mapTotleGene[crom])
                percentageMap[crom] = percentage
        return percentageMap


    def __fullCromNameToCronNumber(self, fullNameArray):
        map = {}
        for currFullName in fullNameArray:
            map[currFullName] = self.__getCromNameFromCytoLocation(currFullName)
        return map

    def __createCromsArray(self, cytoLocationArray):
        cromsArray = []
        for elem in cytoLocationArray:
            if not (elem in cromsArray):
                cromsArray.append(self.__getCromNameFromCytoLocation(elem))
        return cromsArray

    def __getCromNameFromCytoLocation(self, cytoLocationString):
        cromNumberString = ''
        if 'p' in cytoLocationString:
            cromNumberString = cytoLocationString.split('p')[0]
        elif 'q' in cytoLocationString:
            cromNumberString = cytoLocationString.split('q')[0]
        return str(cromNumberString)

