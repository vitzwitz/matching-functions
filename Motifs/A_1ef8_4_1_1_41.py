'''
FUNC:A_1ef8_4_1_1_41
PDB:1ef8
EC:4.1.1.41
RESI:his,gly,tyr
LOCI:a-66,110,140;
'''
import motifFunctions as cmd
HIS_GLY = { 
	'distances':
		[[9.35, 8.52, 7.39, 7.45], [8.45, 7.69, 6.39, 6.52], [8.64, 7.81, 6.35, 6.11], [7.73, 7.2, 5.95, 6.48], [8.07, 7.39, 5.87, 5.78], [7.46, 6.99, 5.59, 6.01], [10.86, 9.82, 9.07, 8.78], [10.35, 9.42, 8.66, 8.62], [8.98, 8.09, 7.26, 7.36], [8.08, 7.07, 6.34, 6.28]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 9.35), ('CB', 'HIS', 'C', 'GLY', 8.52), ('CB', 'HIS', 'CA', 'GLY', 7.39), ('CB', 'HIS', 'N', 'GLY', 7.45)], [('CG', 'HIS', 'O', 'GLY', 8.45), ('CG', 'HIS', 'C', 'GLY', 7.69), ('CG', 'HIS', 'CA', 'GLY', 6.39), ('CG', 'HIS', 'N', 'GLY', 6.52)], [('ND1', 'HIS', 'O', 'GLY', 8.64), ('ND1', 'HIS', 'C', 'GLY', 7.81), ('ND1', 'HIS', 'CA', 'GLY', 6.35), ('ND1', 'HIS', 'N', 'GLY', 6.11)], [('CD2', 'HIS', 'O', 'GLY', 7.73), ('CD2', 'HIS', 'C', 'GLY', 7.2), ('CD2', 'HIS', 'CA', 'GLY', 5.95), ('CD2', 'HIS', 'N', 'GLY', 6.48)], [('CE1', 'HIS', 'O', 'GLY', 8.07), ('CE1', 'HIS', 'C', 'GLY', 7.39), ('CE1', 'HIS', 'CA', 'GLY', 5.87), ('CE1', 'HIS', 'N', 'GLY', 5.78)], [('NE2', 'HIS', 'O', 'GLY', 7.46), ('NE2', 'HIS', 'C', 'GLY', 6.99), ('NE2', 'HIS', 'CA', 'GLY', 5.59), ('NE2', 'HIS', 'N', 'GLY', 6.01)], [('O', 'HIS', 'O', 'GLY', 10.86), ('O', 'HIS', 'C', 'GLY', 9.82), ('O', 'HIS', 'CA', 'GLY', 9.07), ('O', 'HIS', 'N', 'GLY', 8.78)], [('C', 'HIS', 'O', 'GLY', 10.35), ('C', 'HIS', 'C', 'GLY', 9.42), ('C', 'HIS', 'CA', 'GLY', 8.66), ('C', 'HIS', 'N', 'GLY', 8.62)], [('CA', 'HIS', 'O', 'GLY', 8.98), ('CA', 'HIS', 'C', 'GLY', 8.09), ('CA', 'HIS', 'CA', 'GLY', 7.26), ('CA', 'HIS', 'N', 'GLY', 7.36)], [('N', 'HIS', 'O', 'GLY', 8.08), ('N', 'HIS', 'C', 'GLY', 7.07), ('N', 'HIS', 'CA', 'GLY', 6.34), ('N', 'HIS', 'N', 'GLY', 6.28)]]}
GLY_TYR = { 
	'distances':
		[[12.49, 11.0, 10.32, 10.45, 8.95, 9.09, 8.23, 6.87], [12.4, 10.94, 10.1, 10.57, 8.72, 9.27, 8.23, 6.93], [11.21, 9.77, 8.81, 9.57, 7.44, 8.36, 7.16, 5.97], [11.1, 9.75, 8.67, 9.75, 7.4, 8.68, 7.41, 6.45]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TYR', 12.49), ('O', 'GLY', 'CG', 'TYR', 11.0), ('O', 'GLY', 'CD1', 'TYR', 10.32), ('O', 'GLY', 'CD2', 'TYR', 10.45), ('O', 'GLY', 'CE1', 'TYR', 8.95), ('O', 'GLY', 'CE2', 'TYR', 9.09), ('O', 'GLY', 'CZ', 'TYR', 8.23), ('O', 'GLY', 'OH', 'TYR', 6.87)], [('C', 'GLY', 'CB', 'TYR', 12.4), ('C', 'GLY', 'CG', 'TYR', 10.94), ('C', 'GLY', 'CD1', 'TYR', 10.1), ('C', 'GLY', 'CD2', 'TYR', 10.57), ('C', 'GLY', 'CE1', 'TYR', 8.72), ('C', 'GLY', 'CE2', 'TYR', 9.27), ('C', 'GLY', 'CZ', 'TYR', 8.23), ('C', 'GLY', 'OH', 'TYR', 6.93)], [('CA', 'GLY', 'CB', 'TYR', 11.21), ('CA', 'GLY', 'CG', 'TYR', 9.77), ('CA', 'GLY', 'CD1', 'TYR', 8.81), ('CA', 'GLY', 'CD2', 'TYR', 9.57), ('CA', 'GLY', 'CE1', 'TYR', 7.44), ('CA', 'GLY', 'CE2', 'TYR', 8.36), ('CA', 'GLY', 'CZ', 'TYR', 7.16), ('CA', 'GLY', 'OH', 'TYR', 5.97)], [('N', 'GLY', 'CB', 'TYR', 11.1), ('N', 'GLY', 'CG', 'TYR', 9.75), ('N', 'GLY', 'CD1', 'TYR', 8.67), ('N', 'GLY', 'CD2', 'TYR', 9.75), ('N', 'GLY', 'CE1', 'TYR', 7.4), ('N', 'GLY', 'CE2', 'TYR', 8.68), ('N', 'GLY', 'CZ', 'TYR', 7.41), ('N', 'GLY', 'OH', 'TYR', 6.45)]]}
HIS_TYR = { 
	'distances':
		[[12.44, 11.35, 10.09, 11.75, 9.16, 11.01, 9.69, 9.14], [11.07, 9.92, 8.69, 10.28, 7.7, 9.51, 8.2, 7.66], [10.15, 9.06, 7.74, 9.56, 6.83, 8.91, 7.55, 7.22], [10.63, 9.39, 8.3, 9.55, 7.2, 8.68, 7.44, 6.8], [9.05, 7.86, 6.59, 8.27, 5.57, 7.58, 6.22, 5.92], [9.35, 8.06, 6.97, 8.22, 5.83, 7.36, 6.09, 5.54], [15.23, 14.17, 12.83, 14.63, 11.89, 13.85, 12.47, 11.81], [14.85, 13.74, 12.46, 14.13, 11.48, 13.3, 11.96, 11.26], [13.67, 12.49, 11.24, 12.78, 10.18, 11.9, 10.57, 9.81], [13.59, 12.35, 11.1, 12.59, 9.95, 11.63, 10.27, 9.41]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 12.44), ('CB', 'HIS', 'CG', 'TYR', 11.35), ('CB', 'HIS', 'CD1', 'TYR', 10.09), ('CB', 'HIS', 'CD2', 'TYR', 11.75), ('CB', 'HIS', 'CE1', 'TYR', 9.16), ('CB', 'HIS', 'CE2', 'TYR', 11.01), ('CB', 'HIS', 'CZ', 'TYR', 9.69), ('CB', 'HIS', 'OH', 'TYR', 9.14)], [('CG', 'HIS', 'CB', 'TYR', 11.07), ('CG', 'HIS', 'CG', 'TYR', 9.92), ('CG', 'HIS', 'CD1', 'TYR', 8.69), ('CG', 'HIS', 'CD2', 'TYR', 10.28), ('CG', 'HIS', 'CE1', 'TYR', 7.7), ('CG', 'HIS', 'CE2', 'TYR', 9.51), ('CG', 'HIS', 'CZ', 'TYR', 8.2), ('CG', 'HIS', 'OH', 'TYR', 7.66)], [('ND1', 'HIS', 'CB', 'TYR', 10.15), ('ND1', 'HIS', 'CG', 'TYR', 9.06), ('ND1', 'HIS', 'CD1', 'TYR', 7.74), ('ND1', 'HIS', 'CD2', 'TYR', 9.56), ('ND1', 'HIS', 'CE1', 'TYR', 6.83), ('ND1', 'HIS', 'CE2', 'TYR', 8.91), ('ND1', 'HIS', 'CZ', 'TYR', 7.55), ('ND1', 'HIS', 'OH', 'TYR', 7.22)], [('CD2', 'HIS', 'CB', 'TYR', 10.63), ('CD2', 'HIS', 'CG', 'TYR', 9.39), ('CD2', 'HIS', 'CD1', 'TYR', 8.3), ('CD2', 'HIS', 'CD2', 'TYR', 9.55), ('CD2', 'HIS', 'CE1', 'TYR', 7.2), ('CD2', 'HIS', 'CE2', 'TYR', 8.68), ('CD2', 'HIS', 'CZ', 'TYR', 7.44), ('CD2', 'HIS', 'OH', 'TYR', 6.8)], [('CE1', 'HIS', 'CB', 'TYR', 9.05), ('CE1', 'HIS', 'CG', 'TYR', 7.86), ('CE1', 'HIS', 'CD1', 'TYR', 6.59), ('CE1', 'HIS', 'CD2', 'TYR', 8.27), ('CE1', 'HIS', 'CE1', 'TYR', 5.57), ('CE1', 'HIS', 'CE2', 'TYR', 7.58), ('CE1', 'HIS', 'CZ', 'TYR', 6.22), ('CE1', 'HIS', 'OH', 'TYR', 5.92)], [('NE2', 'HIS', 'CB', 'TYR', 9.35), ('NE2', 'HIS', 'CG', 'TYR', 8.06), ('NE2', 'HIS', 'CD1', 'TYR', 6.97), ('NE2', 'HIS', 'CD2', 'TYR', 8.22), ('NE2', 'HIS', 'CE1', 'TYR', 5.83), ('NE2', 'HIS', 'CE2', 'TYR', 7.36), ('NE2', 'HIS', 'CZ', 'TYR', 6.09), ('NE2', 'HIS', 'OH', 'TYR', 5.54)], [('O', 'HIS', 'CB', 'TYR', 15.23), ('O', 'HIS', 'CG', 'TYR', 14.17), ('O', 'HIS', 'CD1', 'TYR', 12.83), ('O', 'HIS', 'CD2', 'TYR', 14.63), ('O', 'HIS', 'CE1', 'TYR', 11.89), ('O', 'HIS', 'CE2', 'TYR', 13.85), ('O', 'HIS', 'CZ', 'TYR', 12.47), ('O', 'HIS', 'OH', 'TYR', 11.81)], [('C', 'HIS', 'CB', 'TYR', 14.85), ('C', 'HIS', 'CG', 'TYR', 13.74), ('C', 'HIS', 'CD1', 'TYR', 12.46), ('C', 'HIS', 'CD2', 'TYR', 14.13), ('C', 'HIS', 'CE1', 'TYR', 11.48), ('C', 'HIS', 'CE2', 'TYR', 13.3), ('C', 'HIS', 'CZ', 'TYR', 11.96), ('C', 'HIS', 'OH', 'TYR', 11.26)], [('CA', 'HIS', 'CB', 'TYR', 13.67), ('CA', 'HIS', 'CG', 'TYR', 12.49), ('CA', 'HIS', 'CD1', 'TYR', 11.24), ('CA', 'HIS', 'CD2', 'TYR', 12.78), ('CA', 'HIS', 'CE1', 'TYR', 10.18), ('CA', 'HIS', 'CE2', 'TYR', 11.9), ('CA', 'HIS', 'CZ', 'TYR', 10.57), ('CA', 'HIS', 'OH', 'TYR', 9.81)], [('N', 'HIS', 'CB', 'TYR', 13.59), ('N', 'HIS', 'CG', 'TYR', 12.35), ('N', 'HIS', 'CD1', 'TYR', 11.1), ('N', 'HIS', 'CD2', 'TYR', 12.59), ('N', 'HIS', 'CE1', 'TYR', 9.95), ('N', 'HIS', 'CE2', 'TYR', 11.63), ('N', 'HIS', 'CZ', 'TYR', 10.27), ('N', 'HIS', 'OH', 'TYR', 9.41)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_GLY, d, 'A_1ef8_4_1_1_41')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_TYR, d, 'A_1ef8_4_1_1_41')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_TYR, d, 'A_1ef8_4_1_1_41')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_GLY' :  match1,
		'GLY_TYR' :  match2,
		'HIS_TYR' :  match3}