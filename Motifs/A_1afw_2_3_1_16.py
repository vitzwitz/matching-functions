'''
FUNC:A_1afw_2_3_1_16
PDB:1afw
EC:2.3.1.16
RESI:cys,his,cys,gly
LOCI:a-125,375,403,405;
'''
import motifFunctions as cmd
CYS_GLY = { 
	'distances':
		[[8.72, 8.86, 7.89, 6.65], [7.71, 7.62, 6.46, 5.46], [10.23, 9.77, 8.85, 7.88], [10.7, 10.14, 8.95, 8.03]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 8.72), ('CB', 'CYS', 'C', 'GLY', 8.86), ('CB', 'CYS', 'CA', 'GLY', 7.89), ('CB', 'CYS', 'N', 'GLY', 6.65)], [('SG', 'CYS', 'O', 'GLY', 7.71), ('SG', 'CYS', 'C', 'GLY', 7.62), ('SG', 'CYS', 'CA', 'GLY', 6.46), ('SG', 'CYS', 'N', 'GLY', 5.46)], [('CB', 'CYS', 'O', 'GLY', 10.23), ('CB', 'CYS', 'C', 'GLY', 9.77), ('CB', 'CYS', 'CA', 'GLY', 8.85), ('CB', 'CYS', 'N', 'GLY', 7.88)], [('SG', 'CYS', 'O', 'GLY', 10.7), ('SG', 'CYS', 'C', 'GLY', 10.14), ('SG', 'CYS', 'CA', 'GLY', 8.95), ('SG', 'CYS', 'N', 'GLY', 8.03)]]}
CYS_HIS = { 
	'distances':
		[[9.54, 8.05, 7.36, 7.33, 6.04, 5.98], [9.8, 8.35, 8.03, 7.32, 6.74, 6.16], [12.79, 11.65, 11.51, 10.76, 10.55, 10.03], [11.21, 10.15, 10.19, 9.24, 9.34, 8.69]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 9.54), ('CB', 'CYS', 'CG', 'HIS', 8.05), ('CB', 'CYS', 'ND1', 'HIS', 7.36), ('CB', 'CYS', 'CD2', 'HIS', 7.33), ('CB', 'CYS', 'CE1', 'HIS', 6.04), ('CB', 'CYS', 'NE2', 'HIS', 5.98)], [('SG', 'CYS', 'CB', 'HIS', 9.8), ('SG', 'CYS', 'CG', 'HIS', 8.35), ('SG', 'CYS', 'ND1', 'HIS', 8.03), ('SG', 'CYS', 'CD2', 'HIS', 7.32), ('SG', 'CYS', 'CE1', 'HIS', 6.74), ('SG', 'CYS', 'NE2', 'HIS', 6.16)], [('CB', 'CYS', 'CB', 'HIS', 12.79), ('CB', 'CYS', 'CG', 'HIS', 11.65), ('CB', 'CYS', 'ND1', 'HIS', 11.51), ('CB', 'CYS', 'CD2', 'HIS', 10.76), ('CB', 'CYS', 'CE1', 'HIS', 10.55), ('CB', 'CYS', 'NE2', 'HIS', 10.03)], [('SG', 'CYS', 'CB', 'HIS', 11.21), ('SG', 'CYS', 'CG', 'HIS', 10.15), ('SG', 'CYS', 'ND1', 'HIS', 10.19), ('SG', 'CYS', 'CD2', 'HIS', 9.24), ('SG', 'CYS', 'CE1', 'HIS', 9.34), ('SG', 'CYS', 'NE2', 'HIS', 8.69)]]}
CYS_CYS = { 
	'distances':
		[[8.53, 8.06], [8.43, 7.82], [8.53, 8.43], [8.06, 7.82]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 8.53), ('CB', 'CYS', 'SG', 'CYS', 8.06)], [('SG', 'CYS', 'CB', 'CYS', 8.43), ('SG', 'CYS', 'SG', 'CYS', 7.82)], [('CB', 'CYS', 'CB', 'CYS', 8.53), ('CB', 'CYS', 'SG', 'CYS', 8.43)], [('SG', 'CYS', 'CB', 'CYS', 8.06), ('SG', 'CYS', 'SG', 'CYS', 7.82)]]}
HIS_CYSI = { 
	'distances':
		[[12.79, 11.21], [11.65, 10.15], [11.51, 10.19], [10.76, 9.24], [10.55, 9.34], [10.03, 8.69]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYSI', 12.79), ('CB', 'HIS', 'SG', 'CYSI', 11.21)], [('CG', 'HIS', 'CB', 'CYSI', 11.65), ('CG', 'HIS', 'SG', 'CYSI', 10.15)], [('ND1', 'HIS', 'CB', 'CYSI', 11.51), ('ND1', 'HIS', 'SG', 'CYSI', 10.19)], [('CD2', 'HIS', 'CB', 'CYSI', 10.76), ('CD2', 'HIS', 'SG', 'CYSI', 9.24)], [('CE1', 'HIS', 'CB', 'CYSI', 10.55), ('CE1', 'HIS', 'SG', 'CYSI', 9.34)], [('NE2', 'HIS', 'CB', 'CYSI', 10.03), ('NE2', 'HIS', 'SG', 'CYSI', 8.69)]]}
GLY_HIS = { 
	'distances':
		[[15.45, 14.02, 13.72, 12.92, 12.42, 11.85], [15.18, 13.8, 13.63, 12.62, 12.36, 11.65], [13.81, 12.45, 12.37, 11.24, 11.13, 10.33], [13.02, 11.62, 11.4, 10.47, 10.12, 9.45]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 15.45), ('O', 'GLY', 'CG', 'HIS', 14.02), ('O', 'GLY', 'ND1', 'HIS', 13.72), ('O', 'GLY', 'CD2', 'HIS', 12.92), ('O', 'GLY', 'CE1', 'HIS', 12.42), ('O', 'GLY', 'NE2', 'HIS', 11.85)], [('C', 'GLY', 'CB', 'HIS', 15.18), ('C', 'GLY', 'CG', 'HIS', 13.8), ('C', 'GLY', 'ND1', 'HIS', 13.63), ('C', 'GLY', 'CD2', 'HIS', 12.62), ('C', 'GLY', 'CE1', 'HIS', 12.36), ('C', 'GLY', 'NE2', 'HIS', 11.65)], [('CA', 'GLY', 'CB', 'HIS', 13.81), ('CA', 'GLY', 'CG', 'HIS', 12.45), ('CA', 'GLY', 'ND1', 'HIS', 12.37), ('CA', 'GLY', 'CD2', 'HIS', 11.24), ('CA', 'GLY', 'CE1', 'HIS', 11.13), ('CA', 'GLY', 'NE2', 'HIS', 10.33)], [('N', 'GLY', 'CB', 'HIS', 13.02), ('N', 'GLY', 'CG', 'HIS', 11.62), ('N', 'GLY', 'ND1', 'HIS', 11.4), ('N', 'GLY', 'CD2', 'HIS', 10.47), ('N', 'GLY', 'CE1', 'HIS', 10.12), ('N', 'GLY', 'NE2', 'HIS', 9.45)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLY, d, 'A_1afw_2_3_1_16')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_HIS, d, 'A_1afw_2_3_1_16')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_CYS, d, 'A_1afw_2_3_1_16')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_CYSI, d, 'A_1afw_2_3_1_16')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_HIS, d, 'A_1afw_2_3_1_16')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLY' :  match1,
		'CYS_HIS' :  match2,
		'CYS_CYS' :  match3,
		'HIS_CYSI' :  match4,
		'GLY_HIS' :  match5}