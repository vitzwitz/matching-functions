'''
FUNC:A_1oya_1_6_99_1
PDB:1oya
EC:1.6.99.1
RESI:his,asn,tyr
LOCI:a-191,194,196;
'''
import motifFunctions as cmd
TYR_HIS = { 
	'distances':
		[[8.11, 7.39, 7.24, 7.35, 7.12, 7.19], [8.44, 7.46, 6.96, 7.42, 6.61, 6.92], [9.56, 8.62, 7.96, 8.7, 7.64, 8.12], [8.02, 6.8, 6.18, 6.6, 5.54, 5.85], [10.22, 9.15, 8.29, 9.23, 7.81, 8.45], [8.83, 7.51, 6.63, 7.33, 5.8, 6.34], [9.9, 8.66, 7.7, 8.63, 7.01, 7.67], [10.89, 9.6, 8.53, 9.57, 7.77, 8.51]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 8.11), ('CB', 'TYR', 'CG', 'HIS', 7.39), ('CB', 'TYR', 'ND1', 'HIS', 7.24), ('CB', 'TYR', 'CD2', 'HIS', 7.35), ('CB', 'TYR', 'CE1', 'HIS', 7.12), ('CB', 'TYR', 'NE2', 'HIS', 7.19)], [('CG', 'TYR', 'CB', 'HIS', 8.44), ('CG', 'TYR', 'CG', 'HIS', 7.46), ('CG', 'TYR', 'ND1', 'HIS', 6.96), ('CG', 'TYR', 'CD2', 'HIS', 7.42), ('CG', 'TYR', 'CE1', 'HIS', 6.61), ('CG', 'TYR', 'NE2', 'HIS', 6.92)], [('CD1', 'TYR', 'CB', 'HIS', 9.56), ('CD1', 'TYR', 'CG', 'HIS', 8.62), ('CD1', 'TYR', 'ND1', 'HIS', 7.96), ('CD1', 'TYR', 'CD2', 'HIS', 8.7), ('CD1', 'TYR', 'CE1', 'HIS', 7.64), ('CD1', 'TYR', 'NE2', 'HIS', 8.12)], [('CD2', 'TYR', 'CB', 'HIS', 8.02), ('CD2', 'TYR', 'CG', 'HIS', 6.8), ('CD2', 'TYR', 'ND1', 'HIS', 6.18), ('CD2', 'TYR', 'CD2', 'HIS', 6.6), ('CD2', 'TYR', 'CE1', 'HIS', 5.54), ('CD2', 'TYR', 'NE2', 'HIS', 5.85)], [('CE1', 'TYR', 'CB', 'HIS', 10.22), ('CE1', 'TYR', 'CG', 'HIS', 9.15), ('CE1', 'TYR', 'ND1', 'HIS', 8.29), ('CE1', 'TYR', 'CD2', 'HIS', 9.23), ('CE1', 'TYR', 'CE1', 'HIS', 7.81), ('CE1', 'TYR', 'NE2', 'HIS', 8.45)], [('CE2', 'TYR', 'CB', 'HIS', 8.83), ('CE2', 'TYR', 'CG', 'HIS', 7.51), ('CE2', 'TYR', 'ND1', 'HIS', 6.63), ('CE2', 'TYR', 'CD2', 'HIS', 7.33), ('CE2', 'TYR', 'CE1', 'HIS', 5.8), ('CE2', 'TYR', 'NE2', 'HIS', 6.34)], [('CZ', 'TYR', 'CB', 'HIS', 9.9), ('CZ', 'TYR', 'CG', 'HIS', 8.66), ('CZ', 'TYR', 'ND1', 'HIS', 7.7), ('CZ', 'TYR', 'CD2', 'HIS', 8.63), ('CZ', 'TYR', 'CE1', 'HIS', 7.01), ('CZ', 'TYR', 'NE2', 'HIS', 7.67)], [('OH', 'TYR', 'CB', 'HIS', 10.89), ('OH', 'TYR', 'CG', 'HIS', 9.6), ('OH', 'TYR', 'ND1', 'HIS', 8.53), ('OH', 'TYR', 'CD2', 'HIS', 9.57), ('OH', 'TYR', 'CE1', 'HIS', 7.77), ('OH', 'TYR', 'NE2', 'HIS', 8.51)]]}
TYR_ASN = { 
	'distances':
		[[7.85, 9.14, 10.07, 9.49], [7.13, 8.43, 9.48, 8.67], [8.01, 9.33, 10.42, 9.52], [5.91, 7.12, 8.23, 7.29], [7.93, 9.17, 10.3, 9.23], [5.77, 6.86, 8.04, 6.86], [6.92, 8.02, 9.19, 7.99], [7.4, 8.32, 9.47, 8.16]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASN', 7.85), ('CB', 'TYR', 'CG', 'ASN', 9.14), ('CB', 'TYR', 'OD1', 'ASN', 10.07), ('CB', 'TYR', 'ND2', 'ASN', 9.49)], [('CG', 'TYR', 'CB', 'ASN', 7.13), ('CG', 'TYR', 'CG', 'ASN', 8.43), ('CG', 'TYR', 'OD1', 'ASN', 9.48), ('CG', 'TYR', 'ND2', 'ASN', 8.67)], [('CD1', 'TYR', 'CB', 'ASN', 8.01), ('CD1', 'TYR', 'CG', 'ASN', 9.33), ('CD1', 'TYR', 'OD1', 'ASN', 10.42), ('CD1', 'TYR', 'ND2', 'ASN', 9.52)], [('CD2', 'TYR', 'CB', 'ASN', 5.91), ('CD2', 'TYR', 'CG', 'ASN', 7.12), ('CD2', 'TYR', 'OD1', 'ASN', 8.23), ('CD2', 'TYR', 'ND2', 'ASN', 7.29)], [('CE1', 'TYR', 'CB', 'ASN', 7.93), ('CE1', 'TYR', 'CG', 'ASN', 9.17), ('CE1', 'TYR', 'OD1', 'ASN', 10.3), ('CE1', 'TYR', 'ND2', 'ASN', 9.23)], [('CE2', 'TYR', 'CB', 'ASN', 5.77), ('CE2', 'TYR', 'CG', 'ASN', 6.86), ('CE2', 'TYR', 'OD1', 'ASN', 8.04), ('CE2', 'TYR', 'ND2', 'ASN', 6.86)], [('CZ', 'TYR', 'CB', 'ASN', 6.92), ('CZ', 'TYR', 'CG', 'ASN', 8.02), ('CZ', 'TYR', 'OD1', 'ASN', 9.19), ('CZ', 'TYR', 'ND2', 'ASN', 7.99)], [('OH', 'TYR', 'CB', 'ASN', 7.4), ('OH', 'TYR', 'CG', 'ASN', 8.32), ('OH', 'TYR', 'OD1', 'ASN', 9.47), ('OH', 'TYR', 'ND2', 'ASN', 8.16)]]}
ASN_HIS = { 
	'distances':
		[[9.4, 7.92, 7.58, 6.93, 6.33, 5.84], [9.58, 8.11, 7.81, 7.07, 6.53, 5.98], [10.32, 8.92, 8.78, 7.76, 7.55, 6.83], [9.23, 7.75, 7.28, 6.89, 6.01, 5.72]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 9.4), ('CB', 'ASN', 'CG', 'HIS', 7.92), ('CB', 'ASN', 'ND1', 'HIS', 7.58), ('CB', 'ASN', 'CD2', 'HIS', 6.93), ('CB', 'ASN', 'CE1', 'HIS', 6.33), ('CB', 'ASN', 'NE2', 'HIS', 5.84)], [('CG', 'ASN', 'CB', 'HIS', 9.58), ('CG', 'ASN', 'CG', 'HIS', 8.11), ('CG', 'ASN', 'ND1', 'HIS', 7.81), ('CG', 'ASN', 'CD2', 'HIS', 7.07), ('CG', 'ASN', 'CE1', 'HIS', 6.53), ('CG', 'ASN', 'NE2', 'HIS', 5.98)], [('OD1', 'ASN', 'CB', 'HIS', 10.32), ('OD1', 'ASN', 'CG', 'HIS', 8.92), ('OD1', 'ASN', 'ND1', 'HIS', 8.78), ('OD1', 'ASN', 'CD2', 'HIS', 7.76), ('OD1', 'ASN', 'CE1', 'HIS', 7.55), ('OD1', 'ASN', 'NE2', 'HIS', 6.83)], [('ND2', 'ASN', 'CB', 'HIS', 9.23), ('ND2', 'ASN', 'CG', 'HIS', 7.75), ('ND2', 'ASN', 'ND1', 'HIS', 7.28), ('ND2', 'ASN', 'CD2', 'HIS', 6.89), ('ND2', 'ASN', 'CE1', 'HIS', 6.01), ('ND2', 'ASN', 'NE2', 'HIS', 5.72)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_HIS, d, 'A_1oya_1_6_99_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_ASN, d, 'A_1oya_1_6_99_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'A_1oya_1_6_99_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_HIS' :  match1,
		'TYR_ASN' :  match2,
		'ASN_HIS' :  match3}