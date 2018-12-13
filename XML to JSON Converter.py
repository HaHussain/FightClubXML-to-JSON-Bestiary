import re

MonsterList = []

def XMLRead(Tag, MonsterText):
    XMLOutput = re.search('<'+ Tag +'>(.*)</'+ Tag +'>', MonsterText)
    if XMLOutput != None:
        return XMLOutput.group(1)
    else:
        return ""

def MonsterElementalAffinities(Tag, MonsterText):
    MonsterAffinities = XMLRead(Tag, MonsterText)
    MonsterAffinities2 = re.search('(.*); (.*)', MonsterAffinities)
    if MonsterAffinities2 == None:
        if re.search('and', MonsterAffinities) != None:
            MonsterAffinityList = [MonsterAffinities]
        else:
            MonsterAffinityList = (MonsterAffinities).split(', ')
    elif MonsterAffinities2 != None:
        MonsterAffinityList = (MonsterAffinities2.group(1)).split(', ')
        MonsterAffinityList.append(MonsterAffinities2.group(2))
    return MonsterAffinityList

def DealWithMonster(MonsterText):
    CreatureAttributes = []
    CreatureAttributes.append(XMLRead("name", MonsterText)) #name
    CreatureAttributes.append(XMLRead("size", MonsterText)) #size
    CreatureAttributes += XMLRead("type", MonsterText).split(', ') #creature type and book name
    CreatureAttributes.append(XMLRead("alignment", MonsterText)) #alignment
    CreatureAttributes.append(XMLRead("ac", MonsterText)) #ac
    CreatureAttributes.append(XMLRead("hp", MonsterText)) #hp
    CreatureAttributes.append(XMLRead("speed", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("str", MonsterText))
    CreatureAttributes.append(XMLRead("dex", MonsterText))
    CreatureAttributes.append(XMLRead("con", MonsterText))
    CreatureAttributes.append(XMLRead("int", MonsterText))
    CreatureAttributes.append(XMLRead("wis", MonsterText))
    CreatureAttributes.append(XMLRead("cha", MonsterText))
    CreatureAttributes.append(XMLRead("save", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("skill", MonsterText).split(', '))
    CreatureAttributes.append(MonsterElementalAffinities("resist", MonsterText))
    CreatureAttributes.append(MonsterElementalAffinities("immune", MonsterText))
    CreatureAttributes.append(MonsterElementalAffinities("vulnerable", MonsterText))
    CreatureAttributes.append(XMLRead("conditionImmune", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("senses", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("languages", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("cr", MonsterText))
    return CreatureAttributes

XML = open(".\\Tome of Beasts.xml")
while True:
    MonsterText = ""
    XMLLine = XML.readline()
    if re.search('<monster>', XMLLine) != None:
        while re.search('</monster>', XMLLine) == None:
            XMLLine = XML.readline()
            MonsterText += XMLLine
        print(DealWithMonster(MonsterText))
    elif XMLLine == '':
        break


# while True:
#     Line = XML.readline()
#     if Line == "    <monster>\n":
#         MonsterName = XMLRead("name")
#         MonsterSize = XMLRead("size")
#         MonsterTemp = XMLRead("type").split(', ')
#         MonsterType = MonsterTemp[0]
#         MonsterBook = MonsterTemp[1]
#         MonsterAlignment = XMLRead("alignment")
#         MonsterAC = XMLRead("ac")
#         MonsterHP = XMLRead("hp")
#         MonsterSpeeds = XMLRead("speed").split(', ')
#         MonsterSTR = XMLRead("str")
#         MonsterDEX = XMLRead("dex")
#         MonsterCON = XMLRead("con")
#         MonsterINT = XMLRead("int")
#         MonsterWIS = XMLRead("wis")
#         MonsterCHA = XMLRead("cha")
#         MonsterSaves = XMLRead("save").split(', ')
#         MonsterSkills = XMLRead("skill").split(', ')
#
#         MonsterResistances = XMLRead("resist")
#         MonsterResistances2 = re.search('(.*); (.*)', MonsterResistances)
#         if MonsterResistances2 == None:
#             if re.search('and', MonsterResistances) != None:
#                 MonsterResistanceList = [MonsterResistances]
#             else:
#                 MonsterResistanceList = (MonsterResistances).split(', ')
#         elif MonsterResistances2 != None:
#             MonsterResistanceList = (MonsterResistances2.group(1)).split(', ')
#             MonsterResistanceList.append(MonsterResistances2.group(2))
#
#         MonsterImmunities = XMLRead("immune")
#         MonsterImmunities2 = re.search('(.*); (.*)', MonsterImmunities)
#         if MonsterImmunities2 == None:
#             if re.search('and', MonsterImmunities) != None:
#                 MonsterImmunityList = [MonsterImmunities]
#             else:
#                 MonsterImmunityList = (MonsterImmunities).split(', ')
#         elif MonsterImmunities2 != None:
#             MonsterImmunityList = (MonsterImmunities2.group(1)).split(', ')
#             MonsterImmunityList.append(MonsterImmunities2.group(2))
#
#         MonsterList.append([MonsterName, MonsterSize, MonsterType, MonsterBook])
#         print(MonsterList[-1])
#         print(MonsterImmunityList)
#     elif Line == "":
#         break
