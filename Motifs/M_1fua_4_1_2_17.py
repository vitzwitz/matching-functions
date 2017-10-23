'''
FUNC:M_1fua_4_1_2_17
PDB:1fua
EC:4.1.2.17
RESI:glu,zn
LOCI:a-73,216;
'''
import motifFunctions as cmd
GLU_ZN = { 
	'distances':
		[[6.84], [5.98], [4.46], [4.38], [3.89]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 6.84)], [('CG', 'GLU', 'ZN', 'ZN', 5.98)], [('CD', 'GLU', 'ZN', 'ZN', 4.46)], [('OE1', 'GLU', 'ZN', 'ZN', 4.38)], [('OE2', 'GLU', 'ZN', 'ZN', 3.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ZN, d, 'M_1fua_4_1_2_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ZN' :  match1}