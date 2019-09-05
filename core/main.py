from flask import Flask, request, json, jsonify
import os
import re
app = Flask(__name__)

@app.route('/hello',methods=['POST'])
def hello():
    return 'ok'

@app.route('/solve', methods=['POST'])
def judge():
    # 将top_module写入当前目录当中
    form_dict = request.form.to_dict()

    if 'top_module' not in form_dict.keys():
        return json.dumps({'status':0,'msg':'top_module is required'})

    top_module = form_dict['top_module']
    write_string(top_module, 'top_module.v')

    if 'stim' not in form_dict.keys():
        return json.dumps({'status':0,'msg':'stim is required'})

    stim = form_dict['stim']
    write_string(stim,'stim.do')
    #编译
    os.system('rm cmpresult')
    cmpresult = cmp()

    errornum = int(re.findall('Errors: (.*?),',cmpresult.split('\n')[-2])[0])
    warningnum = int(re.findall('Warnings: (.*?)$',cmpresult.split('\n')[-2])[0])

    if errornum > 0:
        return json.dumps({'status': 0, 'cmpcode':0,'cmpresult': cmpresult})

    simresult = sim()
    diagram()
    signal = try_get('signal.json')
    if  signal == "":
        code = 0
    else:
        code = 1

    os.system('make clean')
    return json.dumps({'status': code, 'cmpcode':1,'cmpresult': cmpresult, 'signal': signal})

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

app.run(host='0.0.0.0',port=5000)
