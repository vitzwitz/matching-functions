'''
FUNC:Pab_1qgy_1_18_1_2
PDB:1qgy
EC:1.18.1.2
RESI:ser,cys,glu
LOCI:a-80,261,301;
'''
import motifFunctions as cmd
CYS_GLU = { 
	'distances':
		[[6.84, 7.45, 7.56, 8.32, 7.31], [6.25, 6.37, 6.25, 7.15, 5.73]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 6.84), ('CB', 'CYS', 'CG', 'GLU', 7.45), ('CB', 'CYS', 'CD', 'GLU', 7.56), ('CB', 'CYS', 'OE1', 'GLU', 8.32), ('CB', 'CYS', 'OE2', 'GLU', 7.31)], [('SG', 'CYS', 'CB', 'GLU', 6.25), ('SG', 'CYS', 'CG', 'GLU', 6.37), ('SG', 'CYS', 'CD', 'GLU', 6.25), ('SG', 'CYS', 'OE1', 'GLU', 7.15), ('SG', 'CYS', 'OE2', 'GLU', 5.73)]]}
SER_GLU = { 
	'distances':
		[[9.1, 8.28, 6.98, 7.28, 5.91], [8.02, 7.09, 5.94, 6.49, 4.74]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 9.1), ('CB', 'SER', 'CG', 'GLU', 8.28), ('CB', 'SER', 'CD', 'GLU', 6.98), ('CB', 'SER', 'OE1', 'GLU', 7.28), ('CB', 'SER', 'OE2', 'GLU', 5.91)], [('OG', 'SER', 'CB', 'GLU', 8.02), ('OG', 'SER', 'CG', 'GLU', 7.09), ('OG', 'SER', 'CD', 'GLU', 5.94), ('OG', 'SER', 'OE1', 'GLU', 6.49), ('OG', 'SER', 'OE2', 'GLU', 4.74)]]}
SER_CYS = { 
	'distances':
		[[8.81, 7.24], [8.06, 6.34]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'CYS', 8.81), ('CB', 'SER', 'SG', 'CYS', 7.24)], [('OG', 'SER', 'CB', 'CYS', 8.06), ('OG', 'SER', 'SG', 'CYS', 6.34)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLU, d, 'Pab_1qgy_1_18_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLU, d, 'Pab_1qgy_1_18_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_CYS, d, 'Pab_1qgy_1_18_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLU' :  match1,
		'SER_GLU' :  match2,
		'SER_CYS' :  match3}