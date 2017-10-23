'''
FUNC:A_1a7u_1_11_1_10
PDB:1a7u
EC:1.11.1.10
RESI:phe,ser,met,asp,his
LOCI:a-32,98,99,228,257;
'''
import motifFunctions as cmd
HIS_SER = { 
	'distances':
		[[8.79, 8.35], [7.33, 6.83], [6.89, 6.38], [6.54, 6.0], [5.66, 5.06], [5.36, 4.69]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.79), ('CB', 'HIS', 'OG', 'SER', 8.35)], [('CG', 'HIS', 'CB', 'SER', 7.33), ('CG', 'HIS', 'OG', 'SER', 6.83)], [('ND1', 'HIS', 'CB', 'SER', 6.89), ('ND1', 'HIS', 'OG', 'SER', 6.38)], [('CD2', 'HIS', 'CB', 'SER', 6.54), ('CD2', 'HIS', 'OG', 'SER', 6.0)], [('CE1', 'HIS', 'CB', 'SER', 5.66), ('CE1', 'HIS', 'OG', 'SER', 5.06)], [('NE2', 'HIS', 'CB', 'SER', 5.36), ('NE2', 'HIS', 'OG', 'SER', 4.69)]]}
PHE_MET = { 
	'distances':
		[[6.91, 6.41, 5.8, 7.55, 10.11, 9.21, 8.04, 7.83], [8.22, 7.49, 6.64, 8.23, 11.4, 10.57, 9.37, 9.21], [9.23, 8.48, 7.84, 9.46, 12.39, 11.51, 10.21, 9.87], [8.65, 7.82, 6.59, 7.9, 11.77, 11.06, 9.95, 10.02], [10.42, 9.54, 8.76, 10.24, 13.56, 12.74, 11.44, 11.17], [9.96, 9.03, 7.76, 8.91, 13.03, 12.37, 11.23, 11.31], [10.78, 9.82, 8.77, 10.04, 13.89, 13.17, 11.93, 11.85]],
	'comparisons':
		[[('CB', 'PHE', 'CB', 'MET', 6.91), ('CB', 'PHE', 'CG', 'MET', 6.41), ('CB', 'PHE', 'SD', 'MET', 5.8), ('CB', 'PHE', 'CE', 'MET', 7.55), ('CB', 'PHE', 'O', 'MET', 10.11), ('CB', 'PHE', 'C', 'MET', 9.21), ('CB', 'PHE', 'CA', 'MET', 8.04), ('CB', 'PHE', 'N', 'MET', 7.83)], [('CG', 'PHE', 'CB', 'MET', 8.22), ('CG', 'PHE', 'CG', 'MET', 7.49), ('CG', 'PHE', 'SD', 'MET', 6.64), ('CG', 'PHE', 'CE', 'MET', 8.23), ('CG', 'PHE', 'O', 'MET', 11.4), ('CG', 'PHE', 'C', 'MET', 10.57), ('CG', 'PHE', 'CA', 'MET', 9.37), ('CG', 'PHE', 'N', 'MET', 9.21)], [('CD1', 'PHE', 'CB', 'MET', 9.23), ('CD1', 'PHE', 'CG', 'MET', 8.48), ('CD1', 'PHE', 'SD', 'MET', 7.84), ('CD1', 'PHE', 'CE', 'MET', 9.46), ('CD1', 'PHE', 'O', 'MET', 12.39), ('CD1', 'PHE', 'C', 'MET', 11.51), ('CD1', 'PHE', 'CA', 'MET', 10.21), ('CD1', 'PHE', 'N', 'MET', 9.87)], [('CD2', 'PHE', 'CB', 'MET', 8.65), ('CD2', 'PHE', 'CG', 'MET', 7.82), ('CD2', 'PHE', 'SD', 'MET', 6.59), ('CD2', 'PHE', 'CE', 'MET', 7.9), ('CD2', 'PHE', 'O', 'MET', 11.77), ('CD2', 'PHE', 'C', 'MET', 11.06), ('CD2', 'PHE', 'CA', 'MET', 9.95), ('CD2', 'PHE', 'N', 'MET', 10.02)], [('CE1', 'PHE', 'CB', 'MET', 10.42), ('CE1', 'PHE', 'CG', 'MET', 9.54), ('CE1', 'PHE', 'SD', 'MET', 8.76), ('CE1', 'PHE', 'CE', 'MET', 10.24), ('CE1', 'PHE', 'O', 'MET', 13.56), ('CE1', 'PHE', 'C', 'MET', 12.74), ('CE1', 'PHE', 'CA', 'MET', 11.44), ('CE1', 'PHE', 'N', 'MET', 11.17)], [('CE2', 'PHE', 'CB', 'MET', 9.96), ('CE2', 'PHE', 'CG', 'MET', 9.03), ('CE2', 'PHE', 'SD', 'MET', 7.76), ('CE2', 'PHE', 'CE', 'MET', 8.91), ('CE2', 'PHE', 'O', 'MET', 13.03), ('CE2', 'PHE', 'C', 'MET', 12.37), ('CE2', 'PHE', 'CA', 'MET', 11.23), ('CE2', 'PHE', 'N', 'MET', 11.31)], [('CZ', 'PHE', 'CB', 'MET', 10.78), ('CZ', 'PHE', 'CG', 'MET', 9.82), ('CZ', 'PHE', 'SD', 'MET', 8.77), ('CZ', 'PHE', 'CE', 'MET', 10.04), ('CZ', 'PHE', 'O', 'MET', 13.89), ('CZ', 'PHE', 'C', 'MET', 13.17), ('CZ', 'PHE', 'CA', 'MET', 11.93), ('CZ', 'PHE', 'N', 'MET', 11.85)]]}
ASP_MET = { 
	'distances':
		[[16.05, 16.16, 17.51, 18.92, 16.86, 16.02, 15.13, 13.8], [14.58, 14.66, 15.99, 17.42, 15.51, 14.64, 13.7, 12.37], [14.35, 14.31, 15.55, 17.02, 15.52, 14.64, 13.58, 12.28], [13.74, 13.94, 15.33, 16.72, 14.51, 13.65, 12.79, 11.45]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'MET', 16.05), ('CB', 'ASP', 'CG', 'MET', 16.16), ('CB', 'ASP', 'SD', 'MET', 17.51), ('CB', 'ASP', 'CE', 'MET', 18.92), ('CB', 'ASP', 'O', 'MET', 16.86), ('CB', 'ASP', 'C', 'MET', 16.02), ('CB', 'ASP', 'CA', 'MET', 15.13), ('CB', 'ASP', 'N', 'MET', 13.8)], [('CG', 'ASP', 'CB', 'MET', 14.58), ('CG', 'ASP', 'CG', 'MET', 14.66), ('CG', 'ASP', 'SD', 'MET', 15.99), ('CG', 'ASP', 'CE', 'MET', 17.42), ('CG', 'ASP', 'O', 'MET', 15.51), ('CG', 'ASP', 'C', 'MET', 14.64), ('CG', 'ASP', 'CA', 'MET', 13.7), ('CG', 'ASP', 'N', 'MET', 12.37)], [('OD1', 'ASP', 'CB', 'MET', 14.35), ('OD1', 'ASP', 'CG', 'MET', 14.31), ('OD1', 'ASP', 'SD', 'MET', 15.55), ('OD1', 'ASP', 'CE', 'MET', 17.02), ('OD1', 'ASP', 'O', 'MET', 15.52), ('OD1', 'ASP', 'C', 'MET', 14.64), ('OD1', 'ASP', 'CA', 'MET', 13.58), ('OD1', 'ASP', 'N', 'MET', 12.28)], [('OD2', 'ASP', 'CB', 'MET', 13.74), ('OD2', 'ASP', 'CG', 'MET', 13.94), ('OD2', 'ASP', 'SD', 'MET', 15.33), ('OD2', 'ASP', 'CE', 'MET', 16.72), ('OD2', 'ASP', 'O', 'MET', 14.51), ('OD2', 'ASP', 'C', 'MET', 13.65), ('OD2', 'ASP', 'CA', 'MET', 12.79), ('OD2', 'ASP', 'N', 'MET', 11.45)]]}
HIS_ASP = { 
	'distances':
		[[6.67, 5.61, 5.27, 5.7], [7.23, 5.88, 5.55, 5.59], [6.77, 5.31, 5.21, 4.71], [8.57, 7.17, 6.76, 6.81], [7.96, 6.48, 6.33, 5.76], [8.92, 7.43, 7.12, 6.85]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.67), ('CB', 'HIS', 'CG', 'ASP', 5.61), ('CB', 'HIS', 'OD1', 'ASP', 5.27), ('CB', 'HIS', 'OD2', 'ASP', 5.7)], [('CG', 'HIS', 'CB', 'ASP', 7.23), ('CG', 'HIS', 'CG', 'ASP', 5.88), ('CG', 'HIS', 'OD1', 'ASP', 5.55), ('CG', 'HIS', 'OD2', 'ASP', 5.59)], [('ND1', 'HIS', 'CB', 'ASP', 6.77), ('ND1', 'HIS', 'CG', 'ASP', 5.31), ('ND1', 'HIS', 'OD1', 'ASP', 5.21), ('ND1', 'HIS', 'OD2', 'ASP', 4.71)], [('CD2', 'HIS', 'CB', 'ASP', 8.57), ('CD2', 'HIS', 'CG', 'ASP', 7.17), ('CD2', 'HIS', 'OD1', 'ASP', 6.76), ('CD2', 'HIS', 'OD2', 'ASP', 6.81)], [('CE1', 'HIS', 'CB', 'ASP', 7.96), ('CE1', 'HIS', 'CG', 'ASP', 6.48), ('CE1', 'HIS', 'OD1', 'ASP', 6.33), ('CE1', 'HIS', 'OD2', 'ASP', 5.76)], [('NE2', 'HIS', 'CB', 'ASP', 8.92), ('NE2', 'HIS', 'CG', 'ASP', 7.43), ('NE2', 'HIS', 'OD1', 'ASP', 7.12), ('NE2', 'HIS', 'OD2', 'ASP', 6.85)]]}
SER_MET = { 
	'distances':
		[[7.09, 7.75, 9.08, 10.43, 8.34, 7.2, 6.38, 4.91], [7.18, 7.46, 8.79, 10.22, 8.74, 7.68, 6.55, 5.17]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'MET', 7.09), ('CB', 'SER', 'CG', 'MET', 7.75), ('CB', 'SER', 'SD', 'MET', 9.08), ('CB', 'SER', 'CE', 'MET', 10.43), ('CB', 'SER', 'O', 'MET', 8.34), ('CB', 'SER', 'C', 'MET', 7.2), ('CB', 'SER', 'CA', 'MET', 6.38), ('CB', 'SER', 'N', 'MET', 4.91)], [('OG', 'SER', 'CB', 'MET', 7.18), ('OG', 'SER', 'CG', 'MET', 7.46), ('OG', 'SER', 'SD', 'MET', 8.79), ('OG', 'SER', 'CE', 'MET', 10.22), ('OG', 'SER', 'O', 'MET', 8.74), ('OG', 'SER', 'C', 'MET', 7.68), ('OG', 'SER', 'CA', 'MET', 6.55), ('OG', 'SER', 'N', 'MET', 5.17)]]}
SER_PHE = { 
	'distances':
		[[8.45, 9.75, 10.01, 10.9, 11.34, 12.12, 12.33], [7.96, 9.12, 9.22, 10.31, 10.48, 11.43, 11.53]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'PHE', 8.45), ('CB', 'SER', 'CG', 'PHE', 9.75), ('CB', 'SER', 'CD1', 'PHE', 10.01), ('CB', 'SER', 'CD2', 'PHE', 10.9), ('CB', 'SER', 'CE1', 'PHE', 11.34), ('CB', 'SER', 'CE2', 'PHE', 12.12), ('CB', 'SER', 'CZ', 'PHE', 12.33)], [('OG', 'SER', 'CB', 'PHE', 7.96), ('OG', 'SER', 'CG', 'PHE', 9.12), ('OG', 'SER', 'CD1', 'PHE', 9.22), ('OG', 'SER', 'CD2', 'PHE', 10.31), ('OG', 'SER', 'CE1', 'PHE', 10.48), ('OG', 'SER', 'CE2', 'PHE', 11.43), ('OG', 'SER', 'CZ', 'PHE', 11.53)]]}
HIS_PHE = { 
	'distances':
		[[12.21, 12.8, 12.12, 14.19, 12.98, 14.9, 14.35], [11.03, 11.73, 11.17, 13.11, 12.14, 13.91, 13.48], [11.32, 12.12, 11.68, 13.47, 12.7, 14.33, 13.99], [9.72, 10.44, 9.92, 11.82, 10.95, 12.65, 12.27], [10.26, 11.15, 10.83, 12.47, 11.93, 13.4, 13.17], [9.18, 10.05, 9.71, 11.4, 10.82, 12.32, 12.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'PHE', 12.21), ('CB', 'HIS', 'CG', 'PHE', 12.8), ('CB', 'HIS', 'CD1', 'PHE', 12.12), ('CB', 'HIS', 'CD2', 'PHE', 14.19), ('CB', 'HIS', 'CE1', 'PHE', 12.98), ('CB', 'HIS', 'CE2', 'PHE', 14.9), ('CB', 'HIS', 'CZ', 'PHE', 14.35)], [('CG', 'HIS', 'CB', 'PHE', 11.03), ('CG', 'HIS', 'CG', 'PHE', 11.73), ('CG', 'HIS', 'CD1', 'PHE', 11.17), ('CG', 'HIS', 'CD2', 'PHE', 13.11), ('CG', 'HIS', 'CE1', 'PHE', 12.14), ('CG', 'HIS', 'CE2', 'PHE', 13.91), ('CG', 'HIS', 'CZ', 'PHE', 13.48)], [('ND1', 'HIS', 'CB', 'PHE', 11.32), ('ND1', 'HIS', 'CG', 'PHE', 12.12), ('ND1', 'HIS', 'CD1', 'PHE', 11.68), ('ND1', 'HIS', 'CD2', 'PHE', 13.47), ('ND1', 'HIS', 'CE1', 'PHE', 12.7), ('ND1', 'HIS', 'CE2', 'PHE', 14.33), ('ND1', 'HIS', 'CZ', 'PHE', 13.99)], [('CD2', 'HIS', 'CB', 'PHE', 9.72), ('CD2', 'HIS', 'CG', 'PHE', 10.44), ('CD2', 'HIS', 'CD1', 'PHE', 9.92), ('CD2', 'HIS', 'CD2', 'PHE', 11.82), ('CD2', 'HIS', 'CE1', 'PHE', 10.95), ('CD2', 'HIS', 'CE2', 'PHE', 12.65), ('CD2', 'HIS', 'CZ', 'PHE', 12.27)], [('CE1', 'HIS', 'CB', 'PHE', 10.26), ('CE1', 'HIS', 'CG', 'PHE', 11.15), ('CE1', 'HIS', 'CD1', 'PHE', 10.83), ('CE1', 'HIS', 'CD2', 'PHE', 12.47), ('CE1', 'HIS', 'CE1', 'PHE', 11.93), ('CE1', 'HIS', 'CE2', 'PHE', 13.4), ('CE1', 'HIS', 'CZ', 'PHE', 13.17)], [('NE2', 'HIS', 'CB', 'PHE', 9.18), ('NE2', 'HIS', 'CG', 'PHE', 10.05), ('NE2', 'HIS', 'CD1', 'PHE', 9.71), ('NE2', 'HIS', 'CD2', 'PHE', 11.4), ('NE2', 'HIS', 'CE1', 'PHE', 10.82), ('NE2', 'HIS', 'CE2', 'PHE', 12.32), ('NE2', 'HIS', 'CZ', 'PHE', 12.08)]]}
HIS_MET = { 
	'distances':
		[[13.39, 13.54, 14.54, 16.19, 15.0, 13.92, 12.9, 11.48], [11.91, 12.06, 13.14, 14.75, 13.5, 12.42, 11.38, 9.97], [11.56, 11.74, 12.98, 14.49, 12.82, 11.83, 10.84, 9.44], [10.87, 11.01, 11.97, 13.63, 12.7, 11.58, 10.49, 9.1], [10.23, 10.41, 11.7, 13.18, 11.52, 10.52, 9.5, 8.11], [9.73, 9.89, 11.0, 12.59, 11.42, 10.33, 9.24, 7.84]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'MET', 13.39), ('CB', 'HIS', 'CG', 'MET', 13.54), ('CB', 'HIS', 'SD', 'MET', 14.54), ('CB', 'HIS', 'CE', 'MET', 16.19), ('CB', 'HIS', 'O', 'MET', 15.0), ('CB', 'HIS', 'C', 'MET', 13.92), ('CB', 'HIS', 'CA', 'MET', 12.9), ('CB', 'HIS', 'N', 'MET', 11.48)], [('CG', 'HIS', 'CB', 'MET', 11.91), ('CG', 'HIS', 'CG', 'MET', 12.06), ('CG', 'HIS', 'SD', 'MET', 13.14), ('CG', 'HIS', 'CE', 'MET', 14.75), ('CG', 'HIS', 'O', 'MET', 13.5), ('CG', 'HIS', 'C', 'MET', 12.42), ('CG', 'HIS', 'CA', 'MET', 11.38), ('CG', 'HIS', 'N', 'MET', 9.97)], [('ND1', 'HIS', 'CB', 'MET', 11.56), ('ND1', 'HIS', 'CG', 'MET', 11.74), ('ND1', 'HIS', 'SD', 'MET', 12.98), ('ND1', 'HIS', 'CE', 'MET', 14.49), ('ND1', 'HIS', 'O', 'MET', 12.82), ('ND1', 'HIS', 'C', 'MET', 11.83), ('ND1', 'HIS', 'CA', 'MET', 10.84), ('ND1', 'HIS', 'N', 'MET', 9.44)], [('CD2', 'HIS', 'CB', 'MET', 10.87), ('CD2', 'HIS', 'CG', 'MET', 11.01), ('CD2', 'HIS', 'SD', 'MET', 11.97), ('CD2', 'HIS', 'CE', 'MET', 13.63), ('CD2', 'HIS', 'O', 'MET', 12.7), ('CD2', 'HIS', 'C', 'MET', 11.58), ('CD2', 'HIS', 'CA', 'MET', 10.49), ('CD2', 'HIS', 'N', 'MET', 9.1)], [('CE1', 'HIS', 'CB', 'MET', 10.23), ('CE1', 'HIS', 'CG', 'MET', 10.41), ('CE1', 'HIS', 'SD', 'MET', 11.7), ('CE1', 'HIS', 'CE', 'MET', 13.18), ('CE1', 'HIS', 'O', 'MET', 11.52), ('CE1', 'HIS', 'C', 'MET', 10.52), ('CE1', 'HIS', 'CA', 'MET', 9.5), ('CE1', 'HIS', 'N', 'MET', 8.11)], [('NE2', 'HIS', 'CB', 'MET', 9.73), ('NE2', 'HIS', 'CG', 'MET', 9.89), ('NE2', 'HIS', 'SD', 'MET', 11.0), ('NE2', 'HIS', 'CE', 'MET', 12.59), ('NE2', 'HIS', 'O', 'MET', 11.42), ('NE2', 'HIS', 'C', 'MET', 10.33), ('NE2', 'HIS', 'CA', 'MET', 9.24), ('NE2', 'HIS', 'N', 'MET', 7.84)]]}
ASP_PHE = { 
	'distances':
		[[15.93, 16.57, 15.94, 17.91, 16.76, 18.62, 18.09], [14.42, 15.08, 14.48, 16.41, 15.33, 17.15, 16.65], [13.81, 14.36, 13.67, 15.68, 14.44, 16.33, 15.76], [13.95, 14.74, 14.26, 16.07, 15.22, 16.9, 16.51]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'PHE', 15.93), ('CB', 'ASP', 'CG', 'PHE', 16.57), ('CB', 'ASP', 'CD1', 'PHE', 15.94), ('CB', 'ASP', 'CD2', 'PHE', 17.91), ('CB', 'ASP', 'CE1', 'PHE', 16.76), ('CB', 'ASP', 'CE2', 'PHE', 18.62), ('CB', 'ASP', 'CZ', 'PHE', 18.09)], [('CG', 'ASP', 'CB', 'PHE', 14.42), ('CG', 'ASP', 'CG', 'PHE', 15.08), ('CG', 'ASP', 'CD1', 'PHE', 14.48), ('CG', 'ASP', 'CD2', 'PHE', 16.41), ('CG', 'ASP', 'CE1', 'PHE', 15.33), ('CG', 'ASP', 'CE2', 'PHE', 17.15), ('CG', 'ASP', 'CZ', 'PHE', 16.65)], [('OD1', 'ASP', 'CB', 'PHE', 13.81), ('OD1', 'ASP', 'CG', 'PHE', 14.36), ('OD1', 'ASP', 'CD1', 'PHE', 13.67), ('OD1', 'ASP', 'CD2', 'PHE', 15.68), ('OD1', 'ASP', 'CE1', 'PHE', 14.44), ('OD1', 'ASP', 'CE2', 'PHE', 16.33), ('OD1', 'ASP', 'CZ', 'PHE', 15.76)], [('OD2', 'ASP', 'CB', 'PHE', 13.95), ('OD2', 'ASP', 'CG', 'PHE', 14.74), ('OD2', 'ASP', 'CD1', 'PHE', 14.26), ('OD2', 'ASP', 'CD2', 'PHE', 16.07), ('OD2', 'ASP', 'CE1', 'PHE', 15.22), ('OD2', 'ASP', 'CE2', 'PHE', 16.9), ('OD2', 'ASP', 'CZ', 'PHE', 16.51)]]}
ASP_SER = { 
	'distances':
		[[11.4, 10.96], [9.99, 9.47], [9.98, 9.28], [9.05, 8.67]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.4), ('CB', 'ASP', 'OG', 'SER', 10.96)], [('CG', 'ASP', 'CB', 'SER', 9.99), ('CG', 'ASP', 'OG', 'SER', 9.47)], [('OD1', 'ASP', 'CB', 'SER', 9.98), ('OD1', 'ASP', 'OG', 'SER', 9.28)], [('OD2', 'ASP', 'CB', 'SER', 9.05), ('OD2', 'ASP', 'OG', 'SER', 8.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_SER, d, 'A_1a7u_1_11_1_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(PHE_MET, d, 'A_1a7u_1_11_1_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_MET, d, 'A_1a7u_1_11_1_10')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_ASP, d, 'A_1a7u_1_11_1_10')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_MET, d, 'A_1a7u_1_11_1_10')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_PHE, d, 'A_1a7u_1_11_1_10')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_PHE, d, 'A_1a7u_1_11_1_10')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(HIS_MET, d, 'A_1a7u_1_11_1_10')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASP_PHE, d, 'A_1a7u_1_11_1_10')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASP_SER, d, 'A_1a7u_1_11_1_10')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_SER' :  match1,
		'PHE_MET' :  match2,
		'ASP_MET' :  match3,
		'HIS_ASP' :  match4,
		'SER_MET' :  match5,
		'SER_PHE' :  match6,
		'HIS_PHE' :  match7,
		'HIS_MET' :  match8,
		'ASP_PHE' :  match9,
		'ASP_SER' :  match10}