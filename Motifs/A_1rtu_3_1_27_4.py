'''
FUNC:A_1rtu_3_1_27_4
PDB:1rtu
EC:3.1.27.4
RESI:his,glu,his
LOCI:a-41,62,101;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[15.49, 14.11, 13.81, 13.05, 12.58, 12.06], [14.96, 13.57, 13.34, 12.44, 12.08, 11.46], [13.75, 12.33, 12.08, 11.21, 10.81, 10.19], [15.63, 14.25, 14.11, 13.05, 12.86, 12.14], [13.76, 12.35, 12.19, 11.16, 10.93, 10.21], [14.92, 13.54, 13.45, 12.31, 12.2, 11.43], [15.49, 14.96, 13.75, 15.63, 13.76, 14.92], [14.11, 13.57, 12.33, 14.25, 12.35, 13.54], [13.81, 13.34, 12.08, 14.11, 12.19, 13.45], [13.05, 12.44, 11.21, 13.05, 11.16, 12.31], [12.58, 12.08, 10.81, 12.86, 10.93, 12.2], [12.06, 11.46, 10.19, 12.14, 10.21, 11.43]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 15.49), ('CB', 'HIS', 'CG', 'HIS', 14.11), ('CB', 'HIS', 'ND1', 'HIS', 13.81), ('CB', 'HIS', 'CD2', 'HIS', 13.05), ('CB', 'HIS', 'CE1', 'HIS', 12.58), ('CB', 'HIS', 'NE2', 'HIS', 12.06)], [('CG', 'HIS', 'CB', 'HIS', 14.96), ('CG', 'HIS', 'CG', 'HIS', 13.57), ('CG', 'HIS', 'ND1', 'HIS', 13.34), ('CG', 'HIS', 'CD2', 'HIS', 12.44), ('CG', 'HIS', 'CE1', 'HIS', 12.08), ('CG', 'HIS', 'NE2', 'HIS', 11.46)], [('ND1', 'HIS', 'CB', 'HIS', 13.75), ('ND1', 'HIS', 'CG', 'HIS', 12.33), ('ND1', 'HIS', 'ND1', 'HIS', 12.08), ('ND1', 'HIS', 'CD2', 'HIS', 11.21), ('ND1', 'HIS', 'CE1', 'HIS', 10.81), ('ND1', 'HIS', 'NE2', 'HIS', 10.19)], [('CD2', 'HIS', 'CB', 'HIS', 15.63), ('CD2', 'HIS', 'CG', 'HIS', 14.25), ('CD2', 'HIS', 'ND1', 'HIS', 14.11), ('CD2', 'HIS', 'CD2', 'HIS', 13.05), ('CD2', 'HIS', 'CE1', 'HIS', 12.86), ('CD2', 'HIS', 'NE2', 'HIS', 12.14)], [('CE1', 'HIS', 'CB', 'HIS', 13.76), ('CE1', 'HIS', 'CG', 'HIS', 12.35), ('CE1', 'HIS', 'ND1', 'HIS', 12.19), ('CE1', 'HIS', 'CD2', 'HIS', 11.16), ('CE1', 'HIS', 'CE1', 'HIS', 10.93), ('CE1', 'HIS', 'NE2', 'HIS', 10.21)], [('NE2', 'HIS', 'CB', 'HIS', 14.92), ('NE2', 'HIS', 'CG', 'HIS', 13.54), ('NE2', 'HIS', 'ND1', 'HIS', 13.45), ('NE2', 'HIS', 'CD2', 'HIS', 12.31), ('NE2', 'HIS', 'CE1', 'HIS', 12.2), ('NE2', 'HIS', 'NE2', 'HIS', 11.43)], [('CB', 'HIS', 'CB', 'HIS', 15.49), ('CB', 'HIS', 'CG', 'HIS', 14.96), ('CB', 'HIS', 'ND1', 'HIS', 13.75), ('CB', 'HIS', 'CD2', 'HIS', 15.63), ('CB', 'HIS', 'CE1', 'HIS', 13.76), ('CB', 'HIS', 'NE2', 'HIS', 14.92)], [('CG', 'HIS', 'CB', 'HIS', 14.11), ('CG', 'HIS', 'CG', 'HIS', 13.57), ('CG', 'HIS', 'ND1', 'HIS', 12.33), ('CG', 'HIS', 'CD2', 'HIS', 14.25), ('CG', 'HIS', 'CE1', 'HIS', 12.35), ('CG', 'HIS', 'NE2', 'HIS', 13.54)], [('ND1', 'HIS', 'CB', 'HIS', 13.81), ('ND1', 'HIS', 'CG', 'HIS', 13.34), ('ND1', 'HIS', 'ND1', 'HIS', 12.08), ('ND1', 'HIS', 'CD2', 'HIS', 14.11), ('ND1', 'HIS', 'CE1', 'HIS', 12.19), ('ND1', 'HIS', 'NE2', 'HIS', 13.45)], [('CD2', 'HIS', 'CB', 'HIS', 13.05), ('CD2', 'HIS', 'CG', 'HIS', 12.44), ('CD2', 'HIS', 'ND1', 'HIS', 11.21), ('CD2', 'HIS', 'CD2', 'HIS', 13.05), ('CD2', 'HIS', 'CE1', 'HIS', 11.16), ('CD2', 'HIS', 'NE2', 'HIS', 12.31)], [('CE1', 'HIS', 'CB', 'HIS', 12.58), ('CE1', 'HIS', 'CG', 'HIS', 12.08), ('CE1', 'HIS', 'ND1', 'HIS', 10.81), ('CE1', 'HIS', 'CD2', 'HIS', 12.86), ('CE1', 'HIS', 'CE1', 'HIS', 10.93), ('CE1', 'HIS', 'NE2', 'HIS', 12.2)], [('NE2', 'HIS', 'CB', 'HIS', 12.06), ('NE2', 'HIS', 'CG', 'HIS', 11.46), ('NE2', 'HIS', 'ND1', 'HIS', 10.19), ('NE2', 'HIS', 'CD2', 'HIS', 12.14), ('NE2', 'HIS', 'CE1', 'HIS', 10.21), ('NE2', 'HIS', 'NE2', 'HIS', 11.43)]]}
GLU_HIS = { 
	'distances':
		[[7.17, 8.0, 8.18, 9.02, 9.27, 9.73], [6.1, 6.77, 6.79, 7.87, 7.89, 8.47], [6.83, 7.19, 6.8, 8.32, 7.8, 8.63], [7.83, 8.31, 7.89, 9.5, 8.93, 9.82], [6.87, 6.88, 6.22, 7.9, 7.04, 7.98], [13.91, 12.85, 12.74, 12.02, 11.87, 11.4], [13.22, 12.04, 11.88, 11.15, 10.9, 10.41], [11.77, 10.58, 10.38, 9.73, 9.42, 8.97], [11.51, 10.39, 10.11, 9.71, 9.25, 8.97], [11.03, 9.78, 9.64, 8.82, 8.62, 8.04]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 7.17), ('CB', 'GLU', 'CG', 'HIS', 8.0), ('CB', 'GLU', 'ND1', 'HIS', 8.18), ('CB', 'GLU', 'CD2', 'HIS', 9.02), ('CB', 'GLU', 'CE1', 'HIS', 9.27), ('CB', 'GLU', 'NE2', 'HIS', 9.73)], [('CG', 'GLU', 'CB', 'HIS', 6.1), ('CG', 'GLU', 'CG', 'HIS', 6.77), ('CG', 'GLU', 'ND1', 'HIS', 6.79), ('CG', 'GLU', 'CD2', 'HIS', 7.87), ('CG', 'GLU', 'CE1', 'HIS', 7.89), ('CG', 'GLU', 'NE2', 'HIS', 8.47)], [('CD', 'GLU', 'CB', 'HIS', 6.83), ('CD', 'GLU', 'CG', 'HIS', 7.19), ('CD', 'GLU', 'ND1', 'HIS', 6.8), ('CD', 'GLU', 'CD2', 'HIS', 8.32), ('CD', 'GLU', 'CE1', 'HIS', 7.8), ('CD', 'GLU', 'NE2', 'HIS', 8.63)], [('OE1', 'GLU', 'CB', 'HIS', 7.83), ('OE1', 'GLU', 'CG', 'HIS', 8.31), ('OE1', 'GLU', 'ND1', 'HIS', 7.89), ('OE1', 'GLU', 'CD2', 'HIS', 9.5), ('OE1', 'GLU', 'CE1', 'HIS', 8.93), ('OE1', 'GLU', 'NE2', 'HIS', 9.82)], [('OE2', 'GLU', 'CB', 'HIS', 6.87), ('OE2', 'GLU', 'CG', 'HIS', 6.88), ('OE2', 'GLU', 'ND1', 'HIS', 6.22), ('OE2', 'GLU', 'CD2', 'HIS', 7.9), ('OE2', 'GLU', 'CE1', 'HIS', 7.04), ('OE2', 'GLU', 'NE2', 'HIS', 7.98)], [('CB', 'GLU', 'CB', 'HIS', 13.91), ('CB', 'GLU', 'CG', 'HIS', 12.85), ('CB', 'GLU', 'ND1', 'HIS', 12.74), ('CB', 'GLU', 'CD2', 'HIS', 12.02), ('CB', 'GLU', 'CE1', 'HIS', 11.87), ('CB', 'GLU', 'NE2', 'HIS', 11.4)], [('CG', 'GLU', 'CB', 'HIS', 13.22), ('CG', 'GLU', 'CG', 'HIS', 12.04), ('CG', 'GLU', 'ND1', 'HIS', 11.88), ('CG', 'GLU', 'CD2', 'HIS', 11.15), ('CG', 'GLU', 'CE1', 'HIS', 10.9), ('CG', 'GLU', 'NE2', 'HIS', 10.41)], [('CD', 'GLU', 'CB', 'HIS', 11.77), ('CD', 'GLU', 'CG', 'HIS', 10.58), ('CD', 'GLU', 'ND1', 'HIS', 10.38), ('CD', 'GLU', 'CD2', 'HIS', 9.73), ('CD', 'GLU', 'CE1', 'HIS', 9.42), ('CD', 'GLU', 'NE2', 'HIS', 8.97)], [('OE1', 'GLU', 'CB', 'HIS', 11.51), ('OE1', 'GLU', 'CG', 'HIS', 10.39), ('OE1', 'GLU', 'ND1', 'HIS', 10.11), ('OE1', 'GLU', 'CD2', 'HIS', 9.71), ('OE1', 'GLU', 'CE1', 'HIS', 9.25), ('OE1', 'GLU', 'NE2', 'HIS', 8.97)], [('OE2', 'GLU', 'CB', 'HIS', 11.03), ('OE2', 'GLU', 'CG', 'HIS', 9.78), ('OE2', 'GLU', 'ND1', 'HIS', 9.64), ('OE2', 'GLU', 'CD2', 'HIS', 8.82), ('OE2', 'GLU', 'CE1', 'HIS', 8.62), ('OE2', 'GLU', 'NE2', 'HIS', 8.04)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'A_1rtu_3_1_27_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_HIS, d, 'A_1rtu_3_1_27_4')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'GLU_HIS' :  match2}