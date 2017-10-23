'''
FUNC:P_1fva_1_8_4_6
PDB:1fva
EC:1.8.4.6
RESI:cys,tyr,glu,tyr,cys
LOCI:a-72,103,115,155,218;
'''
import motifFunctions as cmd
CYS_CYS = { 
	'distances':
		[[9.28, 10.65], [9.33, 10.64], [9.28, 9.33], [10.65, 10.64]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 9.28), ('CB', 'CYS', 'SG', 'CYS', 10.65)], [('SG', 'CYS', 'CB', 'CYS', 9.33), ('SG', 'CYS', 'SG', 'CYS', 10.64)], [('CB', 'CYS', 'CB', 'CYS', 9.28), ('CB', 'CYS', 'SG', 'CYS', 9.33)], [('SG', 'CYS', 'CB', 'CYS', 10.65), ('SG', 'CYS', 'SG', 'CYS', 10.64)]]}
CYS_TYRI = { 
	'distances':
		[[15.28, 15.06, 16.07, 14.01, 16.09, 14.02, 15.11, 15.35], [16.55, 16.31, 17.23, 15.3, 17.21, 15.26, 16.26, 16.43]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TYRI', 15.28), ('CB', 'CYS', 'CG', 'TYRI', 15.06), ('CB', 'CYS', 'CD1', 'TYRI', 16.07), ('CB', 'CYS', 'CD2', 'TYRI', 14.01), ('CB', 'CYS', 'CE1', 'TYRI', 16.09), ('CB', 'CYS', 'CE2', 'TYRI', 14.02), ('CB', 'CYS', 'CZ', 'TYRI', 15.11), ('CB', 'CYS', 'OH', 'TYRI', 15.35)], [('SG', 'CYS', 'CB', 'TYRI', 16.55), ('SG', 'CYS', 'CG', 'TYRI', 16.31), ('SG', 'CYS', 'CD1', 'TYRI', 17.23), ('SG', 'CYS', 'CD2', 'TYRI', 15.3), ('SG', 'CYS', 'CE1', 'TYRI', 17.21), ('SG', 'CYS', 'CE2', 'TYRI', 15.26), ('SG', 'CYS', 'CZ', 'TYRI', 16.26), ('SG', 'CYS', 'OH', 'TYRI', 16.43)]]}
TYR_GLU = { 
	'distances':
		[[11.41, 10.2, 10.0, 10.76, 9.22], [10.58, 9.31, 8.9, 9.6, 8.03], [9.19, 7.92, 7.54, 8.26, 6.73], [11.38, 10.06, 9.43, 10.03, 8.46], [8.68, 7.38, 6.69, 7.31, 5.78], [11.03, 9.71, 8.87, 9.34, 7.84], [9.71, 8.4, 7.49, 7.96, 6.49], [9.63, 8.36, 7.22, 7.5, 6.22], [8.28, 8.22, 8.15, 8.21, 8.42], [7.95, 7.56, 7.27, 7.41, 7.3], [8.86, 8.22, 7.9, 8.22, 7.63], [7.11, 6.69, 6.15, 6.13, 6.26], [9.06, 8.16, 7.64, 8.03, 7.08], [7.35, 6.59, 5.73, 5.81, 5.48], [8.35, 7.38, 6.6, 6.91, 5.99], [8.96, 7.8, 6.86, 7.23, 5.96]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 11.41), ('CB', 'TYR', 'CG', 'GLU', 10.2), ('CB', 'TYR', 'CD', 'GLU', 10.0), ('CB', 'TYR', 'OE1', 'GLU', 10.76), ('CB', 'TYR', 'OE2', 'GLU', 9.22)], [('CG', 'TYR', 'CB', 'GLU', 10.58), ('CG', 'TYR', 'CG', 'GLU', 9.31), ('CG', 'TYR', 'CD', 'GLU', 8.9), ('CG', 'TYR', 'OE1', 'GLU', 9.6), ('CG', 'TYR', 'OE2', 'GLU', 8.03)], [('CD1', 'TYR', 'CB', 'GLU', 9.19), ('CD1', 'TYR', 'CG', 'GLU', 7.92), ('CD1', 'TYR', 'CD', 'GLU', 7.54), ('CD1', 'TYR', 'OE1', 'GLU', 8.26), ('CD1', 'TYR', 'OE2', 'GLU', 6.73)], [('CD2', 'TYR', 'CB', 'GLU', 11.38), ('CD2', 'TYR', 'CG', 'GLU', 10.06), ('CD2', 'TYR', 'CD', 'GLU', 9.43), ('CD2', 'TYR', 'OE1', 'GLU', 10.03), ('CD2', 'TYR', 'OE2', 'GLU', 8.46)], [('CE1', 'TYR', 'CB', 'GLU', 8.68), ('CE1', 'TYR', 'CG', 'GLU', 7.38), ('CE1', 'TYR', 'CD', 'GLU', 6.69), ('CE1', 'TYR', 'OE1', 'GLU', 7.31), ('CE1', 'TYR', 'OE2', 'GLU', 5.78)], [('CE2', 'TYR', 'CB', 'GLU', 11.03), ('CE2', 'TYR', 'CG', 'GLU', 9.71), ('CE2', 'TYR', 'CD', 'GLU', 8.87), ('CE2', 'TYR', 'OE1', 'GLU', 9.34), ('CE2', 'TYR', 'OE2', 'GLU', 7.84)], [('CZ', 'TYR', 'CB', 'GLU', 9.71), ('CZ', 'TYR', 'CG', 'GLU', 8.4), ('CZ', 'TYR', 'CD', 'GLU', 7.49), ('CZ', 'TYR', 'OE1', 'GLU', 7.96), ('CZ', 'TYR', 'OE2', 'GLU', 6.49)], [('OH', 'TYR', 'CB', 'GLU', 9.63), ('OH', 'TYR', 'CG', 'GLU', 8.36), ('OH', 'TYR', 'CD', 'GLU', 7.22), ('OH', 'TYR', 'OE1', 'GLU', 7.5), ('OH', 'TYR', 'OE2', 'GLU', 6.22)], [('CB', 'TYR', 'CB', 'GLU', 8.28), ('CB', 'TYR', 'CG', 'GLU', 8.22), ('CB', 'TYR', 'CD', 'GLU', 8.15), ('CB', 'TYR', 'OE1', 'GLU', 8.21), ('CB', 'TYR', 'OE2', 'GLU', 8.42)], [('CG', 'TYR', 'CB', 'GLU', 7.95), ('CG', 'TYR', 'CG', 'GLU', 7.56), ('CG', 'TYR', 'CD', 'GLU', 7.27), ('CG', 'TYR', 'OE1', 'GLU', 7.41), ('CG', 'TYR', 'OE2', 'GLU', 7.3)], [('CD1', 'TYR', 'CB', 'GLU', 8.86), ('CD1', 'TYR', 'CG', 'GLU', 8.22), ('CD1', 'TYR', 'CD', 'GLU', 7.9), ('CD1', 'TYR', 'OE1', 'GLU', 8.22), ('CD1', 'TYR', 'OE2', 'GLU', 7.63)], [('CD2', 'TYR', 'CB', 'GLU', 7.11), ('CD2', 'TYR', 'CG', 'GLU', 6.69), ('CD2', 'TYR', 'CD', 'GLU', 6.15), ('CD2', 'TYR', 'OE1', 'GLU', 6.13), ('CD2', 'TYR', 'OE2', 'GLU', 6.26)], [('CE1', 'TYR', 'CB', 'GLU', 9.06), ('CE1', 'TYR', 'CG', 'GLU', 8.16), ('CE1', 'TYR', 'CD', 'GLU', 7.64), ('CE1', 'TYR', 'OE1', 'GLU', 8.03), ('CE1', 'TYR', 'OE2', 'GLU', 7.08)], [('CE2', 'TYR', 'CB', 'GLU', 7.35), ('CE2', 'TYR', 'CG', 'GLU', 6.59), ('CE2', 'TYR', 'CD', 'GLU', 5.73), ('CE2', 'TYR', 'OE1', 'GLU', 5.81), ('CE2', 'TYR', 'OE2', 'GLU', 5.48)], [('CZ', 'TYR', 'CB', 'GLU', 8.35), ('CZ', 'TYR', 'CG', 'GLU', 7.38), ('CZ', 'TYR', 'CD', 'GLU', 6.6), ('CZ', 'TYR', 'OE1', 'GLU', 6.91), ('CZ', 'TYR', 'OE2', 'GLU', 5.99)], [('OH', 'TYR', 'CB', 'GLU', 8.96), ('OH', 'TYR', 'CG', 'GLU', 7.8), ('OH', 'TYR', 'CD', 'GLU', 6.86), ('OH', 'TYR', 'OE1', 'GLU', 7.23), ('OH', 'TYR', 'OE2', 'GLU', 5.96)]]}
TYR_TYR = { 
	'distances':
		[[15.37, 14.16, 14.02, 13.33, 13.07, 12.3, 12.15, 11.33], [14.23, 12.97, 12.84, 12.08, 11.84, 10.99, 10.85, 9.99], [13.01, 11.8, 11.77, 10.88, 10.86, 9.86, 9.85, 9.12], [14.52, 13.18, 12.97, 12.28, 11.85, 11.07, 10.84, 9.81], [12.05, 10.79, 10.78, 9.8, 9.84, 8.7, 8.73, 7.95], [13.73, 12.34, 12.13, 11.4, 10.98, 10.13, 9.89, 8.8], [12.45, 11.09, 10.98, 10.1, 9.9, 8.86, 8.75, 7.76], [11.75, 10.36, 10.27, 9.32, 9.16, 8.02, 7.93, 6.9], [15.37, 14.23, 13.01, 14.52, 12.05, 13.73, 12.45, 11.75], [14.16, 12.97, 11.8, 13.18, 10.79, 12.34, 11.09, 10.36], [14.02, 12.84, 11.77, 12.97, 10.78, 12.13, 10.98, 10.27], [13.33, 12.08, 10.88, 12.28, 9.8, 11.4, 10.1, 9.32], [13.07, 11.84, 10.86, 11.85, 9.84, 10.98, 9.9, 9.16], [12.3, 10.99, 9.86, 11.07, 8.7, 10.13, 8.86, 8.02], [12.15, 10.85, 9.85, 10.84, 8.73, 9.89, 8.75, 7.93], [11.33, 9.99, 9.12, 9.81, 7.95, 8.8, 7.76, 6.9]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TYR', 15.37), ('CB', 'TYR', 'CG', 'TYR', 14.16), ('CB', 'TYR', 'CD1', 'TYR', 14.02), ('CB', 'TYR', 'CD2', 'TYR', 13.33), ('CB', 'TYR', 'CE1', 'TYR', 13.07), ('CB', 'TYR', 'CE2', 'TYR', 12.3), ('CB', 'TYR', 'CZ', 'TYR', 12.15), ('CB', 'TYR', 'OH', 'TYR', 11.33)], [('CG', 'TYR', 'CB', 'TYR', 14.23), ('CG', 'TYR', 'CG', 'TYR', 12.97), ('CG', 'TYR', 'CD1', 'TYR', 12.84), ('CG', 'TYR', 'CD2', 'TYR', 12.08), ('CG', 'TYR', 'CE1', 'TYR', 11.84), ('CG', 'TYR', 'CE2', 'TYR', 10.99), ('CG', 'TYR', 'CZ', 'TYR', 10.85), ('CG', 'TYR', 'OH', 'TYR', 9.99)], [('CD1', 'TYR', 'CB', 'TYR', 13.01), ('CD1', 'TYR', 'CG', 'TYR', 11.8), ('CD1', 'TYR', 'CD1', 'TYR', 11.77), ('CD1', 'TYR', 'CD2', 'TYR', 10.88), ('CD1', 'TYR', 'CE1', 'TYR', 10.86), ('CD1', 'TYR', 'CE2', 'TYR', 9.86), ('CD1', 'TYR', 'CZ', 'TYR', 9.85), ('CD1', 'TYR', 'OH', 'TYR', 9.12)], [('CD2', 'TYR', 'CB', 'TYR', 14.52), ('CD2', 'TYR', 'CG', 'TYR', 13.18), ('CD2', 'TYR', 'CD1', 'TYR', 12.97), ('CD2', 'TYR', 'CD2', 'TYR', 12.28), ('CD2', 'TYR', 'CE1', 'TYR', 11.85), ('CD2', 'TYR', 'CE2', 'TYR', 11.07), ('CD2', 'TYR', 'CZ', 'TYR', 10.84), ('CD2', 'TYR', 'OH', 'TYR', 9.81)], [('CE1', 'TYR', 'CB', 'TYR', 12.05), ('CE1', 'TYR', 'CG', 'TYR', 10.79), ('CE1', 'TYR', 'CD1', 'TYR', 10.78), ('CE1', 'TYR', 'CD2', 'TYR', 9.8), ('CE1', 'TYR', 'CE1', 'TYR', 9.84), ('CE1', 'TYR', 'CE2', 'TYR', 8.7), ('CE1', 'TYR', 'CZ', 'TYR', 8.73), ('CE1', 'TYR', 'OH', 'TYR', 7.95)], [('CE2', 'TYR', 'CB', 'TYR', 13.73), ('CE2', 'TYR', 'CG', 'TYR', 12.34), ('CE2', 'TYR', 'CD1', 'TYR', 12.13), ('CE2', 'TYR', 'CD2', 'TYR', 11.4), ('CE2', 'TYR', 'CE1', 'TYR', 10.98), ('CE2', 'TYR', 'CE2', 'TYR', 10.13), ('CE2', 'TYR', 'CZ', 'TYR', 9.89), ('CE2', 'TYR', 'OH', 'TYR', 8.8)], [('CZ', 'TYR', 'CB', 'TYR', 12.45), ('CZ', 'TYR', 'CG', 'TYR', 11.09), ('CZ', 'TYR', 'CD1', 'TYR', 10.98), ('CZ', 'TYR', 'CD2', 'TYR', 10.1), ('CZ', 'TYR', 'CE1', 'TYR', 9.9), ('CZ', 'TYR', 'CE2', 'TYR', 8.86), ('CZ', 'TYR', 'CZ', 'TYR', 8.75), ('CZ', 'TYR', 'OH', 'TYR', 7.76)], [('OH', 'TYR', 'CB', 'TYR', 11.75), ('OH', 'TYR', 'CG', 'TYR', 10.36), ('OH', 'TYR', 'CD1', 'TYR', 10.27), ('OH', 'TYR', 'CD2', 'TYR', 9.32), ('OH', 'TYR', 'CE1', 'TYR', 9.16), ('OH', 'TYR', 'CE2', 'TYR', 8.02), ('OH', 'TYR', 'CZ', 'TYR', 7.93), ('OH', 'TYR', 'OH', 'TYR', 6.9)], [('CB', 'TYR', 'CB', 'TYR', 15.37), ('CB', 'TYR', 'CG', 'TYR', 14.23), ('CB', 'TYR', 'CD1', 'TYR', 13.01), ('CB', 'TYR', 'CD2', 'TYR', 14.52), ('CB', 'TYR', 'CE1', 'TYR', 12.05), ('CB', 'TYR', 'CE2', 'TYR', 13.73), ('CB', 'TYR', 'CZ', 'TYR', 12.45), ('CB', 'TYR', 'OH', 'TYR', 11.75)], [('CG', 'TYR', 'CB', 'TYR', 14.16), ('CG', 'TYR', 'CG', 'TYR', 12.97), ('CG', 'TYR', 'CD1', 'TYR', 11.8), ('CG', 'TYR', 'CD2', 'TYR', 13.18), ('CG', 'TYR', 'CE1', 'TYR', 10.79), ('CG', 'TYR', 'CE2', 'TYR', 12.34), ('CG', 'TYR', 'CZ', 'TYR', 11.09), ('CG', 'TYR', 'OH', 'TYR', 10.36)], [('CD1', 'TYR', 'CB', 'TYR', 14.02), ('CD1', 'TYR', 'CG', 'TYR', 12.84), ('CD1', 'TYR', 'CD1', 'TYR', 11.77), ('CD1', 'TYR', 'CD2', 'TYR', 12.97), ('CD1', 'TYR', 'CE1', 'TYR', 10.78), ('CD1', 'TYR', 'CE2', 'TYR', 12.13), ('CD1', 'TYR', 'CZ', 'TYR', 10.98), ('CD1', 'TYR', 'OH', 'TYR', 10.27)], [('CD2', 'TYR', 'CB', 'TYR', 13.33), ('CD2', 'TYR', 'CG', 'TYR', 12.08), ('CD2', 'TYR', 'CD1', 'TYR', 10.88), ('CD2', 'TYR', 'CD2', 'TYR', 12.28), ('CD2', 'TYR', 'CE1', 'TYR', 9.8), ('CD2', 'TYR', 'CE2', 'TYR', 11.4), ('CD2', 'TYR', 'CZ', 'TYR', 10.1), ('CD2', 'TYR', 'OH', 'TYR', 9.32)], [('CE1', 'TYR', 'CB', 'TYR', 13.07), ('CE1', 'TYR', 'CG', 'TYR', 11.84), ('CE1', 'TYR', 'CD1', 'TYR', 10.86), ('CE1', 'TYR', 'CD2', 'TYR', 11.85), ('CE1', 'TYR', 'CE1', 'TYR', 9.84), ('CE1', 'TYR', 'CE2', 'TYR', 10.98), ('CE1', 'TYR', 'CZ', 'TYR', 9.9), ('CE1', 'TYR', 'OH', 'TYR', 9.16)], [('CE2', 'TYR', 'CB', 'TYR', 12.3), ('CE2', 'TYR', 'CG', 'TYR', 10.99), ('CE2', 'TYR', 'CD1', 'TYR', 9.86), ('CE2', 'TYR', 'CD2', 'TYR', 11.07), ('CE2', 'TYR', 'CE1', 'TYR', 8.7), ('CE2', 'TYR', 'CE2', 'TYR', 10.13), ('CE2', 'TYR', 'CZ', 'TYR', 8.86), ('CE2', 'TYR', 'OH', 'TYR', 8.02)], [('CZ', 'TYR', 'CB', 'TYR', 12.15), ('CZ', 'TYR', 'CG', 'TYR', 10.85), ('CZ', 'TYR', 'CD1', 'TYR', 9.85), ('CZ', 'TYR', 'CD2', 'TYR', 10.84), ('CZ', 'TYR', 'CE1', 'TYR', 8.73), ('CZ', 'TYR', 'CE2', 'TYR', 9.89), ('CZ', 'TYR', 'CZ', 'TYR', 8.75), ('CZ', 'TYR', 'OH', 'TYR', 7.93)], [('OH', 'TYR', 'CB', 'TYR', 11.33), ('OH', 'TYR', 'CG', 'TYR', 9.99), ('OH', 'TYR', 'CD1', 'TYR', 9.12), ('OH', 'TYR', 'CD2', 'TYR', 9.81), ('OH', 'TYR', 'CE1', 'TYR', 7.95), ('OH', 'TYR', 'CE2', 'TYR', 8.8), ('OH', 'TYR', 'CZ', 'TYR', 7.76), ('OH', 'TYR', 'OH', 'TYR', 6.9)]]}
CYS_TYR = { 
	'distances':
		[[14.12, 12.76, 11.63, 12.75, 10.4, 11.68, 10.42, 9.4], [13.01, 11.63, 10.62, 11.52, 9.38, 10.43, 9.27, 8.25], [8.7, 8.14, 9.1, 6.9, 9.05, 6.8, 8.0, 8.39], [10.05, 9.25, 10.03, 7.91, 9.69, 7.41, 8.44, 8.47], [19.76, 18.48, 17.57, 18.29, 16.44, 17.21, 16.25, 15.24], [21.02, 19.72, 18.88, 19.42, 17.71, 18.29, 17.4, 16.33]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'TYR', 14.12), ('CB', 'CYS', 'CG', 'TYR', 12.76), ('CB', 'CYS', 'CD1', 'TYR', 11.63), ('CB', 'CYS', 'CD2', 'TYR', 12.75), ('CB', 'CYS', 'CE1', 'TYR', 10.4), ('CB', 'CYS', 'CE2', 'TYR', 11.68), ('CB', 'CYS', 'CZ', 'TYR', 10.42), ('CB', 'CYS', 'OH', 'TYR', 9.4)], [('SG', 'CYS', 'CB', 'TYR', 13.01), ('SG', 'CYS', 'CG', 'TYR', 11.63), ('SG', 'CYS', 'CD1', 'TYR', 10.62), ('SG', 'CYS', 'CD2', 'TYR', 11.52), ('SG', 'CYS', 'CE1', 'TYR', 9.38), ('SG', 'CYS', 'CE2', 'TYR', 10.43), ('SG', 'CYS', 'CZ', 'TYR', 9.27), ('SG', 'CYS', 'OH', 'TYR', 8.25)], [('CB', 'CYS', 'CB', 'TYR', 8.7), ('CB', 'CYS', 'CG', 'TYR', 8.14), ('CB', 'CYS', 'CD1', 'TYR', 9.1), ('CB', 'CYS', 'CD2', 'TYR', 6.9), ('CB', 'CYS', 'CE1', 'TYR', 9.05), ('CB', 'CYS', 'CE2', 'TYR', 6.8), ('CB', 'CYS', 'CZ', 'TYR', 8.0), ('CB', 'CYS', 'OH', 'TYR', 8.39)], [('SG', 'CYS', 'CB', 'TYR', 10.05), ('SG', 'CYS', 'CG', 'TYR', 9.25), ('SG', 'CYS', 'CD1', 'TYR', 10.03), ('SG', 'CYS', 'CD2', 'TYR', 7.91), ('SG', 'CYS', 'CE1', 'TYR', 9.69), ('SG', 'CYS', 'CE2', 'TYR', 7.41), ('SG', 'CYS', 'CZ', 'TYR', 8.44), ('SG', 'CYS', 'OH', 'TYR', 8.47)], [('CB', 'CYS', 'CB', 'TYR', 19.76), ('CB', 'CYS', 'CG', 'TYR', 18.48), ('CB', 'CYS', 'CD1', 'TYR', 17.57), ('CB', 'CYS', 'CD2', 'TYR', 18.29), ('CB', 'CYS', 'CE1', 'TYR', 16.44), ('CB', 'CYS', 'CE2', 'TYR', 17.21), ('CB', 'CYS', 'CZ', 'TYR', 16.25), ('CB', 'CYS', 'OH', 'TYR', 15.24)], [('SG', 'CYS', 'CB', 'TYR', 21.02), ('SG', 'CYS', 'CG', 'TYR', 19.72), ('SG', 'CYS', 'CD1', 'TYR', 18.88), ('SG', 'CYS', 'CD2', 'TYR', 19.42), ('SG', 'CYS', 'CE1', 'TYR', 17.71), ('SG', 'CYS', 'CE2', 'TYR', 18.29), ('SG', 'CYS', 'CZ', 'TYR', 17.4), ('SG', 'CYS', 'OH', 'TYR', 16.33)]]}
CYS_GLU = { 
	'distances':
		[[8.4, 8.49, 7.35, 6.26, 7.88], [8.77, 8.63, 7.31, 6.25, 7.66], [14.75, 15.23, 14.19, 12.99, 14.83], [16.4, 16.8, 15.7, 14.51, 16.25]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 8.4), ('CB', 'CYS', 'CG', 'GLU', 8.49), ('CB', 'CYS', 'CD', 'GLU', 7.35), ('CB', 'CYS', 'OE1', 'GLU', 6.26), ('CB', 'CYS', 'OE2', 'GLU', 7.88)], [('SG', 'CYS', 'CB', 'GLU', 8.77), ('SG', 'CYS', 'CG', 'GLU', 8.63), ('SG', 'CYS', 'CD', 'GLU', 7.31), ('SG', 'CYS', 'OE1', 'GLU', 6.25), ('SG', 'CYS', 'OE2', 'GLU', 7.66)], [('CB', 'CYS', 'CB', 'GLU', 14.75), ('CB', 'CYS', 'CG', 'GLU', 15.23), ('CB', 'CYS', 'CD', 'GLU', 14.19), ('CB', 'CYS', 'OE1', 'GLU', 12.99), ('CB', 'CYS', 'OE2', 'GLU', 14.83)], [('SG', 'CYS', 'CB', 'GLU', 16.4), ('SG', 'CYS', 'CG', 'GLU', 16.8), ('SG', 'CYS', 'CD', 'GLU', 15.7), ('SG', 'CYS', 'OE1', 'GLU', 14.51), ('SG', 'CYS', 'OE2', 'GLU', 16.25)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_CYS, d, 'P_1fva_1_8_4_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_TYRI, d, 'P_1fva_1_8_4_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_GLU, d, 'P_1fva_1_8_4_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_TYR, d, 'P_1fva_1_8_4_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_TYR, d, 'P_1fva_1_8_4_6')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_GLU, d, 'P_1fva_1_8_4_6')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_CYS' :  match1,
		'CYS_TYRI' :  match2,
		'TYR_GLU' :  match3,
		'TYR_TYR' :  match4,
		'CYS_TYR' :  match5,
		'CYS_GLU' :  match6}