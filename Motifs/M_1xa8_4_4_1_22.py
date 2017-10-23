'''
FUNC:M_1xa8_4_4_1_22
PDB:1xa8
EC:4.4.1.22
RESI:cys,zn
LOCI:a-56,200;
'''
import motifFunctions as cmd
CYS_ZN = { 
	'distances':
		[[23.73], [23.79]],
	'comparisons':
		[[('CB', 'CYS', 'ZN', 'ZN', 23.73)], [('SG', 'CYS', 'ZN', 'ZN', 23.79)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_ZN, d, 'M_1xa8_4_4_1_22')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_ZN' :  match1}