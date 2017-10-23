'''
FUNC:A_1apx_1_11_1_11
PDB:1apx
EC:1.11.1.11
RESI:arg,his,asn
LOCI:a-38,42,71;
'''
import motifFunctions as cmd
HIS_ARG = { 
	'distances':
		[[8.16, 7.4, 8.26, 7.81, 8.48, 9.49, 8.43], [7.6, 6.55, 7.29, 6.68, 7.42, 8.56, 7.32], [8.0, 6.75, 7.09, 6.15, 6.61, 7.8, 6.25], [7.13, 6.02, 6.89, 6.44, 7.4, 8.58, 7.45], [7.82, 6.4, 6.57, 5.52, 6.06, 7.36, 5.67], [7.28, 5.92, 6.42, 5.7, 6.59, 7.86, 6.51]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 8.16), ('CB', 'HIS', 'CG', 'ARG', 7.4), ('CB', 'HIS', 'CD', 'ARG', 8.26), ('CB', 'HIS', 'NE', 'ARG', 7.81), ('CB', 'HIS', 'CZ', 'ARG', 8.48), ('CB', 'HIS', 'NH1', 'ARG', 9.49), ('CB', 'HIS', 'NH2', 'ARG', 8.43)], [('CG', 'HIS', 'CB', 'ARG', 7.6), ('CG', 'HIS', 'CG', 'ARG', 6.55), ('CG', 'HIS', 'CD', 'ARG', 7.29), ('CG', 'HIS', 'NE', 'ARG', 6.68), ('CG', 'HIS', 'CZ', 'ARG', 7.42), ('CG', 'HIS', 'NH1', 'ARG', 8.56), ('CG', 'HIS', 'NH2', 'ARG', 7.32)], [('ND1', 'HIS', 'CB', 'ARG', 8.0), ('ND1', 'HIS', 'CG', 'ARG', 6.75), ('ND1', 'HIS', 'CD', 'ARG', 7.09), ('ND1', 'HIS', 'NE', 'ARG', 6.15), ('ND1', 'HIS', 'CZ', 'ARG', 6.61), ('ND1', 'HIS', 'NH1', 'ARG', 7.8), ('ND1', 'HIS', 'NH2', 'ARG', 6.25)], [('CD2', 'HIS', 'CB', 'ARG', 7.13), ('CD2', 'HIS', 'CG', 'ARG', 6.02), ('CD2', 'HIS', 'CD', 'ARG', 6.89), ('CD2', 'HIS', 'NE', 'ARG', 6.44), ('CD2', 'HIS', 'CZ', 'ARG', 7.4), ('CD2', 'HIS', 'NH1', 'ARG', 8.58), ('CD2', 'HIS', 'NH2', 'ARG', 7.45)], [('CE1', 'HIS', 'CB', 'ARG', 7.82), ('CE1', 'HIS', 'CG', 'ARG', 6.4), ('CE1', 'HIS', 'CD', 'ARG', 6.57), ('CE1', 'HIS', 'NE', 'ARG', 5.52), ('CE1', 'HIS', 'CZ', 'ARG', 6.06), ('CE1', 'HIS', 'NH1', 'ARG', 7.36), ('CE1', 'HIS', 'NH2', 'ARG', 5.67)], [('NE2', 'HIS', 'CB', 'ARG', 7.28), ('NE2', 'HIS', 'CG', 'ARG', 5.92), ('NE2', 'HIS', 'CD', 'ARG', 6.42), ('NE2', 'HIS', 'NE', 'ARG', 5.7), ('NE2', 'HIS', 'CZ', 'ARG', 6.59), ('NE2', 'HIS', 'NH1', 'ARG', 7.86), ('NE2', 'HIS', 'NH2', 'ARG', 6.51)]]}
ASN_ARG = { 
	'distances':
		[[11.3, 10.19, 9.9, 8.7, 8.16, 8.83, 7.23], [11.11, 10.02, 10.0, 8.87, 8.62, 9.47, 7.79], [10.23, 9.09, 9.19, 8.08, 8.03, 9.02, 7.28], [12.13, 11.12, 11.2, 10.13, 9.91, 10.73, 9.11]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ARG', 11.3), ('CB', 'ASN', 'CG', 'ARG', 10.19), ('CB', 'ASN', 'CD', 'ARG', 9.9), ('CB', 'ASN', 'NE', 'ARG', 8.7), ('CB', 'ASN', 'CZ', 'ARG', 8.16), ('CB', 'ASN', 'NH1', 'ARG', 8.83), ('CB', 'ASN', 'NH2', 'ARG', 7.23)], [('CG', 'ASN', 'CB', 'ARG', 11.11), ('CG', 'ASN', 'CG', 'ARG', 10.02), ('CG', 'ASN', 'CD', 'ARG', 10.0), ('CG', 'ASN', 'NE', 'ARG', 8.87), ('CG', 'ASN', 'CZ', 'ARG', 8.62), ('CG', 'ASN', 'NH1', 'ARG', 9.47), ('CG', 'ASN', 'NH2', 'ARG', 7.79)], [('OD1', 'ASN', 'CB', 'ARG', 10.23), ('OD1', 'ASN', 'CG', 'ARG', 9.09), ('OD1', 'ASN', 'CD', 'ARG', 9.19), ('OD1', 'ASN', 'NE', 'ARG', 8.08), ('OD1', 'ASN', 'CZ', 'ARG', 8.03), ('OD1', 'ASN', 'NH1', 'ARG', 9.02), ('OD1', 'ASN', 'NH2', 'ARG', 7.28)], [('ND2', 'ASN', 'CB', 'ARG', 12.13), ('ND2', 'ASN', 'CG', 'ARG', 11.12), ('ND2', 'ASN', 'CD', 'ARG', 11.2), ('ND2', 'ASN', 'NE', 'ARG', 10.13), ('ND2', 'ASN', 'CZ', 'ARG', 9.91), ('ND2', 'ASN', 'NH1', 'ARG', 10.73), ('ND2', 'ASN', 'NH2', 'ARG', 9.11)]]}
HIS_ASN = { 
	'distances':
		[[7.82, 6.71, 5.69, 7.22], [7.66, 6.74, 5.56, 7.54], [6.58, 5.86, 4.68, 6.88], [8.75, 7.93, 6.72, 8.8], [7.26, 6.77, 5.65, 7.89], [8.52, 7.92, 6.74, 8.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 7.82), ('CB', 'HIS', 'CG', 'ASN', 6.71), ('CB', 'HIS', 'OD1', 'ASN', 5.69), ('CB', 'HIS', 'ND2', 'ASN', 7.22)], [('CG', 'HIS', 'CB', 'ASN', 7.66), ('CG', 'HIS', 'CG', 'ASN', 6.74), ('CG', 'HIS', 'OD1', 'ASN', 5.56), ('CG', 'HIS', 'ND2', 'ASN', 7.54)], [('ND1', 'HIS', 'CB', 'ASN', 6.58), ('ND1', 'HIS', 'CG', 'ASN', 5.86), ('ND1', 'HIS', 'OD1', 'ASN', 4.68), ('ND1', 'HIS', 'ND2', 'ASN', 6.88)], [('CD2', 'HIS', 'CB', 'ASN', 8.75), ('CD2', 'HIS', 'CG', 'ASN', 7.93), ('CD2', 'HIS', 'OD1', 'ASN', 6.72), ('CD2', 'HIS', 'ND2', 'ASN', 8.8)], [('CE1', 'HIS', 'CB', 'ASN', 7.26), ('CE1', 'HIS', 'CG', 'ASN', 6.77), ('CE1', 'HIS', 'OD1', 'ASN', 5.65), ('CE1', 'HIS', 'ND2', 'ASN', 7.89)], [('NE2', 'HIS', 'CB', 'ASN', 8.52), ('NE2', 'HIS', 'CG', 'ASN', 7.92), ('NE2', 'HIS', 'OD1', 'ASN', 6.74), ('NE2', 'HIS', 'ND2', 'ASN', 8.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ARG, d, 'A_1apx_1_11_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_ARG, d, 'A_1apx_1_11_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'A_1apx_1_11_1_11')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ARG' :  match1,
		'ASN_ARG' :  match2,
		'HIS_ASN' :  match3}