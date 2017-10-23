'''
FUNC:A_1b65_3_4_11_19
PDB:1b65
EC:3.4.11.19
RESI:tyr,asn,ser,ser,gly
LOCI:a-146,218,250,288,289;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[7.82, 9.21, 10.25, 9.6, 11.53, 10.95, 11.8, 13.13, 8.42, 8.69, 7.92, 6.71], [7.35, 8.64, 9.61, 9.05, 10.84, 10.34, 11.13, 12.42, 8.49, 8.73, 7.8, 6.79], [11.54, 12.5, 13.59, 12.39, 14.55, 13.43, 14.45, 15.52, 12.15, 12.8, 12.23, 11.4], [11.39, 12.46, 13.61, 12.38, 14.66, 13.51, 14.57, 15.71, 11.71, 12.37, 11.88, 10.93]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 7.82), ('CB', 'SER', 'CG', 'TYR', 9.21), ('CB', 'SER', 'CD1', 'TYR', 10.25), ('CB', 'SER', 'CD2', 'TYR', 9.6), ('CB', 'SER', 'CE1', 'TYR', 11.53), ('CB', 'SER', 'CE2', 'TYR', 10.95), ('CB', 'SER', 'CZ', 'TYR', 11.8), ('CB', 'SER', 'OH', 'TYR', 13.13), ('CB', 'SER', 'O', 'TYR', 8.42), ('CB', 'SER', 'C', 'TYR', 8.69), ('CB', 'SER', 'CA', 'TYR', 7.92), ('CB', 'SER', 'N', 'TYR', 6.71)], [('OG', 'SER', 'CB', 'TYR', 7.35), ('OG', 'SER', 'CG', 'TYR', 8.64), ('OG', 'SER', 'CD1', 'TYR', 9.61), ('OG', 'SER', 'CD2', 'TYR', 9.05), ('OG', 'SER', 'CE1', 'TYR', 10.84), ('OG', 'SER', 'CE2', 'TYR', 10.34), ('OG', 'SER', 'CZ', 'TYR', 11.13), ('OG', 'SER', 'OH', 'TYR', 12.42), ('OG', 'SER', 'O', 'TYR', 8.49), ('OG', 'SER', 'C', 'TYR', 8.73), ('OG', 'SER', 'CA', 'TYR', 7.8), ('OG', 'SER', 'N', 'TYR', 6.79)], [('CB', 'SER', 'CB', 'TYR', 11.54), ('CB', 'SER', 'CG', 'TYR', 12.5), ('CB', 'SER', 'CD1', 'TYR', 13.59), ('CB', 'SER', 'CD2', 'TYR', 12.39), ('CB', 'SER', 'CE1', 'TYR', 14.55), ('CB', 'SER', 'CE2', 'TYR', 13.43), ('CB', 'SER', 'CZ', 'TYR', 14.45), ('CB', 'SER', 'OH', 'TYR', 15.52), ('CB', 'SER', 'O', 'TYR', 12.15), ('CB', 'SER', 'C', 'TYR', 12.8), ('CB', 'SER', 'CA', 'TYR', 12.23), ('CB', 'SER', 'N', 'TYR', 11.4)], [('OG', 'SER', 'CB', 'TYR', 11.39), ('OG', 'SER', 'CG', 'TYR', 12.46), ('OG', 'SER', 'CD1', 'TYR', 13.61), ('OG', 'SER', 'CD2', 'TYR', 12.38), ('OG', 'SER', 'CE1', 'TYR', 14.66), ('OG', 'SER', 'CE2', 'TYR', 13.51), ('OG', 'SER', 'CZ', 'TYR', 14.57), ('OG', 'SER', 'OH', 'TYR', 15.71), ('OG', 'SER', 'O', 'TYR', 11.71), ('OG', 'SER', 'C', 'TYR', 12.37), ('OG', 'SER', 'CA', 'TYR', 11.88), ('OG', 'SER', 'N', 'TYR', 10.93)]]}
SER_SER = { 
	'distances':
		[[7.24, 6.58], [6.93, 6.66], [7.24, 6.93], [6.58, 6.66]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'SER', 7.24), ('CB', 'SER', 'OG', 'SER', 6.58)], [('OG', 'SER', 'CB', 'SER', 6.93), ('OG', 'SER', 'OG', 'SER', 6.66)], [('CB', 'SER', 'CB', 'SER', 7.24), ('CB', 'SER', 'OG', 'SER', 6.93)], [('OG', 'SER', 'CB', 'SER', 6.58), ('OG', 'SER', 'OG', 'SER', 6.66)]]}
ASN_TYR = { 
	'distances':
		[[8.57, 9.7, 10.93, 9.68, 12.03, 10.91, 11.98, 13.21, 6.97, 7.63, 7.96, 7.07], [7.57, 8.52, 9.78, 8.35, 10.79, 9.52, 10.63, 11.82, 5.63, 6.47, 7.03, 6.46], [8.12, 8.86, 10.1, 8.52, 10.96, 9.54, 10.68, 11.77, 5.72, 6.65, 7.53, 7.22], [6.33, 7.34, 8.62, 7.23, 9.67, 8.48, 9.57, 10.8, 4.85, 5.67, 6.0, 5.47]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'TYR', 8.57), ('CB', 'ASN', 'CG', 'TYR', 9.7), ('CB', 'ASN', 'CD1', 'TYR', 10.93), ('CB', 'ASN', 'CD2', 'TYR', 9.68), ('CB', 'ASN', 'CE1', 'TYR', 12.03), ('CB', 'ASN', 'CE2', 'TYR', 10.91), ('CB', 'ASN', 'CZ', 'TYR', 11.98), ('CB', 'ASN', 'OH', 'TYR', 13.21), ('CB', 'ASN', 'O', 'TYR', 6.97), ('CB', 'ASN', 'C', 'TYR', 7.63), ('CB', 'ASN', 'CA', 'TYR', 7.96), ('CB', 'ASN', 'N', 'TYR', 7.07)], [('CG', 'ASN', 'CB', 'TYR', 7.57), ('CG', 'ASN', 'CG', 'TYR', 8.52), ('CG', 'ASN', 'CD1', 'TYR', 9.78), ('CG', 'ASN', 'CD2', 'TYR', 8.35), ('CG', 'ASN', 'CE1', 'TYR', 10.79), ('CG', 'ASN', 'CE2', 'TYR', 9.52), ('CG', 'ASN', 'CZ', 'TYR', 10.63), ('CG', 'ASN', 'OH', 'TYR', 11.82), ('CG', 'ASN', 'O', 'TYR', 5.63), ('CG', 'ASN', 'C', 'TYR', 6.47), ('CG', 'ASN', 'CA', 'TYR', 7.03), ('CG', 'ASN', 'N', 'TYR', 6.46)], [('OD1', 'ASN', 'CB', 'TYR', 8.12), ('OD1', 'ASN', 'CG', 'TYR', 8.86), ('OD1', 'ASN', 'CD1', 'TYR', 10.1), ('OD1', 'ASN', 'CD2', 'TYR', 8.52), ('OD1', 'ASN', 'CE1', 'TYR', 10.96), ('OD1', 'ASN', 'CE2', 'TYR', 9.54), ('OD1', 'ASN', 'CZ', 'TYR', 10.68), ('OD1', 'ASN', 'OH', 'TYR', 11.77), ('OD1', 'ASN', 'O', 'TYR', 5.72), ('OD1', 'ASN', 'C', 'TYR', 6.65), ('OD1', 'ASN', 'CA', 'TYR', 7.53), ('OD1', 'ASN', 'N', 'TYR', 7.22)], [('ND2', 'ASN', 'CB', 'TYR', 6.33), ('ND2', 'ASN', 'CG', 'TYR', 7.34), ('ND2', 'ASN', 'CD1', 'TYR', 8.62), ('ND2', 'ASN', 'CD2', 'TYR', 7.23), ('ND2', 'ASN', 'CE1', 'TYR', 9.67), ('ND2', 'ASN', 'CE2', 'TYR', 8.48), ('ND2', 'ASN', 'CZ', 'TYR', 9.57), ('ND2', 'ASN', 'OH', 'TYR', 10.8), ('ND2', 'ASN', 'O', 'TYR', 4.85), ('ND2', 'ASN', 'C', 'TYR', 5.67), ('ND2', 'ASN', 'CA', 'TYR', 6.0), ('ND2', 'ASN', 'N', 'TYR', 5.47)]]}
SER_GLY = { 
	'distances':
		[[5.4, 6.09, 6.1, 5.55], [5.72, 6.03, 5.51, 4.78], [7.39, 6.95, 6.79, 5.55], [6.84, 6.7, 6.91, 5.78]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 5.4), ('CB', 'SER', 'C', 'GLY', 6.09), ('CB', 'SER', 'CA', 'GLY', 6.1), ('CB', 'SER', 'N', 'GLY', 5.55)], [('OG', 'SER', 'O', 'GLY', 5.72), ('OG', 'SER', 'C', 'GLY', 6.03), ('OG', 'SER', 'CA', 'GLY', 5.51), ('OG', 'SER', 'N', 'GLY', 4.78)], [('CB', 'SER', 'O', 'GLY', 7.39), ('CB', 'SER', 'C', 'GLY', 6.95), ('CB', 'SER', 'CA', 'GLY', 6.79), ('CB', 'SER', 'N', 'GLY', 5.55)], [('OG', 'SER', 'O', 'GLY', 6.84), ('OG', 'SER', 'C', 'GLY', 6.7), ('OG', 'SER', 'CA', 'GLY', 6.91), ('OG', 'SER', 'N', 'GLY', 5.78)]]}
ASN_SERI = { 
	'distances':
		[[10.18, 9.14], [10.5, 9.64], [11.44, 10.6], [9.96, 9.28]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'SERI', 10.18), ('CB', 'ASN', 'OG', 'SERI', 9.14)], [('CG', 'ASN', 'CB', 'SERI', 10.5), ('CG', 'ASN', 'OG', 'SERI', 9.64)], [('OD1', 'ASN', 'CB', 'SERI', 11.44), ('OD1', 'ASN', 'OG', 'SERI', 10.6)], [('ND2', 'ASN', 'CB', 'SERI', 9.96), ('ND2', 'ASN', 'OG', 'SERI', 9.28)]]}
GLY_TYR = { 
	'distances':
		[[10.73, 12.13, 12.96, 12.69, 14.27, 14.0, 14.71, 16.03, 11.72, 11.84, 10.85, 9.56], [11.17, 12.49, 13.29, 13.02, 14.54, 14.28, 14.96, 16.24, 12.38, 12.51, 11.47, 10.27], [10.41, 11.62, 12.35, 12.16, 13.54, 13.35, 13.97, 15.2, 11.95, 12.05, 10.93, 9.88], [9.83, 10.98, 11.83, 11.33, 12.96, 12.5, 13.24, 14.44, 11.2, 11.46, 10.46, 9.51]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TYR', 10.73), ('O', 'GLY', 'CG', 'TYR', 12.13), ('O', 'GLY', 'CD1', 'TYR', 12.96), ('O', 'GLY', 'CD2', 'TYR', 12.69), ('O', 'GLY', 'CE1', 'TYR', 14.27), ('O', 'GLY', 'CE2', 'TYR', 14.0), ('O', 'GLY', 'CZ', 'TYR', 14.71), ('O', 'GLY', 'OH', 'TYR', 16.03), ('O', 'GLY', 'O', 'TYR', 11.72), ('O', 'GLY', 'C', 'TYR', 11.84), ('O', 'GLY', 'CA', 'TYR', 10.85), ('O', 'GLY', 'N', 'TYR', 9.56)], [('C', 'GLY', 'CB', 'TYR', 11.17), ('C', 'GLY', 'CG', 'TYR', 12.49), ('C', 'GLY', 'CD1', 'TYR', 13.29), ('C', 'GLY', 'CD2', 'TYR', 13.02), ('C', 'GLY', 'CE1', 'TYR', 14.54), ('C', 'GLY', 'CE2', 'TYR', 14.28), ('C', 'GLY', 'CZ', 'TYR', 14.96), ('C', 'GLY', 'OH', 'TYR', 16.24), ('C', 'GLY', 'O', 'TYR', 12.38), ('C', 'GLY', 'C', 'TYR', 12.51), ('C', 'GLY', 'CA', 'TYR', 11.47), ('C', 'GLY', 'N', 'TYR', 10.27)], [('CA', 'GLY', 'CB', 'TYR', 10.41), ('CA', 'GLY', 'CG', 'TYR', 11.62), ('CA', 'GLY', 'CD1', 'TYR', 12.35), ('CA', 'GLY', 'CD2', 'TYR', 12.16), ('CA', 'GLY', 'CE1', 'TYR', 13.54), ('CA', 'GLY', 'CE2', 'TYR', 13.35), ('CA', 'GLY', 'CZ', 'TYR', 13.97), ('CA', 'GLY', 'OH', 'TYR', 15.2), ('CA', 'GLY', 'O', 'TYR', 11.95), ('CA', 'GLY', 'C', 'TYR', 12.05), ('CA', 'GLY', 'CA', 'TYR', 10.93), ('CA', 'GLY', 'N', 'TYR', 9.88)], [('N', 'GLY', 'CB', 'TYR', 9.83), ('N', 'GLY', 'CG', 'TYR', 10.98), ('N', 'GLY', 'CD1', 'TYR', 11.83), ('N', 'GLY', 'CD2', 'TYR', 11.33), ('N', 'GLY', 'CE1', 'TYR', 12.96), ('N', 'GLY', 'CE2', 'TYR', 12.5), ('N', 'GLY', 'CZ', 'TYR', 13.24), ('N', 'GLY', 'OH', 'TYR', 14.44), ('N', 'GLY', 'O', 'TYR', 11.2), ('N', 'GLY', 'C', 'TYR', 11.46), ('N', 'GLY', 'CA', 'TYR', 10.46), ('N', 'GLY', 'N', 'TYR', 9.51)]]}
TYR_SERI = { 
	'distances':
		[[11.54, 11.39], [12.5, 12.46], [13.59, 13.61], [12.39, 12.38], [14.55, 14.66], [13.43, 13.51], [14.45, 14.57], [15.52, 15.71], [12.15, 11.71], [12.8, 12.37], [12.23, 11.88], [11.4, 10.93]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'SERI', 11.54), ('CB', 'TYR', 'OG', 'SERI', 11.39)], [('CG', 'TYR', 'CB', 'SERI', 12.5), ('CG', 'TYR', 'OG', 'SERI', 12.46)], [('CD1', 'TYR', 'CB', 'SERI', 13.59), ('CD1', 'TYR', 'OG', 'SERI', 13.61)], [('CD2', 'TYR', 'CB', 'SERI', 12.39), ('CD2', 'TYR', 'OG', 'SERI', 12.38)], [('CE1', 'TYR', 'CB', 'SERI', 14.55), ('CE1', 'TYR', 'OG', 'SERI', 14.66)], [('CE2', 'TYR', 'CB', 'SERI', 13.43), ('CE2', 'TYR', 'OG', 'SERI', 13.51)], [('CZ', 'TYR', 'CB', 'SERI', 14.45), ('CZ', 'TYR', 'OG', 'SERI', 14.57)], [('OH', 'TYR', 'CB', 'SERI', 15.52), ('OH', 'TYR', 'OG', 'SERI', 15.71)], [('O', 'TYR', 'CB', 'SERI', 12.15), ('O', 'TYR', 'OG', 'SERI', 11.71)], [('C', 'TYR', 'CB', 'SERI', 12.8), ('C', 'TYR', 'OG', 'SERI', 12.37)], [('CA', 'TYR', 'CB', 'SERI', 12.23), ('CA', 'TYR', 'OG', 'SERI', 11.88)], [('N', 'TYR', 'CB', 'SERI', 11.4), ('N', 'TYR', 'OG', 'SERI', 10.93)]]}
GLY_ASN = { 
	'distances':
		[[9.47, 10.23, 11.45, 9.71], [10.41, 11.06, 12.28, 10.45], [10.7, 11.11, 12.31, 10.3], [9.99, 10.29, 11.44, 9.45]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASN', 9.47), ('O', 'GLY', 'CG', 'ASN', 10.23), ('O', 'GLY', 'OD1', 'ASN', 11.45), ('O', 'GLY', 'ND2', 'ASN', 9.71)], [('C', 'GLY', 'CB', 'ASN', 10.41), ('C', 'GLY', 'CG', 'ASN', 11.06), ('C', 'GLY', 'OD1', 'ASN', 12.28), ('C', 'GLY', 'ND2', 'ASN', 10.45)], [('CA', 'GLY', 'CB', 'ASN', 10.7), ('CA', 'GLY', 'CG', 'ASN', 11.11), ('CA', 'GLY', 'OD1', 'ASN', 12.31), ('CA', 'GLY', 'ND2', 'ASN', 10.3)], [('N', 'GLY', 'CB', 'ASN', 9.99), ('N', 'GLY', 'CG', 'ASN', 10.29), ('N', 'GLY', 'OD1', 'ASN', 11.44), ('N', 'GLY', 'ND2', 'ASN', 9.45)]]}
SER_ASN = { 
	'distances':
		[[6.65, 7.06, 8.28, 6.36], [7.71, 7.81, 8.98, 6.86], [10.18, 10.5, 11.44, 9.96], [9.14, 9.64, 10.6, 9.28]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 6.65), ('CB', 'SER', 'CG', 'ASN', 7.06), ('CB', 'SER', 'OD1', 'ASN', 8.28), ('CB', 'SER', 'ND2', 'ASN', 6.36)], [('OG', 'SER', 'CB', 'ASN', 7.71), ('OG', 'SER', 'CG', 'ASN', 7.81), ('OG', 'SER', 'OD1', 'ASN', 8.98), ('OG', 'SER', 'ND2', 'ASN', 6.86)], [('CB', 'SER', 'CB', 'ASN', 10.18), ('CB', 'SER', 'CG', 'ASN', 10.5), ('CB', 'SER', 'OD1', 'ASN', 11.44), ('CB', 'SER', 'ND2', 'ASN', 9.96)], [('OG', 'SER', 'CB', 'ASN', 9.14), ('OG', 'SER', 'CG', 'ASN', 9.64), ('OG', 'SER', 'OD1', 'ASN', 10.6), ('OG', 'SER', 'ND2', 'ASN', 9.28)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1b65_3_4_11_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_SER, d, 'A_1b65_3_4_11_19')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_TYR, d, 'A_1b65_3_4_11_19')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_GLY, d, 'A_1b65_3_4_11_19')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_SERI, d, 'A_1b65_3_4_11_19')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLY_TYR, d, 'A_1b65_3_4_11_19')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(TYR_SERI, d, 'A_1b65_3_4_11_19')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLY_ASN, d, 'A_1b65_3_4_11_19')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ASN, d, 'A_1b65_3_4_11_19')
	if match9 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'SER_SER' :  match2,
		'ASN_TYR' :  match3,
		'SER_GLY' :  match4,
		'ASN_SERI' :  match5,
		'GLY_TYR' :  match6,
		'TYR_SERI' :  match7,
		'GLY_ASN' :  match8,
		'SER_ASN' :  match9}