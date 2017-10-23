'''
FUNC:A_1ei5_3_4_11_19
PDB:1ei5
EC:3.4.11.19
RESI:ser,lys,tyr,asn,his
LOCI:a-62,65,153,155,287;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[10.69, 9.18, 8.55, 8.62, 7.18, 7.28, 6.43, 5.06], [10.25, 8.77, 7.91, 8.46, 6.51, 7.24, 6.11, 4.84]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 10.69), ('CB', 'SER', 'CG', 'TYR', 9.18), ('CB', 'SER', 'CD1', 'TYR', 8.55), ('CB', 'SER', 'CD2', 'TYR', 8.62), ('CB', 'SER', 'CE1', 'TYR', 7.18), ('CB', 'SER', 'CE2', 'TYR', 7.28), ('CB', 'SER', 'CZ', 'TYR', 6.43), ('CB', 'SER', 'OH', 'TYR', 5.06)], [('OG', 'SER', 'CB', 'TYR', 10.25), ('OG', 'SER', 'CG', 'TYR', 8.77), ('OG', 'SER', 'CD1', 'TYR', 7.91), ('OG', 'SER', 'CD2', 'TYR', 8.46), ('OG', 'SER', 'CE1', 'TYR', 6.51), ('OG', 'SER', 'CE2', 'TYR', 7.24), ('OG', 'SER', 'CZ', 'TYR', 6.11), ('OG', 'SER', 'OH', 'TYR', 4.84)]]}
LYS_HIS = { 
	'distances':
		[[8.54, 7.68, 7.22, 7.63, 6.87, 7.13], [9.15, 8.09, 7.71, 7.7, 7.04, 7.01], [8.98, 7.71, 7.13, 7.22, 6.18, 6.23], [10.13, 8.78, 8.27, 8.06, 7.16, 6.98], [10.24, 8.93, 8.71, 8.01, 7.64, 7.1]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 8.54), ('CB', 'LYS', 'CG', 'HIS', 7.68), ('CB', 'LYS', 'ND1', 'HIS', 7.22), ('CB', 'LYS', 'CD2', 'HIS', 7.63), ('CB', 'LYS', 'CE1', 'HIS', 6.87), ('CB', 'LYS', 'NE2', 'HIS', 7.13)], [('CG', 'LYS', 'CB', 'HIS', 9.15), ('CG', 'LYS', 'CG', 'HIS', 8.09), ('CG', 'LYS', 'ND1', 'HIS', 7.71), ('CG', 'LYS', 'CD2', 'HIS', 7.7), ('CG', 'LYS', 'CE1', 'HIS', 7.04), ('CG', 'LYS', 'NE2', 'HIS', 7.01)], [('CD', 'LYS', 'CB', 'HIS', 8.98), ('CD', 'LYS', 'CG', 'HIS', 7.71), ('CD', 'LYS', 'ND1', 'HIS', 7.13), ('CD', 'LYS', 'CD2', 'HIS', 7.22), ('CD', 'LYS', 'CE1', 'HIS', 6.18), ('CD', 'LYS', 'NE2', 'HIS', 6.23)], [('CE', 'LYS', 'CB', 'HIS', 10.13), ('CE', 'LYS', 'CG', 'HIS', 8.78), ('CE', 'LYS', 'ND1', 'HIS', 8.27), ('CE', 'LYS', 'CD2', 'HIS', 8.06), ('CE', 'LYS', 'CE1', 'HIS', 7.16), ('CE', 'LYS', 'NE2', 'HIS', 6.98)], [('NZ', 'LYS', 'CB', 'HIS', 10.24), ('NZ', 'LYS', 'CG', 'HIS', 8.93), ('NZ', 'LYS', 'ND1', 'HIS', 8.71), ('NZ', 'LYS', 'CD2', 'HIS', 8.01), ('NZ', 'LYS', 'CE1', 'HIS', 7.64), ('NZ', 'LYS', 'NE2', 'HIS', 7.1)]]}
ASN_TYR = { 
	'distances':
		[[9.6, 8.75, 7.81, 9.23, 7.36, 8.91, 7.97, 8.03], [8.8, 7.83, 6.72, 8.34, 6.12, 7.94, 6.84, 6.9], [8.28, 7.46, 6.23, 8.21, 5.87, 8.0, 6.89, 7.17], [8.99, 7.8, 6.73, 8.07, 5.79, 7.4, 6.22, 5.95]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 9.6), ('CB', 'ASN', 'CG', 'TYR', 8.75), ('CB', 'ASN', 'CD1', 'TYR', 7.81), ('CB', 'ASN', 'CD2', 'TYR', 9.23), ('CB', 'ASN', 'CE1', 'TYR', 7.36), ('CB', 'ASN', 'CE2', 'TYR', 8.91), ('CB', 'ASN', 'CZ', 'TYR', 7.97), ('CB', 'ASN', 'OH', 'TYR', 8.03)], [('CG', 'ASN', 'CB', 'TYR', 8.8), ('CG', 'ASN', 'CG', 'TYR', 7.83), ('CG', 'ASN', 'CD1', 'TYR', 6.72), ('CG', 'ASN', 'CD2', 'TYR', 8.34), ('CG', 'ASN', 'CE1', 'TYR', 6.12), ('CG', 'ASN', 'CE2', 'TYR', 7.94), ('CG', 'ASN', 'CZ', 'TYR', 6.84), ('CG', 'ASN', 'OH', 'TYR', 6.9)], [('OD1', 'ASN', 'CB', 'TYR', 8.28), ('OD1', 'ASN', 'CG', 'TYR', 7.46), ('OD1', 'ASN', 'CD1', 'TYR', 6.23), ('OD1', 'ASN', 'CD2', 'TYR', 8.21), ('OD1', 'ASN', 'CE1', 'TYR', 5.87), ('OD1', 'ASN', 'CE2', 'TYR', 8.0), ('OD1', 'ASN', 'CZ', 'TYR', 6.89), ('OD1', 'ASN', 'OH', 'TYR', 7.17)], [('ND2', 'ASN', 'CB', 'TYR', 8.99), ('ND2', 'ASN', 'CG', 'TYR', 7.8), ('ND2', 'ASN', 'CD1', 'TYR', 6.73), ('ND2', 'ASN', 'CD2', 'TYR', 8.07), ('ND2', 'ASN', 'CE1', 'TYR', 5.79), ('ND2', 'ASN', 'CE2', 'TYR', 7.4), ('ND2', 'ASN', 'CZ', 'TYR', 6.22), ('ND2', 'ASN', 'OH', 'TYR', 5.95)]]}
HIS_TYR = { 
	'distances':
		[[12.78, 11.57, 11.83, 10.35, 10.96, 9.29, 9.67, 8.94], [11.37, 10.13, 10.38, 8.92, 9.5, 7.82, 8.19, 7.5], [10.59, 9.43, 9.85, 8.13, 9.11, 7.13, 7.76, 7.28], [10.72, 9.39, 9.45, 8.3, 8.47, 7.09, 7.23, 6.41], [9.41, 8.19, 8.56, 6.91, 7.81, 5.84, 6.45, 6.05], [9.47, 8.13, 8.25, 7.01, 7.31, 5.77, 6.0, 5.32]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 12.78), ('CB', 'HIS', 'CG', 'TYR', 11.57), ('CB', 'HIS', 'CD1', 'TYR', 11.83), ('CB', 'HIS', 'CD2', 'TYR', 10.35), ('CB', 'HIS', 'CE1', 'TYR', 10.96), ('CB', 'HIS', 'CE2', 'TYR', 9.29), ('CB', 'HIS', 'CZ', 'TYR', 9.67), ('CB', 'HIS', 'OH', 'TYR', 8.94)], [('CG', 'HIS', 'CB', 'TYR', 11.37), ('CG', 'HIS', 'CG', 'TYR', 10.13), ('CG', 'HIS', 'CD1', 'TYR', 10.38), ('CG', 'HIS', 'CD2', 'TYR', 8.92), ('CG', 'HIS', 'CE1', 'TYR', 9.5), ('CG', 'HIS', 'CE2', 'TYR', 7.82), ('CG', 'HIS', 'CZ', 'TYR', 8.19), ('CG', 'HIS', 'OH', 'TYR', 7.5)], [('ND1', 'HIS', 'CB', 'TYR', 10.59), ('ND1', 'HIS', 'CG', 'TYR', 9.43), ('ND1', 'HIS', 'CD1', 'TYR', 9.85), ('ND1', 'HIS', 'CD2', 'TYR', 8.13), ('ND1', 'HIS', 'CE1', 'TYR', 9.11), ('ND1', 'HIS', 'CE2', 'TYR', 7.13), ('ND1', 'HIS', 'CZ', 'TYR', 7.76), ('ND1', 'HIS', 'OH', 'TYR', 7.28)], [('CD2', 'HIS', 'CB', 'TYR', 10.72), ('CD2', 'HIS', 'CG', 'TYR', 9.39), ('CD2', 'HIS', 'CD1', 'TYR', 9.45), ('CD2', 'HIS', 'CD2', 'TYR', 8.3), ('CD2', 'HIS', 'CE1', 'TYR', 8.47), ('CD2', 'HIS', 'CE2', 'TYR', 7.09), ('CD2', 'HIS', 'CZ', 'TYR', 7.23), ('CD2', 'HIS', 'OH', 'TYR', 6.41)], [('CE1', 'HIS', 'CB', 'TYR', 9.41), ('CE1', 'HIS', 'CG', 'TYR', 8.19), ('CE1', 'HIS', 'CD1', 'TYR', 8.56), ('CE1', 'HIS', 'CD2', 'TYR', 6.91), ('CE1', 'HIS', 'CE1', 'TYR', 7.81), ('CE1', 'HIS', 'CE2', 'TYR', 5.84), ('CE1', 'HIS', 'CZ', 'TYR', 6.45), ('CE1', 'HIS', 'OH', 'TYR', 6.05)], [('NE2', 'HIS', 'CB', 'TYR', 9.47), ('NE2', 'HIS', 'CG', 'TYR', 8.13), ('NE2', 'HIS', 'CD1', 'TYR', 8.25), ('NE2', 'HIS', 'CD2', 'TYR', 7.01), ('NE2', 'HIS', 'CE1', 'TYR', 7.31), ('NE2', 'HIS', 'CE2', 'TYR', 5.77), ('NE2', 'HIS', 'CZ', 'TYR', 6.0), ('NE2', 'HIS', 'OH', 'TYR', 5.32)]]}
LYS_TYR = { 
	'distances':
		[[11.99, 10.7, 10.71, 9.7, 9.73, 8.6, 8.63, 7.82], [11.22, 9.87, 9.69, 9.05, 8.64, 7.92, 7.68, 6.82], [9.69, 8.36, 8.26, 7.52, 7.3, 6.43, 6.3, 5.66], [9.06, 7.73, 7.38, 7.2, 6.41, 6.23, 5.74, 5.22], [9.61, 8.2, 7.55, 7.83, 6.35, 6.73, 5.85, 4.97]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 11.99), ('CB', 'LYS', 'CG', 'TYR', 10.7), ('CB', 'LYS', 'CD1', 'TYR', 10.71), ('CB', 'LYS', 'CD2', 'TYR', 9.7), ('CB', 'LYS', 'CE1', 'TYR', 9.73), ('CB', 'LYS', 'CE2', 'TYR', 8.6), ('CB', 'LYS', 'CZ', 'TYR', 8.63), ('CB', 'LYS', 'OH', 'TYR', 7.82)], [('CG', 'LYS', 'CB', 'TYR', 11.22), ('CG', 'LYS', 'CG', 'TYR', 9.87), ('CG', 'LYS', 'CD1', 'TYR', 9.69), ('CG', 'LYS', 'CD2', 'TYR', 9.05), ('CG', 'LYS', 'CE1', 'TYR', 8.64), ('CG', 'LYS', 'CE2', 'TYR', 7.92), ('CG', 'LYS', 'CZ', 'TYR', 7.68), ('CG', 'LYS', 'OH', 'TYR', 6.82)], [('CD', 'LYS', 'CB', 'TYR', 9.69), ('CD', 'LYS', 'CG', 'TYR', 8.36), ('CD', 'LYS', 'CD1', 'TYR', 8.26), ('CD', 'LYS', 'CD2', 'TYR', 7.52), ('CD', 'LYS', 'CE1', 'TYR', 7.3), ('CD', 'LYS', 'CE2', 'TYR', 6.43), ('CD', 'LYS', 'CZ', 'TYR', 6.3), ('CD', 'LYS', 'OH', 'TYR', 5.66)], [('CE', 'LYS', 'CB', 'TYR', 9.06), ('CE', 'LYS', 'CG', 'TYR', 7.73), ('CE', 'LYS', 'CD1', 'TYR', 7.38), ('CE', 'LYS', 'CD2', 'TYR', 7.2), ('CE', 'LYS', 'CE1', 'TYR', 6.41), ('CE', 'LYS', 'CE2', 'TYR', 6.23), ('CE', 'LYS', 'CZ', 'TYR', 5.74), ('CE', 'LYS', 'OH', 'TYR', 5.22)], [('NZ', 'LYS', 'CB', 'TYR', 9.61), ('NZ', 'LYS', 'CG', 'TYR', 8.2), ('NZ', 'LYS', 'CD1', 'TYR', 7.55), ('NZ', 'LYS', 'CD2', 'TYR', 7.83), ('NZ', 'LYS', 'CE1', 'TYR', 6.35), ('NZ', 'LYS', 'CE2', 'TYR', 6.73), ('NZ', 'LYS', 'CZ', 'TYR', 5.85), ('NZ', 'LYS', 'OH', 'TYR', 4.97)]]}
LYS_SER = { 
	'distances':
		[[7.6, 8.19], [6.71, 7.01], [6.48, 6.65], [6.48, 6.17], [5.49, 4.9]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'SER', 7.6), ('CB', 'LYS', 'OG', 'SER', 8.19)], [('CG', 'LYS', 'CB', 'SER', 6.71), ('CG', 'LYS', 'OG', 'SER', 7.01)], [('CD', 'LYS', 'CB', 'SER', 6.48), ('CD', 'LYS', 'OG', 'SER', 6.65)], [('CE', 'LYS', 'CB', 'SER', 6.48), ('CE', 'LYS', 'OG', 'SER', 6.17)], [('NZ', 'LYS', 'CB', 'SER', 5.49), ('NZ', 'LYS', 'OG', 'SER', 4.9)]]}
HIS_ASN = { 
	'distances':
		[[14.54, 13.63, 14.08, 12.49], [13.14, 12.22, 12.65, 11.12], [12.72, 11.9, 12.35, 10.89], [12.16, 11.16, 11.55, 10.04], [11.48, 10.64, 11.05, 9.67], [11.07, 10.1, 10.48, 9.05]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASN', 14.54), ('CB', 'HIS', 'CG', 'ASN', 13.63), ('CB', 'HIS', 'OD1', 'ASN', 14.08), ('CB', 'HIS', 'ND2', 'ASN', 12.49)], [('CG', 'HIS', 'CB', 'ASN', 13.14), ('CG', 'HIS', 'CG', 'ASN', 12.22), ('CG', 'HIS', 'OD1', 'ASN', 12.65), ('CG', 'HIS', 'ND2', 'ASN', 11.12)], [('ND1', 'HIS', 'CB', 'ASN', 12.72), ('ND1', 'HIS', 'CG', 'ASN', 11.9), ('ND1', 'HIS', 'OD1', 'ASN', 12.35), ('ND1', 'HIS', 'ND2', 'ASN', 10.89)], [('CD2', 'HIS', 'CB', 'ASN', 12.16), ('CD2', 'HIS', 'CG', 'ASN', 11.16), ('CD2', 'HIS', 'OD1', 'ASN', 11.55), ('CD2', 'HIS', 'ND2', 'ASN', 10.04)], [('CE1', 'HIS', 'CB', 'ASN', 11.48), ('CE1', 'HIS', 'CG', 'ASN', 10.64), ('CE1', 'HIS', 'OD1', 'ASN', 11.05), ('CE1', 'HIS', 'ND2', 'ASN', 9.67)], [('NE2', 'HIS', 'CB', 'ASN', 11.07), ('NE2', 'HIS', 'CG', 'ASN', 10.1), ('NE2', 'HIS', 'OD1', 'ASN', 10.48), ('NE2', 'HIS', 'ND2', 'ASN', 9.05)]]}
LYS_ASN = { 
	'distances':
		[[10.36, 10.2, 11.18, 9.17], [8.89, 8.7, 9.72, 7.65], [8.27, 7.93, 8.82, 6.97], [6.76, 6.42, 7.34, 5.51], [6.51, 5.92, 6.86, 4.73]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASN', 10.36), ('CB', 'LYS', 'CG', 'ASN', 10.2), ('CB', 'LYS', 'OD1', 'ASN', 11.18), ('CB', 'LYS', 'ND2', 'ASN', 9.17)], [('CG', 'LYS', 'CB', 'ASN', 8.89), ('CG', 'LYS', 'CG', 'ASN', 8.7), ('CG', 'LYS', 'OD1', 'ASN', 9.72), ('CG', 'LYS', 'ND2', 'ASN', 7.65)], [('CD', 'LYS', 'CB', 'ASN', 8.27), ('CD', 'LYS', 'CG', 'ASN', 7.93), ('CD', 'LYS', 'OD1', 'ASN', 8.82), ('CD', 'LYS', 'ND2', 'ASN', 6.97)], [('CE', 'LYS', 'CB', 'ASN', 6.76), ('CE', 'LYS', 'CG', 'ASN', 6.42), ('CE', 'LYS', 'OD1', 'ASN', 7.34), ('CE', 'LYS', 'ND2', 'ASN', 5.51)], [('NZ', 'LYS', 'CB', 'ASN', 6.51), ('NZ', 'LYS', 'CG', 'ASN', 5.92), ('NZ', 'LYS', 'OD1', 'ASN', 6.86), ('NZ', 'LYS', 'ND2', 'ASN', 4.73)]]}
SER_ASN = { 
	'distances':
		[[9.47, 8.4, 8.9, 7.14], [8.28, 7.15, 7.62, 5.91]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 9.47), ('CB', 'SER', 'CG', 'ASN', 8.4), ('CB', 'SER', 'OD1', 'ASN', 8.9), ('CB', 'SER', 'ND2', 'ASN', 7.14)], [('OG', 'SER', 'CB', 'ASN', 8.28), ('OG', 'SER', 'CG', 'ASN', 7.15), ('OG', 'SER', 'OD1', 'ASN', 7.62), ('OG', 'SER', 'ND2', 'ASN', 5.91)]]}
SER_HIS = { 
	'distances':
		[[8.13, 7.06, 7.53, 5.84, 6.82, 5.66], [9.49, 8.33, 8.64, 7.09, 7.74, 6.65]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.13), ('CB', 'SER', 'CG', 'HIS', 7.06), ('CB', 'SER', 'ND1', 'HIS', 7.53), ('CB', 'SER', 'CD2', 'HIS', 5.84), ('CB', 'SER', 'CE1', 'HIS', 6.82), ('CB', 'SER', 'NE2', 'HIS', 5.66)], [('OG', 'SER', 'CB', 'HIS', 9.49), ('OG', 'SER', 'CG', 'HIS', 8.33), ('OG', 'SER', 'ND1', 'HIS', 8.64), ('OG', 'SER', 'CD2', 'HIS', 7.09), ('OG', 'SER', 'CE1', 'HIS', 7.74), ('OG', 'SER', 'NE2', 'HIS', 6.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1ei5_3_4_11_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_HIS, d, 'A_1ei5_3_4_11_19')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_TYR, d, 'A_1ei5_3_4_11_19')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_TYR, d, 'A_1ei5_3_4_11_19')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_TYR, d, 'A_1ei5_3_4_11_19')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_SER, d, 'A_1ei5_3_4_11_19')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_ASN, d, 'A_1ei5_3_4_11_19')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(LYS_ASN, d, 'A_1ei5_3_4_11_19')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ASN, d, 'A_1ei5_3_4_11_19')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_HIS, d, 'A_1ei5_3_4_11_19')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'LYS_HIS' :  match2,
		'ASN_TYR' :  match3,
		'HIS_TYR' :  match4,
		'LYS_TYR' :  match5,
		'LYS_SER' :  match6,
		'HIS_ASN' :  match7,
		'LYS_ASN' :  match8,
		'SER_ASN' :  match9,
		'SER_HIS' :  match10}