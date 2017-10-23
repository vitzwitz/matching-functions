'''
FUNC:A_1nln_3_4_22_39
PDB:1nln
EC:3.4.22.39
RESI:his,glu,gln,cys
LOCI:a-54,71,115,122;
'''
import motifFunctions as cmd
GLN_GLU = { 
	'distances':
		[[11.28, 10.91, 9.98, 10.53, 8.9], [12.06, 11.52, 10.64, 11.3, 9.47], [11.34, 10.67, 9.92, 10.72, 8.7], [12.03, 11.21, 10.51, 11.35, 9.25], [10.11, 9.5, 8.86, 9.73, 7.68]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'GLU', 11.28), ('CB', 'GLN', 'CG', 'GLU', 10.91), ('CB', 'GLN', 'CD', 'GLU', 9.98), ('CB', 'GLN', 'OE1', 'GLU', 10.53), ('CB', 'GLN', 'OE2', 'GLU', 8.9)], [('CG', 'GLN', 'CB', 'GLU', 12.06), ('CG', 'GLN', 'CG', 'GLU', 11.52), ('CG', 'GLN', 'CD', 'GLU', 10.64), ('CG', 'GLN', 'OE1', 'GLU', 11.3), ('CG', 'GLN', 'OE2', 'GLU', 9.47)], [('CD', 'GLN', 'CB', 'GLU', 11.34), ('CD', 'GLN', 'CG', 'GLU', 10.67), ('CD', 'GLN', 'CD', 'GLU', 9.92), ('CD', 'GLN', 'OE1', 'GLU', 10.72), ('CD', 'GLN', 'OE2', 'GLU', 8.7)], [('OE1', 'GLN', 'CB', 'GLU', 12.03), ('OE1', 'GLN', 'CG', 'GLU', 11.21), ('OE1', 'GLN', 'CD', 'GLU', 10.51), ('OE1', 'GLN', 'OE1', 'GLU', 11.35), ('OE1', 'GLN', 'OE2', 'GLU', 9.25)], [('NE2', 'GLN', 'CB', 'GLU', 10.11), ('NE2', 'GLN', 'CG', 'GLU', 9.5), ('NE2', 'GLN', 'CD', 'GLU', 8.86), ('NE2', 'GLN', 'OE1', 'GLU', 9.73), ('NE2', 'GLN', 'OE2', 'GLU', 7.68)]]}
HIS_CYS = { 
	'distances':
		[[7.6, 7.01], [6.76, 6.68], [5.73, 5.87], [7.26, 7.56], [5.7, 6.44], [6.71, 7.45]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 7.6), ('CB', 'HIS', 'SG', 'CYS', 7.01)], [('CG', 'HIS', 'CB', 'CYS', 6.76), ('CG', 'HIS', 'SG', 'CYS', 6.68)], [('ND1', 'HIS', 'CB', 'CYS', 5.73), ('ND1', 'HIS', 'SG', 'CYS', 5.87)], [('CD2', 'HIS', 'CB', 'CYS', 7.26), ('CD2', 'HIS', 'SG', 'CYS', 7.56)], [('CE1', 'HIS', 'CB', 'CYS', 5.7), ('CE1', 'HIS', 'SG', 'CYS', 6.44)], [('NE2', 'HIS', 'CB', 'CYS', 6.71), ('NE2', 'HIS', 'SG', 'CYS', 7.45)]]}
CYS_GLN = { 
	'distances':
		[[7.87, 7.27, 5.92, 5.86, 5.21], [9.42, 8.57, 7.16, 6.66, 6.76]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 7.87), ('CB', 'CYS', 'CG', 'GLN', 7.27), ('CB', 'CYS', 'CD', 'GLN', 5.92), ('CB', 'CYS', 'OE1', 'GLN', 5.86), ('CB', 'CYS', 'NE2', 'GLN', 5.21)], [('SG', 'CYS', 'CB', 'GLN', 9.42), ('SG', 'CYS', 'CG', 'GLN', 8.57), ('SG', 'CYS', 'CD', 'GLN', 7.16), ('SG', 'CYS', 'OE1', 'GLN', 6.66), ('SG', 'CYS', 'NE2', 'GLN', 6.76)]]}
HIS_GLN = { 
	'distances':
		[[11.68, 11.17, 9.74, 9.29, 9.15], [10.37, 10.01, 8.62, 8.36, 7.91], [9.12, 8.68, 7.27, 6.99, 6.63], [10.31, 10.21, 8.93, 8.9, 8.04], [8.22, 8.03, 6.74, 6.78, 5.89], [9.04, 9.07, 7.89, 8.05, 6.92]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 11.68), ('CB', 'HIS', 'CG', 'GLN', 11.17), ('CB', 'HIS', 'CD', 'GLN', 9.74), ('CB', 'HIS', 'OE1', 'GLN', 9.29), ('CB', 'HIS', 'NE2', 'GLN', 9.15)], [('CG', 'HIS', 'CB', 'GLN', 10.37), ('CG', 'HIS', 'CG', 'GLN', 10.01), ('CG', 'HIS', 'CD', 'GLN', 8.62), ('CG', 'HIS', 'OE1', 'GLN', 8.36), ('CG', 'HIS', 'NE2', 'GLN', 7.91)], [('ND1', 'HIS', 'CB', 'GLN', 9.12), ('ND1', 'HIS', 'CG', 'GLN', 8.68), ('ND1', 'HIS', 'CD', 'GLN', 7.27), ('ND1', 'HIS', 'OE1', 'GLN', 6.99), ('ND1', 'HIS', 'NE2', 'GLN', 6.63)], [('CD2', 'HIS', 'CB', 'GLN', 10.31), ('CD2', 'HIS', 'CG', 'GLN', 10.21), ('CD2', 'HIS', 'CD', 'GLN', 8.93), ('CD2', 'HIS', 'OE1', 'GLN', 8.9), ('CD2', 'HIS', 'NE2', 'GLN', 8.04)], [('CE1', 'HIS', 'CB', 'GLN', 8.22), ('CE1', 'HIS', 'CG', 'GLN', 8.03), ('CE1', 'HIS', 'CD', 'GLN', 6.74), ('CE1', 'HIS', 'OE1', 'GLN', 6.78), ('CE1', 'HIS', 'NE2', 'GLN', 5.89)], [('NE2', 'HIS', 'CB', 'GLN', 9.04), ('NE2', 'HIS', 'CG', 'GLN', 9.07), ('NE2', 'HIS', 'CD', 'GLN', 7.89), ('NE2', 'HIS', 'OE1', 'GLN', 8.05), ('NE2', 'HIS', 'NE2', 'GLN', 6.92)]]}
HIS_GLU = { 
	'distances':
		[[10.02, 8.65, 8.83, 9.86, 8.18], [8.85, 7.49, 7.53, 8.6, 6.77], [9.13, 7.87, 7.68, 8.75, 6.68], [7.54, 6.15, 6.26, 7.34, 5.65], [8.15, 6.98, 6.63, 7.71, 5.54], [7.02, 5.73, 5.53, 6.65, 4.63]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 10.02), ('CB', 'HIS', 'CG', 'GLU', 8.65), ('CB', 'HIS', 'CD', 'GLU', 8.83), ('CB', 'HIS', 'OE1', 'GLU', 9.86), ('CB', 'HIS', 'OE2', 'GLU', 8.18)], [('CG', 'HIS', 'CB', 'GLU', 8.85), ('CG', 'HIS', 'CG', 'GLU', 7.49), ('CG', 'HIS', 'CD', 'GLU', 7.53), ('CG', 'HIS', 'OE1', 'GLU', 8.6), ('CG', 'HIS', 'OE2', 'GLU', 6.77)], [('ND1', 'HIS', 'CB', 'GLU', 9.13), ('ND1', 'HIS', 'CG', 'GLU', 7.87), ('ND1', 'HIS', 'CD', 'GLU', 7.68), ('ND1', 'HIS', 'OE1', 'GLU', 8.75), ('ND1', 'HIS', 'OE2', 'GLU', 6.68)], [('CD2', 'HIS', 'CB', 'GLU', 7.54), ('CD2', 'HIS', 'CG', 'GLU', 6.15), ('CD2', 'HIS', 'CD', 'GLU', 6.26), ('CD2', 'HIS', 'OE1', 'GLU', 7.34), ('CD2', 'HIS', 'OE2', 'GLU', 5.65)], [('CE1', 'HIS', 'CB', 'GLU', 8.15), ('CE1', 'HIS', 'CG', 'GLU', 6.98), ('CE1', 'HIS', 'CD', 'GLU', 6.63), ('CE1', 'HIS', 'OE1', 'GLU', 7.71), ('CE1', 'HIS', 'OE2', 'GLU', 5.54)], [('NE2', 'HIS', 'CB', 'GLU', 7.02), ('NE2', 'HIS', 'CG', 'GLU', 5.73), ('NE2', 'HIS', 'CD', 'GLU', 5.53), ('NE2', 'HIS', 'OE1', 'GLU', 6.65), ('NE2', 'HIS', 'OE2', 'GLU', 4.63)]]}
CYS_GLU = { 
	'distances':
		[[10.31, 9.62, 9.57, 10.72, 8.55], [11.51, 10.66, 10.72, 11.9, 9.72]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 10.31), ('CB', 'CYS', 'CG', 'GLU', 9.62), ('CB', 'CYS', 'CD', 'GLU', 9.57), ('CB', 'CYS', 'OE1', 'GLU', 10.72), ('CB', 'CYS', 'OE2', 'GLU', 8.55)], [('SG', 'CYS', 'CB', 'GLU', 11.51), ('SG', 'CYS', 'CG', 'GLU', 10.66), ('SG', 'CYS', 'CD', 'GLU', 10.72), ('SG', 'CYS', 'OE1', 'GLU', 11.9), ('SG', 'CYS', 'OE2', 'GLU', 9.72)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_GLU, d, 'A_1nln_3_4_22_39')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_CYS, d, 'A_1nln_3_4_22_39')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_GLN, d, 'A_1nln_3_4_22_39')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLN, d, 'A_1nln_3_4_22_39')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_GLU, d, 'A_1nln_3_4_22_39')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_GLU, d, 'A_1nln_3_4_22_39')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_GLU' :  match1,
		'HIS_CYS' :  match2,
		'CYS_GLN' :  match3,
		'HIS_GLN' :  match4,
		'HIS_GLU' :  match5,
		'CYS_GLU' :  match6}