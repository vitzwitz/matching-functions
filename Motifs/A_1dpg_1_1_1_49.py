'''
FUNC:A_1dpg_1_1_1_49
PDB:1dpg
EC:1.1.1.49
RESI:asp,his
LOCI:a-177,240;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[8.4, 7.91, 6.66, 8.78, 6.97, 8.27], [6.89, 6.5, 5.35, 7.5, 5.94, 7.2], [6.31, 5.85, 4.67, 6.85, 5.33, 6.57], [6.54, 6.36, 5.44, 7.41, 6.19, 7.3]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.4), ('CB', 'ASP', 'CG', 'HIS', 7.91), ('CB', 'ASP', 'ND1', 'HIS', 6.66), ('CB', 'ASP', 'CD2', 'HIS', 8.78), ('CB', 'ASP', 'CE1', 'HIS', 6.97), ('CB', 'ASP', 'NE2', 'HIS', 8.27)], [('CG', 'ASP', 'CB', 'HIS', 6.89), ('CG', 'ASP', 'CG', 'HIS', 6.5), ('CG', 'ASP', 'ND1', 'HIS', 5.35), ('CG', 'ASP', 'CD2', 'HIS', 7.5), ('CG', 'ASP', 'CE1', 'HIS', 5.94), ('CG', 'ASP', 'NE2', 'HIS', 7.2)], [('OD1', 'ASP', 'CB', 'HIS', 6.31), ('OD1', 'ASP', 'CG', 'HIS', 5.85), ('OD1', 'ASP', 'ND1', 'HIS', 4.67), ('OD1', 'ASP', 'CD2', 'HIS', 6.85), ('OD1', 'ASP', 'CE1', 'HIS', 5.33), ('OD1', 'ASP', 'NE2', 'HIS', 6.57)], [('OD2', 'ASP', 'CB', 'HIS', 6.54), ('OD2', 'ASP', 'CG', 'HIS', 6.36), ('OD2', 'ASP', 'ND1', 'HIS', 5.44), ('OD2', 'ASP', 'CD2', 'HIS', 7.41), ('OD2', 'ASP', 'CE1', 'HIS', 6.19), ('OD2', 'ASP', 'NE2', 'HIS', 7.3)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1dpg_1_1_1_49')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1}