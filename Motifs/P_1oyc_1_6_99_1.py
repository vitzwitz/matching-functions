'''
FUNC:P_1oyc_1_6_99_1
PDB:1oyc
EC:1.6.99.1
RESI:his,asn,tyr
LOCI:a-191,194,196;
'''
import motifFunctions as cmd
ASN_TYR = { 
	'distances':
		[[7.68, 7.04, 7.92, 5.91, 7.87, 5.86, 6.96, 7.53], [8.98, 8.37, 9.29, 7.13, 9.17, 6.97, 8.12, 8.51], [9.89, 9.4, 10.32, 8.23, 10.25, 8.13, 9.24, 9.61], [9.39, 8.7, 9.63, 7.36, 9.43, 7.09, 8.28, 8.56]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 7.68), ('CB', 'ASN', 'CG', 'TYR', 7.04), ('CB', 'ASN', 'CD1', 'TYR', 7.92), ('CB', 'ASN', 'CD2', 'TYR', 5.91), ('CB', 'ASN', 'CE1', 'TYR', 7.87), ('CB', 'ASN', 'CE2', 'TYR', 5.86), ('CB', 'ASN', 'CZ', 'TYR', 6.96), ('CB', 'ASN', 'OH', 'TYR', 7.53)], [('CG', 'ASN', 'CB', 'TYR', 8.98), ('CG', 'ASN', 'CG', 'TYR', 8.37), ('CG', 'ASN', 'CD1', 'TYR', 9.29), ('CG', 'ASN', 'CD2', 'TYR', 7.13), ('CG', 'ASN', 'CE1', 'TYR', 9.17), ('CG', 'ASN', 'CE2', 'TYR', 6.97), ('CG', 'ASN', 'CZ', 'TYR', 8.12), ('CG', 'ASN', 'OH', 'TYR', 8.51)], [('OD1', 'ASN', 'CB', 'TYR', 9.89), ('OD1', 'ASN', 'CG', 'TYR', 9.4), ('OD1', 'ASN', 'CD1', 'TYR', 10.32), ('OD1', 'ASN', 'CD2', 'TYR', 8.23), ('OD1', 'ASN', 'CE1', 'TYR', 10.25), ('OD1', 'ASN', 'CE2', 'TYR', 8.13), ('OD1', 'ASN', 'CZ', 'TYR', 9.24), ('OD1', 'ASN', 'OH', 'TYR', 9.61)], [('ND2', 'ASN', 'CB', 'TYR', 9.39), ('ND2', 'ASN', 'CG', 'TYR', 8.7), ('ND2', 'ASN', 'CD1', 'TYR', 9.63), ('ND2', 'ASN', 'CD2', 'TYR', 7.36), ('ND2', 'ASN', 'CE1', 'TYR', 9.43), ('ND2', 'ASN', 'CE2', 'TYR', 7.09), ('ND2', 'ASN', 'CZ', 'TYR', 8.28), ('ND2', 'ASN', 'OH', 'TYR', 8.56)]]}
HIS_TYR = { 
	'distances':
		[[7.99, 8.4, 9.57, 7.99, 10.28, 8.89, 9.98, 10.94], [7.3, 7.46, 8.68, 6.8, 9.24, 7.6, 8.78, 9.7], [7.17, 6.97, 8.06, 6.17, 8.43, 6.73, 7.86, 8.66], [7.3, 7.47, 8.78, 6.67, 9.33, 7.48, 8.78, 9.72], [7.08, 6.66, 7.77, 5.58, 7.99, 5.96, 7.22, 7.96], [7.17, 7.0, 8.25, 5.96, 8.61, 6.54, 7.88, 8.71]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 7.99), ('CB', 'HIS', 'CG', 'TYR', 8.4), ('CB', 'HIS', 'CD1', 'TYR', 9.57), ('CB', 'HIS', 'CD2', 'TYR', 7.99), ('CB', 'HIS', 'CE1', 'TYR', 10.28), ('CB', 'HIS', 'CE2', 'TYR', 8.89), ('CB', 'HIS', 'CZ', 'TYR', 9.98), ('CB', 'HIS', 'OH', 'TYR', 10.94)], [('CG', 'HIS', 'CB', 'TYR', 7.3), ('CG', 'HIS', 'CG', 'TYR', 7.46), ('CG', 'HIS', 'CD1', 'TYR', 8.68), ('CG', 'HIS', 'CD2', 'TYR', 6.8), ('CG', 'HIS', 'CE1', 'TYR', 9.24), ('CG', 'HIS', 'CE2', 'TYR', 7.6), ('CG', 'HIS', 'CZ', 'TYR', 8.78), ('CG', 'HIS', 'OH', 'TYR', 9.7)], [('ND1', 'HIS', 'CB', 'TYR', 7.17), ('ND1', 'HIS', 'CG', 'TYR', 6.97), ('ND1', 'HIS', 'CD1', 'TYR', 8.06), ('ND1', 'HIS', 'CD2', 'TYR', 6.17), ('ND1', 'HIS', 'CE1', 'TYR', 8.43), ('ND1', 'HIS', 'CE2', 'TYR', 6.73), ('ND1', 'HIS', 'CZ', 'TYR', 7.86), ('ND1', 'HIS', 'OH', 'TYR', 8.66)], [('CD2', 'HIS', 'CB', 'TYR', 7.3), ('CD2', 'HIS', 'CG', 'TYR', 7.47), ('CD2', 'HIS', 'CD1', 'TYR', 8.78), ('CD2', 'HIS', 'CD2', 'TYR', 6.67), ('CD2', 'HIS', 'CE1', 'TYR', 9.33), ('CD2', 'HIS', 'CE2', 'TYR', 7.48), ('CD2', 'HIS', 'CZ', 'TYR', 8.78), ('CD2', 'HIS', 'OH', 'TYR', 9.72)], [('CE1', 'HIS', 'CB', 'TYR', 7.08), ('CE1', 'HIS', 'CG', 'TYR', 6.66), ('CE1', 'HIS', 'CD1', 'TYR', 7.77), ('CE1', 'HIS', 'CD2', 'TYR', 5.58), ('CE1', 'HIS', 'CE1', 'TYR', 7.99), ('CE1', 'HIS', 'CE2', 'TYR', 5.96), ('CE1', 'HIS', 'CZ', 'TYR', 7.22), ('CE1', 'HIS', 'OH', 'TYR', 7.96)], [('NE2', 'HIS', 'CB', 'TYR', 7.17), ('NE2', 'HIS', 'CG', 'TYR', 7.0), ('NE2', 'HIS', 'CD1', 'TYR', 8.25), ('NE2', 'HIS', 'CD2', 'TYR', 5.96), ('NE2', 'HIS', 'CE1', 'TYR', 8.61), ('NE2', 'HIS', 'CE2', 'TYR', 6.54), ('NE2', 'HIS', 'CZ', 'TYR', 7.88), ('NE2', 'HIS', 'OH', 'TYR', 8.71)]]}
HIS_ASN = { 
	'distances':
		[[9.4, 9.61, 10.43, 9.16], [7.94, 8.14, 9.03, 7.69], [7.62, 7.87, 8.9, 7.3], [6.98, 7.09, 7.86, 6.77], [6.38, 6.58, 7.65, 6.02], [5.91, 6.0, 6.91, 5.63]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 9.4), ('CB', 'HIS', 'CG', 'ASN', 9.61), ('CB', 'HIS', 'OD1', 'ASN', 10.43), ('CB', 'HIS', 'ND2', 'ASN', 9.16)], [('CG', 'HIS', 'CB', 'ASN', 7.94), ('CG', 'HIS', 'CG', 'ASN', 8.14), ('CG', 'HIS', 'OD1', 'ASN', 9.03), ('CG', 'HIS', 'ND2', 'ASN', 7.69)], [('ND1', 'HIS', 'CB', 'ASN', 7.62), ('ND1', 'HIS', 'CG', 'ASN', 7.87), ('ND1', 'HIS', 'OD1', 'ASN', 8.9), ('ND1', 'HIS', 'ND2', 'ASN', 7.3)], [('CD2', 'HIS', 'CB', 'ASN', 6.98), ('CD2', 'HIS', 'CG', 'ASN', 7.09), ('CD2', 'HIS', 'OD1', 'ASN', 7.86), ('CD2', 'HIS', 'ND2', 'ASN', 6.77)], [('CE1', 'HIS', 'CB', 'ASN', 6.38), ('CE1', 'HIS', 'CG', 'ASN', 6.58), ('CE1', 'HIS', 'OD1', 'ASN', 7.65), ('CE1', 'HIS', 'ND2', 'ASN', 6.02)], [('NE2', 'HIS', 'CB', 'ASN', 5.91), ('NE2', 'HIS', 'CG', 'ASN', 6.0), ('NE2', 'HIS', 'OD1', 'ASN', 6.91), ('NE2', 'HIS', 'ND2', 'ASN', 5.63)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_TYR, d, 'P_1oyc_1_6_99_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_TYR, d, 'P_1oyc_1_6_99_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'P_1oyc_1_6_99_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_TYR' :  match1,
		'HIS_TYR' :  match2,
		'HIS_ASN' :  match3}