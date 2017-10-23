'''
FUNC:A_1chd_3_1_1_61
PDB:1chd
EC:3.1.1.61
RESI:ser,thr,his,met,asp
LOCI:a-164,165,190,283,286;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[9.38, 9.37, 10.52, 8.39], [7.89, 7.89, 9.05, 6.93], [7.12, 7.44, 8.67, 6.72], [7.25, 6.95, 8.03, 5.87], [5.82, 6.13, 7.37, 5.49], [5.88, 5.7, 6.85, 4.75]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 9.38), ('CB', 'HIS', 'CG', 'ASP', 9.37), ('CB', 'HIS', 'OD1', 'ASP', 10.52), ('CB', 'HIS', 'OD2', 'ASP', 8.39)], [('CG', 'HIS', 'CB', 'ASP', 7.89), ('CG', 'HIS', 'CG', 'ASP', 7.89), ('CG', 'HIS', 'OD1', 'ASP', 9.05), ('CG', 'HIS', 'OD2', 'ASP', 6.93)], [('ND1', 'HIS', 'CB', 'ASP', 7.12), ('ND1', 'HIS', 'CG', 'ASP', 7.44), ('ND1', 'HIS', 'OD1', 'ASP', 8.67), ('ND1', 'HIS', 'OD2', 'ASP', 6.72)], [('CD2', 'HIS', 'CB', 'ASP', 7.25), ('CD2', 'HIS', 'CG', 'ASP', 6.95), ('CD2', 'HIS', 'OD1', 'ASP', 8.03), ('CD2', 'HIS', 'OD2', 'ASP', 5.87)], [('CE1', 'HIS', 'CB', 'ASP', 5.82), ('CE1', 'HIS', 'CG', 'ASP', 6.13), ('CE1', 'HIS', 'OD1', 'ASP', 7.37), ('CE1', 'HIS', 'OD2', 'ASP', 5.49)], [('NE2', 'HIS', 'CB', 'ASP', 5.88), ('NE2', 'HIS', 'CG', 'ASP', 5.7), ('NE2', 'HIS', 'OD1', 'ASP', 6.85), ('NE2', 'HIS', 'OD2', 'ASP', 4.75)]]}
HIS_THR = { 
	'distances':
		[[9.63, 8.85, 10.83, 10.6, 10.02, 8.9, 7.71], [10.16, 9.35, 11.49, 11.03, 10.63, 9.56, 8.23], [9.65, 8.76, 11.03, 10.67, 10.38, 9.26, 7.91], [11.41, 10.64, 12.77, 12.06, 11.74, 10.76, 9.39], [10.64, 9.79, 12.07, 11.5, 11.34, 10.3, 8.91], [11.64, 10.84, 13.06, 12.31, 12.12, 11.14, 9.73]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'THR', 9.63), ('CB', 'HIS', 'OG1', 'THR', 8.85), ('CB', 'HIS', 'CG2', 'THR', 10.83), ('CB', 'HIS', 'O', 'THR', 10.6), ('CB', 'HIS', 'C', 'THR', 10.02), ('CB', 'HIS', 'CA', 'THR', 8.9), ('CB', 'HIS', 'N', 'THR', 7.71)], [('CG', 'HIS', 'CB', 'THR', 10.16), ('CG', 'HIS', 'OG1', 'THR', 9.35), ('CG', 'HIS', 'CG2', 'THR', 11.49), ('CG', 'HIS', 'O', 'THR', 11.03), ('CG', 'HIS', 'C', 'THR', 10.63), ('CG', 'HIS', 'CA', 'THR', 9.56), ('CG', 'HIS', 'N', 'THR', 8.23)], [('ND1', 'HIS', 'CB', 'THR', 9.65), ('ND1', 'HIS', 'OG1', 'THR', 8.76), ('ND1', 'HIS', 'CG2', 'THR', 11.03), ('ND1', 'HIS', 'O', 'THR', 10.67), ('ND1', 'HIS', 'C', 'THR', 10.38), ('ND1', 'HIS', 'CA', 'THR', 9.26), ('ND1', 'HIS', 'N', 'THR', 7.91)], [('CD2', 'HIS', 'CB', 'THR', 11.41), ('CD2', 'HIS', 'OG1', 'THR', 10.64), ('CD2', 'HIS', 'CG2', 'THR', 12.77), ('CD2', 'HIS', 'O', 'THR', 12.06), ('CD2', 'HIS', 'C', 'THR', 11.74), ('CD2', 'HIS', 'CA', 'THR', 10.76), ('CD2', 'HIS', 'N', 'THR', 9.39)], [('CE1', 'HIS', 'CB', 'THR', 10.64), ('CE1', 'HIS', 'OG1', 'THR', 9.79), ('CE1', 'HIS', 'CG2', 'THR', 12.07), ('CE1', 'HIS', 'O', 'THR', 11.5), ('CE1', 'HIS', 'C', 'THR', 11.34), ('CE1', 'HIS', 'CA', 'THR', 10.3), ('CE1', 'HIS', 'N', 'THR', 8.91)], [('NE2', 'HIS', 'CB', 'THR', 11.64), ('NE2', 'HIS', 'OG1', 'THR', 10.84), ('NE2', 'HIS', 'CG2', 'THR', 13.06), ('NE2', 'HIS', 'O', 'THR', 12.31), ('NE2', 'HIS', 'C', 'THR', 12.12), ('NE2', 'HIS', 'CA', 'THR', 11.14), ('NE2', 'HIS', 'N', 'THR', 9.73)]]}
SER_MET = { 
	'distances':
		[[7.35, 8.71, 10.09, 11.33, 6.55, 7.26, 7.06, 5.91], [6.55, 7.83, 9.32, 10.54, 6.33, 6.98, 6.65, 5.71]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'MET', 7.35), ('CB', 'SER', 'CG', 'MET', 8.71), ('CB', 'SER', 'SD', 'MET', 10.09), ('CB', 'SER', 'CE', 'MET', 11.33), ('CB', 'SER', 'O', 'MET', 6.55), ('CB', 'SER', 'C', 'MET', 7.26), ('CB', 'SER', 'CA', 'MET', 7.06), ('CB', 'SER', 'N', 'MET', 5.91)], [('OG', 'SER', 'CB', 'MET', 6.55), ('OG', 'SER', 'CG', 'MET', 7.83), ('OG', 'SER', 'SD', 'MET', 9.32), ('OG', 'SER', 'CE', 'MET', 10.54), ('OG', 'SER', 'O', 'MET', 6.33), ('OG', 'SER', 'C', 'MET', 6.98), ('OG', 'SER', 'CA', 'MET', 6.65), ('OG', 'SER', 'N', 'MET', 5.71)]]}
THR_ASP = { 
	'distances':
		[[13.51, 14.4, 15.62, 14.01], [12.74, 13.63, 14.86, 13.22], [14.98, 15.88, 17.11, 15.47], [14.05, 14.88, 16.03, 14.52], [14.2, 14.96, 16.14, 14.5], [13.35, 14.1, 15.32, 13.61], [11.96, 12.68, 13.89, 12.18]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 13.51), ('CB', 'THR', 'CG', 'ASP', 14.4), ('CB', 'THR', 'OD1', 'ASP', 15.62), ('CB', 'THR', 'OD2', 'ASP', 14.01)], [('OG1', 'THR', 'CB', 'ASP', 12.74), ('OG1', 'THR', 'CG', 'ASP', 13.63), ('OG1', 'THR', 'OD1', 'ASP', 14.86), ('OG1', 'THR', 'OD2', 'ASP', 13.22)], [('CG2', 'THR', 'CB', 'ASP', 14.98), ('CG2', 'THR', 'CG', 'ASP', 15.88), ('CG2', 'THR', 'OD1', 'ASP', 17.11), ('CG2', 'THR', 'OD2', 'ASP', 15.47)], [('O', 'THR', 'CB', 'ASP', 14.05), ('O', 'THR', 'CG', 'ASP', 14.88), ('O', 'THR', 'OD1', 'ASP', 16.03), ('O', 'THR', 'OD2', 'ASP', 14.52)], [('C', 'THR', 'CB', 'ASP', 14.2), ('C', 'THR', 'CG', 'ASP', 14.96), ('C', 'THR', 'OD1', 'ASP', 16.14), ('C', 'THR', 'OD2', 'ASP', 14.5)], [('CA', 'THR', 'CB', 'ASP', 13.35), ('CA', 'THR', 'CG', 'ASP', 14.1), ('CA', 'THR', 'OD1', 'ASP', 15.32), ('CA', 'THR', 'OD2', 'ASP', 13.61)], [('N', 'THR', 'CB', 'ASP', 11.96), ('N', 'THR', 'CG', 'ASP', 12.68), ('N', 'THR', 'OD1', 'ASP', 13.89), ('N', 'THR', 'OD2', 'ASP', 12.18)]]}
SER_THR = { 
	'distances':
		[[6.87, 6.49, 8.36, 7.29, 7.16, 6.3, 4.86], [6.18, 5.45, 7.61, 7.4, 7.09, 5.89, 4.62]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'THR', 6.87), ('CB', 'SER', 'OG1', 'THR', 6.49), ('CB', 'SER', 'CG2', 'THR', 8.36), ('CB', 'SER', 'O', 'THR', 7.29), ('CB', 'SER', 'C', 'THR', 7.16), ('CB', 'SER', 'CA', 'THR', 6.3), ('CB', 'SER', 'N', 'THR', 4.86)], [('OG', 'SER', 'CB', 'THR', 6.18), ('OG', 'SER', 'OG1', 'THR', 5.45), ('OG', 'SER', 'CG2', 'THR', 7.61), ('OG', 'SER', 'O', 'THR', 7.4), ('OG', 'SER', 'C', 'THR', 7.09), ('OG', 'SER', 'CA', 'THR', 5.89), ('OG', 'SER', 'N', 'THR', 4.62)]]}
MET_ASP = { 
	'distances':
		[[10.76, 12.01, 13.12, 12.03], [11.24, 12.53, 13.59, 12.63], [12.44, 13.82, 14.81, 14.04], [12.62, 14.01, 14.91, 14.33], [7.7, 9.01, 10.08, 9.18], [8.72, 10.1, 11.11, 10.34], [10.02, 11.34, 12.41, 11.47], [10.0, 11.21, 12.32, 11.22]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'ASP', 10.76), ('CB', 'MET', 'CG', 'ASP', 12.01), ('CB', 'MET', 'OD1', 'ASP', 13.12), ('CB', 'MET', 'OD2', 'ASP', 12.03)], [('CG', 'MET', 'CB', 'ASP', 11.24), ('CG', 'MET', 'CG', 'ASP', 12.53), ('CG', 'MET', 'OD1', 'ASP', 13.59), ('CG', 'MET', 'OD2', 'ASP', 12.63)], [('SD', 'MET', 'CB', 'ASP', 12.44), ('SD', 'MET', 'CG', 'ASP', 13.82), ('SD', 'MET', 'OD1', 'ASP', 14.81), ('SD', 'MET', 'OD2', 'ASP', 14.04)], [('CE', 'MET', 'CB', 'ASP', 12.62), ('CE', 'MET', 'CG', 'ASP', 14.01), ('CE', 'MET', 'OD1', 'ASP', 14.91), ('CE', 'MET', 'OD2', 'ASP', 14.33)], [('O', 'MET', 'CB', 'ASP', 7.7), ('O', 'MET', 'CG', 'ASP', 9.01), ('O', 'MET', 'OD1', 'ASP', 10.08), ('O', 'MET', 'OD2', 'ASP', 9.18)], [('C', 'MET', 'CB', 'ASP', 8.72), ('C', 'MET', 'CG', 'ASP', 10.1), ('C', 'MET', 'OD1', 'ASP', 11.11), ('C', 'MET', 'OD2', 'ASP', 10.34)], [('CA', 'MET', 'CB', 'ASP', 10.02), ('CA', 'MET', 'CG', 'ASP', 11.34), ('CA', 'MET', 'OD1', 'ASP', 12.41), ('CA', 'MET', 'OD2', 'ASP', 11.47)], [('N', 'MET', 'CB', 'ASP', 10.0), ('N', 'MET', 'CG', 'ASP', 11.21), ('N', 'MET', 'OD1', 'ASP', 12.32), ('N', 'MET', 'OD2', 'ASP', 11.22)]]}
SER_ASP = { 
	'distances':
		[[9.17, 9.84, 11.04, 9.35], [9.65, 10.38, 11.62, 9.89]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 9.17), ('CB', 'SER', 'CG', 'ASP', 9.84), ('CB', 'SER', 'OD1', 'ASP', 11.04), ('CB', 'SER', 'OD2', 'ASP', 9.35)], [('OG', 'SER', 'CB', 'ASP', 9.65), ('OG', 'SER', 'CG', 'ASP', 10.38), ('OG', 'SER', 'OD1', 'ASP', 11.62), ('OG', 'SER', 'OD2', 'ASP', 9.89)]]}
MET_THR = { 
	'distances':
		[[6.95, 6.14, 7.93, 8.84, 8.97, 7.97, 7.55], [8.15, 7.25, 8.94, 10.24, 10.33, 9.3, 8.96], [8.97, 8.34, 9.56, 10.81, 11.07, 10.26, 10.1], [10.61, 9.83, 11.18, 12.56, 12.78, 11.87, 11.63], [8.83, 8.04, 10.16, 10.0, 10.22, 9.27, 8.27], [8.71, 8.03, 9.94, 9.88, 10.21, 9.36, 8.54], [7.46, 6.92, 8.61, 8.69, 9.05, 8.27, 7.67], [6.57, 6.25, 7.88, 7.43, 7.82, 7.14, 6.43]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'THR', 6.95), ('CB', 'MET', 'OG1', 'THR', 6.14), ('CB', 'MET', 'CG2', 'THR', 7.93), ('CB', 'MET', 'O', 'THR', 8.84), ('CB', 'MET', 'C', 'THR', 8.97), ('CB', 'MET', 'CA', 'THR', 7.97), ('CB', 'MET', 'N', 'THR', 7.55)], [('CG', 'MET', 'CB', 'THR', 8.15), ('CG', 'MET', 'OG1', 'THR', 7.25), ('CG', 'MET', 'CG2', 'THR', 8.94), ('CG', 'MET', 'O', 'THR', 10.24), ('CG', 'MET', 'C', 'THR', 10.33), ('CG', 'MET', 'CA', 'THR', 9.3), ('CG', 'MET', 'N', 'THR', 8.96)], [('SD', 'MET', 'CB', 'THR', 8.97), ('SD', 'MET', 'OG1', 'THR', 8.34), ('SD', 'MET', 'CG2', 'THR', 9.56), ('SD', 'MET', 'O', 'THR', 10.81), ('SD', 'MET', 'C', 'THR', 11.07), ('SD', 'MET', 'CA', 'THR', 10.26), ('SD', 'MET', 'N', 'THR', 10.1)], [('CE', 'MET', 'CB', 'THR', 10.61), ('CE', 'MET', 'OG1', 'THR', 9.83), ('CE', 'MET', 'CG2', 'THR', 11.18), ('CE', 'MET', 'O', 'THR', 12.56), ('CE', 'MET', 'C', 'THR', 12.78), ('CE', 'MET', 'CA', 'THR', 11.87), ('CE', 'MET', 'N', 'THR', 11.63)], [('O', 'MET', 'CB', 'THR', 8.83), ('O', 'MET', 'OG1', 'THR', 8.04), ('O', 'MET', 'CG2', 'THR', 10.16), ('O', 'MET', 'O', 'THR', 10.0), ('O', 'MET', 'C', 'THR', 10.22), ('O', 'MET', 'CA', 'THR', 9.27), ('O', 'MET', 'N', 'THR', 8.27)], [('C', 'MET', 'CB', 'THR', 8.71), ('C', 'MET', 'OG1', 'THR', 8.03), ('C', 'MET', 'CG2', 'THR', 9.94), ('C', 'MET', 'O', 'THR', 9.88), ('C', 'MET', 'C', 'THR', 10.21), ('C', 'MET', 'CA', 'THR', 9.36), ('C', 'MET', 'N', 'THR', 8.54)], [('CA', 'MET', 'CB', 'THR', 7.46), ('CA', 'MET', 'OG1', 'THR', 6.92), ('CA', 'MET', 'CG2', 'THR', 8.61), ('CA', 'MET', 'O', 'THR', 8.69), ('CA', 'MET', 'C', 'THR', 9.05), ('CA', 'MET', 'CA', 'THR', 8.27), ('CA', 'MET', 'N', 'THR', 7.67)], [('N', 'MET', 'CB', 'THR', 6.57), ('N', 'MET', 'OG1', 'THR', 6.25), ('N', 'MET', 'CG2', 'THR', 7.88), ('N', 'MET', 'O', 'THR', 7.43), ('N', 'MET', 'C', 'THR', 7.82), ('N', 'MET', 'CA', 'THR', 7.14), ('N', 'MET', 'N', 'THR', 6.43)]]}
HIS_MET = { 
	'distances':
		[[10.11, 11.08, 12.79, 13.65, 9.01, 10.07, 10.26, 9.51], [9.85, 10.77, 12.45, 13.2, 8.22, 9.37, 9.81, 9.16], [8.67, 9.54, 11.2, 11.91, 6.87, 8.05, 8.58, 8.06], [10.84, 11.72, 13.37, 14.03, 8.84, 10.04, 10.65, 10.04], [9.1, 9.88, 11.47, 12.04, 6.78, 8.01, 8.81, 8.4], [10.4, 11.2, 12.78, 13.33, 8.04, 9.27, 10.07, 9.6]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'MET', 10.11), ('CB', 'HIS', 'CG', 'MET', 11.08), ('CB', 'HIS', 'SD', 'MET', 12.79), ('CB', 'HIS', 'CE', 'MET', 13.65), ('CB', 'HIS', 'O', 'MET', 9.01), ('CB', 'HIS', 'C', 'MET', 10.07), ('CB', 'HIS', 'CA', 'MET', 10.26), ('CB', 'HIS', 'N', 'MET', 9.51)], [('CG', 'HIS', 'CB', 'MET', 9.85), ('CG', 'HIS', 'CG', 'MET', 10.77), ('CG', 'HIS', 'SD', 'MET', 12.45), ('CG', 'HIS', 'CE', 'MET', 13.2), ('CG', 'HIS', 'O', 'MET', 8.22), ('CG', 'HIS', 'C', 'MET', 9.37), ('CG', 'HIS', 'CA', 'MET', 9.81), ('CG', 'HIS', 'N', 'MET', 9.16)], [('ND1', 'HIS', 'CB', 'MET', 8.67), ('ND1', 'HIS', 'CG', 'MET', 9.54), ('ND1', 'HIS', 'SD', 'MET', 11.2), ('ND1', 'HIS', 'CE', 'MET', 11.91), ('ND1', 'HIS', 'O', 'MET', 6.87), ('ND1', 'HIS', 'C', 'MET', 8.05), ('ND1', 'HIS', 'CA', 'MET', 8.58), ('ND1', 'HIS', 'N', 'MET', 8.06)], [('CD2', 'HIS', 'CB', 'MET', 10.84), ('CD2', 'HIS', 'CG', 'MET', 11.72), ('CD2', 'HIS', 'SD', 'MET', 13.37), ('CD2', 'HIS', 'CE', 'MET', 14.03), ('CD2', 'HIS', 'O', 'MET', 8.84), ('CD2', 'HIS', 'C', 'MET', 10.04), ('CD2', 'HIS', 'CA', 'MET', 10.65), ('CD2', 'HIS', 'N', 'MET', 10.04)], [('CE1', 'HIS', 'CB', 'MET', 9.1), ('CE1', 'HIS', 'CG', 'MET', 9.88), ('CE1', 'HIS', 'SD', 'MET', 11.47), ('CE1', 'HIS', 'CE', 'MET', 12.04), ('CE1', 'HIS', 'O', 'MET', 6.78), ('CE1', 'HIS', 'C', 'MET', 8.01), ('CE1', 'HIS', 'CA', 'MET', 8.81), ('CE1', 'HIS', 'N', 'MET', 8.4)], [('NE2', 'HIS', 'CB', 'MET', 10.4), ('NE2', 'HIS', 'CG', 'MET', 11.2), ('NE2', 'HIS', 'SD', 'MET', 12.78), ('NE2', 'HIS', 'CE', 'MET', 13.33), ('NE2', 'HIS', 'O', 'MET', 8.04), ('NE2', 'HIS', 'C', 'MET', 9.27), ('NE2', 'HIS', 'CA', 'MET', 10.07), ('NE2', 'HIS', 'N', 'MET', 9.6)]]}
HIS_SER = { 
	'distances':
		[[6.07, 6.02], [5.97, 6.14], [5.44, 5.5], [6.94, 7.32], [6.22, 6.48], [7.04, 7.47]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 6.07), ('CB', 'HIS', 'OG', 'SER', 6.02)], [('CG', 'HIS', 'CB', 'SER', 5.97), ('CG', 'HIS', 'OG', 'SER', 6.14)], [('ND1', 'HIS', 'CB', 'SER', 5.44), ('ND1', 'HIS', 'OG', 'SER', 5.5)], [('CD2', 'HIS', 'CB', 'SER', 6.94), ('CD2', 'HIS', 'OG', 'SER', 7.32)], [('CE1', 'HIS', 'CB', 'SER', 6.22), ('CE1', 'HIS', 'OG', 'SER', 6.48)], [('NE2', 'HIS', 'CB', 'SER', 7.04), ('NE2', 'HIS', 'OG', 'SER', 7.47)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1chd_3_1_1_61')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_THR, d, 'A_1chd_3_1_1_61')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_MET, d, 'A_1chd_3_1_1_61')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_ASP, d, 'A_1chd_3_1_1_61')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_THR, d, 'A_1chd_3_1_1_61')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(MET_ASP, d, 'A_1chd_3_1_1_61')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_ASP, d, 'A_1chd_3_1_1_61')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(MET_THR, d, 'A_1chd_3_1_1_61')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_MET, d, 'A_1chd_3_1_1_61')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(HIS_SER, d, 'A_1chd_3_1_1_61')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'HIS_THR' :  match2,
		'SER_MET' :  match3,
		'THR_ASP' :  match4,
		'SER_THR' :  match5,
		'MET_ASP' :  match6,
		'SER_ASP' :  match7,
		'MET_THR' :  match8,
		'HIS_MET' :  match9,
		'HIS_SER' :  match10}