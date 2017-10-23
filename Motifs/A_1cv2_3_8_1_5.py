'''
FUNC:A_1cv2_3_8_1_5
PDB:1cv2
EC:3.8.1.5
RESI:asp,trp,glu,his
LOCI:a-108,109,132,272;
'''
import motifFunctions as cmd
TRP_GLU = { 
	'distances':
		[[12.81, 14.24, 14.48, 13.76, 15.43], [13.0, 14.37, 14.42, 13.61, 15.33], [12.87, 14.15, 14.11, 13.2, 15.05], [13.64, 14.99, 14.94, 14.14, 15.75], [13.42, 14.64, 14.44, 13.48, 15.29], [13.89, 15.15, 14.94, 14.05, 15.73], [14.24, 15.63, 15.59, 14.87, 16.34], [14.68, 15.9, 15.58, 14.69, 16.27], [15.0, 16.33, 16.18, 15.45, 16.85], [15.2, 16.46, 16.17, 15.36, 16.81]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'GLU', 12.81), ('CB', 'TRP', 'CG', 'GLU', 14.24), ('CB', 'TRP', 'CD', 'GLU', 14.48), ('CB', 'TRP', 'OE1', 'GLU', 13.76), ('CB', 'TRP', 'OE2', 'GLU', 15.43)], [('CG', 'TRP', 'CB', 'GLU', 13.0), ('CG', 'TRP', 'CG', 'GLU', 14.37), ('CG', 'TRP', 'CD', 'GLU', 14.42), ('CG', 'TRP', 'OE1', 'GLU', 13.61), ('CG', 'TRP', 'OE2', 'GLU', 15.33)], [('CD1', 'TRP', 'CB', 'GLU', 12.87), ('CD1', 'TRP', 'CG', 'GLU', 14.15), ('CD1', 'TRP', 'CD', 'GLU', 14.11), ('CD1', 'TRP', 'OE1', 'GLU', 13.2), ('CD1', 'TRP', 'OE2', 'GLU', 15.05)], [('CD2', 'TRP', 'CB', 'GLU', 13.64), ('CD2', 'TRP', 'CG', 'GLU', 14.99), ('CD2', 'TRP', 'CD', 'GLU', 14.94), ('CD2', 'TRP', 'OE1', 'GLU', 14.14), ('CD2', 'TRP', 'OE2', 'GLU', 15.75)], [('NE1', 'TRP', 'CB', 'GLU', 13.42), ('NE1', 'TRP', 'CG', 'GLU', 14.64), ('NE1', 'TRP', 'CD', 'GLU', 14.44), ('NE1', 'TRP', 'OE1', 'GLU', 13.48), ('NE1', 'TRP', 'OE2', 'GLU', 15.29)], [('CE2', 'TRP', 'CB', 'GLU', 13.89), ('CE2', 'TRP', 'CG', 'GLU', 15.15), ('CE2', 'TRP', 'CD', 'GLU', 14.94), ('CE2', 'TRP', 'OE1', 'GLU', 14.05), ('CE2', 'TRP', 'OE2', 'GLU', 15.73)], [('CE3', 'TRP', 'CB', 'GLU', 14.24), ('CE3', 'TRP', 'CG', 'GLU', 15.63), ('CE3', 'TRP', 'CD', 'GLU', 15.59), ('CE3', 'TRP', 'OE1', 'GLU', 14.87), ('CE3', 'TRP', 'OE2', 'GLU', 16.34)], [('CZ2', 'TRP', 'CB', 'GLU', 14.68), ('CZ2', 'TRP', 'CG', 'GLU', 15.9), ('CZ2', 'TRP', 'CD', 'GLU', 15.58), ('CZ2', 'TRP', 'OE1', 'GLU', 14.69), ('CZ2', 'TRP', 'OE2', 'GLU', 16.27)], [('CZ3', 'TRP', 'CB', 'GLU', 15.0), ('CZ3', 'TRP', 'CG', 'GLU', 16.33), ('CZ3', 'TRP', 'CD', 'GLU', 16.18), ('CZ3', 'TRP', 'OE1', 'GLU', 15.45), ('CZ3', 'TRP', 'OE2', 'GLU', 16.85)], [('CH2', 'TRP', 'CB', 'GLU', 15.2), ('CH2', 'TRP', 'CG', 'GLU', 16.46), ('CH2', 'TRP', 'CD', 'GLU', 16.17), ('CH2', 'TRP', 'OE1', 'GLU', 15.36), ('CH2', 'TRP', 'OE2', 'GLU', 16.81)]]}
TRP_ASP = { 
	'distances':
		[[6.96, 6.63, 7.46, 5.79], [7.34, 6.63, 7.17, 5.84], [7.27, 6.23, 6.55, 5.37], [8.36, 7.67, 8.02, 7.05], [8.23, 7.08, 7.11, 6.42], [8.84, 7.89, 7.98, 7.33], [9.2, 8.72, 9.11, 8.19], [10.01, 9.07, 9.01, 8.62], [10.3, 9.75, 9.97, 9.31], [10.65, 9.9, 9.93, 9.48]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'ASP', 6.96), ('CB', 'TRP', 'CG', 'ASP', 6.63), ('CB', 'TRP', 'OD1', 'ASP', 7.46), ('CB', 'TRP', 'OD2', 'ASP', 5.79)], [('CG', 'TRP', 'CB', 'ASP', 7.34), ('CG', 'TRP', 'CG', 'ASP', 6.63), ('CG', 'TRP', 'OD1', 'ASP', 7.17), ('CG', 'TRP', 'OD2', 'ASP', 5.84)], [('CD1', 'TRP', 'CB', 'ASP', 7.27), ('CD1', 'TRP', 'CG', 'ASP', 6.23), ('CD1', 'TRP', 'OD1', 'ASP', 6.55), ('CD1', 'TRP', 'OD2', 'ASP', 5.37)], [('CD2', 'TRP', 'CB', 'ASP', 8.36), ('CD2', 'TRP', 'CG', 'ASP', 7.67), ('CD2', 'TRP', 'OD1', 'ASP', 8.02), ('CD2', 'TRP', 'OD2', 'ASP', 7.05)], [('NE1', 'TRP', 'CB', 'ASP', 8.23), ('NE1', 'TRP', 'CG', 'ASP', 7.08), ('NE1', 'TRP', 'OD1', 'ASP', 7.11), ('NE1', 'TRP', 'OD2', 'ASP', 6.42)], [('CE2', 'TRP', 'CB', 'ASP', 8.84), ('CE2', 'TRP', 'CG', 'ASP', 7.89), ('CE2', 'TRP', 'OD1', 'ASP', 7.98), ('CE2', 'TRP', 'OD2', 'ASP', 7.33)], [('CE3', 'TRP', 'CB', 'ASP', 9.2), ('CE3', 'TRP', 'CG', 'ASP', 8.72), ('CE3', 'TRP', 'OD1', 'ASP', 9.11), ('CE3', 'TRP', 'OD2', 'ASP', 8.19)], [('CZ2', 'TRP', 'CB', 'ASP', 10.01), ('CZ2', 'TRP', 'CG', 'ASP', 9.07), ('CZ2', 'TRP', 'OD1', 'ASP', 9.01), ('CZ2', 'TRP', 'OD2', 'ASP', 8.62)], [('CZ3', 'TRP', 'CB', 'ASP', 10.3), ('CZ3', 'TRP', 'CG', 'ASP', 9.75), ('CZ3', 'TRP', 'OD1', 'ASP', 9.97), ('CZ3', 'TRP', 'OD2', 'ASP', 9.31)], [('CH2', 'TRP', 'CB', 'ASP', 10.65), ('CH2', 'TRP', 'CG', 'ASP', 9.9), ('CH2', 'TRP', 'OD1', 'ASP', 9.93), ('CH2', 'TRP', 'OD2', 'ASP', 9.48)]]}
ASP_HIS = { 
	'distances':
		[[9.23, 7.75, 7.3, 6.86, 6.0, 5.61], [9.13, 7.66, 7.32, 6.66, 6.03, 5.46], [8.45, 6.99, 6.59, 6.13, 5.37, 4.94], [10.1, 8.66, 8.46, 7.55, 7.21, 6.49]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 9.23), ('CB', 'ASP', 'CG', 'HIS', 7.75), ('CB', 'ASP', 'ND1', 'HIS', 7.3), ('CB', 'ASP', 'CD2', 'HIS', 6.86), ('CB', 'ASP', 'CE1', 'HIS', 6.0), ('CB', 'ASP', 'NE2', 'HIS', 5.61)], [('CG', 'ASP', 'CB', 'HIS', 9.13), ('CG', 'ASP', 'CG', 'HIS', 7.66), ('CG', 'ASP', 'ND1', 'HIS', 7.32), ('CG', 'ASP', 'CD2', 'HIS', 6.66), ('CG', 'ASP', 'CE1', 'HIS', 6.03), ('CG', 'ASP', 'NE2', 'HIS', 5.46)], [('OD1', 'ASP', 'CB', 'HIS', 8.45), ('OD1', 'ASP', 'CG', 'HIS', 6.99), ('OD1', 'ASP', 'ND1', 'HIS', 6.59), ('OD1', 'ASP', 'CD2', 'HIS', 6.13), ('OD1', 'ASP', 'CE1', 'HIS', 5.37), ('OD1', 'ASP', 'NE2', 'HIS', 4.94)], [('OD2', 'ASP', 'CB', 'HIS', 10.1), ('OD2', 'ASP', 'CG', 'HIS', 8.66), ('OD2', 'ASP', 'ND1', 'HIS', 8.46), ('OD2', 'ASP', 'CD2', 'HIS', 7.55), ('OD2', 'ASP', 'CE1', 'HIS', 7.21), ('OD2', 'ASP', 'NE2', 'HIS', 6.49)]]}
HIS_GLU = { 
	'distances':
		[[7.26, 7.03, 6.82, 5.93, 7.82], [6.61, 6.82, 6.72, 5.72, 7.84], [5.67, 6.05, 5.81, 4.74, 6.93], [7.23, 7.74, 7.81, 6.84, 8.99], [5.87, 6.68, 6.62, 5.65, 7.75], [6.83, 7.66, 7.76, 6.8, 8.93]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 7.26), ('CB', 'HIS', 'CG', 'GLU', 7.03), ('CB', 'HIS', 'CD', 'GLU', 6.82), ('CB', 'HIS', 'OE1', 'GLU', 5.93), ('CB', 'HIS', 'OE2', 'GLU', 7.82)], [('CG', 'HIS', 'CB', 'GLU', 6.61), ('CG', 'HIS', 'CG', 'GLU', 6.82), ('CG', 'HIS', 'CD', 'GLU', 6.72), ('CG', 'HIS', 'OE1', 'GLU', 5.72), ('CG', 'HIS', 'OE2', 'GLU', 7.84)], [('ND1', 'HIS', 'CB', 'GLU', 5.67), ('ND1', 'HIS', 'CG', 'GLU', 6.05), ('ND1', 'HIS', 'CD', 'GLU', 5.81), ('ND1', 'HIS', 'OE1', 'GLU', 4.74), ('ND1', 'HIS', 'OE2', 'GLU', 6.93)], [('CD2', 'HIS', 'CB', 'GLU', 7.23), ('CD2', 'HIS', 'CG', 'GLU', 7.74), ('CD2', 'HIS', 'CD', 'GLU', 7.81), ('CD2', 'HIS', 'OE1', 'GLU', 6.84), ('CD2', 'HIS', 'OE2', 'GLU', 8.99)], [('CE1', 'HIS', 'CB', 'GLU', 5.87), ('CE1', 'HIS', 'CG', 'GLU', 6.68), ('CE1', 'HIS', 'CD', 'GLU', 6.62), ('CE1', 'HIS', 'OE1', 'GLU', 5.65), ('CE1', 'HIS', 'OE2', 'GLU', 7.75)], [('NE2', 'HIS', 'CB', 'GLU', 6.83), ('NE2', 'HIS', 'CG', 'GLU', 7.66), ('NE2', 'HIS', 'CD', 'GLU', 7.76), ('NE2', 'HIS', 'OE1', 'GLU', 6.8), ('NE2', 'HIS', 'OE2', 'GLU', 8.93)]]}
ASP_GLU = { 
	'distances':
		[[8.12, 9.5, 9.91, 9.25, 11.0], [8.94, 10.2, 10.37, 9.53, 11.45], [8.68, 9.82, 9.78, 8.82, 10.81], [10.15, 11.42, 11.62, 10.76, 12.7]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 8.12), ('CB', 'ASP', 'CG', 'GLU', 9.5), ('CB', 'ASP', 'CD', 'GLU', 9.91), ('CB', 'ASP', 'OE1', 'GLU', 9.25), ('CB', 'ASP', 'OE2', 'GLU', 11.0)], [('CG', 'ASP', 'CB', 'GLU', 8.94), ('CG', 'ASP', 'CG', 'GLU', 10.2), ('CG', 'ASP', 'CD', 'GLU', 10.37), ('CG', 'ASP', 'OE1', 'GLU', 9.53), ('CG', 'ASP', 'OE2', 'GLU', 11.45)], [('OD1', 'ASP', 'CB', 'GLU', 8.68), ('OD1', 'ASP', 'CG', 'GLU', 9.82), ('OD1', 'ASP', 'CD', 'GLU', 9.78), ('OD1', 'ASP', 'OE1', 'GLU', 8.82), ('OD1', 'ASP', 'OE2', 'GLU', 10.81)], [('OD2', 'ASP', 'CB', 'GLU', 10.15), ('OD2', 'ASP', 'CG', 'GLU', 11.42), ('OD2', 'ASP', 'CD', 'GLU', 11.62), ('OD2', 'ASP', 'OE1', 'GLU', 10.76), ('OD2', 'ASP', 'OE2', 'GLU', 12.7)]]}
TRP_HIS = { 
	'distances':
		[[13.76, 12.28, 11.85, 11.26, 10.53, 10.08], [13.6, 12.15, 11.69, 11.18, 10.41, 10.01], [12.88, 11.48, 11.13, 10.49, 9.9, 9.42], [14.44, 13.0, 12.42, 12.13, 11.17, 10.93], [13.28, 11.93, 11.53, 11.04, 10.37, 10.0], [14.24, 12.85, 12.31, 12.04, 11.13, 10.91], [15.49, 14.03, 13.36, 13.22, 12.09, 11.96], [15.09, 13.74, 13.13, 13.02, 12.0, 11.9], [16.25, 14.81, 14.08, 14.09, 12.87, 12.84], [16.06, 14.68, 13.97, 14.0, 12.82, 12.8]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'HIS', 13.76), ('CB', 'TRP', 'CG', 'HIS', 12.28), ('CB', 'TRP', 'ND1', 'HIS', 11.85), ('CB', 'TRP', 'CD2', 'HIS', 11.26), ('CB', 'TRP', 'CE1', 'HIS', 10.53), ('CB', 'TRP', 'NE2', 'HIS', 10.08)], [('CG', 'TRP', 'CB', 'HIS', 13.6), ('CG', 'TRP', 'CG', 'HIS', 12.15), ('CG', 'TRP', 'ND1', 'HIS', 11.69), ('CG', 'TRP', 'CD2', 'HIS', 11.18), ('CG', 'TRP', 'CE1', 'HIS', 10.41), ('CG', 'TRP', 'NE2', 'HIS', 10.01)], [('CD1', 'TRP', 'CB', 'HIS', 12.88), ('CD1', 'TRP', 'CG', 'HIS', 11.48), ('CD1', 'TRP', 'ND1', 'HIS', 11.13), ('CD1', 'TRP', 'CD2', 'HIS', 10.49), ('CD1', 'TRP', 'CE1', 'HIS', 9.9), ('CD1', 'TRP', 'NE2', 'HIS', 9.42)], [('CD2', 'TRP', 'CB', 'HIS', 14.44), ('CD2', 'TRP', 'CG', 'HIS', 13.0), ('CD2', 'TRP', 'ND1', 'HIS', 12.42), ('CD2', 'TRP', 'CD2', 'HIS', 12.13), ('CD2', 'TRP', 'CE1', 'HIS', 11.17), ('CD2', 'TRP', 'NE2', 'HIS', 10.93)], [('NE1', 'TRP', 'CB', 'HIS', 13.28), ('NE1', 'TRP', 'CG', 'HIS', 11.93), ('NE1', 'TRP', 'ND1', 'HIS', 11.53), ('NE1', 'TRP', 'CD2', 'HIS', 11.04), ('NE1', 'TRP', 'CE1', 'HIS', 10.37), ('NE1', 'TRP', 'NE2', 'HIS', 10.0)], [('CE2', 'TRP', 'CB', 'HIS', 14.24), ('CE2', 'TRP', 'CG', 'HIS', 12.85), ('CE2', 'TRP', 'ND1', 'HIS', 12.31), ('CE2', 'TRP', 'CD2', 'HIS', 12.04), ('CE2', 'TRP', 'CE1', 'HIS', 11.13), ('CE2', 'TRP', 'NE2', 'HIS', 10.91)], [('CE3', 'TRP', 'CB', 'HIS', 15.49), ('CE3', 'TRP', 'CG', 'HIS', 14.03), ('CE3', 'TRP', 'ND1', 'HIS', 13.36), ('CE3', 'TRP', 'CD2', 'HIS', 13.22), ('CE3', 'TRP', 'CE1', 'HIS', 12.09), ('CE3', 'TRP', 'NE2', 'HIS', 11.96)], [('CZ2', 'TRP', 'CB', 'HIS', 15.09), ('CZ2', 'TRP', 'CG', 'HIS', 13.74), ('CZ2', 'TRP', 'ND1', 'HIS', 13.13), ('CZ2', 'TRP', 'CD2', 'HIS', 13.02), ('CZ2', 'TRP', 'CE1', 'HIS', 12.0), ('CZ2', 'TRP', 'NE2', 'HIS', 11.9)], [('CZ3', 'TRP', 'CB', 'HIS', 16.25), ('CZ3', 'TRP', 'CG', 'HIS', 14.81), ('CZ3', 'TRP', 'ND1', 'HIS', 14.08), ('CZ3', 'TRP', 'CD2', 'HIS', 14.09), ('CZ3', 'TRP', 'CE1', 'HIS', 12.87), ('CZ3', 'TRP', 'NE2', 'HIS', 12.84)], [('CH2', 'TRP', 'CB', 'HIS', 16.06), ('CH2', 'TRP', 'CG', 'HIS', 14.68), ('CH2', 'TRP', 'ND1', 'HIS', 13.97), ('CH2', 'TRP', 'CD2', 'HIS', 14.0), ('CH2', 'TRP', 'CE1', 'HIS', 12.82), ('CH2', 'TRP', 'NE2', 'HIS', 12.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_GLU, d, 'A_1cv2_3_8_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TRP_ASP, d, 'A_1cv2_3_8_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'A_1cv2_3_8_1_5')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_1cv2_3_8_1_5')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLU, d, 'A_1cv2_3_8_1_5')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TRP_HIS, d, 'A_1cv2_3_8_1_5')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_GLU' :  match1,
		'TRP_ASP' :  match2,
		'ASP_HIS' :  match3,
		'HIS_GLU' :  match4,
		'ASP_GLU' :  match5,
		'TRP_HIS' :  match6}