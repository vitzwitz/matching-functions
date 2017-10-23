'''
FUNC:P_1dlu_2_3_1_9
PDB:1dlu
EC:2.3.1.9
RESI:cys,his,cys,gly
LOCI:a-89,348,378,380;
'''
import motifFunctions as cmd
CYS_GLY = { 
	'distances':
		[[8.99, 9.22, 8.19, 7.04], [8.08, 8.1, 6.9, 6.0], [10.34, 9.91, 8.91, 7.84], [10.62, 10.11, 8.88, 7.89]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 8.99), ('CB', 'CYS', 'C', 'GLY', 9.22), ('CB', 'CYS', 'CA', 'GLY', 8.19), ('CB', 'CYS', 'N', 'GLY', 7.04)], [('SG', 'CYS', 'O', 'GLY', 8.08), ('SG', 'CYS', 'C', 'GLY', 8.1), ('SG', 'CYS', 'CA', 'GLY', 6.9), ('SG', 'CYS', 'N', 'GLY', 6.0)], [('CB', 'CYS', 'O', 'GLY', 10.34), ('CB', 'CYS', 'C', 'GLY', 9.91), ('CB', 'CYS', 'CA', 'GLY', 8.91), ('CB', 'CYS', 'N', 'GLY', 7.84)], [('SG', 'CYS', 'O', 'GLY', 10.62), ('SG', 'CYS', 'C', 'GLY', 10.11), ('SG', 'CYS', 'CA', 'GLY', 8.88), ('SG', 'CYS', 'N', 'GLY', 7.89)]]}
HIS_GLY = { 
	'distances':
		[[15.58, 15.39, 14.01, 13.37], [14.23, 14.07, 12.7, 11.98], [14.04, 13.98, 12.66, 11.79], [13.0, 12.79, 11.4, 10.74], [12.81, 12.78, 11.47, 10.54], [12.13, 12.0, 10.64, 9.83]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 15.58), ('CB', 'HIS', 'C', 'GLY', 15.39), ('CB', 'HIS', 'CA', 'GLY', 14.01), ('CB', 'HIS', 'N', 'GLY', 13.37)], [('CG', 'HIS', 'O', 'GLY', 14.23), ('CG', 'HIS', 'C', 'GLY', 14.07), ('CG', 'HIS', 'CA', 'GLY', 12.7), ('CG', 'HIS', 'N', 'GLY', 11.98)], [('ND1', 'HIS', 'O', 'GLY', 14.04), ('ND1', 'HIS', 'C', 'GLY', 13.98), ('ND1', 'HIS', 'CA', 'GLY', 12.66), ('ND1', 'HIS', 'N', 'GLY', 11.79)], [('CD2', 'HIS', 'O', 'GLY', 13.0), ('CD2', 'HIS', 'C', 'GLY', 12.79), ('CD2', 'HIS', 'CA', 'GLY', 11.4), ('CD2', 'HIS', 'N', 'GLY', 10.74)], [('CE1', 'HIS', 'O', 'GLY', 12.81), ('CE1', 'HIS', 'C', 'GLY', 12.78), ('CE1', 'HIS', 'CA', 'GLY', 11.47), ('CE1', 'HIS', 'N', 'GLY', 10.54)], [('NE2', 'HIS', 'O', 'GLY', 12.13), ('NE2', 'HIS', 'C', 'GLY', 12.0), ('NE2', 'HIS', 'CA', 'GLY', 10.64), ('NE2', 'HIS', 'N', 'GLY', 9.83)]]}
CYS_HIS = { 
	'distances':
		[[9.78, 8.29, 7.62, 7.47, 6.31, 6.2], [9.68, 8.25, 7.96, 7.13, 6.73, 6.11], [13.09, 11.76, 11.36, 10.88, 10.22, 9.9], [11.51, 10.24, 9.98, 9.34, 8.93, 8.5]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 9.78), ('CB', 'CYS', 'CG', 'HIS', 8.29), ('CB', 'CYS', 'ND1', 'HIS', 7.62), ('CB', 'CYS', 'CD2', 'HIS', 7.47), ('CB', 'CYS', 'CE1', 'HIS', 6.31), ('CB', 'CYS', 'NE2', 'HIS', 6.2)], [('SG', 'CYS', 'CB', 'HIS', 9.68), ('SG', 'CYS', 'CG', 'HIS', 8.25), ('SG', 'CYS', 'ND1', 'HIS', 7.96), ('SG', 'CYS', 'CD2', 'HIS', 7.13), ('SG', 'CYS', 'CE1', 'HIS', 6.73), ('SG', 'CYS', 'NE2', 'HIS', 6.11)], [('CB', 'CYS', 'CB', 'HIS', 13.09), ('CB', 'CYS', 'CG', 'HIS', 11.76), ('CB', 'CYS', 'ND1', 'HIS', 11.36), ('CB', 'CYS', 'CD2', 'HIS', 10.88), ('CB', 'CYS', 'CE1', 'HIS', 10.22), ('CB', 'CYS', 'NE2', 'HIS', 9.9)], [('SG', 'CYS', 'CB', 'HIS', 11.51), ('SG', 'CYS', 'CG', 'HIS', 10.24), ('SG', 'CYS', 'ND1', 'HIS', 9.98), ('SG', 'CYS', 'CD2', 'HIS', 9.34), ('SG', 'CYS', 'CE1', 'HIS', 8.93), ('SG', 'CYS', 'NE2', 'HIS', 8.5)]]}
CYS_CYS = { 
	'distances':
		[[8.47, 7.91], [8.44, 7.67], [8.47, 8.44], [7.91, 7.67]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 8.47), ('CB', 'CYS', 'SG', 'CYS', 7.91)], [('SG', 'CYS', 'CB', 'CYS', 8.44), ('SG', 'CYS', 'SG', 'CYS', 7.67)], [('CB', 'CYS', 'CB', 'CYS', 8.47), ('CB', 'CYS', 'SG', 'CYS', 8.44)], [('SG', 'CYS', 'CB', 'CYS', 7.91), ('SG', 'CYS', 'SG', 'CYS', 7.67)]]}
GLY_CYSI = { 
	'distances':
		[[10.34, 10.62], [9.91, 10.11], [8.91, 8.88], [7.84, 7.89]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'CYSI', 10.34), ('O', 'GLY', 'SG', 'CYSI', 10.62)], [('C', 'GLY', 'CB', 'CYSI', 9.91), ('C', 'GLY', 'SG', 'CYSI', 10.11)], [('CA', 'GLY', 'CB', 'CYSI', 8.91), ('CA', 'GLY', 'SG', 'CYSI', 8.88)], [('N', 'GLY', 'CB', 'CYSI', 7.84), ('N', 'GLY', 'SG', 'CYSI', 7.89)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLY, d, 'P_1dlu_2_3_1_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLY, d, 'P_1dlu_2_3_1_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_HIS, d, 'P_1dlu_2_3_1_9')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_CYS, d, 'P_1dlu_2_3_1_9')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_CYSI, d, 'P_1dlu_2_3_1_9')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLY' :  match1,
		'HIS_GLY' :  match2,
		'CYS_HIS' :  match3,
		'CYS_CYS' :  match4,
		'GLY_CYSI' :  match5}