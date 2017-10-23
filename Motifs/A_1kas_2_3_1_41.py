'''
FUNC:A_1kas_2_3_1_41
PDB:1kas
EC:2.3.1.41
RESI:cys,his,his,phe
LOCI:a-163,303,340,400;
'''
import motifFunctions as cmd
PHE_HIS = { 
	'distances':
		[[12.8, 11.55, 11.7, 10.25, 10.59, 9.6], [11.56, 10.39, 10.69, 9.06, 9.69, 8.58], [11.71, 10.65, 11.11, 9.29, 10.2, 9.0], [10.41, 9.23, 9.53, 7.94, 8.56, 7.46], [10.78, 9.85, 10.48, 8.51, 9.73, 8.45], [9.31, 8.25, 8.75, 6.93, 7.95, 6.73], [9.53, 8.62, 9.3, 7.28, 8.61, 7.31], [14.8, 13.4, 13.19, 12.23, 11.93, 11.24], [14.62, 13.27, 13.2, 12.03, 11.98, 11.16], [13.27, 11.95, 11.99, 10.68, 10.81, 9.9], [12.38, 11.0, 10.9, 9.78, 9.67, 8.87], [13.35, 11.96, 11.56, 11.02, 10.36, 9.95], [12.78, 11.33, 10.96, 10.32, 9.7, 9.22], [12.78, 11.37, 11.18, 10.23, 9.95, 9.26], [12.49, 11.0, 10.47, 10.08, 9.17, 8.85], [12.5, 11.1, 10.95, 9.91, 9.7, 8.95], [12.2, 10.71, 10.21, 9.75, 8.9, 8.53], [12.21, 10.76, 10.46, 9.66, 9.18, 8.58], [13.52, 12.31, 11.88, 11.62, 10.93, 10.73], [13.47, 12.23, 11.92, 11.4, 10.91, 10.54], [12.58, 11.26, 10.97, 10.35, 9.87, 9.42], [11.29, 9.97, 9.6, 9.15, 8.53, 8.19]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'HIS', 12.8), ('CB', 'PHE', 'CG', 'HIS', 11.55), ('CB', 'PHE', 'ND1', 'HIS', 11.7), ('CB', 'PHE', 'CD2', 'HIS', 10.25), ('CB', 'PHE', 'CE1', 'HIS', 10.59), ('CB', 'PHE', 'NE2', 'HIS', 9.6)], [('CG', 'PHE', 'CB', 'HIS', 11.56), ('CG', 'PHE', 'CG', 'HIS', 10.39), ('CG', 'PHE', 'ND1', 'HIS', 10.69), ('CG', 'PHE', 'CD2', 'HIS', 9.06), ('CG', 'PHE', 'CE1', 'HIS', 9.69), ('CG', 'PHE', 'NE2', 'HIS', 8.58)], [('CD1', 'PHE', 'CB', 'HIS', 11.71), ('CD1', 'PHE', 'CG', 'HIS', 10.65), ('CD1', 'PHE', 'ND1', 'HIS', 11.11), ('CD1', 'PHE', 'CD2', 'HIS', 9.29), ('CD1', 'PHE', 'CE1', 'HIS', 10.2), ('CD1', 'PHE', 'NE2', 'HIS', 9.0)], [('CD2', 'PHE', 'CB', 'HIS', 10.41), ('CD2', 'PHE', 'CG', 'HIS', 9.23), ('CD2', 'PHE', 'ND1', 'HIS', 9.53), ('CD2', 'PHE', 'CD2', 'HIS', 7.94), ('CD2', 'PHE', 'CE1', 'HIS', 8.56), ('CD2', 'PHE', 'NE2', 'HIS', 7.46)], [('CE1', 'PHE', 'CB', 'HIS', 10.78), ('CE1', 'PHE', 'CG', 'HIS', 9.85), ('CE1', 'PHE', 'ND1', 'HIS', 10.48), ('CE1', 'PHE', 'CD2', 'HIS', 8.51), ('CE1', 'PHE', 'CE1', 'HIS', 9.73), ('CE1', 'PHE', 'NE2', 'HIS', 8.45)], [('CE2', 'PHE', 'CB', 'HIS', 9.31), ('CE2', 'PHE', 'CG', 'HIS', 8.25), ('CE2', 'PHE', 'ND1', 'HIS', 8.75), ('CE2', 'PHE', 'CD2', 'HIS', 6.93), ('CE2', 'PHE', 'CE1', 'HIS', 7.95), ('CE2', 'PHE', 'NE2', 'HIS', 6.73)], [('CZ', 'PHE', 'CB', 'HIS', 9.53), ('CZ', 'PHE', 'CG', 'HIS', 8.62), ('CZ', 'PHE', 'ND1', 'HIS', 9.3), ('CZ', 'PHE', 'CD2', 'HIS', 7.28), ('CZ', 'PHE', 'CE1', 'HIS', 8.61), ('CZ', 'PHE', 'NE2', 'HIS', 7.31)], [('O', 'PHE', 'CB', 'HIS', 14.8), ('O', 'PHE', 'CG', 'HIS', 13.4), ('O', 'PHE', 'ND1', 'HIS', 13.19), ('O', 'PHE', 'CD2', 'HIS', 12.23), ('O', 'PHE', 'CE1', 'HIS', 11.93), ('O', 'PHE', 'NE2', 'HIS', 11.24)], [('C', 'PHE', 'CB', 'HIS', 14.62), ('C', 'PHE', 'CG', 'HIS', 13.27), ('C', 'PHE', 'ND1', 'HIS', 13.2), ('C', 'PHE', 'CD2', 'HIS', 12.03), ('C', 'PHE', 'CE1', 'HIS', 11.98), ('C', 'PHE', 'NE2', 'HIS', 11.16)], [('CA', 'PHE', 'CB', 'HIS', 13.27), ('CA', 'PHE', 'CG', 'HIS', 11.95), ('CA', 'PHE', 'ND1', 'HIS', 11.99), ('CA', 'PHE', 'CD2', 'HIS', 10.68), ('CA', 'PHE', 'CE1', 'HIS', 10.81), ('CA', 'PHE', 'NE2', 'HIS', 9.9)], [('N', 'PHE', 'CB', 'HIS', 12.38), ('N', 'PHE', 'CG', 'HIS', 11.0), ('N', 'PHE', 'ND1', 'HIS', 10.9), ('N', 'PHE', 'CD2', 'HIS', 9.78), ('N', 'PHE', 'CE1', 'HIS', 9.67), ('N', 'PHE', 'NE2', 'HIS', 8.87)], [('CB', 'PHE', 'CB', 'HIS', 13.35), ('CB', 'PHE', 'CG', 'HIS', 11.96), ('CB', 'PHE', 'ND1', 'HIS', 11.56), ('CB', 'PHE', 'CD2', 'HIS', 11.02), ('CB', 'PHE', 'CE1', 'HIS', 10.36), ('CB', 'PHE', 'NE2', 'HIS', 9.95)], [('CG', 'PHE', 'CB', 'HIS', 12.78), ('CG', 'PHE', 'CG', 'HIS', 11.33), ('CG', 'PHE', 'ND1', 'HIS', 10.96), ('CG', 'PHE', 'CD2', 'HIS', 10.32), ('CG', 'PHE', 'CE1', 'HIS', 9.7), ('CG', 'PHE', 'NE2', 'HIS', 9.22)], [('CD1', 'PHE', 'CB', 'HIS', 12.78), ('CD1', 'PHE', 'CG', 'HIS', 11.37), ('CD1', 'PHE', 'ND1', 'HIS', 11.18), ('CD1', 'PHE', 'CD2', 'HIS', 10.23), ('CD1', 'PHE', 'CE1', 'HIS', 9.95), ('CD1', 'PHE', 'NE2', 'HIS', 9.26)], [('CD2', 'PHE', 'CB', 'HIS', 12.49), ('CD2', 'PHE', 'CG', 'HIS', 11.0), ('CD2', 'PHE', 'ND1', 'HIS', 10.47), ('CD2', 'PHE', 'CD2', 'HIS', 10.08), ('CD2', 'PHE', 'CE1', 'HIS', 9.17), ('CD2', 'PHE', 'NE2', 'HIS', 8.85)], [('CE1', 'PHE', 'CB', 'HIS', 12.5), ('CE1', 'PHE', 'CG', 'HIS', 11.1), ('CE1', 'PHE', 'ND1', 'HIS', 10.95), ('CE1', 'PHE', 'CD2', 'HIS', 9.91), ('CE1', 'PHE', 'CE1', 'HIS', 9.7), ('CE1', 'PHE', 'NE2', 'HIS', 8.95)], [('CE2', 'PHE', 'CB', 'HIS', 12.2), ('CE2', 'PHE', 'CG', 'HIS', 10.71), ('CE2', 'PHE', 'ND1', 'HIS', 10.21), ('CE2', 'PHE', 'CD2', 'HIS', 9.75), ('CE2', 'PHE', 'CE1', 'HIS', 8.9), ('CE2', 'PHE', 'NE2', 'HIS', 8.53)], [('CZ', 'PHE', 'CB', 'HIS', 12.21), ('CZ', 'PHE', 'CG', 'HIS', 10.76), ('CZ', 'PHE', 'ND1', 'HIS', 10.46), ('CZ', 'PHE', 'CD2', 'HIS', 9.66), ('CZ', 'PHE', 'CE1', 'HIS', 9.18), ('CZ', 'PHE', 'NE2', 'HIS', 8.58)], [('O', 'PHE', 'CB', 'HIS', 13.52), ('O', 'PHE', 'CG', 'HIS', 12.31), ('O', 'PHE', 'ND1', 'HIS', 11.88), ('O', 'PHE', 'CD2', 'HIS', 11.62), ('O', 'PHE', 'CE1', 'HIS', 10.93), ('O', 'PHE', 'NE2', 'HIS', 10.73)], [('C', 'PHE', 'CB', 'HIS', 13.47), ('C', 'PHE', 'CG', 'HIS', 12.23), ('C', 'PHE', 'ND1', 'HIS', 11.92), ('C', 'PHE', 'CD2', 'HIS', 11.4), ('C', 'PHE', 'CE1', 'HIS', 10.91), ('C', 'PHE', 'NE2', 'HIS', 10.54)], [('CA', 'PHE', 'CB', 'HIS', 12.58), ('CA', 'PHE', 'CG', 'HIS', 11.26), ('CA', 'PHE', 'ND1', 'HIS', 10.97), ('CA', 'PHE', 'CD2', 'HIS', 10.35), ('CA', 'PHE', 'CE1', 'HIS', 9.87), ('CA', 'PHE', 'NE2', 'HIS', 9.42)], [('N', 'PHE', 'CB', 'HIS', 11.29), ('N', 'PHE', 'CG', 'HIS', 9.97), ('N', 'PHE', 'ND1', 'HIS', 9.6), ('N', 'PHE', 'CD2', 'HIS', 9.15), ('N', 'PHE', 'CE1', 'HIS', 8.53), ('N', 'PHE', 'NE2', 'HIS', 8.19)]]}
CYS_HIS = { 
	'distances':
		[[9.12, 7.63, 6.99, 6.87, 5.67, 5.53], [8.83, 7.38, 7.18, 6.29, 5.96, 5.21], [9.04, 7.68, 6.62, 7.45, 5.58, 6.19], [9.83, 8.35, 7.54, 7.76, 6.28, 6.41]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 9.12), ('CB', 'CYS', 'CG', 'HIS', 7.63), ('CB', 'CYS', 'ND1', 'HIS', 6.99), ('CB', 'CYS', 'CD2', 'HIS', 6.87), ('CB', 'CYS', 'CE1', 'HIS', 5.67), ('CB', 'CYS', 'NE2', 'HIS', 5.53)], [('SG', 'CYS', 'CB', 'HIS', 8.83), ('SG', 'CYS', 'CG', 'HIS', 7.38), ('SG', 'CYS', 'ND1', 'HIS', 7.18), ('SG', 'CYS', 'CD2', 'HIS', 6.29), ('SG', 'CYS', 'CE1', 'HIS', 5.96), ('SG', 'CYS', 'NE2', 'HIS', 5.21)], [('CB', 'CYS', 'CB', 'HIS', 9.04), ('CB', 'CYS', 'CG', 'HIS', 7.68), ('CB', 'CYS', 'ND1', 'HIS', 6.62), ('CB', 'CYS', 'CD2', 'HIS', 7.45), ('CB', 'CYS', 'CE1', 'HIS', 5.58), ('CB', 'CYS', 'NE2', 'HIS', 6.19)], [('SG', 'CYS', 'CB', 'HIS', 9.83), ('SG', 'CYS', 'CG', 'HIS', 8.35), ('SG', 'CYS', 'ND1', 'HIS', 7.54), ('SG', 'CYS', 'CD2', 'HIS', 7.76), ('SG', 'CYS', 'CE1', 'HIS', 6.28), ('SG', 'CYS', 'NE2', 'HIS', 6.41)]]}
PHE_CYS = { 
	'distances':
		[[8.11, 6.77], [7.74, 6.13], [8.57, 6.91], [6.97, 5.27], [8.72, 6.98], [7.16, 5.37], [8.07, 6.29], [8.57, 8.04], [8.83, 8.02], [7.95, 6.88], [6.62, 5.77]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'CYS', 8.11), ('CB', 'PHE', 'SG', 'CYS', 6.77)], [('CG', 'PHE', 'CB', 'CYS', 7.74), ('CG', 'PHE', 'SG', 'CYS', 6.13)], [('CD1', 'PHE', 'CB', 'CYS', 8.57), ('CD1', 'PHE', 'SG', 'CYS', 6.91)], [('CD2', 'PHE', 'CB', 'CYS', 6.97), ('CD2', 'PHE', 'SG', 'CYS', 5.27)], [('CE1', 'PHE', 'CB', 'CYS', 8.72), ('CE1', 'PHE', 'SG', 'CYS', 6.98)], [('CE2', 'PHE', 'CB', 'CYS', 7.16), ('CE2', 'PHE', 'SG', 'CYS', 5.37)], [('CZ', 'PHE', 'CB', 'CYS', 8.07), ('CZ', 'PHE', 'SG', 'CYS', 6.29)], [('O', 'PHE', 'CB', 'CYS', 8.57), ('O', 'PHE', 'SG', 'CYS', 8.04)], [('C', 'PHE', 'CB', 'CYS', 8.83), ('C', 'PHE', 'SG', 'CYS', 8.02)], [('CA', 'PHE', 'CB', 'CYS', 7.95), ('CA', 'PHE', 'SG', 'CYS', 6.88)], [('N', 'PHE', 'CB', 'CYS', 6.62), ('N', 'PHE', 'SG', 'CYS', 5.77)]]}
HIS_HIS = { 
	'distances':
		[[11.02, 9.99, 9.3, 9.77, 8.65, 8.94], [10.17, 9.01, 8.21, 8.77, 7.42, 7.79], [9.66, 8.55, 7.55, 8.54, 6.88, 7.55], [10.03, 8.72, 7.98, 8.26, 6.98, 7.15], [9.21, 7.97, 6.88, 7.9, 6.04, 6.76], [9.43, 8.07, 7.16, 7.7, 6.08, 6.46], [11.02, 10.17, 9.66, 10.03, 9.21, 9.43], [9.99, 9.01, 8.55, 8.72, 7.97, 8.07], [9.3, 8.21, 7.55, 7.98, 6.88, 7.16], [9.77, 8.77, 8.54, 8.26, 7.9, 7.7], [8.65, 7.42, 6.88, 6.98, 6.04, 6.08], [8.94, 7.79, 7.55, 7.15, 6.76, 6.46]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 11.02), ('CB', 'HIS', 'CG', 'HIS', 9.99), ('CB', 'HIS', 'ND1', 'HIS', 9.3), ('CB', 'HIS', 'CD2', 'HIS', 9.77), ('CB', 'HIS', 'CE1', 'HIS', 8.65), ('CB', 'HIS', 'NE2', 'HIS', 8.94)], [('CG', 'HIS', 'CB', 'HIS', 10.17), ('CG', 'HIS', 'CG', 'HIS', 9.01), ('CG', 'HIS', 'ND1', 'HIS', 8.21), ('CG', 'HIS', 'CD2', 'HIS', 8.77), ('CG', 'HIS', 'CE1', 'HIS', 7.42), ('CG', 'HIS', 'NE2', 'HIS', 7.79)], [('ND1', 'HIS', 'CB', 'HIS', 9.66), ('ND1', 'HIS', 'CG', 'HIS', 8.55), ('ND1', 'HIS', 'ND1', 'HIS', 7.55), ('ND1', 'HIS', 'CD2', 'HIS', 8.54), ('ND1', 'HIS', 'CE1', 'HIS', 6.88), ('ND1', 'HIS', 'NE2', 'HIS', 7.55)], [('CD2', 'HIS', 'CB', 'HIS', 10.03), ('CD2', 'HIS', 'CG', 'HIS', 8.72), ('CD2', 'HIS', 'ND1', 'HIS', 7.98), ('CD2', 'HIS', 'CD2', 'HIS', 8.26), ('CD2', 'HIS', 'CE1', 'HIS', 6.98), ('CD2', 'HIS', 'NE2', 'HIS', 7.15)], [('CE1', 'HIS', 'CB', 'HIS', 9.21), ('CE1', 'HIS', 'CG', 'HIS', 7.97), ('CE1', 'HIS', 'ND1', 'HIS', 6.88), ('CE1', 'HIS', 'CD2', 'HIS', 7.9), ('CE1', 'HIS', 'CE1', 'HIS', 6.04), ('CE1', 'HIS', 'NE2', 'HIS', 6.76)], [('NE2', 'HIS', 'CB', 'HIS', 9.43), ('NE2', 'HIS', 'CG', 'HIS', 8.07), ('NE2', 'HIS', 'ND1', 'HIS', 7.16), ('NE2', 'HIS', 'CD2', 'HIS', 7.7), ('NE2', 'HIS', 'CE1', 'HIS', 6.08), ('NE2', 'HIS', 'NE2', 'HIS', 6.46)], [('CB', 'HIS', 'CB', 'HIS', 11.02), ('CB', 'HIS', 'CG', 'HIS', 10.17), ('CB', 'HIS', 'ND1', 'HIS', 9.66), ('CB', 'HIS', 'CD2', 'HIS', 10.03), ('CB', 'HIS', 'CE1', 'HIS', 9.21), ('CB', 'HIS', 'NE2', 'HIS', 9.43)], [('CG', 'HIS', 'CB', 'HIS', 9.99), ('CG', 'HIS', 'CG', 'HIS', 9.01), ('CG', 'HIS', 'ND1', 'HIS', 8.55), ('CG', 'HIS', 'CD2', 'HIS', 8.72), ('CG', 'HIS', 'CE1', 'HIS', 7.97), ('CG', 'HIS', 'NE2', 'HIS', 8.07)], [('ND1', 'HIS', 'CB', 'HIS', 9.3), ('ND1', 'HIS', 'CG', 'HIS', 8.21), ('ND1', 'HIS', 'ND1', 'HIS', 7.55), ('ND1', 'HIS', 'CD2', 'HIS', 7.98), ('ND1', 'HIS', 'CE1', 'HIS', 6.88), ('ND1', 'HIS', 'NE2', 'HIS', 7.16)], [('CD2', 'HIS', 'CB', 'HIS', 9.77), ('CD2', 'HIS', 'CG', 'HIS', 8.77), ('CD2', 'HIS', 'ND1', 'HIS', 8.54), ('CD2', 'HIS', 'CD2', 'HIS', 8.26), ('CD2', 'HIS', 'CE1', 'HIS', 7.9), ('CD2', 'HIS', 'NE2', 'HIS', 7.7)], [('CE1', 'HIS', 'CB', 'HIS', 8.65), ('CE1', 'HIS', 'CG', 'HIS', 7.42), ('CE1', 'HIS', 'ND1', 'HIS', 6.88), ('CE1', 'HIS', 'CD2', 'HIS', 6.98), ('CE1', 'HIS', 'CE1', 'HIS', 6.04), ('CE1', 'HIS', 'NE2', 'HIS', 6.08)], [('NE2', 'HIS', 'CB', 'HIS', 8.94), ('NE2', 'HIS', 'CG', 'HIS', 7.79), ('NE2', 'HIS', 'ND1', 'HIS', 7.55), ('NE2', 'HIS', 'CD2', 'HIS', 7.15), ('NE2', 'HIS', 'CE1', 'HIS', 6.76), ('NE2', 'HIS', 'NE2', 'HIS', 6.46)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(PHE_HIS, d, 'A_1kas_2_3_1_41')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_HIS, d, 'A_1kas_2_3_1_41')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_CYS, d, 'A_1kas_2_3_1_41')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_HIS, d, 'A_1kas_2_3_1_41')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'PHE_HIS' :  match1,
		'CYS_HIS' :  match2,
		'PHE_CYS' :  match3,
		'HIS_HIS' :  match4}