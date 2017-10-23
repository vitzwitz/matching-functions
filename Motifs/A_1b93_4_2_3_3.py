'''
FUNC:A_1b93_4_2_3_3
PDB:1b93
EC:4.2.3.3
RESI:his,gly,asp,asp,his,asp
LOCI:a-19,66,71,91,98,101;
'''
import motifFunctions as cmd
ASP_HISI = { 
	'distances':
		[[5.95, 6.2, 5.54, 7.49, 6.65, 7.68], [7.05, 7.55, 7.0, 8.86, 8.12, 9.13], [8.14, 8.57, 7.9, 9.86, 8.93, 10.03], [7.1, 7.8, 7.46, 9.11, 8.64, 9.53]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HISI', 5.95), ('CB', 'ASP', 'CG', 'HISI', 6.2), ('CB', 'ASP', 'ND1', 'HISI', 5.54), ('CB', 'ASP', 'CD2', 'HISI', 7.49), ('CB', 'ASP', 'CE1', 'HISI', 6.65), ('CB', 'ASP', 'NE2', 'HISI', 7.68)], [('CG', 'ASP', 'CB', 'HISI', 7.05), ('CG', 'ASP', 'CG', 'HISI', 7.55), ('CG', 'ASP', 'ND1', 'HISI', 7.0), ('CG', 'ASP', 'CD2', 'HISI', 8.86), ('CG', 'ASP', 'CE1', 'HISI', 8.12), ('CG', 'ASP', 'NE2', 'HISI', 9.13)], [('OD1', 'ASP', 'CB', 'HISI', 8.14), ('OD1', 'ASP', 'CG', 'HISI', 8.57), ('OD1', 'ASP', 'ND1', 'HISI', 7.9), ('OD1', 'ASP', 'CD2', 'HISI', 9.86), ('OD1', 'ASP', 'CE1', 'HISI', 8.93), ('OD1', 'ASP', 'NE2', 'HISI', 10.03)], [('OD2', 'ASP', 'CB', 'HISI', 7.1), ('OD2', 'ASP', 'CG', 'HISI', 7.8), ('OD2', 'ASP', 'ND1', 'HISI', 7.46), ('OD2', 'ASP', 'CD2', 'HISI', 9.11), ('OD2', 'ASP', 'CE1', 'HISI', 8.64), ('OD2', 'ASP', 'NE2', 'HISI', 9.53)]]}
ASP_GLY = { 
	'distances':
		[[6.68, 7.2, 6.86, 8.03], [6.58, 6.75, 6.16, 7.33], [6.88, 6.83, 5.87, 6.79], [6.72, 6.82, 6.42, 7.7], [7.19, 7.97, 8.53, 9.96], [7.05, 7.97, 8.84, 10.22], [7.89, 8.74, 9.71, 11.08], [6.47, 7.54, 8.48, 9.77], [15.19, 14.37, 13.88, 14.31], [16.46, 15.6, 15.14, 15.5], [17.53, 16.71, 16.24, 16.64], [16.46, 15.55, 15.12, 15.38]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 6.68), ('CB', 'ASP', 'C', 'GLY', 7.2), ('CB', 'ASP', 'CA', 'GLY', 6.86), ('CB', 'ASP', 'N', 'GLY', 8.03)], [('CG', 'ASP', 'O', 'GLY', 6.58), ('CG', 'ASP', 'C', 'GLY', 6.75), ('CG', 'ASP', 'CA', 'GLY', 6.16), ('CG', 'ASP', 'N', 'GLY', 7.33)], [('OD1', 'ASP', 'O', 'GLY', 6.88), ('OD1', 'ASP', 'C', 'GLY', 6.83), ('OD1', 'ASP', 'CA', 'GLY', 5.87), ('OD1', 'ASP', 'N', 'GLY', 6.79)], [('OD2', 'ASP', 'O', 'GLY', 6.72), ('OD2', 'ASP', 'C', 'GLY', 6.82), ('OD2', 'ASP', 'CA', 'GLY', 6.42), ('OD2', 'ASP', 'N', 'GLY', 7.7)], [('CB', 'ASP', 'O', 'GLY', 7.19), ('CB', 'ASP', 'C', 'GLY', 7.97), ('CB', 'ASP', 'CA', 'GLY', 8.53), ('CB', 'ASP', 'N', 'GLY', 9.96)], [('CG', 'ASP', 'O', 'GLY', 7.05), ('CG', 'ASP', 'C', 'GLY', 7.97), ('CG', 'ASP', 'CA', 'GLY', 8.84), ('CG', 'ASP', 'N', 'GLY', 10.22)], [('OD1', 'ASP', 'O', 'GLY', 7.89), ('OD1', 'ASP', 'C', 'GLY', 8.74), ('OD1', 'ASP', 'CA', 'GLY', 9.71), ('OD1', 'ASP', 'N', 'GLY', 11.08)], [('OD2', 'ASP', 'O', 'GLY', 6.47), ('OD2', 'ASP', 'C', 'GLY', 7.54), ('OD2', 'ASP', 'CA', 'GLY', 8.48), ('OD2', 'ASP', 'N', 'GLY', 9.77)], [('CB', 'ASP', 'O', 'GLY', 15.19), ('CB', 'ASP', 'C', 'GLY', 14.37), ('CB', 'ASP', 'CA', 'GLY', 13.88), ('CB', 'ASP', 'N', 'GLY', 14.31)], [('CG', 'ASP', 'O', 'GLY', 16.46), ('CG', 'ASP', 'C', 'GLY', 15.6), ('CG', 'ASP', 'CA', 'GLY', 15.14), ('CG', 'ASP', 'N', 'GLY', 15.5)], [('OD1', 'ASP', 'O', 'GLY', 17.53), ('OD1', 'ASP', 'C', 'GLY', 16.71), ('OD1', 'ASP', 'CA', 'GLY', 16.24), ('OD1', 'ASP', 'N', 'GLY', 16.64)], [('OD2', 'ASP', 'O', 'GLY', 16.46), ('OD2', 'ASP', 'C', 'GLY', 15.55), ('OD2', 'ASP', 'CA', 'GLY', 15.12), ('OD2', 'ASP', 'N', 'GLY', 15.38)]]}
ASP_ASP = { 
	'distances':
		[[5.94, 6.96, 8.13, 6.86], [6.42, 7.54, 8.59, 7.61], [7.64, 8.69, 9.75, 8.66], [5.92, 7.13, 8.03, 7.44], [15.11, 16.58, 17.43, 16.96], [13.7, 15.16, 16.03, 15.53], [13.59, 15.04, 15.94, 15.37], [12.79, 14.25, 15.11, 14.65], [5.94, 6.42, 7.64, 5.92], [6.96, 7.54, 8.69, 7.13], [8.13, 8.59, 9.75, 8.03], [6.86, 7.61, 8.66, 7.44], [15.13, 16.52, 17.32, 16.91], [16.04, 17.38, 18.21, 17.68], [16.11, 17.4, 18.2, 17.7], [16.8, 18.14, 19.03, 18.39], [15.11, 13.7, 13.59, 12.79], [16.58, 15.16, 15.04, 14.25], [17.43, 16.03, 15.94, 15.11], [16.96, 15.53, 15.37, 14.65]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 5.94), ('CB', 'ASP', 'CG', 'ASP', 6.96), ('CB', 'ASP', 'OD1', 'ASP', 8.13), ('CB', 'ASP', 'OD2', 'ASP', 6.86)], [('CG', 'ASP', 'CB', 'ASP', 6.42), ('CG', 'ASP', 'CG', 'ASP', 7.54), ('CG', 'ASP', 'OD1', 'ASP', 8.59), ('CG', 'ASP', 'OD2', 'ASP', 7.61)], [('OD1', 'ASP', 'CB', 'ASP', 7.64), ('OD1', 'ASP', 'CG', 'ASP', 8.69), ('OD1', 'ASP', 'OD1', 'ASP', 9.75), ('OD1', 'ASP', 'OD2', 'ASP', 8.66)], [('OD2', 'ASP', 'CB', 'ASP', 5.92), ('OD2', 'ASP', 'CG', 'ASP', 7.13), ('OD2', 'ASP', 'OD1', 'ASP', 8.03), ('OD2', 'ASP', 'OD2', 'ASP', 7.44)], [('CB', 'ASP', 'CB', 'ASP', 15.11), ('CB', 'ASP', 'CG', 'ASP', 16.58), ('CB', 'ASP', 'OD1', 'ASP', 17.43), ('CB', 'ASP', 'OD2', 'ASP', 16.96)], [('CG', 'ASP', 'CB', 'ASP', 13.7), ('CG', 'ASP', 'CG', 'ASP', 15.16), ('CG', 'ASP', 'OD1', 'ASP', 16.03), ('CG', 'ASP', 'OD2', 'ASP', 15.53)], [('OD1', 'ASP', 'CB', 'ASP', 13.59), ('OD1', 'ASP', 'CG', 'ASP', 15.04), ('OD1', 'ASP', 'OD1', 'ASP', 15.94), ('OD1', 'ASP', 'OD2', 'ASP', 15.37)], [('OD2', 'ASP', 'CB', 'ASP', 12.79), ('OD2', 'ASP', 'CG', 'ASP', 14.25), ('OD2', 'ASP', 'OD1', 'ASP', 15.11), ('OD2', 'ASP', 'OD2', 'ASP', 14.65)], [('CB', 'ASP', 'CB', 'ASP', 5.94), ('CB', 'ASP', 'CG', 'ASP', 6.42), ('CB', 'ASP', 'OD1', 'ASP', 7.64), ('CB', 'ASP', 'OD2', 'ASP', 5.92)], [('CG', 'ASP', 'CB', 'ASP', 6.96), ('CG', 'ASP', 'CG', 'ASP', 7.54), ('CG', 'ASP', 'OD1', 'ASP', 8.69), ('CG', 'ASP', 'OD2', 'ASP', 7.13)], [('OD1', 'ASP', 'CB', 'ASP', 8.13), ('OD1', 'ASP', 'CG', 'ASP', 8.59), ('OD1', 'ASP', 'OD1', 'ASP', 9.75), ('OD1', 'ASP', 'OD2', 'ASP', 8.03)], [('OD2', 'ASP', 'CB', 'ASP', 6.86), ('OD2', 'ASP', 'CG', 'ASP', 7.61), ('OD2', 'ASP', 'OD1', 'ASP', 8.66), ('OD2', 'ASP', 'OD2', 'ASP', 7.44)], [('CB', 'ASP', 'CB', 'ASP', 15.13), ('CB', 'ASP', 'CG', 'ASP', 16.52), ('CB', 'ASP', 'OD1', 'ASP', 17.32), ('CB', 'ASP', 'OD2', 'ASP', 16.91)], [('CG', 'ASP', 'CB', 'ASP', 16.04), ('CG', 'ASP', 'CG', 'ASP', 17.38), ('CG', 'ASP', 'OD1', 'ASP', 18.21), ('CG', 'ASP', 'OD2', 'ASP', 17.68)], [('OD1', 'ASP', 'CB', 'ASP', 16.11), ('OD1', 'ASP', 'CG', 'ASP', 17.4), ('OD1', 'ASP', 'OD1', 'ASP', 18.2), ('OD1', 'ASP', 'OD2', 'ASP', 17.7)], [('OD2', 'ASP', 'CB', 'ASP', 16.8), ('OD2', 'ASP', 'CG', 'ASP', 18.14), ('OD2', 'ASP', 'OD1', 'ASP', 19.03), ('OD2', 'ASP', 'OD2', 'ASP', 18.39)], [('CB', 'ASP', 'CB', 'ASP', 15.11), ('CB', 'ASP', 'CG', 'ASP', 13.7), ('CB', 'ASP', 'OD1', 'ASP', 13.59), ('CB', 'ASP', 'OD2', 'ASP', 12.79)], [('CG', 'ASP', 'CB', 'ASP', 16.58), ('CG', 'ASP', 'CG', 'ASP', 15.16), ('CG', 'ASP', 'OD1', 'ASP', 15.04), ('CG', 'ASP', 'OD2', 'ASP', 14.25)], [('OD1', 'ASP', 'CB', 'ASP', 17.43), ('OD1', 'ASP', 'CG', 'ASP', 16.03), ('OD1', 'ASP', 'OD1', 'ASP', 15.94), ('OD1', 'ASP', 'OD2', 'ASP', 15.11)], [('OD2', 'ASP', 'CB', 'ASP', 16.96), ('OD2', 'ASP', 'CG', 'ASP', 15.53), ('OD2', 'ASP', 'OD1', 'ASP', 15.37), ('OD2', 'ASP', 'OD2', 'ASP', 14.65)]]}
HIS_ASPI = { 
	'distances':
		[[6.18, 5.9, 5.73, 6.43], [6.75, 6.86, 6.94, 7.35], [8.11, 8.21, 8.19, 8.67], [6.55, 7.01, 7.37, 7.44], [8.65, 8.98, 9.13, 9.4], [7.85, 8.38, 8.73, 8.78], [13.29, 14.18, 14.53, 14.68], [11.92, 12.85, 13.18, 13.41], [11.79, 12.75, 12.98, 13.45], [10.73, 11.68, 12.1, 12.19], [10.56, 11.57, 11.78, 12.31], [9.81, 10.82, 11.16, 11.45]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 6.18), ('CB', 'HIS', 'CG', 'ASPI', 5.9), ('CB', 'HIS', 'OD1', 'ASPI', 5.73), ('CB', 'HIS', 'OD2', 'ASPI', 6.43)], [('CG', 'HIS', 'CB', 'ASPI', 6.75), ('CG', 'HIS', 'CG', 'ASPI', 6.86), ('CG', 'HIS', 'OD1', 'ASPI', 6.94), ('CG', 'HIS', 'OD2', 'ASPI', 7.35)], [('ND1', 'HIS', 'CB', 'ASPI', 8.11), ('ND1', 'HIS', 'CG', 'ASPI', 8.21), ('ND1', 'HIS', 'OD1', 'ASPI', 8.19), ('ND1', 'HIS', 'OD2', 'ASPI', 8.67)], [('CD2', 'HIS', 'CB', 'ASPI', 6.55), ('CD2', 'HIS', 'CG', 'ASPI', 7.01), ('CD2', 'HIS', 'OD1', 'ASPI', 7.37), ('CD2', 'HIS', 'OD2', 'ASPI', 7.44)], [('CE1', 'HIS', 'CB', 'ASPI', 8.65), ('CE1', 'HIS', 'CG', 'ASPI', 8.98), ('CE1', 'HIS', 'OD1', 'ASPI', 9.13), ('CE1', 'HIS', 'OD2', 'ASPI', 9.4)], [('NE2', 'HIS', 'CB', 'ASPI', 7.85), ('NE2', 'HIS', 'CG', 'ASPI', 8.38), ('NE2', 'HIS', 'OD1', 'ASPI', 8.73), ('NE2', 'HIS', 'OD2', 'ASPI', 8.78)], [('CB', 'HIS', 'CB', 'ASPI', 13.29), ('CB', 'HIS', 'CG', 'ASPI', 14.18), ('CB', 'HIS', 'OD1', 'ASPI', 14.53), ('CB', 'HIS', 'OD2', 'ASPI', 14.68)], [('CG', 'HIS', 'CB', 'ASPI', 11.92), ('CG', 'HIS', 'CG', 'ASPI', 12.85), ('CG', 'HIS', 'OD1', 'ASPI', 13.18), ('CG', 'HIS', 'OD2', 'ASPI', 13.41)], [('ND1', 'HIS', 'CB', 'ASPI', 11.79), ('ND1', 'HIS', 'CG', 'ASPI', 12.75), ('ND1', 'HIS', 'OD1', 'ASPI', 12.98), ('ND1', 'HIS', 'OD2', 'ASPI', 13.45)], [('CD2', 'HIS', 'CB', 'ASPI', 10.73), ('CD2', 'HIS', 'CG', 'ASPI', 11.68), ('CD2', 'HIS', 'OD1', 'ASPI', 12.1), ('CD2', 'HIS', 'OD2', 'ASPI', 12.19)], [('CE1', 'HIS', 'CB', 'ASPI', 10.56), ('CE1', 'HIS', 'CG', 'ASPI', 11.57), ('CE1', 'HIS', 'OD1', 'ASPI', 11.78), ('CE1', 'HIS', 'OD2', 'ASPI', 12.31)], [('NE2', 'HIS', 'CB', 'ASPI', 9.81), ('NE2', 'HIS', 'CG', 'ASPI', 10.82), ('NE2', 'HIS', 'OD1', 'ASPI', 11.16), ('NE2', 'HIS', 'OD2', 'ASPI', 11.45)]]}
ASP_ASPI = { 
	'distances':
		[[15.13, 16.04, 16.11, 16.8], [16.52, 17.38, 17.4, 18.14], [17.32, 18.21, 18.2, 19.03], [16.91, 17.68, 17.7, 18.39]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASPI', 15.13), ('CB', 'ASP', 'CG', 'ASPI', 16.04), ('CB', 'ASP', 'OD1', 'ASPI', 16.11), ('CB', 'ASP', 'OD2', 'ASPI', 16.8)], [('CG', 'ASP', 'CB', 'ASPI', 16.52), ('CG', 'ASP', 'CG', 'ASPI', 17.38), ('CG', 'ASP', 'OD1', 'ASPI', 17.4), ('CG', 'ASP', 'OD2', 'ASPI', 18.14)], [('OD1', 'ASP', 'CB', 'ASPI', 17.32), ('OD1', 'ASP', 'CG', 'ASPI', 18.21), ('OD1', 'ASP', 'OD1', 'ASPI', 18.2), ('OD1', 'ASP', 'OD2', 'ASPI', 19.03)], [('OD2', 'ASP', 'CB', 'ASPI', 16.91), ('OD2', 'ASP', 'CG', 'ASPI', 17.68), ('OD2', 'ASP', 'OD1', 'ASPI', 17.7), ('OD2', 'ASP', 'OD2', 'ASPI', 18.39)]]}
ASP_HIS = { 
	'distances':
		[[8.58, 8.33, 9.49, 7.34, 9.37, 8.14], [8.23, 7.66, 8.65, 6.47, 8.32, 7.02], [9.07, 8.32, 9.15, 7.05, 8.62, 7.32], [7.39, 6.76, 7.74, 5.57, 7.43, 6.15], [12.45, 11.29, 11.58, 9.96, 10.55, 9.46], [10.96, 9.81, 10.17, 8.48, 9.2, 8.05], [10.58, 9.58, 10.11, 8.26, 9.3, 8.08], [10.3, 9.05, 9.26, 7.74, 8.2, 7.13], [6.18, 6.75, 8.11, 6.55, 8.65, 7.85], [5.9, 6.86, 8.21, 7.01, 8.98, 8.38], [5.73, 6.94, 8.19, 7.37, 9.13, 8.73], [6.43, 7.35, 8.67, 7.44, 9.4, 8.78], [13.29, 11.92, 11.79, 10.73, 10.56, 9.81], [14.18, 12.85, 12.75, 11.68, 11.57, 10.82], [14.53, 13.18, 12.98, 12.1, 11.78, 11.16], [14.68, 13.41, 13.45, 12.19, 12.31, 11.45], [13.29, 12.03, 11.23, 11.63, 10.28, 10.53], [14.47, 13.23, 12.33, 12.92, 11.42, 11.79], [15.4, 14.21, 13.35, 13.9, 12.49, 12.83], [14.57, 13.32, 12.31, 13.06, 11.39, 11.87]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 8.58), ('CB', 'ASP', 'CG', 'HIS', 8.33), ('CB', 'ASP', 'ND1', 'HIS', 9.49), ('CB', 'ASP', 'CD2', 'HIS', 7.34), ('CB', 'ASP', 'CE1', 'HIS', 9.37), ('CB', 'ASP', 'NE2', 'HIS', 8.14)], [('CG', 'ASP', 'CB', 'HIS', 8.23), ('CG', 'ASP', 'CG', 'HIS', 7.66), ('CG', 'ASP', 'ND1', 'HIS', 8.65), ('CG', 'ASP', 'CD2', 'HIS', 6.47), ('CG', 'ASP', 'CE1', 'HIS', 8.32), ('CG', 'ASP', 'NE2', 'HIS', 7.02)], [('OD1', 'ASP', 'CB', 'HIS', 9.07), ('OD1', 'ASP', 'CG', 'HIS', 8.32), ('OD1', 'ASP', 'ND1', 'HIS', 9.15), ('OD1', 'ASP', 'CD2', 'HIS', 7.05), ('OD1', 'ASP', 'CE1', 'HIS', 8.62), ('OD1', 'ASP', 'NE2', 'HIS', 7.32)], [('OD2', 'ASP', 'CB', 'HIS', 7.39), ('OD2', 'ASP', 'CG', 'HIS', 6.76), ('OD2', 'ASP', 'ND1', 'HIS', 7.74), ('OD2', 'ASP', 'CD2', 'HIS', 5.57), ('OD2', 'ASP', 'CE1', 'HIS', 7.43), ('OD2', 'ASP', 'NE2', 'HIS', 6.15)], [('CB', 'ASP', 'CB', 'HIS', 12.45), ('CB', 'ASP', 'CG', 'HIS', 11.29), ('CB', 'ASP', 'ND1', 'HIS', 11.58), ('CB', 'ASP', 'CD2', 'HIS', 9.96), ('CB', 'ASP', 'CE1', 'HIS', 10.55), ('CB', 'ASP', 'NE2', 'HIS', 9.46)], [('CG', 'ASP', 'CB', 'HIS', 10.96), ('CG', 'ASP', 'CG', 'HIS', 9.81), ('CG', 'ASP', 'ND1', 'HIS', 10.17), ('CG', 'ASP', 'CD2', 'HIS', 8.48), ('CG', 'ASP', 'CE1', 'HIS', 9.2), ('CG', 'ASP', 'NE2', 'HIS', 8.05)], [('OD1', 'ASP', 'CB', 'HIS', 10.58), ('OD1', 'ASP', 'CG', 'HIS', 9.58), ('OD1', 'ASP', 'ND1', 'HIS', 10.11), ('OD1', 'ASP', 'CD2', 'HIS', 8.26), ('OD1', 'ASP', 'CE1', 'HIS', 9.3), ('OD1', 'ASP', 'NE2', 'HIS', 8.08)], [('OD2', 'ASP', 'CB', 'HIS', 10.3), ('OD2', 'ASP', 'CG', 'HIS', 9.05), ('OD2', 'ASP', 'ND1', 'HIS', 9.26), ('OD2', 'ASP', 'CD2', 'HIS', 7.74), ('OD2', 'ASP', 'CE1', 'HIS', 8.2), ('OD2', 'ASP', 'NE2', 'HIS', 7.13)], [('CB', 'ASP', 'CB', 'HIS', 6.18), ('CB', 'ASP', 'CG', 'HIS', 6.75), ('CB', 'ASP', 'ND1', 'HIS', 8.11), ('CB', 'ASP', 'CD2', 'HIS', 6.55), ('CB', 'ASP', 'CE1', 'HIS', 8.65), ('CB', 'ASP', 'NE2', 'HIS', 7.85)], [('CG', 'ASP', 'CB', 'HIS', 5.9), ('CG', 'ASP', 'CG', 'HIS', 6.86), ('CG', 'ASP', 'ND1', 'HIS', 8.21), ('CG', 'ASP', 'CD2', 'HIS', 7.01), ('CG', 'ASP', 'CE1', 'HIS', 8.98), ('CG', 'ASP', 'NE2', 'HIS', 8.38)], [('OD1', 'ASP', 'CB', 'HIS', 5.73), ('OD1', 'ASP', 'CG', 'HIS', 6.94), ('OD1', 'ASP', 'ND1', 'HIS', 8.19), ('OD1', 'ASP', 'CD2', 'HIS', 7.37), ('OD1', 'ASP', 'CE1', 'HIS', 9.13), ('OD1', 'ASP', 'NE2', 'HIS', 8.73)], [('OD2', 'ASP', 'CB', 'HIS', 6.43), ('OD2', 'ASP', 'CG', 'HIS', 7.35), ('OD2', 'ASP', 'ND1', 'HIS', 8.67), ('OD2', 'ASP', 'CD2', 'HIS', 7.44), ('OD2', 'ASP', 'CE1', 'HIS', 9.4), ('OD2', 'ASP', 'NE2', 'HIS', 8.78)], [('CB', 'ASP', 'CB', 'HIS', 13.29), ('CB', 'ASP', 'CG', 'HIS', 11.92), ('CB', 'ASP', 'ND1', 'HIS', 11.79), ('CB', 'ASP', 'CD2', 'HIS', 10.73), ('CB', 'ASP', 'CE1', 'HIS', 10.56), ('CB', 'ASP', 'NE2', 'HIS', 9.81)], [('CG', 'ASP', 'CB', 'HIS', 14.18), ('CG', 'ASP', 'CG', 'HIS', 12.85), ('CG', 'ASP', 'ND1', 'HIS', 12.75), ('CG', 'ASP', 'CD2', 'HIS', 11.68), ('CG', 'ASP', 'CE1', 'HIS', 11.57), ('CG', 'ASP', 'NE2', 'HIS', 10.82)], [('OD1', 'ASP', 'CB', 'HIS', 14.53), ('OD1', 'ASP', 'CG', 'HIS', 13.18), ('OD1', 'ASP', 'ND1', 'HIS', 12.98), ('OD1', 'ASP', 'CD2', 'HIS', 12.1), ('OD1', 'ASP', 'CE1', 'HIS', 11.78), ('OD1', 'ASP', 'NE2', 'HIS', 11.16)], [('OD2', 'ASP', 'CB', 'HIS', 14.68), ('OD2', 'ASP', 'CG', 'HIS', 13.41), ('OD2', 'ASP', 'ND1', 'HIS', 13.45), ('OD2', 'ASP', 'CD2', 'HIS', 12.19), ('OD2', 'ASP', 'CE1', 'HIS', 12.31), ('OD2', 'ASP', 'NE2', 'HIS', 11.45)], [('CB', 'ASP', 'CB', 'HIS', 13.29), ('CB', 'ASP', 'CG', 'HIS', 12.03), ('CB', 'ASP', 'ND1', 'HIS', 11.23), ('CB', 'ASP', 'CD2', 'HIS', 11.63), ('CB', 'ASP', 'CE1', 'HIS', 10.28), ('CB', 'ASP', 'NE2', 'HIS', 10.53)], [('CG', 'ASP', 'CB', 'HIS', 14.47), ('CG', 'ASP', 'CG', 'HIS', 13.23), ('CG', 'ASP', 'ND1', 'HIS', 12.33), ('CG', 'ASP', 'CD2', 'HIS', 12.92), ('CG', 'ASP', 'CE1', 'HIS', 11.42), ('CG', 'ASP', 'NE2', 'HIS', 11.79)], [('OD1', 'ASP', 'CB', 'HIS', 15.4), ('OD1', 'ASP', 'CG', 'HIS', 14.21), ('OD1', 'ASP', 'ND1', 'HIS', 13.35), ('OD1', 'ASP', 'CD2', 'HIS', 13.9), ('OD1', 'ASP', 'CE1', 'HIS', 12.49), ('OD1', 'ASP', 'NE2', 'HIS', 12.83)], [('OD2', 'ASP', 'CB', 'HIS', 14.57), ('OD2', 'ASP', 'CG', 'HIS', 13.32), ('OD2', 'ASP', 'ND1', 'HIS', 12.31), ('OD2', 'ASP', 'CD2', 'HIS', 13.06), ('OD2', 'ASP', 'CE1', 'HIS', 11.39), ('OD2', 'ASP', 'NE2', 'HIS', 11.87)]]}
GLY_ASPII = { 
	'distances':
		[[15.19, 16.46, 17.53, 16.46], [14.37, 15.6, 16.71, 15.55], [13.88, 15.14, 16.24, 15.12], [14.31, 15.5, 16.64, 15.38]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASPII', 15.19), ('O', 'GLY', 'CG', 'ASPII', 16.46), ('O', 'GLY', 'OD1', 'ASPII', 17.53), ('O', 'GLY', 'OD2', 'ASPII', 16.46)], [('C', 'GLY', 'CB', 'ASPII', 14.37), ('C', 'GLY', 'CG', 'ASPII', 15.6), ('C', 'GLY', 'OD1', 'ASPII', 16.71), ('C', 'GLY', 'OD2', 'ASPII', 15.55)], [('CA', 'GLY', 'CB', 'ASPII', 13.88), ('CA', 'GLY', 'CG', 'ASPII', 15.14), ('CA', 'GLY', 'OD1', 'ASPII', 16.24), ('CA', 'GLY', 'OD2', 'ASPII', 15.12)], [('N', 'GLY', 'CB', 'ASPII', 14.31), ('N', 'GLY', 'CG', 'ASPII', 15.5), ('N', 'GLY', 'OD1', 'ASPII', 16.64), ('N', 'GLY', 'OD2', 'ASPII', 15.38)]]}
GLY_HISI = { 
	'distances':
		[[12.2, 11.29, 11.83, 10.03, 11.05, 9.89], [11.24, 10.44, 11.09, 9.22, 10.44, 9.25], [10.5, 9.78, 10.57, 8.54, 10.01, 8.73], [10.7, 10.21, 11.17, 9.07, 10.79, 9.51]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HISI', 12.2), ('O', 'GLY', 'CG', 'HISI', 11.29), ('O', 'GLY', 'ND1', 'HISI', 11.83), ('O', 'GLY', 'CD2', 'HISI', 10.03), ('O', 'GLY', 'CE1', 'HISI', 11.05), ('O', 'GLY', 'NE2', 'HISI', 9.89)], [('C', 'GLY', 'CB', 'HISI', 11.24), ('C', 'GLY', 'CG', 'HISI', 10.44), ('C', 'GLY', 'ND1', 'HISI', 11.09), ('C', 'GLY', 'CD2', 'HISI', 9.22), ('C', 'GLY', 'CE1', 'HISI', 10.44), ('C', 'GLY', 'NE2', 'HISI', 9.25)], [('CA', 'GLY', 'CB', 'HISI', 10.5), ('CA', 'GLY', 'CG', 'HISI', 9.78), ('CA', 'GLY', 'ND1', 'HISI', 10.57), ('CA', 'GLY', 'CD2', 'HISI', 8.54), ('CA', 'GLY', 'CE1', 'HISI', 10.01), ('CA', 'GLY', 'NE2', 'HISI', 8.73)], [('N', 'GLY', 'CB', 'HISI', 10.7), ('N', 'GLY', 'CG', 'HISI', 10.21), ('N', 'GLY', 'ND1', 'HISI', 11.17), ('N', 'GLY', 'CD2', 'HISI', 9.07), ('N', 'GLY', 'CE1', 'HISI', 10.79), ('N', 'GLY', 'NE2', 'HISI', 9.51)]]}
GLY_ASPI = { 
	'distances':
		[[7.19, 7.05, 7.89, 6.47], [7.97, 7.97, 8.74, 7.54], [8.53, 8.84, 9.71, 8.48], [9.96, 10.22, 11.08, 9.77]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASPI', 7.19), ('O', 'GLY', 'CG', 'ASPI', 7.05), ('O', 'GLY', 'OD1', 'ASPI', 7.89), ('O', 'GLY', 'OD2', 'ASPI', 6.47)], [('C', 'GLY', 'CB', 'ASPI', 7.97), ('C', 'GLY', 'CG', 'ASPI', 7.97), ('C', 'GLY', 'OD1', 'ASPI', 8.74), ('C', 'GLY', 'OD2', 'ASPI', 7.54)], [('CA', 'GLY', 'CB', 'ASPI', 8.53), ('CA', 'GLY', 'CG', 'ASPI', 8.84), ('CA', 'GLY', 'OD1', 'ASPI', 9.71), ('CA', 'GLY', 'OD2', 'ASPI', 8.48)], [('N', 'GLY', 'CB', 'ASPI', 9.96), ('N', 'GLY', 'CG', 'ASPI', 10.22), ('N', 'GLY', 'OD1', 'ASPI', 11.08), ('N', 'GLY', 'OD2', 'ASPI', 9.77)]]}
HIS_GLY = { 
	'distances':
		[[6.66, 6.86, 7.87, 9.11], [6.48, 6.32, 7.06, 8.25], [7.31, 6.88, 7.54, 8.52], [6.09, 5.82, 6.2, 7.45], [7.47, 6.81, 7.11, 7.97], [6.79, 6.18, 6.26, 7.27], [12.2, 11.24, 10.5, 10.7], [11.29, 10.44, 9.78, 10.21], [11.83, 11.09, 10.57, 11.17], [10.03, 9.22, 8.54, 9.07], [11.05, 10.44, 10.01, 10.79], [9.89, 9.25, 8.73, 9.51]],
	'comparisons':
		[[('CB', 'HIS', 'O', 'GLY', 6.66), ('CB', 'HIS', 'C', 'GLY', 6.86), ('CB', 'HIS', 'CA', 'GLY', 7.87), ('CB', 'HIS', 'N', 'GLY', 9.11)], [('CG', 'HIS', 'O', 'GLY', 6.48), ('CG', 'HIS', 'C', 'GLY', 6.32), ('CG', 'HIS', 'CA', 'GLY', 7.06), ('CG', 'HIS', 'N', 'GLY', 8.25)], [('ND1', 'HIS', 'O', 'GLY', 7.31), ('ND1', 'HIS', 'C', 'GLY', 6.88), ('ND1', 'HIS', 'CA', 'GLY', 7.54), ('ND1', 'HIS', 'N', 'GLY', 8.52)], [('CD2', 'HIS', 'O', 'GLY', 6.09), ('CD2', 'HIS', 'C', 'GLY', 5.82), ('CD2', 'HIS', 'CA', 'GLY', 6.2), ('CD2', 'HIS', 'N', 'GLY', 7.45)], [('CE1', 'HIS', 'O', 'GLY', 7.47), ('CE1', 'HIS', 'C', 'GLY', 6.81), ('CE1', 'HIS', 'CA', 'GLY', 7.11), ('CE1', 'HIS', 'N', 'GLY', 7.97)], [('NE2', 'HIS', 'O', 'GLY', 6.79), ('NE2', 'HIS', 'C', 'GLY', 6.18), ('NE2', 'HIS', 'CA', 'GLY', 6.26), ('NE2', 'HIS', 'N', 'GLY', 7.27)], [('CB', 'HIS', 'O', 'GLY', 12.2), ('CB', 'HIS', 'C', 'GLY', 11.24), ('CB', 'HIS', 'CA', 'GLY', 10.5), ('CB', 'HIS', 'N', 'GLY', 10.7)], [('CG', 'HIS', 'O', 'GLY', 11.29), ('CG', 'HIS', 'C', 'GLY', 10.44), ('CG', 'HIS', 'CA', 'GLY', 9.78), ('CG', 'HIS', 'N', 'GLY', 10.21)], [('ND1', 'HIS', 'O', 'GLY', 11.83), ('ND1', 'HIS', 'C', 'GLY', 11.09), ('ND1', 'HIS', 'CA', 'GLY', 10.57), ('ND1', 'HIS', 'N', 'GLY', 11.17)], [('CD2', 'HIS', 'O', 'GLY', 10.03), ('CD2', 'HIS', 'C', 'GLY', 9.22), ('CD2', 'HIS', 'CA', 'GLY', 8.54), ('CD2', 'HIS', 'N', 'GLY', 9.07)], [('CE1', 'HIS', 'O', 'GLY', 11.05), ('CE1', 'HIS', 'C', 'GLY', 10.44), ('CE1', 'HIS', 'CA', 'GLY', 10.01), ('CE1', 'HIS', 'N', 'GLY', 10.79)], [('NE2', 'HIS', 'O', 'GLY', 9.89), ('NE2', 'HIS', 'C', 'GLY', 9.25), ('NE2', 'HIS', 'CA', 'GLY', 8.73), ('NE2', 'HIS', 'N', 'GLY', 9.51)]]}
HIS_HIS = { 
	'distances':
		[[11.56, 10.37, 10.29, 9.4, 9.32, 8.69], [10.1, 8.94, 8.96, 7.96, 8.06, 7.35], [9.39, 8.36, 8.41, 7.57, 7.71, 7.12], [9.38, 8.18, 8.32, 7.05, 7.39, 6.48], [8.14, 7.15, 7.37, 6.35, 6.78, 6.09], [8.09, 6.98, 7.27, 5.91, 6.53, 5.57], [11.56, 10.1, 9.39, 9.38, 8.14, 8.09], [10.37, 8.94, 8.36, 8.18, 7.15, 6.98], [10.29, 8.96, 8.41, 8.32, 7.37, 7.27], [9.4, 7.96, 7.57, 7.05, 6.35, 5.91], [9.32, 8.06, 7.71, 7.39, 6.78, 6.53], [8.69, 7.35, 7.12, 6.48, 6.09, 5.57]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 11.56), ('CB', 'HIS', 'CG', 'HIS', 10.37), ('CB', 'HIS', 'ND1', 'HIS', 10.29), ('CB', 'HIS', 'CD2', 'HIS', 9.4), ('CB', 'HIS', 'CE1', 'HIS', 9.32), ('CB', 'HIS', 'NE2', 'HIS', 8.69)], [('CG', 'HIS', 'CB', 'HIS', 10.1), ('CG', 'HIS', 'CG', 'HIS', 8.94), ('CG', 'HIS', 'ND1', 'HIS', 8.96), ('CG', 'HIS', 'CD2', 'HIS', 7.96), ('CG', 'HIS', 'CE1', 'HIS', 8.06), ('CG', 'HIS', 'NE2', 'HIS', 7.35)], [('ND1', 'HIS', 'CB', 'HIS', 9.39), ('ND1', 'HIS', 'CG', 'HIS', 8.36), ('ND1', 'HIS', 'ND1', 'HIS', 8.41), ('ND1', 'HIS', 'CD2', 'HIS', 7.57), ('ND1', 'HIS', 'CE1', 'HIS', 7.71), ('ND1', 'HIS', 'NE2', 'HIS', 7.12)], [('CD2', 'HIS', 'CB', 'HIS', 9.38), ('CD2', 'HIS', 'CG', 'HIS', 8.18), ('CD2', 'HIS', 'ND1', 'HIS', 8.32), ('CD2', 'HIS', 'CD2', 'HIS', 7.05), ('CD2', 'HIS', 'CE1', 'HIS', 7.39), ('CD2', 'HIS', 'NE2', 'HIS', 6.48)], [('CE1', 'HIS', 'CB', 'HIS', 8.14), ('CE1', 'HIS', 'CG', 'HIS', 7.15), ('CE1', 'HIS', 'ND1', 'HIS', 7.37), ('CE1', 'HIS', 'CD2', 'HIS', 6.35), ('CE1', 'HIS', 'CE1', 'HIS', 6.78), ('CE1', 'HIS', 'NE2', 'HIS', 6.09)], [('NE2', 'HIS', 'CB', 'HIS', 8.09), ('NE2', 'HIS', 'CG', 'HIS', 6.98), ('NE2', 'HIS', 'ND1', 'HIS', 7.27), ('NE2', 'HIS', 'CD2', 'HIS', 5.91), ('NE2', 'HIS', 'CE1', 'HIS', 6.53), ('NE2', 'HIS', 'NE2', 'HIS', 5.57)], [('CB', 'HIS', 'CB', 'HIS', 11.56), ('CB', 'HIS', 'CG', 'HIS', 10.1), ('CB', 'HIS', 'ND1', 'HIS', 9.39), ('CB', 'HIS', 'CD2', 'HIS', 9.38), ('CB', 'HIS', 'CE1', 'HIS', 8.14), ('CB', 'HIS', 'NE2', 'HIS', 8.09)], [('CG', 'HIS', 'CB', 'HIS', 10.37), ('CG', 'HIS', 'CG', 'HIS', 8.94), ('CG', 'HIS', 'ND1', 'HIS', 8.36), ('CG', 'HIS', 'CD2', 'HIS', 8.18), ('CG', 'HIS', 'CE1', 'HIS', 7.15), ('CG', 'HIS', 'NE2', 'HIS', 6.98)], [('ND1', 'HIS', 'CB', 'HIS', 10.29), ('ND1', 'HIS', 'CG', 'HIS', 8.96), ('ND1', 'HIS', 'ND1', 'HIS', 8.41), ('ND1', 'HIS', 'CD2', 'HIS', 8.32), ('ND1', 'HIS', 'CE1', 'HIS', 7.37), ('ND1', 'HIS', 'NE2', 'HIS', 7.27)], [('CD2', 'HIS', 'CB', 'HIS', 9.4), ('CD2', 'HIS', 'CG', 'HIS', 7.96), ('CD2', 'HIS', 'ND1', 'HIS', 7.57), ('CD2', 'HIS', 'CD2', 'HIS', 7.05), ('CD2', 'HIS', 'CE1', 'HIS', 6.35), ('CD2', 'HIS', 'NE2', 'HIS', 5.91)], [('CE1', 'HIS', 'CB', 'HIS', 9.32), ('CE1', 'HIS', 'CG', 'HIS', 8.06), ('CE1', 'HIS', 'ND1', 'HIS', 7.71), ('CE1', 'HIS', 'CD2', 'HIS', 7.39), ('CE1', 'HIS', 'CE1', 'HIS', 6.78), ('CE1', 'HIS', 'NE2', 'HIS', 6.53)], [('NE2', 'HIS', 'CB', 'HIS', 8.69), ('NE2', 'HIS', 'CG', 'HIS', 7.35), ('NE2', 'HIS', 'ND1', 'HIS', 7.12), ('NE2', 'HIS', 'CD2', 'HIS', 6.48), ('NE2', 'HIS', 'CE1', 'HIS', 6.09), ('NE2', 'HIS', 'NE2', 'HIS', 5.57)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HISI, d, 'A_1b93_4_2_3_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLY, d, 'A_1b93_4_2_3_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'A_1b93_4_2_3_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ASPI, d, 'A_1b93_4_2_3_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_ASPI, d, 'A_1b93_4_2_3_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_HIS, d, 'A_1b93_4_2_3_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_ASPII, d, 'A_1b93_4_2_3_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(GLY_HISI, d, 'A_1b93_4_2_3_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLY_ASPI, d, 'A_1b93_4_2_3_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(HIS_GLY, d, 'A_1b93_4_2_3_3')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(HIS_HIS, d, 'A_1b93_4_2_3_3')
	if match11 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HISI' :  match1,
		'ASP_GLY' :  match2,
		'ASP_ASP' :  match3,
		'HIS_ASPI' :  match4,
		'ASP_ASPI' :  match5,
		'ASP_HIS' :  match6,
		'GLY_ASPII' :  match7,
		'GLY_HISI' :  match8,
		'GLY_ASPI' :  match9,
		'HIS_GLY' :  match10,
		'HIS_HIS' :  match11}