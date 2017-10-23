'''
FUNC:M_1v04_3_1_1_2
PDB:1v04
EC:3.1.1.2
RESI:his,his,ca
LOCI:a-115,134,1357;
'''
import motifFunctions as cmd
HIS_CA = { 
	'distances':
		[[14.14], [12.82], [12.84], [11.53], [11.66], [10.75], [8.98], [7.78], [7.98], [6.63], [7.09], [6.13]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 14.14)], [('CG', 'HIS', 'CA', 'CA', 12.82)], [('ND1', 'HIS', 'CA', 'CA', 12.84)], [('CD2', 'HIS', 'CA', 'CA', 11.53)], [('CE1', 'HIS', 'CA', 'CA', 11.66)], [('NE2', 'HIS', 'CA', 'CA', 10.75)], [('CB', 'HIS', 'CA', 'CA', 8.98)], [('CG', 'HIS', 'CA', 'CA', 7.78)], [('ND1', 'HIS', 'CA', 'CA', 7.98)], [('CD2', 'HIS', 'CA', 'CA', 6.63)], [('CE1', 'HIS', 'CA', 'CA', 7.09)], [('NE2', 'HIS', 'CA', 'CA', 6.13)]]}
HIS_HIS = { 
	'distances':
		[[8.19, 8.66, 8.18, 9.88, 9.16, 10.12], [7.16, 7.48, 6.84, 8.71, 7.84, 8.87], [7.66, 7.86, 7.03, 9.1, 7.95, 9.11], [5.95, 6.15, 5.56, 7.36, 6.59, 7.55], [6.96, 6.96, 6.01, 8.16, 6.9, 8.1], [5.82, 5.76, 4.88, 6.96, 5.87, 6.99], [8.19, 7.16, 7.66, 5.95, 6.96, 5.82], [8.66, 7.48, 7.86, 6.15, 6.96, 5.76], [8.18, 6.84, 7.03, 5.56, 6.01, 4.88], [9.88, 8.71, 9.1, 7.36, 8.16, 6.96], [9.16, 7.84, 7.95, 6.59, 6.9, 5.87], [10.12, 8.87, 9.11, 7.55, 8.1, 6.99]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 8.19), ('CB', 'HIS', 'CG', 'HIS', 8.66), ('CB', 'HIS', 'ND1', 'HIS', 8.18), ('CB', 'HIS', 'CD2', 'HIS', 9.88), ('CB', 'HIS', 'CE1', 'HIS', 9.16), ('CB', 'HIS', 'NE2', 'HIS', 10.12)], [('CG', 'HIS', 'CB', 'HIS', 7.16), ('CG', 'HIS', 'CG', 'HIS', 7.48), ('CG', 'HIS', 'ND1', 'HIS', 6.84), ('CG', 'HIS', 'CD2', 'HIS', 8.71), ('CG', 'HIS', 'CE1', 'HIS', 7.84), ('CG', 'HIS', 'NE2', 'HIS', 8.87)], [('ND1', 'HIS', 'CB', 'HIS', 7.66), ('ND1', 'HIS', 'CG', 'HIS', 7.86), ('ND1', 'HIS', 'ND1', 'HIS', 7.03), ('ND1', 'HIS', 'CD2', 'HIS', 9.1), ('ND1', 'HIS', 'CE1', 'HIS', 7.95), ('ND1', 'HIS', 'NE2', 'HIS', 9.11)], [('CD2', 'HIS', 'CB', 'HIS', 5.95), ('CD2', 'HIS', 'CG', 'HIS', 6.15), ('CD2', 'HIS', 'ND1', 'HIS', 5.56), ('CD2', 'HIS', 'CD2', 'HIS', 7.36), ('CD2', 'HIS', 'CE1', 'HIS', 6.59), ('CD2', 'HIS', 'NE2', 'HIS', 7.55)], [('CE1', 'HIS', 'CB', 'HIS', 6.96), ('CE1', 'HIS', 'CG', 'HIS', 6.96), ('CE1', 'HIS', 'ND1', 'HIS', 6.01), ('CE1', 'HIS', 'CD2', 'HIS', 8.16), ('CE1', 'HIS', 'CE1', 'HIS', 6.9), ('CE1', 'HIS', 'NE2', 'HIS', 8.1)], [('NE2', 'HIS', 'CB', 'HIS', 5.82), ('NE2', 'HIS', 'CG', 'HIS', 5.76), ('NE2', 'HIS', 'ND1', 'HIS', 4.88), ('NE2', 'HIS', 'CD2', 'HIS', 6.96), ('NE2', 'HIS', 'CE1', 'HIS', 5.87), ('NE2', 'HIS', 'NE2', 'HIS', 6.99)], [('CB', 'HIS', 'CB', 'HIS', 8.19), ('CB', 'HIS', 'CG', 'HIS', 7.16), ('CB', 'HIS', 'ND1', 'HIS', 7.66), ('CB', 'HIS', 'CD2', 'HIS', 5.95), ('CB', 'HIS', 'CE1', 'HIS', 6.96), ('CB', 'HIS', 'NE2', 'HIS', 5.82)], [('CG', 'HIS', 'CB', 'HIS', 8.66), ('CG', 'HIS', 'CG', 'HIS', 7.48), ('CG', 'HIS', 'ND1', 'HIS', 7.86), ('CG', 'HIS', 'CD2', 'HIS', 6.15), ('CG', 'HIS', 'CE1', 'HIS', 6.96), ('CG', 'HIS', 'NE2', 'HIS', 5.76)], [('ND1', 'HIS', 'CB', 'HIS', 8.18), ('ND1', 'HIS', 'CG', 'HIS', 6.84), ('ND1', 'HIS', 'ND1', 'HIS', 7.03), ('ND1', 'HIS', 'CD2', 'HIS', 5.56), ('ND1', 'HIS', 'CE1', 'HIS', 6.01), ('ND1', 'HIS', 'NE2', 'HIS', 4.88)], [('CD2', 'HIS', 'CB', 'HIS', 9.88), ('CD2', 'HIS', 'CG', 'HIS', 8.71), ('CD2', 'HIS', 'ND1', 'HIS', 9.1), ('CD2', 'HIS', 'CD2', 'HIS', 7.36), ('CD2', 'HIS', 'CE1', 'HIS', 8.16), ('CD2', 'HIS', 'NE2', 'HIS', 6.96)], [('CE1', 'HIS', 'CB', 'HIS', 9.16), ('CE1', 'HIS', 'CG', 'HIS', 7.84), ('CE1', 'HIS', 'ND1', 'HIS', 7.95), ('CE1', 'HIS', 'CD2', 'HIS', 6.59), ('CE1', 'HIS', 'CE1', 'HIS', 6.9), ('CE1', 'HIS', 'NE2', 'HIS', 5.87)], [('NE2', 'HIS', 'CB', 'HIS', 10.12), ('NE2', 'HIS', 'CG', 'HIS', 8.87), ('NE2', 'HIS', 'ND1', 'HIS', 9.11), ('NE2', 'HIS', 'CD2', 'HIS', 7.55), ('NE2', 'HIS', 'CE1', 'HIS', 8.1), ('NE2', 'HIS', 'NE2', 'HIS', 6.99)]]}
CA_HISI = { 
	'distances':
		[8.98, 7.78, 7.98, 6.63, 7.09, 6.13],
	'comparisons':
		[('CA', 'CA', 'CB', 'HISI', 8.98), ('CA', 'CA', 'CG', 'HISI', 7.78), ('CA', 'CA', 'ND1', 'HISI', 7.98), ('CA', 'CA', 'CD2', 'HISI', 6.63), ('CA', 'CA', 'CE1', 'HISI', 7.09), ('CA', 'CA', 'NE2', 'HISI', 6.13)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CA, d, 'M_1v04_3_1_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'M_1v04_3_1_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CA_HISI, d, 'M_1v04_3_1_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CA' :  match1,
		'HIS_HIS' :  match2,
		'CA_HISI' :  match3}