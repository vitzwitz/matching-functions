'''
FUNC:P_1n7n_4_2_2_1
PDB:1n7n
EC:4.2.2.1
RESI:asn,his,tyr
LOCI:a-349,399,408;
'''
import motifFunctions as cmd
ASN_TYR = { 
	'distances':
		[[9.37, 8.92, 7.75, 9.93, 7.79, 9.97, 8.98, 9.43], [8.7, 7.98, 6.74, 8.84, 6.53, 8.7, 7.63, 7.96], [8.71, 7.89, 6.77, 8.57, 6.44, 8.35, 7.34, 7.6], [8.52, 7.69, 6.33, 8.52, 5.96, 8.3, 7.11, 7.38]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 9.37), ('CB', 'ASN', 'CG', 'TYR', 8.92), ('CB', 'ASN', 'CD1', 'TYR', 7.75), ('CB', 'ASN', 'CD2', 'TYR', 9.93), ('CB', 'ASN', 'CE1', 'TYR', 7.79), ('CB', 'ASN', 'CE2', 'TYR', 9.97), ('CB', 'ASN', 'CZ', 'TYR', 8.98), ('CB', 'ASN', 'OH', 'TYR', 9.43)], [('CG', 'ASN', 'CB', 'TYR', 8.7), ('CG', 'ASN', 'CG', 'TYR', 7.98), ('CG', 'ASN', 'CD1', 'TYR', 6.74), ('CG', 'ASN', 'CD2', 'TYR', 8.84), ('CG', 'ASN', 'CE1', 'TYR', 6.53), ('CG', 'ASN', 'CE2', 'TYR', 8.7), ('CG', 'ASN', 'CZ', 'TYR', 7.63), ('CG', 'ASN', 'OH', 'TYR', 7.96)], [('OD1', 'ASN', 'CB', 'TYR', 8.71), ('OD1', 'ASN', 'CG', 'TYR', 7.89), ('OD1', 'ASN', 'CD1', 'TYR', 6.77), ('OD1', 'ASN', 'CD2', 'TYR', 8.57), ('OD1', 'ASN', 'CE1', 'TYR', 6.44), ('OD1', 'ASN', 'CE2', 'TYR', 8.35), ('OD1', 'ASN', 'CZ', 'TYR', 7.34), ('OD1', 'ASN', 'OH', 'TYR', 7.6)], [('ND2', 'ASN', 'CB', 'TYR', 8.52), ('ND2', 'ASN', 'CG', 'TYR', 7.69), ('ND2', 'ASN', 'CD1', 'TYR', 6.33), ('ND2', 'ASN', 'CD2', 'TYR', 8.52), ('ND2', 'ASN', 'CE1', 'TYR', 5.96), ('ND2', 'ASN', 'CE2', 'TYR', 8.3), ('ND2', 'ASN', 'CZ', 'TYR', 7.11), ('ND2', 'ASN', 'OH', 'TYR', 7.38)]]}
HIS_TYR = { 
	'distances':
		[[9.6, 8.82, 9.18, 8.15, 8.91, 7.82, 8.24, 8.39], [8.92, 7.92, 8.08, 7.26, 7.63, 6.72, 6.93, 6.97], [8.94, 7.77, 7.95, 6.88, 7.31, 6.08, 6.34, 6.16], [8.57, 7.51, 7.4, 7.12, 6.89, 6.58, 6.45, 6.51], [8.64, 7.31, 7.22, 6.53, 6.35, 5.5, 5.39, 4.99], [8.4, 7.12, 6.82, 6.67, 6.01, 5.84, 5.44, 5.24]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 9.6), ('CB', 'HIS', 'CG', 'TYR', 8.82), ('CB', 'HIS', 'CD1', 'TYR', 9.18), ('CB', 'HIS', 'CD2', 'TYR', 8.15), ('CB', 'HIS', 'CE1', 'TYR', 8.91), ('CB', 'HIS', 'CE2', 'TYR', 7.82), ('CB', 'HIS', 'CZ', 'TYR', 8.24), ('CB', 'HIS', 'OH', 'TYR', 8.39)], [('CG', 'HIS', 'CB', 'TYR', 8.92), ('CG', 'HIS', 'CG', 'TYR', 7.92), ('CG', 'HIS', 'CD1', 'TYR', 8.08), ('CG', 'HIS', 'CD2', 'TYR', 7.26), ('CG', 'HIS', 'CE1', 'TYR', 7.63), ('CG', 'HIS', 'CE2', 'TYR', 6.72), ('CG', 'HIS', 'CZ', 'TYR', 6.93), ('CG', 'HIS', 'OH', 'TYR', 6.97)], [('ND1', 'HIS', 'CB', 'TYR', 8.94), ('ND1', 'HIS', 'CG', 'TYR', 7.77), ('ND1', 'HIS', 'CD1', 'TYR', 7.95), ('ND1', 'HIS', 'CD2', 'TYR', 6.88), ('ND1', 'HIS', 'CE1', 'TYR', 7.31), ('ND1', 'HIS', 'CE2', 'TYR', 6.08), ('ND1', 'HIS', 'CZ', 'TYR', 6.34), ('ND1', 'HIS', 'OH', 'TYR', 6.16)], [('CD2', 'HIS', 'CB', 'TYR', 8.57), ('CD2', 'HIS', 'CG', 'TYR', 7.51), ('CD2', 'HIS', 'CD1', 'TYR', 7.4), ('CD2', 'HIS', 'CD2', 'TYR', 7.12), ('CD2', 'HIS', 'CE1', 'TYR', 6.89), ('CD2', 'HIS', 'CE2', 'TYR', 6.58), ('CD2', 'HIS', 'CZ', 'TYR', 6.45), ('CD2', 'HIS', 'OH', 'TYR', 6.51)], [('CE1', 'HIS', 'CB', 'TYR', 8.64), ('CE1', 'HIS', 'CG', 'TYR', 7.31), ('CE1', 'HIS', 'CD1', 'TYR', 7.22), ('CE1', 'HIS', 'CD2', 'TYR', 6.53), ('CE1', 'HIS', 'CE1', 'TYR', 6.35), ('CE1', 'HIS', 'CE2', 'TYR', 5.5), ('CE1', 'HIS', 'CZ', 'TYR', 5.39), ('CE1', 'HIS', 'OH', 'TYR', 4.99)], [('NE2', 'HIS', 'CB', 'TYR', 8.4), ('NE2', 'HIS', 'CG', 'TYR', 7.12), ('NE2', 'HIS', 'CD1', 'TYR', 6.82), ('NE2', 'HIS', 'CD2', 'TYR', 6.67), ('NE2', 'HIS', 'CE1', 'TYR', 6.01), ('NE2', 'HIS', 'CE2', 'TYR', 5.84), ('NE2', 'HIS', 'CZ', 'TYR', 5.44), ('NE2', 'HIS', 'OH', 'TYR', 5.24)]]}
ASN_HIS = { 
	'distances':
		[[11.73, 10.7, 11.16, 9.4, 10.3, 9.13], [10.66, 9.51, 9.85, 8.22, 8.9, 7.78], [9.58, 8.47, 8.9, 7.14, 8.03, 6.82], [11.11, 9.84, 9.95, 8.61, 8.87, 7.92]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 11.73), ('CB', 'ASN', 'CG', 'HIS', 10.7), ('CB', 'ASN', 'ND1', 'HIS', 11.16), ('CB', 'ASN', 'CD2', 'HIS', 9.4), ('CB', 'ASN', 'CE1', 'HIS', 10.3), ('CB', 'ASN', 'NE2', 'HIS', 9.13)], [('CG', 'ASN', 'CB', 'HIS', 10.66), ('CG', 'ASN', 'CG', 'HIS', 9.51), ('CG', 'ASN', 'ND1', 'HIS', 9.85), ('CG', 'ASN', 'CD2', 'HIS', 8.22), ('CG', 'ASN', 'CE1', 'HIS', 8.9), ('CG', 'ASN', 'NE2', 'HIS', 7.78)], [('OD1', 'ASN', 'CB', 'HIS', 9.58), ('OD1', 'ASN', 'CG', 'HIS', 8.47), ('OD1', 'ASN', 'ND1', 'HIS', 8.9), ('OD1', 'ASN', 'CD2', 'HIS', 7.14), ('OD1', 'ASN', 'CE1', 'HIS', 8.03), ('OD1', 'ASN', 'NE2', 'HIS', 6.82)], [('ND2', 'ASN', 'CB', 'HIS', 11.11), ('ND2', 'ASN', 'CG', 'HIS', 9.84), ('ND2', 'ASN', 'ND1', 'HIS', 9.95), ('ND2', 'ASN', 'CD2', 'HIS', 8.61), ('ND2', 'ASN', 'CE1', 'HIS', 8.87), ('ND2', 'ASN', 'NE2', 'HIS', 7.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_TYR, d, 'P_1n7n_4_2_2_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_TYR, d, 'P_1n7n_4_2_2_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_HIS, d, 'P_1n7n_4_2_2_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_TYR' :  match1,
		'HIS_TYR' :  match2,
		'ASN_HIS' :  match3}