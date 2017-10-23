'''
FUNC:A_1l6p_1_8_1_8
PDB:1l6p
EC:1.8.1.8
RESI:tyr,asp,phe,tyr,cys,cys
LOCI:a-42,68,70,71,103,109;
'''
import motifFunctions as cmd
CYS_CYS = { 
	'distances':
		[[5.95, 5.04], [5.11, 4.04], [5.95, 5.11], [5.04, 4.04]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 5.95), ('CB', 'CYS', 'SG', 'CYS', 5.04)], [('SG', 'CYS', 'CB', 'CYS', 5.11), ('SG', 'CYS', 'SG', 'CYS', 4.04)], [('CB', 'CYS', 'CB', 'CYS', 5.95), ('CB', 'CYS', 'SG', 'CYS', 5.11)], [('SG', 'CYS', 'CB', 'CYS', 5.04), ('SG', 'CYS', 'SG', 'CYS', 4.04)]]}
PHE_TYR = { 
	'distances':
		[[6.68, 6.09, 5.38, 6.81, 5.58, 6.97, 6.4, 7.14], [8.2, 7.51, 6.65, 8.15, 6.52, 8.07, 7.29, 7.71], [8.96, 8.45, 7.5, 9.26, 7.5, 9.27, 8.43, 8.86], [9.02, 8.14, 7.32, 8.5, 6.88, 8.17, 7.35, 7.47], [10.33, 9.75, 8.75, 10.49, 8.59, 10.38, 9.46, 9.69], [10.37, 9.48, 8.58, 9.84, 8.05, 9.41, 8.51, 8.44], [10.95, 10.19, 9.2, 10.73, 8.8, 10.42, 9.47, 9.47], [10.61, 9.16, 8.71, 8.48, 7.49, 7.19, 6.59, 5.44], [11.21, 9.75, 9.43, 8.89, 8.21, 7.54, 7.12, 5.9], [11.46, 9.97, 9.56, 9.18, 8.27, 7.8, 7.26, 5.94], [11.81, 10.41, 10.29, 9.39, 9.17, 8.1, 7.97, 6.91], [12.26, 10.81, 10.5, 9.91, 9.27, 8.57, 8.19, 6.96], [12.56, 11.18, 11.13, 10.08, 10.04, 8.81, 8.78, 7.73], [12.77, 11.36, 11.22, 10.31, 10.08, 9.01, 8.87, 7.75]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'TYR', 6.68), ('CB', 'PHE', 'CG', 'TYR', 6.09), ('CB', 'PHE', 'CD1', 'TYR', 5.38), ('CB', 'PHE', 'CD2', 'TYR', 6.81), ('CB', 'PHE', 'CE1', 'TYR', 5.58), ('CB', 'PHE', 'CE2', 'TYR', 6.97), ('CB', 'PHE', 'CZ', 'TYR', 6.4), ('CB', 'PHE', 'OH', 'TYR', 7.14)], [('CG', 'PHE', 'CB', 'TYR', 8.2), ('CG', 'PHE', 'CG', 'TYR', 7.51), ('CG', 'PHE', 'CD1', 'TYR', 6.65), ('CG', 'PHE', 'CD2', 'TYR', 8.15), ('CG', 'PHE', 'CE1', 'TYR', 6.52), ('CG', 'PHE', 'CE2', 'TYR', 8.07), ('CG', 'PHE', 'CZ', 'TYR', 7.29), ('CG', 'PHE', 'OH', 'TYR', 7.71)], [('CD1', 'PHE', 'CB', 'TYR', 8.96), ('CD1', 'PHE', 'CG', 'TYR', 8.45), ('CD1', 'PHE', 'CD1', 'TYR', 7.5), ('CD1', 'PHE', 'CD2', 'TYR', 9.26), ('CD1', 'PHE', 'CE1', 'TYR', 7.5), ('CD1', 'PHE', 'CE2', 'TYR', 9.27), ('CD1', 'PHE', 'CZ', 'TYR', 8.43), ('CD1', 'PHE', 'OH', 'TYR', 8.86)], [('CD2', 'PHE', 'CB', 'TYR', 9.02), ('CD2', 'PHE', 'CG', 'TYR', 8.14), ('CD2', 'PHE', 'CD1', 'TYR', 7.32), ('CD2', 'PHE', 'CD2', 'TYR', 8.5), ('CD2', 'PHE', 'CE1', 'TYR', 6.88), ('CD2', 'PHE', 'CE2', 'TYR', 8.17), ('CD2', 'PHE', 'CZ', 'TYR', 7.35), ('CD2', 'PHE', 'OH', 'TYR', 7.47)], [('CE1', 'PHE', 'CB', 'TYR', 10.33), ('CE1', 'PHE', 'CG', 'TYR', 9.75), ('CE1', 'PHE', 'CD1', 'TYR', 8.75), ('CE1', 'PHE', 'CD2', 'TYR', 10.49), ('CE1', 'PHE', 'CE1', 'TYR', 8.59), ('CE1', 'PHE', 'CE2', 'TYR', 10.38), ('CE1', 'PHE', 'CZ', 'TYR', 9.46), ('CE1', 'PHE', 'OH', 'TYR', 9.69)], [('CE2', 'PHE', 'CB', 'TYR', 10.37), ('CE2', 'PHE', 'CG', 'TYR', 9.48), ('CE2', 'PHE', 'CD1', 'TYR', 8.58), ('CE2', 'PHE', 'CD2', 'TYR', 9.84), ('CE2', 'PHE', 'CE1', 'TYR', 8.05), ('CE2', 'PHE', 'CE2', 'TYR', 9.41), ('CE2', 'PHE', 'CZ', 'TYR', 8.51), ('CE2', 'PHE', 'OH', 'TYR', 8.44)], [('CZ', 'PHE', 'CB', 'TYR', 10.95), ('CZ', 'PHE', 'CG', 'TYR', 10.19), ('CZ', 'PHE', 'CD1', 'TYR', 9.2), ('CZ', 'PHE', 'CD2', 'TYR', 10.73), ('CZ', 'PHE', 'CE1', 'TYR', 8.8), ('CZ', 'PHE', 'CE2', 'TYR', 10.42), ('CZ', 'PHE', 'CZ', 'TYR', 9.47), ('CZ', 'PHE', 'OH', 'TYR', 9.47)], [('CB', 'PHE', 'CB', 'TYR', 10.61), ('CB', 'PHE', 'CG', 'TYR', 9.16), ('CB', 'PHE', 'CD1', 'TYR', 8.71), ('CB', 'PHE', 'CD2', 'TYR', 8.48), ('CB', 'PHE', 'CE1', 'TYR', 7.49), ('CB', 'PHE', 'CE2', 'TYR', 7.19), ('CB', 'PHE', 'CZ', 'TYR', 6.59), ('CB', 'PHE', 'OH', 'TYR', 5.44)], [('CG', 'PHE', 'CB', 'TYR', 11.21), ('CG', 'PHE', 'CG', 'TYR', 9.75), ('CG', 'PHE', 'CD1', 'TYR', 9.43), ('CG', 'PHE', 'CD2', 'TYR', 8.89), ('CG', 'PHE', 'CE1', 'TYR', 8.21), ('CG', 'PHE', 'CE2', 'TYR', 7.54), ('CG', 'PHE', 'CZ', 'TYR', 7.12), ('CG', 'PHE', 'OH', 'TYR', 5.9)], [('CD1', 'PHE', 'CB', 'TYR', 11.46), ('CD1', 'PHE', 'CG', 'TYR', 9.97), ('CD1', 'PHE', 'CD1', 'TYR', 9.56), ('CD1', 'PHE', 'CD2', 'TYR', 9.18), ('CD1', 'PHE', 'CE1', 'TYR', 8.27), ('CD1', 'PHE', 'CE2', 'TYR', 7.8), ('CD1', 'PHE', 'CZ', 'TYR', 7.26), ('CD1', 'PHE', 'OH', 'TYR', 5.94)], [('CD2', 'PHE', 'CB', 'TYR', 11.81), ('CD2', 'PHE', 'CG', 'TYR', 10.41), ('CD2', 'PHE', 'CD1', 'TYR', 10.29), ('CD2', 'PHE', 'CD2', 'TYR', 9.39), ('CD2', 'PHE', 'CE1', 'TYR', 9.17), ('CD2', 'PHE', 'CE2', 'TYR', 8.1), ('CD2', 'PHE', 'CZ', 'TYR', 7.97), ('CD2', 'PHE', 'OH', 'TYR', 6.91)], [('CE1', 'PHE', 'CB', 'TYR', 12.26), ('CE1', 'PHE', 'CG', 'TYR', 10.81), ('CE1', 'PHE', 'CD1', 'TYR', 10.5), ('CE1', 'PHE', 'CD2', 'TYR', 9.91), ('CE1', 'PHE', 'CE1', 'TYR', 9.27), ('CE1', 'PHE', 'CE2', 'TYR', 8.57), ('CE1', 'PHE', 'CZ', 'TYR', 8.19), ('CE1', 'PHE', 'OH', 'TYR', 6.96)], [('CE2', 'PHE', 'CB', 'TYR', 12.56), ('CE2', 'PHE', 'CG', 'TYR', 11.18), ('CE2', 'PHE', 'CD1', 'TYR', 11.13), ('CE2', 'PHE', 'CD2', 'TYR', 10.08), ('CE2', 'PHE', 'CE1', 'TYR', 10.04), ('CE2', 'PHE', 'CE2', 'TYR', 8.81), ('CE2', 'PHE', 'CZ', 'TYR', 8.78), ('CE2', 'PHE', 'OH', 'TYR', 7.73)], [('CZ', 'PHE', 'CB', 'TYR', 12.77), ('CZ', 'PHE', 'CG', 'TYR', 11.36), ('CZ', 'PHE', 'CD1', 'TYR', 11.22), ('CZ', 'PHE', 'CD2', 'TYR', 10.31), ('CZ', 'PHE', 'CE1', 'TYR', 10.08), ('CZ', 'PHE', 'CE2', 'TYR', 9.01), ('CZ', 'PHE', 'CZ', 'TYR', 8.87), ('CZ', 'PHE', 'OH', 'TYR', 7.75)]]}
TYR_ASP = { 
	'distances':
		[[8.73, 7.39, 7.66, 6.33], [9.1, 7.68, 7.79, 6.69], [8.48, 7.02, 6.93, 6.22], [10.38, 8.99, 9.12, 7.96], [9.29, 7.87, 7.66, 7.2], [11.04, 9.64, 9.67, 8.71], [10.53, 9.13, 9.01, 8.36], [11.46, 10.11, 9.91, 9.44], [11.65, 10.35, 9.33, 10.42], [10.25, 8.93, 7.93, 9.0], [9.2, 7.89, 6.9, 8.0], [10.17, 8.86, 7.92, 8.9], [7.89, 6.55, 5.59, 6.66], [9.04, 7.74, 6.87, 7.77], [7.8, 6.46, 5.57, 6.53], [6.7, 5.4, 4.69, 5.46]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 8.73), ('CB', 'TYR', 'CG', 'ASP', 7.39), ('CB', 'TYR', 'OD1', 'ASP', 7.66), ('CB', 'TYR', 'OD2', 'ASP', 6.33)], [('CG', 'TYR', 'CB', 'ASP', 9.1), ('CG', 'TYR', 'CG', 'ASP', 7.68), ('CG', 'TYR', 'OD1', 'ASP', 7.79), ('CG', 'TYR', 'OD2', 'ASP', 6.69)], [('CD1', 'TYR', 'CB', 'ASP', 8.48), ('CD1', 'TYR', 'CG', 'ASP', 7.02), ('CD1', 'TYR', 'OD1', 'ASP', 6.93), ('CD1', 'TYR', 'OD2', 'ASP', 6.22)], [('CD2', 'TYR', 'CB', 'ASP', 10.38), ('CD2', 'TYR', 'CG', 'ASP', 8.99), ('CD2', 'TYR', 'OD1', 'ASP', 9.12), ('CD2', 'TYR', 'OD2', 'ASP', 7.96)], [('CE1', 'TYR', 'CB', 'ASP', 9.29), ('CE1', 'TYR', 'CG', 'ASP', 7.87), ('CE1', 'TYR', 'OD1', 'ASP', 7.66), ('CE1', 'TYR', 'OD2', 'ASP', 7.2)], [('CE2', 'TYR', 'CB', 'ASP', 11.04), ('CE2', 'TYR', 'CG', 'ASP', 9.64), ('CE2', 'TYR', 'OD1', 'ASP', 9.67), ('CE2', 'TYR', 'OD2', 'ASP', 8.71)], [('CZ', 'TYR', 'CB', 'ASP', 10.53), ('CZ', 'TYR', 'CG', 'ASP', 9.13), ('CZ', 'TYR', 'OD1', 'ASP', 9.01), ('CZ', 'TYR', 'OD2', 'ASP', 8.36)], [('OH', 'TYR', 'CB', 'ASP', 11.46), ('OH', 'TYR', 'CG', 'ASP', 10.11), ('OH', 'TYR', 'OD1', 'ASP', 9.91), ('OH', 'TYR', 'OD2', 'ASP', 9.44)], [('CB', 'TYR', 'CB', 'ASP', 11.65), ('CB', 'TYR', 'CG', 'ASP', 10.35), ('CB', 'TYR', 'OD1', 'ASP', 9.33), ('CB', 'TYR', 'OD2', 'ASP', 10.42)], [('CG', 'TYR', 'CB', 'ASP', 10.25), ('CG', 'TYR', 'CG', 'ASP', 8.93), ('CG', 'TYR', 'OD1', 'ASP', 7.93), ('CG', 'TYR', 'OD2', 'ASP', 9.0)], [('CD1', 'TYR', 'CB', 'ASP', 9.2), ('CD1', 'TYR', 'CG', 'ASP', 7.89), ('CD1', 'TYR', 'OD1', 'ASP', 6.9), ('CD1', 'TYR', 'OD2', 'ASP', 8.0)], [('CD2', 'TYR', 'CB', 'ASP', 10.17), ('CD2', 'TYR', 'CG', 'ASP', 8.86), ('CD2', 'TYR', 'OD1', 'ASP', 7.92), ('CD2', 'TYR', 'OD2', 'ASP', 8.9)], [('CE1', 'TYR', 'CB', 'ASP', 7.89), ('CE1', 'TYR', 'CG', 'ASP', 6.55), ('CE1', 'TYR', 'OD1', 'ASP', 5.59), ('CE1', 'TYR', 'OD2', 'ASP', 6.66)], [('CE2', 'TYR', 'CB', 'ASP', 9.04), ('CE2', 'TYR', 'CG', 'ASP', 7.74), ('CE2', 'TYR', 'OD1', 'ASP', 6.87), ('CE2', 'TYR', 'OD2', 'ASP', 7.77)], [('CZ', 'TYR', 'CB', 'ASP', 7.8), ('CZ', 'TYR', 'CG', 'ASP', 6.46), ('CZ', 'TYR', 'OD1', 'ASP', 5.57), ('CZ', 'TYR', 'OD2', 'ASP', 6.53)], [('OH', 'TYR', 'CB', 'ASP', 6.7), ('OH', 'TYR', 'CG', 'ASP', 5.4), ('OH', 'TYR', 'OD1', 'ASP', 4.69), ('OH', 'TYR', 'OD2', 'ASP', 5.46)]]}
CYS_PHE = { 
	'distances':
		[[8.81, 8.11, 7.35, 8.62, 7.14, 8.43, 7.71], [7.74, 7.21, 6.84, 7.62, 6.93, 7.66, 7.32], [7.89, 6.81, 6.73, 6.43, 6.27, 5.89, 5.78], [6.59, 5.66, 5.4, 5.8, 5.28, 5.65, 5.38]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'PHE', 8.81), ('CB', 'CYS', 'CG', 'PHE', 8.11), ('CB', 'CYS', 'CD1', 'PHE', 7.35), ('CB', 'CYS', 'CD2', 'PHE', 8.62), ('CB', 'CYS', 'CE1', 'PHE', 7.14), ('CB', 'CYS', 'CE2', 'PHE', 8.43), ('CB', 'CYS', 'CZ', 'PHE', 7.71)], [('SG', 'CYS', 'CB', 'PHE', 7.74), ('SG', 'CYS', 'CG', 'PHE', 7.21), ('SG', 'CYS', 'CD1', 'PHE', 6.84), ('SG', 'CYS', 'CD2', 'PHE', 7.62), ('SG', 'CYS', 'CE1', 'PHE', 6.93), ('SG', 'CYS', 'CE2', 'PHE', 7.66), ('SG', 'CYS', 'CZ', 'PHE', 7.32)], [('CB', 'CYS', 'CB', 'PHE', 7.89), ('CB', 'CYS', 'CG', 'PHE', 6.81), ('CB', 'CYS', 'CD1', 'PHE', 6.73), ('CB', 'CYS', 'CD2', 'PHE', 6.43), ('CB', 'CYS', 'CE1', 'PHE', 6.27), ('CB', 'CYS', 'CE2', 'PHE', 5.89), ('CB', 'CYS', 'CZ', 'PHE', 5.78)], [('SG', 'CYS', 'CB', 'PHE', 6.59), ('SG', 'CYS', 'CG', 'PHE', 5.66), ('SG', 'CYS', 'CD1', 'PHE', 5.4), ('SG', 'CYS', 'CD2', 'PHE', 5.8), ('SG', 'CYS', 'CE1', 'PHE', 5.28), ('SG', 'CYS', 'CE2', 'PHE', 5.65), ('SG', 'CYS', 'CZ', 'PHE', 5.38)]]}
TYR_TYR = { 
	'distances':
		[[9.58, 8.54, 7.8, 8.64, 7.1, 8.02, 7.24, 7.05], [8.96, 7.89, 7.44, 7.74, 6.78, 7.1, 6.6, 6.49], [8.15, 6.93, 6.54, 6.59, 5.77, 5.8, 5.33, 5.22], [9.55, 8.63, 8.4, 8.37, 7.91, 7.85, 7.62, 7.59], [7.98, 6.81, 6.81, 6.14, 6.19, 5.37, 5.41, 5.42], [9.44, 8.57, 8.62, 8.07, 8.21, 7.61, 7.69, 7.73], [8.68, 7.71, 7.88, 6.99, 7.45, 6.45, 6.7, 6.78], [8.96, 8.1, 8.55, 7.17, 8.23, 6.73, 7.33, 7.47], [9.58, 8.96, 8.15, 9.55, 7.98, 9.44, 8.68, 8.96], [8.54, 7.89, 6.93, 8.63, 6.81, 8.57, 7.71, 8.1], [7.8, 7.44, 6.54, 8.4, 6.81, 8.62, 7.88, 8.55], [8.64, 7.74, 6.59, 8.37, 6.14, 8.07, 6.99, 7.17], [7.1, 6.78, 5.77, 7.91, 6.19, 8.21, 7.45, 8.23], [8.02, 7.1, 5.8, 7.85, 5.37, 7.61, 6.45, 6.73], [7.24, 6.6, 5.33, 7.62, 5.41, 7.69, 6.7, 7.33], [7.05, 6.49, 5.22, 7.59, 5.42, 7.73, 6.78, 7.47]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TYR', 9.58), ('CB', 'TYR', 'CG', 'TYR', 8.54), ('CB', 'TYR', 'CD1', 'TYR', 7.8), ('CB', 'TYR', 'CD2', 'TYR', 8.64), ('CB', 'TYR', 'CE1', 'TYR', 7.1), ('CB', 'TYR', 'CE2', 'TYR', 8.02), ('CB', 'TYR', 'CZ', 'TYR', 7.24), ('CB', 'TYR', 'OH', 'TYR', 7.05)], [('CG', 'TYR', 'CB', 'TYR', 8.96), ('CG', 'TYR', 'CG', 'TYR', 7.89), ('CG', 'TYR', 'CD1', 'TYR', 7.44), ('CG', 'TYR', 'CD2', 'TYR', 7.74), ('CG', 'TYR', 'CE1', 'TYR', 6.78), ('CG', 'TYR', 'CE2', 'TYR', 7.1), ('CG', 'TYR', 'CZ', 'TYR', 6.6), ('CG', 'TYR', 'OH', 'TYR', 6.49)], [('CD1', 'TYR', 'CB', 'TYR', 8.15), ('CD1', 'TYR', 'CG', 'TYR', 6.93), ('CD1', 'TYR', 'CD1', 'TYR', 6.54), ('CD1', 'TYR', 'CD2', 'TYR', 6.59), ('CD1', 'TYR', 'CE1', 'TYR', 5.77), ('CD1', 'TYR', 'CE2', 'TYR', 5.8), ('CD1', 'TYR', 'CZ', 'TYR', 5.33), ('CD1', 'TYR', 'OH', 'TYR', 5.22)], [('CD2', 'TYR', 'CB', 'TYR', 9.55), ('CD2', 'TYR', 'CG', 'TYR', 8.63), ('CD2', 'TYR', 'CD1', 'TYR', 8.4), ('CD2', 'TYR', 'CD2', 'TYR', 8.37), ('CD2', 'TYR', 'CE1', 'TYR', 7.91), ('CD2', 'TYR', 'CE2', 'TYR', 7.85), ('CD2', 'TYR', 'CZ', 'TYR', 7.62), ('CD2', 'TYR', 'OH', 'TYR', 7.59)], [('CE1', 'TYR', 'CB', 'TYR', 7.98), ('CE1', 'TYR', 'CG', 'TYR', 6.81), ('CE1', 'TYR', 'CD1', 'TYR', 6.81), ('CE1', 'TYR', 'CD2', 'TYR', 6.14), ('CE1', 'TYR', 'CE1', 'TYR', 6.19), ('CE1', 'TYR', 'CE2', 'TYR', 5.37), ('CE1', 'TYR', 'CZ', 'TYR', 5.41), ('CE1', 'TYR', 'OH', 'TYR', 5.42)], [('CE2', 'TYR', 'CB', 'TYR', 9.44), ('CE2', 'TYR', 'CG', 'TYR', 8.57), ('CE2', 'TYR', 'CD1', 'TYR', 8.62), ('CE2', 'TYR', 'CD2', 'TYR', 8.07), ('CE2', 'TYR', 'CE1', 'TYR', 8.21), ('CE2', 'TYR', 'CE2', 'TYR', 7.61), ('CE2', 'TYR', 'CZ', 'TYR', 7.69), ('CE2', 'TYR', 'OH', 'TYR', 7.73)], [('CZ', 'TYR', 'CB', 'TYR', 8.68), ('CZ', 'TYR', 'CG', 'TYR', 7.71), ('CZ', 'TYR', 'CD1', 'TYR', 7.88), ('CZ', 'TYR', 'CD2', 'TYR', 6.99), ('CZ', 'TYR', 'CE1', 'TYR', 7.45), ('CZ', 'TYR', 'CE2', 'TYR', 6.45), ('CZ', 'TYR', 'CZ', 'TYR', 6.7), ('CZ', 'TYR', 'OH', 'TYR', 6.78)], [('OH', 'TYR', 'CB', 'TYR', 8.96), ('OH', 'TYR', 'CG', 'TYR', 8.1), ('OH', 'TYR', 'CD1', 'TYR', 8.55), ('OH', 'TYR', 'CD2', 'TYR', 7.17), ('OH', 'TYR', 'CE1', 'TYR', 8.23), ('OH', 'TYR', 'CE2', 'TYR', 6.73), ('OH', 'TYR', 'CZ', 'TYR', 7.33), ('OH', 'TYR', 'OH', 'TYR', 7.47)], [('CB', 'TYR', 'CB', 'TYR', 9.58), ('CB', 'TYR', 'CG', 'TYR', 8.96), ('CB', 'TYR', 'CD1', 'TYR', 8.15), ('CB', 'TYR', 'CD2', 'TYR', 9.55), ('CB', 'TYR', 'CE1', 'TYR', 7.98), ('CB', 'TYR', 'CE2', 'TYR', 9.44), ('CB', 'TYR', 'CZ', 'TYR', 8.68), ('CB', 'TYR', 'OH', 'TYR', 8.96)], [('CG', 'TYR', 'CB', 'TYR', 8.54), ('CG', 'TYR', 'CG', 'TYR', 7.89), ('CG', 'TYR', 'CD1', 'TYR', 6.93), ('CG', 'TYR', 'CD2', 'TYR', 8.63), ('CG', 'TYR', 'CE1', 'TYR', 6.81), ('CG', 'TYR', 'CE2', 'TYR', 8.57), ('CG', 'TYR', 'CZ', 'TYR', 7.71), ('CG', 'TYR', 'OH', 'TYR', 8.1)], [('CD1', 'TYR', 'CB', 'TYR', 7.8), ('CD1', 'TYR', 'CG', 'TYR', 7.44), ('CD1', 'TYR', 'CD1', 'TYR', 6.54), ('CD1', 'TYR', 'CD2', 'TYR', 8.4), ('CD1', 'TYR', 'CE1', 'TYR', 6.81), ('CD1', 'TYR', 'CE2', 'TYR', 8.62), ('CD1', 'TYR', 'CZ', 'TYR', 7.88), ('CD1', 'TYR', 'OH', 'TYR', 8.55)], [('CD2', 'TYR', 'CB', 'TYR', 8.64), ('CD2', 'TYR', 'CG', 'TYR', 7.74), ('CD2', 'TYR', 'CD1', 'TYR', 6.59), ('CD2', 'TYR', 'CD2', 'TYR', 8.37), ('CD2', 'TYR', 'CE1', 'TYR', 6.14), ('CD2', 'TYR', 'CE2', 'TYR', 8.07), ('CD2', 'TYR', 'CZ', 'TYR', 6.99), ('CD2', 'TYR', 'OH', 'TYR', 7.17)], [('CE1', 'TYR', 'CB', 'TYR', 7.1), ('CE1', 'TYR', 'CG', 'TYR', 6.78), ('CE1', 'TYR', 'CD1', 'TYR', 5.77), ('CE1', 'TYR', 'CD2', 'TYR', 7.91), ('CE1', 'TYR', 'CE1', 'TYR', 6.19), ('CE1', 'TYR', 'CE2', 'TYR', 8.21), ('CE1', 'TYR', 'CZ', 'TYR', 7.45), ('CE1', 'TYR', 'OH', 'TYR', 8.23)], [('CE2', 'TYR', 'CB', 'TYR', 8.02), ('CE2', 'TYR', 'CG', 'TYR', 7.1), ('CE2', 'TYR', 'CD1', 'TYR', 5.8), ('CE2', 'TYR', 'CD2', 'TYR', 7.85), ('CE2', 'TYR', 'CE1', 'TYR', 5.37), ('CE2', 'TYR', 'CE2', 'TYR', 7.61), ('CE2', 'TYR', 'CZ', 'TYR', 6.45), ('CE2', 'TYR', 'OH', 'TYR', 6.73)], [('CZ', 'TYR', 'CB', 'TYR', 7.24), ('CZ', 'TYR', 'CG', 'TYR', 6.6), ('CZ', 'TYR', 'CD1', 'TYR', 5.33), ('CZ', 'TYR', 'CD2', 'TYR', 7.62), ('CZ', 'TYR', 'CE1', 'TYR', 5.41), ('CZ', 'TYR', 'CE2', 'TYR', 7.69), ('CZ', 'TYR', 'CZ', 'TYR', 6.7), ('CZ', 'TYR', 'OH', 'TYR', 7.33)], [('OH', 'TYR', 'CB', 'TYR', 7.05), ('OH', 'TYR', 'CG', 'TYR', 6.49), ('OH', 'TYR', 'CD1', 'TYR', 5.22), ('OH', 'TYR', 'CD2', 'TYR', 7.59), ('OH', 'TYR', 'CE1', 'TYR', 5.42), ('OH', 'TYR', 'CE2', 'TYR', 7.73), ('OH', 'TYR', 'CZ', 'TYR', 6.78), ('OH', 'TYR', 'OH', 'TYR', 7.47)]]}
PHE_CYSI = { 
	'distances':
		[[7.89, 6.59], [6.81, 5.66], [6.73, 5.4], [6.43, 5.8], [6.27, 5.28], [5.89, 5.65], [5.78, 5.38]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'CYSI', 7.89), ('CB', 'PHE', 'SG', 'CYSI', 6.59)], [('CG', 'PHE', 'CB', 'CYSI', 6.81), ('CG', 'PHE', 'SG', 'CYSI', 5.66)], [('CD1', 'PHE', 'CB', 'CYSI', 6.73), ('CD1', 'PHE', 'SG', 'CYSI', 5.4)], [('CD2', 'PHE', 'CB', 'CYSI', 6.43), ('CD2', 'PHE', 'SG', 'CYSI', 5.8)], [('CE1', 'PHE', 'CB', 'CYSI', 6.27), ('CE1', 'PHE', 'SG', 'CYSI', 5.28)], [('CE2', 'PHE', 'CB', 'CYSI', 5.89), ('CE2', 'PHE', 'SG', 'CYSI', 5.65)], [('CZ', 'PHE', 'CB', 'CYSI', 5.78), ('CZ', 'PHE', 'SG', 'CYSI', 5.38)]]}
PHE_ASP = { 
	'distances':
		[[6.92, 5.95, 6.37, 5.25], [7.18, 6.51, 6.83, 6.16], [6.38, 6.02, 6.3, 6.04], [8.54, 7.9, 8.17, 7.51], [7.2, 7.1, 7.29, 7.3], [9.12, 8.69, 8.89, 8.5], [8.55, 8.36, 8.52, 8.41]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ASP', 6.92), ('CB', 'PHE', 'CG', 'ASP', 5.95), ('CB', 'PHE', 'OD1', 'ASP', 6.37), ('CB', 'PHE', 'OD2', 'ASP', 5.25)], [('CG', 'PHE', 'CB', 'ASP', 7.18), ('CG', 'PHE', 'CG', 'ASP', 6.51), ('CG', 'PHE', 'OD1', 'ASP', 6.83), ('CG', 'PHE', 'OD2', 'ASP', 6.16)], [('CD1', 'PHE', 'CB', 'ASP', 6.38), ('CD1', 'PHE', 'CG', 'ASP', 6.02), ('CD1', 'PHE', 'OD1', 'ASP', 6.3), ('CD1', 'PHE', 'OD2', 'ASP', 6.04)], [('CD2', 'PHE', 'CB', 'ASP', 8.54), ('CD2', 'PHE', 'CG', 'ASP', 7.9), ('CD2', 'PHE', 'OD1', 'ASP', 8.17), ('CD2', 'PHE', 'OD2', 'ASP', 7.51)], [('CE1', 'PHE', 'CB', 'ASP', 7.2), ('CE1', 'PHE', 'CG', 'ASP', 7.1), ('CE1', 'PHE', 'OD1', 'ASP', 7.29), ('CE1', 'PHE', 'OD2', 'ASP', 7.3)], [('CE2', 'PHE', 'CB', 'ASP', 9.12), ('CE2', 'PHE', 'CG', 'ASP', 8.69), ('CE2', 'PHE', 'OD1', 'ASP', 8.89), ('CE2', 'PHE', 'OD2', 'ASP', 8.5)], [('CZ', 'PHE', 'CB', 'ASP', 8.55), ('CZ', 'PHE', 'CG', 'ASP', 8.36), ('CZ', 'PHE', 'OD1', 'ASP', 8.52), ('CZ', 'PHE', 'OD2', 'ASP', 8.41)]]}
CYS_TYR = { 
	'distances':
		[[11.7, 11.03, 9.68, 11.95, 9.35, 11.72, 10.47, 10.52], [10.44, 9.59, 8.21, 10.39, 7.71, 10.05, 8.76, 8.74], [9.47, 8.36, 8.38, 7.62, 7.73, 6.84, 6.9, 6.65], [8.31, 7.12, 7.33, 6.15, 6.7, 5.27, 5.62, 5.51], [11.61, 10.52, 9.24, 10.96, 8.37, 10.29, 8.98, 8.54], [10.23, 9.3, 7.99, 9.96, 7.38, 9.54, 8.28, 8.19], [10.66, 9.51, 9.9, 8.24, 9.2, 7.31, 7.88, 7.43], [9.76, 8.46, 8.58, 7.34, 7.7, 6.19, 6.41, 5.77]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TYR', 11.7), ('CB', 'CYS', 'CG', 'TYR', 11.03), ('CB', 'CYS', 'CD1', 'TYR', 9.68), ('CB', 'CYS', 'CD2', 'TYR', 11.95), ('CB', 'CYS', 'CE1', 'TYR', 9.35), ('CB', 'CYS', 'CE2', 'TYR', 11.72), ('CB', 'CYS', 'CZ', 'TYR', 10.47), ('CB', 'CYS', 'OH', 'TYR', 10.52)], [('SG', 'CYS', 'CB', 'TYR', 10.44), ('SG', 'CYS', 'CG', 'TYR', 9.59), ('SG', 'CYS', 'CD1', 'TYR', 8.21), ('SG', 'CYS', 'CD2', 'TYR', 10.39), ('SG', 'CYS', 'CE1', 'TYR', 7.71), ('SG', 'CYS', 'CE2', 'TYR', 10.05), ('SG', 'CYS', 'CZ', 'TYR', 8.76), ('SG', 'CYS', 'OH', 'TYR', 8.74)], [('CB', 'CYS', 'CB', 'TYR', 9.47), ('CB', 'CYS', 'CG', 'TYR', 8.36), ('CB', 'CYS', 'CD1', 'TYR', 8.38), ('CB', 'CYS', 'CD2', 'TYR', 7.62), ('CB', 'CYS', 'CE1', 'TYR', 7.73), ('CB', 'CYS', 'CE2', 'TYR', 6.84), ('CB', 'CYS', 'CZ', 'TYR', 6.9), ('CB', 'CYS', 'OH', 'TYR', 6.65)], [('SG', 'CYS', 'CB', 'TYR', 8.31), ('SG', 'CYS', 'CG', 'TYR', 7.12), ('SG', 'CYS', 'CD1', 'TYR', 7.33), ('SG', 'CYS', 'CD2', 'TYR', 6.15), ('SG', 'CYS', 'CE1', 'TYR', 6.7), ('SG', 'CYS', 'CE2', 'TYR', 5.27), ('SG', 'CYS', 'CZ', 'TYR', 5.62), ('SG', 'CYS', 'OH', 'TYR', 5.51)], [('CB', 'CYS', 'CB', 'TYR', 11.61), ('CB', 'CYS', 'CG', 'TYR', 10.52), ('CB', 'CYS', 'CD1', 'TYR', 9.24), ('CB', 'CYS', 'CD2', 'TYR', 10.96), ('CB', 'CYS', 'CE1', 'TYR', 8.37), ('CB', 'CYS', 'CE2', 'TYR', 10.29), ('CB', 'CYS', 'CZ', 'TYR', 8.98), ('CB', 'CYS', 'OH', 'TYR', 8.54)], [('SG', 'CYS', 'CB', 'TYR', 10.23), ('SG', 'CYS', 'CG', 'TYR', 9.3), ('SG', 'CYS', 'CD1', 'TYR', 7.99), ('SG', 'CYS', 'CD2', 'TYR', 9.96), ('SG', 'CYS', 'CE1', 'TYR', 7.38), ('SG', 'CYS', 'CE2', 'TYR', 9.54), ('SG', 'CYS', 'CZ', 'TYR', 8.28), ('SG', 'CYS', 'OH', 'TYR', 8.19)], [('CB', 'CYS', 'CB', 'TYR', 10.66), ('CB', 'CYS', 'CG', 'TYR', 9.51), ('CB', 'CYS', 'CD1', 'TYR', 9.9), ('CB', 'CYS', 'CD2', 'TYR', 8.24), ('CB', 'CYS', 'CE1', 'TYR', 9.2), ('CB', 'CYS', 'CE2', 'TYR', 7.31), ('CB', 'CYS', 'CZ', 'TYR', 7.88), ('CB', 'CYS', 'OH', 'TYR', 7.43)], [('SG', 'CYS', 'CB', 'TYR', 9.76), ('SG', 'CYS', 'CG', 'TYR', 8.46), ('SG', 'CYS', 'CD1', 'TYR', 8.58), ('SG', 'CYS', 'CD2', 'TYR', 7.34), ('SG', 'CYS', 'CE1', 'TYR', 7.7), ('SG', 'CYS', 'CE2', 'TYR', 6.19), ('SG', 'CYS', 'CZ', 'TYR', 6.41), ('SG', 'CYS', 'OH', 'TYR', 5.77)]]}
CYS_ASP = { 
	'distances':
		[[8.71, 8.33, 7.43, 9.08], [8.78, 8.03, 7.15, 8.51], [10.31, 9.69, 9.22, 9.9], [8.57, 7.91, 7.41, 8.18]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 8.71), ('CB', 'CYS', 'CG', 'ASP', 8.33), ('CB', 'CYS', 'OD1', 'ASP', 7.43), ('CB', 'CYS', 'OD2', 'ASP', 9.08)], [('SG', 'CYS', 'CB', 'ASP', 8.78), ('SG', 'CYS', 'CG', 'ASP', 8.03), ('SG', 'CYS', 'OD1', 'ASP', 7.15), ('SG', 'CYS', 'OD2', 'ASP', 8.51)], [('CB', 'CYS', 'CB', 'ASP', 10.31), ('CB', 'CYS', 'CG', 'ASP', 9.69), ('CB', 'CYS', 'OD1', 'ASP', 9.22), ('CB', 'CYS', 'OD2', 'ASP', 9.9)], [('SG', 'CYS', 'CB', 'ASP', 8.57), ('SG', 'CYS', 'CG', 'ASP', 7.91), ('SG', 'CYS', 'OD1', 'ASP', 7.41), ('SG', 'CYS', 'OD2', 'ASP', 8.18)]]}
ASP_CYSI = { 
	'distances':
		[[10.31, 8.57], [9.69, 7.91], [9.22, 7.41], [9.9, 8.18]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYSI', 10.31), ('CB', 'ASP', 'SG', 'CYSI', 8.57)], [('CG', 'ASP', 'CB', 'CYSI', 9.69), ('CG', 'ASP', 'SG', 'CYSI', 7.91)], [('OD1', 'ASP', 'CB', 'CYSI', 9.22), ('OD1', 'ASP', 'SG', 'CYSI', 7.41)], [('OD2', 'ASP', 'CB', 'CYSI', 9.9), ('OD2', 'ASP', 'SG', 'CYSI', 8.18)]]}
TYR_CYSI = { 
	'distances':
		[[11.61, 10.23], [10.52, 9.3], [9.24, 7.99], [10.96, 9.96], [8.37, 7.38], [10.29, 9.54], [8.98, 8.28], [8.54, 8.19], [10.66, 9.76], [9.51, 8.46], [9.9, 8.58], [8.24, 7.34], [9.2, 7.7], [7.31, 6.19], [7.88, 6.41], [7.43, 5.77]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'CYSI', 11.61), ('CB', 'TYR', 'SG', 'CYSI', 10.23)], [('CG', 'TYR', 'CB', 'CYSI', 10.52), ('CG', 'TYR', 'SG', 'CYSI', 9.3)], [('CD1', 'TYR', 'CB', 'CYSI', 9.24), ('CD1', 'TYR', 'SG', 'CYSI', 7.99)], [('CD2', 'TYR', 'CB', 'CYSI', 10.96), ('CD2', 'TYR', 'SG', 'CYSI', 9.96)], [('CE1', 'TYR', 'CB', 'CYSI', 8.37), ('CE1', 'TYR', 'SG', 'CYSI', 7.38)], [('CE2', 'TYR', 'CB', 'CYSI', 10.29), ('CE2', 'TYR', 'SG', 'CYSI', 9.54)], [('CZ', 'TYR', 'CB', 'CYSI', 8.98), ('CZ', 'TYR', 'SG', 'CYSI', 8.28)], [('OH', 'TYR', 'CB', 'CYSI', 8.54), ('OH', 'TYR', 'SG', 'CYSI', 8.19)], [('CB', 'TYR', 'CB', 'CYSI', 10.66), ('CB', 'TYR', 'SG', 'CYSI', 9.76)], [('CG', 'TYR', 'CB', 'CYSI', 9.51), ('CG', 'TYR', 'SG', 'CYSI', 8.46)], [('CD1', 'TYR', 'CB', 'CYSI', 9.9), ('CD1', 'TYR', 'SG', 'CYSI', 8.58)], [('CD2', 'TYR', 'CB', 'CYSI', 8.24), ('CD2', 'TYR', 'SG', 'CYSI', 7.34)], [('CE1', 'TYR', 'CB', 'CYSI', 9.2), ('CE1', 'TYR', 'SG', 'CYSI', 7.7)], [('CE2', 'TYR', 'CB', 'CYSI', 7.31), ('CE2', 'TYR', 'SG', 'CYSI', 6.19)], [('CZ', 'TYR', 'CB', 'CYSI', 7.88), ('CZ', 'TYR', 'SG', 'CYSI', 6.41)], [('OH', 'TYR', 'CB', 'CYSI', 7.43), ('OH', 'TYR', 'SG', 'CYSI', 5.77)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_CYS, d, 'A_1l6p_1_8_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PHE_TYR, d, 'A_1l6p_1_8_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ASP, d, 'A_1l6p_1_8_1_8')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_PHE, d, 'A_1l6p_1_8_1_8')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TYR_TYR, d, 'A_1l6p_1_8_1_8')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(PHE_CYSI, d, 'A_1l6p_1_8_1_8')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(PHE_ASP, d, 'A_1l6p_1_8_1_8')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(CYS_TYR, d, 'A_1l6p_1_8_1_8')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(CYS_ASP, d, 'A_1l6p_1_8_1_8')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASP_CYSI, d, 'A_1l6p_1_8_1_8')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(TYR_CYSI, d, 'A_1l6p_1_8_1_8')
	if match11 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_CYS' :  match1,
		'PHE_TYR' :  match2,
		'TYR_ASP' :  match3,
		'CYS_PHE' :  match4,
		'TYR_TYR' :  match5,
		'PHE_CYSI' :  match6,
		'PHE_ASP' :  match7,
		'CYS_TYR' :  match8,
		'CYS_ASP' :  match9,
		'ASP_CYSI' :  match10,
		'TYR_CYSI' :  match11}