'''
FUNC:P_1h16_2_3_1_54
PDB:1h16
EC:2.3.1.54
RESI:trp,cys,cys,gly
LOCI:a-333,418,419,734;
'''
import motifFunctions as cmd
CYS_GLY = { 
	'distances':
		[[9.18, 9.98, 10.48, 11.45], [8.79, 9.35, 9.86, 10.58], [5.77, 6.21, 6.12, 7.25], [5.77, 5.89, 6.03, 6.75]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 9.18), ('CB', 'CYS', 'C', 'GLY', 9.98), ('CB', 'CYS', 'CA', 'GLY', 10.48), ('CB', 'CYS', 'N', 'GLY', 11.45)], [('SG', 'CYS', 'O', 'GLY', 8.79), ('SG', 'CYS', 'C', 'GLY', 9.35), ('SG', 'CYS', 'CA', 'GLY', 9.86), ('SG', 'CYS', 'N', 'GLY', 10.58)], [('CB', 'CYS', 'O', 'GLY', 5.77), ('CB', 'CYS', 'C', 'GLY', 6.21), ('CB', 'CYS', 'CA', 'GLY', 6.12), ('CB', 'CYS', 'N', 'GLY', 7.25)], [('SG', 'CYS', 'O', 'GLY', 5.77), ('SG', 'CYS', 'C', 'GLY', 5.89), ('SG', 'CYS', 'CA', 'GLY', 6.03), ('SG', 'CYS', 'N', 'GLY', 6.75)]]}
TRP_CYS = { 
	'distances':
		[[7.15, 6.86], [6.92, 6.11], [6.9, 6.05], [7.4, 6.14], [7.36, 6.06], [7.65, 6.11], [8.11, 6.84], [8.54, 6.8], [8.91, 7.4], [9.08, 7.37], [9.43, 8.74], [8.52, 7.55], [7.39, 6.4], [9.04, 7.78], [7.22, 5.81], [8.31, 6.81], [10.28, 8.99], [9.0, 7.34], [10.8, 9.33], [10.22, 8.6]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'CYS', 7.15), ('CB', 'TRP', 'SG', 'CYS', 6.86)], [('CG', 'TRP', 'CB', 'CYS', 6.92), ('CG', 'TRP', 'SG', 'CYS', 6.11)], [('CD1', 'TRP', 'CB', 'CYS', 6.9), ('CD1', 'TRP', 'SG', 'CYS', 6.05)], [('CD2', 'TRP', 'CB', 'CYS', 7.4), ('CD2', 'TRP', 'SG', 'CYS', 6.14)], [('NE1', 'TRP', 'CB', 'CYS', 7.36), ('NE1', 'TRP', 'SG', 'CYS', 6.06)], [('CE2', 'TRP', 'CB', 'CYS', 7.65), ('CE2', 'TRP', 'SG', 'CYS', 6.11)], [('CE3', 'TRP', 'CB', 'CYS', 8.11), ('CE3', 'TRP', 'SG', 'CYS', 6.84)], [('CZ2', 'TRP', 'CB', 'CYS', 8.54), ('CZ2', 'TRP', 'SG', 'CYS', 6.8)], [('CZ3', 'TRP', 'CB', 'CYS', 8.91), ('CZ3', 'TRP', 'SG', 'CYS', 7.4)], [('CH2', 'TRP', 'CB', 'CYS', 9.08), ('CH2', 'TRP', 'SG', 'CYS', 7.37)], [('CB', 'TRP', 'CB', 'CYS', 9.43), ('CB', 'TRP', 'SG', 'CYS', 8.74)], [('CG', 'TRP', 'CB', 'CYS', 8.52), ('CG', 'TRP', 'SG', 'CYS', 7.55)], [('CD1', 'TRP', 'CB', 'CYS', 7.39), ('CD1', 'TRP', 'SG', 'CYS', 6.4)], [('CD2', 'TRP', 'CB', 'CYS', 9.04), ('CD2', 'TRP', 'SG', 'CYS', 7.78)], [('NE1', 'TRP', 'CB', 'CYS', 7.22), ('NE1', 'TRP', 'SG', 'CYS', 5.81)], [('CE2', 'TRP', 'CB', 'CYS', 8.31), ('CE2', 'TRP', 'SG', 'CYS', 6.81)], [('CE3', 'TRP', 'CB', 'CYS', 10.28), ('CE3', 'TRP', 'SG', 'CYS', 8.99)], [('CZ2', 'TRP', 'CB', 'CYS', 9.0), ('CZ2', 'TRP', 'SG', 'CYS', 7.34)], [('CZ3', 'TRP', 'CB', 'CYS', 10.8), ('CZ3', 'TRP', 'SG', 'CYS', 9.33)], [('CH2', 'TRP', 'CB', 'CYS', 10.22), ('CH2', 'TRP', 'SG', 'CYS', 8.6)]]}
CYS_CYS = { 
	'distances':
		[[7.21, 7.26], [7.03, 6.4], [7.21, 7.03], [7.26, 6.4]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 7.21), ('CB', 'CYS', 'SG', 'CYS', 7.26)], [('SG', 'CYS', 'CB', 'CYS', 7.03), ('SG', 'CYS', 'SG', 'CYS', 6.4)], [('CB', 'CYS', 'CB', 'CYS', 7.21), ('CB', 'CYS', 'SG', 'CYS', 7.03)], [('SG', 'CYS', 'CB', 'CYS', 7.26), ('SG', 'CYS', 'SG', 'CYS', 6.4)]]}
TRP_GLY = { 
	'distances':
		[[9.14, 9.93, 11.13, 11.86], [8.29, 8.91, 10.04, 10.65], [6.95, 7.55, 8.68, 9.33], [9.03, 9.43, 10.43, 10.83], [6.95, 7.23, 8.19, 8.6], [8.31, 8.51, 9.38, 9.64], [10.42, 10.78, 11.74, 12.05], [9.18, 9.15, 9.83, 9.85], [11.06, 11.25, 12.07, 12.2], [10.51, 10.51, 11.2, 11.18]],
	'comparisons':
		[[('CB', 'TRP', 'O', 'GLY', 9.14), ('CB', 'TRP', 'C', 'GLY', 9.93), ('CB', 'TRP', 'CA', 'GLY', 11.13), ('CB', 'TRP', 'N', 'GLY', 11.86)], [('CG', 'TRP', 'O', 'GLY', 8.29), ('CG', 'TRP', 'C', 'GLY', 8.91), ('CG', 'TRP', 'CA', 'GLY', 10.04), ('CG', 'TRP', 'N', 'GLY', 10.65)], [('CD1', 'TRP', 'O', 'GLY', 6.95), ('CD1', 'TRP', 'C', 'GLY', 7.55), ('CD1', 'TRP', 'CA', 'GLY', 8.68), ('CD1', 'TRP', 'N', 'GLY', 9.33)], [('CD2', 'TRP', 'O', 'GLY', 9.03), ('CD2', 'TRP', 'C', 'GLY', 9.43), ('CD2', 'TRP', 'CA', 'GLY', 10.43), ('CD2', 'TRP', 'N', 'GLY', 10.83)], [('NE1', 'TRP', 'O', 'GLY', 6.95), ('NE1', 'TRP', 'C', 'GLY', 7.23), ('NE1', 'TRP', 'CA', 'GLY', 8.19), ('NE1', 'TRP', 'N', 'GLY', 8.6)], [('CE2', 'TRP', 'O', 'GLY', 8.31), ('CE2', 'TRP', 'C', 'GLY', 8.51), ('CE2', 'TRP', 'CA', 'GLY', 9.38), ('CE2', 'TRP', 'N', 'GLY', 9.64)], [('CE3', 'TRP', 'O', 'GLY', 10.42), ('CE3', 'TRP', 'C', 'GLY', 10.78), ('CE3', 'TRP', 'CA', 'GLY', 11.74), ('CE3', 'TRP', 'N', 'GLY', 12.05)], [('CZ2', 'TRP', 'O', 'GLY', 9.18), ('CZ2', 'TRP', 'C', 'GLY', 9.15), ('CZ2', 'TRP', 'CA', 'GLY', 9.83), ('CZ2', 'TRP', 'N', 'GLY', 9.85)], [('CZ3', 'TRP', 'O', 'GLY', 11.06), ('CZ3', 'TRP', 'C', 'GLY', 11.25), ('CZ3', 'TRP', 'CA', 'GLY', 12.07), ('CZ3', 'TRP', 'N', 'GLY', 12.2)], [('CH2', 'TRP', 'O', 'GLY', 10.51), ('CH2', 'TRP', 'C', 'GLY', 10.51), ('CH2', 'TRP', 'CA', 'GLY', 11.2), ('CH2', 'TRP', 'N', 'GLY', 11.18)]]}
GLY_CYSI = { 
	'distances':
		[[5.77, 5.77], [6.21, 5.89], [6.12, 6.03], [7.25, 6.75]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'CYSI', 5.77), ('O', 'GLY', 'SG', 'CYSI', 5.77)], [('C', 'GLY', 'CB', 'CYSI', 6.21), ('C', 'GLY', 'SG', 'CYSI', 5.89)], [('CA', 'GLY', 'CB', 'CYSI', 6.12), ('CA', 'GLY', 'SG', 'CYSI', 6.03)], [('N', 'GLY', 'CB', 'CYSI', 7.25), ('N', 'GLY', 'SG', 'CYSI', 6.75)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLY, d, 'P_1h16_2_3_1_54')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TRP_CYS, d, 'P_1h16_2_3_1_54')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_CYS, d, 'P_1h16_2_3_1_54')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TRP_GLY, d, 'P_1h16_2_3_1_54')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_CYSI, d, 'P_1h16_2_3_1_54')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLY' :  match1,
		'TRP_CYS' :  match2,
		'CYS_CYS' :  match3,
		'TRP_GLY' :  match4,
		'GLY_CYSI' :  match5}