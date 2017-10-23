'''
FUNC:R_1fwj_3_5_1_5
PDB:1fwj
EC:3.5.1.5
RESI:ni,ni
LOCI:c-574,575;
'''
import motifFunctions as cmd
NI_NI = { 
	'distances':
		[5.59, 5.59],
	'comparisons':
		[('NI', 'NI', 'NI', 'NI', 5.59), ('NI', 'NI', 'NI', 'NI', 5.59)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(NI_NI, d, 'R_1fwj_3_5_1_5')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'NI_NI' :  match1}