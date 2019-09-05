run:
	vlog top_module.v >> cmpresult
	vsim -c -do sim.do top_module


clean:
	rm sim.lst
	rm *.wlf
	rm -r work
	rm transcript
	rm var_name
	rm cmpresult
	rm stim.do
	rm sim.do
	rm signal.json
	rm top_module.v
