'''
FUNC:P_1o2u_3_4_21_4
PDB:1o2u
EC:3.4.21.4
RESI:his,asp
LOCI:a-57,102;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[7.92, 6.54, 6.0, 6.45], [7.9, 6.4, 6.11, 5.96], [7.01, 5.52, 5.51, 4.85], [9.14, 7.62, 7.39, 7.03], [7.84, 6.4, 6.55, 5.53], [9.05, 7.57, 7.55, 6.77]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.92), ('CB', 'HIS', 'CG', 'ASP', 6.54), ('CB', 'HIS', 'OD1', 'ASP', 6.0), ('CB', 'HIS', 'OD2', 'ASP', 6.45)], [('CG', 'HIS', 'CB', 'ASP', 7.9), ('CG', 'HIS', 'CG', 'ASP', 6.4), ('CG', 'HIS', 'OD1', 'ASP', 6.11), ('CG', 'HIS', 'OD2', 'ASP', 5.96)], [('ND1', 'HIS', 'CB', 'ASP', 7.01), ('ND1', 'HIS', 'CG', 'ASP', 5.52), ('ND1', 'HIS', 'OD1', 'ASP', 5.51), ('ND1', 'HIS', 'OD2', 'ASP', 4.85)], [('CD2', 'HIS', 'CB', 'ASP', 9.14), ('CD2', 'HIS', 'CG', 'ASP', 7.62), ('CD2', 'HIS', 'OD1', 'ASP', 7.39), ('CD2', 'HIS', 'OD2', 'ASP', 7.03)], [('CE1', 'HIS', 'CB', 'ASP', 7.84), ('CE1', 'HIS', 'CG', 'ASP', 6.4), ('CE1', 'HIS', 'OD1', 'ASP', 6.55), ('CE1', 'HIS', 'OD2', 'ASP', 5.53)], [('NE2', 'HIS', 'CB', 'ASP', 9.05), ('NE2', 'HIS', 'CG', 'ASP', 7.57), ('NE2', 'HIS', 'OD1', 'ASP', 7.55), ('NE2', 'HIS', 'OD2', 'ASP', 6.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'P_1o2u_3_4_21_4')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1}