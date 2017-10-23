'''
FUNC:A_1ca3_4_2_1_1
PDB:1ca3
EC:4.2.1.1
RESI:glu,thr
LOCI:a-106,199;
'''
import motifFunctions as cmd
THR_GLU = { 
	'distances':
		[[7.09, 6.86, 5.54, 4.82, 5.81], [7.2, 6.62, 5.21, 4.29, 5.57], [6.91, 7.06, 6.06, 5.21, 6.69]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLU', 7.09), ('CB', 'THR', 'CG', 'GLU', 6.86), ('CB', 'THR', 'CD', 'GLU', 5.54), ('CB', 'THR', 'OE1', 'GLU', 4.82), ('CB', 'THR', 'OE2', 'GLU', 5.81)], [('OG1', 'THR', 'CB', 'GLU', 7.2), ('OG1', 'THR', 'CG', 'GLU', 6.62), ('OG1', 'THR', 'CD', 'GLU', 5.21), ('OG1', 'THR', 'OE1', 'GLU', 4.29), ('OG1', 'THR', 'OE2', 'GLU', 5.57)], [('CG2', 'THR', 'CB', 'GLU', 6.91), ('CG2', 'THR', 'CG', 'GLU', 7.06), ('CG2', 'THR', 'CD', 'GLU', 6.06), ('CG2', 'THR', 'OE1', 'GLU', 5.21), ('CG2', 'THR', 'OE2', 'GLU', 6.69)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_GLU, d, 'A_1ca3_4_2_1_1')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_GLU' :  match1}