'''
FUNC:P_1c1h_4_99_1_1
PDB:1c1h
EC:4.99.1.1
RESI:his,his,glu
LOCI:a-183,262,264;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[12.38, 12.11, 13.21, 11.03, 12.94, 11.64], [13.02, 12.83, 13.96, 11.82, 13.74, 12.48], [14.4, 14.21, 15.32, 13.18, 15.08, 13.8], [12.64, 12.54, 13.68, 11.61, 13.54, 12.33], [14.83, 14.7, 15.82, 13.74, 15.63, 14.39], [13.85, 13.78, 14.91, 12.88, 14.78, 13.59], [12.38, 13.02, 14.4, 12.64, 14.83, 13.85], [12.11, 12.83, 14.21, 12.54, 14.7, 13.78], [13.21, 13.96, 15.32, 13.68, 15.82, 14.91], [11.03, 11.82, 13.18, 11.61, 13.74, 12.88], [12.94, 13.74, 15.08, 13.54, 15.63, 14.78], [11.64, 12.48, 13.8, 12.33, 14.39, 13.59]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 12.38), ('CB', 'HIS', 'CG', 'HIS', 12.11), ('CB', 'HIS', 'ND1', 'HIS', 13.21), ('CB', 'HIS', 'CD2', 'HIS', 11.03), ('CB', 'HIS', 'CE1', 'HIS', 12.94), ('CB', 'HIS', 'NE2', 'HIS', 11.64)], [('CG', 'HIS', 'CB', 'HIS', 13.02), ('CG', 'HIS', 'CG', 'HIS', 12.83), ('CG', 'HIS', 'ND1', 'HIS', 13.96), ('CG', 'HIS', 'CD2', 'HIS', 11.82), ('CG', 'HIS', 'CE1', 'HIS', 13.74), ('CG', 'HIS', 'NE2', 'HIS', 12.48)], [('ND1', 'HIS', 'CB', 'HIS', 14.4), ('ND1', 'HIS', 'CG', 'HIS', 14.21), ('ND1', 'HIS', 'ND1', 'HIS', 15.32), ('ND1', 'HIS', 'CD2', 'HIS', 13.18), ('ND1', 'HIS', 'CE1', 'HIS', 15.08), ('ND1', 'HIS', 'NE2', 'HIS', 13.8)], [('CD2', 'HIS', 'CB', 'HIS', 12.64), ('CD2', 'HIS', 'CG', 'HIS', 12.54), ('CD2', 'HIS', 'ND1', 'HIS', 13.68), ('CD2', 'HIS', 'CD2', 'HIS', 11.61), ('CD2', 'HIS', 'CE1', 'HIS', 13.54), ('CD2', 'HIS', 'NE2', 'HIS', 12.33)], [('CE1', 'HIS', 'CB', 'HIS', 14.83), ('CE1', 'HIS', 'CG', 'HIS', 14.7), ('CE1', 'HIS', 'ND1', 'HIS', 15.82), ('CE1', 'HIS', 'CD2', 'HIS', 13.74), ('CE1', 'HIS', 'CE1', 'HIS', 15.63), ('CE1', 'HIS', 'NE2', 'HIS', 14.39)], [('NE2', 'HIS', 'CB', 'HIS', 13.85), ('NE2', 'HIS', 'CG', 'HIS', 13.78), ('NE2', 'HIS', 'ND1', 'HIS', 14.91), ('NE2', 'HIS', 'CD2', 'HIS', 12.88), ('NE2', 'HIS', 'CE1', 'HIS', 14.78), ('NE2', 'HIS', 'NE2', 'HIS', 13.59)], [('CB', 'HIS', 'CB', 'HIS', 12.38), ('CB', 'HIS', 'CG', 'HIS', 13.02), ('CB', 'HIS', 'ND1', 'HIS', 14.4), ('CB', 'HIS', 'CD2', 'HIS', 12.64), ('CB', 'HIS', 'CE1', 'HIS', 14.83), ('CB', 'HIS', 'NE2', 'HIS', 13.85)], [('CG', 'HIS', 'CB', 'HIS', 12.11), ('CG', 'HIS', 'CG', 'HIS', 12.83), ('CG', 'HIS', 'ND1', 'HIS', 14.21), ('CG', 'HIS', 'CD2', 'HIS', 12.54), ('CG', 'HIS', 'CE1', 'HIS', 14.7), ('CG', 'HIS', 'NE2', 'HIS', 13.78)], [('ND1', 'HIS', 'CB', 'HIS', 13.21), ('ND1', 'HIS', 'CG', 'HIS', 13.96), ('ND1', 'HIS', 'ND1', 'HIS', 15.32), ('ND1', 'HIS', 'CD2', 'HIS', 13.68), ('ND1', 'HIS', 'CE1', 'HIS', 15.82), ('ND1', 'HIS', 'NE2', 'HIS', 14.91)], [('CD2', 'HIS', 'CB', 'HIS', 11.03), ('CD2', 'HIS', 'CG', 'HIS', 11.82), ('CD2', 'HIS', 'ND1', 'HIS', 13.18), ('CD2', 'HIS', 'CD2', 'HIS', 11.61), ('CD2', 'HIS', 'CE1', 'HIS', 13.74), ('CD2', 'HIS', 'NE2', 'HIS', 12.88)], [('CE1', 'HIS', 'CB', 'HIS', 12.94), ('CE1', 'HIS', 'CG', 'HIS', 13.74), ('CE1', 'HIS', 'ND1', 'HIS', 15.08), ('CE1', 'HIS', 'CD2', 'HIS', 13.54), ('CE1', 'HIS', 'CE1', 'HIS', 15.63), ('CE1', 'HIS', 'NE2', 'HIS', 14.78)], [('NE2', 'HIS', 'CB', 'HIS', 11.64), ('NE2', 'HIS', 'CG', 'HIS', 12.48), ('NE2', 'HIS', 'ND1', 'HIS', 13.8), ('NE2', 'HIS', 'CD2', 'HIS', 12.33), ('NE2', 'HIS', 'CE1', 'HIS', 14.39), ('NE2', 'HIS', 'NE2', 'HIS', 13.59)]]}
GLU_HIS = { 
	'distances':
		[[7.69, 8.96, 10.19, 9.37, 11.15, 10.74], [7.93, 9.1, 10.37, 9.37, 11.24, 10.73], [6.86, 7.94, 9.2, 8.19, 10.03, 9.52], [7.44, 8.4, 9.59, 8.6, 10.36, 9.86], [5.69, 6.76, 8.04, 7.04, 8.88, 8.39], [8.35, 7.94, 8.93, 6.95, 8.72, 7.56], [7.79, 7.09, 7.98, 5.91, 7.59, 6.34], [8.59, 7.86, 8.74, 6.6, 8.27, 6.95], [8.95, 8.02, 8.7, 6.69, 8.03, 6.73], [9.15, 8.64, 9.65, 7.47, 9.3, 8.0]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 7.69), ('CB', 'GLU', 'CG', 'HIS', 8.96), ('CB', 'GLU', 'ND1', 'HIS', 10.19), ('CB', 'GLU', 'CD2', 'HIS', 9.37), ('CB', 'GLU', 'CE1', 'HIS', 11.15), ('CB', 'GLU', 'NE2', 'HIS', 10.74)], [('CG', 'GLU', 'CB', 'HIS', 7.93), ('CG', 'GLU', 'CG', 'HIS', 9.1), ('CG', 'GLU', 'ND1', 'HIS', 10.37), ('CG', 'GLU', 'CD2', 'HIS', 9.37), ('CG', 'GLU', 'CE1', 'HIS', 11.24), ('CG', 'GLU', 'NE2', 'HIS', 10.73)], [('CD', 'GLU', 'CB', 'HIS', 6.86), ('CD', 'GLU', 'CG', 'HIS', 7.94), ('CD', 'GLU', 'ND1', 'HIS', 9.2), ('CD', 'GLU', 'CD2', 'HIS', 8.19), ('CD', 'GLU', 'CE1', 'HIS', 10.03), ('CD', 'GLU', 'NE2', 'HIS', 9.52)], [('OE1', 'GLU', 'CB', 'HIS', 7.44), ('OE1', 'GLU', 'CG', 'HIS', 8.4), ('OE1', 'GLU', 'ND1', 'HIS', 9.59), ('OE1', 'GLU', 'CD2', 'HIS', 8.6), ('OE1', 'GLU', 'CE1', 'HIS', 10.36), ('OE1', 'GLU', 'NE2', 'HIS', 9.86)], [('OE2', 'GLU', 'CB', 'HIS', 5.69), ('OE2', 'GLU', 'CG', 'HIS', 6.76), ('OE2', 'GLU', 'ND1', 'HIS', 8.04), ('OE2', 'GLU', 'CD2', 'HIS', 7.04), ('OE2', 'GLU', 'CE1', 'HIS', 8.88), ('OE2', 'GLU', 'NE2', 'HIS', 8.39)], [('CB', 'GLU', 'CB', 'HIS', 8.35), ('CB', 'GLU', 'CG', 'HIS', 7.94), ('CB', 'GLU', 'ND1', 'HIS', 8.93), ('CB', 'GLU', 'CD2', 'HIS', 6.95), ('CB', 'GLU', 'CE1', 'HIS', 8.72), ('CB', 'GLU', 'NE2', 'HIS', 7.56)], [('CG', 'GLU', 'CB', 'HIS', 7.79), ('CG', 'GLU', 'CG', 'HIS', 7.09), ('CG', 'GLU', 'ND1', 'HIS', 7.98), ('CG', 'GLU', 'CD2', 'HIS', 5.91), ('CG', 'GLU', 'CE1', 'HIS', 7.59), ('CG', 'GLU', 'NE2', 'HIS', 6.34)], [('CD', 'GLU', 'CB', 'HIS', 8.59), ('CD', 'GLU', 'CG', 'HIS', 7.86), ('CD', 'GLU', 'ND1', 'HIS', 8.74), ('CD', 'GLU', 'CD2', 'HIS', 6.6), ('CD', 'GLU', 'CE1', 'HIS', 8.27), ('CD', 'GLU', 'NE2', 'HIS', 6.95)], [('OE1', 'GLU', 'CB', 'HIS', 8.95), ('OE1', 'GLU', 'CG', 'HIS', 8.02), ('OE1', 'GLU', 'ND1', 'HIS', 8.7), ('OE1', 'GLU', 'CD2', 'HIS', 6.69), ('OE1', 'GLU', 'CE1', 'HIS', 8.03), ('OE1', 'GLU', 'NE2', 'HIS', 6.73)], [('OE2', 'GLU', 'CB', 'HIS', 9.15), ('OE2', 'GLU', 'CG', 'HIS', 8.64), ('OE2', 'GLU', 'ND1', 'HIS', 9.65), ('OE2', 'GLU', 'CD2', 'HIS', 7.47), ('OE2', 'GLU', 'CE1', 'HIS', 9.3), ('OE2', 'GLU', 'NE2', 'HIS', 8.0)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'P_1c1h_4_99_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_HIS, d, 'P_1c1h_4_99_1_1')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'GLU_HIS' :  match2}