'''
FUNC:A_1mka_4_2_1_60
PDB:1mka
EC:4.2.1.60
RESI:his,val,gly,cys,asp
LOCI:a-70,76,79,80,84;
'''
import motifFunctions as cmd
VAL_ASP = { 
	'distances':
		[[17.87, 19.16, 19.6, 19.85], [17.65, 18.87, 19.23, 19.6], [17.31, 18.65, 19.08, 19.38], [15.58, 16.77, 17.27, 17.37], [15.98, 17.23, 17.78, 17.82], [17.46, 18.73, 19.26, 19.33], [18.22, 19.43, 19.97, 19.98]],
	'comparisons':
		[[('CB', 'VAL', 'CB', 'ASP', 17.87), ('CB', 'VAL', 'CG', 'ASP', 19.16), ('CB', 'VAL', 'OD1', 'ASP', 19.6), ('CB', 'VAL', 'OD2', 'ASP', 19.85)], [('CG1', 'VAL', 'CB', 'ASP', 17.65), ('CG1', 'VAL', 'CG', 'ASP', 18.87), ('CG1', 'VAL', 'OD1', 'ASP', 19.23), ('CG1', 'VAL', 'OD2', 'ASP', 19.6)], [('CG2', 'VAL', 'CB', 'ASP', 17.31), ('CG2', 'VAL', 'CG', 'ASP', 18.65), ('CG2', 'VAL', 'OD1', 'ASP', 19.08), ('CG2', 'VAL', 'OD2', 'ASP', 19.38)], [('O', 'VAL', 'CB', 'ASP', 15.58), ('O', 'VAL', 'CG', 'ASP', 16.77), ('O', 'VAL', 'OD1', 'ASP', 17.27), ('O', 'VAL', 'OD2', 'ASP', 17.37)], [('C', 'VAL', 'CB', 'ASP', 15.98), ('C', 'VAL', 'CG', 'ASP', 17.23), ('C', 'VAL', 'OD1', 'ASP', 17.78), ('C', 'VAL', 'OD2', 'ASP', 17.82)], [('CA', 'VAL', 'CB', 'ASP', 17.46), ('CA', 'VAL', 'CG', 'ASP', 18.73), ('CA', 'VAL', 'OD1', 'ASP', 19.26), ('CA', 'VAL', 'OD2', 'ASP', 19.33)], [('N', 'VAL', 'CB', 'ASP', 18.22), ('N', 'VAL', 'CG', 'ASP', 19.43), ('N', 'VAL', 'OD1', 'ASP', 19.97), ('N', 'VAL', 'OD2', 'ASP', 19.98)]]}
GLY_HIS = { 
	'distances':
		[[12.71, 11.8, 11.57, 11.21, 10.82, 10.56], [11.7, 10.7, 10.45, 10.09, 9.64, 9.38], [11.07, 10.06, 10.0, 9.26, 9.14, 8.63], [9.62, 8.61, 8.59, 7.83, 7.78, 7.25]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 12.71), ('O', 'GLY', 'CG', 'HIS', 11.8), ('O', 'GLY', 'ND1', 'HIS', 11.57), ('O', 'GLY', 'CD2', 'HIS', 11.21), ('O', 'GLY', 'CE1', 'HIS', 10.82), ('O', 'GLY', 'NE2', 'HIS', 10.56)], [('C', 'GLY', 'CB', 'HIS', 11.7), ('C', 'GLY', 'CG', 'HIS', 10.7), ('C', 'GLY', 'ND1', 'HIS', 10.45), ('C', 'GLY', 'CD2', 'HIS', 10.09), ('C', 'GLY', 'CE1', 'HIS', 9.64), ('C', 'GLY', 'NE2', 'HIS', 9.38)], [('CA', 'GLY', 'CB', 'HIS', 11.07), ('CA', 'GLY', 'CG', 'HIS', 10.06), ('CA', 'GLY', 'ND1', 'HIS', 10.0), ('CA', 'GLY', 'CD2', 'HIS', 9.26), ('CA', 'GLY', 'CE1', 'HIS', 9.14), ('CA', 'GLY', 'NE2', 'HIS', 8.63)], [('N', 'GLY', 'CB', 'HIS', 9.62), ('N', 'GLY', 'CG', 'HIS', 8.61), ('N', 'GLY', 'ND1', 'HIS', 8.59), ('N', 'GLY', 'CD2', 'HIS', 7.83), ('N', 'GLY', 'CE1', 'HIS', 7.78), ('N', 'GLY', 'NE2', 'HIS', 7.25)]]}
GLY_VAL = { 
	'distances':
		[[12.53, 12.37, 11.62, 11.2, 11.37, 12.6, 13.7], [11.7, 11.42, 10.87, 10.35, 10.62, 11.84, 12.89], [10.34, 10.11, 9.44, 9.3, 9.47, 10.59, 11.71], [9.34, 8.98, 8.63, 8.03, 8.35, 9.53, 10.54]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'VAL', 12.53), ('O', 'GLY', 'CG1', 'VAL', 12.37), ('O', 'GLY', 'CG2', 'VAL', 11.62), ('O', 'GLY', 'O', 'VAL', 11.2), ('O', 'GLY', 'C', 'VAL', 11.37), ('O', 'GLY', 'CA', 'VAL', 12.6), ('O', 'GLY', 'N', 'VAL', 13.7)], [('C', 'GLY', 'CB', 'VAL', 11.7), ('C', 'GLY', 'CG1', 'VAL', 11.42), ('C', 'GLY', 'CG2', 'VAL', 10.87), ('C', 'GLY', 'O', 'VAL', 10.35), ('C', 'GLY', 'C', 'VAL', 10.62), ('C', 'GLY', 'CA', 'VAL', 11.84), ('C', 'GLY', 'N', 'VAL', 12.89)], [('CA', 'GLY', 'CB', 'VAL', 10.34), ('CA', 'GLY', 'CG1', 'VAL', 10.11), ('CA', 'GLY', 'CG2', 'VAL', 9.44), ('CA', 'GLY', 'O', 'VAL', 9.3), ('CA', 'GLY', 'C', 'VAL', 9.47), ('CA', 'GLY', 'CA', 'VAL', 10.59), ('CA', 'GLY', 'N', 'VAL', 11.71)], [('N', 'GLY', 'CB', 'VAL', 9.34), ('N', 'GLY', 'CG1', 'VAL', 8.98), ('N', 'GLY', 'CG2', 'VAL', 8.63), ('N', 'GLY', 'O', 'VAL', 8.03), ('N', 'GLY', 'C', 'VAL', 8.35), ('N', 'GLY', 'CA', 'VAL', 9.53), ('N', 'GLY', 'N', 'VAL', 10.54)]]}
ASP_HIS = { 
	'distances':
		[[15.81, 15.3, 14.74, 15.37, 14.47, 14.84], [16.69, 16.2, 15.55, 16.37, 15.32, 15.81], [17.04, 16.46, 15.72, 16.61, 15.41, 15.95], [17.22, 16.84, 16.22, 17.08, 16.08, 16.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 15.81), ('CB', 'ASP', 'CG', 'HIS', 15.3), ('CB', 'ASP', 'ND1', 'HIS', 14.74), ('CB', 'ASP', 'CD2', 'HIS', 15.37), ('CB', 'ASP', 'CE1', 'HIS', 14.47), ('CB', 'ASP', 'NE2', 'HIS', 14.84)], [('CG', 'ASP', 'CB', 'HIS', 16.69), ('CG', 'ASP', 'CG', 'HIS', 16.2), ('CG', 'ASP', 'ND1', 'HIS', 15.55), ('CG', 'ASP', 'CD2', 'HIS', 16.37), ('CG', 'ASP', 'CE1', 'HIS', 15.32), ('CG', 'ASP', 'NE2', 'HIS', 15.81)], [('OD1', 'ASP', 'CB', 'HIS', 17.04), ('OD1', 'ASP', 'CG', 'HIS', 16.46), ('OD1', 'ASP', 'ND1', 'HIS', 15.72), ('OD1', 'ASP', 'CD2', 'HIS', 16.61), ('OD1', 'ASP', 'CE1', 'HIS', 15.41), ('OD1', 'ASP', 'NE2', 'HIS', 15.95)], [('OD2', 'ASP', 'CB', 'HIS', 17.22), ('OD2', 'ASP', 'CG', 'HIS', 16.84), ('OD2', 'ASP', 'ND1', 'HIS', 16.22), ('OD2', 'ASP', 'CD2', 'HIS', 17.08), ('OD2', 'ASP', 'CE1', 'HIS', 16.08), ('OD2', 'ASP', 'NE2', 'HIS', 16.6)]]}
CYS_GLY = { 
	'distances':
		[[6.31, 5.75, 6.88, 6.87], [7.25, 6.57, 7.44, 6.98], [5.57, 5.96, 7.43, 7.93], [4.93, 5.02, 6.42, 6.77], [4.81, 4.45, 5.81, 6.17], [4.26, 3.34, 4.43, 4.76]],
	'comparisons':
		[[('CB', 'CYS', 'O', 'GLY', 6.31), ('CB', 'CYS', 'C', 'GLY', 5.75), ('CB', 'CYS', 'CA', 'GLY', 6.88), ('CB', 'CYS', 'N', 'GLY', 6.87)], [('SG', 'CYS', 'O', 'GLY', 7.25), ('SG', 'CYS', 'C', 'GLY', 6.57), ('SG', 'CYS', 'CA', 'GLY', 7.44), ('SG', 'CYS', 'N', 'GLY', 6.98)], [('O', 'CYS', 'O', 'GLY', 5.57), ('O', 'CYS', 'C', 'GLY', 5.96), ('O', 'CYS', 'CA', 'GLY', 7.43), ('O', 'CYS', 'N', 'GLY', 7.93)], [('C', 'CYS', 'O', 'GLY', 4.93), ('C', 'CYS', 'C', 'GLY', 5.02), ('C', 'CYS', 'CA', 'GLY', 6.42), ('C', 'CYS', 'N', 'GLY', 6.77)], [('CA', 'CYS', 'O', 'GLY', 4.81), ('CA', 'CYS', 'C', 'GLY', 4.45), ('CA', 'CYS', 'CA', 'GLY', 5.81), ('CA', 'CYS', 'N', 'GLY', 6.17)], [('N', 'CYS', 'O', 'GLY', 4.26), ('N', 'CYS', 'C', 'GLY', 3.34), ('N', 'CYS', 'CA', 'GLY', 4.43), ('N', 'CYS', 'N', 'GLY', 4.76)]]}
CYS_VAL = { 
	'distances':
		[[13.78, 13.11, 13.33, 11.84, 12.51, 13.84, 14.56], [13.2, 12.49, 12.95, 10.9, 11.69, 13.08, 13.64], [15.0, 14.66, 14.37, 13.0, 13.43, 14.84, 15.7], [13.83, 13.45, 13.22, 11.83, 12.29, 13.69, 14.54], [13.42, 12.92, 12.79, 11.64, 12.14, 13.47, 14.33], [12.06, 11.59, 11.38, 10.47, 10.91, 12.18, 13.1]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'VAL', 13.78), ('CB', 'CYS', 'CG1', 'VAL', 13.11), ('CB', 'CYS', 'CG2', 'VAL', 13.33), ('CB', 'CYS', 'O', 'VAL', 11.84), ('CB', 'CYS', 'C', 'VAL', 12.51), ('CB', 'CYS', 'CA', 'VAL', 13.84), ('CB', 'CYS', 'N', 'VAL', 14.56)], [('SG', 'CYS', 'CB', 'VAL', 13.2), ('SG', 'CYS', 'CG1', 'VAL', 12.49), ('SG', 'CYS', 'CG2', 'VAL', 12.95), ('SG', 'CYS', 'O', 'VAL', 10.9), ('SG', 'CYS', 'C', 'VAL', 11.69), ('SG', 'CYS', 'CA', 'VAL', 13.08), ('SG', 'CYS', 'N', 'VAL', 13.64)], [('O', 'CYS', 'CB', 'VAL', 15.0), ('O', 'CYS', 'CG1', 'VAL', 14.66), ('O', 'CYS', 'CG2', 'VAL', 14.37), ('O', 'CYS', 'O', 'VAL', 13.0), ('O', 'CYS', 'C', 'VAL', 13.43), ('O', 'CYS', 'CA', 'VAL', 14.84), ('O', 'CYS', 'N', 'VAL', 15.7)], [('C', 'CYS', 'CB', 'VAL', 13.83), ('C', 'CYS', 'CG1', 'VAL', 13.45), ('C', 'CYS', 'CG2', 'VAL', 13.22), ('C', 'CYS', 'O', 'VAL', 11.83), ('C', 'CYS', 'C', 'VAL', 12.29), ('C', 'CYS', 'CA', 'VAL', 13.69), ('C', 'CYS', 'N', 'VAL', 14.54)], [('CA', 'CYS', 'CB', 'VAL', 13.42), ('CA', 'CYS', 'CG1', 'VAL', 12.92), ('CA', 'CYS', 'CG2', 'VAL', 12.79), ('CA', 'CYS', 'O', 'VAL', 11.64), ('CA', 'CYS', 'C', 'VAL', 12.14), ('CA', 'CYS', 'CA', 'VAL', 13.47), ('CA', 'CYS', 'N', 'VAL', 14.33)], [('N', 'CYS', 'CB', 'VAL', 12.06), ('N', 'CYS', 'CG1', 'VAL', 11.59), ('N', 'CYS', 'CG2', 'VAL', 11.38), ('N', 'CYS', 'O', 'VAL', 10.47), ('N', 'CYS', 'C', 'VAL', 10.91), ('N', 'CYS', 'CA', 'VAL', 12.18), ('N', 'CYS', 'N', 'VAL', 13.1)]]}
GLY_ASP = { 
	'distances':
		[[8.78, 10.14, 10.34, 11.15], [9.42, 10.7, 10.85, 11.73], [10.82, 12.14, 12.34, 13.12], [11.26, 12.53, 12.76, 13.45]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 8.78), ('O', 'GLY', 'CG', 'ASP', 10.14), ('O', 'GLY', 'OD1', 'ASP', 10.34), ('O', 'GLY', 'OD2', 'ASP', 11.15)], [('C', 'GLY', 'CB', 'ASP', 9.42), ('C', 'GLY', 'CG', 'ASP', 10.7), ('C', 'GLY', 'OD1', 'ASP', 10.85), ('C', 'GLY', 'OD2', 'ASP', 11.73)], [('CA', 'GLY', 'CB', 'ASP', 10.82), ('CA', 'GLY', 'CG', 'ASP', 12.14), ('CA', 'GLY', 'OD1', 'ASP', 12.34), ('CA', 'GLY', 'OD2', 'ASP', 13.12)], [('N', 'GLY', 'CB', 'ASP', 11.26), ('N', 'GLY', 'CG', 'ASP', 12.53), ('N', 'GLY', 'OD1', 'ASP', 12.76), ('N', 'GLY', 'OD2', 'ASP', 13.45)]]}
VAL_HIS = { 
	'distances':
		[[8.46, 8.26, 9.45, 7.25, 9.31, 8.06], [7.51, 7.11, 8.25, 6.03, 8.05, 6.8], [9.41, 9.01, 10.07, 7.88, 9.73, 8.44], [6.02, 6.05, 7.25, 5.46, 7.43, 6.5], [7.21, 7.27, 8.46, 6.59, 8.56, 7.56], [8.0, 8.1, 9.38, 7.35, 9.47, 8.36], [7.48, 7.87, 9.23, 7.35, 9.53, 8.54]],
	'comparisons':
		[[('CB', 'VAL', 'CB', 'HIS', 8.46), ('CB', 'VAL', 'CG', 'HIS', 8.26), ('CB', 'VAL', 'ND1', 'HIS', 9.45), ('CB', 'VAL', 'CD2', 'HIS', 7.25), ('CB', 'VAL', 'CE1', 'HIS', 9.31), ('CB', 'VAL', 'NE2', 'HIS', 8.06)], [('CG1', 'VAL', 'CB', 'HIS', 7.51), ('CG1', 'VAL', 'CG', 'HIS', 7.11), ('CG1', 'VAL', 'ND1', 'HIS', 8.25), ('CG1', 'VAL', 'CD2', 'HIS', 6.03), ('CG1', 'VAL', 'CE1', 'HIS', 8.05), ('CG1', 'VAL', 'NE2', 'HIS', 6.8)], [('CG2', 'VAL', 'CB', 'HIS', 9.41), ('CG2', 'VAL', 'CG', 'HIS', 9.01), ('CG2', 'VAL', 'ND1', 'HIS', 10.07), ('CG2', 'VAL', 'CD2', 'HIS', 7.88), ('CG2', 'VAL', 'CE1', 'HIS', 9.73), ('CG2', 'VAL', 'NE2', 'HIS', 8.44)], [('O', 'VAL', 'CB', 'HIS', 6.02), ('O', 'VAL', 'CG', 'HIS', 6.05), ('O', 'VAL', 'ND1', 'HIS', 7.25), ('O', 'VAL', 'CD2', 'HIS', 5.46), ('O', 'VAL', 'CE1', 'HIS', 7.43), ('O', 'VAL', 'NE2', 'HIS', 6.5)], [('C', 'VAL', 'CB', 'HIS', 7.21), ('C', 'VAL', 'CG', 'HIS', 7.27), ('C', 'VAL', 'ND1', 'HIS', 8.46), ('C', 'VAL', 'CD2', 'HIS', 6.59), ('C', 'VAL', 'CE1', 'HIS', 8.56), ('C', 'VAL', 'NE2', 'HIS', 7.56)], [('CA', 'VAL', 'CB', 'HIS', 8.0), ('CA', 'VAL', 'CG', 'HIS', 8.1), ('CA', 'VAL', 'ND1', 'HIS', 9.38), ('CA', 'VAL', 'CD2', 'HIS', 7.35), ('CA', 'VAL', 'CE1', 'HIS', 9.47), ('CA', 'VAL', 'NE2', 'HIS', 8.36)], [('N', 'VAL', 'CB', 'HIS', 7.48), ('N', 'VAL', 'CG', 'HIS', 7.87), ('N', 'VAL', 'ND1', 'HIS', 9.23), ('N', 'VAL', 'CD2', 'HIS', 7.35), ('N', 'VAL', 'CE1', 'HIS', 9.53), ('N', 'VAL', 'NE2', 'HIS', 8.54)]]}
CYS_ASP = { 
	'distances':
		[[8.4, 9.19, 9.0, 10.27], [8.66, 9.4, 9.38, 10.28], [5.65, 6.8, 6.9, 7.89], [6.68, 7.85, 8.0, 8.87], [7.99, 9.03, 8.97, 10.12], [9.13, 10.29, 10.33, 11.33]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 8.4), ('CB', 'CYS', 'CG', 'ASP', 9.19), ('CB', 'CYS', 'OD1', 'ASP', 9.0), ('CB', 'CYS', 'OD2', 'ASP', 10.27)], [('SG', 'CYS', 'CB', 'ASP', 8.66), ('SG', 'CYS', 'CG', 'ASP', 9.4), ('SG', 'CYS', 'OD1', 'ASP', 9.38), ('SG', 'CYS', 'OD2', 'ASP', 10.28)], [('O', 'CYS', 'CB', 'ASP', 5.65), ('O', 'CYS', 'CG', 'ASP', 6.8), ('O', 'CYS', 'OD1', 'ASP', 6.9), ('O', 'CYS', 'OD2', 'ASP', 7.89)], [('C', 'CYS', 'CB', 'ASP', 6.68), ('C', 'CYS', 'CG', 'ASP', 7.85), ('C', 'CYS', 'OD1', 'ASP', 8.0), ('C', 'CYS', 'OD2', 'ASP', 8.87)], [('CA', 'CYS', 'CB', 'ASP', 7.99), ('CA', 'CYS', 'CG', 'ASP', 9.03), ('CA', 'CYS', 'OD1', 'ASP', 8.97), ('CA', 'CYS', 'OD2', 'ASP', 10.12)], [('N', 'CYS', 'CB', 'ASP', 9.13), ('N', 'CYS', 'CG', 'ASP', 10.29), ('N', 'CYS', 'OD1', 'ASP', 10.33), ('N', 'CYS', 'OD2', 'ASP', 11.33)]]}
CYS_HIS = { 
	'distances':
		[[11.63, 10.6, 9.8, 10.44, 9.09, 9.49], [10.24, 9.36, 8.53, 9.44, 8.06, 8.64], [13.44, 12.66, 12.1, 12.5, 11.57, 11.8], [12.31, 11.49, 10.97, 11.29, 10.42, 10.6], [12.04, 11.05, 10.45, 10.73, 9.71, 9.87], [11.24, 10.19, 9.75, 9.71, 8.93, 8.88]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 11.63), ('CB', 'CYS', 'CG', 'HIS', 10.6), ('CB', 'CYS', 'ND1', 'HIS', 9.8), ('CB', 'CYS', 'CD2', 'HIS', 10.44), ('CB', 'CYS', 'CE1', 'HIS', 9.09), ('CB', 'CYS', 'NE2', 'HIS', 9.49)], [('SG', 'CYS', 'CB', 'HIS', 10.24), ('SG', 'CYS', 'CG', 'HIS', 9.36), ('SG', 'CYS', 'ND1', 'HIS', 8.53), ('SG', 'CYS', 'CD2', 'HIS', 9.44), ('SG', 'CYS', 'CE1', 'HIS', 8.06), ('SG', 'CYS', 'NE2', 'HIS', 8.64)], [('O', 'CYS', 'CB', 'HIS', 13.44), ('O', 'CYS', 'CG', 'HIS', 12.66), ('O', 'CYS', 'ND1', 'HIS', 12.1), ('O', 'CYS', 'CD2', 'HIS', 12.5), ('O', 'CYS', 'CE1', 'HIS', 11.57), ('O', 'CYS', 'NE2', 'HIS', 11.8)], [('C', 'CYS', 'CB', 'HIS', 12.31), ('C', 'CYS', 'CG', 'HIS', 11.49), ('C', 'CYS', 'ND1', 'HIS', 10.97), ('C', 'CYS', 'CD2', 'HIS', 11.29), ('C', 'CYS', 'CE1', 'HIS', 10.42), ('C', 'CYS', 'NE2', 'HIS', 10.6)], [('CA', 'CYS', 'CB', 'HIS', 12.04), ('CA', 'CYS', 'CG', 'HIS', 11.05), ('CA', 'CYS', 'ND1', 'HIS', 10.45), ('CA', 'CYS', 'CD2', 'HIS', 10.73), ('CA', 'CYS', 'CE1', 'HIS', 9.71), ('CA', 'CYS', 'NE2', 'HIS', 9.87)], [('N', 'CYS', 'CB', 'HIS', 11.24), ('N', 'CYS', 'CG', 'HIS', 10.19), ('N', 'CYS', 'ND1', 'HIS', 9.75), ('N', 'CYS', 'CD2', 'HIS', 9.71), ('N', 'CYS', 'CE1', 'HIS', 8.93), ('N', 'CYS', 'NE2', 'HIS', 8.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(VAL_ASP, d, 'A_1mka_4_2_1_60')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_HIS, d, 'A_1mka_4_2_1_60')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_VAL, d, 'A_1mka_4_2_1_60')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_HIS, d, 'A_1mka_4_2_1_60')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_GLY, d, 'A_1mka_4_2_1_60')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_VAL, d, 'A_1mka_4_2_1_60')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_ASP, d, 'A_1mka_4_2_1_60')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(VAL_HIS, d, 'A_1mka_4_2_1_60')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(CYS_ASP, d, 'A_1mka_4_2_1_60')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(CYS_HIS, d, 'A_1mka_4_2_1_60')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'VAL_ASP' :  match1,
		'GLY_HIS' :  match2,
		'GLY_VAL' :  match3,
		'ASP_HIS' :  match4,
		'CYS_GLY' :  match5,
		'CYS_VAL' :  match6,
		'GLY_ASP' :  match7,
		'VAL_HIS' :  match8,
		'CYS_ASP' :  match9,
		'CYS_HIS' :  match10}