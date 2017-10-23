'''
FUNC:A_1zym_2_7_3_9
PDB:1zym
EC:2.7.3.9
RESI:thr,his
LOCI:a-168,189;
'''
import motifFunctions as cmd
HIS_THR = { 
	'distances':
		[[8.8, 8.32, 7.92], [7.45, 6.86, 6.75], [7.4, 6.58, 7.06], [6.32, 5.85, 5.52], [6.28, 5.33, 6.21], [5.43, 4.68, 5.1]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'THR', 8.8), ('CB', 'HIS', 'OG1', 'THR', 8.32), ('CB', 'HIS', 'CG2', 'THR', 7.92)], [('CG', 'HIS', 'CB', 'THR', 7.45), ('CG', 'HIS', 'OG1', 'THR', 6.86), ('CG', 'HIS', 'CG2', 'THR', 6.75)], [('ND1', 'HIS', 'CB', 'THR', 7.4), ('ND1', 'HIS', 'OG1', 'THR', 6.58), ('ND1', 'HIS', 'CG2', 'THR', 7.06)], [('CD2', 'HIS', 'CB', 'THR', 6.32), ('CD2', 'HIS', 'OG1', 'THR', 5.85), ('CD2', 'HIS', 'CG2', 'THR', 5.52)], [('CE1', 'HIS', 'CB', 'THR', 6.28), ('CE1', 'HIS', 'OG1', 'THR', 5.33), ('CE1', 'HIS', 'CG2', 'THR', 6.21)], [('NE2', 'HIS', 'CB', 'THR', 5.43), ('NE2', 'HIS', 'OG1', 'THR', 4.68), ('NE2', 'HIS', 'CG2', 'THR', 5.1)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_THR, d, 'A_1zym_2_7_3_9')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_THR' :  match1}