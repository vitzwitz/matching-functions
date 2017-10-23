'''
FUNC:M_1gqg_1_13_11_24
PDB:1gqg
EC:1.13.11.24
RESI:glu,cu
LOCI:a-73,1352;
'''
import motifFunctions as cmd
GLU_CU = { 
	'distances':
		[[7.47], [6.61], [6.71], [6.63], [7.35]],
	'comparisons':
		[[('CB', 'GLU', 'CU', 'CU', 7.47)], [('CG', 'GLU', 'CU', 'CU', 6.61)], [('CD', 'GLU', 'CU', 'CU', 6.71)], [('OE1', 'GLU', 'CU', 'CU', 6.63)], [('OE2', 'GLU', 'CU', 'CU', 7.35)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_CU, d, 'M_1gqg_1_13_11_24')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_CU' :  match1}