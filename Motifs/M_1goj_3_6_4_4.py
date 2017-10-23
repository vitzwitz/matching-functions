'''
FUNC:M_1goj_3_6_4_4
PDB:1goj
EC:3.6.4.4
RESI:gly,mg
LOCI:a-238,401;
'''
import motifFunctions as cmd
GLY_MG = { 
	'distances':
		[[12.22], [11.43], [9.98], [9.48]],
	'comparisons':
		[[('O', 'GLY', 'MG', 'MG', 12.22)], [('C', 'GLY', 'MG', 'MG', 11.43)], [('CA', 'GLY', 'MG', 'MG', 9.98)], [('N', 'GLY', 'MG', 'MG', 9.48)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_MG, d, 'M_1goj_3_6_4_4')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_MG' :  match1}