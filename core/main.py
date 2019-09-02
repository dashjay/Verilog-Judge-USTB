from flask import Flask, request, json, jsonify
import os

app = Flask(__name__)


@app.route('/solve', methods=['POST'])
def judge():
    # 将top_module写入当前目录当中
    if request.method == 'POST':
        top_module = request.form['top_module']
        write_string(top_module, 'top_module.v')

        stim = request.form['stim']
        write_string(stim,'stim.do')

    #编译
    cmpresult = cmp()

    simresult = sim()
    
    diagram()

    signal = try_get('signal.json')

    if  signal == "":
        code = 0
    else:
        code = 1

    # os.system('make clean')
    return json.dumps({'status': code,'comresult': cmpresult, 'signal': signal})


def write_string(file_string, filename):
    f = open(filename, 'w')
    f.write(file_string)
    f.flush()
    f.close()

def cmp():
    os.system("vlog top_module.v >> cmpresult")
    cmpresult = try_get('cmpresult')
    return cmpresult

def sim():
    os.system("vsim -c -do sim.do top_module")
    simresult = try_get('sim.lst')
    return simresult

def diagram():
    getvar()
    os.system("./generate.sh top_module")

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

def try_get(filename):
    try:
        file = open(filename, 'r')
        return file.read()
    except Exception as e:
        print(e)
        return ""

app.run()
