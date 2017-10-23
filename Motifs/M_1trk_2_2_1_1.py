'''
FUNC:M_1trk_2_2_1_1
PDB:1trk
EC:2.2.1.1
RESI:his,his,ca
LOCI:a-30,263,681;
'''
import motifFunctions as cmd
HIS_CA = { 
	'distances':
		[[13.0], [13.37], [14.46], [12.83], [14.64], [13.69], [9.74], [9.5], [8.56], [10.53], [9.11], [10.27]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 13.0)], [('CG', 'HIS', 'CA', 'CA', 13.37)], [('ND1', 'HIS', 'CA', 'CA', 14.46)], [('CD2', 'HIS', 'CA', 'CA', 12.83)], [('CE1', 'HIS', 'CA', 'CA', 14.64)], [('NE2', 'HIS', 'CA', 'CA', 13.69)], [('CB', 'HIS', 'CA', 'CA', 9.74)], [('CG', 'HIS', 'CA', 'CA', 9.5)], [('ND1', 'HIS', 'CA', 'CA', 8.56)], [('CD2', 'HIS', 'CA', 'CA', 10.53)], [('CE1', 'HIS', 'CA', 'CA', 9.11)], [('NE2', 'HIS', 'CA', 'CA', 10.27)]]}
HIS_HIS = { 
	'distances':
		[[8.32, 7.76, 7.64, 7.72, 7.49, 7.53], [8.53, 7.71, 7.62, 7.31, 7.16, 6.95], [9.79, 8.89, 8.79, 8.35, 8.18, 7.88], [7.8, 6.79, 6.77, 6.16, 6.15, 5.73], [9.94, 8.9, 8.83, 8.12, 8.03, 7.56], [8.83, 7.72, 7.71, 6.87, 6.87, 6.29], [8.32, 8.53, 9.79, 7.8, 9.94, 8.83], [7.76, 7.71, 8.89, 6.79, 8.9, 7.72], [7.64, 7.62, 8.79, 6.77, 8.83, 7.71], [7.72, 7.31, 8.35, 6.16, 8.12, 6.87], [7.49, 7.16, 8.18, 6.15, 8.03, 6.87], [7.53, 6.95, 7.88, 5.73, 7.56, 6.29]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 8.32), ('CB', 'HIS', 'CG', 'HIS', 7.76), ('CB', 'HIS', 'ND1', 'HIS', 7.64), ('CB', 'HIS', 'CD2', 'HIS', 7.72), ('CB', 'HIS', 'CE1', 'HIS', 7.49), ('CB', 'HIS', 'NE2', 'HIS', 7.53)], [('CG', 'HIS', 'CB', 'HIS', 8.53), ('CG', 'HIS', 'CG', 'HIS', 7.71), ('CG', 'HIS', 'ND1', 'HIS', 7.62), ('CG', 'HIS', 'CD2', 'HIS', 7.31), ('CG', 'HIS', 'CE1', 'HIS', 7.16), ('CG', 'HIS', 'NE2', 'HIS', 6.95)], [('ND1', 'HIS', 'CB', 'HIS', 9.79), ('ND1', 'HIS', 'CG', 'HIS', 8.89), ('ND1', 'HIS', 'ND1', 'HIS', 8.79), ('ND1', 'HIS', 'CD2', 'HIS', 8.35), ('ND1', 'HIS', 'CE1', 'HIS', 8.18), ('ND1', 'HIS', 'NE2', 'HIS', 7.88)], [('CD2', 'HIS', 'CB', 'HIS', 7.8), ('CD2', 'HIS', 'CG', 'HIS', 6.79), ('CD2', 'HIS', 'ND1', 'HIS', 6.77), ('CD2', 'HIS', 'CD2', 'HIS', 6.16), ('CD2', 'HIS', 'CE1', 'HIS', 6.15), ('CD2', 'HIS', 'NE2', 'HIS', 5.73)], [('CE1', 'HIS', 'CB', 'HIS', 9.94), ('CE1', 'HIS', 'CG', 'HIS', 8.9), ('CE1', 'HIS', 'ND1', 'HIS', 8.83), ('CE1', 'HIS', 'CD2', 'HIS', 8.12), ('CE1', 'HIS', 'CE1', 'HIS', 8.03), ('CE1', 'HIS', 'NE2', 'HIS', 7.56)], [('NE2', 'HIS', 'CB', 'HIS', 8.83), ('NE2', 'HIS', 'CG', 'HIS', 7.72), ('NE2', 'HIS', 'ND1', 'HIS', 7.71), ('NE2', 'HIS', 'CD2', 'HIS', 6.87), ('NE2', 'HIS', 'CE1', 'HIS', 6.87), ('NE2', 'HIS', 'NE2', 'HIS', 6.29)], [('CB', 'HIS', 'CB', 'HIS', 8.32), ('CB', 'HIS', 'CG', 'HIS', 8.53), ('CB', 'HIS', 'ND1', 'HIS', 9.79), ('CB', 'HIS', 'CD2', 'HIS', 7.8), ('CB', 'HIS', 'CE1', 'HIS', 9.94), ('CB', 'HIS', 'NE2', 'HIS', 8.83)], [('CG', 'HIS', 'CB', 'HIS', 7.76), ('CG', 'HIS', 'CG', 'HIS', 7.71), ('CG', 'HIS', 'ND1', 'HIS', 8.89), ('CG', 'HIS', 'CD2', 'HIS', 6.79), ('CG', 'HIS', 'CE1', 'HIS', 8.9), ('CG', 'HIS', 'NE2', 'HIS', 7.72)], [('ND1', 'HIS', 'CB', 'HIS', 7.64), ('ND1', 'HIS', 'CG', 'HIS', 7.62), ('ND1', 'HIS', 'ND1', 'HIS', 8.79), ('ND1', 'HIS', 'CD2', 'HIS', 6.77), ('ND1', 'HIS', 'CE1', 'HIS', 8.83), ('ND1', 'HIS', 'NE2', 'HIS', 7.71)], [('CD2', 'HIS', 'CB', 'HIS', 7.72), ('CD2', 'HIS', 'CG', 'HIS', 7.31), ('CD2', 'HIS', 'ND1', 'HIS', 8.35), ('CD2', 'HIS', 'CD2', 'HIS', 6.16), ('CD2', 'HIS', 'CE1', 'HIS', 8.12), ('CD2', 'HIS', 'NE2', 'HIS', 6.87)], [('CE1', 'HIS', 'CB', 'HIS', 7.49), ('CE1', 'HIS', 'CG', 'HIS', 7.16), ('CE1', 'HIS', 'ND1', 'HIS', 8.18), ('CE1', 'HIS', 'CD2', 'HIS', 6.15), ('CE1', 'HIS', 'CE1', 'HIS', 8.03), ('CE1', 'HIS', 'NE2', 'HIS', 6.87)], [('NE2', 'HIS', 'CB', 'HIS', 7.53), ('NE2', 'HIS', 'CG', 'HIS', 6.95), ('NE2', 'HIS', 'ND1', 'HIS', 7.88), ('NE2', 'HIS', 'CD2', 'HIS', 5.73), ('NE2', 'HIS', 'CE1', 'HIS', 7.56), ('NE2', 'HIS', 'NE2', 'HIS', 6.29)]]}
CA_HISI = { 
	'distances':
		[9.74, 9.5, 8.56, 10.53, 9.11, 10.27],
	'comparisons':
		[('CA', 'CA', 'CB', 'HISI', 9.74), ('CA', 'CA', 'CG', 'HISI', 9.5), ('CA', 'CA', 'ND1', 'HISI', 8.56), ('CA', 'CA', 'CD2', 'HISI', 10.53), ('CA', 'CA', 'CE1', 'HISI', 9.11), ('CA', 'CA', 'NE2', 'HISI', 10.27)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CA, d, 'M_1trk_2_2_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'M_1trk_2_2_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CA_HISI, d, 'M_1trk_2_2_1_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CA' :  match1,
		'HIS_HIS' :  match2,
		'CA_HISI' :  match3}