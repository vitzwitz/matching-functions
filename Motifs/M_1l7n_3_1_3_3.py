'''
FUNC:M_1l7n_3_1_3_3
PDB:1l7n
EC:3.1.3.3
RESI:asp,phe,asp,gly,lys,asp,mg
LOCI:a-11,12,13,100,144,171,221;
'''
import motifFunctions as cmd
MG_ASPII = { 
	'distances':
		[8.63, 7.26, 7.41, 6.28],
	'comparisons':
		[('MG', 'MG', 'CB', 'ASPII', 8.63), ('MG', 'MG', 'CG', 'ASPII', 7.26), ('MG', 'MG', 'OD1', 'ASPII', 7.41), ('MG', 'MG', 'OD2', 'ASPII', 6.28)]}
ASP_MG = { 
	'distances':
		[[6.15], [7.45], [7.66], [8.47], [6.37], [5.06], [5.41], [4.1], [8.63], [7.26], [7.41], [6.28]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 6.15)], [('CG', 'ASP', 'MG', 'MG', 7.45)], [('OD1', 'ASP', 'MG', 'MG', 7.66)], [('OD2', 'ASP', 'MG', 'MG', 8.47)], [('CB', 'ASP', 'MG', 'MG', 6.37)], [('CG', 'ASP', 'MG', 'MG', 5.06)], [('OD1', 'ASP', 'MG', 'MG', 5.41)], [('OD2', 'ASP', 'MG', 'MG', 4.1)], [('CB', 'ASP', 'MG', 'MG', 8.63)], [('CG', 'ASP', 'MG', 'MG', 7.26)], [('OD1', 'ASP', 'MG', 'MG', 7.41)], [('OD2', 'ASP', 'MG', 'MG', 6.28)]]}
PHE_MG = { 
	'distances':
		[[8.46], [9.47], [10.57], [9.6], [11.67], [10.8], [11.76]],
	'comparisons':
		[[('CB', 'PHE', 'MG', 'MG', 8.46)], [('CG', 'PHE', 'MG', 'MG', 9.47)], [('CD1', 'PHE', 'MG', 'MG', 10.57)], [('CD2', 'PHE', 'MG', 'MG', 9.6)], [('CE1', 'PHE', 'MG', 'MG', 11.67)], [('CE2', 'PHE', 'MG', 'MG', 10.8)], [('CZ', 'PHE', 'MG', 'MG', 11.76)]]}
ASP_ASP = { 
	'distances':
		[[8.95, 7.61, 7.42, 7.03], [9.74, 8.45, 8.03, 8.1], [9.67, 8.36, 7.71, 8.23], [10.67, 9.44, 9.1, 9.07], [12.39, 10.93, 10.66, 10.18], [13.3, 11.82, 11.39, 11.21], [12.99, 11.53, 10.98, 11.05], [14.45, 12.96, 12.53, 12.33], [8.95, 9.74, 9.67, 10.67], [7.61, 8.45, 8.36, 9.44], [7.42, 8.03, 7.71, 9.1], [7.03, 8.1, 8.23, 9.07], [7.21, 5.92, 5.57, 5.67], [7.5, 6.03, 5.68, 5.57], [7.7, 6.22, 5.57, 5.99], [7.95, 6.51, 6.46, 5.72], [12.39, 13.3, 12.99, 14.45], [10.93, 11.82, 11.53, 12.96], [10.66, 11.39, 10.98, 12.53], [10.18, 11.21, 11.05, 12.33]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 8.95), ('CB', 'ASP', 'CG', 'ASP', 7.61), ('CB', 'ASP', 'OD1', 'ASP', 7.42), ('CB', 'ASP', 'OD2', 'ASP', 7.03)], [('CG', 'ASP', 'CB', 'ASP', 9.74), ('CG', 'ASP', 'CG', 'ASP', 8.45), ('CG', 'ASP', 'OD1', 'ASP', 8.03), ('CG', 'ASP', 'OD2', 'ASP', 8.1)], [('OD1', 'ASP', 'CB', 'ASP', 9.67), ('OD1', 'ASP', 'CG', 'ASP', 8.36), ('OD1', 'ASP', 'OD1', 'ASP', 7.71), ('OD1', 'ASP', 'OD2', 'ASP', 8.23)], [('OD2', 'ASP', 'CB', 'ASP', 10.67), ('OD2', 'ASP', 'CG', 'ASP', 9.44), ('OD2', 'ASP', 'OD1', 'ASP', 9.1), ('OD2', 'ASP', 'OD2', 'ASP', 9.07)], [('CB', 'ASP', 'CB', 'ASP', 12.39), ('CB', 'ASP', 'CG', 'ASP', 10.93), ('CB', 'ASP', 'OD1', 'ASP', 10.66), ('CB', 'ASP', 'OD2', 'ASP', 10.18)], [('CG', 'ASP', 'CB', 'ASP', 13.3), ('CG', 'ASP', 'CG', 'ASP', 11.82), ('CG', 'ASP', 'OD1', 'ASP', 11.39), ('CG', 'ASP', 'OD2', 'ASP', 11.21)], [('OD1', 'ASP', 'CB', 'ASP', 12.99), ('OD1', 'ASP', 'CG', 'ASP', 11.53), ('OD1', 'ASP', 'OD1', 'ASP', 10.98), ('OD1', 'ASP', 'OD2', 'ASP', 11.05)], [('OD2', 'ASP', 'CB', 'ASP', 14.45), ('OD2', 'ASP', 'CG', 'ASP', 12.96), ('OD2', 'ASP', 'OD1', 'ASP', 12.53), ('OD2', 'ASP', 'OD2', 'ASP', 12.33)], [('CB', 'ASP', 'CB', 'ASP', 8.95), ('CB', 'ASP', 'CG', 'ASP', 9.74), ('CB', 'ASP', 'OD1', 'ASP', 9.67), ('CB', 'ASP', 'OD2', 'ASP', 10.67)], [('CG', 'ASP', 'CB', 'ASP', 7.61), ('CG', 'ASP', 'CG', 'ASP', 8.45), ('CG', 'ASP', 'OD1', 'ASP', 8.36), ('CG', 'ASP', 'OD2', 'ASP', 9.44)], [('OD1', 'ASP', 'CB', 'ASP', 7.42), ('OD1', 'ASP', 'CG', 'ASP', 8.03), ('OD1', 'ASP', 'OD1', 'ASP', 7.71), ('OD1', 'ASP', 'OD2', 'ASP', 9.1)], [('OD2', 'ASP', 'CB', 'ASP', 7.03), ('OD2', 'ASP', 'CG', 'ASP', 8.1), ('OD2', 'ASP', 'OD1', 'ASP', 8.23), ('OD2', 'ASP', 'OD2', 'ASP', 9.07)], [('CB', 'ASP', 'CB', 'ASP', 7.21), ('CB', 'ASP', 'CG', 'ASP', 5.92), ('CB', 'ASP', 'OD1', 'ASP', 5.57), ('CB', 'ASP', 'OD2', 'ASP', 5.67)], [('CG', 'ASP', 'CB', 'ASP', 7.5), ('CG', 'ASP', 'CG', 'ASP', 6.03), ('CG', 'ASP', 'OD1', 'ASP', 5.68), ('CG', 'ASP', 'OD2', 'ASP', 5.57)], [('OD1', 'ASP', 'CB', 'ASP', 7.7), ('OD1', 'ASP', 'CG', 'ASP', 6.22), ('OD1', 'ASP', 'OD1', 'ASP', 5.57), ('OD1', 'ASP', 'OD2', 'ASP', 5.99)], [('OD2', 'ASP', 'CB', 'ASP', 7.95), ('OD2', 'ASP', 'CG', 'ASP', 6.51), ('OD2', 'ASP', 'OD1', 'ASP', 6.46), ('OD2', 'ASP', 'OD2', 'ASP', 5.72)], [('CB', 'ASP', 'CB', 'ASP', 12.39), ('CB', 'ASP', 'CG', 'ASP', 13.3), ('CB', 'ASP', 'OD1', 'ASP', 12.99), ('CB', 'ASP', 'OD2', 'ASP', 14.45)], [('CG', 'ASP', 'CB', 'ASP', 10.93), ('CG', 'ASP', 'CG', 'ASP', 11.82), ('CG', 'ASP', 'OD1', 'ASP', 11.53), ('CG', 'ASP', 'OD2', 'ASP', 12.96)], [('OD1', 'ASP', 'CB', 'ASP', 10.66), ('OD1', 'ASP', 'CG', 'ASP', 11.39), ('OD1', 'ASP', 'OD1', 'ASP', 10.98), ('OD1', 'ASP', 'OD2', 'ASP', 12.53)], [('OD2', 'ASP', 'CB', 'ASP', 10.18), ('OD2', 'ASP', 'CG', 'ASP', 11.21), ('OD2', 'ASP', 'OD1', 'ASP', 11.05), ('OD2', 'ASP', 'OD2', 'ASP', 12.33)]]}
GLY_LYS = { 
	'distances':
		[[12.29, 10.78, 10.66, 9.25, 9.57], [11.48, 9.95, 9.74, 8.3, 8.54], [9.97, 8.45, 8.29, 6.9, 7.34], [9.39, 7.88, 7.51, 6.08, 6.31]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'LYS', 12.29), ('O', 'GLY', 'CG', 'LYS', 10.78), ('O', 'GLY', 'CD', 'LYS', 10.66), ('O', 'GLY', 'CE', 'LYS', 9.25), ('O', 'GLY', 'NZ', 'LYS', 9.57)], [('C', 'GLY', 'CB', 'LYS', 11.48), ('C', 'GLY', 'CG', 'LYS', 9.95), ('C', 'GLY', 'CD', 'LYS', 9.74), ('C', 'GLY', 'CE', 'LYS', 8.3), ('C', 'GLY', 'NZ', 'LYS', 8.54)], [('CA', 'GLY', 'CB', 'LYS', 9.97), ('CA', 'GLY', 'CG', 'LYS', 8.45), ('CA', 'GLY', 'CD', 'LYS', 8.29), ('CA', 'GLY', 'CE', 'LYS', 6.9), ('CA', 'GLY', 'NZ', 'LYS', 7.34)], [('N', 'GLY', 'CB', 'LYS', 9.39), ('N', 'GLY', 'CG', 'LYS', 7.88), ('N', 'GLY', 'CD', 'LYS', 7.51), ('N', 'GLY', 'CE', 'LYS', 6.08), ('N', 'GLY', 'NZ', 'LYS', 6.31)]]}
PHE_ASPII = { 
	'distances':
		[[12.44, 10.99, 10.28, 10.7], [13.9, 12.44, 11.77, 12.08], [14.77, 13.35, 12.68, 13.0], [14.54, 13.05, 12.4, 12.63], [16.16, 14.72, 14.06, 14.34], [15.92, 14.43, 13.8, 13.98], [16.68, 15.21, 14.57, 14.78]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ASPII', 12.44), ('CB', 'PHE', 'CG', 'ASPII', 10.99), ('CB', 'PHE', 'OD1', 'ASPII', 10.28), ('CB', 'PHE', 'OD2', 'ASPII', 10.7)], [('CG', 'PHE', 'CB', 'ASPII', 13.9), ('CG', 'PHE', 'CG', 'ASPII', 12.44), ('CG', 'PHE', 'OD1', 'ASPII', 11.77), ('CG', 'PHE', 'OD2', 'ASPII', 12.08)], [('CD1', 'PHE', 'CB', 'ASPII', 14.77), ('CD1', 'PHE', 'CG', 'ASPII', 13.35), ('CD1', 'PHE', 'OD1', 'ASPII', 12.68), ('CD1', 'PHE', 'OD2', 'ASPII', 13.0)], [('CD2', 'PHE', 'CB', 'ASPII', 14.54), ('CD2', 'PHE', 'CG', 'ASPII', 13.05), ('CD2', 'PHE', 'OD1', 'ASPII', 12.4), ('CD2', 'PHE', 'OD2', 'ASPII', 12.63)], [('CE1', 'PHE', 'CB', 'ASPII', 16.16), ('CE1', 'PHE', 'CG', 'ASPII', 14.72), ('CE1', 'PHE', 'OD1', 'ASPII', 14.06), ('CE1', 'PHE', 'OD2', 'ASPII', 14.34)], [('CE2', 'PHE', 'CB', 'ASPII', 15.92), ('CE2', 'PHE', 'CG', 'ASPII', 14.43), ('CE2', 'PHE', 'OD1', 'ASPII', 13.8), ('CE2', 'PHE', 'OD2', 'ASPII', 13.98)], [('CZ', 'PHE', 'CB', 'ASPII', 16.68), ('CZ', 'PHE', 'CG', 'ASPII', 15.21), ('CZ', 'PHE', 'OD1', 'ASPII', 14.57), ('CZ', 'PHE', 'OD2', 'ASPII', 14.78)]]}
LYS_ASPI = { 
	'distances':
		[[9.95, 10.34, 9.71, 11.47], [9.23, 9.4, 8.61, 10.53], [7.75, 7.93, 7.22, 9.05], [7.32, 7.14, 6.2, 8.23], [5.88, 5.65, 4.76, 6.75]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASPI', 9.95), ('CB', 'LYS', 'CG', 'ASPI', 10.34), ('CB', 'LYS', 'OD1', 'ASPI', 9.71), ('CB', 'LYS', 'OD2', 'ASPI', 11.47)], [('CG', 'LYS', 'CB', 'ASPI', 9.23), ('CG', 'LYS', 'CG', 'ASPI', 9.4), ('CG', 'LYS', 'OD1', 'ASPI', 8.61), ('CG', 'LYS', 'OD2', 'ASPI', 10.53)], [('CD', 'LYS', 'CB', 'ASPI', 7.75), ('CD', 'LYS', 'CG', 'ASPI', 7.93), ('CD', 'LYS', 'OD1', 'ASPI', 7.22), ('CD', 'LYS', 'OD2', 'ASPI', 9.05)], [('CE', 'LYS', 'CB', 'ASPI', 7.32), ('CE', 'LYS', 'CG', 'ASPI', 7.14), ('CE', 'LYS', 'OD1', 'ASPI', 6.2), ('CE', 'LYS', 'OD2', 'ASPI', 8.23)], [('NZ', 'LYS', 'CB', 'ASPI', 5.88), ('NZ', 'LYS', 'CG', 'ASPI', 5.65), ('NZ', 'LYS', 'OD1', 'ASPI', 4.76), ('NZ', 'LYS', 'OD2', 'ASPI', 6.75)]]}
LYS_PHE = { 
	'distances':
		[[12.96, 14.4, 15.12, 15.11, 16.46, 16.43, 17.07], [11.81, 13.22, 14.04, 13.85, 15.36, 15.16, 15.87], [10.78, 12.24, 13.09, 12.9, 14.44, 14.26, 14.97], [9.68, 11.11, 12.07, 11.65, 13.39, 13.0, 13.8], [8.69, 10.17, 11.14, 10.75, 12.49, 12.13, 12.93]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'PHE', 12.96), ('CB', 'LYS', 'CG', 'PHE', 14.4), ('CB', 'LYS', 'CD1', 'PHE', 15.12), ('CB', 'LYS', 'CD2', 'PHE', 15.11), ('CB', 'LYS', 'CE1', 'PHE', 16.46), ('CB', 'LYS', 'CE2', 'PHE', 16.43), ('CB', 'LYS', 'CZ', 'PHE', 17.07)], [('CG', 'LYS', 'CB', 'PHE', 11.81), ('CG', 'LYS', 'CG', 'PHE', 13.22), ('CG', 'LYS', 'CD1', 'PHE', 14.04), ('CG', 'LYS', 'CD2', 'PHE', 13.85), ('CG', 'LYS', 'CE1', 'PHE', 15.36), ('CG', 'LYS', 'CE2', 'PHE', 15.16), ('CG', 'LYS', 'CZ', 'PHE', 15.87)], [('CD', 'LYS', 'CB', 'PHE', 10.78), ('CD', 'LYS', 'CG', 'PHE', 12.24), ('CD', 'LYS', 'CD1', 'PHE', 13.09), ('CD', 'LYS', 'CD2', 'PHE', 12.9), ('CD', 'LYS', 'CE1', 'PHE', 14.44), ('CD', 'LYS', 'CE2', 'PHE', 14.26), ('CD', 'LYS', 'CZ', 'PHE', 14.97)], [('CE', 'LYS', 'CB', 'PHE', 9.68), ('CE', 'LYS', 'CG', 'PHE', 11.11), ('CE', 'LYS', 'CD1', 'PHE', 12.07), ('CE', 'LYS', 'CD2', 'PHE', 11.65), ('CE', 'LYS', 'CE1', 'PHE', 13.39), ('CE', 'LYS', 'CE2', 'PHE', 13.0), ('CE', 'LYS', 'CZ', 'PHE', 13.8)], [('NZ', 'LYS', 'CB', 'PHE', 8.69), ('NZ', 'LYS', 'CG', 'PHE', 10.17), ('NZ', 'LYS', 'CD1', 'PHE', 11.14), ('NZ', 'LYS', 'CD2', 'PHE', 10.75), ('NZ', 'LYS', 'CE1', 'PHE', 12.49), ('NZ', 'LYS', 'CE2', 'PHE', 12.13), ('NZ', 'LYS', 'CZ', 'PHE', 12.93)]]}
PHE_ASPI = { 
	'distances':
		[[7.64, 7.15, 6.91, 7.45], [9.04, 8.52, 8.33, 8.66], [9.74, 9.44, 9.37, 9.6], [9.9, 9.16, 8.87, 9.17], [11.12, 10.77, 10.7, 10.85], [11.24, 10.51, 10.26, 10.46], [11.79, 11.24, 11.08, 11.23]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'ASPI', 7.64), ('CB', 'PHE', 'CG', 'ASPI', 7.15), ('CB', 'PHE', 'OD1', 'ASPI', 6.91), ('CB', 'PHE', 'OD2', 'ASPI', 7.45)], [('CG', 'PHE', 'CB', 'ASPI', 9.04), ('CG', 'PHE', 'CG', 'ASPI', 8.52), ('CG', 'PHE', 'OD1', 'ASPI', 8.33), ('CG', 'PHE', 'OD2', 'ASPI', 8.66)], [('CD1', 'PHE', 'CB', 'ASPI', 9.74), ('CD1', 'PHE', 'CG', 'ASPI', 9.44), ('CD1', 'PHE', 'OD1', 'ASPI', 9.37), ('CD1', 'PHE', 'OD2', 'ASPI', 9.6)], [('CD2', 'PHE', 'CB', 'ASPI', 9.9), ('CD2', 'PHE', 'CG', 'ASPI', 9.16), ('CD2', 'PHE', 'OD1', 'ASPI', 8.87), ('CD2', 'PHE', 'OD2', 'ASPI', 9.17)], [('CE1', 'PHE', 'CB', 'ASPI', 11.12), ('CE1', 'PHE', 'CG', 'ASPI', 10.77), ('CE1', 'PHE', 'OD1', 'ASPI', 10.7), ('CE1', 'PHE', 'OD2', 'ASPI', 10.85)], [('CE2', 'PHE', 'CB', 'ASPI', 11.24), ('CE2', 'PHE', 'CG', 'ASPI', 10.51), ('CE2', 'PHE', 'OD1', 'ASPI', 10.26), ('CE2', 'PHE', 'OD2', 'ASPI', 10.46)], [('CZ', 'PHE', 'CB', 'ASPI', 11.79), ('CZ', 'PHE', 'CG', 'ASPI', 11.24), ('CZ', 'PHE', 'OD1', 'ASPI', 11.08), ('CZ', 'PHE', 'OD2', 'ASPI', 11.23)]]}
GLY_MG = { 
	'distances':
		[[11.27], [10.49], [10.18], [9.43]],
	'comparisons':
		[[('O', 'GLY', 'MG', 'MG', 11.27)], [('C', 'GLY', 'MG', 'MG', 10.49)], [('CA', 'GLY', 'MG', 'MG', 10.18)], [('N', 'GLY', 'MG', 'MG', 9.43)]]}
MG_ASPI = { 
	'distances':
		[6.37, 5.06, 5.41, 4.1],
	'comparisons':
		[('MG', 'MG', 'CB', 'ASPI', 6.37), ('MG', 'MG', 'CG', 'ASPI', 5.06), ('MG', 'MG', 'OD1', 'ASPI', 5.41), ('MG', 'MG', 'OD2', 'ASPI', 4.1)]}
ASP_ASPI = { 
	'distances':
		[[7.21, 7.5, 7.7, 7.95], [5.92, 6.03, 6.22, 6.51], [5.57, 5.68, 5.57, 6.46], [5.67, 5.57, 5.99, 5.72]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASPI', 7.21), ('CB', 'ASP', 'CG', 'ASPI', 7.5), ('CB', 'ASP', 'OD1', 'ASPI', 7.7), ('CB', 'ASP', 'OD2', 'ASPI', 7.95)], [('CG', 'ASP', 'CB', 'ASPI', 5.92), ('CG', 'ASP', 'CG', 'ASPI', 6.03), ('CG', 'ASP', 'OD1', 'ASPI', 6.22), ('CG', 'ASP', 'OD2', 'ASPI', 6.51)], [('OD1', 'ASP', 'CB', 'ASPI', 5.57), ('OD1', 'ASP', 'CG', 'ASPI', 5.68), ('OD1', 'ASP', 'OD1', 'ASPI', 5.57), ('OD1', 'ASP', 'OD2', 'ASPI', 6.46)], [('OD2', 'ASP', 'CB', 'ASPI', 5.67), ('OD2', 'ASP', 'CG', 'ASPI', 5.57), ('OD2', 'ASP', 'OD1', 'ASPI', 5.99), ('OD2', 'ASP', 'OD2', 'ASPI', 5.72)]]}
LYS_MG = { 
	'distances':
		[[12.56], [11.5], [10.09], [9.09], [7.75]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 12.56)], [('CG', 'LYS', 'MG', 'MG', 11.5)], [('CD', 'LYS', 'MG', 'MG', 10.09)], [('CE', 'LYS', 'MG', 'MG', 9.09)], [('NZ', 'LYS', 'MG', 'MG', 7.75)]]}
ASP_LYS = { 
	'distances':
		[[14.74, 13.41, 12.24, 10.88, 9.77], [14.91, 13.51, 12.47, 11.03, 10.09], [14.09, 12.64, 11.71, 10.22, 9.43], [15.98, 14.59, 13.57, 12.14, 11.2], [9.95, 9.23, 7.75, 7.32, 5.88], [10.34, 9.4, 7.93, 7.14, 5.65], [9.71, 8.61, 7.22, 6.2, 4.76], [11.47, 10.53, 9.05, 8.23, 6.75], [8.49, 8.33, 7.12, 7.54, 6.93], [8.58, 8.11, 6.71, 6.75, 5.84], [7.63, 7.02, 5.56, 5.55, 4.65], [9.76, 9.19, 7.74, 7.55, 6.42]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 14.74), ('CB', 'ASP', 'CG', 'LYS', 13.41), ('CB', 'ASP', 'CD', 'LYS', 12.24), ('CB', 'ASP', 'CE', 'LYS', 10.88), ('CB', 'ASP', 'NZ', 'LYS', 9.77)], [('CG', 'ASP', 'CB', 'LYS', 14.91), ('CG', 'ASP', 'CG', 'LYS', 13.51), ('CG', 'ASP', 'CD', 'LYS', 12.47), ('CG', 'ASP', 'CE', 'LYS', 11.03), ('CG', 'ASP', 'NZ', 'LYS', 10.09)], [('OD1', 'ASP', 'CB', 'LYS', 14.09), ('OD1', 'ASP', 'CG', 'LYS', 12.64), ('OD1', 'ASP', 'CD', 'LYS', 11.71), ('OD1', 'ASP', 'CE', 'LYS', 10.22), ('OD1', 'ASP', 'NZ', 'LYS', 9.43)], [('OD2', 'ASP', 'CB', 'LYS', 15.98), ('OD2', 'ASP', 'CG', 'LYS', 14.59), ('OD2', 'ASP', 'CD', 'LYS', 13.57), ('OD2', 'ASP', 'CE', 'LYS', 12.14), ('OD2', 'ASP', 'NZ', 'LYS', 11.2)], [('CB', 'ASP', 'CB', 'LYS', 9.95), ('CB', 'ASP', 'CG', 'LYS', 9.23), ('CB', 'ASP', 'CD', 'LYS', 7.75), ('CB', 'ASP', 'CE', 'LYS', 7.32), ('CB', 'ASP', 'NZ', 'LYS', 5.88)], [('CG', 'ASP', 'CB', 'LYS', 10.34), ('CG', 'ASP', 'CG', 'LYS', 9.4), ('CG', 'ASP', 'CD', 'LYS', 7.93), ('CG', 'ASP', 'CE', 'LYS', 7.14), ('CG', 'ASP', 'NZ', 'LYS', 5.65)], [('OD1', 'ASP', 'CB', 'LYS', 9.71), ('OD1', 'ASP', 'CG', 'LYS', 8.61), ('OD1', 'ASP', 'CD', 'LYS', 7.22), ('OD1', 'ASP', 'CE', 'LYS', 6.2), ('OD1', 'ASP', 'NZ', 'LYS', 4.76)], [('OD2', 'ASP', 'CB', 'LYS', 11.47), ('OD2', 'ASP', 'CG', 'LYS', 10.53), ('OD2', 'ASP', 'CD', 'LYS', 9.05), ('OD2', 'ASP', 'CE', 'LYS', 8.23), ('OD2', 'ASP', 'NZ', 'LYS', 6.75)], [('CB', 'ASP', 'CB', 'LYS', 8.49), ('CB', 'ASP', 'CG', 'LYS', 8.33), ('CB', 'ASP', 'CD', 'LYS', 7.12), ('CB', 'ASP', 'CE', 'LYS', 7.54), ('CB', 'ASP', 'NZ', 'LYS', 6.93)], [('CG', 'ASP', 'CB', 'LYS', 8.58), ('CG', 'ASP', 'CG', 'LYS', 8.11), ('CG', 'ASP', 'CD', 'LYS', 6.71), ('CG', 'ASP', 'CE', 'LYS', 6.75), ('CG', 'ASP', 'NZ', 'LYS', 5.84)], [('OD1', 'ASP', 'CB', 'LYS', 7.63), ('OD1', 'ASP', 'CG', 'LYS', 7.02), ('OD1', 'ASP', 'CD', 'LYS', 5.56), ('OD1', 'ASP', 'CE', 'LYS', 5.55), ('OD1', 'ASP', 'NZ', 'LYS', 4.65)], [('OD2', 'ASP', 'CB', 'LYS', 9.76), ('OD2', 'ASP', 'CG', 'LYS', 9.19), ('OD2', 'ASP', 'CD', 'LYS', 7.74), ('OD2', 'ASP', 'CE', 'LYS', 7.55), ('OD2', 'ASP', 'NZ', 'LYS', 6.42)]]}
ASP_GLY = { 
	'distances':
		[[9.9, 9.26, 9.7, 9.12], [9.01, 8.42, 9.1, 8.61], [7.77, 7.17, 7.89, 7.49], [9.73, 9.2, 10.01, 9.55], [12.24, 11.13, 10.35, 9.11], [11.16, 10.1, 9.45, 8.31], [9.95, 8.89, 8.19, 7.07], [11.64, 10.66, 10.15, 9.11], [13.76, 12.93, 11.74, 11.01], [12.65, 11.77, 10.67, 9.86], [11.76, 10.84, 9.67, 8.8], [12.79, 11.93, 10.97, 10.16]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 9.9), ('CB', 'ASP', 'C', 'GLY', 9.26), ('CB', 'ASP', 'CA', 'GLY', 9.7), ('CB', 'ASP', 'N', 'GLY', 9.12)], [('CG', 'ASP', 'O', 'GLY', 9.01), ('CG', 'ASP', 'C', 'GLY', 8.42), ('CG', 'ASP', 'CA', 'GLY', 9.1), ('CG', 'ASP', 'N', 'GLY', 8.61)], [('OD1', 'ASP', 'O', 'GLY', 7.77), ('OD1', 'ASP', 'C', 'GLY', 7.17), ('OD1', 'ASP', 'CA', 'GLY', 7.89), ('OD1', 'ASP', 'N', 'GLY', 7.49)], [('OD2', 'ASP', 'O', 'GLY', 9.73), ('OD2', 'ASP', 'C', 'GLY', 9.2), ('OD2', 'ASP', 'CA', 'GLY', 10.01), ('OD2', 'ASP', 'N', 'GLY', 9.55)], [('CB', 'ASP', 'O', 'GLY', 12.24), ('CB', 'ASP', 'C', 'GLY', 11.13), ('CB', 'ASP', 'CA', 'GLY', 10.35), ('CB', 'ASP', 'N', 'GLY', 9.11)], [('CG', 'ASP', 'O', 'GLY', 11.16), ('CG', 'ASP', 'C', 'GLY', 10.1), ('CG', 'ASP', 'CA', 'GLY', 9.45), ('CG', 'ASP', 'N', 'GLY', 8.31)], [('OD1', 'ASP', 'O', 'GLY', 9.95), ('OD1', 'ASP', 'C', 'GLY', 8.89), ('OD1', 'ASP', 'CA', 'GLY', 8.19), ('OD1', 'ASP', 'N', 'GLY', 7.07)], [('OD2', 'ASP', 'O', 'GLY', 11.64), ('OD2', 'ASP', 'C', 'GLY', 10.66), ('OD2', 'ASP', 'CA', 'GLY', 10.15), ('OD2', 'ASP', 'N', 'GLY', 9.11)], [('CB', 'ASP', 'O', 'GLY', 13.76), ('CB', 'ASP', 'C', 'GLY', 12.93), ('CB', 'ASP', 'CA', 'GLY', 11.74), ('CB', 'ASP', 'N', 'GLY', 11.01)], [('CG', 'ASP', 'O', 'GLY', 12.65), ('CG', 'ASP', 'C', 'GLY', 11.77), ('CG', 'ASP', 'CA', 'GLY', 10.67), ('CG', 'ASP', 'N', 'GLY', 9.86)], [('OD1', 'ASP', 'O', 'GLY', 11.76), ('OD1', 'ASP', 'C', 'GLY', 10.84), ('OD1', 'ASP', 'CA', 'GLY', 9.67), ('OD1', 'ASP', 'N', 'GLY', 8.8)], [('OD2', 'ASP', 'O', 'GLY', 12.79), ('OD2', 'ASP', 'C', 'GLY', 11.93), ('OD2', 'ASP', 'CA', 'GLY', 10.97), ('OD2', 'ASP', 'N', 'GLY', 10.16)]]}
GLY_PHE = { 
	'distances':
		[[10.4, 10.97, 12.18, 10.47, 12.86, 11.27, 12.44], [9.3, 9.97, 11.17, 9.6, 11.94, 10.5, 11.64], [9.39, 10.3, 11.47, 10.17, 12.41, 11.22, 12.29], [8.17, 9.21, 10.34, 9.26, 11.38, 10.42, 11.4]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'PHE', 10.4), ('O', 'GLY', 'CG', 'PHE', 10.97), ('O', 'GLY', 'CD1', 'PHE', 12.18), ('O', 'GLY', 'CD2', 'PHE', 10.47), ('O', 'GLY', 'CE1', 'PHE', 12.86), ('O', 'GLY', 'CE2', 'PHE', 11.27), ('O', 'GLY', 'CZ', 'PHE', 12.44)], [('C', 'GLY', 'CB', 'PHE', 9.3), ('C', 'GLY', 'CG', 'PHE', 9.97), ('C', 'GLY', 'CD1', 'PHE', 11.17), ('C', 'GLY', 'CD2', 'PHE', 9.6), ('C', 'GLY', 'CE1', 'PHE', 11.94), ('C', 'GLY', 'CE2', 'PHE', 10.5), ('C', 'GLY', 'CZ', 'PHE', 11.64)], [('CA', 'GLY', 'CB', 'PHE', 9.39), ('CA', 'GLY', 'CG', 'PHE', 10.3), ('CA', 'GLY', 'CD1', 'PHE', 11.47), ('CA', 'GLY', 'CD2', 'PHE', 10.17), ('CA', 'GLY', 'CE1', 'PHE', 12.41), ('CA', 'GLY', 'CE2', 'PHE', 11.22), ('CA', 'GLY', 'CZ', 'PHE', 12.29)], [('N', 'GLY', 'CB', 'PHE', 8.17), ('N', 'GLY', 'CG', 'PHE', 9.21), ('N', 'GLY', 'CD1', 'PHE', 10.34), ('N', 'GLY', 'CD2', 'PHE', 9.26), ('N', 'GLY', 'CE1', 'PHE', 11.38), ('N', 'GLY', 'CE2', 'PHE', 10.42), ('N', 'GLY', 'CZ', 'PHE', 11.4)]]}
ASP_PHE = { 
	'distances':
		[[6.96, 7.21, 8.45, 6.63, 9.12, 7.49, 8.7], [6.69, 6.71, 8.0, 5.83, 8.51, 6.58, 7.91], [6.68, 6.89, 8.24, 6.07, 8.85, 6.94, 8.3], [6.99, 6.62, 7.77, 5.51, 8.02, 5.89, 7.22], [7.64, 9.04, 9.74, 9.9, 11.12, 11.24, 11.79], [7.15, 8.52, 9.44, 9.16, 10.77, 10.51, 11.24], [6.91, 8.33, 9.37, 8.87, 10.7, 10.26, 11.08], [7.45, 8.66, 9.6, 9.17, 10.85, 10.46, 11.23], [12.44, 13.9, 14.77, 14.54, 16.16, 15.92, 16.68], [10.99, 12.44, 13.35, 13.05, 14.72, 14.43, 15.21], [10.28, 11.77, 12.68, 12.4, 14.06, 13.8, 14.57], [10.7, 12.08, 13.0, 12.63, 14.34, 13.98, 14.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'PHE', 6.96), ('CB', 'ASP', 'CG', 'PHE', 7.21), ('CB', 'ASP', 'CD1', 'PHE', 8.45), ('CB', 'ASP', 'CD2', 'PHE', 6.63), ('CB', 'ASP', 'CE1', 'PHE', 9.12), ('CB', 'ASP', 'CE2', 'PHE', 7.49), ('CB', 'ASP', 'CZ', 'PHE', 8.7)], [('CG', 'ASP', 'CB', 'PHE', 6.69), ('CG', 'ASP', 'CG', 'PHE', 6.71), ('CG', 'ASP', 'CD1', 'PHE', 8.0), ('CG', 'ASP', 'CD2', 'PHE', 5.83), ('CG', 'ASP', 'CE1', 'PHE', 8.51), ('CG', 'ASP', 'CE2', 'PHE', 6.58), ('CG', 'ASP', 'CZ', 'PHE', 7.91)], [('OD1', 'ASP', 'CB', 'PHE', 6.68), ('OD1', 'ASP', 'CG', 'PHE', 6.89), ('OD1', 'ASP', 'CD1', 'PHE', 8.24), ('OD1', 'ASP', 'CD2', 'PHE', 6.07), ('OD1', 'ASP', 'CE1', 'PHE', 8.85), ('OD1', 'ASP', 'CE2', 'PHE', 6.94), ('OD1', 'ASP', 'CZ', 'PHE', 8.3)], [('OD2', 'ASP', 'CB', 'PHE', 6.99), ('OD2', 'ASP', 'CG', 'PHE', 6.62), ('OD2', 'ASP', 'CD1', 'PHE', 7.77), ('OD2', 'ASP', 'CD2', 'PHE', 5.51), ('OD2', 'ASP', 'CE1', 'PHE', 8.02), ('OD2', 'ASP', 'CE2', 'PHE', 5.89), ('OD2', 'ASP', 'CZ', 'PHE', 7.22)], [('CB', 'ASP', 'CB', 'PHE', 7.64), ('CB', 'ASP', 'CG', 'PHE', 9.04), ('CB', 'ASP', 'CD1', 'PHE', 9.74), ('CB', 'ASP', 'CD2', 'PHE', 9.9), ('CB', 'ASP', 'CE1', 'PHE', 11.12), ('CB', 'ASP', 'CE2', 'PHE', 11.24), ('CB', 'ASP', 'CZ', 'PHE', 11.79)], [('CG', 'ASP', 'CB', 'PHE', 7.15), ('CG', 'ASP', 'CG', 'PHE', 8.52), ('CG', 'ASP', 'CD1', 'PHE', 9.44), ('CG', 'ASP', 'CD2', 'PHE', 9.16), ('CG', 'ASP', 'CE1', 'PHE', 10.77), ('CG', 'ASP', 'CE2', 'PHE', 10.51), ('CG', 'ASP', 'CZ', 'PHE', 11.24)], [('OD1', 'ASP', 'CB', 'PHE', 6.91), ('OD1', 'ASP', 'CG', 'PHE', 8.33), ('OD1', 'ASP', 'CD1', 'PHE', 9.37), ('OD1', 'ASP', 'CD2', 'PHE', 8.87), ('OD1', 'ASP', 'CE1', 'PHE', 10.7), ('OD1', 'ASP', 'CE2', 'PHE', 10.26), ('OD1', 'ASP', 'CZ', 'PHE', 11.08)], [('OD2', 'ASP', 'CB', 'PHE', 7.45), ('OD2', 'ASP', 'CG', 'PHE', 8.66), ('OD2', 'ASP', 'CD1', 'PHE', 9.6), ('OD2', 'ASP', 'CD2', 'PHE', 9.17), ('OD2', 'ASP', 'CE1', 'PHE', 10.85), ('OD2', 'ASP', 'CE2', 'PHE', 10.46), ('OD2', 'ASP', 'CZ', 'PHE', 11.23)], [('CB', 'ASP', 'CB', 'PHE', 12.44), ('CB', 'ASP', 'CG', 'PHE', 13.9), ('CB', 'ASP', 'CD1', 'PHE', 14.77), ('CB', 'ASP', 'CD2', 'PHE', 14.54), ('CB', 'ASP', 'CE1', 'PHE', 16.16), ('CB', 'ASP', 'CE2', 'PHE', 15.92), ('CB', 'ASP', 'CZ', 'PHE', 16.68)], [('CG', 'ASP', 'CB', 'PHE', 10.99), ('CG', 'ASP', 'CG', 'PHE', 12.44), ('CG', 'ASP', 'CD1', 'PHE', 13.35), ('CG', 'ASP', 'CD2', 'PHE', 13.05), ('CG', 'ASP', 'CE1', 'PHE', 14.72), ('CG', 'ASP', 'CE2', 'PHE', 14.43), ('CG', 'ASP', 'CZ', 'PHE', 15.21)], [('OD1', 'ASP', 'CB', 'PHE', 10.28), ('OD1', 'ASP', 'CG', 'PHE', 11.77), ('OD1', 'ASP', 'CD1', 'PHE', 12.68), ('OD1', 'ASP', 'CD2', 'PHE', 12.4), ('OD1', 'ASP', 'CE1', 'PHE', 14.06), ('OD1', 'ASP', 'CE2', 'PHE', 13.8), ('OD1', 'ASP', 'CZ', 'PHE', 14.57)], [('OD2', 'ASP', 'CB', 'PHE', 10.7), ('OD2', 'ASP', 'CG', 'PHE', 12.08), ('OD2', 'ASP', 'CD1', 'PHE', 13.0), ('OD2', 'ASP', 'CD2', 'PHE', 12.63), ('OD2', 'ASP', 'CE1', 'PHE', 14.34), ('OD2', 'ASP', 'CE2', 'PHE', 13.98), ('OD2', 'ASP', 'CZ', 'PHE', 14.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MG_ASPII, d, 'M_1l7n_3_1_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_MG, d, 'M_1l7n_3_1_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(PHE_MG, d, 'M_1l7n_3_1_3_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ASP, d, 'M_1l7n_3_1_3_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_LYS, d, 'M_1l7n_3_1_3_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(PHE_ASPII, d, 'M_1l7n_3_1_3_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(LYS_ASPI, d, 'M_1l7n_3_1_3_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(LYS_PHE, d, 'M_1l7n_3_1_3_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(PHE_ASPI, d, 'M_1l7n_3_1_3_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLY_MG, d, 'M_1l7n_3_1_3_3')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(MG_ASPI, d, 'M_1l7n_3_1_3_3')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(ASP_ASPI, d, 'M_1l7n_3_1_3_3')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(LYS_MG, d, 'M_1l7n_3_1_3_3')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(ASP_LYS, d, 'M_1l7n_3_1_3_3')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(ASP_GLY, d, 'M_1l7n_3_1_3_3')
	if match15 == []:
		 flag = True
		 break
	match16 , totTime16 = cmd.detect(GLY_PHE, d, 'M_1l7n_3_1_3_3')
	if match16 == []:
		 flag = True
		 break
	match17 , totTime17 = cmd.detect(ASP_PHE, d, 'M_1l7n_3_1_3_3')
	if match17 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MG_ASPII' :  match1,
		'ASP_MG' :  match2,
		'PHE_MG' :  match3,
		'ASP_ASP' :  match4,
		'GLY_LYS' :  match5,
		'PHE_ASPII' :  match6,
		'LYS_ASPI' :  match7,
		'LYS_PHE' :  match8,
		'PHE_ASPI' :  match9,
		'GLY_MG' :  match10,
		'MG_ASPI' :  match11,
		'ASP_ASPI' :  match12,
		'LYS_MG' :  match13,
		'ASP_LYS' :  match14,
		'ASP_GLY' :  match15,
		'GLY_PHE' :  match16,
		'ASP_PHE' :  match17}