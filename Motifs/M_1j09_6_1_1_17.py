'''
FUNC:M_1j09_6_1_1_17
PDB:1j09
EC:6.1.1.17
RESI:lys,mg
LOCI:a-246,502;
'''
import motifFunctions as cmd
LYS_MG = { 
	'distances':
		[[9.5], [8.65], [8.48], [8.03], [8.12]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 9.5)], [('CG', 'LYS', 'MG', 'MG', 8.65)], [('CD', 'LYS', 'MG', 'MG', 8.48)], [('CE', 'LYS', 'MG', 'MG', 8.03)], [('NZ', 'LYS', 'MG', 'MG', 8.12)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_MG, d, 'M_1j09_6_1_1_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_MG' :  match1}