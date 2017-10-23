'''
FUNC:M_1ctt_3_5_4_5
PDB:1ctt
EC:3.5.4.5
RESI:glu,cys,zn
LOCI:a-104,132,296;
'''
import motifFunctions as cmd
GLU_ZN = { 
	'distances':
		[[7.4], [7.09], [5.93], [6.17], [5.49]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 7.4)], [('CG', 'GLU', 'ZN', 'ZN', 7.09)], [('CD', 'GLU', 'ZN', 'ZN', 5.93)], [('OE1', 'GLU', 'ZN', 'ZN', 6.17)], [('OE2', 'GLU', 'ZN', 'ZN', 5.49)]]}
CYS_GLU = { 
	'distances':
		[[6.21, 6.12, 5.83, 6.83, 5.44], [5.91, 6.09, 5.51, 6.02, 5.47]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 6.21), ('CB', 'CYS', 'CG', 'GLU', 6.12), ('CB', 'CYS', 'CD', 'GLU', 5.83), ('CB', 'CYS', 'OE1', 'GLU', 6.83), ('CB', 'CYS', 'OE2', 'GLU', 5.44)], [('SG', 'CYS', 'CB', 'GLU', 5.91), ('SG', 'CYS', 'CG', 'GLU', 6.09), ('SG', 'CYS', 'CD', 'GLU', 5.51), ('SG', 'CYS', 'OE1', 'GLU', 6.02), ('SG', 'CYS', 'OE2', 'GLU', 5.47)]]}
CYS_ZN = { 
	'distances':
		[[5.17], [4.11]],
	'comparisons':
		[[('CB', 'CYS', 'ZN', 'ZN', 5.17)], [('SG', 'CYS', 'ZN', 'ZN', 4.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ZN, d, 'M_1ctt_3_5_4_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_GLU, d, 'M_1ctt_3_5_4_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_ZN, d, 'M_1ctt_3_5_4_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ZN' :  match1,
		'CYS_GLU' :  match2,
		'CYS_ZN' :  match3}