import requests

url = "http://localhost:33778/solve"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"top_module\"\r\n\r\nmodule top_module(\n\tinput [3:0] a,\n\tinput [3:0] b,\n\toutput reg[7:0] p\n);\n\n\treg [7:0] pv;\n\treg [7:0] ap;\n\tinteger i;\n\n\talways@(*)\n\tbegin\n\t\tpv = 8'b00000000;\n\t\tap = {4'b0000,a};\n\t\tfor(i = 0; i<=3; i=i+1)\n\t\t\tbegin\n\t\t\t\tif(b[i]==1)\n\t\t\t\t\tpv = pv + ap;\n\t\t\t\t\tap = {ap[6:0],1'b0};\n\t\t\tend\n\t\tp = pv;\n\tend\nendmodule\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"stim\"\r\n\r\nadd wave a\nadd wave b\nadd wave p\nforce a 16#0x8\nforce b 16#0xa\nrun 1000\nforce b 16#0x2\nrun 1000\nforce b 16#0x3\nrun 1000\nforce b 16#0x4\nrun 1000\nforce b 16#0x5\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'Postman-Token': "b2e96f20-02bf-470b-a8d0-5fd956120502"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
