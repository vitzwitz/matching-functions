'''
FUNC:A_1gcb_3_4_22_40
PDB:1gcb
EC:3.4.22.40
RESI:gln,cys,his,asn
LOCI:a-67,73,369,392;
'''
import motifFunctions as cmd
GLN_ASN = { 
	'distances':
		[[11.34, 10.73, 9.77, 11.48], [10.53, 9.75, 8.81, 10.36], [10.13, 9.21, 8.14, 9.82], [9.18, 8.3, 7.17, 9.02], [11.08, 10.02, 8.94, 10.5]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASN', 11.34), ('CB', 'GLN', 'CG', 'ASN', 10.73), ('CB', 'GLN', 'OD1', 'ASN', 9.77), ('CB', 'GLN', 'ND2', 'ASN', 11.48)], [('CG', 'GLN', 'CB', 'ASN', 10.53), ('CG', 'GLN', 'CG', 'ASN', 9.75), ('CG', 'GLN', 'OD1', 'ASN', 8.81), ('CG', 'GLN', 'ND2', 'ASN', 10.36)], [('CD', 'GLN', 'CB', 'ASN', 10.13), ('CD', 'GLN', 'CG', 'ASN', 9.21), ('CD', 'GLN', 'OD1', 'ASN', 8.14), ('CD', 'GLN', 'ND2', 'ASN', 9.82)], [('OE1', 'GLN', 'CB', 'ASN', 9.18), ('OE1', 'GLN', 'CG', 'ASN', 8.3), ('OE1', 'GLN', 'OD1', 'ASN', 7.17), ('OE1', 'GLN', 'ND2', 'ASN', 9.02)], [('NE2', 'GLN', 'CB', 'ASN', 11.08), ('NE2', 'GLN', 'CG', 'ASN', 10.02), ('NE2', 'GLN', 'OD1', 'ASN', 8.94), ('NE2', 'GLN', 'ND2', 'ASN', 10.5)]]}
HIS_CYS = { 
	'distances':
		[[7.33, 6.92, 9.98, 9.35, 8.84, 9.53], [6.52, 6.63, 9.14, 8.63, 8.0, 8.83], [5.37, 5.69, 8.25, 7.65, 6.82, 7.58], [7.15, 7.63, 9.42, 9.11, 8.51, 9.49], [5.46, 6.36, 8.01, 7.61, 6.71, 7.6], [6.59, 7.47, 8.75, 8.52, 7.79, 8.81]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 7.33), ('CB', 'HIS', 'SG', 'CYS', 6.92), ('CB', 'HIS', 'O', 'CYS', 9.98), ('CB', 'HIS', 'C', 'CYS', 9.35), ('CB', 'HIS', 'CA', 'CYS', 8.84), ('CB', 'HIS', 'N', 'CYS', 9.53)], [('CG', 'HIS', 'CB', 'CYS', 6.52), ('CG', 'HIS', 'SG', 'CYS', 6.63), ('CG', 'HIS', 'O', 'CYS', 9.14), ('CG', 'HIS', 'C', 'CYS', 8.63), ('CG', 'HIS', 'CA', 'CYS', 8.0), ('CG', 'HIS', 'N', 'CYS', 8.83)], [('ND1', 'HIS', 'CB', 'CYS', 5.37), ('ND1', 'HIS', 'SG', 'CYS', 5.69), ('ND1', 'HIS', 'O', 'CYS', 8.25), ('ND1', 'HIS', 'C', 'CYS', 7.65), ('ND1', 'HIS', 'CA', 'CYS', 6.82), ('ND1', 'HIS', 'N', 'CYS', 7.58)], [('CD2', 'HIS', 'CB', 'CYS', 7.15), ('CD2', 'HIS', 'SG', 'CYS', 7.63), ('CD2', 'HIS', 'O', 'CYS', 9.42), ('CD2', 'HIS', 'C', 'CYS', 9.11), ('CD2', 'HIS', 'CA', 'CYS', 8.51), ('CD2', 'HIS', 'N', 'CYS', 9.49)], [('CE1', 'HIS', 'CB', 'CYS', 5.46), ('CE1', 'HIS', 'SG', 'CYS', 6.36), ('CE1', 'HIS', 'O', 'CYS', 8.01), ('CE1', 'HIS', 'C', 'CYS', 7.61), ('CE1', 'HIS', 'CA', 'CYS', 6.71), ('CE1', 'HIS', 'N', 'CYS', 7.6)], [('NE2', 'HIS', 'CB', 'CYS', 6.59), ('NE2', 'HIS', 'SG', 'CYS', 7.47), ('NE2', 'HIS', 'O', 'CYS', 8.75), ('NE2', 'HIS', 'C', 'CYS', 8.52), ('NE2', 'HIS', 'CA', 'CYS', 7.79), ('NE2', 'HIS', 'N', 'CYS', 8.81)]]}
CYS_GLN = { 
	'distances':
		[[7.82, 7.42, 5.98, 5.3, 5.9], [9.06, 8.62, 7.15, 6.78, 6.62], [8.63, 8.91, 7.91, 7.08, 8.29], [8.34, 8.52, 7.39, 6.7, 7.53], [7.13, 7.14, 5.93, 5.33, 6.03], [6.74, 6.89, 5.8, 5.67, 5.57]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 7.82), ('CB', 'CYS', 'CG', 'GLN', 7.42), ('CB', 'CYS', 'CD', 'GLN', 5.98), ('CB', 'CYS', 'OE1', 'GLN', 5.3), ('CB', 'CYS', 'NE2', 'GLN', 5.9)], [('SG', 'CYS', 'CB', 'GLN', 9.06), ('SG', 'CYS', 'CG', 'GLN', 8.62), ('SG', 'CYS', 'CD', 'GLN', 7.15), ('SG', 'CYS', 'OE1', 'GLN', 6.78), ('SG', 'CYS', 'NE2', 'GLN', 6.62)], [('O', 'CYS', 'CB', 'GLN', 8.63), ('O', 'CYS', 'CG', 'GLN', 8.91), ('O', 'CYS', 'CD', 'GLN', 7.91), ('O', 'CYS', 'OE1', 'GLN', 7.08), ('O', 'CYS', 'NE2', 'GLN', 8.29)], [('C', 'CYS', 'CB', 'GLN', 8.34), ('C', 'CYS', 'CG', 'GLN', 8.52), ('C', 'CYS', 'CD', 'GLN', 7.39), ('C', 'CYS', 'OE1', 'GLN', 6.7), ('C', 'CYS', 'NE2', 'GLN', 7.53)], [('CA', 'CYS', 'CB', 'GLN', 7.13), ('CA', 'CYS', 'CG', 'GLN', 7.14), ('CA', 'CYS', 'CD', 'GLN', 5.93), ('CA', 'CYS', 'OE1', 'GLN', 5.33), ('CA', 'CYS', 'NE2', 'GLN', 6.03)], [('N', 'CYS', 'CB', 'GLN', 6.74), ('N', 'CYS', 'CG', 'GLN', 6.89), ('N', 'CYS', 'CD', 'GLN', 5.8), ('N', 'CYS', 'OE1', 'GLN', 5.67), ('N', 'CYS', 'NE2', 'GLN', 5.57)]]}
HIS_GLN = { 
	'distances':
		[[12.06, 11.0, 9.58, 9.01, 9.23], [10.92, 9.85, 8.48, 7.8, 8.33], [9.58, 8.55, 7.14, 6.49, 6.98], [11.08, 10.0, 8.75, 7.93, 8.84], [8.91, 7.86, 6.57, 5.75, 6.74], [9.91, 8.84, 7.67, 6.79, 7.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 12.06), ('CB', 'HIS', 'CG', 'GLN', 11.0), ('CB', 'HIS', 'CD', 'GLN', 9.58), ('CB', 'HIS', 'OE1', 'GLN', 9.01), ('CB', 'HIS', 'NE2', 'GLN', 9.23)], [('CG', 'HIS', 'CB', 'GLN', 10.92), ('CG', 'HIS', 'CG', 'GLN', 9.85), ('CG', 'HIS', 'CD', 'GLN', 8.48), ('CG', 'HIS', 'OE1', 'GLN', 7.8), ('CG', 'HIS', 'NE2', 'GLN', 8.33)], [('ND1', 'HIS', 'CB', 'GLN', 9.58), ('ND1', 'HIS', 'CG', 'GLN', 8.55), ('ND1', 'HIS', 'CD', 'GLN', 7.14), ('ND1', 'HIS', 'OE1', 'GLN', 6.49), ('ND1', 'HIS', 'NE2', 'GLN', 6.98)], [('CD2', 'HIS', 'CB', 'GLN', 11.08), ('CD2', 'HIS', 'CG', 'GLN', 10.0), ('CD2', 'HIS', 'CD', 'GLN', 8.75), ('CD2', 'HIS', 'OE1', 'GLN', 7.93), ('CD2', 'HIS', 'NE2', 'GLN', 8.84)], [('CE1', 'HIS', 'CB', 'GLN', 8.91), ('CE1', 'HIS', 'CG', 'GLN', 7.86), ('CE1', 'HIS', 'CD', 'GLN', 6.57), ('CE1', 'HIS', 'OE1', 'GLN', 5.75), ('CE1', 'HIS', 'NE2', 'GLN', 6.74)], [('NE2', 'HIS', 'CB', 'GLN', 9.91), ('NE2', 'HIS', 'CG', 'GLN', 8.84), ('NE2', 'HIS', 'CD', 'GLN', 7.67), ('NE2', 'HIS', 'OE1', 'GLN', 6.79), ('NE2', 'HIS', 'NE2', 'GLN', 7.97)]]}
HIS_ASN = { 
	'distances':
		[[10.52, 9.19, 8.43, 9.13], [9.15, 7.81, 6.98, 7.87], [9.12, 7.79, 6.78, 8.03], [7.92, 6.61, 5.9, 6.64], [7.93, 6.64, 5.55, 7.02], [7.04, 5.71, 4.79, 5.99]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 10.52), ('CB', 'HIS', 'CG', 'ASN', 9.19), ('CB', 'HIS', 'OD1', 'ASN', 8.43), ('CB', 'HIS', 'ND2', 'ASN', 9.13)], [('CG', 'HIS', 'CB', 'ASN', 9.15), ('CG', 'HIS', 'CG', 'ASN', 7.81), ('CG', 'HIS', 'OD1', 'ASN', 6.98), ('CG', 'HIS', 'ND2', 'ASN', 7.87)], [('ND1', 'HIS', 'CB', 'ASN', 9.12), ('ND1', 'HIS', 'CG', 'ASN', 7.79), ('ND1', 'HIS', 'OD1', 'ASN', 6.78), ('ND1', 'HIS', 'ND2', 'ASN', 8.03)], [('CD2', 'HIS', 'CB', 'ASN', 7.92), ('CD2', 'HIS', 'CG', 'ASN', 6.61), ('CD2', 'HIS', 'OD1', 'ASN', 5.9), ('CD2', 'HIS', 'ND2', 'ASN', 6.64)], [('CE1', 'HIS', 'CB', 'ASN', 7.93), ('CE1', 'HIS', 'CG', 'ASN', 6.64), ('CE1', 'HIS', 'OD1', 'ASN', 5.55), ('CE1', 'HIS', 'ND2', 'ASN', 7.02)], [('NE2', 'HIS', 'CB', 'ASN', 7.04), ('NE2', 'HIS', 'CG', 'ASN', 5.71), ('NE2', 'HIS', 'OD1', 'ASN', 4.79), ('NE2', 'HIS', 'ND2', 'ASN', 5.99)]]}
CYS_ASN = { 
	'distances':
		[[10.39, 9.43, 8.21, 10.15], [11.85, 10.78, 9.59, 11.33], [11.09, 10.63, 9.5, 11.68], [11.48, 10.84, 9.65, 11.78], [10.94, 10.16, 8.94, 11.02], [12.1, 11.26, 10.04, 12.05]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASN', 10.39), ('CB', 'CYS', 'CG', 'ASN', 9.43), ('CB', 'CYS', 'OD1', 'ASN', 8.21), ('CB', 'CYS', 'ND2', 'ASN', 10.15)], [('SG', 'CYS', 'CB', 'ASN', 11.85), ('SG', 'CYS', 'CG', 'ASN', 10.78), ('SG', 'CYS', 'OD1', 'ASN', 9.59), ('SG', 'CYS', 'ND2', 'ASN', 11.33)], [('O', 'CYS', 'CB', 'ASN', 11.09), ('O', 'CYS', 'CG', 'ASN', 10.63), ('O', 'CYS', 'OD1', 'ASN', 9.5), ('O', 'CYS', 'ND2', 'ASN', 11.68)], [('C', 'CYS', 'CB', 'ASN', 11.48), ('C', 'CYS', 'CG', 'ASN', 10.84), ('C', 'CYS', 'OD1', 'ASN', 9.65), ('C', 'CYS', 'ND2', 'ASN', 11.78)], [('CA', 'CYS', 'CB', 'ASN', 10.94), ('CA', 'CYS', 'CG', 'ASN', 10.16), ('CA', 'CYS', 'OD1', 'ASN', 8.94), ('CA', 'CYS', 'ND2', 'ASN', 11.02)], [('N', 'CYS', 'CB', 'ASN', 12.1), ('N', 'CYS', 'CG', 'ASN', 11.26), ('N', 'CYS', 'OD1', 'ASN', 10.04), ('N', 'CYS', 'ND2', 'ASN', 12.05)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_ASN, d, 'A_1gcb_3_4_22_40')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CYS, d, 'A_1gcb_3_4_22_40')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_GLN, d, 'A_1gcb_3_4_22_40')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLN, d, 'A_1gcb_3_4_22_40')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_ASN, d, 'A_1gcb_3_4_22_40')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_ASN, d, 'A_1gcb_3_4_22_40')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_ASN' :  match1,
		'HIS_CYS' :  match2,
		'CYS_GLN' :  match3,
		'HIS_GLN' :  match4,
		'HIS_ASN' :  match5,
		'CYS_ASN' :  match6}