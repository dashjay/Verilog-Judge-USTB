#!/usr/local/python/bin/python3

def getvar():
    import re

    f = open("./top_module.v",'r')
    content = f.read()

    patten = r'top_module\((.*?)\)'

    string = re.findall(patten,content,re.S)[0].split(',')
    #print(string)
    result = []
    for i in string:
        if '[' in i:
            var = re.findall('](.*?)$',i)[0]
            result.append(var.strip())
    
        else:
            temp = i.split(" ")
            index = -1

            while(temp[index] == ''):
                index = index - 1
            result.append(temp[index].strip())
    f = open('var_name','w')
    for i in result:
        f.write('{0} '.format(i))
    f.close()
