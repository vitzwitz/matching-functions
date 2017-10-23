'''
FUNC:A_1bwz_5_1_1_7
PDB:1bwz
EC:5.1.1.7
RESI:cys,his,glu,cys
LOCI:a-73,159,208,217;
'''
import motifFunctions as cmd
CYS_CYS = { 
	'distances':
		[[5.77, 5.04], [5.03, 4.03], [5.77, 5.03], [5.04, 4.03]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 5.77), ('CB', 'CYS', 'SG', 'CYS', 5.04)], [('SG', 'CYS', 'CB', 'CYS', 5.03), ('SG', 'CYS', 'SG', 'CYS', 4.03)], [('CB', 'CYS', 'CB', 'CYS', 5.77), ('CB', 'CYS', 'SG', 'CYS', 5.03)], [('SG', 'CYS', 'CB', 'CYS', 5.04), ('SG', 'CYS', 'SG', 'CYS', 4.03)]]}
CYS_GLU = { 
	'distances':
		[[8.49, 7.73, 6.86, 7.18, 6.24], [6.79, 6.07, 5.49, 5.99, 5.13], [7.69, 6.4, 6.2, 7.29, 5.31], [7.4, 6.48, 6.41, 7.31, 5.88]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 8.49), ('CB', 'CYS', 'CG', 'GLU', 7.73), ('CB', 'CYS', 'CD', 'GLU', 6.86), ('CB', 'CYS', 'OE1', 'GLU', 7.18), ('CB', 'CYS', 'OE2', 'GLU', 6.24)], [('SG', 'CYS', 'CB', 'GLU', 6.79), ('SG', 'CYS', 'CG', 'GLU', 6.07), ('SG', 'CYS', 'CD', 'GLU', 5.49), ('SG', 'CYS', 'OE1', 'GLU', 5.99), ('SG', 'CYS', 'OE2', 'GLU', 5.13)], [('CB', 'CYS', 'CB', 'GLU', 7.69), ('CB', 'CYS', 'CG', 'GLU', 6.4), ('CB', 'CYS', 'CD', 'GLU', 6.2), ('CB', 'CYS', 'OE1', 'GLU', 7.29), ('CB', 'CYS', 'OE2', 'GLU', 5.31)], [('SG', 'CYS', 'CB', 'GLU', 7.4), ('SG', 'CYS', 'CG', 'GLU', 6.48), ('SG', 'CYS', 'CD', 'GLU', 6.41), ('SG', 'CYS', 'OE1', 'GLU', 7.31), ('SG', 'CYS', 'OE2', 'GLU', 5.88)]]}
GLU_HIS = { 
	'distances':
		[[12.32, 11.27, 10.1, 11.4, 9.48, 10.33], [12.4, 11.28, 10.02, 11.39, 9.33, 10.24], [13.25, 12.02, 10.8, 11.95, 9.94, 10.7], [13.98, 12.73, 11.58, 12.58, 10.68, 11.33], [13.36, 12.08, 10.85, 11.98, 9.94, 10.68]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 12.32), ('CB', 'GLU', 'CG', 'HIS', 11.27), ('CB', 'GLU', 'ND1', 'HIS', 10.1), ('CB', 'GLU', 'CD2', 'HIS', 11.4), ('CB', 'GLU', 'CE1', 'HIS', 9.48), ('CB', 'GLU', 'NE2', 'HIS', 10.33)], [('CG', 'GLU', 'CB', 'HIS', 12.4), ('CG', 'GLU', 'CG', 'HIS', 11.28), ('CG', 'GLU', 'ND1', 'HIS', 10.02), ('CG', 'GLU', 'CD2', 'HIS', 11.39), ('CG', 'GLU', 'CE1', 'HIS', 9.33), ('CG', 'GLU', 'NE2', 'HIS', 10.24)], [('CD', 'GLU', 'CB', 'HIS', 13.25), ('CD', 'GLU', 'CG', 'HIS', 12.02), ('CD', 'GLU', 'ND1', 'HIS', 10.8), ('CD', 'GLU', 'CD2', 'HIS', 11.95), ('CD', 'GLU', 'CE1', 'HIS', 9.94), ('CD', 'GLU', 'NE2', 'HIS', 10.7)], [('OE1', 'GLU', 'CB', 'HIS', 13.98), ('OE1', 'GLU', 'CG', 'HIS', 12.73), ('OE1', 'GLU', 'ND1', 'HIS', 11.58), ('OE1', 'GLU', 'CD2', 'HIS', 12.58), ('OE1', 'GLU', 'CE1', 'HIS', 10.68), ('OE1', 'GLU', 'NE2', 'HIS', 11.33)], [('OE2', 'GLU', 'CB', 'HIS', 13.36), ('OE2', 'GLU', 'CG', 'HIS', 12.08), ('OE2', 'GLU', 'ND1', 'HIS', 10.85), ('OE2', 'GLU', 'CD2', 'HIS', 11.98), ('OE2', 'GLU', 'CE1', 'HIS', 9.94), ('OE2', 'GLU', 'NE2', 'HIS', 10.68)]]}
CYS_HIS = { 
	'distances':
		[[12.27, 10.79, 9.94, 10.16, 8.67, 8.8], [11.36, 9.93, 8.92, 9.51, 7.75, 8.15], [11.44, 10.17, 8.96, 10.09, 8.07, 8.84], [10.13, 8.76, 7.64, 8.54, 6.58, 7.22]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 12.27), ('CB', 'CYS', 'CG', 'HIS', 10.79), ('CB', 'CYS', 'ND1', 'HIS', 9.94), ('CB', 'CYS', 'CD2', 'HIS', 10.16), ('CB', 'CYS', 'CE1', 'HIS', 8.67), ('CB', 'CYS', 'NE2', 'HIS', 8.8)], [('SG', 'CYS', 'CB', 'HIS', 11.36), ('SG', 'CYS', 'CG', 'HIS', 9.93), ('SG', 'CYS', 'ND1', 'HIS', 8.92), ('SG', 'CYS', 'CD2', 'HIS', 9.51), ('SG', 'CYS', 'CE1', 'HIS', 7.75), ('SG', 'CYS', 'NE2', 'HIS', 8.15)], [('CB', 'CYS', 'CB', 'HIS', 11.44), ('CB', 'CYS', 'CG', 'HIS', 10.17), ('CB', 'CYS', 'ND1', 'HIS', 8.96), ('CB', 'CYS', 'CD2', 'HIS', 10.09), ('CB', 'CYS', 'CE1', 'HIS', 8.07), ('CB', 'CYS', 'NE2', 'HIS', 8.84)], [('SG', 'CYS', 'CB', 'HIS', 10.13), ('SG', 'CYS', 'CG', 'HIS', 8.76), ('SG', 'CYS', 'ND1', 'HIS', 7.64), ('SG', 'CYS', 'CD2', 'HIS', 8.54), ('SG', 'CYS', 'CE1', 'HIS', 6.58), ('SG', 'CYS', 'NE2', 'HIS', 7.22)]]}
HIS_CYSI = { 
	'distances':
		[[11.44, 10.13], [10.17, 8.76], [8.96, 7.64], [10.09, 8.54], [8.07, 6.58], [8.84, 7.22]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYSI', 11.44), ('CB', 'HIS', 'SG', 'CYSI', 10.13)], [('CG', 'HIS', 'CB', 'CYSI', 10.17), ('CG', 'HIS', 'SG', 'CYSI', 8.76)], [('ND1', 'HIS', 'CB', 'CYSI', 8.96), ('ND1', 'HIS', 'SG', 'CYSI', 7.64)], [('CD2', 'HIS', 'CB', 'CYSI', 10.09), ('CD2', 'HIS', 'SG', 'CYSI', 8.54)], [('CE1', 'HIS', 'CB', 'CYSI', 8.07), ('CE1', 'HIS', 'SG', 'CYSI', 6.58)], [('NE2', 'HIS', 'CB', 'CYSI', 8.84), ('NE2', 'HIS', 'SG', 'CYSI', 7.22)]]}
GLU_CYSI = { 
	'distances':
		[[7.69, 7.4], [6.4, 6.48], [6.2, 6.41], [7.29, 7.31], [5.31, 5.88]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYSI', 7.69), ('CB', 'GLU', 'SG', 'CYSI', 7.4)], [('CG', 'GLU', 'CB', 'CYSI', 6.4), ('CG', 'GLU', 'SG', 'CYSI', 6.48)], [('CD', 'GLU', 'CB', 'CYSI', 6.2), ('CD', 'GLU', 'SG', 'CYSI', 6.41)], [('OE1', 'GLU', 'CB', 'CYSI', 7.29), ('OE1', 'GLU', 'SG', 'CYSI', 7.31)], [('OE2', 'GLU', 'CB', 'CYSI', 5.31), ('OE2', 'GLU', 'SG', 'CYSI', 5.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_CYS, d, 'A_1bwz_5_1_1_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_GLU, d, 'A_1bwz_5_1_1_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_HIS, d, 'A_1bwz_5_1_1_7')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_HIS, d, 'A_1bwz_5_1_1_7')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_CYSI, d, 'A_1bwz_5_1_1_7')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_CYSI, d, 'A_1bwz_5_1_1_7')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_CYS' :  match1,
		'CYS_GLU' :  match2,
		'GLU_HIS' :  match3,
		'CYS_HIS' :  match4,
		'HIS_CYSI' :  match5,
		'GLU_CYSI' :  match6}