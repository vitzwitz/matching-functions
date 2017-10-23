'''
FUNC:A_1bwd_2_1_4_2
PDB:1bwd
EC:2.1.4.2
RESI:asp,arg,asp,his,asp,his,cys
LOCI:a-108,127,179,227,229,331,332;
'''
import motifFunctions as cmd
HIS_ASPII = { 
	'distances':
		[[15.12, 15.87, 17.07, 15.32], [14.54, 15.43, 16.63, 15.01], [13.34, 14.28, 15.48, 13.89], [15.17, 16.15, 17.33, 15.83], [13.3, 14.35, 15.54, 14.1], [14.42, 15.5, 16.67, 15.27]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPII', 15.12), ('CB', 'HIS', 'CG', 'ASPII', 15.87), ('CB', 'HIS', 'OD1', 'ASPII', 17.07), ('CB', 'HIS', 'OD2', 'ASPII', 15.32)], [('CG', 'HIS', 'CB', 'ASPII', 14.54), ('CG', 'HIS', 'CG', 'ASPII', 15.43), ('CG', 'HIS', 'OD1', 'ASPII', 16.63), ('CG', 'HIS', 'OD2', 'ASPII', 15.01)], [('ND1', 'HIS', 'CB', 'ASPII', 13.34), ('ND1', 'HIS', 'CG', 'ASPII', 14.28), ('ND1', 'HIS', 'OD1', 'ASPII', 15.48), ('ND1', 'HIS', 'OD2', 'ASPII', 13.89)], [('CD2', 'HIS', 'CB', 'ASPII', 15.17), ('CD2', 'HIS', 'CG', 'ASPII', 16.15), ('CD2', 'HIS', 'OD1', 'ASPII', 17.33), ('CD2', 'HIS', 'OD2', 'ASPII', 15.83)], [('CE1', 'HIS', 'CB', 'ASPII', 13.3), ('CE1', 'HIS', 'CG', 'ASPII', 14.35), ('CE1', 'HIS', 'OD1', 'ASPII', 15.54), ('CE1', 'HIS', 'OD2', 'ASPII', 14.1)], [('NE2', 'HIS', 'CB', 'ASPII', 14.42), ('NE2', 'HIS', 'CG', 'ASPII', 15.5), ('NE2', 'HIS', 'OD1', 'ASPII', 16.67), ('NE2', 'HIS', 'OD2', 'ASPII', 15.27)]]}
ARG_HISI = { 
	'distances':
		[[19.64, 19.48, 18.68, 20.17, 18.93, 19.82], [19.26, 19.21, 18.44, 20.0, 18.8, 19.73], [17.81, 17.79, 17.01, 18.6, 17.4, 18.36], [16.99, 16.96, 16.26, 17.73, 16.65, 17.52], [15.69, 15.71, 15.04, 16.5, 15.48, 16.35], [15.21, 15.27, 14.55, 16.15, 15.05, 16.0], [15.12, 15.13, 14.55, 15.87, 14.98, 15.76]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HISI', 19.64), ('CB', 'ARG', 'CG', 'HISI', 19.48), ('CB', 'ARG', 'ND1', 'HISI', 18.68), ('CB', 'ARG', 'CD2', 'HISI', 20.17), ('CB', 'ARG', 'CE1', 'HISI', 18.93), ('CB', 'ARG', 'NE2', 'HISI', 19.82)], [('CG', 'ARG', 'CB', 'HISI', 19.26), ('CG', 'ARG', 'CG', 'HISI', 19.21), ('CG', 'ARG', 'ND1', 'HISI', 18.44), ('CG', 'ARG', 'CD2', 'HISI', 20.0), ('CG', 'ARG', 'CE1', 'HISI', 18.8), ('CG', 'ARG', 'NE2', 'HISI', 19.73)], [('CD', 'ARG', 'CB', 'HISI', 17.81), ('CD', 'ARG', 'CG', 'HISI', 17.79), ('CD', 'ARG', 'ND1', 'HISI', 17.01), ('CD', 'ARG', 'CD2', 'HISI', 18.6), ('CD', 'ARG', 'CE1', 'HISI', 17.4), ('CD', 'ARG', 'NE2', 'HISI', 18.36)], [('NE', 'ARG', 'CB', 'HISI', 16.99), ('NE', 'ARG', 'CG', 'HISI', 16.96), ('NE', 'ARG', 'ND1', 'HISI', 16.26), ('NE', 'ARG', 'CD2', 'HISI', 17.73), ('NE', 'ARG', 'CE1', 'HISI', 16.65), ('NE', 'ARG', 'NE2', 'HISI', 17.52)], [('CZ', 'ARG', 'CB', 'HISI', 15.69), ('CZ', 'ARG', 'CG', 'HISI', 15.71), ('CZ', 'ARG', 'ND1', 'HISI', 15.04), ('CZ', 'ARG', 'CD2', 'HISI', 16.5), ('CZ', 'ARG', 'CE1', 'HISI', 15.48), ('CZ', 'ARG', 'NE2', 'HISI', 16.35)], [('NH1', 'ARG', 'CB', 'HISI', 15.21), ('NH1', 'ARG', 'CG', 'HISI', 15.27), ('NH1', 'ARG', 'ND1', 'HISI', 14.55), ('NH1', 'ARG', 'CD2', 'HISI', 16.15), ('NH1', 'ARG', 'CE1', 'HISI', 15.05), ('NH1', 'ARG', 'NE2', 'HISI', 16.0)], [('NH2', 'ARG', 'CB', 'HISI', 15.12), ('NH2', 'ARG', 'CG', 'HISI', 15.13), ('NH2', 'ARG', 'ND1', 'HISI', 14.55), ('NH2', 'ARG', 'CD2', 'HISI', 15.87), ('NH2', 'ARG', 'CE1', 'HISI', 14.98), ('NH2', 'ARG', 'NE2', 'HISI', 15.76)]]}
HIS_ASP = { 
	'distances':
		[[6.04, 6.7, 7.81, 6.41], [7.1, 7.41, 8.53, 6.79], [7.22, 7.25, 8.4, 6.37], [8.36, 8.59, 9.66, 7.94], [8.48, 8.36, 9.46, 7.38], [9.07, 9.08, 10.14, 8.22], [9.74, 9.01, 8.21, 9.5], [8.5, 7.82, 7.19, 8.25], [7.53, 6.65, 5.98, 7.0], [8.26, 7.82, 7.45, 8.22], [6.64, 5.87, 5.54, 6.11], [7.13, 6.7, 6.55, 6.99], [8.53, 8.89, 10.04, 8.16], [7.3, 7.52, 8.68, 6.72], [7.46, 7.55, 8.7, 6.62], [6.16, 6.31, 7.44, 5.58], [6.6, 6.48, 7.58, 5.47], [5.63, 5.5, 6.63, 4.57], [7.77, 6.68, 5.78, 7.09], [7.71, 6.53, 5.43, 7.03], [6.75, 5.53, 4.39, 6.08], [8.83, 7.67, 6.51, 8.18], [7.47, 6.34, 5.22, 6.89], [8.68, 7.55, 6.39, 8.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.04), ('CB', 'HIS', 'CG', 'ASP', 6.7), ('CB', 'HIS', 'OD1', 'ASP', 7.81), ('CB', 'HIS', 'OD2', 'ASP', 6.41)], [('CG', 'HIS', 'CB', 'ASP', 7.1), ('CG', 'HIS', 'CG', 'ASP', 7.41), ('CG', 'HIS', 'OD1', 'ASP', 8.53), ('CG', 'HIS', 'OD2', 'ASP', 6.79)], [('ND1', 'HIS', 'CB', 'ASP', 7.22), ('ND1', 'HIS', 'CG', 'ASP', 7.25), ('ND1', 'HIS', 'OD1', 'ASP', 8.4), ('ND1', 'HIS', 'OD2', 'ASP', 6.37)], [('CD2', 'HIS', 'CB', 'ASP', 8.36), ('CD2', 'HIS', 'CG', 'ASP', 8.59), ('CD2', 'HIS', 'OD1', 'ASP', 9.66), ('CD2', 'HIS', 'OD2', 'ASP', 7.94)], [('CE1', 'HIS', 'CB', 'ASP', 8.48), ('CE1', 'HIS', 'CG', 'ASP', 8.36), ('CE1', 'HIS', 'OD1', 'ASP', 9.46), ('CE1', 'HIS', 'OD2', 'ASP', 7.38)], [('NE2', 'HIS', 'CB', 'ASP', 9.07), ('NE2', 'HIS', 'CG', 'ASP', 9.08), ('NE2', 'HIS', 'OD1', 'ASP', 10.14), ('NE2', 'HIS', 'OD2', 'ASP', 8.22)], [('CB', 'HIS', 'CB', 'ASP', 9.74), ('CB', 'HIS', 'CG', 'ASP', 9.01), ('CB', 'HIS', 'OD1', 'ASP', 8.21), ('CB', 'HIS', 'OD2', 'ASP', 9.5)], [('CG', 'HIS', 'CB', 'ASP', 8.5), ('CG', 'HIS', 'CG', 'ASP', 7.82), ('CG', 'HIS', 'OD1', 'ASP', 7.19), ('CG', 'HIS', 'OD2', 'ASP', 8.25)], [('ND1', 'HIS', 'CB', 'ASP', 7.53), ('ND1', 'HIS', 'CG', 'ASP', 6.65), ('ND1', 'HIS', 'OD1', 'ASP', 5.98), ('ND1', 'HIS', 'OD2', 'ASP', 7.0)], [('CD2', 'HIS', 'CB', 'ASP', 8.26), ('CD2', 'HIS', 'CG', 'ASP', 7.82), ('CD2', 'HIS', 'OD1', 'ASP', 7.45), ('CD2', 'HIS', 'OD2', 'ASP', 8.22)], [('CE1', 'HIS', 'CB', 'ASP', 6.64), ('CE1', 'HIS', 'CG', 'ASP', 5.87), ('CE1', 'HIS', 'OD1', 'ASP', 5.54), ('CE1', 'HIS', 'OD2', 'ASP', 6.11)], [('NE2', 'HIS', 'CB', 'ASP', 7.13), ('NE2', 'HIS', 'CG', 'ASP', 6.7), ('NE2', 'HIS', 'OD1', 'ASP', 6.55), ('NE2', 'HIS', 'OD2', 'ASP', 6.99)], [('CB', 'HIS', 'CB', 'ASP', 8.53), ('CB', 'HIS', 'CG', 'ASP', 8.89), ('CB', 'HIS', 'OD1', 'ASP', 10.04), ('CB', 'HIS', 'OD2', 'ASP', 8.16)], [('CG', 'HIS', 'CB', 'ASP', 7.3), ('CG', 'HIS', 'CG', 'ASP', 7.52), ('CG', 'HIS', 'OD1', 'ASP', 8.68), ('CG', 'HIS', 'OD2', 'ASP', 6.72)], [('ND1', 'HIS', 'CB', 'ASP', 7.46), ('ND1', 'HIS', 'CG', 'ASP', 7.55), ('ND1', 'HIS', 'OD1', 'ASP', 8.7), ('ND1', 'HIS', 'OD2', 'ASP', 6.62)], [('CD2', 'HIS', 'CB', 'ASP', 6.16), ('CD2', 'HIS', 'CG', 'ASP', 6.31), ('CD2', 'HIS', 'OD1', 'ASP', 7.44), ('CD2', 'HIS', 'OD2', 'ASP', 5.58)], [('CE1', 'HIS', 'CB', 'ASP', 6.6), ('CE1', 'HIS', 'CG', 'ASP', 6.48), ('CE1', 'HIS', 'OD1', 'ASP', 7.58), ('CE1', 'HIS', 'OD2', 'ASP', 5.47)], [('NE2', 'HIS', 'CB', 'ASP', 5.63), ('NE2', 'HIS', 'CG', 'ASP', 5.5), ('NE2', 'HIS', 'OD1', 'ASP', 6.63), ('NE2', 'HIS', 'OD2', 'ASP', 4.57)], [('CB', 'HIS', 'CB', 'ASP', 7.77), ('CB', 'HIS', 'CG', 'ASP', 6.68), ('CB', 'HIS', 'OD1', 'ASP', 5.78), ('CB', 'HIS', 'OD2', 'ASP', 7.09)], [('CG', 'HIS', 'CB', 'ASP', 7.71), ('CG', 'HIS', 'CG', 'ASP', 6.53), ('CG', 'HIS', 'OD1', 'ASP', 5.43), ('CG', 'HIS', 'OD2', 'ASP', 7.03)], [('ND1', 'HIS', 'CB', 'ASP', 6.75), ('ND1', 'HIS', 'CG', 'ASP', 5.53), ('ND1', 'HIS', 'OD1', 'ASP', 4.39), ('ND1', 'HIS', 'OD2', 'ASP', 6.08)], [('CD2', 'HIS', 'CB', 'ASP', 8.83), ('CD2', 'HIS', 'CG', 'ASP', 7.67), ('CD2', 'HIS', 'OD1', 'ASP', 6.51), ('CD2', 'HIS', 'OD2', 'ASP', 8.18)], [('CE1', 'HIS', 'CB', 'ASP', 7.47), ('CE1', 'HIS', 'CG', 'ASP', 6.34), ('CE1', 'HIS', 'OD1', 'ASP', 5.22), ('CE1', 'HIS', 'OD2', 'ASP', 6.89)], [('NE2', 'HIS', 'CB', 'ASP', 8.68), ('NE2', 'HIS', 'CG', 'ASP', 7.55), ('NE2', 'HIS', 'OD1', 'ASP', 6.39), ('NE2', 'HIS', 'OD2', 'ASP', 8.08)]]}
ASP_ASPI = { 
	'distances':
		[[7.18, 7.78, 8.11, 8.33], [7.3, 7.76, 8.26, 8.02], [8.03, 8.59, 9.25, 8.73], [7.04, 7.18, 7.62, 7.3]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASPI', 7.18), ('CB', 'ASP', 'CG', 'ASPI', 7.78), ('CB', 'ASP', 'OD1', 'ASPI', 8.11), ('CB', 'ASP', 'OD2', 'ASPI', 8.33)], [('CG', 'ASP', 'CB', 'ASPI', 7.3), ('CG', 'ASP', 'CG', 'ASPI', 7.76), ('CG', 'ASP', 'OD1', 'ASPI', 8.26), ('CG', 'ASP', 'OD2', 'ASPI', 8.02)], [('OD1', 'ASP', 'CB', 'ASPI', 8.03), ('OD1', 'ASP', 'CG', 'ASPI', 8.59), ('OD1', 'ASP', 'OD1', 'ASPI', 9.25), ('OD1', 'ASP', 'OD2', 'ASPI', 8.73)], [('OD2', 'ASP', 'CB', 'ASPI', 7.04), ('OD2', 'ASP', 'CG', 'ASPI', 7.18), ('OD2', 'ASP', 'OD1', 'ASPI', 7.62), ('OD2', 'ASP', 'OD2', 'ASPI', 7.3)]]}
HIS_CYS = { 
	'distances':
		[[9.39, 7.61], [9.28, 7.42], [8.19, 6.34], [10.29, 8.44], [8.74, 6.96], [9.98, 8.19], [7.29, 8.07], [8.03, 8.5], [7.9, 7.98], [9.22, 9.71], [9.02, 8.96], [9.75, 9.94]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 9.39), ('CB', 'HIS', 'SG', 'CYS', 7.61)], [('CG', 'HIS', 'CB', 'CYS', 9.28), ('CG', 'HIS', 'SG', 'CYS', 7.42)], [('ND1', 'HIS', 'CB', 'CYS', 8.19), ('ND1', 'HIS', 'SG', 'CYS', 6.34)], [('CD2', 'HIS', 'CB', 'CYS', 10.29), ('CD2', 'HIS', 'SG', 'CYS', 8.44)], [('CE1', 'HIS', 'CB', 'CYS', 8.74), ('CE1', 'HIS', 'SG', 'CYS', 6.96)], [('NE2', 'HIS', 'CB', 'CYS', 9.98), ('NE2', 'HIS', 'SG', 'CYS', 8.19)], [('CB', 'HIS', 'CB', 'CYS', 7.29), ('CB', 'HIS', 'SG', 'CYS', 8.07)], [('CG', 'HIS', 'CB', 'CYS', 8.03), ('CG', 'HIS', 'SG', 'CYS', 8.5)], [('ND1', 'HIS', 'CB', 'CYS', 7.9), ('ND1', 'HIS', 'SG', 'CYS', 7.98)], [('CD2', 'HIS', 'CB', 'CYS', 9.22), ('CD2', 'HIS', 'SG', 'CYS', 9.71)], [('CE1', 'HIS', 'CB', 'CYS', 9.02), ('CE1', 'HIS', 'SG', 'CYS', 8.96)], [('NE2', 'HIS', 'CB', 'CYS', 9.75), ('NE2', 'HIS', 'SG', 'CYS', 9.94)]]}
HIS_ARG = { 
	'distances':
		[[14.97, 14.44, 13.04, 13.08, 12.18, 11.09, 12.57], [13.47, 12.94, 11.56, 11.63, 10.77, 9.68, 11.23], [12.73, 12.14, 10.69, 10.65, 9.69, 8.6, 10.08], [12.62, 12.18, 10.87, 11.07, 10.35, 9.29, 10.93], [11.42, 10.85, 9.41, 9.42, 8.53, 7.43, 9.03], [11.32, 10.85, 9.51, 9.68, 8.97, 7.91, 9.59], [19.64, 19.26, 17.81, 16.99, 15.69, 15.21, 15.12], [19.48, 19.21, 17.79, 16.96, 15.71, 15.27, 15.13], [18.68, 18.44, 17.01, 16.26, 15.04, 14.55, 14.55], [20.17, 20.0, 18.6, 17.73, 16.5, 16.15, 15.87], [18.93, 18.8, 17.4, 16.65, 15.48, 15.05, 14.98], [19.82, 19.73, 18.36, 17.52, 16.35, 16.0, 15.76]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 14.97), ('CB', 'HIS', 'CG', 'ARG', 14.44), ('CB', 'HIS', 'CD', 'ARG', 13.04), ('CB', 'HIS', 'NE', 'ARG', 13.08), ('CB', 'HIS', 'CZ', 'ARG', 12.18), ('CB', 'HIS', 'NH1', 'ARG', 11.09), ('CB', 'HIS', 'NH2', 'ARG', 12.57)], [('CG', 'HIS', 'CB', 'ARG', 13.47), ('CG', 'HIS', 'CG', 'ARG', 12.94), ('CG', 'HIS', 'CD', 'ARG', 11.56), ('CG', 'HIS', 'NE', 'ARG', 11.63), ('CG', 'HIS', 'CZ', 'ARG', 10.77), ('CG', 'HIS', 'NH1', 'ARG', 9.68), ('CG', 'HIS', 'NH2', 'ARG', 11.23)], [('ND1', 'HIS', 'CB', 'ARG', 12.73), ('ND1', 'HIS', 'CG', 'ARG', 12.14), ('ND1', 'HIS', 'CD', 'ARG', 10.69), ('ND1', 'HIS', 'NE', 'ARG', 10.65), ('ND1', 'HIS', 'CZ', 'ARG', 9.69), ('ND1', 'HIS', 'NH1', 'ARG', 8.6), ('ND1', 'HIS', 'NH2', 'ARG', 10.08)], [('CD2', 'HIS', 'CB', 'ARG', 12.62), ('CD2', 'HIS', 'CG', 'ARG', 12.18), ('CD2', 'HIS', 'CD', 'ARG', 10.87), ('CD2', 'HIS', 'NE', 'ARG', 11.07), ('CD2', 'HIS', 'CZ', 'ARG', 10.35), ('CD2', 'HIS', 'NH1', 'ARG', 9.29), ('CD2', 'HIS', 'NH2', 'ARG', 10.93)], [('CE1', 'HIS', 'CB', 'ARG', 11.42), ('CE1', 'HIS', 'CG', 'ARG', 10.85), ('CE1', 'HIS', 'CD', 'ARG', 9.41), ('CE1', 'HIS', 'NE', 'ARG', 9.42), ('CE1', 'HIS', 'CZ', 'ARG', 8.53), ('CE1', 'HIS', 'NH1', 'ARG', 7.43), ('CE1', 'HIS', 'NH2', 'ARG', 9.03)], [('NE2', 'HIS', 'CB', 'ARG', 11.32), ('NE2', 'HIS', 'CG', 'ARG', 10.85), ('NE2', 'HIS', 'CD', 'ARG', 9.51), ('NE2', 'HIS', 'NE', 'ARG', 9.68), ('NE2', 'HIS', 'CZ', 'ARG', 8.97), ('NE2', 'HIS', 'NH1', 'ARG', 7.91), ('NE2', 'HIS', 'NH2', 'ARG', 9.59)], [('CB', 'HIS', 'CB', 'ARG', 19.64), ('CB', 'HIS', 'CG', 'ARG', 19.26), ('CB', 'HIS', 'CD', 'ARG', 17.81), ('CB', 'HIS', 'NE', 'ARG', 16.99), ('CB', 'HIS', 'CZ', 'ARG', 15.69), ('CB', 'HIS', 'NH1', 'ARG', 15.21), ('CB', 'HIS', 'NH2', 'ARG', 15.12)], [('CG', 'HIS', 'CB', 'ARG', 19.48), ('CG', 'HIS', 'CG', 'ARG', 19.21), ('CG', 'HIS', 'CD', 'ARG', 17.79), ('CG', 'HIS', 'NE', 'ARG', 16.96), ('CG', 'HIS', 'CZ', 'ARG', 15.71), ('CG', 'HIS', 'NH1', 'ARG', 15.27), ('CG', 'HIS', 'NH2', 'ARG', 15.13)], [('ND1', 'HIS', 'CB', 'ARG', 18.68), ('ND1', 'HIS', 'CG', 'ARG', 18.44), ('ND1', 'HIS', 'CD', 'ARG', 17.01), ('ND1', 'HIS', 'NE', 'ARG', 16.26), ('ND1', 'HIS', 'CZ', 'ARG', 15.04), ('ND1', 'HIS', 'NH1', 'ARG', 14.55), ('ND1', 'HIS', 'NH2', 'ARG', 14.55)], [('CD2', 'HIS', 'CB', 'ARG', 20.17), ('CD2', 'HIS', 'CG', 'ARG', 20.0), ('CD2', 'HIS', 'CD', 'ARG', 18.6), ('CD2', 'HIS', 'NE', 'ARG', 17.73), ('CD2', 'HIS', 'CZ', 'ARG', 16.5), ('CD2', 'HIS', 'NH1', 'ARG', 16.15), ('CD2', 'HIS', 'NH2', 'ARG', 15.87)], [('CE1', 'HIS', 'CB', 'ARG', 18.93), ('CE1', 'HIS', 'CG', 'ARG', 18.8), ('CE1', 'HIS', 'CD', 'ARG', 17.4), ('CE1', 'HIS', 'NE', 'ARG', 16.65), ('CE1', 'HIS', 'CZ', 'ARG', 15.48), ('CE1', 'HIS', 'NH1', 'ARG', 15.05), ('CE1', 'HIS', 'NH2', 'ARG', 14.98)], [('NE2', 'HIS', 'CB', 'ARG', 19.82), ('NE2', 'HIS', 'CG', 'ARG', 19.73), ('NE2', 'HIS', 'CD', 'ARG', 18.36), ('NE2', 'HIS', 'NE', 'ARG', 17.52), ('NE2', 'HIS', 'CZ', 'ARG', 16.35), ('NE2', 'HIS', 'NH1', 'ARG', 16.0), ('NE2', 'HIS', 'NH2', 'ARG', 15.76)]]}
HIS_ASPI = { 
	'distances':
		[[12.64, 11.9, 10.72, 12.64], [12.38, 11.82, 10.66, 12.7], [11.58, 11.07, 9.9, 12.01], [13.06, 12.65, 11.54, 13.59], [11.84, 11.51, 10.41, 12.55], [12.73, 12.45, 11.38, 13.49]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 12.64), ('CB', 'HIS', 'CG', 'ASPI', 11.9), ('CB', 'HIS', 'OD1', 'ASPI', 10.72), ('CB', 'HIS', 'OD2', 'ASPI', 12.64)], [('CG', 'HIS', 'CB', 'ASPI', 12.38), ('CG', 'HIS', 'CG', 'ASPI', 11.82), ('CG', 'HIS', 'OD1', 'ASPI', 10.66), ('CG', 'HIS', 'OD2', 'ASPI', 12.7)], [('ND1', 'HIS', 'CB', 'ASPI', 11.58), ('ND1', 'HIS', 'CG', 'ASPI', 11.07), ('ND1', 'HIS', 'OD1', 'ASPI', 9.9), ('ND1', 'HIS', 'OD2', 'ASPI', 12.01)], [('CD2', 'HIS', 'CB', 'ASPI', 13.06), ('CD2', 'HIS', 'CG', 'ASPI', 12.65), ('CD2', 'HIS', 'OD1', 'ASPI', 11.54), ('CD2', 'HIS', 'OD2', 'ASPI', 13.59)], [('CE1', 'HIS', 'CB', 'ASPI', 11.84), ('CE1', 'HIS', 'CG', 'ASPI', 11.51), ('CE1', 'HIS', 'OD1', 'ASPI', 10.41), ('CE1', 'HIS', 'OD2', 'ASPI', 12.55)], [('NE2', 'HIS', 'CB', 'ASPI', 12.73), ('NE2', 'HIS', 'CG', 'ASPI', 12.45), ('NE2', 'HIS', 'OD1', 'ASPI', 11.38), ('NE2', 'HIS', 'OD2', 'ASPI', 13.49)]]}
ARG_ASPII = { 
	'distances':
		[[10.15, 9.18, 8.54, 9.28], [10.28, 9.16, 8.63, 9.01], [9.29, 8.2, 7.89, 7.89], [9.46, 8.61, 8.49, 8.33], [9.16, 8.45, 8.58, 8.02], [8.62, 7.81, 8.06, 7.17], [9.75, 9.25, 9.48, 8.89]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASPII', 10.15), ('CB', 'ARG', 'CG', 'ASPII', 9.18), ('CB', 'ARG', 'OD1', 'ASPII', 8.54), ('CB', 'ARG', 'OD2', 'ASPII', 9.28)], [('CG', 'ARG', 'CB', 'ASPII', 10.28), ('CG', 'ARG', 'CG', 'ASPII', 9.16), ('CG', 'ARG', 'OD1', 'ASPII', 8.63), ('CG', 'ARG', 'OD2', 'ASPII', 9.01)], [('CD', 'ARG', 'CB', 'ASPII', 9.29), ('CD', 'ARG', 'CG', 'ASPII', 8.2), ('CD', 'ARG', 'OD1', 'ASPII', 7.89), ('CD', 'ARG', 'OD2', 'ASPII', 7.89)], [('NE', 'ARG', 'CB', 'ASPII', 9.46), ('NE', 'ARG', 'CG', 'ASPII', 8.61), ('NE', 'ARG', 'OD1', 'ASPII', 8.49), ('NE', 'ARG', 'OD2', 'ASPII', 8.33)], [('CZ', 'ARG', 'CB', 'ASPII', 9.16), ('CZ', 'ARG', 'CG', 'ASPII', 8.45), ('CZ', 'ARG', 'OD1', 'ASPII', 8.58), ('CZ', 'ARG', 'OD2', 'ASPII', 8.02)], [('NH1', 'ARG', 'CB', 'ASPII', 8.62), ('NH1', 'ARG', 'CG', 'ASPII', 7.81), ('NH1', 'ARG', 'OD1', 'ASPII', 8.06), ('NH1', 'ARG', 'OD2', 'ASPII', 7.17)], [('NH2', 'ARG', 'CB', 'ASPII', 9.75), ('NH2', 'ARG', 'CG', 'ASPII', 9.25), ('NH2', 'ARG', 'OD1', 'ASPII', 9.48), ('NH2', 'ARG', 'OD2', 'ASPII', 8.89)]]}
HIS_HIS = { 
	'distances':
		[[11.35, 11.15, 9.99, 12.16, 10.42, 11.73], [11.88, 11.68, 10.53, 12.68, 10.94, 12.24], [11.4, 11.32, 10.28, 12.37, 10.81, 12.06], [13.0, 12.71, 11.52, 13.64, 11.82, 13.11], [12.28, 12.17, 11.14, 13.17, 11.62, 12.83], [13.2, 12.97, 11.85, 13.9, 12.19, 13.43], [11.35, 11.88, 11.4, 13.0, 12.28, 13.2], [11.15, 11.68, 11.32, 12.71, 12.17, 12.97], [9.99, 10.53, 10.28, 11.52, 11.14, 11.85], [12.16, 12.68, 12.37, 13.64, 13.17, 13.9], [10.42, 10.94, 10.81, 11.82, 11.62, 12.19], [11.73, 12.24, 12.06, 13.11, 12.83, 13.43]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 11.35), ('CB', 'HIS', 'CG', 'HIS', 11.15), ('CB', 'HIS', 'ND1', 'HIS', 9.99), ('CB', 'HIS', 'CD2', 'HIS', 12.16), ('CB', 'HIS', 'CE1', 'HIS', 10.42), ('CB', 'HIS', 'NE2', 'HIS', 11.73)], [('CG', 'HIS', 'CB', 'HIS', 11.88), ('CG', 'HIS', 'CG', 'HIS', 11.68), ('CG', 'HIS', 'ND1', 'HIS', 10.53), ('CG', 'HIS', 'CD2', 'HIS', 12.68), ('CG', 'HIS', 'CE1', 'HIS', 10.94), ('CG', 'HIS', 'NE2', 'HIS', 12.24)], [('ND1', 'HIS', 'CB', 'HIS', 11.4), ('ND1', 'HIS', 'CG', 'HIS', 11.32), ('ND1', 'HIS', 'ND1', 'HIS', 10.28), ('ND1', 'HIS', 'CD2', 'HIS', 12.37), ('ND1', 'HIS', 'CE1', 'HIS', 10.81), ('ND1', 'HIS', 'NE2', 'HIS', 12.06)], [('CD2', 'HIS', 'CB', 'HIS', 13.0), ('CD2', 'HIS', 'CG', 'HIS', 12.71), ('CD2', 'HIS', 'ND1', 'HIS', 11.52), ('CD2', 'HIS', 'CD2', 'HIS', 13.64), ('CD2', 'HIS', 'CE1', 'HIS', 11.82), ('CD2', 'HIS', 'NE2', 'HIS', 13.11)], [('CE1', 'HIS', 'CB', 'HIS', 12.28), ('CE1', 'HIS', 'CG', 'HIS', 12.17), ('CE1', 'HIS', 'ND1', 'HIS', 11.14), ('CE1', 'HIS', 'CD2', 'HIS', 13.17), ('CE1', 'HIS', 'CE1', 'HIS', 11.62), ('CE1', 'HIS', 'NE2', 'HIS', 12.83)], [('NE2', 'HIS', 'CB', 'HIS', 13.2), ('NE2', 'HIS', 'CG', 'HIS', 12.97), ('NE2', 'HIS', 'ND1', 'HIS', 11.85), ('NE2', 'HIS', 'CD2', 'HIS', 13.9), ('NE2', 'HIS', 'CE1', 'HIS', 12.19), ('NE2', 'HIS', 'NE2', 'HIS', 13.43)], [('CB', 'HIS', 'CB', 'HIS', 11.35), ('CB', 'HIS', 'CG', 'HIS', 11.88), ('CB', 'HIS', 'ND1', 'HIS', 11.4), ('CB', 'HIS', 'CD2', 'HIS', 13.0), ('CB', 'HIS', 'CE1', 'HIS', 12.28), ('CB', 'HIS', 'NE2', 'HIS', 13.2)], [('CG', 'HIS', 'CB', 'HIS', 11.15), ('CG', 'HIS', 'CG', 'HIS', 11.68), ('CG', 'HIS', 'ND1', 'HIS', 11.32), ('CG', 'HIS', 'CD2', 'HIS', 12.71), ('CG', 'HIS', 'CE1', 'HIS', 12.17), ('CG', 'HIS', 'NE2', 'HIS', 12.97)], [('ND1', 'HIS', 'CB', 'HIS', 9.99), ('ND1', 'HIS', 'CG', 'HIS', 10.53), ('ND1', 'HIS', 'ND1', 'HIS', 10.28), ('ND1', 'HIS', 'CD2', 'HIS', 11.52), ('ND1', 'HIS', 'CE1', 'HIS', 11.14), ('ND1', 'HIS', 'NE2', 'HIS', 11.85)], [('CD2', 'HIS', 'CB', 'HIS', 12.16), ('CD2', 'HIS', 'CG', 'HIS', 12.68), ('CD2', 'HIS', 'ND1', 'HIS', 12.37), ('CD2', 'HIS', 'CD2', 'HIS', 13.64), ('CD2', 'HIS', 'CE1', 'HIS', 13.17), ('CD2', 'HIS', 'NE2', 'HIS', 13.9)], [('CE1', 'HIS', 'CB', 'HIS', 10.42), ('CE1', 'HIS', 'CG', 'HIS', 10.94), ('CE1', 'HIS', 'ND1', 'HIS', 10.81), ('CE1', 'HIS', 'CD2', 'HIS', 11.82), ('CE1', 'HIS', 'CE1', 'HIS', 11.62), ('CE1', 'HIS', 'NE2', 'HIS', 12.19)], [('NE2', 'HIS', 'CB', 'HIS', 11.73), ('NE2', 'HIS', 'CG', 'HIS', 12.24), ('NE2', 'HIS', 'ND1', 'HIS', 12.06), ('NE2', 'HIS', 'CD2', 'HIS', 13.11), ('NE2', 'HIS', 'CE1', 'HIS', 12.83), ('NE2', 'HIS', 'NE2', 'HIS', 13.43)]]}
ASP_CYS = { 
	'distances':
		[[7.73, 6.69], [6.76, 5.89], [7.21, 6.71], [5.93, 4.8], [9.15, 8.17], [7.94, 6.91], [6.87, 5.75], [8.22, 7.26], [12.5, 10.88], [12.74, 11.1], [13.82, 12.22], [11.91, 10.25]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 7.73), ('CB', 'ASP', 'SG', 'CYS', 6.69)], [('CG', 'ASP', 'CB', 'CYS', 6.76), ('CG', 'ASP', 'SG', 'CYS', 5.89)], [('OD1', 'ASP', 'CB', 'CYS', 7.21), ('OD1', 'ASP', 'SG', 'CYS', 6.71)], [('OD2', 'ASP', 'CB', 'CYS', 5.93), ('OD2', 'ASP', 'SG', 'CYS', 4.8)], [('CB', 'ASP', 'CB', 'CYS', 9.15), ('CB', 'ASP', 'SG', 'CYS', 8.17)], [('CG', 'ASP', 'CB', 'CYS', 7.94), ('CG', 'ASP', 'SG', 'CYS', 6.91)], [('OD1', 'ASP', 'CB', 'CYS', 6.87), ('OD1', 'ASP', 'SG', 'CYS', 5.75)], [('OD2', 'ASP', 'CB', 'CYS', 8.22), ('OD2', 'ASP', 'SG', 'CYS', 7.26)], [('CB', 'ASP', 'CB', 'CYS', 12.5), ('CB', 'ASP', 'SG', 'CYS', 10.88)], [('CG', 'ASP', 'CB', 'CYS', 12.74), ('CG', 'ASP', 'SG', 'CYS', 11.1)], [('OD1', 'ASP', 'CB', 'CYS', 13.82), ('OD1', 'ASP', 'SG', 'CYS', 12.22)], [('OD2', 'ASP', 'CB', 'CYS', 11.91), ('OD2', 'ASP', 'SG', 'CYS', 10.25)]]}
ASP_ARG = { 
	'distances':
		[[17.6, 17.09, 15.6, 15.28, 14.13, 13.22, 14.12], [17.03, 16.58, 15.1, 14.63, 13.43, 12.64, 13.28], [17.86, 17.48, 16.01, 15.45, 14.25, 13.54, 13.99], [15.86, 15.4, 13.91, 13.41, 12.21, 11.43, 12.05], [9.12, 9.02, 7.72, 6.89, 5.89, 5.79, 5.64], [9.78, 9.4, 7.97, 7.23, 6.02, 5.55, 5.86], [11.02, 10.6, 9.15, 8.46, 7.24, 6.66, 7.03], [9.23, 8.65, 7.19, 6.49, 5.22, 4.58, 5.23], [10.15, 10.28, 9.29, 9.46, 9.16, 8.62, 9.75], [9.18, 9.16, 8.2, 8.61, 8.45, 7.81, 9.25], [8.54, 8.63, 7.89, 8.49, 8.58, 8.06, 9.48], [9.28, 9.01, 7.89, 8.33, 8.02, 7.17, 8.89]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 17.6), ('CB', 'ASP', 'CG', 'ARG', 17.09), ('CB', 'ASP', 'CD', 'ARG', 15.6), ('CB', 'ASP', 'NE', 'ARG', 15.28), ('CB', 'ASP', 'CZ', 'ARG', 14.13), ('CB', 'ASP', 'NH1', 'ARG', 13.22), ('CB', 'ASP', 'NH2', 'ARG', 14.12)], [('CG', 'ASP', 'CB', 'ARG', 17.03), ('CG', 'ASP', 'CG', 'ARG', 16.58), ('CG', 'ASP', 'CD', 'ARG', 15.1), ('CG', 'ASP', 'NE', 'ARG', 14.63), ('CG', 'ASP', 'CZ', 'ARG', 13.43), ('CG', 'ASP', 'NH1', 'ARG', 12.64), ('CG', 'ASP', 'NH2', 'ARG', 13.28)], [('OD1', 'ASP', 'CB', 'ARG', 17.86), ('OD1', 'ASP', 'CG', 'ARG', 17.48), ('OD1', 'ASP', 'CD', 'ARG', 16.01), ('OD1', 'ASP', 'NE', 'ARG', 15.45), ('OD1', 'ASP', 'CZ', 'ARG', 14.25), ('OD1', 'ASP', 'NH1', 'ARG', 13.54), ('OD1', 'ASP', 'NH2', 'ARG', 13.99)], [('OD2', 'ASP', 'CB', 'ARG', 15.86), ('OD2', 'ASP', 'CG', 'ARG', 15.4), ('OD2', 'ASP', 'CD', 'ARG', 13.91), ('OD2', 'ASP', 'NE', 'ARG', 13.41), ('OD2', 'ASP', 'CZ', 'ARG', 12.21), ('OD2', 'ASP', 'NH1', 'ARG', 11.43), ('OD2', 'ASP', 'NH2', 'ARG', 12.05)], [('CB', 'ASP', 'CB', 'ARG', 9.12), ('CB', 'ASP', 'CG', 'ARG', 9.02), ('CB', 'ASP', 'CD', 'ARG', 7.72), ('CB', 'ASP', 'NE', 'ARG', 6.89), ('CB', 'ASP', 'CZ', 'ARG', 5.89), ('CB', 'ASP', 'NH1', 'ARG', 5.79), ('CB', 'ASP', 'NH2', 'ARG', 5.64)], [('CG', 'ASP', 'CB', 'ARG', 9.78), ('CG', 'ASP', 'CG', 'ARG', 9.4), ('CG', 'ASP', 'CD', 'ARG', 7.97), ('CG', 'ASP', 'NE', 'ARG', 7.23), ('CG', 'ASP', 'CZ', 'ARG', 6.02), ('CG', 'ASP', 'NH1', 'ARG', 5.55), ('CG', 'ASP', 'NH2', 'ARG', 5.86)], [('OD1', 'ASP', 'CB', 'ARG', 11.02), ('OD1', 'ASP', 'CG', 'ARG', 10.6), ('OD1', 'ASP', 'CD', 'ARG', 9.15), ('OD1', 'ASP', 'NE', 'ARG', 8.46), ('OD1', 'ASP', 'CZ', 'ARG', 7.24), ('OD1', 'ASP', 'NH1', 'ARG', 6.66), ('OD1', 'ASP', 'NH2', 'ARG', 7.03)], [('OD2', 'ASP', 'CB', 'ARG', 9.23), ('OD2', 'ASP', 'CG', 'ARG', 8.65), ('OD2', 'ASP', 'CD', 'ARG', 7.19), ('OD2', 'ASP', 'NE', 'ARG', 6.49), ('OD2', 'ASP', 'CZ', 'ARG', 5.22), ('OD2', 'ASP', 'NH1', 'ARG', 4.58), ('OD2', 'ASP', 'NH2', 'ARG', 5.23)], [('CB', 'ASP', 'CB', 'ARG', 10.15), ('CB', 'ASP', 'CG', 'ARG', 10.28), ('CB', 'ASP', 'CD', 'ARG', 9.29), ('CB', 'ASP', 'NE', 'ARG', 9.46), ('CB', 'ASP', 'CZ', 'ARG', 9.16), ('CB', 'ASP', 'NH1', 'ARG', 8.62), ('CB', 'ASP', 'NH2', 'ARG', 9.75)], [('CG', 'ASP', 'CB', 'ARG', 9.18), ('CG', 'ASP', 'CG', 'ARG', 9.16), ('CG', 'ASP', 'CD', 'ARG', 8.2), ('CG', 'ASP', 'NE', 'ARG', 8.61), ('CG', 'ASP', 'CZ', 'ARG', 8.45), ('CG', 'ASP', 'NH1', 'ARG', 7.81), ('CG', 'ASP', 'NH2', 'ARG', 9.25)], [('OD1', 'ASP', 'CB', 'ARG', 8.54), ('OD1', 'ASP', 'CG', 'ARG', 8.63), ('OD1', 'ASP', 'CD', 'ARG', 7.89), ('OD1', 'ASP', 'NE', 'ARG', 8.49), ('OD1', 'ASP', 'CZ', 'ARG', 8.58), ('OD1', 'ASP', 'NH1', 'ARG', 8.06), ('OD1', 'ASP', 'NH2', 'ARG', 9.48)], [('OD2', 'ASP', 'CB', 'ARG', 9.28), ('OD2', 'ASP', 'CG', 'ARG', 9.01), ('OD2', 'ASP', 'CD', 'ARG', 7.89), ('OD2', 'ASP', 'NE', 'ARG', 8.33), ('OD2', 'ASP', 'CZ', 'ARG', 8.02), ('OD2', 'ASP', 'NH1', 'ARG', 7.17), ('OD2', 'ASP', 'NH2', 'ARG', 8.89)]]}
ARG_ASPI = { 
	'distances':
		[[9.12, 9.78, 11.02, 9.23], [9.02, 9.4, 10.6, 8.65], [7.72, 7.97, 9.15, 7.19], [6.89, 7.23, 8.46, 6.49], [5.89, 6.02, 7.24, 5.22], [5.79, 5.55, 6.66, 4.58], [5.64, 5.86, 7.03, 5.23]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASPI', 9.12), ('CB', 'ARG', 'CG', 'ASPI', 9.78), ('CB', 'ARG', 'OD1', 'ASPI', 11.02), ('CB', 'ARG', 'OD2', 'ASPI', 9.23)], [('CG', 'ARG', 'CB', 'ASPI', 9.02), ('CG', 'ARG', 'CG', 'ASPI', 9.4), ('CG', 'ARG', 'OD1', 'ASPI', 10.6), ('CG', 'ARG', 'OD2', 'ASPI', 8.65)], [('CD', 'ARG', 'CB', 'ASPI', 7.72), ('CD', 'ARG', 'CG', 'ASPI', 7.97), ('CD', 'ARG', 'OD1', 'ASPI', 9.15), ('CD', 'ARG', 'OD2', 'ASPI', 7.19)], [('NE', 'ARG', 'CB', 'ASPI', 6.89), ('NE', 'ARG', 'CG', 'ASPI', 7.23), ('NE', 'ARG', 'OD1', 'ASPI', 8.46), ('NE', 'ARG', 'OD2', 'ASPI', 6.49)], [('CZ', 'ARG', 'CB', 'ASPI', 5.89), ('CZ', 'ARG', 'CG', 'ASPI', 6.02), ('CZ', 'ARG', 'OD1', 'ASPI', 7.24), ('CZ', 'ARG', 'OD2', 'ASPI', 5.22)], [('NH1', 'ARG', 'CB', 'ASPI', 5.79), ('NH1', 'ARG', 'CG', 'ASPI', 5.55), ('NH1', 'ARG', 'OD1', 'ASPI', 6.66), ('NH1', 'ARG', 'OD2', 'ASPI', 4.58)], [('NH2', 'ARG', 'CB', 'ASPI', 5.64), ('NH2', 'ARG', 'CG', 'ASPI', 5.86), ('NH2', 'ARG', 'OD1', 'ASPI', 7.03), ('NH2', 'ARG', 'OD2', 'ASPI', 5.23)]]}
CYS_ARG = { 
	'distances':
		[[15.42, 14.76, 13.3, 12.56, 11.23, 10.62, 10.8], [14.47, 13.81, 12.32, 11.74, 10.45, 9.67, 10.24]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 15.42), ('CB', 'CYS', 'CG', 'ARG', 14.76), ('CB', 'CYS', 'CD', 'ARG', 13.3), ('CB', 'CYS', 'NE', 'ARG', 12.56), ('CB', 'CYS', 'CZ', 'ARG', 11.23), ('CB', 'CYS', 'NH1', 'ARG', 10.62), ('CB', 'CYS', 'NH2', 'ARG', 10.8)], [('SG', 'CYS', 'CB', 'ARG', 14.47), ('SG', 'CYS', 'CG', 'ARG', 13.81), ('SG', 'CYS', 'CD', 'ARG', 12.32), ('SG', 'CYS', 'NE', 'ARG', 11.74), ('SG', 'CYS', 'CZ', 'ARG', 10.45), ('SG', 'CYS', 'NH1', 'ARG', 9.67), ('SG', 'CYS', 'NH2', 'ARG', 10.24)]]}
ASP_ASP = { 
	'distances':
		[[11.19, 10.32, 9.13, 10.98], [10.31, 9.5, 8.26, 10.25], [10.97, 10.25, 9.02, 11.08], [9.16, 8.28, 7.04, 9.01], [11.61, 12.23, 13.46, 11.56], [11.36, 12.05, 13.29, 11.44], [12.15, 12.95, 14.18, 12.42], [10.57, 11.18, 12.4, 10.53], [11.19, 10.31, 10.97, 9.16], [10.32, 9.5, 10.25, 8.28], [9.13, 8.26, 9.02, 7.04], [10.98, 10.25, 11.08, 9.01], [7.18, 7.3, 8.03, 7.04], [7.78, 7.76, 8.59, 7.18], [8.11, 8.26, 9.25, 7.62], [8.33, 8.02, 8.73, 7.3], [11.61, 11.36, 12.15, 10.57], [12.23, 12.05, 12.95, 11.18], [13.46, 13.29, 14.18, 12.4], [11.56, 11.44, 12.42, 10.53]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.19), ('CB', 'ASP', 'CG', 'ASP', 10.32), ('CB', 'ASP', 'OD1', 'ASP', 9.13), ('CB', 'ASP', 'OD2', 'ASP', 10.98)], [('CG', 'ASP', 'CB', 'ASP', 10.31), ('CG', 'ASP', 'CG', 'ASP', 9.5), ('CG', 'ASP', 'OD1', 'ASP', 8.26), ('CG', 'ASP', 'OD2', 'ASP', 10.25)], [('OD1', 'ASP', 'CB', 'ASP', 10.97), ('OD1', 'ASP', 'CG', 'ASP', 10.25), ('OD1', 'ASP', 'OD1', 'ASP', 9.02), ('OD1', 'ASP', 'OD2', 'ASP', 11.08)], [('OD2', 'ASP', 'CB', 'ASP', 9.16), ('OD2', 'ASP', 'CG', 'ASP', 8.28), ('OD2', 'ASP', 'OD1', 'ASP', 7.04), ('OD2', 'ASP', 'OD2', 'ASP', 9.01)], [('CB', 'ASP', 'CB', 'ASP', 11.61), ('CB', 'ASP', 'CG', 'ASP', 12.23), ('CB', 'ASP', 'OD1', 'ASP', 13.46), ('CB', 'ASP', 'OD2', 'ASP', 11.56)], [('CG', 'ASP', 'CB', 'ASP', 11.36), ('CG', 'ASP', 'CG', 'ASP', 12.05), ('CG', 'ASP', 'OD1', 'ASP', 13.29), ('CG', 'ASP', 'OD2', 'ASP', 11.44)], [('OD1', 'ASP', 'CB', 'ASP', 12.15), ('OD1', 'ASP', 'CG', 'ASP', 12.95), ('OD1', 'ASP', 'OD1', 'ASP', 14.18), ('OD1', 'ASP', 'OD2', 'ASP', 12.42)], [('OD2', 'ASP', 'CB', 'ASP', 10.57), ('OD2', 'ASP', 'CG', 'ASP', 11.18), ('OD2', 'ASP', 'OD1', 'ASP', 12.4), ('OD2', 'ASP', 'OD2', 'ASP', 10.53)], [('CB', 'ASP', 'CB', 'ASP', 11.19), ('CB', 'ASP', 'CG', 'ASP', 10.31), ('CB', 'ASP', 'OD1', 'ASP', 10.97), ('CB', 'ASP', 'OD2', 'ASP', 9.16)], [('CG', 'ASP', 'CB', 'ASP', 10.32), ('CG', 'ASP', 'CG', 'ASP', 9.5), ('CG', 'ASP', 'OD1', 'ASP', 10.25), ('CG', 'ASP', 'OD2', 'ASP', 8.28)], [('OD1', 'ASP', 'CB', 'ASP', 9.13), ('OD1', 'ASP', 'CG', 'ASP', 8.26), ('OD1', 'ASP', 'OD1', 'ASP', 9.02), ('OD1', 'ASP', 'OD2', 'ASP', 7.04)], [('OD2', 'ASP', 'CB', 'ASP', 10.98), ('OD2', 'ASP', 'CG', 'ASP', 10.25), ('OD2', 'ASP', 'OD1', 'ASP', 11.08), ('OD2', 'ASP', 'OD2', 'ASP', 9.01)], [('CB', 'ASP', 'CB', 'ASP', 7.18), ('CB', 'ASP', 'CG', 'ASP', 7.3), ('CB', 'ASP', 'OD1', 'ASP', 8.03), ('CB', 'ASP', 'OD2', 'ASP', 7.04)], [('CG', 'ASP', 'CB', 'ASP', 7.78), ('CG', 'ASP', 'CG', 'ASP', 7.76), ('CG', 'ASP', 'OD1', 'ASP', 8.59), ('CG', 'ASP', 'OD2', 'ASP', 7.18)], [('OD1', 'ASP', 'CB', 'ASP', 8.11), ('OD1', 'ASP', 'CG', 'ASP', 8.26), ('OD1', 'ASP', 'OD1', 'ASP', 9.25), ('OD1', 'ASP', 'OD2', 'ASP', 7.62)], [('OD2', 'ASP', 'CB', 'ASP', 8.33), ('OD2', 'ASP', 'CG', 'ASP', 8.02), ('OD2', 'ASP', 'OD1', 'ASP', 8.73), ('OD2', 'ASP', 'OD2', 'ASP', 7.3)], [('CB', 'ASP', 'CB', 'ASP', 11.61), ('CB', 'ASP', 'CG', 'ASP', 11.36), ('CB', 'ASP', 'OD1', 'ASP', 12.15), ('CB', 'ASP', 'OD2', 'ASP', 10.57)], [('CG', 'ASP', 'CB', 'ASP', 12.23), ('CG', 'ASP', 'CG', 'ASP', 12.05), ('CG', 'ASP', 'OD1', 'ASP', 12.95), ('CG', 'ASP', 'OD2', 'ASP', 11.18)], [('OD1', 'ASP', 'CB', 'ASP', 13.46), ('OD1', 'ASP', 'CG', 'ASP', 13.29), ('OD1', 'ASP', 'OD1', 'ASP', 14.18), ('OD1', 'ASP', 'OD2', 'ASP', 12.4)], [('OD2', 'ASP', 'CB', 'ASP', 11.56), ('OD2', 'ASP', 'CG', 'ASP', 11.44), ('OD2', 'ASP', 'OD1', 'ASP', 12.42), ('OD2', 'ASP', 'OD2', 'ASP', 10.53)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASPII, d, 'A_1bwd_2_1_4_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_HISI, d, 'A_1bwd_2_1_4_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'A_1bwd_2_1_4_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ASPI, d, 'A_1bwd_2_1_4_2')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_CYS, d, 'A_1bwd_2_1_4_2')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_ARG, d, 'A_1bwd_2_1_4_2')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_ASPI, d, 'A_1bwd_2_1_4_2')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ARG_ASPII, d, 'A_1bwd_2_1_4_2')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_HIS, d, 'A_1bwd_2_1_4_2')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASP_CYS, d, 'A_1bwd_2_1_4_2')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ASP_ARG, d, 'A_1bwd_2_1_4_2')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(ARG_ASPI, d, 'A_1bwd_2_1_4_2')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(CYS_ARG, d, 'A_1bwd_2_1_4_2')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(ASP_ASP, d, 'A_1bwd_2_1_4_2')
	if match14 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASPII' :  match1,
		'ARG_HISI' :  match2,
		'HIS_ASP' :  match3,
		'ASP_ASPI' :  match4,
		'HIS_CYS' :  match5,
		'HIS_ARG' :  match6,
		'HIS_ASPI' :  match7,
		'ARG_ASPII' :  match8,
		'HIS_HIS' :  match9,
		'ASP_CYS' :  match10,
		'ASP_ARG' :  match11,
		'ARG_ASPI' :  match12,
		'CYS_ARG' :  match13,
		'ASP_ASP' :  match14}