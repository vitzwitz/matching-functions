'''
FUNC:A_1aql_3_1_1_13
PDB:1aql
EC:3.1.1.13
RESI:gly,ala,ser,ala,asp,his
LOCI:a-107,108,194,195,320,435;
'''
import motifFunctions as cmd
GLY_SER = { 
	'distances':
		[[9.61, 10.2], [8.39, 8.99], [7.98, 8.63], [7.28, 8.18]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'SER', 9.61), ('O', 'GLY', 'OG', 'SER', 10.2)], [('C', 'GLY', 'CB', 'SER', 8.39), ('C', 'GLY', 'OG', 'SER', 8.99)], [('CA', 'GLY', 'CB', 'SER', 7.98), ('CA', 'GLY', 'OG', 'SER', 8.63)], [('N', 'GLY', 'CB', 'SER', 7.28), ('N', 'GLY', 'OG', 'SER', 8.18)]]}
ASP_ALAI = { 
	'distances':
		[[15.53, 16.06, 15.34, 14.63, 13.36], [14.58, 14.99, 14.25, 13.64, 12.33], [14.2, 14.81, 13.98, 13.36, 11.99], [14.37, 14.47, 13.82, 13.33, 12.06]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ALAI', 15.53), ('CB', 'ASP', 'O', 'ALAI', 16.06), ('CB', 'ASP', 'C', 'ALAI', 15.34), ('CB', 'ASP', 'CA', 'ALAI', 14.63), ('CB', 'ASP', 'N', 'ALAI', 13.36)], [('CG', 'ASP', 'CB', 'ALAI', 14.58), ('CG', 'ASP', 'O', 'ALAI', 14.99), ('CG', 'ASP', 'C', 'ALAI', 14.25), ('CG', 'ASP', 'CA', 'ALAI', 13.64), ('CG', 'ASP', 'N', 'ALAI', 12.33)], [('OD1', 'ASP', 'CB', 'ALAI', 14.2), ('OD1', 'ASP', 'O', 'ALAI', 14.81), ('OD1', 'ASP', 'C', 'ALAI', 13.98), ('OD1', 'ASP', 'CA', 'ALAI', 13.36), ('OD1', 'ASP', 'N', 'ALAI', 11.99)], [('OD2', 'ASP', 'CB', 'ALAI', 14.37), ('OD2', 'ASP', 'O', 'ALAI', 14.47), ('OD2', 'ASP', 'C', 'ALAI', 13.82), ('OD2', 'ASP', 'CA', 'ALAI', 13.33), ('OD2', 'ASP', 'N', 'ALAI', 12.06)]]}
ASP_HIS = { 
	'distances':
		[[6.84, 7.03, 6.36, 8.18, 7.27, 8.28], [6.49, 6.41, 5.49, 7.56, 6.36, 7.51], [5.48, 5.48, 4.7, 6.71, 5.78, 6.83], [7.53, 7.22, 6.08, 8.24, 6.66, 7.93]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.84), ('CB', 'ASP', 'CG', 'HIS', 7.03), ('CB', 'ASP', 'ND1', 'HIS', 6.36), ('CB', 'ASP', 'CD2', 'HIS', 8.18), ('CB', 'ASP', 'CE1', 'HIS', 7.27), ('CB', 'ASP', 'NE2', 'HIS', 8.28)], [('CG', 'ASP', 'CB', 'HIS', 6.49), ('CG', 'ASP', 'CG', 'HIS', 6.41), ('CG', 'ASP', 'ND1', 'HIS', 5.49), ('CG', 'ASP', 'CD2', 'HIS', 7.56), ('CG', 'ASP', 'CE1', 'HIS', 6.36), ('CG', 'ASP', 'NE2', 'HIS', 7.51)], [('OD1', 'ASP', 'CB', 'HIS', 5.48), ('OD1', 'ASP', 'CG', 'HIS', 5.48), ('OD1', 'ASP', 'ND1', 'HIS', 4.7), ('OD1', 'ASP', 'CD2', 'HIS', 6.71), ('OD1', 'ASP', 'CE1', 'HIS', 5.78), ('OD1', 'ASP', 'NE2', 'HIS', 6.83)], [('OD2', 'ASP', 'CB', 'HIS', 7.53), ('OD2', 'ASP', 'CG', 'HIS', 7.22), ('OD2', 'ASP', 'ND1', 'HIS', 6.08), ('OD2', 'ASP', 'CD2', 'HIS', 8.24), ('OD2', 'ASP', 'CE1', 'HIS', 6.66), ('OD2', 'ASP', 'NE2', 'HIS', 7.93)]]}
SER_ALAI = { 
	'distances':
		[[6.64, 7.93, 6.82, 6.07, 4.63], [7.84, 9.22, 8.15, 7.3, 5.89]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ALAI', 6.64), ('CB', 'SER', 'O', 'ALAI', 7.93), ('CB', 'SER', 'C', 'ALAI', 6.82), ('CB', 'SER', 'CA', 'ALAI', 6.07), ('CB', 'SER', 'N', 'ALAI', 4.63)], [('OG', 'SER', 'CB', 'ALAI', 7.84), ('OG', 'SER', 'O', 'ALAI', 9.22), ('OG', 'SER', 'C', 'ALAI', 8.15), ('OG', 'SER', 'CA', 'ALAI', 7.3), ('OG', 'SER', 'N', 'ALAI', 5.89)]]}
GLY_ALA = { 
	'distances':
		[[5.15, 5.78, 4.9, 4.82, 4.26], [5.1, 6.11, 5.02, 4.46, 3.33], [6.45, 7.57, 6.42, 5.81, 4.42], [7.29, 7.92, 6.71, 6.27, 4.89], [7.46, 10.67, 9.85, 8.82, 9.0], [6.67, 9.92, 9.0, 7.94, 7.95], [6.86, 9.92, 8.9, 8.03, 7.85], [5.82, 8.67, 7.63, 6.94, 6.83]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ALA', 5.15), ('O', 'GLY', 'O', 'ALA', 5.78), ('O', 'GLY', 'C', 'ALA', 4.9), ('O', 'GLY', 'CA', 'ALA', 4.82), ('O', 'GLY', 'N', 'ALA', 4.26)], [('C', 'GLY', 'CB', 'ALA', 5.1), ('C', 'GLY', 'O', 'ALA', 6.11), ('C', 'GLY', 'C', 'ALA', 5.02), ('C', 'GLY', 'CA', 'ALA', 4.46), ('C', 'GLY', 'N', 'ALA', 3.33)], [('CA', 'GLY', 'CB', 'ALA', 6.45), ('CA', 'GLY', 'O', 'ALA', 7.57), ('CA', 'GLY', 'C', 'ALA', 6.42), ('CA', 'GLY', 'CA', 'ALA', 5.81), ('CA', 'GLY', 'N', 'ALA', 4.42)], [('N', 'GLY', 'CB', 'ALA', 7.29), ('N', 'GLY', 'O', 'ALA', 7.92), ('N', 'GLY', 'C', 'ALA', 6.71), ('N', 'GLY', 'CA', 'ALA', 6.27), ('N', 'GLY', 'N', 'ALA', 4.89)], [('O', 'GLY', 'CB', 'ALA', 7.46), ('O', 'GLY', 'O', 'ALA', 10.67), ('O', 'GLY', 'C', 'ALA', 9.85), ('O', 'GLY', 'CA', 'ALA', 8.82), ('O', 'GLY', 'N', 'ALA', 9.0)], [('C', 'GLY', 'CB', 'ALA', 6.67), ('C', 'GLY', 'O', 'ALA', 9.92), ('C', 'GLY', 'C', 'ALA', 9.0), ('C', 'GLY', 'CA', 'ALA', 7.94), ('C', 'GLY', 'N', 'ALA', 7.95)], [('CA', 'GLY', 'CB', 'ALA', 6.86), ('CA', 'GLY', 'O', 'ALA', 9.92), ('CA', 'GLY', 'C', 'ALA', 8.9), ('CA', 'GLY', 'CA', 'ALA', 8.03), ('CA', 'GLY', 'N', 'ALA', 7.85)], [('N', 'GLY', 'CB', 'ALA', 5.82), ('N', 'GLY', 'O', 'ALA', 8.67), ('N', 'GLY', 'C', 'ALA', 7.63), ('N', 'GLY', 'CA', 'ALA', 6.94), ('N', 'GLY', 'N', 'ALA', 6.83)]]}
ALA_HIS = { 
	'distances':
		[[13.09, 12.01, 12.37, 10.68, 11.39, 10.27], [15.39, 14.16, 14.27, 12.87, 13.13, 12.19], [14.62, 13.36, 13.47, 12.06, 12.33, 11.37], [13.14, 11.92, 12.11, 10.6, 11.01, 9.98], [12.62, 11.4, 11.62, 10.08, 10.55, 9.49], [13.63, 12.18, 11.86, 11.1, 10.58, 10.02], [15.09, 13.6, 12.92, 12.78, 11.65, 11.52], [14.08, 12.6, 11.99, 11.74, 10.72, 10.51], [13.19, 11.7, 11.19, 10.74, 9.89, 9.54], [11.8, 10.32, 9.8, 9.4, 8.52, 8.19]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'HIS', 13.09), ('CB', 'ALA', 'CG', 'HIS', 12.01), ('CB', 'ALA', 'ND1', 'HIS', 12.37), ('CB', 'ALA', 'CD2', 'HIS', 10.68), ('CB', 'ALA', 'CE1', 'HIS', 11.39), ('CB', 'ALA', 'NE2', 'HIS', 10.27)], [('O', 'ALA', 'CB', 'HIS', 15.39), ('O', 'ALA', 'CG', 'HIS', 14.16), ('O', 'ALA', 'ND1', 'HIS', 14.27), ('O', 'ALA', 'CD2', 'HIS', 12.87), ('O', 'ALA', 'CE1', 'HIS', 13.13), ('O', 'ALA', 'NE2', 'HIS', 12.19)], [('C', 'ALA', 'CB', 'HIS', 14.62), ('C', 'ALA', 'CG', 'HIS', 13.36), ('C', 'ALA', 'ND1', 'HIS', 13.47), ('C', 'ALA', 'CD2', 'HIS', 12.06), ('C', 'ALA', 'CE1', 'HIS', 12.33), ('C', 'ALA', 'NE2', 'HIS', 11.37)], [('CA', 'ALA', 'CB', 'HIS', 13.14), ('CA', 'ALA', 'CG', 'HIS', 11.92), ('CA', 'ALA', 'ND1', 'HIS', 12.11), ('CA', 'ALA', 'CD2', 'HIS', 10.6), ('CA', 'ALA', 'CE1', 'HIS', 11.01), ('CA', 'ALA', 'NE2', 'HIS', 9.98)], [('N', 'ALA', 'CB', 'HIS', 12.62), ('N', 'ALA', 'CG', 'HIS', 11.4), ('N', 'ALA', 'ND1', 'HIS', 11.62), ('N', 'ALA', 'CD2', 'HIS', 10.08), ('N', 'ALA', 'CE1', 'HIS', 10.55), ('N', 'ALA', 'NE2', 'HIS', 9.49)], [('CB', 'ALA', 'CB', 'HIS', 13.63), ('CB', 'ALA', 'CG', 'HIS', 12.18), ('CB', 'ALA', 'ND1', 'HIS', 11.86), ('CB', 'ALA', 'CD2', 'HIS', 11.1), ('CB', 'ALA', 'CE1', 'HIS', 10.58), ('CB', 'ALA', 'NE2', 'HIS', 10.02)], [('O', 'ALA', 'CB', 'HIS', 15.09), ('O', 'ALA', 'CG', 'HIS', 13.6), ('O', 'ALA', 'ND1', 'HIS', 12.92), ('O', 'ALA', 'CD2', 'HIS', 12.78), ('O', 'ALA', 'CE1', 'HIS', 11.65), ('O', 'ALA', 'NE2', 'HIS', 11.52)], [('C', 'ALA', 'CB', 'HIS', 14.08), ('C', 'ALA', 'CG', 'HIS', 12.6), ('C', 'ALA', 'ND1', 'HIS', 11.99), ('C', 'ALA', 'CD2', 'HIS', 11.74), ('C', 'ALA', 'CE1', 'HIS', 10.72), ('C', 'ALA', 'NE2', 'HIS', 10.51)], [('CA', 'ALA', 'CB', 'HIS', 13.19), ('CA', 'ALA', 'CG', 'HIS', 11.7), ('CA', 'ALA', 'ND1', 'HIS', 11.19), ('CA', 'ALA', 'CD2', 'HIS', 10.74), ('CA', 'ALA', 'CE1', 'HIS', 9.89), ('CA', 'ALA', 'NE2', 'HIS', 9.54)], [('N', 'ALA', 'CB', 'HIS', 11.8), ('N', 'ALA', 'CG', 'HIS', 10.32), ('N', 'ALA', 'ND1', 'HIS', 9.8), ('N', 'ALA', 'CD2', 'HIS', 9.4), ('N', 'ALA', 'CE1', 'HIS', 8.52), ('N', 'ALA', 'NE2', 'HIS', 8.19)]]}
HIS_ALAI = { 
	'distances':
		[[13.63, 15.09, 14.08, 13.19, 11.8], [12.18, 13.6, 12.6, 11.7, 10.32], [11.86, 12.92, 11.99, 11.19, 9.8], [11.1, 12.78, 11.74, 10.74, 9.4], [10.58, 11.65, 10.72, 9.89, 8.52], [10.02, 11.52, 10.51, 9.54, 8.19]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ALAI', 13.63), ('CB', 'HIS', 'O', 'ALAI', 15.09), ('CB', 'HIS', 'C', 'ALAI', 14.08), ('CB', 'HIS', 'CA', 'ALAI', 13.19), ('CB', 'HIS', 'N', 'ALAI', 11.8)], [('CG', 'HIS', 'CB', 'ALAI', 12.18), ('CG', 'HIS', 'O', 'ALAI', 13.6), ('CG', 'HIS', 'C', 'ALAI', 12.6), ('CG', 'HIS', 'CA', 'ALAI', 11.7), ('CG', 'HIS', 'N', 'ALAI', 10.32)], [('ND1', 'HIS', 'CB', 'ALAI', 11.86), ('ND1', 'HIS', 'O', 'ALAI', 12.92), ('ND1', 'HIS', 'C', 'ALAI', 11.99), ('ND1', 'HIS', 'CA', 'ALAI', 11.19), ('ND1', 'HIS', 'N', 'ALAI', 9.8)], [('CD2', 'HIS', 'CB', 'ALAI', 11.1), ('CD2', 'HIS', 'O', 'ALAI', 12.78), ('CD2', 'HIS', 'C', 'ALAI', 11.74), ('CD2', 'HIS', 'CA', 'ALAI', 10.74), ('CD2', 'HIS', 'N', 'ALAI', 9.4)], [('CE1', 'HIS', 'CB', 'ALAI', 10.58), ('CE1', 'HIS', 'O', 'ALAI', 11.65), ('CE1', 'HIS', 'C', 'ALAI', 10.72), ('CE1', 'HIS', 'CA', 'ALAI', 9.89), ('CE1', 'HIS', 'N', 'ALAI', 8.52)], [('NE2', 'HIS', 'CB', 'ALAI', 10.02), ('NE2', 'HIS', 'O', 'ALAI', 11.52), ('NE2', 'HIS', 'C', 'ALAI', 10.51), ('NE2', 'HIS', 'CA', 'ALAI', 9.54), ('NE2', 'HIS', 'N', 'ALAI', 8.19)]]}
GLY_HIS = { 
	'distances':
		[[14.4, 13.28, 13.63, 11.94, 12.62, 11.51], [13.33, 12.17, 12.48, 10.84, 11.46, 10.37], [12.96, 11.84, 12.16, 10.55, 11.2, 10.13], [13.09, 11.87, 12.0, 10.64, 10.96, 10.04]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 14.4), ('O', 'GLY', 'CG', 'HIS', 13.28), ('O', 'GLY', 'ND1', 'HIS', 13.63), ('O', 'GLY', 'CD2', 'HIS', 11.94), ('O', 'GLY', 'CE1', 'HIS', 12.62), ('O', 'GLY', 'NE2', 'HIS', 11.51)], [('C', 'GLY', 'CB', 'HIS', 13.33), ('C', 'GLY', 'CG', 'HIS', 12.17), ('C', 'GLY', 'ND1', 'HIS', 12.48), ('C', 'GLY', 'CD2', 'HIS', 10.84), ('C', 'GLY', 'CE1', 'HIS', 11.46), ('C', 'GLY', 'NE2', 'HIS', 10.37)], [('CA', 'GLY', 'CB', 'HIS', 12.96), ('CA', 'GLY', 'CG', 'HIS', 11.84), ('CA', 'GLY', 'ND1', 'HIS', 12.16), ('CA', 'GLY', 'CD2', 'HIS', 10.55), ('CA', 'GLY', 'CE1', 'HIS', 11.2), ('CA', 'GLY', 'NE2', 'HIS', 10.13)], [('N', 'GLY', 'CB', 'HIS', 13.09), ('N', 'GLY', 'CG', 'HIS', 11.87), ('N', 'GLY', 'ND1', 'HIS', 12.0), ('N', 'GLY', 'CD2', 'HIS', 10.64), ('N', 'GLY', 'CE1', 'HIS', 10.96), ('N', 'GLY', 'NE2', 'HIS', 10.04)]]}
ALA_ASP = { 
	'distances':
		[[15.99, 15.52, 15.02, 15.82], [17.75, 17.22, 16.86, 17.32], [17.13, 16.51, 16.08, 16.61], [15.81, 15.22, 14.75, 15.4], [15.58, 14.87, 14.29, 15.05], [15.53, 14.58, 14.2, 14.37], [16.06, 14.99, 14.81, 14.47], [15.34, 14.25, 13.98, 13.82], [14.63, 13.64, 13.36, 13.33], [13.36, 12.33, 11.99, 12.06]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ASP', 15.99), ('CB', 'ALA', 'CG', 'ASP', 15.52), ('CB', 'ALA', 'OD1', 'ASP', 15.02), ('CB', 'ALA', 'OD2', 'ASP', 15.82)], [('O', 'ALA', 'CB', 'ASP', 17.75), ('O', 'ALA', 'CG', 'ASP', 17.22), ('O', 'ALA', 'OD1', 'ASP', 16.86), ('O', 'ALA', 'OD2', 'ASP', 17.32)], [('C', 'ALA', 'CB', 'ASP', 17.13), ('C', 'ALA', 'CG', 'ASP', 16.51), ('C', 'ALA', 'OD1', 'ASP', 16.08), ('C', 'ALA', 'OD2', 'ASP', 16.61)], [('CA', 'ALA', 'CB', 'ASP', 15.81), ('CA', 'ALA', 'CG', 'ASP', 15.22), ('CA', 'ALA', 'OD1', 'ASP', 14.75), ('CA', 'ALA', 'OD2', 'ASP', 15.4)], [('N', 'ALA', 'CB', 'ASP', 15.58), ('N', 'ALA', 'CG', 'ASP', 14.87), ('N', 'ALA', 'OD1', 'ASP', 14.29), ('N', 'ALA', 'OD2', 'ASP', 15.05)], [('CB', 'ALA', 'CB', 'ASP', 15.53), ('CB', 'ALA', 'CG', 'ASP', 14.58), ('CB', 'ALA', 'OD1', 'ASP', 14.2), ('CB', 'ALA', 'OD2', 'ASP', 14.37)], [('O', 'ALA', 'CB', 'ASP', 16.06), ('O', 'ALA', 'CG', 'ASP', 14.99), ('O', 'ALA', 'OD1', 'ASP', 14.81), ('O', 'ALA', 'OD2', 'ASP', 14.47)], [('C', 'ALA', 'CB', 'ASP', 15.34), ('C', 'ALA', 'CG', 'ASP', 14.25), ('C', 'ALA', 'OD1', 'ASP', 13.98), ('C', 'ALA', 'OD2', 'ASP', 13.82)], [('CA', 'ALA', 'CB', 'ASP', 14.63), ('CA', 'ALA', 'CG', 'ASP', 13.64), ('CA', 'ALA', 'OD1', 'ASP', 13.36), ('CA', 'ALA', 'OD2', 'ASP', 13.33)], [('N', 'ALA', 'CB', 'ASP', 13.36), ('N', 'ALA', 'CG', 'ASP', 12.33), ('N', 'ALA', 'OD1', 'ASP', 11.99), ('N', 'ALA', 'OD2', 'ASP', 12.06)]]}
SER_ASP = { 
	'distances':
		[[11.38, 10.29, 9.75, 10.2], [10.14, 9.12, 8.53, 9.18]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 11.38), ('CB', 'SER', 'CG', 'ASP', 10.29), ('CB', 'SER', 'OD1', 'ASP', 9.75), ('CB', 'SER', 'OD2', 'ASP', 10.2)], [('OG', 'SER', 'CB', 'ASP', 10.14), ('OG', 'SER', 'CG', 'ASP', 9.12), ('OG', 'SER', 'OD1', 'ASP', 8.53), ('OG', 'SER', 'OD2', 'ASP', 9.18)]]}
ALA_SER = { 
	'distances':
		[[9.33, 9.53], [10.42, 10.99], [9.4, 10.03], [8.38, 8.83], [7.6, 8.15], [6.64, 7.84], [7.93, 9.22], [6.82, 8.15], [6.07, 7.3], [4.63, 5.89]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'SER', 9.33), ('CB', 'ALA', 'OG', 'SER', 9.53)], [('O', 'ALA', 'CB', 'SER', 10.42), ('O', 'ALA', 'OG', 'SER', 10.99)], [('C', 'ALA', 'CB', 'SER', 9.4), ('C', 'ALA', 'OG', 'SER', 10.03)], [('CA', 'ALA', 'CB', 'SER', 8.38), ('CA', 'ALA', 'OG', 'SER', 8.83)], [('N', 'ALA', 'CB', 'SER', 7.6), ('N', 'ALA', 'OG', 'SER', 8.15)], [('CB', 'ALA', 'CB', 'SER', 6.64), ('CB', 'ALA', 'OG', 'SER', 7.84)], [('O', 'ALA', 'CB', 'SER', 7.93), ('O', 'ALA', 'OG', 'SER', 9.22)], [('C', 'ALA', 'CB', 'SER', 6.82), ('C', 'ALA', 'OG', 'SER', 8.15)], [('CA', 'ALA', 'CB', 'SER', 6.07), ('CA', 'ALA', 'OG', 'SER', 7.3)], [('N', 'ALA', 'CB', 'SER', 4.63), ('N', 'ALA', 'OG', 'SER', 5.89)]]}
SER_HIS = { 
	'distances':
		[[9.32, 7.87, 7.45, 7.0, 6.25, 5.87], [7.94, 6.48, 6.1, 5.63, 4.92, 4.46]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.32), ('CB', 'SER', 'CG', 'HIS', 7.87), ('CB', 'SER', 'ND1', 'HIS', 7.45), ('CB', 'SER', 'CD2', 'HIS', 7.0), ('CB', 'SER', 'CE1', 'HIS', 6.25), ('CB', 'SER', 'NE2', 'HIS', 5.87)], [('OG', 'SER', 'CB', 'HIS', 7.94), ('OG', 'SER', 'CG', 'HIS', 6.48), ('OG', 'SER', 'ND1', 'HIS', 6.1), ('OG', 'SER', 'CD2', 'HIS', 5.63), ('OG', 'SER', 'CE1', 'HIS', 4.92), ('OG', 'SER', 'NE2', 'HIS', 4.46)]]}
ALA_ALA = { 
	'distances':
		[[7.98, 11.13, 10.36, 8.96, 8.97], [7.4, 10.17, 9.73, 8.52, 9.11], [6.45, 9.44, 8.87, 7.65, 8.16], [6.45, 9.61, 8.86, 7.5, 7.64], [6.02, 9.3, 8.39, 7.14, 7.1], [7.98, 7.4, 6.45, 6.45, 6.02], [11.13, 10.17, 9.44, 9.61, 9.3], [10.36, 9.73, 8.87, 8.86, 8.39], [8.96, 8.52, 7.65, 7.5, 7.14], [8.97, 9.11, 8.16, 7.64, 7.1]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ALA', 7.98), ('CB', 'ALA', 'O', 'ALA', 11.13), ('CB', 'ALA', 'C', 'ALA', 10.36), ('CB', 'ALA', 'CA', 'ALA', 8.96), ('CB', 'ALA', 'N', 'ALA', 8.97)], [('O', 'ALA', 'CB', 'ALA', 7.4), ('O', 'ALA', 'O', 'ALA', 10.17), ('O', 'ALA', 'C', 'ALA', 9.73), ('O', 'ALA', 'CA', 'ALA', 8.52), ('O', 'ALA', 'N', 'ALA', 9.11)], [('C', 'ALA', 'CB', 'ALA', 6.45), ('C', 'ALA', 'O', 'ALA', 9.44), ('C', 'ALA', 'C', 'ALA', 8.87), ('C', 'ALA', 'CA', 'ALA', 7.65), ('C', 'ALA', 'N', 'ALA', 8.16)], [('CA', 'ALA', 'CB', 'ALA', 6.45), ('CA', 'ALA', 'O', 'ALA', 9.61), ('CA', 'ALA', 'C', 'ALA', 8.86), ('CA', 'ALA', 'CA', 'ALA', 7.5), ('CA', 'ALA', 'N', 'ALA', 7.64)], [('N', 'ALA', 'CB', 'ALA', 6.02), ('N', 'ALA', 'O', 'ALA', 9.3), ('N', 'ALA', 'C', 'ALA', 8.39), ('N', 'ALA', 'CA', 'ALA', 7.14), ('N', 'ALA', 'N', 'ALA', 7.1)], [('CB', 'ALA', 'CB', 'ALA', 7.98), ('CB', 'ALA', 'O', 'ALA', 7.4), ('CB', 'ALA', 'C', 'ALA', 6.45), ('CB', 'ALA', 'CA', 'ALA', 6.45), ('CB', 'ALA', 'N', 'ALA', 6.02)], [('O', 'ALA', 'CB', 'ALA', 11.13), ('O', 'ALA', 'O', 'ALA', 10.17), ('O', 'ALA', 'C', 'ALA', 9.44), ('O', 'ALA', 'CA', 'ALA', 9.61), ('O', 'ALA', 'N', 'ALA', 9.3)], [('C', 'ALA', 'CB', 'ALA', 10.36), ('C', 'ALA', 'O', 'ALA', 9.73), ('C', 'ALA', 'C', 'ALA', 8.87), ('C', 'ALA', 'CA', 'ALA', 8.86), ('C', 'ALA', 'N', 'ALA', 8.39)], [('CA', 'ALA', 'CB', 'ALA', 8.96), ('CA', 'ALA', 'O', 'ALA', 8.52), ('CA', 'ALA', 'C', 'ALA', 7.65), ('CA', 'ALA', 'CA', 'ALA', 7.5), ('CA', 'ALA', 'N', 'ALA', 7.14)], [('N', 'ALA', 'CB', 'ALA', 8.97), ('N', 'ALA', 'O', 'ALA', 9.11), ('N', 'ALA', 'C', 'ALA', 8.16), ('N', 'ALA', 'CA', 'ALA', 7.64), ('N', 'ALA', 'N', 'ALA', 7.1)]]}
GLY_ASP = { 
	'distances':
		[[17.68, 16.96, 16.32, 17.2], [16.57, 15.81, 15.16, 16.03], [16.4, 15.54, 14.79, 15.75], [16.23, 15.26, 14.56, 15.35]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 17.68), ('O', 'GLY', 'CG', 'ASP', 16.96), ('O', 'GLY', 'OD1', 'ASP', 16.32), ('O', 'GLY', 'OD2', 'ASP', 17.2)], [('C', 'GLY', 'CB', 'ASP', 16.57), ('C', 'GLY', 'CG', 'ASP', 15.81), ('C', 'GLY', 'OD1', 'ASP', 15.16), ('C', 'GLY', 'OD2', 'ASP', 16.03)], [('CA', 'GLY', 'CB', 'ASP', 16.4), ('CA', 'GLY', 'CG', 'ASP', 15.54), ('CA', 'GLY', 'OD1', 'ASP', 14.79), ('CA', 'GLY', 'OD2', 'ASP', 15.75)], [('N', 'GLY', 'CB', 'ASP', 16.23), ('N', 'GLY', 'CG', 'ASP', 15.26), ('N', 'GLY', 'OD1', 'ASP', 14.56), ('N', 'GLY', 'OD2', 'ASP', 15.35)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_SER, d, 'A_1aql_3_1_1_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ALAI, d, 'A_1aql_3_1_1_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'A_1aql_3_1_1_13')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_ALAI, d, 'A_1aql_3_1_1_13')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_ALA, d, 'A_1aql_3_1_1_13')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ALA_HIS, d, 'A_1aql_3_1_1_13')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_ALAI, d, 'A_1aql_3_1_1_13')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLY_HIS, d, 'A_1aql_3_1_1_13')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ALA_ASP, d, 'A_1aql_3_1_1_13')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'A_1aql_3_1_1_13')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ALA_SER, d, 'A_1aql_3_1_1_13')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(SER_HIS, d, 'A_1aql_3_1_1_13')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(ALA_ALA, d, 'A_1aql_3_1_1_13')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(GLY_ASP, d, 'A_1aql_3_1_1_13')
	if match14 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_SER' :  match1,
		'ASP_ALAI' :  match2,
		'ASP_HIS' :  match3,
		'SER_ALAI' :  match4,
		'GLY_ALA' :  match5,
		'ALA_HIS' :  match6,
		'HIS_ALAI' :  match7,
		'GLY_HIS' :  match8,
		'ALA_ASP' :  match9,
		'SER_ASP' :  match10,
		'ALA_SER' :  match11,
		'SER_HIS' :  match12,
		'ALA_ALA' :  match13,
		'GLY_ASP' :  match14}