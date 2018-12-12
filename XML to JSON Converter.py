import re

MonsterList = []
XML = open(".\\Mordenkainens Tome of Foes.xml")

def XMLRead(Tag, MultiOutput = 0):
    XMLOutput = re.search('<'+ Tag +'>(.*)</'+ Tag +'>', XML.readline())
    if XMLOutput != None:
        return XMLOutput.group(1)
    else:
        return ""

while True:
    Line = XML.readline()
    if Line == "    <monster>\n":
        MonsterName = XMLRead("name")
        MonsterSize = XMLRead("size")
        MonsterTemp = XMLRead("type").split(', ')
        MonsterType = MonsterTemp[0]
        MonsterBook = MonsterTemp[1]
        MonsterAlignment = XMLRead("alignment")
        MonsterAC = XMLRead("ac")
        MonsterHP = XMLRead("hp")
        MonsterSpeeds = XMLRead("speed").split(', ')
        MonsterSTR = XMLRead("str")
        MonsterDEX = XMLRead("dex")
        MonsterCON = XMLRead("con")
        MonsterINT = XMLRead("int")
        MonsterWIS = XMLRead("wis")
        MonsterCHA = XMLRead("cha")
        MonsterSaves = XMLRead("save").split(', ')
        MonsterSkills = XMLRead("skill").split(', ')

        MonsterResistances = XMLRead("resist")
        MonsterResistances2 = re.search('(.*); (.*)', MonsterResistances)
        if MonsterResistances2 == None:
            if re.search('and', MonsterResistances) != None:
                MonsterResistanceList = [MonsterResistances]
            else:
                MonsterResistanceList = (MonsterResistances).split(', ')
        elif MonsterResistances2 != None:
            MonsterResistanceList = (MonsterResistances2.group(1)).split(', ')
            MonsterResistanceList.append(MonsterResistances2.group(2))

        MonsterImmunities = XMLRead("immune")
        MonsterImmunities2 = re.search('(.*); (.*)', MonsterImmunities)
        if MonsterImmunities2 == None:
            if re.search('and', MonsterImmunities) != None:
                MonsterImmunityList = [MonsterImmunities]
            else:
                MonsterImmunityList = (MonsterImmunities).split(', ')
        elif MonsterImmunities2 != None:
            MonsterImmunityList = (MonsterImmunities2.group(1)).split(', ')
            MonsterImmunityList.append(MonsterImmunities2.group(2))

        MonsterList.append([MonsterName, MonsterSize, MonsterType, MonsterBook])
        print(MonsterList[-1])
        print(MonsterImmunityList)
    elif Line == "":
        break
