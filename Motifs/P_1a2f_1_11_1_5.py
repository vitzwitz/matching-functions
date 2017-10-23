'''
FUNC:P_1a2f_1_11_1_5
PDB:1a2f
EC:1.11.1.5
RESI:arg,his,asn
LOCI:a-48,52,82;
'''
import motifFunctions as cmd
ARG_HIS = { 
	'distances':
		[[8.22, 7.78, 8.3, 7.25, 8.15, 7.51], [7.47, 6.72, 7.09, 6.09, 6.77, 6.14], [8.27, 7.33, 7.33, 6.82, 6.83, 6.49], [7.96, 6.77, 6.47, 6.29, 5.76, 5.63], [8.37, 7.19, 6.57, 7.0, 5.93, 6.23], [9.03, 8.03, 7.43, 8.02, 7.01, 7.39], [8.49, 7.18, 6.31, 7.06, 5.52, 6.07]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 8.22), ('CB', 'ARG', 'CG', 'HIS', 7.78), ('CB', 'ARG', 'ND1', 'HIS', 8.3), ('CB', 'ARG', 'CD2', 'HIS', 7.25), ('CB', 'ARG', 'CE1', 'HIS', 8.15), ('CB', 'ARG', 'NE2', 'HIS', 7.51)], [('CG', 'ARG', 'CB', 'HIS', 7.47), ('CG', 'ARG', 'CG', 'HIS', 6.72), ('CG', 'ARG', 'ND1', 'HIS', 7.09), ('CG', 'ARG', 'CD2', 'HIS', 6.09), ('CG', 'ARG', 'CE1', 'HIS', 6.77), ('CG', 'ARG', 'NE2', 'HIS', 6.14)], [('CD', 'ARG', 'CB', 'HIS', 8.27), ('CD', 'ARG', 'CG', 'HIS', 7.33), ('CD', 'ARG', 'ND1', 'HIS', 7.33), ('CD', 'ARG', 'CD2', 'HIS', 6.82), ('CD', 'ARG', 'CE1', 'HIS', 6.83), ('CD', 'ARG', 'NE2', 'HIS', 6.49)], [('NE', 'ARG', 'CB', 'HIS', 7.96), ('NE', 'ARG', 'CG', 'HIS', 6.77), ('NE', 'ARG', 'ND1', 'HIS', 6.47), ('NE', 'ARG', 'CD2', 'HIS', 6.29), ('NE', 'ARG', 'CE1', 'HIS', 5.76), ('NE', 'ARG', 'NE2', 'HIS', 5.63)], [('CZ', 'ARG', 'CB', 'HIS', 8.37), ('CZ', 'ARG', 'CG', 'HIS', 7.19), ('CZ', 'ARG', 'ND1', 'HIS', 6.57), ('CZ', 'ARG', 'CD2', 'HIS', 7.0), ('CZ', 'ARG', 'CE1', 'HIS', 5.93), ('CZ', 'ARG', 'NE2', 'HIS', 6.23)], [('NH1', 'ARG', 'CB', 'HIS', 9.03), ('NH1', 'ARG', 'CG', 'HIS', 8.03), ('NH1', 'ARG', 'ND1', 'HIS', 7.43), ('NH1', 'ARG', 'CD2', 'HIS', 8.02), ('NH1', 'ARG', 'CE1', 'HIS', 7.01), ('NH1', 'ARG', 'NE2', 'HIS', 7.39)], [('NH2', 'ARG', 'CB', 'HIS', 8.49), ('NH2', 'ARG', 'CG', 'HIS', 7.18), ('NH2', 'ARG', 'ND1', 'HIS', 6.31), ('NH2', 'ARG', 'CD2', 'HIS', 7.06), ('NH2', 'ARG', 'CE1', 'HIS', 5.52), ('NH2', 'ARG', 'NE2', 'HIS', 6.07)]]}
ARG_ASN = { 
	'distances':
		[[11.29, 11.19, 10.31, 12.23], [10.35, 10.24, 9.31, 11.34], [10.04, 10.19, 9.38, 11.39], [9.19, 9.37, 8.56, 10.61], [8.43, 8.85, 8.21, 10.14], [8.47, 9.1, 8.64, 10.4], [7.95, 8.39, 7.8, 9.69]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 11.29), ('CB', 'ARG', 'CG', 'ASN', 11.19), ('CB', 'ARG', 'OD1', 'ASN', 10.31), ('CB', 'ARG', 'ND2', 'ASN', 12.23)], [('CG', 'ARG', 'CB', 'ASN', 10.35), ('CG', 'ARG', 'CG', 'ASN', 10.24), ('CG', 'ARG', 'OD1', 'ASN', 9.31), ('CG', 'ARG', 'ND2', 'ASN', 11.34)], [('CD', 'ARG', 'CB', 'ASN', 10.04), ('CD', 'ARG', 'CG', 'ASN', 10.19), ('CD', 'ARG', 'OD1', 'ASN', 9.38), ('CD', 'ARG', 'ND2', 'ASN', 11.39)], [('NE', 'ARG', 'CB', 'ASN', 9.19), ('NE', 'ARG', 'CG', 'ASN', 9.37), ('NE', 'ARG', 'OD1', 'ASN', 8.56), ('NE', 'ARG', 'ND2', 'ASN', 10.61)], [('CZ', 'ARG', 'CB', 'ASN', 8.43), ('CZ', 'ARG', 'CG', 'ASN', 8.85), ('CZ', 'ARG', 'OD1', 'ASN', 8.21), ('CZ', 'ARG', 'ND2', 'ASN', 10.14)], [('NH1', 'ARG', 'CB', 'ASN', 8.47), ('NH1', 'ARG', 'CG', 'ASN', 9.1), ('NH1', 'ARG', 'OD1', 'ASN', 8.64), ('NH1', 'ARG', 'ND2', 'ASN', 10.4)], [('NH2', 'ARG', 'CB', 'ASN', 7.95), ('NH2', 'ARG', 'CG', 'ASN', 8.39), ('NH2', 'ARG', 'OD1', 'ASN', 7.8), ('NH2', 'ARG', 'ND2', 'ASN', 9.69)]]}
HIS_ASN = { 
	'distances':
		[[7.83, 6.78, 5.68, 7.29], [7.59, 6.75, 5.54, 7.53], [6.61, 5.93, 4.77, 6.89], [8.74, 8.0, 6.79, 8.83], [7.34, 6.88, 5.8, 7.92], [8.54, 8.0, 6.85, 8.96]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 7.83), ('CB', 'HIS', 'CG', 'ASN', 6.78), ('CB', 'HIS', 'OD1', 'ASN', 5.68), ('CB', 'HIS', 'ND2', 'ASN', 7.29)], [('CG', 'HIS', 'CB', 'ASN', 7.59), ('CG', 'HIS', 'CG', 'ASN', 6.75), ('CG', 'HIS', 'OD1', 'ASN', 5.54), ('CG', 'HIS', 'ND2', 'ASN', 7.53)], [('ND1', 'HIS', 'CB', 'ASN', 6.61), ('ND1', 'HIS', 'CG', 'ASN', 5.93), ('ND1', 'HIS', 'OD1', 'ASN', 4.77), ('ND1', 'HIS', 'ND2', 'ASN', 6.89)], [('CD2', 'HIS', 'CB', 'ASN', 8.74), ('CD2', 'HIS', 'CG', 'ASN', 8.0), ('CD2', 'HIS', 'OD1', 'ASN', 6.79), ('CD2', 'HIS', 'ND2', 'ASN', 8.83)], [('CE1', 'HIS', 'CB', 'ASN', 7.34), ('CE1', 'HIS', 'CG', 'ASN', 6.88), ('CE1', 'HIS', 'OD1', 'ASN', 5.8), ('CE1', 'HIS', 'ND2', 'ASN', 7.92)], [('NE2', 'HIS', 'CB', 'ASN', 8.54), ('NE2', 'HIS', 'CG', 'ASN', 8.0), ('NE2', 'HIS', 'OD1', 'ASN', 6.85), ('NE2', 'HIS', 'ND2', 'ASN', 8.96)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_HIS, d, 'P_1a2f_1_11_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_ASN, d, 'P_1a2f_1_11_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASN, d, 'P_1a2f_1_11_1_5')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_HIS' :  match1,
		'ARG_ASN' :  match2,
		'HIS_ASN' :  match3}