import handleFile

data= handleFile.readJsonFile('/sample.json')
print(data)


if data != '':
    start = data["scripts"]['devStart']
    test= data["scripts"]['test']
    
    dev = test + start
    

    