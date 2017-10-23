'''
FUNC:P_1h1y_5_1_3_1
PDB:1h1y
EC:5.1.3.1
RESI:his,asp,his,asp
LOCI:a-36,38,69,178;
'''
import motifFunctions as cmd
ASP_HISI = { 
	'distances':
		[[7.33, 6.84, 5.72, 7.59, 5.93, 7.08], [7.06, 6.68, 5.5, 7.58, 5.87, 7.13], [8.09, 7.79, 6.62, 8.74, 7.01, 8.3], [5.99, 5.63, 4.45, 6.59, 4.93, 6.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HISI', 7.33), ('CB', 'ASP', 'CG', 'HISI', 6.84), ('CB', 'ASP', 'ND1', 'HISI', 5.72), ('CB', 'ASP', 'CD2', 'HISI', 7.59), ('CB', 'ASP', 'CE1', 'HISI', 5.93), ('CB', 'ASP', 'NE2', 'HISI', 7.08)], [('CG', 'ASP', 'CB', 'HISI', 7.06), ('CG', 'ASP', 'CG', 'HISI', 6.68), ('CG', 'ASP', 'ND1', 'HISI', 5.5), ('CG', 'ASP', 'CD2', 'HISI', 7.58), ('CG', 'ASP', 'CE1', 'HISI', 5.87), ('CG', 'ASP', 'NE2', 'HISI', 7.13)], [('OD1', 'ASP', 'CB', 'HISI', 8.09), ('OD1', 'ASP', 'CG', 'HISI', 7.79), ('OD1', 'ASP', 'ND1', 'HISI', 6.62), ('OD1', 'ASP', 'CD2', 'HISI', 8.74), ('OD1', 'ASP', 'CE1', 'HISI', 7.01), ('OD1', 'ASP', 'NE2', 'HISI', 8.3)], [('OD2', 'ASP', 'CB', 'HISI', 5.99), ('OD2', 'ASP', 'CG', 'HISI', 5.63), ('OD2', 'ASP', 'ND1', 'HISI', 4.45), ('OD2', 'ASP', 'CD2', 'HISI', 6.59), ('OD2', 'ASP', 'CE1', 'HISI', 4.93), ('OD2', 'ASP', 'NE2', 'HISI', 6.21)]]}
ASP_ASP = { 
	'distances':
		[[8.48, 7.28, 7.61, 6.15], [7.03, 5.8, 6.14, 4.7], [6.24, 5.15, 5.71, 3.96], [6.87, 5.53, 5.64, 4.6], [8.48, 7.03, 6.24, 6.87], [7.28, 5.8, 5.15, 5.53], [7.61, 6.14, 5.71, 5.64], [6.15, 4.7, 3.96, 4.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 8.48), ('CB', 'ASP', 'CG', 'ASP', 7.28), ('CB', 'ASP', 'OD1', 'ASP', 7.61), ('CB', 'ASP', 'OD2', 'ASP', 6.15)], [('CG', 'ASP', 'CB', 'ASP', 7.03), ('CG', 'ASP', 'CG', 'ASP', 5.8), ('CG', 'ASP', 'OD1', 'ASP', 6.14), ('CG', 'ASP', 'OD2', 'ASP', 4.7)], [('OD1', 'ASP', 'CB', 'ASP', 6.24), ('OD1', 'ASP', 'CG', 'ASP', 5.15), ('OD1', 'ASP', 'OD1', 'ASP', 5.71), ('OD1', 'ASP', 'OD2', 'ASP', 3.96)], [('OD2', 'ASP', 'CB', 'ASP', 6.87), ('OD2', 'ASP', 'CG', 'ASP', 5.53), ('OD2', 'ASP', 'OD1', 'ASP', 5.64), ('OD2', 'ASP', 'OD2', 'ASP', 4.6)], [('CB', 'ASP', 'CB', 'ASP', 8.48), ('CB', 'ASP', 'CG', 'ASP', 7.03), ('CB', 'ASP', 'OD1', 'ASP', 6.24), ('CB', 'ASP', 'OD2', 'ASP', 6.87)], [('CG', 'ASP', 'CB', 'ASP', 7.28), ('CG', 'ASP', 'CG', 'ASP', 5.8), ('CG', 'ASP', 'OD1', 'ASP', 5.15), ('CG', 'ASP', 'OD2', 'ASP', 5.53)], [('OD1', 'ASP', 'CB', 'ASP', 7.61), ('OD1', 'ASP', 'CG', 'ASP', 6.14), ('OD1', 'ASP', 'OD1', 'ASP', 5.71), ('OD1', 'ASP', 'OD2', 'ASP', 5.64)], [('OD2', 'ASP', 'CB', 'ASP', 6.15), ('OD2', 'ASP', 'CG', 'ASP', 4.7), ('OD2', 'ASP', 'OD1', 'ASP', 3.96), ('OD2', 'ASP', 'OD2', 'ASP', 4.6)]]}
HIS_ASP = { 
	'distances':
		[[6.85, 5.96, 6.14, 5.42], [6.11, 5.11, 5.03, 4.79], [6.83, 5.86, 5.52, 5.77], [4.99, 3.86, 3.71, 3.62], [6.33, 5.34, 4.76, 5.48], [5.18, 4.08, 3.51, 4.21], [7.24, 6.66, 6.89, 6.31], [6.21, 5.68, 6.13, 5.17], [6.13, 5.91, 6.58, 5.42], [5.59, 4.85, 5.35, 4.15], [5.5, 5.33, 6.18, 4.68], [5.12, 4.61, 5.41, 3.79], [5.48, 5.12, 4.27, 6.0], [5.92, 5.46, 4.38, 6.4], [5.66, 4.95, 3.75, 5.82], [6.97, 6.62, 5.52, 7.62], [6.59, 5.92, 4.69, 6.8], [7.32, 6.84, 5.65, 7.81], [7.33, 7.06, 8.09, 5.99], [6.84, 6.68, 7.79, 5.63], [5.72, 5.5, 6.62, 4.45], [7.59, 7.58, 8.74, 6.59], [5.93, 5.87, 7.01, 4.93], [7.08, 7.13, 8.3, 6.21]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.85), ('CB', 'HIS', 'CG', 'ASP', 5.96), ('CB', 'HIS', 'OD1', 'ASP', 6.14), ('CB', 'HIS', 'OD2', 'ASP', 5.42)], [('CG', 'HIS', 'CB', 'ASP', 6.11), ('CG', 'HIS', 'CG', 'ASP', 5.11), ('CG', 'HIS', 'OD1', 'ASP', 5.03), ('CG', 'HIS', 'OD2', 'ASP', 4.79)], [('ND1', 'HIS', 'CB', 'ASP', 6.83), ('ND1', 'HIS', 'CG', 'ASP', 5.86), ('ND1', 'HIS', 'OD1', 'ASP', 5.52), ('ND1', 'HIS', 'OD2', 'ASP', 5.77)], [('CD2', 'HIS', 'CB', 'ASP', 4.99), ('CD2', 'HIS', 'CG', 'ASP', 3.86), ('CD2', 'HIS', 'OD1', 'ASP', 3.71), ('CD2', 'HIS', 'OD2', 'ASP', 3.62)], [('CE1', 'HIS', 'CB', 'ASP', 6.33), ('CE1', 'HIS', 'CG', 'ASP', 5.34), ('CE1', 'HIS', 'OD1', 'ASP', 4.76), ('CE1', 'HIS', 'OD2', 'ASP', 5.48)], [('NE2', 'HIS', 'CB', 'ASP', 5.18), ('NE2', 'HIS', 'CG', 'ASP', 4.08), ('NE2', 'HIS', 'OD1', 'ASP', 3.51), ('NE2', 'HIS', 'OD2', 'ASP', 4.21)], [('CB', 'HIS', 'CB', 'ASP', 7.24), ('CB', 'HIS', 'CG', 'ASP', 6.66), ('CB', 'HIS', 'OD1', 'ASP', 6.89), ('CB', 'HIS', 'OD2', 'ASP', 6.31)], [('CG', 'HIS', 'CB', 'ASP', 6.21), ('CG', 'HIS', 'CG', 'ASP', 5.68), ('CG', 'HIS', 'OD1', 'ASP', 6.13), ('CG', 'HIS', 'OD2', 'ASP', 5.17)], [('ND1', 'HIS', 'CB', 'ASP', 6.13), ('ND1', 'HIS', 'CG', 'ASP', 5.91), ('ND1', 'HIS', 'OD1', 'ASP', 6.58), ('ND1', 'HIS', 'OD2', 'ASP', 5.42)], [('CD2', 'HIS', 'CB', 'ASP', 5.59), ('CD2', 'HIS', 'CG', 'ASP', 4.85), ('CD2', 'HIS', 'OD1', 'ASP', 5.35), ('CD2', 'HIS', 'OD2', 'ASP', 4.15)], [('CE1', 'HIS', 'CB', 'ASP', 5.5), ('CE1', 'HIS', 'CG', 'ASP', 5.33), ('CE1', 'HIS', 'OD1', 'ASP', 6.18), ('CE1', 'HIS', 'OD2', 'ASP', 4.68)], [('NE2', 'HIS', 'CB', 'ASP', 5.12), ('NE2', 'HIS', 'CG', 'ASP', 4.61), ('NE2', 'HIS', 'OD1', 'ASP', 5.41), ('NE2', 'HIS', 'OD2', 'ASP', 3.79)], [('CB', 'HIS', 'CB', 'ASP', 5.48), ('CB', 'HIS', 'CG', 'ASP', 5.12), ('CB', 'HIS', 'OD1', 'ASP', 4.27), ('CB', 'HIS', 'OD2', 'ASP', 6.0)], [('CG', 'HIS', 'CB', 'ASP', 5.92), ('CG', 'HIS', 'CG', 'ASP', 5.46), ('CG', 'HIS', 'OD1', 'ASP', 4.38), ('CG', 'HIS', 'OD2', 'ASP', 6.4)], [('ND1', 'HIS', 'CB', 'ASP', 5.66), ('ND1', 'HIS', 'CG', 'ASP', 4.95), ('ND1', 'HIS', 'OD1', 'ASP', 3.75), ('ND1', 'HIS', 'OD2', 'ASP', 5.82)], [('CD2', 'HIS', 'CB', 'ASP', 6.97), ('CD2', 'HIS', 'CG', 'ASP', 6.62), ('CD2', 'HIS', 'OD1', 'ASP', 5.52), ('CD2', 'HIS', 'OD2', 'ASP', 7.62)], [('CE1', 'HIS', 'CB', 'ASP', 6.59), ('CE1', 'HIS', 'CG', 'ASP', 5.92), ('CE1', 'HIS', 'OD1', 'ASP', 4.69), ('CE1', 'HIS', 'OD2', 'ASP', 6.8)], [('NE2', 'HIS', 'CB', 'ASP', 7.32), ('NE2', 'HIS', 'CG', 'ASP', 6.84), ('NE2', 'HIS', 'OD1', 'ASP', 5.65), ('NE2', 'HIS', 'OD2', 'ASP', 7.81)], [('CB', 'HIS', 'CB', 'ASP', 7.33), ('CB', 'HIS', 'CG', 'ASP', 7.06), ('CB', 'HIS', 'OD1', 'ASP', 8.09), ('CB', 'HIS', 'OD2', 'ASP', 5.99)], [('CG', 'HIS', 'CB', 'ASP', 6.84), ('CG', 'HIS', 'CG', 'ASP', 6.68), ('CG', 'HIS', 'OD1', 'ASP', 7.79), ('CG', 'HIS', 'OD2', 'ASP', 5.63)], [('ND1', 'HIS', 'CB', 'ASP', 5.72), ('ND1', 'HIS', 'CG', 'ASP', 5.5), ('ND1', 'HIS', 'OD1', 'ASP', 6.62), ('ND1', 'HIS', 'OD2', 'ASP', 4.45)], [('CD2', 'HIS', 'CB', 'ASP', 7.59), ('CD2', 'HIS', 'CG', 'ASP', 7.58), ('CD2', 'HIS', 'OD1', 'ASP', 8.74), ('CD2', 'HIS', 'OD2', 'ASP', 6.59)], [('CE1', 'HIS', 'CB', 'ASP', 5.93), ('CE1', 'HIS', 'CG', 'ASP', 5.87), ('CE1', 'HIS', 'OD1', 'ASP', 7.01), ('CE1', 'HIS', 'OD2', 'ASP', 4.93)], [('NE2', 'HIS', 'CB', 'ASP', 7.08), ('NE2', 'HIS', 'CG', 'ASP', 7.13), ('NE2', 'HIS', 'OD1', 'ASP', 8.3), ('NE2', 'HIS', 'OD2', 'ASP', 6.21)]]}
HIS_HIS = { 
	'distances':
		[[6.62, 7.62, 7.54, 8.93, 8.77, 9.54], [5.27, 6.17, 6.06, 7.48, 7.28, 8.05], [4.71, 5.61, 5.65, 6.82, 6.84, 7.46], [4.65, 5.39, 5.1, 6.73, 6.31, 7.18], [3.62, 4.36, 4.36, 5.56, 5.52, 6.15], [3.53, 4.15, 3.88, 5.45, 5.09, 5.91], [6.62, 5.27, 4.71, 4.65, 3.62, 3.53], [7.62, 6.17, 5.61, 5.39, 4.36, 4.15], [7.54, 6.06, 5.65, 5.1, 4.36, 3.88], [8.93, 7.48, 6.82, 6.73, 5.56, 5.45], [8.77, 7.28, 6.84, 6.31, 5.52, 5.09], [9.54, 8.05, 7.46, 7.18, 6.15, 5.91]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 6.62), ('CB', 'HIS', 'CG', 'HIS', 7.62), ('CB', 'HIS', 'ND1', 'HIS', 7.54), ('CB', 'HIS', 'CD2', 'HIS', 8.93), ('CB', 'HIS', 'CE1', 'HIS', 8.77), ('CB', 'HIS', 'NE2', 'HIS', 9.54)], [('CG', 'HIS', 'CB', 'HIS', 5.27), ('CG', 'HIS', 'CG', 'HIS', 6.17), ('CG', 'HIS', 'ND1', 'HIS', 6.06), ('CG', 'HIS', 'CD2', 'HIS', 7.48), ('CG', 'HIS', 'CE1', 'HIS', 7.28), ('CG', 'HIS', 'NE2', 'HIS', 8.05)], [('ND1', 'HIS', 'CB', 'HIS', 4.71), ('ND1', 'HIS', 'CG', 'HIS', 5.61), ('ND1', 'HIS', 'ND1', 'HIS', 5.65), ('ND1', 'HIS', 'CD2', 'HIS', 6.82), ('ND1', 'HIS', 'CE1', 'HIS', 6.84), ('ND1', 'HIS', 'NE2', 'HIS', 7.46)], [('CD2', 'HIS', 'CB', 'HIS', 4.65), ('CD2', 'HIS', 'CG', 'HIS', 5.39), ('CD2', 'HIS', 'ND1', 'HIS', 5.1), ('CD2', 'HIS', 'CD2', 'HIS', 6.73), ('CD2', 'HIS', 'CE1', 'HIS', 6.31), ('CD2', 'HIS', 'NE2', 'HIS', 7.18)], [('CE1', 'HIS', 'CB', 'HIS', 3.62), ('CE1', 'HIS', 'CG', 'HIS', 4.36), ('CE1', 'HIS', 'ND1', 'HIS', 4.36), ('CE1', 'HIS', 'CD2', 'HIS', 5.56), ('CE1', 'HIS', 'CE1', 'HIS', 5.52), ('CE1', 'HIS', 'NE2', 'HIS', 6.15)], [('NE2', 'HIS', 'CB', 'HIS', 3.53), ('NE2', 'HIS', 'CG', 'HIS', 4.15), ('NE2', 'HIS', 'ND1', 'HIS', 3.88), ('NE2', 'HIS', 'CD2', 'HIS', 5.45), ('NE2', 'HIS', 'CE1', 'HIS', 5.09), ('NE2', 'HIS', 'NE2', 'HIS', 5.91)], [('CB', 'HIS', 'CB', 'HIS', 6.62), ('CB', 'HIS', 'CG', 'HIS', 5.27), ('CB', 'HIS', 'ND1', 'HIS', 4.71), ('CB', 'HIS', 'CD2', 'HIS', 4.65), ('CB', 'HIS', 'CE1', 'HIS', 3.62), ('CB', 'HIS', 'NE2', 'HIS', 3.53)], [('CG', 'HIS', 'CB', 'HIS', 7.62), ('CG', 'HIS', 'CG', 'HIS', 6.17), ('CG', 'HIS', 'ND1', 'HIS', 5.61), ('CG', 'HIS', 'CD2', 'HIS', 5.39), ('CG', 'HIS', 'CE1', 'HIS', 4.36), ('CG', 'HIS', 'NE2', 'HIS', 4.15)], [('ND1', 'HIS', 'CB', 'HIS', 7.54), ('ND1', 'HIS', 'CG', 'HIS', 6.06), ('ND1', 'HIS', 'ND1', 'HIS', 5.65), ('ND1', 'HIS', 'CD2', 'HIS', 5.1), ('ND1', 'HIS', 'CE1', 'HIS', 4.36), ('ND1', 'HIS', 'NE2', 'HIS', 3.88)], [('CD2', 'HIS', 'CB', 'HIS', 8.93), ('CD2', 'HIS', 'CG', 'HIS', 7.48), ('CD2', 'HIS', 'ND1', 'HIS', 6.82), ('CD2', 'HIS', 'CD2', 'HIS', 6.73), ('CD2', 'HIS', 'CE1', 'HIS', 5.56), ('CD2', 'HIS', 'NE2', 'HIS', 5.45)], [('CE1', 'HIS', 'CB', 'HIS', 8.77), ('CE1', 'HIS', 'CG', 'HIS', 7.28), ('CE1', 'HIS', 'ND1', 'HIS', 6.84), ('CE1', 'HIS', 'CD2', 'HIS', 6.31), ('CE1', 'HIS', 'CE1', 'HIS', 5.52), ('CE1', 'HIS', 'NE2', 'HIS', 5.09)], [('NE2', 'HIS', 'CB', 'HIS', 9.54), ('NE2', 'HIS', 'CG', 'HIS', 8.05), ('NE2', 'HIS', 'ND1', 'HIS', 7.46), ('NE2', 'HIS', 'CD2', 'HIS', 7.18), ('NE2', 'HIS', 'CE1', 'HIS', 6.15), ('NE2', 'HIS', 'NE2', 'HIS', 5.91)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HISI, d, 'P_1h1y_5_1_3_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'P_1h1y_5_1_3_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'P_1h1y_5_1_3_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_HIS, d, 'P_1h1y_5_1_3_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HISI' :  match1,
		'ASP_ASP' :  match2,
		'HIS_ASP' :  match3,
		'HIS_HIS' :  match4}