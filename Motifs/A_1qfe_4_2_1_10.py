'''
FUNC:A_1qfe_4_2_1_10
PDB:1qfe
EC:4.2.1.10
RESI:glu,his,lys
LOCI:a-86,143,170;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[10.53, 9.61, 9.49, 8.85, 8.38], [9.39, 8.46, 8.17, 7.56, 6.99], [9.09, 8.38, 8.0, 7.67, 6.99], [8.72, 7.6, 7.18, 6.38, 5.8], [8.22, 7.49, 6.91, 6.65, 5.86], [7.94, 6.93, 6.29, 5.68, 4.9]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 10.53), ('CB', 'HIS', 'CG', 'LYS', 9.61), ('CB', 'HIS', 'CD', 'LYS', 9.49), ('CB', 'HIS', 'CE', 'LYS', 8.85), ('CB', 'HIS', 'NZ', 'LYS', 8.38)], [('CG', 'HIS', 'CB', 'LYS', 9.39), ('CG', 'HIS', 'CG', 'LYS', 8.46), ('CG', 'HIS', 'CD', 'LYS', 8.17), ('CG', 'HIS', 'CE', 'LYS', 7.56), ('CG', 'HIS', 'NZ', 'LYS', 6.99)], [('ND1', 'HIS', 'CB', 'LYS', 9.09), ('ND1', 'HIS', 'CG', 'LYS', 8.38), ('ND1', 'HIS', 'CD', 'LYS', 8.0), ('ND1', 'HIS', 'CE', 'LYS', 7.67), ('ND1', 'HIS', 'NZ', 'LYS', 6.99)], [('CD2', 'HIS', 'CB', 'LYS', 8.72), ('CD2', 'HIS', 'CG', 'LYS', 7.6), ('CD2', 'HIS', 'CD', 'LYS', 7.18), ('CD2', 'HIS', 'CE', 'LYS', 6.38), ('CD2', 'HIS', 'NZ', 'LYS', 5.8)], [('CE1', 'HIS', 'CB', 'LYS', 8.22), ('CE1', 'HIS', 'CG', 'LYS', 7.49), ('CE1', 'HIS', 'CD', 'LYS', 6.91), ('CE1', 'HIS', 'CE', 'LYS', 6.65), ('CE1', 'HIS', 'NZ', 'LYS', 5.86)], [('NE2', 'HIS', 'CB', 'LYS', 7.94), ('NE2', 'HIS', 'CG', 'LYS', 6.93), ('NE2', 'HIS', 'CD', 'LYS', 6.29), ('NE2', 'HIS', 'CE', 'LYS', 5.68), ('NE2', 'HIS', 'NZ', 'LYS', 4.9)]]}
GLU_LYS = { 
	'distances':
		[[13.03, 12.38, 11.88, 11.44, 10.47], [13.33, 12.84, 12.49, 12.22, 11.36], [12.21, 11.87, 11.63, 11.55, 10.82], [11.02, 10.64, 10.38, 10.31, 9.6], [12.65, 12.46, 12.33, 12.39, 11.74]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 13.03), ('CB', 'GLU', 'CG', 'LYS', 12.38), ('CB', 'GLU', 'CD', 'LYS', 11.88), ('CB', 'GLU', 'CE', 'LYS', 11.44), ('CB', 'GLU', 'NZ', 'LYS', 10.47)], [('CG', 'GLU', 'CB', 'LYS', 13.33), ('CG', 'GLU', 'CG', 'LYS', 12.84), ('CG', 'GLU', 'CD', 'LYS', 12.49), ('CG', 'GLU', 'CE', 'LYS', 12.22), ('CG', 'GLU', 'NZ', 'LYS', 11.36)], [('CD', 'GLU', 'CB', 'LYS', 12.21), ('CD', 'GLU', 'CG', 'LYS', 11.87), ('CD', 'GLU', 'CD', 'LYS', 11.63), ('CD', 'GLU', 'CE', 'LYS', 11.55), ('CD', 'GLU', 'NZ', 'LYS', 10.82)], [('OE1', 'GLU', 'CB', 'LYS', 11.02), ('OE1', 'GLU', 'CG', 'LYS', 10.64), ('OE1', 'GLU', 'CD', 'LYS', 10.38), ('OE1', 'GLU', 'CE', 'LYS', 10.31), ('OE1', 'GLU', 'NZ', 'LYS', 9.6)], [('OE2', 'GLU', 'CB', 'LYS', 12.65), ('OE2', 'GLU', 'CG', 'LYS', 12.46), ('OE2', 'GLU', 'CD', 'LYS', 12.33), ('OE2', 'GLU', 'CE', 'LYS', 12.39), ('OE2', 'GLU', 'NZ', 'LYS', 11.74)]]}
GLU_HIS = { 
	'distances':
		[[6.21, 6.42, 6.02, 7.5, 6.97, 7.77], [6.85, 7.17, 6.6, 8.38, 7.62, 8.59], [6.66, 6.78, 5.98, 8.01, 6.96, 8.07], [5.9, 5.75, 4.8, 6.91, 5.75, 6.88], [7.63, 7.81, 6.97, 9.04, 7.9, 9.06]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 6.21), ('CB', 'GLU', 'CG', 'HIS', 6.42), ('CB', 'GLU', 'ND1', 'HIS', 6.02), ('CB', 'GLU', 'CD2', 'HIS', 7.5), ('CB', 'GLU', 'CE1', 'HIS', 6.97), ('CB', 'GLU', 'NE2', 'HIS', 7.77)], [('CG', 'GLU', 'CB', 'HIS', 6.85), ('CG', 'GLU', 'CG', 'HIS', 7.17), ('CG', 'GLU', 'ND1', 'HIS', 6.6), ('CG', 'GLU', 'CD2', 'HIS', 8.38), ('CG', 'GLU', 'CE1', 'HIS', 7.62), ('CG', 'GLU', 'NE2', 'HIS', 8.59)], [('CD', 'GLU', 'CB', 'HIS', 6.66), ('CD', 'GLU', 'CG', 'HIS', 6.78), ('CD', 'GLU', 'ND1', 'HIS', 5.98), ('CD', 'GLU', 'CD2', 'HIS', 8.01), ('CD', 'GLU', 'CE1', 'HIS', 6.96), ('CD', 'GLU', 'NE2', 'HIS', 8.07)], [('OE1', 'GLU', 'CB', 'HIS', 5.9), ('OE1', 'GLU', 'CG', 'HIS', 5.75), ('OE1', 'GLU', 'ND1', 'HIS', 4.8), ('OE1', 'GLU', 'CD2', 'HIS', 6.91), ('OE1', 'GLU', 'CE1', 'HIS', 5.75), ('OE1', 'GLU', 'NE2', 'HIS', 6.88)], [('OE2', 'GLU', 'CB', 'HIS', 7.63), ('OE2', 'GLU', 'CG', 'HIS', 7.81), ('OE2', 'GLU', 'ND1', 'HIS', 6.97), ('OE2', 'GLU', 'CD2', 'HIS', 9.04), ('OE2', 'GLU', 'CE1', 'HIS', 7.9), ('OE2', 'GLU', 'NE2', 'HIS', 9.06)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'A_1qfe_4_2_1_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LYS, d, 'A_1qfe_4_2_1_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_1qfe_4_2_1_10')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'GLU_LYS' :  match2,
		'GLU_HIS' :  match3}