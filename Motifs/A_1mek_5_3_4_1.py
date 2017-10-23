'''
FUNC:A_1mek_5_3_4_1
PDB:1mek
EC:5.3.4.1
RESI:cys,gly,his,cys
LOCI:a-36,37,38,39;
'''
import motifFunctions as cmd
CYS_CYS = { 
	'distances':
		[[5.58, 5.02], [5.02, 4.02], [5.58, 5.02], [5.02, 4.02]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 5.58), ('CB', 'CYS', 'SG', 'CYS', 5.02)], [('SG', 'CYS', 'CB', 'CYS', 5.02), ('SG', 'CYS', 'SG', 'CYS', 4.02)], [('CB', 'CYS', 'CB', 'CYS', 5.58), ('CB', 'CYS', 'SG', 'CYS', 5.02)], [('SG', 'CYS', 'CB', 'CYS', 5.02), ('SG', 'CYS', 'SG', 'CYS', 4.02)]]}
CYS_GLY = { 
	'distances':
		[[7.35, 7.02, 7.56, 7.0], [7.99, 7.34, 7.78, 6.89], [7.91, 6.99, 6.57, 5.24], [7.13, 6.18, 6.25, 5.11]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 7.35), ('CB', 'CYS', 'C', 'GLY', 7.02), ('CB', 'CYS', 'CA', 'GLY', 7.56), ('CB', 'CYS', 'N', 'GLY', 7.0)], [('SG', 'CYS', 'O', 'GLY', 7.99), ('SG', 'CYS', 'C', 'GLY', 7.34), ('SG', 'CYS', 'CA', 'GLY', 7.78), ('SG', 'CYS', 'N', 'GLY', 6.89)], [('CB', 'CYS', 'O', 'GLY', 7.91), ('CB', 'CYS', 'C', 'GLY', 6.99), ('CB', 'CYS', 'CA', 'GLY', 6.57), ('CB', 'CYS', 'N', 'GLY', 5.24)], [('SG', 'CYS', 'O', 'GLY', 7.13), ('SG', 'CYS', 'C', 'GLY', 6.18), ('SG', 'CYS', 'CA', 'GLY', 6.25), ('SG', 'CYS', 'N', 'GLY', 5.11)]]}
GLY_HIS = { 
	'distances':
		[[6.05, 6.57, 6.56, 7.61, 7.57, 8.17], [5.57, 6.33, 6.35, 7.55, 7.54, 8.21], [6.75, 7.55, 7.37, 8.85, 8.59, 9.42], [6.88, 7.95, 7.97, 9.29, 9.28, 10.03]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 6.05), ('O', 'GLY', 'CG', 'HIS', 6.57), ('O', 'GLY', 'ND1', 'HIS', 6.56), ('O', 'GLY', 'CD2', 'HIS', 7.61), ('O', 'GLY', 'CE1', 'HIS', 7.57), ('O', 'GLY', 'NE2', 'HIS', 8.17)], [('C', 'GLY', 'CB', 'HIS', 5.57), ('C', 'GLY', 'CG', 'HIS', 6.33), ('C', 'GLY', 'ND1', 'HIS', 6.35), ('C', 'GLY', 'CD2', 'HIS', 7.55), ('C', 'GLY', 'CE1', 'HIS', 7.54), ('C', 'GLY', 'NE2', 'HIS', 8.21)], [('CA', 'GLY', 'CB', 'HIS', 6.75), ('CA', 'GLY', 'CG', 'HIS', 7.55), ('CA', 'GLY', 'ND1', 'HIS', 7.37), ('CA', 'GLY', 'CD2', 'HIS', 8.85), ('CA', 'GLY', 'CE1', 'HIS', 8.59), ('CA', 'GLY', 'NE2', 'HIS', 9.42)], [('N', 'GLY', 'CB', 'HIS', 6.88), ('N', 'GLY', 'CG', 'HIS', 7.95), ('N', 'GLY', 'ND1', 'HIS', 7.97), ('N', 'GLY', 'CD2', 'HIS', 9.29), ('N', 'GLY', 'CE1', 'HIS', 9.28), ('N', 'GLY', 'NE2', 'HIS', 10.03)]]}
CYS_HIS = { 
	'distances':
		[[7.59, 8.97, 9.87, 9.79, 11.01, 11.03], [7.16, 8.65, 9.6, 9.51, 10.79, 10.8], [8.25, 9.68, 10.19, 10.87, 11.52, 11.94], [6.58, 8.06, 8.71, 9.19, 10.02, 10.32]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 7.59), ('CB', 'CYS', 'CG', 'HIS', 8.97), ('CB', 'CYS', 'ND1', 'HIS', 9.87), ('CB', 'CYS', 'CD2', 'HIS', 9.79), ('CB', 'CYS', 'CE1', 'HIS', 11.01), ('CB', 'CYS', 'NE2', 'HIS', 11.03)], [('SG', 'CYS', 'CB', 'HIS', 7.16), ('SG', 'CYS', 'CG', 'HIS', 8.65), ('SG', 'CYS', 'ND1', 'HIS', 9.6), ('SG', 'CYS', 'CD2', 'HIS', 9.51), ('SG', 'CYS', 'CE1', 'HIS', 10.79), ('SG', 'CYS', 'NE2', 'HIS', 10.8)], [('CB', 'CYS', 'CB', 'HIS', 8.25), ('CB', 'CYS', 'CG', 'HIS', 9.68), ('CB', 'CYS', 'ND1', 'HIS', 10.19), ('CB', 'CYS', 'CD2', 'HIS', 10.87), ('CB', 'CYS', 'CE1', 'HIS', 11.52), ('CB', 'CYS', 'NE2', 'HIS', 11.94)], [('SG', 'CYS', 'CB', 'HIS', 6.58), ('SG', 'CYS', 'CG', 'HIS', 8.06), ('SG', 'CYS', 'ND1', 'HIS', 8.71), ('SG', 'CYS', 'CD2', 'HIS', 9.19), ('SG', 'CYS', 'CE1', 'HIS', 10.02), ('SG', 'CYS', 'NE2', 'HIS', 10.32)]]}
HIS_CYSI = { 
	'distances':
		[[8.25, 6.58], [9.68, 8.06], [10.19, 8.71], [10.87, 9.19], [11.52, 10.02], [11.94, 10.32]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYSI', 8.25), ('CB', 'HIS', 'SG', 'CYSI', 6.58)], [('CG', 'HIS', 'CB', 'CYSI', 9.68), ('CG', 'HIS', 'SG', 'CYSI', 8.06)], [('ND1', 'HIS', 'CB', 'CYSI', 10.19), ('ND1', 'HIS', 'SG', 'CYSI', 8.71)], [('CD2', 'HIS', 'CB', 'CYSI', 10.87), ('CD2', 'HIS', 'SG', 'CYSI', 9.19)], [('CE1', 'HIS', 'CB', 'CYSI', 11.52), ('CE1', 'HIS', 'SG', 'CYSI', 10.02)], [('NE2', 'HIS', 'CB', 'CYSI', 11.94), ('NE2', 'HIS', 'SG', 'CYSI', 10.32)]]}
GLY_CYSI = { 
	'distances':
		[[7.91, 7.13], [6.99, 6.18], [6.57, 6.25], [5.24, 5.11]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'CYSI', 7.91), ('O', 'GLY', 'SG', 'CYSI', 7.13)], [('C', 'GLY', 'CB', 'CYSI', 6.99), ('C', 'GLY', 'SG', 'CYSI', 6.18)], [('CA', 'GLY', 'CB', 'CYSI', 6.57), ('CA', 'GLY', 'SG', 'CYSI', 6.25)], [('N', 'GLY', 'CB', 'CYSI', 5.24), ('N', 'GLY', 'SG', 'CYSI', 5.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_CYS, d, 'A_1mek_5_3_4_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_GLY, d, 'A_1mek_5_3_4_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_HIS, d, 'A_1mek_5_3_4_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_HIS, d, 'A_1mek_5_3_4_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_CYSI, d, 'A_1mek_5_3_4_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLY_CYSI, d, 'A_1mek_5_3_4_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_CYS' :  match1,
		'CYS_GLY' :  match2,
		'GLY_HIS' :  match3,
		'CYS_HIS' :  match4,
		'HIS_CYSI' :  match5,
		'GLY_CYSI' :  match6}