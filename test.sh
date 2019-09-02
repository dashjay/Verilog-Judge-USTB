wget --quiet \
  --method POST \
  --header 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  --header 'cache-control: no-cache' \
  --header 'Postman-Token: c791c741-4721-4f52-ad79-560c56e1eb5e' \
  --body-data '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="top_module"\r\n\r\nmodule top_module(\n	input [3:0] a,\n	input [3:0] b,\n	output reg[7:0] p\n);\n\n	reg [7:0] pv;\n	reg [7:0] ap;\n	integer i;\n\n	always@(*)\n	begin\n		pv = 8'\''b00000000;\n		ap = {4'\''b0000,a};\n		for(i = 0; i<=3; i=i+1)\n			begin\n				if(b[i]==1)\n					pv = pv + ap;\n					ap = {ap[6:0],1'\''b0};\n			end\n		p = pv;\n	end\nendmodule\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name="stim"\r\n\r\nadd wave a\nadd wave b\nadd wave p\nforce a 16#0x8\nforce b 16#0xa\nrun 1000\nforce b 16#0x2\nrun 1000\nforce b 16#0x3\nrun 1000\nforce b 16#0x4\nrun 1000\nforce b 16#0x5\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--' \
  --output-document \
  - http://localhost:33778/solve
