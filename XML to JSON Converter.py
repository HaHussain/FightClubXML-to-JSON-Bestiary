import re
import json


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


def SplitAbilities(Tag, MonsterText):
    AbilityList = []
    MonsterText = "".join(MonsterText.split("\n"))
    MonsterText = "".join(MonsterText.split("\t"))
    TempList = MonsterText.split("<"+Tag+">")
    for element in TempList:
        try:
            Ability = element[:element.index("</"+Tag+">")]
            AbilityList.append([])
            AbilityList[-1].append(Ability[Ability.index("<name>")+6:Ability.index("</name>")])
            AbilityList[-1].append("")
            Ability = "\n".join(Ability.split("<text />"))
            while True:
                AbilityList[-1][1] += Ability[Ability.index("<text>")+6:Ability.index("</text>")]
                Ability = Ability[(Ability.index("</text>")+7):]
                AbilityList[-1][1] += "\n"
        except ValueError:
            pass
    return AbilityList

def DealWithMonster(MonsterText):
    CreatureAttributes = {}
    CreatureAttributes["Name"] = (XMLRead("name", MonsterText)) #name
    CreatureAttributes.append(XMLRead("size", MonsterText)) #size
    CreatureAttributes += XMLRead("type", MonsterText).split(', ') #creature type and book name
    CreatureAttributes.append(XMLRead("alignment", MonsterText)) #alignment
    CreatureAttributes["AC"] = {}
    CreatureAC = (XMLRead("ac", MonsterText)).split(' ') #ac
    if len(CreatureAC) > 1:
        CreatureAttributes["AC"]["Notes"] = CreatureAC[1][1:-1]
    CreatureAttributes["AC"]["Value"] = CreatureAC[0]
    CreatureAttributes["HP"] = {}
    CreatureHP = re.split('+ | ',(XMLRead("hp", MonsterText)))
    if len(CreatureHP) > 1:
        if CreatureHP[1][-1] == ")":
            CreatureAttributes["HP"]["Notes"] = CreatureHP[1][1:-1]
        else:
            CreatureAttributes["HP"]["Notes"] = CreatureHP[1][1:]
    CreatureAttributes["HP"]["Value"] = CreatureHP[0]
    CreatureAttributes.append(XMLRead("speed", MonsterText).split(', '))
    CreatureAttribures["Abilities"] = {}
    CreatureAttributes["Abilities"]["Str"] = (XMLRead("str", MonsterText))
    CreatureAttributes["Abilities"]["Dex"] = (XMLRead("dex", MonsterText))
    CreatureAttributes["Abilities"]["Con"] = (XMLRead("con", MonsterText))
    CreatureAttributes["Abilities"]["Int"] = (XMLRead("int", MonsterText))
    CreatureAttributes["Abilities"]["Wis"] = (XMLRead("wis", MonsterText))
    CreatureAttributes["Abilities"]["Cha"] = (XMLRead("cha", MonsterText))
    CreatureAttributes.append(XMLRead("save", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("skill", MonsterText).split(', '))
    CreatureAttributes.append(MonsterElementalAffinities("resist", MonsterText))
    CreatureAttributes.append(MonsterElementalAffinities("immune", MonsterText))
    CreatureAttributes.append(MonsterElementalAffinities("vulnerable", MonsterText))
    CreatureAttributes.append(XMLRead("conditionImmune", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("senses", MonsterText).split(', '))
    CreatureAttributes.append(XMLRead("languages", MonsterText).split(', '))
    CreatureAttributes["Challenge"] = (XMLRead("cr", MonsterText))

    CreatureAttributes.append(SplitAbilities("trait", MonsterText))
    CreatureAttributes.append(SplitAbilities("action", MonsterText))
    CreatureAttributes.append(SplitAbilities("reaction", MonsterText))
    CreatureAttributes.append(SplitAbilities("legendary", MonsterText))
    return CreatureAttributes


XML = open(".\\Mordenkainens Tome of Foes.xml")
while True:
    MonsterText = ""
    XMLLine = XML.readline()
    if re.search('<monster>', XMLLine) != None:
        while re.search('</monster>', XMLLine) == None:
            XMLLine = XML.readline()
            MonsterText += XMLLine
        MonsterList.append(DealWithMonster(MonsterText))
    elif XMLLine == '':
        break
XML.close()
JSON = open(".\\myMonsters.json","w+")
