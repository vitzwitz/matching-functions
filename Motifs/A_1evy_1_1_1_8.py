'''
FUNC:A_1evy_1_1_1_8
PDB:1evy
EC:1.1.1.8
RESI:lys,thr
LOCI:a-210,267;
'''
import motifFunctions as cmd
LYS_THR = { 
	'distances':
		[[6.39, 6.48, 6.42], [6.5, 6.24, 6.32], [6.05, 5.34, 6.19], [6.65, 5.76, 6.54], [6.55, 5.35, 6.68]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'THR', 6.39), ('CB', 'LYS', 'OG1', 'THR', 6.48), ('CB', 'LYS', 'CG2', 'THR', 6.42)], [('CG', 'LYS', 'CB', 'THR', 6.5), ('CG', 'LYS', 'OG1', 'THR', 6.24), ('CG', 'LYS', 'CG2', 'THR', 6.32)], [('CD', 'LYS', 'CB', 'THR', 6.05), ('CD', 'LYS', 'OG1', 'THR', 5.34), ('CD', 'LYS', 'CG2', 'THR', 6.19)], [('CE', 'LYS', 'CB', 'THR', 6.65), ('CE', 'LYS', 'OG1', 'THR', 5.76), ('CE', 'LYS', 'CG2', 'THR', 6.54)], [('NZ', 'LYS', 'CB', 'THR', 6.55), ('NZ', 'LYS', 'OG1', 'THR', 5.35), ('NZ', 'LYS', 'CG2', 'THR', 6.68)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_THR, d, 'A_1evy_1_1_1_8')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_THR' :  match1}