'''
FUNC:A_1naa_1_1_99_18
PDB:1naa
EC:1.1.99.18
RESI:tyr,his,asn
LOCI:a-609,689,732;
'''
import motifFunctions as cmd
ASN_TYR = { 
	'distances':
		[[10.55, 9.82, 9.85, 9.44, 9.47, 9.1, 9.11, 9.1], [9.67, 8.82, 8.96, 8.26, 8.52, 7.83, 7.96, 7.95], [9.54, 8.8, 9.18, 8.09, 8.87, 7.79, 8.2, 8.3], [9.39, 8.35, 8.29, 7.78, 7.63, 7.13, 7.03, 6.83]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 10.55), ('CB', 'ASN', 'CG', 'TYR', 9.82), ('CB', 'ASN', 'CD1', 'TYR', 9.85), ('CB', 'ASN', 'CD2', 'TYR', 9.44), ('CB', 'ASN', 'CE1', 'TYR', 9.47), ('CB', 'ASN', 'CE2', 'TYR', 9.1), ('CB', 'ASN', 'CZ', 'TYR', 9.11), ('CB', 'ASN', 'OH', 'TYR', 9.1)], [('CG', 'ASN', 'CB', 'TYR', 9.67), ('CG', 'ASN', 'CG', 'TYR', 8.82), ('CG', 'ASN', 'CD1', 'TYR', 8.96), ('CG', 'ASN', 'CD2', 'TYR', 8.26), ('CG', 'ASN', 'CE1', 'TYR', 8.52), ('CG', 'ASN', 'CE2', 'TYR', 7.83), ('CG', 'ASN', 'CZ', 'TYR', 7.96), ('CG', 'ASN', 'OH', 'TYR', 7.95)], [('OD1', 'ASN', 'CB', 'TYR', 9.54), ('OD1', 'ASN', 'CG', 'TYR', 8.8), ('OD1', 'ASN', 'CD1', 'TYR', 9.18), ('OD1', 'ASN', 'CD2', 'TYR', 8.09), ('OD1', 'ASN', 'CE1', 'TYR', 8.87), ('OD1', 'ASN', 'CE2', 'TYR', 7.79), ('OD1', 'ASN', 'CZ', 'TYR', 8.2), ('OD1', 'ASN', 'OH', 'TYR', 8.3)], [('ND2', 'ASN', 'CB', 'TYR', 9.39), ('ND2', 'ASN', 'CG', 'TYR', 8.35), ('ND2', 'ASN', 'CD1', 'TYR', 8.29), ('ND2', 'ASN', 'CD2', 'TYR', 7.78), ('ND2', 'ASN', 'CE1', 'TYR', 7.63), ('ND2', 'ASN', 'CE2', 'TYR', 7.13), ('ND2', 'ASN', 'CZ', 'TYR', 7.03), ('ND2', 'ASN', 'OH', 'TYR', 6.83)]]}
HIS_TYR = { 
	'distances':
		[[10.44, 10.01, 9.18, 10.75, 9.15, 10.73, 9.97, 10.32], [9.84, 9.22, 8.42, 9.77, 8.19, 9.61, 8.85, 9.09], [8.55, 7.91, 7.23, 8.44, 7.09, 8.36, 7.71, 8.11], [10.59, 9.78, 8.97, 10.13, 8.48, 9.76, 8.93, 8.91], [8.62, 7.76, 7.13, 8.01, 6.72, 7.7, 7.05, 7.24], [9.9, 8.95, 8.25, 9.12, 7.63, 8.64, 7.87, 7.78]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 10.44), ('CB', 'HIS', 'CG', 'TYR', 10.01), ('CB', 'HIS', 'CD1', 'TYR', 9.18), ('CB', 'HIS', 'CD2', 'TYR', 10.75), ('CB', 'HIS', 'CE1', 'TYR', 9.15), ('CB', 'HIS', 'CE2', 'TYR', 10.73), ('CB', 'HIS', 'CZ', 'TYR', 9.97), ('CB', 'HIS', 'OH', 'TYR', 10.32)], [('CG', 'HIS', 'CB', 'TYR', 9.84), ('CG', 'HIS', 'CG', 'TYR', 9.22), ('CG', 'HIS', 'CD1', 'TYR', 8.42), ('CG', 'HIS', 'CD2', 'TYR', 9.77), ('CG', 'HIS', 'CE1', 'TYR', 8.19), ('CG', 'HIS', 'CE2', 'TYR', 9.61), ('CG', 'HIS', 'CZ', 'TYR', 8.85), ('CG', 'HIS', 'OH', 'TYR', 9.09)], [('ND1', 'HIS', 'CB', 'TYR', 8.55), ('ND1', 'HIS', 'CG', 'TYR', 7.91), ('ND1', 'HIS', 'CD1', 'TYR', 7.23), ('ND1', 'HIS', 'CD2', 'TYR', 8.44), ('ND1', 'HIS', 'CE1', 'TYR', 7.09), ('ND1', 'HIS', 'CE2', 'TYR', 8.36), ('ND1', 'HIS', 'CZ', 'TYR', 7.71), ('ND1', 'HIS', 'OH', 'TYR', 8.11)], [('CD2', 'HIS', 'CB', 'TYR', 10.59), ('CD2', 'HIS', 'CG', 'TYR', 9.78), ('CD2', 'HIS', 'CD1', 'TYR', 8.97), ('CD2', 'HIS', 'CD2', 'TYR', 10.13), ('CD2', 'HIS', 'CE1', 'TYR', 8.48), ('CD2', 'HIS', 'CE2', 'TYR', 9.76), ('CD2', 'HIS', 'CZ', 'TYR', 8.93), ('CD2', 'HIS', 'OH', 'TYR', 8.91)], [('CE1', 'HIS', 'CB', 'TYR', 8.62), ('CE1', 'HIS', 'CG', 'TYR', 7.76), ('CE1', 'HIS', 'CD1', 'TYR', 7.13), ('CE1', 'HIS', 'CD2', 'TYR', 8.01), ('CE1', 'HIS', 'CE1', 'TYR', 6.72), ('CE1', 'HIS', 'CE2', 'TYR', 7.7), ('CE1', 'HIS', 'CZ', 'TYR', 7.05), ('CE1', 'HIS', 'OH', 'TYR', 7.24)], [('NE2', 'HIS', 'CB', 'TYR', 9.9), ('NE2', 'HIS', 'CG', 'TYR', 8.95), ('NE2', 'HIS', 'CD1', 'TYR', 8.25), ('NE2', 'HIS', 'CD2', 'TYR', 9.12), ('NE2', 'HIS', 'CE1', 'TYR', 7.63), ('NE2', 'HIS', 'CE2', 'TYR', 8.64), ('NE2', 'HIS', 'CZ', 'TYR', 7.87), ('NE2', 'HIS', 'OH', 'TYR', 7.78)]]}
HIS_ASN = { 
	'distances':
		[[8.82, 9.36, 10.33, 9.06], [7.57, 8.01, 9.03, 7.62], [7.01, 7.18, 8.09, 6.79], [7.11, 7.6, 8.75, 7.1], [6.12, 6.14, 7.13, 5.57], [6.18, 6.42, 7.57, 5.77]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 8.82), ('CB', 'HIS', 'CG', 'ASN', 9.36), ('CB', 'HIS', 'OD1', 'ASN', 10.33), ('CB', 'HIS', 'ND2', 'ASN', 9.06)], [('CG', 'HIS', 'CB', 'ASN', 7.57), ('CG', 'HIS', 'CG', 'ASN', 8.01), ('CG', 'HIS', 'OD1', 'ASN', 9.03), ('CG', 'HIS', 'ND2', 'ASN', 7.62)], [('ND1', 'HIS', 'CB', 'ASN', 7.01), ('ND1', 'HIS', 'CG', 'ASN', 7.18), ('ND1', 'HIS', 'OD1', 'ASN', 8.09), ('ND1', 'HIS', 'ND2', 'ASN', 6.79)], [('CD2', 'HIS', 'CB', 'ASN', 7.11), ('CD2', 'HIS', 'CG', 'ASN', 7.6), ('CD2', 'HIS', 'OD1', 'ASN', 8.75), ('CD2', 'HIS', 'ND2', 'ASN', 7.1)], [('CE1', 'HIS', 'CB', 'ASN', 6.12), ('CE1', 'HIS', 'CG', 'ASN', 6.14), ('CE1', 'HIS', 'OD1', 'ASN', 7.13), ('CE1', 'HIS', 'ND2', 'ASN', 5.57)], [('NE2', 'HIS', 'CB', 'ASN', 6.18), ('NE2', 'HIS', 'CG', 'ASN', 6.42), ('NE2', 'HIS', 'OD1', 'ASN', 7.57), ('NE2', 'HIS', 'ND2', 'ASN', 5.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_TYR, d, 'A_1naa_1_1_99_18')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_TYR, d, 'A_1naa_1_1_99_18')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1naa_1_1_99_18')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_TYR' :  match1,
		'HIS_TYR' :  match2,
		'HIS_ASN' :  match3}