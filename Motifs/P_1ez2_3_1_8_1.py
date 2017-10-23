'''
FUNC:P_1ez2_3_1_8_1
PDB:1ez2
EC:3.1.8.1
RESI:asp,his,asp
LOCI:a-233,254,301;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[7.12, 6.08, 6.52, 5.05], [7.24, 5.98, 6.04, 5.24], [6.46, 5.06, 4.86, 4.61], [8.42, 7.13, 6.99, 6.53], [7.37, 5.96, 5.41, 5.78], [8.46, 7.1, 6.65, 6.77], [7.3, 8.08, 7.81, 9.35], [6.39, 6.91, 6.48, 8.2], [7.14, 7.31, 6.61, 8.58], [5.06, 5.58, 5.25, 6.87], [6.54, 6.39, 5.53, 7.61], [5.22, 5.16, 4.45, 6.43]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.12), ('CB', 'HIS', 'CG', 'ASP', 6.08), ('CB', 'HIS', 'OD1', 'ASP', 6.52), ('CB', 'HIS', 'OD2', 'ASP', 5.05)], [('CG', 'HIS', 'CB', 'ASP', 7.24), ('CG', 'HIS', 'CG', 'ASP', 5.98), ('CG', 'HIS', 'OD1', 'ASP', 6.04), ('CG', 'HIS', 'OD2', 'ASP', 5.24)], [('ND1', 'HIS', 'CB', 'ASP', 6.46), ('ND1', 'HIS', 'CG', 'ASP', 5.06), ('ND1', 'HIS', 'OD1', 'ASP', 4.86), ('ND1', 'HIS', 'OD2', 'ASP', 4.61)], [('CD2', 'HIS', 'CB', 'ASP', 8.42), ('CD2', 'HIS', 'CG', 'ASP', 7.13), ('CD2', 'HIS', 'OD1', 'ASP', 6.99), ('CD2', 'HIS', 'OD2', 'ASP', 6.53)], [('CE1', 'HIS', 'CB', 'ASP', 7.37), ('CE1', 'HIS', 'CG', 'ASP', 5.96), ('CE1', 'HIS', 'OD1', 'ASP', 5.41), ('CE1', 'HIS', 'OD2', 'ASP', 5.78)], [('NE2', 'HIS', 'CB', 'ASP', 8.46), ('NE2', 'HIS', 'CG', 'ASP', 7.1), ('NE2', 'HIS', 'OD1', 'ASP', 6.65), ('NE2', 'HIS', 'OD2', 'ASP', 6.77)], [('CB', 'HIS', 'CB', 'ASP', 7.3), ('CB', 'HIS', 'CG', 'ASP', 8.08), ('CB', 'HIS', 'OD1', 'ASP', 7.81), ('CB', 'HIS', 'OD2', 'ASP', 9.35)], [('CG', 'HIS', 'CB', 'ASP', 6.39), ('CG', 'HIS', 'CG', 'ASP', 6.91), ('CG', 'HIS', 'OD1', 'ASP', 6.48), ('CG', 'HIS', 'OD2', 'ASP', 8.2)], [('ND1', 'HIS', 'CB', 'ASP', 7.14), ('ND1', 'HIS', 'CG', 'ASP', 7.31), ('ND1', 'HIS', 'OD1', 'ASP', 6.61), ('ND1', 'HIS', 'OD2', 'ASP', 8.58)], [('CD2', 'HIS', 'CB', 'ASP', 5.06), ('CD2', 'HIS', 'CG', 'ASP', 5.58), ('CD2', 'HIS', 'OD1', 'ASP', 5.25), ('CD2', 'HIS', 'OD2', 'ASP', 6.87)], [('CE1', 'HIS', 'CB', 'ASP', 6.54), ('CE1', 'HIS', 'CG', 'ASP', 6.39), ('CE1', 'HIS', 'OD1', 'ASP', 5.53), ('CE1', 'HIS', 'OD2', 'ASP', 7.61)], [('NE2', 'HIS', 'CB', 'ASP', 5.22), ('NE2', 'HIS', 'CG', 'ASP', 5.16), ('NE2', 'HIS', 'OD1', 'ASP', 4.45), ('NE2', 'HIS', 'OD2', 'ASP', 6.43)]]}
ASP_ASP = { 
	'distances':
		[[11.62, 11.77, 11.05, 12.95], [10.37, 10.48, 9.72, 11.69], [10.07, 9.98, 9.11, 11.14], [9.88, 10.18, 9.51, 11.44], [11.62, 10.37, 10.07, 9.88], [11.77, 10.48, 9.98, 10.18], [11.05, 9.72, 9.11, 9.51], [12.95, 11.69, 11.14, 11.44]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.62), ('CB', 'ASP', 'CG', 'ASP', 11.77), ('CB', 'ASP', 'OD1', 'ASP', 11.05), ('CB', 'ASP', 'OD2', 'ASP', 12.95)], [('CG', 'ASP', 'CB', 'ASP', 10.37), ('CG', 'ASP', 'CG', 'ASP', 10.48), ('CG', 'ASP', 'OD1', 'ASP', 9.72), ('CG', 'ASP', 'OD2', 'ASP', 11.69)], [('OD1', 'ASP', 'CB', 'ASP', 10.07), ('OD1', 'ASP', 'CG', 'ASP', 9.98), ('OD1', 'ASP', 'OD1', 'ASP', 9.11), ('OD1', 'ASP', 'OD2', 'ASP', 11.14)], [('OD2', 'ASP', 'CB', 'ASP', 9.88), ('OD2', 'ASP', 'CG', 'ASP', 10.18), ('OD2', 'ASP', 'OD1', 'ASP', 9.51), ('OD2', 'ASP', 'OD2', 'ASP', 11.44)], [('CB', 'ASP', 'CB', 'ASP', 11.62), ('CB', 'ASP', 'CG', 'ASP', 10.37), ('CB', 'ASP', 'OD1', 'ASP', 10.07), ('CB', 'ASP', 'OD2', 'ASP', 9.88)], [('CG', 'ASP', 'CB', 'ASP', 11.77), ('CG', 'ASP', 'CG', 'ASP', 10.48), ('CG', 'ASP', 'OD1', 'ASP', 9.98), ('CG', 'ASP', 'OD2', 'ASP', 10.18)], [('OD1', 'ASP', 'CB', 'ASP', 11.05), ('OD1', 'ASP', 'CG', 'ASP', 9.72), ('OD1', 'ASP', 'OD1', 'ASP', 9.11), ('OD1', 'ASP', 'OD2', 'ASP', 9.51)], [('OD2', 'ASP', 'CB', 'ASP', 12.95), ('OD2', 'ASP', 'CG', 'ASP', 11.69), ('OD2', 'ASP', 'OD1', 'ASP', 11.14), ('OD2', 'ASP', 'OD2', 'ASP', 11.44)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'P_1ez2_3_1_8_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'P_1ez2_3_1_8_1')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'ASP_ASP' :  match2}