'''
FUNC:A_1emd_1_1_1_37
PDB:1emd
EC:1.1.1.37
RESI:asp,his
LOCI:a-150,177;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[8.43, 7.14, 7.38, 6.11], [7.97, 6.57, 6.5, 5.81], [6.74, 5.3, 5.12, 4.75], [8.88, 7.45, 7.11, 6.9], [7.11, 5.7, 5.08, 5.57], [8.41, 7.0, 6.39, 6.77]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 8.43), ('CB', 'HIS', 'CG', 'ASP', 7.14), ('CB', 'HIS', 'OD1', 'ASP', 7.38), ('CB', 'HIS', 'OD2', 'ASP', 6.11)], [('CG', 'HIS', 'CB', 'ASP', 7.97), ('CG', 'HIS', 'CG', 'ASP', 6.57), ('CG', 'HIS', 'OD1', 'ASP', 6.5), ('CG', 'HIS', 'OD2', 'ASP', 5.81)], [('ND1', 'HIS', 'CB', 'ASP', 6.74), ('ND1', 'HIS', 'CG', 'ASP', 5.3), ('ND1', 'HIS', 'OD1', 'ASP', 5.12), ('ND1', 'HIS', 'OD2', 'ASP', 4.75)], [('CD2', 'HIS', 'CB', 'ASP', 8.88), ('CD2', 'HIS', 'CG', 'ASP', 7.45), ('CD2', 'HIS', 'OD1', 'ASP', 7.11), ('CD2', 'HIS', 'OD2', 'ASP', 6.9)], [('CE1', 'HIS', 'CB', 'ASP', 7.11), ('CE1', 'HIS', 'CG', 'ASP', 5.7), ('CE1', 'HIS', 'OD1', 'ASP', 5.08), ('CE1', 'HIS', 'OD2', 'ASP', 5.57)], [('NE2', 'HIS', 'CB', 'ASP', 8.41), ('NE2', 'HIS', 'CG', 'ASP', 7.0), ('NE2', 'HIS', 'OD1', 'ASP', 6.39), ('NE2', 'HIS', 'OD2', 'ASP', 6.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1emd_1_1_1_37')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1}