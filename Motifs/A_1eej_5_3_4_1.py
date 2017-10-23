'''
FUNC:A_1eej_5_3_4_1
PDB:1eej
EC:5.3.4.1
RESI:cys,tyr,cys,arg
LOCI:a-98,100,101,125;
'''
import motifFunctions as cmd
ARG_CYSI = { 
	'distances':
		[[8.57, 9.55], [7.57, 8.31], [6.51, 7.25], [5.79, 6.97], [5.52, 6.81], [5.93, 6.86], [5.54, 7.13]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYSI', 8.57), ('CB', 'ARG', 'SG', 'CYSI', 9.55)], [('CG', 'ARG', 'CB', 'CYSI', 7.57), ('CG', 'ARG', 'SG', 'CYSI', 8.31)], [('CD', 'ARG', 'CB', 'CYSI', 6.51), ('CD', 'ARG', 'SG', 'CYSI', 7.25)], [('NE', 'ARG', 'CB', 'CYSI', 5.79), ('NE', 'ARG', 'SG', 'CYSI', 6.97)], [('CZ', 'ARG', 'CB', 'CYSI', 5.52), ('CZ', 'ARG', 'SG', 'CYSI', 6.81)], [('NH1', 'ARG', 'CB', 'CYSI', 5.93), ('NH1', 'ARG', 'SG', 'CYSI', 6.86)], [('NH2', 'ARG', 'CB', 'CYSI', 5.54), ('NH2', 'ARG', 'SG', 'CYSI', 7.13)]]}
CYS_CYS = { 
	'distances':
		[[5.82, 5.08], [5.04, 4.06], [5.82, 5.04], [5.08, 4.06]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 5.82), ('CB', 'CYS', 'SG', 'CYS', 5.08)], [('SG', 'CYS', 'CB', 'CYS', 5.04), ('SG', 'CYS', 'SG', 'CYS', 4.06)], [('CB', 'CYS', 'CB', 'CYS', 5.82), ('CB', 'CYS', 'SG', 'CYS', 5.04)], [('SG', 'CYS', 'CB', 'CYS', 5.08), ('SG', 'CYS', 'SG', 'CYS', 4.06)]]}
TYR_ARG = { 
	'distances':
		[[12.95, 11.67, 10.46, 10.49, 10.06, 9.52, 10.47], [13.71, 12.49, 11.21, 11.3, 10.76, 10.02, 11.22], [15.07, 13.83, 12.57, 12.68, 12.15, 11.41, 12.58], [13.21, 12.09, 10.74, 10.86, 10.23, 9.33, 10.74], [15.89, 14.71, 13.41, 13.56, 12.96, 12.1, 13.42], [14.16, 13.1, 11.73, 11.89, 11.21, 10.19, 11.73], [15.47, 14.37, 13.03, 13.19, 12.53, 11.55, 13.02], [16.47, 15.43, 14.07, 14.27, 13.56, 12.5, 14.06], [14.57, 13.23, 12.22, 12.05, 11.75, 11.58, 11.89], [13.52, 12.23, 11.16, 10.93, 10.57, 10.38, 10.7], [13.45, 12.22, 11.0, 10.79, 10.27, 9.86, 10.44], [12.76, 11.66, 10.35, 9.96, 9.28, 8.89, 9.32]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 12.95), ('CB', 'TYR', 'CG', 'ARG', 11.67), ('CB', 'TYR', 'CD', 'ARG', 10.46), ('CB', 'TYR', 'NE', 'ARG', 10.49), ('CB', 'TYR', 'CZ', 'ARG', 10.06), ('CB', 'TYR', 'NH1', 'ARG', 9.52), ('CB', 'TYR', 'NH2', 'ARG', 10.47)], [('CG', 'TYR', 'CB', 'ARG', 13.71), ('CG', 'TYR', 'CG', 'ARG', 12.49), ('CG', 'TYR', 'CD', 'ARG', 11.21), ('CG', 'TYR', 'NE', 'ARG', 11.3), ('CG', 'TYR', 'CZ', 'ARG', 10.76), ('CG', 'TYR', 'NH1', 'ARG', 10.02), ('CG', 'TYR', 'NH2', 'ARG', 11.22)], [('CD1', 'TYR', 'CB', 'ARG', 15.07), ('CD1', 'TYR', 'CG', 'ARG', 13.83), ('CD1', 'TYR', 'CD', 'ARG', 12.57), ('CD1', 'TYR', 'NE', 'ARG', 12.68), ('CD1', 'TYR', 'CZ', 'ARG', 12.15), ('CD1', 'TYR', 'NH1', 'ARG', 11.41), ('CD1', 'TYR', 'NH2', 'ARG', 12.58)], [('CD2', 'TYR', 'CB', 'ARG', 13.21), ('CD2', 'TYR', 'CG', 'ARG', 12.09), ('CD2', 'TYR', 'CD', 'ARG', 10.74), ('CD2', 'TYR', 'NE', 'ARG', 10.86), ('CD2', 'TYR', 'CZ', 'ARG', 10.23), ('CD2', 'TYR', 'NH1', 'ARG', 9.33), ('CD2', 'TYR', 'NH2', 'ARG', 10.74)], [('CE1', 'TYR', 'CB', 'ARG', 15.89), ('CE1', 'TYR', 'CG', 'ARG', 14.71), ('CE1', 'TYR', 'CD', 'ARG', 13.41), ('CE1', 'TYR', 'NE', 'ARG', 13.56), ('CE1', 'TYR', 'CZ', 'ARG', 12.96), ('CE1', 'TYR', 'NH1', 'ARG', 12.1), ('CE1', 'TYR', 'NH2', 'ARG', 13.42)], [('CE2', 'TYR', 'CB', 'ARG', 14.16), ('CE2', 'TYR', 'CG', 'ARG', 13.1), ('CE2', 'TYR', 'CD', 'ARG', 11.73), ('CE2', 'TYR', 'NE', 'ARG', 11.89), ('CE2', 'TYR', 'CZ', 'ARG', 11.21), ('CE2', 'TYR', 'NH1', 'ARG', 10.19), ('CE2', 'TYR', 'NH2', 'ARG', 11.73)], [('CZ', 'TYR', 'CB', 'ARG', 15.47), ('CZ', 'TYR', 'CG', 'ARG', 14.37), ('CZ', 'TYR', 'CD', 'ARG', 13.03), ('CZ', 'TYR', 'NE', 'ARG', 13.19), ('CZ', 'TYR', 'CZ', 'ARG', 12.53), ('CZ', 'TYR', 'NH1', 'ARG', 11.55), ('CZ', 'TYR', 'NH2', 'ARG', 13.02)], [('OH', 'TYR', 'CB', 'ARG', 16.47), ('OH', 'TYR', 'CG', 'ARG', 15.43), ('OH', 'TYR', 'CD', 'ARG', 14.07), ('OH', 'TYR', 'NE', 'ARG', 14.27), ('OH', 'TYR', 'CZ', 'ARG', 13.56), ('OH', 'TYR', 'NH1', 'ARG', 12.5), ('OH', 'TYR', 'NH2', 'ARG', 14.06)], [('O', 'TYR', 'CB', 'ARG', 14.57), ('O', 'TYR', 'CG', 'ARG', 13.23), ('O', 'TYR', 'CD', 'ARG', 12.22), ('O', 'TYR', 'NE', 'ARG', 12.05), ('O', 'TYR', 'CZ', 'ARG', 11.75), ('O', 'TYR', 'NH1', 'ARG', 11.58), ('O', 'TYR', 'NH2', 'ARG', 11.89)], [('C', 'TYR', 'CB', 'ARG', 13.52), ('C', 'TYR', 'CG', 'ARG', 12.23), ('C', 'TYR', 'CD', 'ARG', 11.16), ('C', 'TYR', 'NE', 'ARG', 10.93), ('C', 'TYR', 'CZ', 'ARG', 10.57), ('C', 'TYR', 'NH1', 'ARG', 10.38), ('C', 'TYR', 'NH2', 'ARG', 10.7)], [('CA', 'TYR', 'CB', 'ARG', 13.45), ('CA', 'TYR', 'CG', 'ARG', 12.22), ('CA', 'TYR', 'CD', 'ARG', 11.0), ('CA', 'TYR', 'NE', 'ARG', 10.79), ('CA', 'TYR', 'CZ', 'ARG', 10.27), ('CA', 'TYR', 'NH1', 'ARG', 9.86), ('CA', 'TYR', 'NH2', 'ARG', 10.44)], [('N', 'TYR', 'CB', 'ARG', 12.76), ('N', 'TYR', 'CG', 'ARG', 11.66), ('N', 'TYR', 'CD', 'ARG', 10.35), ('N', 'TYR', 'NE', 'ARG', 9.96), ('N', 'TYR', 'CZ', 'ARG', 9.28), ('N', 'TYR', 'NH1', 'ARG', 8.89), ('N', 'TYR', 'NH2', 'ARG', 9.32)]]}
TYR_CYSI = { 
	'distances':
		[[7.7, 6.12], [8.83, 7.38], [10.12, 8.62], [8.84, 7.6], [11.22, 9.8], [10.12, 8.96], [11.21, 9.94], [12.46, 11.26], [8.56, 7.08], [7.44, 6.0], [7.55, 6.16], [6.73, 5.73]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'CYSI', 7.7), ('CB', 'TYR', 'SG', 'CYSI', 6.12)], [('CG', 'TYR', 'CB', 'CYSI', 8.83), ('CG', 'TYR', 'SG', 'CYSI', 7.38)], [('CD1', 'TYR', 'CB', 'CYSI', 10.12), ('CD1', 'TYR', 'SG', 'CYSI', 8.62)], [('CD2', 'TYR', 'CB', 'CYSI', 8.84), ('CD2', 'TYR', 'SG', 'CYSI', 7.6)], [('CE1', 'TYR', 'CB', 'CYSI', 11.22), ('CE1', 'TYR', 'SG', 'CYSI', 9.8)], [('CE2', 'TYR', 'CB', 'CYSI', 10.12), ('CE2', 'TYR', 'SG', 'CYSI', 8.96)], [('CZ', 'TYR', 'CB', 'CYSI', 11.21), ('CZ', 'TYR', 'SG', 'CYSI', 9.94)], [('OH', 'TYR', 'CB', 'CYSI', 12.46), ('OH', 'TYR', 'SG', 'CYSI', 11.26)], [('O', 'TYR', 'CB', 'CYSI', 8.56), ('O', 'TYR', 'SG', 'CYSI', 7.08)], [('C', 'TYR', 'CB', 'CYSI', 7.44), ('C', 'TYR', 'SG', 'CYSI', 6.0)], [('CA', 'TYR', 'CB', 'CYSI', 7.55), ('CA', 'TYR', 'SG', 'CYSI', 6.16)], [('N', 'TYR', 'CB', 'CYSI', 6.73), ('N', 'TYR', 'SG', 'CYSI', 5.73)]]}
CYS_TYR = { 
	'distances':
		[[7.38, 8.87, 9.74, 9.6, 11.09, 10.99, 11.64, 13.01, 6.24, 5.69, 6.82, 6.83], [7.12, 8.56, 9.6, 9.09, 10.91, 10.48, 11.29, 12.65, 7.0, 6.27, 7.07, 7.05], [7.7, 8.83, 10.12, 8.84, 11.22, 10.12, 11.21, 12.46, 8.56, 7.44, 7.55, 6.73], [6.12, 7.38, 8.62, 7.6, 9.8, 8.96, 9.94, 11.26, 7.08, 6.0, 6.16, 5.73]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TYR', 7.38), ('CB', 'CYS', 'CG', 'TYR', 8.87), ('CB', 'CYS', 'CD1', 'TYR', 9.74), ('CB', 'CYS', 'CD2', 'TYR', 9.6), ('CB', 'CYS', 'CE1', 'TYR', 11.09), ('CB', 'CYS', 'CE2', 'TYR', 10.99), ('CB', 'CYS', 'CZ', 'TYR', 11.64), ('CB', 'CYS', 'OH', 'TYR', 13.01), ('CB', 'CYS', 'O', 'TYR', 6.24), ('CB', 'CYS', 'C', 'TYR', 5.69), ('CB', 'CYS', 'CA', 'TYR', 6.82), ('CB', 'CYS', 'N', 'TYR', 6.83)], [('SG', 'CYS', 'CB', 'TYR', 7.12), ('SG', 'CYS', 'CG', 'TYR', 8.56), ('SG', 'CYS', 'CD1', 'TYR', 9.6), ('SG', 'CYS', 'CD2', 'TYR', 9.09), ('SG', 'CYS', 'CE1', 'TYR', 10.91), ('SG', 'CYS', 'CE2', 'TYR', 10.48), ('SG', 'CYS', 'CZ', 'TYR', 11.29), ('SG', 'CYS', 'OH', 'TYR', 12.65), ('SG', 'CYS', 'O', 'TYR', 7.0), ('SG', 'CYS', 'C', 'TYR', 6.27), ('SG', 'CYS', 'CA', 'TYR', 7.07), ('SG', 'CYS', 'N', 'TYR', 7.05)], [('CB', 'CYS', 'CB', 'TYR', 7.7), ('CB', 'CYS', 'CG', 'TYR', 8.83), ('CB', 'CYS', 'CD1', 'TYR', 10.12), ('CB', 'CYS', 'CD2', 'TYR', 8.84), ('CB', 'CYS', 'CE1', 'TYR', 11.22), ('CB', 'CYS', 'CE2', 'TYR', 10.12), ('CB', 'CYS', 'CZ', 'TYR', 11.21), ('CB', 'CYS', 'OH', 'TYR', 12.46), ('CB', 'CYS', 'O', 'TYR', 8.56), ('CB', 'CYS', 'C', 'TYR', 7.44), ('CB', 'CYS', 'CA', 'TYR', 7.55), ('CB', 'CYS', 'N', 'TYR', 6.73)], [('SG', 'CYS', 'CB', 'TYR', 6.12), ('SG', 'CYS', 'CG', 'TYR', 7.38), ('SG', 'CYS', 'CD1', 'TYR', 8.62), ('SG', 'CYS', 'CD2', 'TYR', 7.6), ('SG', 'CYS', 'CE1', 'TYR', 9.8), ('SG', 'CYS', 'CE2', 'TYR', 8.96), ('SG', 'CYS', 'CZ', 'TYR', 9.94), ('SG', 'CYS', 'OH', 'TYR', 11.26), ('SG', 'CYS', 'O', 'TYR', 7.08), ('SG', 'CYS', 'C', 'TYR', 6.0), ('SG', 'CYS', 'CA', 'TYR', 6.16), ('SG', 'CYS', 'N', 'TYR', 5.73)]]}
CYS_ARG = { 
	'distances':
		[[11.59, 10.35, 9.65, 9.25, 9.28, 9.66, 9.27], [10.1, 8.76, 8.1, 7.94, 8.15, 8.48, 8.43], [8.57, 7.57, 6.51, 5.79, 5.52, 5.93, 5.54], [9.55, 8.31, 7.25, 6.97, 6.81, 6.86, 7.13]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 11.59), ('CB', 'CYS', 'CG', 'ARG', 10.35), ('CB', 'CYS', 'CD', 'ARG', 9.65), ('CB', 'CYS', 'NE', 'ARG', 9.25), ('CB', 'CYS', 'CZ', 'ARG', 9.28), ('CB', 'CYS', 'NH1', 'ARG', 9.66), ('CB', 'CYS', 'NH2', 'ARG', 9.27)], [('SG', 'CYS', 'CB', 'ARG', 10.1), ('SG', 'CYS', 'CG', 'ARG', 8.76), ('SG', 'CYS', 'CD', 'ARG', 8.1), ('SG', 'CYS', 'NE', 'ARG', 7.94), ('SG', 'CYS', 'CZ', 'ARG', 8.15), ('SG', 'CYS', 'NH1', 'ARG', 8.48), ('SG', 'CYS', 'NH2', 'ARG', 8.43)], [('CB', 'CYS', 'CB', 'ARG', 8.57), ('CB', 'CYS', 'CG', 'ARG', 7.57), ('CB', 'CYS', 'CD', 'ARG', 6.51), ('CB', 'CYS', 'NE', 'ARG', 5.79), ('CB', 'CYS', 'CZ', 'ARG', 5.52), ('CB', 'CYS', 'NH1', 'ARG', 5.93), ('CB', 'CYS', 'NH2', 'ARG', 5.54)], [('SG', 'CYS', 'CB', 'ARG', 9.55), ('SG', 'CYS', 'CG', 'ARG', 8.31), ('SG', 'CYS', 'CD', 'ARG', 7.25), ('SG', 'CYS', 'NE', 'ARG', 6.97), ('SG', 'CYS', 'CZ', 'ARG', 6.81), ('SG', 'CYS', 'NH1', 'ARG', 6.86), ('SG', 'CYS', 'NH2', 'ARG', 7.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_CYSI, d, 'A_1eej_5_3_4_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_CYS, d, 'A_1eej_5_3_4_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ARG, d, 'A_1eej_5_3_4_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_CYSI, d, 'A_1eej_5_3_4_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_TYR, d, 'A_1eej_5_3_4_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_ARG, d, 'A_1eej_5_3_4_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_CYSI' :  match1,
		'CYS_CYS' :  match2,
		'TYR_ARG' :  match3,
		'TYR_CYSI' :  match4,
		'CYS_TYR' :  match5,
		'CYS_ARG' :  match6}