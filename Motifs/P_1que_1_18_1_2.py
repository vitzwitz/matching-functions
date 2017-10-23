'''
FUNC:P_1que_1_18_1_2
PDB:1que
EC:1.18.1.2
RESI:ser,cys,glu
LOCI:a-80,261,301;
'''
import motifFunctions as cmd
CYS_GLU = { 
	'distances':
		[[6.75, 7.47, 7.7, 8.58, 7.34], [6.23, 6.46, 6.47, 7.49, 5.86]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 6.75), ('CB', 'CYS', 'CG', 'GLU', 7.47), ('CB', 'CYS', 'CD', 'GLU', 7.7), ('CB', 'CYS', 'OE1', 'GLU', 8.58), ('CB', 'CYS', 'OE2', 'GLU', 7.34)], [('SG', 'CYS', 'CB', 'GLU', 6.23), ('SG', 'CYS', 'CG', 'GLU', 6.46), ('SG', 'CYS', 'CD', 'GLU', 6.47), ('SG', 'CYS', 'OE1', 'GLU', 7.49), ('SG', 'CYS', 'OE2', 'GLU', 5.86)]]}
SER_GLU = { 
	'distances':
		[[9.15, 8.39, 7.17, 7.57, 6.02], [7.99, 7.15, 6.07, 6.7, 4.85]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 9.15), ('CB', 'SER', 'CG', 'GLU', 8.39), ('CB', 'SER', 'CD', 'GLU', 7.17), ('CB', 'SER', 'OE1', 'GLU', 7.57), ('CB', 'SER', 'OE2', 'GLU', 6.02)], [('OG', 'SER', 'CB', 'GLU', 7.99), ('OG', 'SER', 'CG', 'GLU', 7.15), ('OG', 'SER', 'CD', 'GLU', 6.07), ('OG', 'SER', 'OE1', 'GLU', 6.7), ('OG', 'SER', 'OE2', 'GLU', 4.85)]]}
SER_CYS = { 
	'distances':
		[[8.91, 7.36], [8.06, 6.38]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'CYS', 8.91), ('CB', 'SER', 'SG', 'CYS', 7.36)], [('OG', 'SER', 'CB', 'CYS', 8.06), ('OG', 'SER', 'SG', 'CYS', 6.38)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLU, d, 'P_1que_1_18_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLU, d, 'P_1que_1_18_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_CYS, d, 'P_1que_1_18_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLU' :  match1,
		'SER_GLU' :  match2,
		'SER_CYS' :  match3}