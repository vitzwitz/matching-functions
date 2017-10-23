'''
FUNC:A_1b6g_3_8_1_5
PDB:1b6g
EC:3.8.1.5
RESI:asp,asp,his
LOCI:a-124,260,289;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[6.27, 7.0, 6.7, 8.36, 7.97, 8.84], [5.46, 5.85, 5.35, 7.18, 6.59, 7.52], [5.18, 5.61, 5.28, 6.89, 6.49, 7.3], [5.72, 5.69, 4.85, 6.9, 5.91, 6.99], [8.92, 7.52, 7.14, 6.64, 5.92, 5.54], [9.05, 7.58, 7.21, 6.6, 5.89, 5.41], [8.51, 7.03, 6.48, 6.24, 5.14, 4.95], [9.95, 8.51, 8.28, 7.4, 6.98, 6.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.27), ('CB', 'ASP', 'CG', 'HIS', 7.0), ('CB', 'ASP', 'ND1', 'HIS', 6.7), ('CB', 'ASP', 'CD2', 'HIS', 8.36), ('CB', 'ASP', 'CE1', 'HIS', 7.97), ('CB', 'ASP', 'NE2', 'HIS', 8.84)], [('CG', 'ASP', 'CB', 'HIS', 5.46), ('CG', 'ASP', 'CG', 'HIS', 5.85), ('CG', 'ASP', 'ND1', 'HIS', 5.35), ('CG', 'ASP', 'CD2', 'HIS', 7.18), ('CG', 'ASP', 'CE1', 'HIS', 6.59), ('CG', 'ASP', 'NE2', 'HIS', 7.52)], [('OD1', 'ASP', 'CB', 'HIS', 5.18), ('OD1', 'ASP', 'CG', 'HIS', 5.61), ('OD1', 'ASP', 'ND1', 'HIS', 5.28), ('OD1', 'ASP', 'CD2', 'HIS', 6.89), ('OD1', 'ASP', 'CE1', 'HIS', 6.49), ('OD1', 'ASP', 'NE2', 'HIS', 7.3)], [('OD2', 'ASP', 'CB', 'HIS', 5.72), ('OD2', 'ASP', 'CG', 'HIS', 5.69), ('OD2', 'ASP', 'ND1', 'HIS', 4.85), ('OD2', 'ASP', 'CD2', 'HIS', 6.9), ('OD2', 'ASP', 'CE1', 'HIS', 5.91), ('OD2', 'ASP', 'NE2', 'HIS', 6.99)], [('CB', 'ASP', 'CB', 'HIS', 8.92), ('CB', 'ASP', 'CG', 'HIS', 7.52), ('CB', 'ASP', 'ND1', 'HIS', 7.14), ('CB', 'ASP', 'CD2', 'HIS', 6.64), ('CB', 'ASP', 'CE1', 'HIS', 5.92), ('CB', 'ASP', 'NE2', 'HIS', 5.54)], [('CG', 'ASP', 'CB', 'HIS', 9.05), ('CG', 'ASP', 'CG', 'HIS', 7.58), ('CG', 'ASP', 'ND1', 'HIS', 7.21), ('CG', 'ASP', 'CD2', 'HIS', 6.6), ('CG', 'ASP', 'CE1', 'HIS', 5.89), ('CG', 'ASP', 'NE2', 'HIS', 5.41)], [('OD1', 'ASP', 'CB', 'HIS', 8.51), ('OD1', 'ASP', 'CG', 'HIS', 7.03), ('OD1', 'ASP', 'ND1', 'HIS', 6.48), ('OD1', 'ASP', 'CD2', 'HIS', 6.24), ('OD1', 'ASP', 'CE1', 'HIS', 5.14), ('OD1', 'ASP', 'NE2', 'HIS', 4.95)], [('OD2', 'ASP', 'CB', 'HIS', 9.95), ('OD2', 'ASP', 'CG', 'HIS', 8.51), ('OD2', 'ASP', 'ND1', 'HIS', 8.28), ('OD2', 'ASP', 'CD2', 'HIS', 7.4), ('OD2', 'ASP', 'CE1', 'HIS', 6.98), ('OD2', 'ASP', 'NE2', 'HIS', 6.33)]]}
ASP_ASP = { 
	'distances':
		[[11.53, 11.82, 11.03, 12.95], [10.27, 10.45, 9.59, 11.56], [10.38, 10.34, 9.41, 11.37], [9.35, 9.64, 8.82, 10.81], [11.53, 10.27, 10.38, 9.35], [11.82, 10.45, 10.34, 9.64], [11.03, 9.59, 9.41, 8.82], [12.95, 11.56, 11.37, 10.81]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.53), ('CB', 'ASP', 'CG', 'ASP', 11.82), ('CB', 'ASP', 'OD1', 'ASP', 11.03), ('CB', 'ASP', 'OD2', 'ASP', 12.95)], [('CG', 'ASP', 'CB', 'ASP', 10.27), ('CG', 'ASP', 'CG', 'ASP', 10.45), ('CG', 'ASP', 'OD1', 'ASP', 9.59), ('CG', 'ASP', 'OD2', 'ASP', 11.56)], [('OD1', 'ASP', 'CB', 'ASP', 10.38), ('OD1', 'ASP', 'CG', 'ASP', 10.34), ('OD1', 'ASP', 'OD1', 'ASP', 9.41), ('OD1', 'ASP', 'OD2', 'ASP', 11.37)], [('OD2', 'ASP', 'CB', 'ASP', 9.35), ('OD2', 'ASP', 'CG', 'ASP', 9.64), ('OD2', 'ASP', 'OD1', 'ASP', 8.82), ('OD2', 'ASP', 'OD2', 'ASP', 10.81)], [('CB', 'ASP', 'CB', 'ASP', 11.53), ('CB', 'ASP', 'CG', 'ASP', 10.27), ('CB', 'ASP', 'OD1', 'ASP', 10.38), ('CB', 'ASP', 'OD2', 'ASP', 9.35)], [('CG', 'ASP', 'CB', 'ASP', 11.82), ('CG', 'ASP', 'CG', 'ASP', 10.45), ('CG', 'ASP', 'OD1', 'ASP', 10.34), ('CG', 'ASP', 'OD2', 'ASP', 9.64)], [('OD1', 'ASP', 'CB', 'ASP', 11.03), ('OD1', 'ASP', 'CG', 'ASP', 9.59), ('OD1', 'ASP', 'OD1', 'ASP', 9.41), ('OD1', 'ASP', 'OD2', 'ASP', 8.82)], [('OD2', 'ASP', 'CB', 'ASP', 12.95), ('OD2', 'ASP', 'CG', 'ASP', 11.56), ('OD2', 'ASP', 'OD1', 'ASP', 11.37), ('OD2', 'ASP', 'OD2', 'ASP', 10.81)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_1b6g_3_8_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'A_1b6g_3_8_1_5')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'ASP_ASP' :  match2}