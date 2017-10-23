'''
FUNC:R_1hxq_2_7_7_12
PDB:1hxq
EC:2.7.7.12
RESI:zn,fe
LOCI:a-350,351;
'''
import motifFunctions as cmd
ZN_FE = { 
	'distances':
		[31.79],
	'comparisons':
		[('ZN', 'ZN', 'FE', 'FE', 31.79)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ZN_FE, d, 'R_1hxq_2_7_7_12')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ZN_FE' :  match1}