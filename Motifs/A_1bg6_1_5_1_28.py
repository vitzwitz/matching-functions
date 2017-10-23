'''
FUNC:A_1bg6_1_5_1_28
PDB:1bg6
EC:1.5.1.28
RESI:his,asp
LOCI:a-202,297;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[6.13, 6.88, 6.65, 8.22, 7.88, 8.71], [5.93, 6.21, 5.59, 7.49, 6.7, 7.71], [6.9, 6.94, 6.1, 8.11, 6.99, 8.1], [5.27, 5.35, 4.66, 6.62, 5.8, 6.81]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.13), ('CB', 'ASP', 'CG', 'HIS', 6.88), ('CB', 'ASP', 'ND1', 'HIS', 6.65), ('CB', 'ASP', 'CD2', 'HIS', 8.22), ('CB', 'ASP', 'CE1', 'HIS', 7.88), ('CB', 'ASP', 'NE2', 'HIS', 8.71)], [('CG', 'ASP', 'CB', 'HIS', 5.93), ('CG', 'ASP', 'CG', 'HIS', 6.21), ('CG', 'ASP', 'ND1', 'HIS', 5.59), ('CG', 'ASP', 'CD2', 'HIS', 7.49), ('CG', 'ASP', 'CE1', 'HIS', 6.7), ('CG', 'ASP', 'NE2', 'HIS', 7.71)], [('OD1', 'ASP', 'CB', 'HIS', 6.9), ('OD1', 'ASP', 'CG', 'HIS', 6.94), ('OD1', 'ASP', 'ND1', 'HIS', 6.1), ('OD1', 'ASP', 'CD2', 'HIS', 8.11), ('OD1', 'ASP', 'CE1', 'HIS', 6.99), ('OD1', 'ASP', 'NE2', 'HIS', 8.1)], [('OD2', 'ASP', 'CB', 'HIS', 5.27), ('OD2', 'ASP', 'CG', 'HIS', 5.35), ('OD2', 'ASP', 'ND1', 'HIS', 4.66), ('OD2', 'ASP', 'CD2', 'HIS', 6.62), ('OD2', 'ASP', 'CE1', 'HIS', 5.8), ('OD2', 'ASP', 'NE2', 'HIS', 6.81)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1bg6_1_5_1_28')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1}