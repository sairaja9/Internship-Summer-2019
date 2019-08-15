import json
#from copy import deepcopy

class node:
    botBanelings = -1
    botImmortals = -1
    botMarines = -1
    topBanelings = -1
    topImmortals = -1
    topMarines = -1
    pylons = -1
    name = "404"

def processTree(root, outFile):
    myNode = node()
    #childKeys = []

    # iterate over the keys
    for key in root:
        # determine if the key is a child node via a terrible hack
        #if key[:2] == "dp":
            #childKeys.append(key)
        if key == "BOT Banelings":
            myNode.botBanelings = root[key]
        elif key == "TOP Banelings":
            myNode.topBanelings = root[key]
        elif key == "BOT Marines":
            myNode.botMarines = root[key]
        elif key == "TOP Marines":
            myNode.topMarines = root[key]
        elif key == "BOT Immortals":
            myNode.botImmortals = root[key]
        elif key == "TOP Immortals":
            myNode.topImmortals = root[key]
        elif key == "Pylons":
            myNode.pylons = root[key]
        elif key == "name":
            myNode.name = root[key]

    if "state" in myNode.name:
        # enemyNode = deepcopy(myNode)
        # enemyNode.name += "_enemy"
        # enemyNode.topMarine = root["state"][8]
        # enemyNode.topBanelings = root["state"][9]
        # enemyNode.topImmortal = root["state"][10]
        # enemyNode.botMarine = root["state"][11]
        # enemyNode.botBanelings = root["state"][12]
        # enemyNode.botImmortal = root["state"][13]
        # enemyNode.pylons = root['state'][14]

        # outFile.write(enemyNode.name + "\t")
        # outFile.write(str(enemyNode.pylons) + "\t")
        # outFile.write(str(enemyNode.botMarines) + "\t" + str(enemyNode.topMarines) + "\t")
        # outFile.write(str(enemyNode.botBanelings) + "\t" + str(enemyNode.topBanelings) + "\t")
        # outFile.write(str(enemyNode.botImmortals) + "\t" + str(enemyNode.topImmortals) + "\n")

        outFile.write(myNode.name + "_enemy" + "\t")
        outFile.write(str(root['state'][14]) + "\t")
        outFile.write(str(root['state'][11]) + "\t" + str(root['state'][8]) + "\t")
        outFile.write(str(root['state'][12]) + "\t" + str(root['state'][9]) + "\t")
        outFile.write(str(root['state'][13]) + "\t" + str(root['state'][10]) + "\n")

    outFile.write(myNode.name + "\t")
    outFile.write(str(myNode.pylons) + "\t")
    outFile.write(str(myNode.botMarines) + "\t" + str(myNode.topMarines) + "\t")
    outFile.write(str(myNode.botBanelings) + "\t" + str(myNode.topBanelings) + "\t")
    outFile.write(str(myNode.botImmortals) + "\t" + str(myNode.topImmortals) + "\n")

    # Make recursive calls. Unfortunately need to use a different loop to avoid iterator problems
    #for key in childKeys:
        #print(root[key])
        #processTree(root[key], outFile)

    for MyList in root['children']:
        for i in MyList:
            processTree(i, outFile)
            


inFile = open("partial_decision_point_1.json", "r") #FIXME check this ptr
outFile = open("DP1parsed.txt", "w") #FIXME check this ptr

# write down headers in txt file
outFile.write("Name\tPylons\tBOT Marines\tTOP Marines\tBOT Banelings\tTOP Banelings\tBOT Immortals\tTOP Immortals\n")

data = json.loads(inFile.read())

processTree(data, outFile)
outFile.close()

# json.dump(data, outFile, sort_keys=True, indent=4)

