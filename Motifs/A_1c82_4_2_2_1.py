'''
FUNC:A_1c82_4_2_2_1
PDB:1c82
EC:4.2.2.1
RESI:asn,his,tyr
LOCI:a-349,399,408;
'''
import motifFunctions as cmd
ASN_TYR = { 
	'distances':
		[[9.39, 8.81, 7.63, 9.77, 7.58, 9.74, 8.73, 9.14], [8.82, 7.98, 6.72, 8.76, 6.38, 8.53, 7.43, 7.71], [8.78, 7.82, 6.7, 8.42, 6.24, 8.09, 7.06, 7.26], [8.75, 7.83, 6.46, 8.6, 5.97, 8.29, 7.07, 7.25]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 9.39), ('CB', 'ASN', 'CG', 'TYR', 8.81), ('CB', 'ASN', 'CD1', 'TYR', 7.63), ('CB', 'ASN', 'CD2', 'TYR', 9.77), ('CB', 'ASN', 'CE1', 'TYR', 7.58), ('CB', 'ASN', 'CE2', 'TYR', 9.74), ('CB', 'ASN', 'CZ', 'TYR', 8.73), ('CB', 'ASN', 'OH', 'TYR', 9.14)], [('CG', 'ASN', 'CB', 'TYR', 8.82), ('CG', 'ASN', 'CG', 'TYR', 7.98), ('CG', 'ASN', 'CD1', 'TYR', 6.72), ('CG', 'ASN', 'CD2', 'TYR', 8.76), ('CG', 'ASN', 'CE1', 'TYR', 6.38), ('CG', 'ASN', 'CE2', 'TYR', 8.53), ('CG', 'ASN', 'CZ', 'TYR', 7.43), ('CG', 'ASN', 'OH', 'TYR', 7.71)], [('OD1', 'ASN', 'CB', 'TYR', 8.78), ('OD1', 'ASN', 'CG', 'TYR', 7.82), ('OD1', 'ASN', 'CD1', 'TYR', 6.7), ('OD1', 'ASN', 'CD2', 'TYR', 8.42), ('OD1', 'ASN', 'CE1', 'TYR', 6.24), ('OD1', 'ASN', 'CE2', 'TYR', 8.09), ('OD1', 'ASN', 'CZ', 'TYR', 7.06), ('OD1', 'ASN', 'OH', 'TYR', 7.26)], [('ND2', 'ASN', 'CB', 'TYR', 8.75), ('ND2', 'ASN', 'CG', 'TYR', 7.83), ('ND2', 'ASN', 'CD1', 'TYR', 6.46), ('ND2', 'ASN', 'CD2', 'TYR', 8.6), ('ND2', 'ASN', 'CE1', 'TYR', 5.97), ('ND2', 'ASN', 'CE2', 'TYR', 8.29), ('ND2', 'ASN', 'CZ', 'TYR', 7.07), ('ND2', 'ASN', 'OH', 'TYR', 7.25)]]}
TYR_HIS = { 
	'distances':
		[[9.5, 8.96, 9.19, 8.61, 9.01, 8.65], [8.64, 7.87, 7.97, 7.44, 7.63, 7.29], [9.06, 8.08, 8.17, 7.37, 7.56, 7.03], [7.85, 7.08, 6.97, 6.92, 6.76, 6.71], [8.8, 7.61, 7.49, 6.82, 6.66, 6.16], [7.53, 6.5, 6.11, 6.31, 5.66, 5.78], [8.05, 6.81, 6.44, 6.27, 5.61, 5.46], [8.25, 6.86, 6.22, 6.32, 5.13, 5.17]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 9.5), ('CB', 'TYR', 'CG', 'HIS', 8.96), ('CB', 'TYR', 'ND1', 'HIS', 9.19), ('CB', 'TYR', 'CD2', 'HIS', 8.61), ('CB', 'TYR', 'CE1', 'HIS', 9.01), ('CB', 'TYR', 'NE2', 'HIS', 8.65)], [('CG', 'TYR', 'CB', 'HIS', 8.64), ('CG', 'TYR', 'CG', 'HIS', 7.87), ('CG', 'TYR', 'ND1', 'HIS', 7.97), ('CG', 'TYR', 'CD2', 'HIS', 7.44), ('CG', 'TYR', 'CE1', 'HIS', 7.63), ('CG', 'TYR', 'NE2', 'HIS', 7.29)], [('CD1', 'TYR', 'CB', 'HIS', 9.06), ('CD1', 'TYR', 'CG', 'HIS', 8.08), ('CD1', 'TYR', 'ND1', 'HIS', 8.17), ('CD1', 'TYR', 'CD2', 'HIS', 7.37), ('CD1', 'TYR', 'CE1', 'HIS', 7.56), ('CD1', 'TYR', 'NE2', 'HIS', 7.03)], [('CD2', 'TYR', 'CB', 'HIS', 7.85), ('CD2', 'TYR', 'CG', 'HIS', 7.08), ('CD2', 'TYR', 'ND1', 'HIS', 6.97), ('CD2', 'TYR', 'CD2', 'HIS', 6.92), ('CD2', 'TYR', 'CE1', 'HIS', 6.76), ('CD2', 'TYR', 'NE2', 'HIS', 6.71)], [('CE1', 'TYR', 'CB', 'HIS', 8.8), ('CE1', 'TYR', 'CG', 'HIS', 7.61), ('CE1', 'TYR', 'ND1', 'HIS', 7.49), ('CE1', 'TYR', 'CD2', 'HIS', 6.82), ('CE1', 'TYR', 'CE1', 'HIS', 6.66), ('CE1', 'TYR', 'NE2', 'HIS', 6.16)], [('CE2', 'TYR', 'CB', 'HIS', 7.53), ('CE2', 'TYR', 'CG', 'HIS', 6.5), ('CE2', 'TYR', 'ND1', 'HIS', 6.11), ('CE2', 'TYR', 'CD2', 'HIS', 6.31), ('CE2', 'TYR', 'CE1', 'HIS', 5.66), ('CE2', 'TYR', 'NE2', 'HIS', 5.78)], [('CZ', 'TYR', 'CB', 'HIS', 8.05), ('CZ', 'TYR', 'CG', 'HIS', 6.81), ('CZ', 'TYR', 'ND1', 'HIS', 6.44), ('CZ', 'TYR', 'CD2', 'HIS', 6.27), ('CZ', 'TYR', 'CE1', 'HIS', 5.61), ('CZ', 'TYR', 'NE2', 'HIS', 5.46)], [('OH', 'TYR', 'CB', 'HIS', 8.25), ('OH', 'TYR', 'CG', 'HIS', 6.86), ('OH', 'TYR', 'ND1', 'HIS', 6.22), ('OH', 'TYR', 'CD2', 'HIS', 6.32), ('OH', 'TYR', 'CE1', 'HIS', 5.13), ('OH', 'TYR', 'NE2', 'HIS', 5.17)]]}
ASN_HIS = { 
	'distances':
		[[11.6, 10.63, 11.16, 9.32, 10.34, 9.14], [10.61, 9.51, 9.9, 8.2, 8.99, 7.84], [9.53, 8.44, 8.9, 7.1, 8.05, 6.83], [11.15, 9.93, 10.11, 8.68, 9.08, 8.08]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 11.6), ('CB', 'ASN', 'CG', 'HIS', 10.63), ('CB', 'ASN', 'ND1', 'HIS', 11.16), ('CB', 'ASN', 'CD2', 'HIS', 9.32), ('CB', 'ASN', 'CE1', 'HIS', 10.34), ('CB', 'ASN', 'NE2', 'HIS', 9.14)], [('CG', 'ASN', 'CB', 'HIS', 10.61), ('CG', 'ASN', 'CG', 'HIS', 9.51), ('CG', 'ASN', 'ND1', 'HIS', 9.9), ('CG', 'ASN', 'CD2', 'HIS', 8.2), ('CG', 'ASN', 'CE1', 'HIS', 8.99), ('CG', 'ASN', 'NE2', 'HIS', 7.84)], [('OD1', 'ASN', 'CB', 'HIS', 9.53), ('OD1', 'ASN', 'CG', 'HIS', 8.44), ('OD1', 'ASN', 'ND1', 'HIS', 8.9), ('OD1', 'ASN', 'CD2', 'HIS', 7.1), ('OD1', 'ASN', 'CE1', 'HIS', 8.05), ('OD1', 'ASN', 'NE2', 'HIS', 6.83)], [('ND2', 'ASN', 'CB', 'HIS', 11.15), ('ND2', 'ASN', 'CG', 'HIS', 9.93), ('ND2', 'ASN', 'ND1', 'HIS', 10.11), ('ND2', 'ASN', 'CD2', 'HIS', 8.68), ('ND2', 'ASN', 'CE1', 'HIS', 9.08), ('ND2', 'ASN', 'NE2', 'HIS', 8.08)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_TYR, d, 'A_1c82_4_2_2_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_HIS, d, 'A_1c82_4_2_2_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'A_1c82_4_2_2_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_TYR' :  match1,
		'TYR_HIS' :  match2,
		'ASN_HIS' :  match3}