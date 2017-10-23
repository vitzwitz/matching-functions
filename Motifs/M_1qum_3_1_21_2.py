'''
FUNC:M_1qum_3_1_21_2
PDB:1qum
EC:3.1.21.2
RESI:glu,zn,zn,zn
LOCI:a-261,301,302,303;
'''
import motifFunctions as cmd
ZN_ZNI = { 
	'distances':
		[6.11],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZNI', 6.11)]}
GLU_ZN = { 
	'distances':
		[[9.58], [8.81], [7.32], [7.11], [6.63], [8.46], [8.8], [7.77], [6.75], [8.3], [7.16], [6.52], [5.17], [4.25], [5.5]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 9.58)], [('CG', 'GLU', 'ZN', 'ZN', 8.81)], [('CD', 'GLU', 'ZN', 'ZN', 7.32)], [('OE1', 'GLU', 'ZN', 'ZN', 7.11)], [('OE2', 'GLU', 'ZN', 'ZN', 6.63)], [('CB', 'GLU', 'ZN', 'ZN', 8.46)], [('CG', 'GLU', 'ZN', 'ZN', 8.8)], [('CD', 'GLU', 'ZN', 'ZN', 7.77)], [('OE1', 'GLU', 'ZN', 'ZN', 6.75)], [('OE2', 'GLU', 'ZN', 'ZN', 8.3)], [('CB', 'GLU', 'ZN', 'ZN', 7.16)], [('CG', 'GLU', 'ZN', 'ZN', 6.52)], [('CD', 'GLU', 'ZN', 'ZN', 5.17)], [('OE1', 'GLU', 'ZN', 'ZN', 4.25)], [('OE2', 'GLU', 'ZN', 'ZN', 5.5)]]}
ZN_ZN = { 
	'distances':
		[7.75, 5.78, 7.75, 6.11, 5.78],
	'comparisons':
		[('ZN', 'ZN', 'ZN', 'ZN', 7.75), ('ZN', 'ZN', 'ZN', 'ZN', 5.78), ('ZN', 'ZN', 'ZN', 'ZN', 7.75), ('ZN', 'ZN', 'ZN', 'ZN', 6.11), ('ZN', 'ZN', 'ZN', 'ZN', 5.78)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ZN_ZNI, d, 'M_1qum_3_1_21_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ZN, d, 'M_1qum_3_1_21_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ZN_ZN, d, 'M_1qum_3_1_21_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ZN_ZNI' :  match1,
		'GLU_ZN' :  match2,
		'ZN_ZN' :  match3}