'''
FUNC:A_1a8q_1_11_1_10
PDB:1a8q
EC:1.11.1.10
RESI:trp,ser,met,asp,his
LOCI:a-28,94,95,223,252;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.81, 8.37], [7.35, 6.87], [6.88, 6.46], [6.51, 5.94], [5.64, 5.18], [5.3, 4.66]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.81), ('CB', 'HIS', 'OG', 'SER', 8.37)], [('CG', 'HIS', 'CB', 'SER', 7.35), ('CG', 'HIS', 'OG', 'SER', 6.87)], [('ND1', 'HIS', 'CB', 'SER', 6.88), ('ND1', 'HIS', 'OG', 'SER', 6.46)], [('CD2', 'HIS', 'CB', 'SER', 6.51), ('CD2', 'HIS', 'OG', 'SER', 5.94)], [('CE1', 'HIS', 'CB', 'SER', 5.64), ('CE1', 'HIS', 'OG', 'SER', 5.18)], [('NE2', 'HIS', 'CB', 'SER', 5.3), ('NE2', 'HIS', 'OG', 'SER', 4.66)]]}
HIS_MET = { 
	'distances':
		[[13.19, 13.39, 14.68, 16.16, 14.89, 13.74, 12.72, 11.34], [11.69, 11.92, 13.24, 14.69, 13.39, 12.24, 11.21, 9.84], [11.21, 11.61, 13.04, 14.39, 12.7, 11.59, 10.57, 9.21], [10.71, 10.81, 12.08, 13.57, 12.57, 11.39, 10.35, 8.99], [9.91, 10.33, 11.79, 13.11, 11.4, 10.29, 9.26, 7.9], [9.5, 9.72, 11.08, 12.5, 11.26, 10.1, 9.05, 7.68]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'MET', 13.19), ('CB', 'HIS', 'CG', 'MET', 13.39), ('CB', 'HIS', 'SD', 'MET', 14.68), ('CB', 'HIS', 'CE', 'MET', 16.16), ('CB', 'HIS', 'O', 'MET', 14.89), ('CB', 'HIS', 'C', 'MET', 13.74), ('CB', 'HIS', 'CA', 'MET', 12.72), ('CB', 'HIS', 'N', 'MET', 11.34)], [('CG', 'HIS', 'CB', 'MET', 11.69), ('CG', 'HIS', 'CG', 'MET', 11.92), ('CG', 'HIS', 'SD', 'MET', 13.24), ('CG', 'HIS', 'CE', 'MET', 14.69), ('CG', 'HIS', 'O', 'MET', 13.39), ('CG', 'HIS', 'C', 'MET', 12.24), ('CG', 'HIS', 'CA', 'MET', 11.21), ('CG', 'HIS', 'N', 'MET', 9.84)], [('ND1', 'HIS', 'CB', 'MET', 11.21), ('ND1', 'HIS', 'CG', 'MET', 11.61), ('ND1', 'HIS', 'SD', 'MET', 13.04), ('ND1', 'HIS', 'CE', 'MET', 14.39), ('ND1', 'HIS', 'O', 'MET', 12.7), ('ND1', 'HIS', 'C', 'MET', 11.59), ('ND1', 'HIS', 'CA', 'MET', 10.57), ('ND1', 'HIS', 'N', 'MET', 9.21)], [('CD2', 'HIS', 'CB', 'MET', 10.71), ('CD2', 'HIS', 'CG', 'MET', 10.81), ('CD2', 'HIS', 'SD', 'MET', 12.08), ('CD2', 'HIS', 'CE', 'MET', 13.57), ('CD2', 'HIS', 'O', 'MET', 12.57), ('CD2', 'HIS', 'C', 'MET', 11.39), ('CD2', 'HIS', 'CA', 'MET', 10.35), ('CD2', 'HIS', 'N', 'MET', 8.99)], [('CE1', 'HIS', 'CB', 'MET', 9.91), ('CE1', 'HIS', 'CG', 'MET', 10.33), ('CE1', 'HIS', 'SD', 'MET', 11.79), ('CE1', 'HIS', 'CE', 'MET', 13.11), ('CE1', 'HIS', 'O', 'MET', 11.4), ('CE1', 'HIS', 'C', 'MET', 10.29), ('CE1', 'HIS', 'CA', 'MET', 9.26), ('CE1', 'HIS', 'N', 'MET', 7.9)], [('NE2', 'HIS', 'CB', 'MET', 9.5), ('NE2', 'HIS', 'CG', 'MET', 9.72), ('NE2', 'HIS', 'SD', 'MET', 11.08), ('NE2', 'HIS', 'CE', 'MET', 12.5), ('NE2', 'HIS', 'O', 'MET', 11.26), ('NE2', 'HIS', 'C', 'MET', 10.1), ('NE2', 'HIS', 'CA', 'MET', 9.05), ('NE2', 'HIS', 'N', 'MET', 7.68)]]}
HIS_ASP = { 
	'distances':
		[[6.76, 5.65, 5.31, 5.67], [7.31, 5.93, 5.56, 5.67], [6.8, 5.32, 5.19, 4.78], [8.57, 7.15, 6.66, 6.84], [7.9, 6.41, 6.23, 5.77], [8.87, 7.37, 6.99, 6.88]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.76), ('CB', 'HIS', 'CG', 'ASP', 5.65), ('CB', 'HIS', 'OD1', 'ASP', 5.31), ('CB', 'HIS', 'OD2', 'ASP', 5.67)], [('CG', 'HIS', 'CB', 'ASP', 7.31), ('CG', 'HIS', 'CG', 'ASP', 5.93), ('CG', 'HIS', 'OD1', 'ASP', 5.56), ('CG', 'HIS', 'OD2', 'ASP', 5.67)], [('ND1', 'HIS', 'CB', 'ASP', 6.8), ('ND1', 'HIS', 'CG', 'ASP', 5.32), ('ND1', 'HIS', 'OD1', 'ASP', 5.19), ('ND1', 'HIS', 'OD2', 'ASP', 4.78)], [('CD2', 'HIS', 'CB', 'ASP', 8.57), ('CD2', 'HIS', 'CG', 'ASP', 7.15), ('CD2', 'HIS', 'OD1', 'ASP', 6.66), ('CD2', 'HIS', 'OD2', 'ASP', 6.84)], [('CE1', 'HIS', 'CB', 'ASP', 7.9), ('CE1', 'HIS', 'CG', 'ASP', 6.41), ('CE1', 'HIS', 'OD1', 'ASP', 6.23), ('CE1', 'HIS', 'OD2', 'ASP', 5.77)], [('NE2', 'HIS', 'CB', 'ASP', 8.87), ('NE2', 'HIS', 'CG', 'ASP', 7.37), ('NE2', 'HIS', 'OD1', 'ASP', 6.99), ('NE2', 'HIS', 'OD2', 'ASP', 6.88)]]}
SER_MET = { 
	'distances':
		[[7.06, 7.19, 8.85, 9.96, 8.23, 7.04, 6.28, 4.85], [6.88, 7.15, 8.64, 9.94, 8.66, 7.5, 6.41, 5.07]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'MET', 7.06), ('CB', 'SER', 'CG', 'MET', 7.19), ('CB', 'SER', 'SD', 'MET', 8.85), ('CB', 'SER', 'CE', 'MET', 9.96), ('CB', 'SER', 'O', 'MET', 8.23), ('CB', 'SER', 'C', 'MET', 7.04), ('CB', 'SER', 'CA', 'MET', 6.28), ('CB', 'SER', 'N', 'MET', 4.85)], [('OG', 'SER', 'CB', 'MET', 6.88), ('OG', 'SER', 'CG', 'MET', 7.15), ('OG', 'SER', 'SD', 'MET', 8.64), ('OG', 'SER', 'CE', 'MET', 9.94), ('OG', 'SER', 'O', 'MET', 8.66), ('OG', 'SER', 'C', 'MET', 7.5), ('OG', 'SER', 'CA', 'MET', 6.41), ('OG', 'SER', 'N', 'MET', 5.07)]]}
SER_TRP = { 
	'distances':
		[[8.15, 9.47, 10.63, 9.92, 11.65, 11.29, 9.56, 12.22, 10.64, 11.91, 7.54, 8.25, 8.01, 6.76], [7.62, 8.77, 9.97, 9.04, 10.87, 10.38, 8.55, 11.21, 9.54, 10.82, 7.08, 7.9, 7.75, 6.75]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TRP', 8.15), ('CB', 'SER', 'CG', 'TRP', 9.47), ('CB', 'SER', 'CD1', 'TRP', 10.63), ('CB', 'SER', 'CD2', 'TRP', 9.92), ('CB', 'SER', 'NE1', 'TRP', 11.65), ('CB', 'SER', 'CE2', 'TRP', 11.29), ('CB', 'SER', 'CE3', 'TRP', 9.56), ('CB', 'SER', 'CZ2', 'TRP', 12.22), ('CB', 'SER', 'CZ3', 'TRP', 10.64), ('CB', 'SER', 'CH2', 'TRP', 11.91), ('CB', 'SER', 'O', 'TRP', 7.54), ('CB', 'SER', 'C', 'TRP', 8.25), ('CB', 'SER', 'CA', 'TRP', 8.01), ('CB', 'SER', 'N', 'TRP', 6.76)], [('OG', 'SER', 'CB', 'TRP', 7.62), ('OG', 'SER', 'CG', 'TRP', 8.77), ('OG', 'SER', 'CD1', 'TRP', 9.97), ('OG', 'SER', 'CD2', 'TRP', 9.04), ('OG', 'SER', 'NE1', 'TRP', 10.87), ('OG', 'SER', 'CE2', 'TRP', 10.38), ('OG', 'SER', 'CE3', 'TRP', 8.55), ('OG', 'SER', 'CZ2', 'TRP', 11.21), ('OG', 'SER', 'CZ3', 'TRP', 9.54), ('OG', 'SER', 'CH2', 'TRP', 10.82), ('OG', 'SER', 'O', 'TRP', 7.08), ('OG', 'SER', 'C', 'TRP', 7.9), ('OG', 'SER', 'CA', 'TRP', 7.75), ('OG', 'SER', 'N', 'TRP', 6.75)]]}
HIS_TRP = { 
	'distances':
		[[12.42, 13.13, 14.47, 12.68, 14.92, 13.9, 11.51, 14.12, 11.74, 13.1, 10.21, 11.44, 12.25, 11.67], [11.16, 11.96, 13.29, 11.62, 13.83, 12.89, 10.53, 13.23, 10.92, 12.31, 9.15, 10.37, 11.04, 10.38], [11.39, 12.27, 13.58, 12.04, 14.19, 13.33, 11.05, 13.75, 11.53, 12.9, 9.74, 10.91, 11.37, 10.57], [9.86, 10.67, 12.01, 10.37, 12.58, 11.68, 9.33, 12.08, 9.82, 11.23, 7.82, 9.04, 9.71, 9.09], [10.36, 11.32, 12.61, 11.21, 13.29, 12.53, 10.34, 13.06, 10.96, 12.33, 8.97, 10.07, 10.38, 9.5], [9.28, 10.21, 11.52, 10.08, 12.2, 11.41, 9.18, 11.95, 9.84, 11.22, 7.69, 8.82, 9.23, 8.46]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TRP', 12.42), ('CB', 'HIS', 'CG', 'TRP', 13.13), ('CB', 'HIS', 'CD1', 'TRP', 14.47), ('CB', 'HIS', 'CD2', 'TRP', 12.68), ('CB', 'HIS', 'NE1', 'TRP', 14.92), ('CB', 'HIS', 'CE2', 'TRP', 13.9), ('CB', 'HIS', 'CE3', 'TRP', 11.51), ('CB', 'HIS', 'CZ2', 'TRP', 14.12), ('CB', 'HIS', 'CZ3', 'TRP', 11.74), ('CB', 'HIS', 'CH2', 'TRP', 13.1), ('CB', 'HIS', 'O', 'TRP', 10.21), ('CB', 'HIS', 'C', 'TRP', 11.44), ('CB', 'HIS', 'CA', 'TRP', 12.25), ('CB', 'HIS', 'N', 'TRP', 11.67)], [('CG', 'HIS', 'CB', 'TRP', 11.16), ('CG', 'HIS', 'CG', 'TRP', 11.96), ('CG', 'HIS', 'CD1', 'TRP', 13.29), ('CG', 'HIS', 'CD2', 'TRP', 11.62), ('CG', 'HIS', 'NE1', 'TRP', 13.83), ('CG', 'HIS', 'CE2', 'TRP', 12.89), ('CG', 'HIS', 'CE3', 'TRP', 10.53), ('CG', 'HIS', 'CZ2', 'TRP', 13.23), ('CG', 'HIS', 'CZ3', 'TRP', 10.92), ('CG', 'HIS', 'CH2', 'TRP', 12.31), ('CG', 'HIS', 'O', 'TRP', 9.15), ('CG', 'HIS', 'C', 'TRP', 10.37), ('CG', 'HIS', 'CA', 'TRP', 11.04), ('CG', 'HIS', 'N', 'TRP', 10.38)], [('ND1', 'HIS', 'CB', 'TRP', 11.39), ('ND1', 'HIS', 'CG', 'TRP', 12.27), ('ND1', 'HIS', 'CD1', 'TRP', 13.58), ('ND1', 'HIS', 'CD2', 'TRP', 12.04), ('ND1', 'HIS', 'NE1', 'TRP', 14.19), ('ND1', 'HIS', 'CE2', 'TRP', 13.33), ('ND1', 'HIS', 'CE3', 'TRP', 11.05), ('ND1', 'HIS', 'CZ2', 'TRP', 13.75), ('ND1', 'HIS', 'CZ3', 'TRP', 11.53), ('ND1', 'HIS', 'CH2', 'TRP', 12.9), ('ND1', 'HIS', 'O', 'TRP', 9.74), ('ND1', 'HIS', 'C', 'TRP', 10.91), ('ND1', 'HIS', 'CA', 'TRP', 11.37), ('ND1', 'HIS', 'N', 'TRP', 10.57)], [('CD2', 'HIS', 'CB', 'TRP', 9.86), ('CD2', 'HIS', 'CG', 'TRP', 10.67), ('CD2', 'HIS', 'CD1', 'TRP', 12.01), ('CD2', 'HIS', 'CD2', 'TRP', 10.37), ('CD2', 'HIS', 'NE1', 'TRP', 12.58), ('CD2', 'HIS', 'CE2', 'TRP', 11.68), ('CD2', 'HIS', 'CE3', 'TRP', 9.33), ('CD2', 'HIS', 'CZ2', 'TRP', 12.08), ('CD2', 'HIS', 'CZ3', 'TRP', 9.82), ('CD2', 'HIS', 'CH2', 'TRP', 11.23), ('CD2', 'HIS', 'O', 'TRP', 7.82), ('CD2', 'HIS', 'C', 'TRP', 9.04), ('CD2', 'HIS', 'CA', 'TRP', 9.71), ('CD2', 'HIS', 'N', 'TRP', 9.09)], [('CE1', 'HIS', 'CB', 'TRP', 10.36), ('CE1', 'HIS', 'CG', 'TRP', 11.32), ('CE1', 'HIS', 'CD1', 'TRP', 12.61), ('CE1', 'HIS', 'CD2', 'TRP', 11.21), ('CE1', 'HIS', 'NE1', 'TRP', 13.29), ('CE1', 'HIS', 'CE2', 'TRP', 12.53), ('CE1', 'HIS', 'CE3', 'TRP', 10.34), ('CE1', 'HIS', 'CZ2', 'TRP', 13.06), ('CE1', 'HIS', 'CZ3', 'TRP', 10.96), ('CE1', 'HIS', 'CH2', 'TRP', 12.33), ('CE1', 'HIS', 'O', 'TRP', 8.97), ('CE1', 'HIS', 'C', 'TRP', 10.07), ('CE1', 'HIS', 'CA', 'TRP', 10.38), ('CE1', 'HIS', 'N', 'TRP', 9.5)], [('NE2', 'HIS', 'CB', 'TRP', 9.28), ('NE2', 'HIS', 'CG', 'TRP', 10.21), ('NE2', 'HIS', 'CD1', 'TRP', 11.52), ('NE2', 'HIS', 'CD2', 'TRP', 10.08), ('NE2', 'HIS', 'NE1', 'TRP', 12.2), ('NE2', 'HIS', 'CE2', 'TRP', 11.41), ('NE2', 'HIS', 'CE3', 'TRP', 9.18), ('NE2', 'HIS', 'CZ2', 'TRP', 11.95), ('NE2', 'HIS', 'CZ3', 'TRP', 9.84), ('NE2', 'HIS', 'CH2', 'TRP', 11.22), ('NE2', 'HIS', 'O', 'TRP', 7.69), ('NE2', 'HIS', 'C', 'TRP', 8.82), ('NE2', 'HIS', 'CA', 'TRP', 9.23), ('NE2', 'HIS', 'N', 'TRP', 8.46)]]}
MET_TRP = { 
	'distances':
		[[6.89, 7.91, 8.41, 8.84, 9.52, 9.76, 9.28, 10.92, 10.48, 11.21, 8.84, 8.8, 7.63, 6.89], [5.91, 7.07, 7.53, 8.21, 8.78, 9.14, 8.8, 10.42, 10.11, 10.81, 8.01, 7.75, 6.44, 5.72], [5.72, 6.44, 6.46, 7.69, 7.66, 8.31, 8.59, 9.62, 9.83, 10.27, 8.47, 7.94, 6.54, 6.38], [7.38, 8.05, 7.86, 9.34, 9.02, 9.83, 10.32, 11.14, 11.54, 11.89, 10.07, 9.47, 8.0, 7.73], [9.51, 10.67, 11.05, 11.76, 12.26, 12.66, 12.24, 13.89, 13.49, 14.25, 11.23, 11.12, 9.87, 8.84], [8.69, 9.94, 10.47, 10.98, 11.7, 11.99, 11.36, 13.21, 12.63, 13.47, 10.16, 10.13, 8.97, 7.85], [7.94, 9.12, 9.77, 10.01, 10.9, 11.04, 10.27, 12.18, 11.47, 12.35, 9.36, 9.48, 8.42, 7.39], [7.74, 9.02, 9.88, 9.77, 11.0, 10.95, 9.82, 12.03, 11.01, 12.03, 8.57, 8.88, 8.05, 6.88]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'TRP', 6.89), ('CB', 'MET', 'CG', 'TRP', 7.91), ('CB', 'MET', 'CD1', 'TRP', 8.41), ('CB', 'MET', 'CD2', 'TRP', 8.84), ('CB', 'MET', 'NE1', 'TRP', 9.52), ('CB', 'MET', 'CE2', 'TRP', 9.76), ('CB', 'MET', 'CE3', 'TRP', 9.28), ('CB', 'MET', 'CZ2', 'TRP', 10.92), ('CB', 'MET', 'CZ3', 'TRP', 10.48), ('CB', 'MET', 'CH2', 'TRP', 11.21), ('CB', 'MET', 'O', 'TRP', 8.84), ('CB', 'MET', 'C', 'TRP', 8.8), ('CB', 'MET', 'CA', 'TRP', 7.63), ('CB', 'MET', 'N', 'TRP', 6.89)], [('CG', 'MET', 'CB', 'TRP', 5.91), ('CG', 'MET', 'CG', 'TRP', 7.07), ('CG', 'MET', 'CD1', 'TRP', 7.53), ('CG', 'MET', 'CD2', 'TRP', 8.21), ('CG', 'MET', 'NE1', 'TRP', 8.78), ('CG', 'MET', 'CE2', 'TRP', 9.14), ('CG', 'MET', 'CE3', 'TRP', 8.8), ('CG', 'MET', 'CZ2', 'TRP', 10.42), ('CG', 'MET', 'CZ3', 'TRP', 10.11), ('CG', 'MET', 'CH2', 'TRP', 10.81), ('CG', 'MET', 'O', 'TRP', 8.01), ('CG', 'MET', 'C', 'TRP', 7.75), ('CG', 'MET', 'CA', 'TRP', 6.44), ('CG', 'MET', 'N', 'TRP', 5.72)], [('SD', 'MET', 'CB', 'TRP', 5.72), ('SD', 'MET', 'CG', 'TRP', 6.44), ('SD', 'MET', 'CD1', 'TRP', 6.46), ('SD', 'MET', 'CD2', 'TRP', 7.69), ('SD', 'MET', 'NE1', 'TRP', 7.66), ('SD', 'MET', 'CE2', 'TRP', 8.31), ('SD', 'MET', 'CE3', 'TRP', 8.59), ('SD', 'MET', 'CZ2', 'TRP', 9.62), ('SD', 'MET', 'CZ3', 'TRP', 9.83), ('SD', 'MET', 'CH2', 'TRP', 10.27), ('SD', 'MET', 'O', 'TRP', 8.47), ('SD', 'MET', 'C', 'TRP', 7.94), ('SD', 'MET', 'CA', 'TRP', 6.54), ('SD', 'MET', 'N', 'TRP', 6.38)], [('CE', 'MET', 'CB', 'TRP', 7.38), ('CE', 'MET', 'CG', 'TRP', 8.05), ('CE', 'MET', 'CD1', 'TRP', 7.86), ('CE', 'MET', 'CD2', 'TRP', 9.34), ('CE', 'MET', 'NE1', 'TRP', 9.02), ('CE', 'MET', 'CE2', 'TRP', 9.83), ('CE', 'MET', 'CE3', 'TRP', 10.32), ('CE', 'MET', 'CZ2', 'TRP', 11.14), ('CE', 'MET', 'CZ3', 'TRP', 11.54), ('CE', 'MET', 'CH2', 'TRP', 11.89), ('CE', 'MET', 'O', 'TRP', 10.07), ('CE', 'MET', 'C', 'TRP', 9.47), ('CE', 'MET', 'CA', 'TRP', 8.0), ('CE', 'MET', 'N', 'TRP', 7.73)], [('O', 'MET', 'CB', 'TRP', 9.51), ('O', 'MET', 'CG', 'TRP', 10.67), ('O', 'MET', 'CD1', 'TRP', 11.05), ('O', 'MET', 'CD2', 'TRP', 11.76), ('O', 'MET', 'NE1', 'TRP', 12.26), ('O', 'MET', 'CE2', 'TRP', 12.66), ('O', 'MET', 'CE3', 'TRP', 12.24), ('O', 'MET', 'CZ2', 'TRP', 13.89), ('O', 'MET', 'CZ3', 'TRP', 13.49), ('O', 'MET', 'CH2', 'TRP', 14.25), ('O', 'MET', 'O', 'TRP', 11.23), ('O', 'MET', 'C', 'TRP', 11.12), ('O', 'MET', 'CA', 'TRP', 9.87), ('O', 'MET', 'N', 'TRP', 8.84)], [('C', 'MET', 'CB', 'TRP', 8.69), ('C', 'MET', 'CG', 'TRP', 9.94), ('C', 'MET', 'CD1', 'TRP', 10.47), ('C', 'MET', 'CD2', 'TRP', 10.98), ('C', 'MET', 'NE1', 'TRP', 11.7), ('C', 'MET', 'CE2', 'TRP', 11.99), ('C', 'MET', 'CE3', 'TRP', 11.36), ('C', 'MET', 'CZ2', 'TRP', 13.21), ('C', 'MET', 'CZ3', 'TRP', 12.63), ('C', 'MET', 'CH2', 'TRP', 13.47), ('C', 'MET', 'O', 'TRP', 10.16), ('C', 'MET', 'C', 'TRP', 10.13), ('C', 'MET', 'CA', 'TRP', 8.97), ('C', 'MET', 'N', 'TRP', 7.85)], [('CA', 'MET', 'CB', 'TRP', 7.94), ('CA', 'MET', 'CG', 'TRP', 9.12), ('CA', 'MET', 'CD1', 'TRP', 9.77), ('CA', 'MET', 'CD2', 'TRP', 10.01), ('CA', 'MET', 'NE1', 'TRP', 10.9), ('CA', 'MET', 'CE2', 'TRP', 11.04), ('CA', 'MET', 'CE3', 'TRP', 10.27), ('CA', 'MET', 'CZ2', 'TRP', 12.18), ('CA', 'MET', 'CZ3', 'TRP', 11.47), ('CA', 'MET', 'CH2', 'TRP', 12.35), ('CA', 'MET', 'O', 'TRP', 9.36), ('CA', 'MET', 'C', 'TRP', 9.48), ('CA', 'MET', 'CA', 'TRP', 8.42), ('CA', 'MET', 'N', 'TRP', 7.39)], [('N', 'MET', 'CB', 'TRP', 7.74), ('N', 'MET', 'CG', 'TRP', 9.02), ('N', 'MET', 'CD1', 'TRP', 9.88), ('N', 'MET', 'CD2', 'TRP', 9.77), ('N', 'MET', 'NE1', 'TRP', 11.0), ('N', 'MET', 'CE2', 'TRP', 10.95), ('N', 'MET', 'CE3', 'TRP', 9.82), ('N', 'MET', 'CZ2', 'TRP', 12.03), ('N', 'MET', 'CZ3', 'TRP', 11.01), ('N', 'MET', 'CH2', 'TRP', 12.03), ('N', 'MET', 'O', 'TRP', 8.57), ('N', 'MET', 'C', 'TRP', 8.88), ('N', 'MET', 'CA', 'TRP', 8.05), ('N', 'MET', 'N', 'TRP', 6.88)]]}
ASP_TRP = { 
	'distances':
		[[15.91, 16.62, 17.89, 16.17, 18.31, 17.32, 15.04, 17.47, 15.18, 16.44, 14.3, 15.51, 16.04, 15.32], [14.42, 15.15, 16.43, 14.74, 16.89, 15.92, 13.64, 16.13, 13.85, 15.14, 12.84, 14.04, 14.54, 13.81], [13.74, 14.36, 15.63, 13.86, 16.0, 14.98, 12.71, 15.11, 12.83, 14.08, 12.18, 13.39, 13.95, 13.34], [14.05, 14.91, 16.19, 14.63, 16.76, 15.87, 13.6, 16.2, 13.96, 15.29, 12.51, 13.68, 14.11, 13.26]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TRP', 15.91), ('CB', 'ASP', 'CG', 'TRP', 16.62), ('CB', 'ASP', 'CD1', 'TRP', 17.89), ('CB', 'ASP', 'CD2', 'TRP', 16.17), ('CB', 'ASP', 'NE1', 'TRP', 18.31), ('CB', 'ASP', 'CE2', 'TRP', 17.32), ('CB', 'ASP', 'CE3', 'TRP', 15.04), ('CB', 'ASP', 'CZ2', 'TRP', 17.47), ('CB', 'ASP', 'CZ3', 'TRP', 15.18), ('CB', 'ASP', 'CH2', 'TRP', 16.44), ('CB', 'ASP', 'O', 'TRP', 14.3), ('CB', 'ASP', 'C', 'TRP', 15.51), ('CB', 'ASP', 'CA', 'TRP', 16.04), ('CB', 'ASP', 'N', 'TRP', 15.32)], [('CG', 'ASP', 'CB', 'TRP', 14.42), ('CG', 'ASP', 'CG', 'TRP', 15.15), ('CG', 'ASP', 'CD1', 'TRP', 16.43), ('CG', 'ASP', 'CD2', 'TRP', 14.74), ('CG', 'ASP', 'NE1', 'TRP', 16.89), ('CG', 'ASP', 'CE2', 'TRP', 15.92), ('CG', 'ASP', 'CE3', 'TRP', 13.64), ('CG', 'ASP', 'CZ2', 'TRP', 16.13), ('CG', 'ASP', 'CZ3', 'TRP', 13.85), ('CG', 'ASP', 'CH2', 'TRP', 15.14), ('CG', 'ASP', 'O', 'TRP', 12.84), ('CG', 'ASP', 'C', 'TRP', 14.04), ('CG', 'ASP', 'CA', 'TRP', 14.54), ('CG', 'ASP', 'N', 'TRP', 13.81)], [('OD1', 'ASP', 'CB', 'TRP', 13.74), ('OD1', 'ASP', 'CG', 'TRP', 14.36), ('OD1', 'ASP', 'CD1', 'TRP', 15.63), ('OD1', 'ASP', 'CD2', 'TRP', 13.86), ('OD1', 'ASP', 'NE1', 'TRP', 16.0), ('OD1', 'ASP', 'CE2', 'TRP', 14.98), ('OD1', 'ASP', 'CE3', 'TRP', 12.71), ('OD1', 'ASP', 'CZ2', 'TRP', 15.11), ('OD1', 'ASP', 'CZ3', 'TRP', 12.83), ('OD1', 'ASP', 'CH2', 'TRP', 14.08), ('OD1', 'ASP', 'O', 'TRP', 12.18), ('OD1', 'ASP', 'C', 'TRP', 13.39), ('OD1', 'ASP', 'CA', 'TRP', 13.95), ('OD1', 'ASP', 'N', 'TRP', 13.34)], [('OD2', 'ASP', 'CB', 'TRP', 14.05), ('OD2', 'ASP', 'CG', 'TRP', 14.91), ('OD2', 'ASP', 'CD1', 'TRP', 16.19), ('OD2', 'ASP', 'CD2', 'TRP', 14.63), ('OD2', 'ASP', 'NE1', 'TRP', 16.76), ('OD2', 'ASP', 'CE2', 'TRP', 15.87), ('OD2', 'ASP', 'CE3', 'TRP', 13.6), ('OD2', 'ASP', 'CZ2', 'TRP', 16.2), ('OD2', 'ASP', 'CZ3', 'TRP', 13.96), ('OD2', 'ASP', 'CH2', 'TRP', 15.29), ('OD2', 'ASP', 'O', 'TRP', 12.51), ('OD2', 'ASP', 'C', 'TRP', 13.68), ('OD2', 'ASP', 'CA', 'TRP', 14.11), ('OD2', 'ASP', 'N', 'TRP', 13.26)]]}
ASP_MET = { 
	'distances':
		[[15.32, 16.0, 17.4, 18.7, 16.6, 15.64, 14.6, 13.37], [13.89, 14.53, 15.92, 17.24, 15.26, 14.27, 13.2, 11.95], [13.53, 14.14, 15.42, 16.82, 15.16, 14.15, 12.99, 11.77], [13.29, 13.91, 15.39, 16.64, 14.45, 13.45, 12.48, 11.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'MET', 15.32), ('CB', 'ASP', 'CG', 'MET', 16.0), ('CB', 'ASP', 'SD', 'MET', 17.4), ('CB', 'ASP', 'CE', 'MET', 18.7), ('CB', 'ASP', 'O', 'MET', 16.6), ('CB', 'ASP', 'C', 'MET', 15.64), ('CB', 'ASP', 'CA', 'MET', 14.6), ('CB', 'ASP', 'N', 'MET', 13.37)], [('CG', 'ASP', 'CB', 'MET', 13.89), ('CG', 'ASP', 'CG', 'MET', 14.53), ('CG', 'ASP', 'SD', 'MET', 15.92), ('CG', 'ASP', 'CE', 'MET', 17.24), ('CG', 'ASP', 'O', 'MET', 15.26), ('CG', 'ASP', 'C', 'MET', 14.27), ('CG', 'ASP', 'CA', 'MET', 13.2), ('CG', 'ASP', 'N', 'MET', 11.95)], [('OD1', 'ASP', 'CB', 'MET', 13.53), ('OD1', 'ASP', 'CG', 'MET', 14.14), ('OD1', 'ASP', 'SD', 'MET', 15.42), ('OD1', 'ASP', 'CE', 'MET', 16.82), ('OD1', 'ASP', 'O', 'MET', 15.16), ('OD1', 'ASP', 'C', 'MET', 14.15), ('OD1', 'ASP', 'CA', 'MET', 12.99), ('OD1', 'ASP', 'N', 'MET', 11.77)], [('OD2', 'ASP', 'CB', 'MET', 13.29), ('OD2', 'ASP', 'CG', 'MET', 13.91), ('OD2', 'ASP', 'SD', 'MET', 15.39), ('OD2', 'ASP', 'CE', 'MET', 16.64), ('OD2', 'ASP', 'O', 'MET', 14.45), ('OD2', 'ASP', 'C', 'MET', 13.45), ('OD2', 'ASP', 'CA', 'MET', 12.48), ('OD2', 'ASP', 'N', 'MET', 11.21)]]}
ASP_SER = { 
	'distances':
		[[11.42, 10.98], [9.97, 9.49], [9.84, 9.17], [9.16, 8.86]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.42), ('CB', 'ASP', 'OG', 'SER', 10.98)], [('CG', 'ASP', 'CB', 'SER', 9.97), ('CG', 'ASP', 'OG', 'SER', 9.49)], [('OD1', 'ASP', 'CB', 'SER', 9.84), ('OD1', 'ASP', 'OG', 'SER', 9.17)], [('OD2', 'ASP', 'CB', 'SER', 9.16), ('OD2', 'ASP', 'OG', 'SER', 8.86)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_1a8q_1_11_1_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_MET, d, 'A_1a8q_1_11_1_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1a8q_1_11_1_10')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_MET, d, 'A_1a8q_1_11_1_10')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_TRP, d, 'A_1a8q_1_11_1_10')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_TRP, d, 'A_1a8q_1_11_1_10')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(MET_TRP, d, 'A_1a8q_1_11_1_10')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_TRP, d, 'A_1a8q_1_11_1_10')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASP_MET, d, 'A_1a8q_1_11_1_10')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASP_SER, d, 'A_1a8q_1_11_1_10')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'HIS_MET' :  match2,
		'HIS_ASP' :  match3,
		'SER_MET' :  match4,
		'SER_TRP' :  match5,
		'HIS_TRP' :  match6,
		'MET_TRP' :  match7,
		'ASP_TRP' :  match8,
		'ASP_MET' :  match9,
		'ASP_SER' :  match10}