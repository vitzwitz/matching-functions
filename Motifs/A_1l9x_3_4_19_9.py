'''
FUNC:A_1l9x_3_4_19_9
PDB:1l9x
EC:3.4.19.9
RESI:cys,his
LOCI:a-110,220;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[8.07, 8.85], [6.81, 7.49], [6.48, 7.35], [6.18, 6.48], [5.6, 6.27], [5.34, 5.58]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 8.07), ('CB', 'HIS', 'SG', 'CYS', 8.85)], [('CG', 'HIS', 'CB', 'CYS', 6.81), ('CG', 'HIS', 'SG', 'CYS', 7.49)], [('ND1', 'HIS', 'CB', 'CYS', 6.48), ('ND1', 'HIS', 'SG', 'CYS', 7.35)], [('CD2', 'HIS', 'CB', 'CYS', 6.18), ('CD2', 'HIS', 'SG', 'CYS', 6.48)], [('CE1', 'HIS', 'CB', 'CYS', 5.6), ('CE1', 'HIS', 'SG', 'CYS', 6.27)], [('NE2', 'HIS', 'CB', 'CYS', 5.34), ('NE2', 'HIS', 'SG', 'CYS', 5.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1l9x_3_4_19_9')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1}