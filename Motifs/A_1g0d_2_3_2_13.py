'''
FUNC:A_1g0d_2_3_2_13
PDB:1g0d
EC:2.3.2.13
RESI:cys,his,asp,tyr
LOCI:a-272,332,355,515;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[10.41, 9.01, 8.83, 8.3], [9.04, 7.6, 7.39, 6.92], [8.9, 7.4, 6.92, 6.96], [7.95, 6.57, 6.6, 5.73], [7.74, 6.23, 5.72, 5.88], [7.03, 5.55, 5.43, 4.89]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 10.41), ('CB', 'HIS', 'CG', 'ASP', 9.01), ('CB', 'HIS', 'OD1', 'ASP', 8.83), ('CB', 'HIS', 'OD2', 'ASP', 8.3)], [('CG', 'HIS', 'CB', 'ASP', 9.04), ('CG', 'HIS', 'CG', 'ASP', 7.6), ('CG', 'HIS', 'OD1', 'ASP', 7.39), ('CG', 'HIS', 'OD2', 'ASP', 6.92)], [('ND1', 'HIS', 'CB', 'ASP', 8.9), ('ND1', 'HIS', 'CG', 'ASP', 7.4), ('ND1', 'HIS', 'OD1', 'ASP', 6.92), ('ND1', 'HIS', 'OD2', 'ASP', 6.96)], [('CD2', 'HIS', 'CB', 'ASP', 7.95), ('CD2', 'HIS', 'CG', 'ASP', 6.57), ('CD2', 'HIS', 'OD1', 'ASP', 6.6), ('CD2', 'HIS', 'OD2', 'ASP', 5.73)], [('CE1', 'HIS', 'CB', 'ASP', 7.74), ('CE1', 'HIS', 'CG', 'ASP', 6.23), ('CE1', 'HIS', 'OD1', 'ASP', 5.72), ('CE1', 'HIS', 'OD2', 'ASP', 5.88)], [('NE2', 'HIS', 'CB', 'ASP', 7.03), ('NE2', 'HIS', 'CG', 'ASP', 5.55), ('NE2', 'HIS', 'OD1', 'ASP', 5.43), ('NE2', 'HIS', 'OD2', 'ASP', 4.89)]]}
HIS_CYS = { 
	'distances':
		[[7.37, 6.53, 9.66, 9.17, 8.84, 9.67], [6.62, 6.25, 8.84, 8.5, 8.08, 9.04], [5.27, 5.18, 7.66, 7.27, 6.74, 7.7], [7.35, 7.33, 9.32, 9.17, 8.74, 9.79], [5.42, 5.93, 7.49, 7.33, 6.72, 7.77], [6.73, 7.15, 8.56, 8.52, 8.0, 9.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 7.37), ('CB', 'HIS', 'SG', 'CYS', 6.53), ('CB', 'HIS', 'O', 'CYS', 9.66), ('CB', 'HIS', 'C', 'CYS', 9.17), ('CB', 'HIS', 'CA', 'CYS', 8.84), ('CB', 'HIS', 'N', 'CYS', 9.67)], [('CG', 'HIS', 'CB', 'CYS', 6.62), ('CG', 'HIS', 'SG', 'CYS', 6.25), ('CG', 'HIS', 'O', 'CYS', 8.84), ('CG', 'HIS', 'C', 'CYS', 8.5), ('CG', 'HIS', 'CA', 'CYS', 8.08), ('CG', 'HIS', 'N', 'CYS', 9.04)], [('ND1', 'HIS', 'CB', 'CYS', 5.27), ('ND1', 'HIS', 'SG', 'CYS', 5.18), ('ND1', 'HIS', 'O', 'CYS', 7.66), ('ND1', 'HIS', 'C', 'CYS', 7.27), ('ND1', 'HIS', 'CA', 'CYS', 6.74), ('ND1', 'HIS', 'N', 'CYS', 7.7)], [('CD2', 'HIS', 'CB', 'CYS', 7.35), ('CD2', 'HIS', 'SG', 'CYS', 7.33), ('CD2', 'HIS', 'O', 'CYS', 9.32), ('CD2', 'HIS', 'C', 'CYS', 9.17), ('CD2', 'HIS', 'CA', 'CYS', 8.74), ('CD2', 'HIS', 'N', 'CYS', 9.79)], [('CE1', 'HIS', 'CB', 'CYS', 5.42), ('CE1', 'HIS', 'SG', 'CYS', 5.93), ('CE1', 'HIS', 'O', 'CYS', 7.49), ('CE1', 'HIS', 'C', 'CYS', 7.33), ('CE1', 'HIS', 'CA', 'CYS', 6.72), ('CE1', 'HIS', 'N', 'CYS', 7.77)], [('NE2', 'HIS', 'CB', 'CYS', 6.73), ('NE2', 'HIS', 'SG', 'CYS', 7.15), ('NE2', 'HIS', 'O', 'CYS', 8.56), ('NE2', 'HIS', 'C', 'CYS', 8.52), ('NE2', 'HIS', 'CA', 'CYS', 8.0), ('NE2', 'HIS', 'N', 'CYS', 9.08)]]}
ASP_TYR = { 
	'distances':
		[[17.97, 16.67, 16.75, 15.45, 15.66, 14.22, 14.36, 13.34], [16.47, 15.18, 15.27, 13.96, 14.21, 12.73, 12.89, 11.9], [15.82, 14.47, 14.48, 13.3, 13.36, 12.02, 12.08, 11.02], [16.04, 14.8, 14.99, 13.55, 14.0, 12.39, 12.67, 11.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 17.97), ('CB', 'ASP', 'CG', 'TYR', 16.67), ('CB', 'ASP', 'CD1', 'TYR', 16.75), ('CB', 'ASP', 'CD2', 'TYR', 15.45), ('CB', 'ASP', 'CE1', 'TYR', 15.66), ('CB', 'ASP', 'CE2', 'TYR', 14.22), ('CB', 'ASP', 'CZ', 'TYR', 14.36), ('CB', 'ASP', 'OH', 'TYR', 13.34)], [('CG', 'ASP', 'CB', 'TYR', 16.47), ('CG', 'ASP', 'CG', 'TYR', 15.18), ('CG', 'ASP', 'CD1', 'TYR', 15.27), ('CG', 'ASP', 'CD2', 'TYR', 13.96), ('CG', 'ASP', 'CE1', 'TYR', 14.21), ('CG', 'ASP', 'CE2', 'TYR', 12.73), ('CG', 'ASP', 'CZ', 'TYR', 12.89), ('CG', 'ASP', 'OH', 'TYR', 11.9)], [('OD1', 'ASP', 'CB', 'TYR', 15.82), ('OD1', 'ASP', 'CG', 'TYR', 14.47), ('OD1', 'ASP', 'CD1', 'TYR', 14.48), ('OD1', 'ASP', 'CD2', 'TYR', 13.3), ('OD1', 'ASP', 'CE1', 'TYR', 13.36), ('OD1', 'ASP', 'CE2', 'TYR', 12.02), ('OD1', 'ASP', 'CZ', 'TYR', 12.08), ('OD1', 'ASP', 'OH', 'TYR', 11.02)], [('OD2', 'ASP', 'CB', 'TYR', 16.04), ('OD2', 'ASP', 'CG', 'TYR', 14.8), ('OD2', 'ASP', 'CD1', 'TYR', 14.99), ('OD2', 'ASP', 'CD2', 'TYR', 13.55), ('OD2', 'ASP', 'CE1', 'TYR', 14.0), ('OD2', 'ASP', 'CE2', 'TYR', 12.39), ('OD2', 'ASP', 'CZ', 'TYR', 12.67), ('OD2', 'ASP', 'OH', 'TYR', 11.78)]]}
HIS_TYR = { 
	'distances':
		[[10.5, 9.58, 10.27, 8.19, 9.8, 7.52, 8.48, 8.37], [11.39, 10.29, 10.77, 8.95, 10.08, 8.02, 8.72, 8.3], [11.11, 9.87, 10.15, 8.6, 9.29, 7.47, 7.91, 7.28], [12.7, 11.6, 12.04, 10.27, 11.29, 9.31, 9.93, 9.41], [12.27, 10.97, 11.12, 9.76, 10.14, 8.54, 8.8, 7.97], [13.16, 11.94, 12.2, 10.68, 11.3, 9.56, 9.94, 9.2]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 10.5), ('CB', 'HIS', 'CG', 'TYR', 9.58), ('CB', 'HIS', 'CD1', 'TYR', 10.27), ('CB', 'HIS', 'CD2', 'TYR', 8.19), ('CB', 'HIS', 'CE1', 'TYR', 9.8), ('CB', 'HIS', 'CE2', 'TYR', 7.52), ('CB', 'HIS', 'CZ', 'TYR', 8.48), ('CB', 'HIS', 'OH', 'TYR', 8.37)], [('CG', 'HIS', 'CB', 'TYR', 11.39), ('CG', 'HIS', 'CG', 'TYR', 10.29), ('CG', 'HIS', 'CD1', 'TYR', 10.77), ('CG', 'HIS', 'CD2', 'TYR', 8.95), ('CG', 'HIS', 'CE1', 'TYR', 10.08), ('CG', 'HIS', 'CE2', 'TYR', 8.02), ('CG', 'HIS', 'CZ', 'TYR', 8.72), ('CG', 'HIS', 'OH', 'TYR', 8.3)], [('ND1', 'HIS', 'CB', 'TYR', 11.11), ('ND1', 'HIS', 'CG', 'TYR', 9.87), ('ND1', 'HIS', 'CD1', 'TYR', 10.15), ('ND1', 'HIS', 'CD2', 'TYR', 8.6), ('ND1', 'HIS', 'CE1', 'TYR', 9.29), ('ND1', 'HIS', 'CE2', 'TYR', 7.47), ('ND1', 'HIS', 'CZ', 'TYR', 7.91), ('ND1', 'HIS', 'OH', 'TYR', 7.28)], [('CD2', 'HIS', 'CB', 'TYR', 12.7), ('CD2', 'HIS', 'CG', 'TYR', 11.6), ('CD2', 'HIS', 'CD1', 'TYR', 12.04), ('CD2', 'HIS', 'CD2', 'TYR', 10.27), ('CD2', 'HIS', 'CE1', 'TYR', 11.29), ('CD2', 'HIS', 'CE2', 'TYR', 9.31), ('CD2', 'HIS', 'CZ', 'TYR', 9.93), ('CD2', 'HIS', 'OH', 'TYR', 9.41)], [('CE1', 'HIS', 'CB', 'TYR', 12.27), ('CE1', 'HIS', 'CG', 'TYR', 10.97), ('CE1', 'HIS', 'CD1', 'TYR', 11.12), ('CE1', 'HIS', 'CD2', 'TYR', 9.76), ('CE1', 'HIS', 'CE1', 'TYR', 10.14), ('CE1', 'HIS', 'CE2', 'TYR', 8.54), ('CE1', 'HIS', 'CZ', 'TYR', 8.8), ('CE1', 'HIS', 'OH', 'TYR', 7.97)], [('NE2', 'HIS', 'CB', 'TYR', 13.16), ('NE2', 'HIS', 'CG', 'TYR', 11.94), ('NE2', 'HIS', 'CD1', 'TYR', 12.2), ('NE2', 'HIS', 'CD2', 'TYR', 10.68), ('NE2', 'HIS', 'CE1', 'TYR', 11.3), ('NE2', 'HIS', 'CE2', 'TYR', 9.56), ('NE2', 'HIS', 'CZ', 'TYR', 9.94), ('NE2', 'HIS', 'OH', 'TYR', 9.2)]]}
CYS_TYR = { 
	'distances':
		[[10.65, 9.2, 8.94, 8.28, 7.73, 6.86, 6.54, 5.36], [9.26, 7.89, 7.87, 6.86, 6.85, 5.52, 5.55, 4.78], [12.88, 11.51, 11.14, 10.71, 9.93, 9.4, 8.97, 7.84], [11.69, 10.31, 9.92, 9.56, 8.71, 8.25, 7.77, 6.66], [11.25, 9.79, 9.32, 9.07, 8.01, 7.67, 7.05, 5.77], [10.73, 9.26, 8.56, 8.77, 7.18, 7.41, 6.48, 5.16]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TYR', 10.65), ('CB', 'CYS', 'CG', 'TYR', 9.2), ('CB', 'CYS', 'CD1', 'TYR', 8.94), ('CB', 'CYS', 'CD2', 'TYR', 8.28), ('CB', 'CYS', 'CE1', 'TYR', 7.73), ('CB', 'CYS', 'CE2', 'TYR', 6.86), ('CB', 'CYS', 'CZ', 'TYR', 6.54), ('CB', 'CYS', 'OH', 'TYR', 5.36)], [('SG', 'CYS', 'CB', 'TYR', 9.26), ('SG', 'CYS', 'CG', 'TYR', 7.89), ('SG', 'CYS', 'CD1', 'TYR', 7.87), ('SG', 'CYS', 'CD2', 'TYR', 6.86), ('SG', 'CYS', 'CE1', 'TYR', 6.85), ('SG', 'CYS', 'CE2', 'TYR', 5.52), ('SG', 'CYS', 'CZ', 'TYR', 5.55), ('SG', 'CYS', 'OH', 'TYR', 4.78)], [('O', 'CYS', 'CB', 'TYR', 12.88), ('O', 'CYS', 'CG', 'TYR', 11.51), ('O', 'CYS', 'CD1', 'TYR', 11.14), ('O', 'CYS', 'CD2', 'TYR', 10.71), ('O', 'CYS', 'CE1', 'TYR', 9.93), ('O', 'CYS', 'CE2', 'TYR', 9.4), ('O', 'CYS', 'CZ', 'TYR', 8.97), ('O', 'CYS', 'OH', 'TYR', 7.84)], [('C', 'CYS', 'CB', 'TYR', 11.69), ('C', 'CYS', 'CG', 'TYR', 10.31), ('C', 'CYS', 'CD1', 'TYR', 9.92), ('C', 'CYS', 'CD2', 'TYR', 9.56), ('C', 'CYS', 'CE1', 'TYR', 8.71), ('C', 'CYS', 'CE2', 'TYR', 8.25), ('C', 'CYS', 'CZ', 'TYR', 7.77), ('C', 'CYS', 'OH', 'TYR', 6.66)], [('CA', 'CYS', 'CB', 'TYR', 11.25), ('CA', 'CYS', 'CG', 'TYR', 9.79), ('CA', 'CYS', 'CD1', 'TYR', 9.32), ('CA', 'CYS', 'CD2', 'TYR', 9.07), ('CA', 'CYS', 'CE1', 'TYR', 8.01), ('CA', 'CYS', 'CE2', 'TYR', 7.67), ('CA', 'CYS', 'CZ', 'TYR', 7.05), ('CA', 'CYS', 'OH', 'TYR', 5.77)], [('N', 'CYS', 'CB', 'TYR', 10.73), ('N', 'CYS', 'CG', 'TYR', 9.26), ('N', 'CYS', 'CD1', 'TYR', 8.56), ('N', 'CYS', 'CD2', 'TYR', 8.77), ('N', 'CYS', 'CE1', 'TYR', 7.18), ('N', 'CYS', 'CE2', 'TYR', 7.41), ('N', 'CYS', 'CZ', 'TYR', 6.48), ('N', 'CYS', 'OH', 'TYR', 5.16)]]}
CYS_ASP = { 
	'distances':
		[[10.16, 8.79, 7.8, 8.89], [11.15, 9.74, 8.86, 9.67], [10.19, 9.21, 8.0, 9.79], [10.87, 9.74, 8.57, 10.17], [10.73, 9.5, 8.37, 9.81], [11.98, 10.73, 9.63, 11.0]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 10.16), ('CB', 'CYS', 'CG', 'ASP', 8.79), ('CB', 'CYS', 'OD1', 'ASP', 7.8), ('CB', 'CYS', 'OD2', 'ASP', 8.89)], [('SG', 'CYS', 'CB', 'ASP', 11.15), ('SG', 'CYS', 'CG', 'ASP', 9.74), ('SG', 'CYS', 'OD1', 'ASP', 8.86), ('SG', 'CYS', 'OD2', 'ASP', 9.67)], [('O', 'CYS', 'CB', 'ASP', 10.19), ('O', 'CYS', 'CG', 'ASP', 9.21), ('O', 'CYS', 'OD1', 'ASP', 8.0), ('O', 'CYS', 'OD2', 'ASP', 9.79)], [('C', 'CYS', 'CB', 'ASP', 10.87), ('C', 'CYS', 'CG', 'ASP', 9.74), ('C', 'CYS', 'OD1', 'ASP', 8.57), ('C', 'CYS', 'OD2', 'ASP', 10.17)], [('CA', 'CYS', 'CB', 'ASP', 10.73), ('CA', 'CYS', 'CG', 'ASP', 9.5), ('CA', 'CYS', 'OD1', 'ASP', 8.37), ('CA', 'CYS', 'OD2', 'ASP', 9.81)], [('N', 'CYS', 'CB', 'ASP', 11.98), ('N', 'CYS', 'CG', 'ASP', 10.73), ('N', 'CYS', 'OD1', 'ASP', 9.63), ('N', 'CYS', 'OD2', 'ASP', 11.0)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1g0d_2_3_2_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CYS, d, 'A_1g0d_2_3_2_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TYR, d, 'A_1g0d_2_3_2_13')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_TYR, d, 'A_1g0d_2_3_2_13')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_TYR, d, 'A_1g0d_2_3_2_13')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_ASP, d, 'A_1g0d_2_3_2_13')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'HIS_CYS' :  match2,
		'ASP_TYR' :  match3,
		'HIS_TYR' :  match4,
		'CYS_TYR' :  match5,
		'CYS_ASP' :  match6}