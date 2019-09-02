# Verilog-Judge-USTB
来自北京科技大学某小组的一个verilog的评测沙箱，基于Flask编写

A verilog online judger from USTB, based on Flask-python 

### Usage

**构建**(build)

```
git clone https://github.com/dashjay/Verilog-Judge-USTB.git
cd Verilog-Judge-USTB
docker build . -t verilog-judge
```

**运行**(run)

```bash
docker run verilog-judge -v ./modelsim_ase:/root/modelsim_ase -p 33778:5000
```

>  内部指定的modelsim_ase来自FPGA微软的免费软件Quartus Lite 中的modelsim组件
>
> docker内部运行的端口是5000，开在外部

**测试**(test)

```bash
chmod +x test.sh
python test.py | python -m json.tool
```

----

> 以下是测试输出
>
> The following is the test output

```json
{
    "cmpcode": 1,
    "cmpresult": "Start time: 07:46:33 on Sep 02,2019\nvlog top_module.v \nModel Technology ModelSim - Intel FPGA Edition vlog 10.5b Compiler 2016.10 Oct  5 2016\n-- Compiling module top_module\n\nTop level modules:\n\ttop_module\nEnd time: 07:46:34 on Sep 02,2019, Elapsed time: 0:00:01\nErrors: 0, Warnings: 0\n",
    "signal": "{\"signal\":[{\"name\":\"a\",\"wave\":\"==========\",\"data\":[\"/top_module/i\",\"8\",\"8\",\"8\",\"8\",\"8\"]},{\"name\":\"b\",\"wave\":\"==========\",\"data\":[\"a\",\"a\",\"2\",\"3\",\"4\"]},{\"name\":\"p\",\"wave\":\"==========\",\"data\":[\"xx\",\"50\",\"10\",\"18\",\"20\"]}]}\n",
    "status": 1
}
```

参数表

| 参数(parameter) | 值(value)                     |
| --------------- | ----------------------------- |
| top_module      | top_module.v字符串形式传送    |
| stim            | stim.v 激励文件字符串形式传送 |

### thanks

[Explainaur](https://github.com/orgs/806Cypher/people/Explainaur) 编写了最复杂的shell脚本

在下只写了点破Web服务并且测试了一下