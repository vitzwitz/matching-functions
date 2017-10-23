'''
FUNC:M_1f7l_2_7_8_7
PDB:1f7l
EC:2.7.8.7
RESI:lys,his,ca
LOCI:a-62,105,130;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[21.81, 21.22, 20.78, 21.15, 20.44, 20.66], [21.45, 20.88, 20.36, 20.89, 20.06, 20.38], [20.46, 19.98, 19.49, 20.07, 19.29, 19.64], [20.09, 19.63, 19.06, 19.81, 18.91, 19.36], [19.2, 18.84, 18.31, 19.11, 18.26, 18.74]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 21.81), ('CB', 'LYS', 'CG', 'HIS', 21.22), ('CB', 'LYS', 'ND1', 'HIS', 20.78), ('CB', 'LYS', 'CD2', 'HIS', 21.15), ('CB', 'LYS', 'CE1', 'HIS', 20.44), ('CB', 'LYS', 'NE2', 'HIS', 20.66)], [('CG', 'LYS', 'CB', 'HIS', 21.45), ('CG', 'LYS', 'CG', 'HIS', 20.88), ('CG', 'LYS', 'ND1', 'HIS', 20.36), ('CG', 'LYS', 'CD2', 'HIS', 20.89), ('CG', 'LYS', 'CE1', 'HIS', 20.06), ('CG', 'LYS', 'NE2', 'HIS', 20.38)], [('CD', 'LYS', 'CB', 'HIS', 20.46), ('CD', 'LYS', 'CG', 'HIS', 19.98), ('CD', 'LYS', 'ND1', 'HIS', 19.49), ('CD', 'LYS', 'CD2', 'HIS', 20.07), ('CD', 'LYS', 'CE1', 'HIS', 19.29), ('CD', 'LYS', 'NE2', 'HIS', 19.64)], [('CE', 'LYS', 'CB', 'HIS', 20.09), ('CE', 'LYS', 'CG', 'HIS', 19.63), ('CE', 'LYS', 'ND1', 'HIS', 19.06), ('CE', 'LYS', 'CD2', 'HIS', 19.81), ('CE', 'LYS', 'CE1', 'HIS', 18.91), ('CE', 'LYS', 'NE2', 'HIS', 19.36)], [('NZ', 'LYS', 'CB', 'HIS', 19.2), ('NZ', 'LYS', 'CG', 'HIS', 18.84), ('NZ', 'LYS', 'ND1', 'HIS', 18.31), ('NZ', 'LYS', 'CD2', 'HIS', 19.11), ('NZ', 'LYS', 'CE1', 'HIS', 18.26), ('NZ', 'LYS', 'NE2', 'HIS', 18.74)]]}
HIS_CA = { 
	'distances':
		[[17.27], [16.86], [16.04], [17.32], [16.04], [16.81]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 17.27)], [('CG', 'HIS', 'CA', 'CA', 16.86)], [('ND1', 'HIS', 'CA', 'CA', 16.04)], [('CD2', 'HIS', 'CA', 'CA', 17.32)], [('CE1', 'HIS', 'CA', 'CA', 16.04)], [('NE2', 'HIS', 'CA', 'CA', 16.81)]]}
LYS_CA = { 
	'distances':
		[[10.76], [9.41], [8.52], [7.14], [6.53]],
	'comparisons':
		[[('CB', 'LYS', 'CA', 'CA', 10.76)], [('CG', 'LYS', 'CA', 'CA', 9.41)], [('CD', 'LYS', 'CA', 'CA', 8.52)], [('CE', 'LYS', 'CA', 'CA', 7.14)], [('NZ', 'LYS', 'CA', 'CA', 6.53)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'M_1f7l_2_7_8_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CA, d, 'M_1f7l_2_7_8_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_CA, d, 'M_1f7l_2_7_8_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'HIS_CA' :  match2,
		'LYS_CA' :  match3}