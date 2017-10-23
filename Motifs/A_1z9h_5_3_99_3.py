'''
FUNC:A_1z9h_5_3_99_3
PDB:1z9h
EC:5.3.99.3
RESI:tyr,cys,phe,cys
LOCI:a-107,110,112,113;
'''
import motifFunctions as cmd
CYS_PHE = { 
	'distances':
		[[7.15, 7.56, 7.12, 8.73, 7.98, 9.41, 9.07, 8.52, 7.34, 7.16, 6.32], [5.6, 5.84, 5.34, 7.07, 6.3, 7.74, 7.42, 7.65, 6.48, 5.94, 5.29], [7.32, 8.64, 9.07, 9.67, 10.39, 10.89, 11.21, 6.19, 5.67, 6.81, 6.92], [6.92, 8.17, 8.37, 9.38, 9.69, 10.55, 10.69, 6.69, 6.08, 6.95, 7.17]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'PHE', 7.15), ('CB', 'CYS', 'CG', 'PHE', 7.56), ('CB', 'CYS', 'CD1', 'PHE', 7.12), ('CB', 'CYS', 'CD2', 'PHE', 8.73), ('CB', 'CYS', 'CE1', 'PHE', 7.98), ('CB', 'CYS', 'CE2', 'PHE', 9.41), ('CB', 'CYS', 'CZ', 'PHE', 9.07), ('CB', 'CYS', 'O', 'PHE', 8.52), ('CB', 'CYS', 'C', 'PHE', 7.34), ('CB', 'CYS', 'CA', 'PHE', 7.16), ('CB', 'CYS', 'N', 'PHE', 6.32)], [('SG', 'CYS', 'CB', 'PHE', 5.6), ('SG', 'CYS', 'CG', 'PHE', 5.84), ('SG', 'CYS', 'CD1', 'PHE', 5.34), ('SG', 'CYS', 'CD2', 'PHE', 7.07), ('SG', 'CYS', 'CE1', 'PHE', 6.3), ('SG', 'CYS', 'CE2', 'PHE', 7.74), ('SG', 'CYS', 'CZ', 'PHE', 7.42), ('SG', 'CYS', 'O', 'PHE', 7.65), ('SG', 'CYS', 'C', 'PHE', 6.48), ('SG', 'CYS', 'CA', 'PHE', 5.94), ('SG', 'CYS', 'N', 'PHE', 5.29)], [('CB', 'CYS', 'CB', 'PHE', 7.32), ('CB', 'CYS', 'CG', 'PHE', 8.64), ('CB', 'CYS', 'CD1', 'PHE', 9.07), ('CB', 'CYS', 'CD2', 'PHE', 9.67), ('CB', 'CYS', 'CE1', 'PHE', 10.39), ('CB', 'CYS', 'CE2', 'PHE', 10.89), ('CB', 'CYS', 'CZ', 'PHE', 11.21), ('CB', 'CYS', 'O', 'PHE', 6.19), ('CB', 'CYS', 'C', 'PHE', 5.67), ('CB', 'CYS', 'CA', 'PHE', 6.81), ('CB', 'CYS', 'N', 'PHE', 6.92)], [('SG', 'CYS', 'CB', 'PHE', 6.92), ('SG', 'CYS', 'CG', 'PHE', 8.17), ('SG', 'CYS', 'CD1', 'PHE', 8.37), ('SG', 'CYS', 'CD2', 'PHE', 9.38), ('SG', 'CYS', 'CE1', 'PHE', 9.69), ('SG', 'CYS', 'CE2', 'PHE', 10.55), ('SG', 'CYS', 'CZ', 'PHE', 10.69), ('SG', 'CYS', 'O', 'PHE', 6.69), ('SG', 'CYS', 'C', 'PHE', 6.08), ('SG', 'CYS', 'CA', 'PHE', 6.95), ('SG', 'CYS', 'N', 'PHE', 7.17)]]}
CYS_CYS = { 
	'distances':
		[[6.54, 6.09], [6.86, 6.19], [6.54, 6.86], [6.09, 6.19]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 6.54), ('CB', 'CYS', 'SG', 'CYS', 6.09)], [('SG', 'CYS', 'CB', 'CYS', 6.86), ('SG', 'CYS', 'SG', 'CYS', 6.19)], [('CB', 'CYS', 'CB', 'CYS', 6.54), ('CB', 'CYS', 'SG', 'CYS', 6.86)], [('SG', 'CYS', 'CB', 'CYS', 6.09), ('SG', 'CYS', 'SG', 'CYS', 6.19)]]}
TYR_CYS = { 
	'distances':
		[[5.6, 6.74], [6.58, 7.34], [7.92, 8.74], [6.53, 6.85], [8.96, 9.55], [7.82, 7.91], [8.91, 9.19], [10.16, 10.29], [7.22, 6.18], [8.24, 6.89], [9.21, 7.88], [8.56, 7.03], [10.29, 8.82], [9.72, 8.08], [10.51, 8.9], [11.73, 10.05]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'CYS', 5.6), ('CB', 'TYR', 'SG', 'CYS', 6.74)], [('CG', 'TYR', 'CB', 'CYS', 6.58), ('CG', 'TYR', 'SG', 'CYS', 7.34)], [('CD1', 'TYR', 'CB', 'CYS', 7.92), ('CD1', 'TYR', 'SG', 'CYS', 8.74)], [('CD2', 'TYR', 'CB', 'CYS', 6.53), ('CD2', 'TYR', 'SG', 'CYS', 6.85)], [('CE1', 'TYR', 'CB', 'CYS', 8.96), ('CE1', 'TYR', 'SG', 'CYS', 9.55)], [('CE2', 'TYR', 'CB', 'CYS', 7.82), ('CE2', 'TYR', 'SG', 'CYS', 7.91)], [('CZ', 'TYR', 'CB', 'CYS', 8.91), ('CZ', 'TYR', 'SG', 'CYS', 9.19)], [('OH', 'TYR', 'CB', 'CYS', 10.16), ('OH', 'TYR', 'SG', 'CYS', 10.29)], [('CB', 'TYR', 'CB', 'CYS', 7.22), ('CB', 'TYR', 'SG', 'CYS', 6.18)], [('CG', 'TYR', 'CB', 'CYS', 8.24), ('CG', 'TYR', 'SG', 'CYS', 6.89)], [('CD1', 'TYR', 'CB', 'CYS', 9.21), ('CD1', 'TYR', 'SG', 'CYS', 7.88)], [('CD2', 'TYR', 'CB', 'CYS', 8.56), ('CD2', 'TYR', 'SG', 'CYS', 7.03)], [('CE1', 'TYR', 'CB', 'CYS', 10.29), ('CE1', 'TYR', 'SG', 'CYS', 8.82)], [('CE2', 'TYR', 'CB', 'CYS', 9.72), ('CE2', 'TYR', 'SG', 'CYS', 8.08)], [('CZ', 'TYR', 'CB', 'CYS', 10.51), ('CZ', 'TYR', 'SG', 'CYS', 8.9)], [('OH', 'TYR', 'CB', 'CYS', 11.73), ('OH', 'TYR', 'SG', 'CYS', 10.05)]]}
PHE_CYSI = { 
	'distances':
		[[7.32, 6.92], [8.64, 8.17], [9.07, 8.37], [9.67, 9.38], [10.39, 9.69], [10.89, 10.55], [11.21, 10.69], [6.19, 6.69], [5.67, 6.08], [6.81, 6.95], [6.92, 7.17]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'CYSI', 7.32), ('CB', 'PHE', 'SG', 'CYSI', 6.92)], [('CG', 'PHE', 'CB', 'CYSI', 8.64), ('CG', 'PHE', 'SG', 'CYSI', 8.17)], [('CD1', 'PHE', 'CB', 'CYSI', 9.07), ('CD1', 'PHE', 'SG', 'CYSI', 8.37)], [('CD2', 'PHE', 'CB', 'CYSI', 9.67), ('CD2', 'PHE', 'SG', 'CYSI', 9.38)], [('CE1', 'PHE', 'CB', 'CYSI', 10.39), ('CE1', 'PHE', 'SG', 'CYSI', 9.69)], [('CE2', 'PHE', 'CB', 'CYSI', 10.89), ('CE2', 'PHE', 'SG', 'CYSI', 10.55)], [('CZ', 'PHE', 'CB', 'CYSI', 11.21), ('CZ', 'PHE', 'SG', 'CYSI', 10.69)], [('O', 'PHE', 'CB', 'CYSI', 6.19), ('O', 'PHE', 'SG', 'CYSI', 6.69)], [('C', 'PHE', 'CB', 'CYSI', 5.67), ('C', 'PHE', 'SG', 'CYSI', 6.08)], [('CA', 'PHE', 'CB', 'CYSI', 6.81), ('CA', 'PHE', 'SG', 'CYSI', 6.95)], [('N', 'PHE', 'CB', 'CYSI', 6.92), ('N', 'PHE', 'SG', 'CYSI', 7.17)]]}
TYR_PHE = { 
	'distances':
		[[9.59, 10.26, 9.74, 11.6, 10.68, 12.37, 11.96, 10.51, 9.58, 9.87, 9.46], [10.02, 10.6, 9.95, 11.98, 10.82, 12.69, 12.16, 11.22, 10.35, 10.56, 10.28], [11.32, 11.93, 11.28, 13.32, 12.14, 14.03, 13.49, 12.38, 11.57, 11.87, 11.64], [9.36, 9.78, 9.02, 11.16, 9.82, 11.79, 11.19, 10.96, 10.07, 10.1, 9.91], [11.96, 12.48, 11.75, 13.87, 12.54, 14.52, 13.91, 13.19, 12.43, 12.66, 12.53], [10.13, 10.46, 9.62, 11.82, 10.32, 12.37, 11.69, 11.87, 11.06, 11.04, 10.96], [11.41, 11.8, 11.0, 13.17, 11.7, 13.75, 13.08, 12.96, 12.19, 12.28, 12.22], [12.29, 12.6, 11.75, 13.94, 12.37, 14.45, 13.73, 13.95, 13.23, 13.28, 13.29]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'PHE', 9.59), ('CB', 'TYR', 'CG', 'PHE', 10.26), ('CB', 'TYR', 'CD1', 'PHE', 9.74), ('CB', 'TYR', 'CD2', 'PHE', 11.6), ('CB', 'TYR', 'CE1', 'PHE', 10.68), ('CB', 'TYR', 'CE2', 'PHE', 12.37), ('CB', 'TYR', 'CZ', 'PHE', 11.96), ('CB', 'TYR', 'O', 'PHE', 10.51), ('CB', 'TYR', 'C', 'PHE', 9.58), ('CB', 'TYR', 'CA', 'PHE', 9.87), ('CB', 'TYR', 'N', 'PHE', 9.46)], [('CG', 'TYR', 'CB', 'PHE', 10.02), ('CG', 'TYR', 'CG', 'PHE', 10.6), ('CG', 'TYR', 'CD1', 'PHE', 9.95), ('CG', 'TYR', 'CD2', 'PHE', 11.98), ('CG', 'TYR', 'CE1', 'PHE', 10.82), ('CG', 'TYR', 'CE2', 'PHE', 12.69), ('CG', 'TYR', 'CZ', 'PHE', 12.16), ('CG', 'TYR', 'O', 'PHE', 11.22), ('CG', 'TYR', 'C', 'PHE', 10.35), ('CG', 'TYR', 'CA', 'PHE', 10.56), ('CG', 'TYR', 'N', 'PHE', 10.28)], [('CD1', 'TYR', 'CB', 'PHE', 11.32), ('CD1', 'TYR', 'CG', 'PHE', 11.93), ('CD1', 'TYR', 'CD1', 'PHE', 11.28), ('CD1', 'TYR', 'CD2', 'PHE', 13.32), ('CD1', 'TYR', 'CE1', 'PHE', 12.14), ('CD1', 'TYR', 'CE2', 'PHE', 14.03), ('CD1', 'TYR', 'CZ', 'PHE', 13.49), ('CD1', 'TYR', 'O', 'PHE', 12.38), ('CD1', 'TYR', 'C', 'PHE', 11.57), ('CD1', 'TYR', 'CA', 'PHE', 11.87), ('CD1', 'TYR', 'N', 'PHE', 11.64)], [('CD2', 'TYR', 'CB', 'PHE', 9.36), ('CD2', 'TYR', 'CG', 'PHE', 9.78), ('CD2', 'TYR', 'CD1', 'PHE', 9.02), ('CD2', 'TYR', 'CD2', 'PHE', 11.16), ('CD2', 'TYR', 'CE1', 'PHE', 9.82), ('CD2', 'TYR', 'CE2', 'PHE', 11.79), ('CD2', 'TYR', 'CZ', 'PHE', 11.19), ('CD2', 'TYR', 'O', 'PHE', 10.96), ('CD2', 'TYR', 'C', 'PHE', 10.07), ('CD2', 'TYR', 'CA', 'PHE', 10.1), ('CD2', 'TYR', 'N', 'PHE', 9.91)], [('CE1', 'TYR', 'CB', 'PHE', 11.96), ('CE1', 'TYR', 'CG', 'PHE', 12.48), ('CE1', 'TYR', 'CD1', 'PHE', 11.75), ('CE1', 'TYR', 'CD2', 'PHE', 13.87), ('CE1', 'TYR', 'CE1', 'PHE', 12.54), ('CE1', 'TYR', 'CE2', 'PHE', 14.52), ('CE1', 'TYR', 'CZ', 'PHE', 13.91), ('CE1', 'TYR', 'O', 'PHE', 13.19), ('CE1', 'TYR', 'C', 'PHE', 12.43), ('CE1', 'TYR', 'CA', 'PHE', 12.66), ('CE1', 'TYR', 'N', 'PHE', 12.53)], [('CE2', 'TYR', 'CB', 'PHE', 10.13), ('CE2', 'TYR', 'CG', 'PHE', 10.46), ('CE2', 'TYR', 'CD1', 'PHE', 9.62), ('CE2', 'TYR', 'CD2', 'PHE', 11.82), ('CE2', 'TYR', 'CE1', 'PHE', 10.32), ('CE2', 'TYR', 'CE2', 'PHE', 12.37), ('CE2', 'TYR', 'CZ', 'PHE', 11.69), ('CE2', 'TYR', 'O', 'PHE', 11.87), ('CE2', 'TYR', 'C', 'PHE', 11.06), ('CE2', 'TYR', 'CA', 'PHE', 11.04), ('CE2', 'TYR', 'N', 'PHE', 10.96)], [('CZ', 'TYR', 'CB', 'PHE', 11.41), ('CZ', 'TYR', 'CG', 'PHE', 11.8), ('CZ', 'TYR', 'CD1', 'PHE', 11.0), ('CZ', 'TYR', 'CD2', 'PHE', 13.17), ('CZ', 'TYR', 'CE1', 'PHE', 11.7), ('CZ', 'TYR', 'CE2', 'PHE', 13.75), ('CZ', 'TYR', 'CZ', 'PHE', 13.08), ('CZ', 'TYR', 'O', 'PHE', 12.96), ('CZ', 'TYR', 'C', 'PHE', 12.19), ('CZ', 'TYR', 'CA', 'PHE', 12.28), ('CZ', 'TYR', 'N', 'PHE', 12.22)], [('OH', 'TYR', 'CB', 'PHE', 12.29), ('OH', 'TYR', 'CG', 'PHE', 12.6), ('OH', 'TYR', 'CD1', 'PHE', 11.75), ('OH', 'TYR', 'CD2', 'PHE', 13.94), ('OH', 'TYR', 'CE1', 'PHE', 12.37), ('OH', 'TYR', 'CE2', 'PHE', 14.45), ('OH', 'TYR', 'CZ', 'PHE', 13.73), ('OH', 'TYR', 'O', 'PHE', 13.95), ('OH', 'TYR', 'C', 'PHE', 13.23), ('OH', 'TYR', 'CA', 'PHE', 13.28), ('OH', 'TYR', 'N', 'PHE', 13.29)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_PHE, d, 'A_1z9h_5_3_99_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_CYS, d, 'A_1z9h_5_3_99_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_CYS, d, 'A_1z9h_5_3_99_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(PHE_CYSI, d, 'A_1z9h_5_3_99_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_PHE, d, 'A_1z9h_5_3_99_3')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_PHE' :  match1,
		'CYS_CYS' :  match2,
		'TYR_CYS' :  match3,
		'PHE_CYSI' :  match4,
		'TYR_PHE' :  match5}