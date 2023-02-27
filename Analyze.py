import json
from Answer import *
from Options import *

def Analyze_text(text):
    text = text[0].lower() + text[1:]
    with open('Data\Languages\FR\Conversations\Input.json', 'r', encoding='utf-8') as jsonFile :
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    find = False

    for key in jsonObject :
        for line in jsonObject[key] :
            if line in text :
                find = True
                Answer('Data\Languages\FR\Conversations\Output.json', key)
                return
    
    if find == False :
        with open('Data\Languages\FR\Options\Input.json', 'r', encoding='utf-8') as jsonFile :
            jsonObject = json.load(jsonFile)
            jsonFile.close()
        for key in jsonObject :
            for line in jsonObject[key] :
                if line in text :
                    find = True
                    Options_choice(key, text)
                    return

    if find == False :
        Answer('Data\Languages\FR\Conversations\Output.json','error')
        return