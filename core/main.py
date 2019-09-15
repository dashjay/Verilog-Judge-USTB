from flask import Flask, request, json, jsonify
import os
import re
from grab import getvar
import wavedrom
from util import write_string, getparam, try_get
app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    return 'ok'


@app.route('/solve', methods=['POST'])
def judge():
    # 将top_module写入当前目录当中
    form_dict = request.form.to_dict()

    if 'top_module' not in form_dict.keys():
        return json.dumps({'status': 0, 'msg': 'top_module is required'})

    top_module = form_dict['top_module']
    write_string(top_module, 'top_module.v')

    if 'stim' not in form_dict.keys():
        return json.dumps({'status': 0, 'msg': 'stim is required'})

    stim = form_dict['stim']
    write_string(stim, 'stim.do')

    if not getparam(stim):
        return json.dumps({'status': 0, 'msg': 'your stim do not add any wave!'})
    # 编译
    os.system('rm cmpresult')
    cmpresult = cmp()

    errornum = int(re.findall('Errors: (.*?),', cmpresult.split('\n')[-2])[0])
    warningnum = int(re.findall('Warnings: (.*?)$',
                                cmpresult.split('\n')[-2])[0])

    if errornum > 0:
        return json.dumps({'status': 0, 'cmpcode': 0, 'cmpresult': cmpresult})

    simresult = sim()
    diagram()
    signal = try_get('signal.json')
    if signal == "":
        code = 0
    else:
        code = 1
        svg = render(signal)

    os.system('make clean')
    return json.dumps({'status': code, 'cmpcode': 1, 'cmpresult': cmpresult, 'signal': signal, 'svg': svg})

def cmp():
    os.system("vlog top_module.v >> cmpresult")
    cmpresult=try_get('cmpresult')
    return cmpresult


def sim():
    os.system("vsim -c -do sim.do top_module")
    simresult=try_get('sim.lst')
    return simresult


def diagram():
    getvar()
    os.system("./generate.sh top_module")


def render(wave):
    return wavedrom.render(wave).tostring()


app.run(host='0.0.0.0', port=5000)
