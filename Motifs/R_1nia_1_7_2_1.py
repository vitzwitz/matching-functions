'''
FUNC:R_1nia_1_7_2_1
PDB:1nia
EC:1.7.2.1
RESI:cu,cu
LOCI:a-501,502;
'''
import motifFunctions as cmd
CU_CU = { 
	'distances':
		[14.6, 14.6],
	'comparisons':
		[('CU', 'CU', 'CU', 'CU', 14.6), ('CU', 'CU', 'CU', 'CU', 14.6)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CU_CU, d, 'R_1nia_1_7_2_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CU_CU' :  match1}