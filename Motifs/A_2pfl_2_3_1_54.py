'''
FUNC:A_2pfl_2_3_1_54
PDB:2pfl
EC:2.3.1.54
RESI:trp,cys,cys,gly
LOCI:a-333,418,419,734;
'''
import motifFunctions as cmd
CYS_TRP = { 
	'distances':
		[[8.96, 8.01, 6.87, 8.43, 6.55, 7.6, 9.66, 8.2, 10.09, 9.43], [8.25, 7.05, 5.9, 7.18, 5.17, 6.13, 8.38, 6.56, 8.65, 7.85], [6.77, 6.54, 6.45, 7.01, 6.84, 7.18, 7.76, 8.03, 8.52, 8.63], [6.7, 6.0, 5.91, 5.98, 5.83, 5.88, 6.64, 6.47, 7.12, 7.03]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TRP', 8.96), ('CB', 'CYS', 'CG', 'TRP', 8.01), ('CB', 'CYS', 'CD1', 'TRP', 6.87), ('CB', 'CYS', 'CD2', 'TRP', 8.43), ('CB', 'CYS', 'NE1', 'TRP', 6.55), ('CB', 'CYS', 'CE2', 'TRP', 7.6), ('CB', 'CYS', 'CE3', 'TRP', 9.66), ('CB', 'CYS', 'CZ2', 'TRP', 8.2), ('CB', 'CYS', 'CZ3', 'TRP', 10.09), ('CB', 'CYS', 'CH2', 'TRP', 9.43)], [('SG', 'CYS', 'CB', 'TRP', 8.25), ('SG', 'CYS', 'CG', 'TRP', 7.05), ('SG', 'CYS', 'CD1', 'TRP', 5.9), ('SG', 'CYS', 'CD2', 'TRP', 7.18), ('SG', 'CYS', 'NE1', 'TRP', 5.17), ('SG', 'CYS', 'CE2', 'TRP', 6.13), ('SG', 'CYS', 'CE3', 'TRP', 8.38), ('SG', 'CYS', 'CZ2', 'TRP', 6.56), ('SG', 'CYS', 'CZ3', 'TRP', 8.65), ('SG', 'CYS', 'CH2', 'TRP', 7.85)], [('CB', 'CYS', 'CB', 'TRP', 6.77), ('CB', 'CYS', 'CG', 'TRP', 6.54), ('CB', 'CYS', 'CD1', 'TRP', 6.45), ('CB', 'CYS', 'CD2', 'TRP', 7.01), ('CB', 'CYS', 'NE1', 'TRP', 6.84), ('CB', 'CYS', 'CE2', 'TRP', 7.18), ('CB', 'CYS', 'CE3', 'TRP', 7.76), ('CB', 'CYS', 'CZ2', 'TRP', 8.03), ('CB', 'CYS', 'CZ3', 'TRP', 8.52), ('CB', 'CYS', 'CH2', 'TRP', 8.63)], [('SG', 'CYS', 'CB', 'TRP', 6.7), ('SG', 'CYS', 'CG', 'TRP', 6.0), ('SG', 'CYS', 'CD1', 'TRP', 5.91), ('SG', 'CYS', 'CD2', 'TRP', 5.98), ('SG', 'CYS', 'NE1', 'TRP', 5.83), ('SG', 'CYS', 'CE2', 'TRP', 5.88), ('SG', 'CYS', 'CE3', 'TRP', 6.64), ('SG', 'CYS', 'CZ2', 'TRP', 6.47), ('SG', 'CYS', 'CZ3', 'TRP', 7.12), ('SG', 'CYS', 'CH2', 'TRP', 7.03)]]}
GLY_CYS = { 
	'distances':
		[[5.55, 5.38], [6.04, 5.55], [5.99, 5.72], [7.12, 6.5], [8.97, 8.72], [9.76, 9.27], [10.28, 9.73], [11.28, 10.51]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'CYS', 5.55), ('O', 'GLY', 'SG', 'CYS', 5.38)], [('C', 'GLY', 'CB', 'CYS', 6.04), ('C', 'GLY', 'SG', 'CYS', 5.55)], [('CA', 'GLY', 'CB', 'CYS', 5.99), ('CA', 'GLY', 'SG', 'CYS', 5.72)], [('N', 'GLY', 'CB', 'CYS', 7.12), ('N', 'GLY', 'SG', 'CYS', 6.5)], [('O', 'GLY', 'CB', 'CYS', 8.97), ('O', 'GLY', 'SG', 'CYS', 8.72)], [('C', 'GLY', 'CB', 'CYS', 9.76), ('C', 'GLY', 'SG', 'CYS', 9.27)], [('CA', 'GLY', 'CB', 'CYS', 10.28), ('CA', 'GLY', 'SG', 'CYS', 9.73)], [('N', 'GLY', 'CB', 'CYS', 11.28), ('N', 'GLY', 'SG', 'CYS', 10.51)]]}
CYS_CYS = { 
	'distances':
		[[6.66, 6.46], [6.85, 6.05], [6.66, 6.85], [6.46, 6.05]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 6.66), ('CB', 'CYS', 'SG', 'CYS', 6.46)], [('SG', 'CYS', 'CB', 'CYS', 6.85), ('SG', 'CYS', 'SG', 'CYS', 6.05)], [('CB', 'CYS', 'CB', 'CYS', 6.66), ('CB', 'CYS', 'SG', 'CYS', 6.85)], [('SG', 'CYS', 'CB', 'CYS', 6.46), ('SG', 'CYS', 'SG', 'CYS', 6.05)]]}
GLY_TRP = { 
	'distances':
		[[8.87, 7.96, 6.62, 8.6, 6.47, 7.79, 9.98, 8.55, 10.54, 9.9], [9.61, 8.54, 7.21, 8.96, 6.77, 7.97, 10.28, 8.5, 10.66, 9.86], [10.8, 9.67, 8.34, 9.95, 7.72, 8.83, 11.23, 9.16, 11.46, 10.52], [11.56, 10.31, 9.04, 10.4, 8.23, 9.16, 11.57, 9.25, 11.62, 10.55]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'TRP', 8.87), ('O', 'GLY', 'CG', 'TRP', 7.96), ('O', 'GLY', 'CD1', 'TRP', 6.62), ('O', 'GLY', 'CD2', 'TRP', 8.6), ('O', 'GLY', 'NE1', 'TRP', 6.47), ('O', 'GLY', 'CE2', 'TRP', 7.79), ('O', 'GLY', 'CE3', 'TRP', 9.98), ('O', 'GLY', 'CZ2', 'TRP', 8.55), ('O', 'GLY', 'CZ3', 'TRP', 10.54), ('O', 'GLY', 'CH2', 'TRP', 9.9)], [('C', 'GLY', 'CB', 'TRP', 9.61), ('C', 'GLY', 'CG', 'TRP', 8.54), ('C', 'GLY', 'CD1', 'TRP', 7.21), ('C', 'GLY', 'CD2', 'TRP', 8.96), ('C', 'GLY', 'NE1', 'TRP', 6.77), ('C', 'GLY', 'CE2', 'TRP', 7.97), ('C', 'GLY', 'CE3', 'TRP', 10.28), ('C', 'GLY', 'CZ2', 'TRP', 8.5), ('C', 'GLY', 'CZ3', 'TRP', 10.66), ('C', 'GLY', 'CH2', 'TRP', 9.86)], [('CA', 'GLY', 'CB', 'TRP', 10.8), ('CA', 'GLY', 'CG', 'TRP', 9.67), ('CA', 'GLY', 'CD1', 'TRP', 8.34), ('CA', 'GLY', 'CD2', 'TRP', 9.95), ('CA', 'GLY', 'NE1', 'TRP', 7.72), ('CA', 'GLY', 'CE2', 'TRP', 8.83), ('CA', 'GLY', 'CE3', 'TRP', 11.23), ('CA', 'GLY', 'CZ2', 'TRP', 9.16), ('CA', 'GLY', 'CZ3', 'TRP', 11.46), ('CA', 'GLY', 'CH2', 'TRP', 10.52)], [('N', 'GLY', 'CB', 'TRP', 11.56), ('N', 'GLY', 'CG', 'TRP', 10.31), ('N', 'GLY', 'CD1', 'TRP', 9.04), ('N', 'GLY', 'CD2', 'TRP', 10.4), ('N', 'GLY', 'NE1', 'TRP', 8.23), ('N', 'GLY', 'CE2', 'TRP', 9.16), ('N', 'GLY', 'CE3', 'TRP', 11.57), ('N', 'GLY', 'CZ2', 'TRP', 9.25), ('N', 'GLY', 'CZ3', 'TRP', 11.62), ('N', 'GLY', 'CH2', 'TRP', 10.55)]]}
TRP_CYSI = { 
	'distances':
		[[6.77, 6.7], [6.54, 6.0], [6.45, 5.91], [7.01, 5.98], [6.84, 5.83], [7.18, 5.88], [7.76, 6.64], [8.03, 6.47], [8.52, 7.12], [8.63, 7.03]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'CYSI', 6.77), ('CB', 'TRP', 'SG', 'CYSI', 6.7)], [('CG', 'TRP', 'CB', 'CYSI', 6.54), ('CG', 'TRP', 'SG', 'CYSI', 6.0)], [('CD1', 'TRP', 'CB', 'CYSI', 6.45), ('CD1', 'TRP', 'SG', 'CYSI', 5.91)], [('CD2', 'TRP', 'CB', 'CYSI', 7.01), ('CD2', 'TRP', 'SG', 'CYSI', 5.98)], [('NE1', 'TRP', 'CB', 'CYSI', 6.84), ('NE1', 'TRP', 'SG', 'CYSI', 5.83)], [('CE2', 'TRP', 'CB', 'CYSI', 7.18), ('CE2', 'TRP', 'SG', 'CYSI', 5.88)], [('CE3', 'TRP', 'CB', 'CYSI', 7.76), ('CE3', 'TRP', 'SG', 'CYSI', 6.64)], [('CZ2', 'TRP', 'CB', 'CYSI', 8.03), ('CZ2', 'TRP', 'SG', 'CYSI', 6.47)], [('CZ3', 'TRP', 'CB', 'CYSI', 8.52), ('CZ3', 'TRP', 'SG', 'CYSI', 7.12)], [('CH2', 'TRP', 'CB', 'CYSI', 8.63), ('CH2', 'TRP', 'SG', 'CYSI', 7.03)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_TRP, d, 'A_2pfl_2_3_1_54')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_CYS, d, 'A_2pfl_2_3_1_54')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_CYS, d, 'A_2pfl_2_3_1_54')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_TRP, d, 'A_2pfl_2_3_1_54')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TRP_CYSI, d, 'A_2pfl_2_3_1_54')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_TRP' :  match1,
		'GLY_CYS' :  match2,
		'CYS_CYS' :  match3,
		'GLY_TRP' :  match4,
		'TRP_CYSI' :  match5}