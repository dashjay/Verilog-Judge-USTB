def write_string(file_string, filename):
    f=open(filename, 'w')
    f.write(file_string)
    f.flush()
    f.close()

def getparam(stim):
    params=re.findall("wave (.*?)\n", stim)
    if len(params) <= 0:
        return False
    sim_part=""
    for param in params:
        sim_part=sim_part + 'add list -hexadecimal /top_module/' + param + '\n'
    write_string(sim_part, 'sim.do')
    os.system('cat sim.do.example >> sim.do')
    return True



def try_get(filename):
    try:
        file=open(filename, 'r')
        return file.read()
    except Exception as e:
        print(e)
        return ""
