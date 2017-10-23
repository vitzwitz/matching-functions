'''
FUNC:M_1hdh_3_1_6_1
PDB:1hdh
EC:3.1.6.1
RESI:arg,lys,his,his,asp,lys,ca
LOCI:a-55,113,115,211,317,375,1528;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[11.93, 11.27, 11.85, 10.35, 11.36, 10.41], [11.29, 10.48, 11.01, 9.44, 10.39, 9.37], [9.9, 9.06, 9.55, 8.06, 8.96, 7.99], [9.41, 8.38, 8.78, 7.25, 8.01, 6.96], [8.28, 7.15, 7.4, 6.11, 6.62, 5.69], [16.03, 15.19, 13.81, 15.67, 13.51, 14.67], [14.71, 13.81, 12.42, 14.24, 12.07, 13.21], [14.07, 13.17, 11.8, 13.6, 11.44, 12.58], [12.79, 11.81, 10.45, 12.17, 10.01, 11.12], [12.65, 11.66, 10.35, 11.96, 9.89, 10.92], [10.18, 10.35, 10.97, 10.3, 11.24, 10.88], [9.94, 9.84, 10.34, 9.63, 10.42, 10.02], [8.52, 8.35, 8.91, 8.11, 8.98, 8.54], [8.75, 8.4, 9.05, 7.84, 8.92, 8.22], [7.7, 7.16, 7.85, 6.46, 7.63, 6.81], [7.66, 8.53, 8.85, 9.48, 9.87, 10.22], [6.39, 7.11, 7.46, 8.01, 8.42, 8.72], [6.7, 7.04, 7.0, 7.94, 7.84, 8.35], [5.91, 6.12, 5.83, 7.18, 6.77, 7.49], [6.81, 6.59, 5.87, 7.51, 6.52, 7.44]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 11.93), ('CB', 'LYS', 'CG', 'HIS', 11.27), ('CB', 'LYS', 'ND1', 'HIS', 11.85), ('CB', 'LYS', 'CD2', 'HIS', 10.35), ('CB', 'LYS', 'CE1', 'HIS', 11.36), ('CB', 'LYS', 'NE2', 'HIS', 10.41)], [('CG', 'LYS', 'CB', 'HIS', 11.29), ('CG', 'LYS', 'CG', 'HIS', 10.48), ('CG', 'LYS', 'ND1', 'HIS', 11.01), ('CG', 'LYS', 'CD2', 'HIS', 9.44), ('CG', 'LYS', 'CE1', 'HIS', 10.39), ('CG', 'LYS', 'NE2', 'HIS', 9.37)], [('CD', 'LYS', 'CB', 'HIS', 9.9), ('CD', 'LYS', 'CG', 'HIS', 9.06), ('CD', 'LYS', 'ND1', 'HIS', 9.55), ('CD', 'LYS', 'CD2', 'HIS', 8.06), ('CD', 'LYS', 'CE1', 'HIS', 8.96), ('CD', 'LYS', 'NE2', 'HIS', 7.99)], [('CE', 'LYS', 'CB', 'HIS', 9.41), ('CE', 'LYS', 'CG', 'HIS', 8.38), ('CE', 'LYS', 'ND1', 'HIS', 8.78), ('CE', 'LYS', 'CD2', 'HIS', 7.25), ('CE', 'LYS', 'CE1', 'HIS', 8.01), ('CE', 'LYS', 'NE2', 'HIS', 6.96)], [('NZ', 'LYS', 'CB', 'HIS', 8.28), ('NZ', 'LYS', 'CG', 'HIS', 7.15), ('NZ', 'LYS', 'ND1', 'HIS', 7.4), ('NZ', 'LYS', 'CD2', 'HIS', 6.11), ('NZ', 'LYS', 'CE1', 'HIS', 6.62), ('NZ', 'LYS', 'NE2', 'HIS', 5.69)], [('CB', 'LYS', 'CB', 'HIS', 16.03), ('CB', 'LYS', 'CG', 'HIS', 15.19), ('CB', 'LYS', 'ND1', 'HIS', 13.81), ('CB', 'LYS', 'CD2', 'HIS', 15.67), ('CB', 'LYS', 'CE1', 'HIS', 13.51), ('CB', 'LYS', 'NE2', 'HIS', 14.67)], [('CG', 'LYS', 'CB', 'HIS', 14.71), ('CG', 'LYS', 'CG', 'HIS', 13.81), ('CG', 'LYS', 'ND1', 'HIS', 12.42), ('CG', 'LYS', 'CD2', 'HIS', 14.24), ('CG', 'LYS', 'CE1', 'HIS', 12.07), ('CG', 'LYS', 'NE2', 'HIS', 13.21)], [('CD', 'LYS', 'CB', 'HIS', 14.07), ('CD', 'LYS', 'CG', 'HIS', 13.17), ('CD', 'LYS', 'ND1', 'HIS', 11.8), ('CD', 'LYS', 'CD2', 'HIS', 13.6), ('CD', 'LYS', 'CE1', 'HIS', 11.44), ('CD', 'LYS', 'NE2', 'HIS', 12.58)], [('CE', 'LYS', 'CB', 'HIS', 12.79), ('CE', 'LYS', 'CG', 'HIS', 11.81), ('CE', 'LYS', 'ND1', 'HIS', 10.45), ('CE', 'LYS', 'CD2', 'HIS', 12.17), ('CE', 'LYS', 'CE1', 'HIS', 10.01), ('CE', 'LYS', 'NE2', 'HIS', 11.12)], [('NZ', 'LYS', 'CB', 'HIS', 12.65), ('NZ', 'LYS', 'CG', 'HIS', 11.66), ('NZ', 'LYS', 'ND1', 'HIS', 10.35), ('NZ', 'LYS', 'CD2', 'HIS', 11.96), ('NZ', 'LYS', 'CE1', 'HIS', 9.89), ('NZ', 'LYS', 'NE2', 'HIS', 10.92)], [('CB', 'LYS', 'CB', 'HIS', 10.18), ('CB', 'LYS', 'CG', 'HIS', 10.35), ('CB', 'LYS', 'ND1', 'HIS', 10.97), ('CB', 'LYS', 'CD2', 'HIS', 10.3), ('CB', 'LYS', 'CE1', 'HIS', 11.24), ('CB', 'LYS', 'NE2', 'HIS', 10.88)], [('CG', 'LYS', 'CB', 'HIS', 9.94), ('CG', 'LYS', 'CG', 'HIS', 9.84), ('CG', 'LYS', 'ND1', 'HIS', 10.34), ('CG', 'LYS', 'CD2', 'HIS', 9.63), ('CG', 'LYS', 'CE1', 'HIS', 10.42), ('CG', 'LYS', 'NE2', 'HIS', 10.02)], [('CD', 'LYS', 'CB', 'HIS', 8.52), ('CD', 'LYS', 'CG', 'HIS', 8.35), ('CD', 'LYS', 'ND1', 'HIS', 8.91), ('CD', 'LYS', 'CD2', 'HIS', 8.11), ('CD', 'LYS', 'CE1', 'HIS', 8.98), ('CD', 'LYS', 'NE2', 'HIS', 8.54)], [('CE', 'LYS', 'CB', 'HIS', 8.75), ('CE', 'LYS', 'CG', 'HIS', 8.4), ('CE', 'LYS', 'ND1', 'HIS', 9.05), ('CE', 'LYS', 'CD2', 'HIS', 7.84), ('CE', 'LYS', 'CE1', 'HIS', 8.92), ('CE', 'LYS', 'NE2', 'HIS', 8.22)], [('NZ', 'LYS', 'CB', 'HIS', 7.7), ('NZ', 'LYS', 'CG', 'HIS', 7.16), ('NZ', 'LYS', 'ND1', 'HIS', 7.85), ('NZ', 'LYS', 'CD2', 'HIS', 6.46), ('NZ', 'LYS', 'CE1', 'HIS', 7.63), ('NZ', 'LYS', 'NE2', 'HIS', 6.81)], [('CB', 'LYS', 'CB', 'HIS', 7.66), ('CB', 'LYS', 'CG', 'HIS', 8.53), ('CB', 'LYS', 'ND1', 'HIS', 8.85), ('CB', 'LYS', 'CD2', 'HIS', 9.48), ('CB', 'LYS', 'CE1', 'HIS', 9.87), ('CB', 'LYS', 'NE2', 'HIS', 10.22)], [('CG', 'LYS', 'CB', 'HIS', 6.39), ('CG', 'LYS', 'CG', 'HIS', 7.11), ('CG', 'LYS', 'ND1', 'HIS', 7.46), ('CG', 'LYS', 'CD2', 'HIS', 8.01), ('CG', 'LYS', 'CE1', 'HIS', 8.42), ('CG', 'LYS', 'NE2', 'HIS', 8.72)], [('CD', 'LYS', 'CB', 'HIS', 6.7), ('CD', 'LYS', 'CG', 'HIS', 7.04), ('CD', 'LYS', 'ND1', 'HIS', 7.0), ('CD', 'LYS', 'CD2', 'HIS', 7.94), ('CD', 'LYS', 'CE1', 'HIS', 7.84), ('CD', 'LYS', 'NE2', 'HIS', 8.35)], [('CE', 'LYS', 'CB', 'HIS', 5.91), ('CE', 'LYS', 'CG', 'HIS', 6.12), ('CE', 'LYS', 'ND1', 'HIS', 5.83), ('CE', 'LYS', 'CD2', 'HIS', 7.18), ('CE', 'LYS', 'CE1', 'HIS', 6.77), ('CE', 'LYS', 'NE2', 'HIS', 7.49)], [('NZ', 'LYS', 'CB', 'HIS', 6.81), ('NZ', 'LYS', 'CG', 'HIS', 6.59), ('NZ', 'LYS', 'ND1', 'HIS', 5.87), ('NZ', 'LYS', 'CD2', 'HIS', 7.51), ('NZ', 'LYS', 'CE1', 'HIS', 6.52), ('NZ', 'LYS', 'NE2', 'HIS', 7.44)]]}
HIS_LYSI = { 
	'distances':
		[[7.66, 6.39, 6.7, 5.91, 6.81], [8.53, 7.11, 7.04, 6.12, 6.59], [8.85, 7.46, 7.0, 5.83, 5.87], [9.48, 8.01, 7.94, 7.18, 7.51], [9.87, 8.42, 7.84, 6.77, 6.52], [10.22, 8.72, 8.35, 7.49, 7.44]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYSI', 7.66), ('CB', 'HIS', 'CG', 'LYSI', 6.39), ('CB', 'HIS', 'CD', 'LYSI', 6.7), ('CB', 'HIS', 'CE', 'LYSI', 5.91), ('CB', 'HIS', 'NZ', 'LYSI', 6.81)], [('CG', 'HIS', 'CB', 'LYSI', 8.53), ('CG', 'HIS', 'CG', 'LYSI', 7.11), ('CG', 'HIS', 'CD', 'LYSI', 7.04), ('CG', 'HIS', 'CE', 'LYSI', 6.12), ('CG', 'HIS', 'NZ', 'LYSI', 6.59)], [('ND1', 'HIS', 'CB', 'LYSI', 8.85), ('ND1', 'HIS', 'CG', 'LYSI', 7.46), ('ND1', 'HIS', 'CD', 'LYSI', 7.0), ('ND1', 'HIS', 'CE', 'LYSI', 5.83), ('ND1', 'HIS', 'NZ', 'LYSI', 5.87)], [('CD2', 'HIS', 'CB', 'LYSI', 9.48), ('CD2', 'HIS', 'CG', 'LYSI', 8.01), ('CD2', 'HIS', 'CD', 'LYSI', 7.94), ('CD2', 'HIS', 'CE', 'LYSI', 7.18), ('CD2', 'HIS', 'NZ', 'LYSI', 7.51)], [('CE1', 'HIS', 'CB', 'LYSI', 9.87), ('CE1', 'HIS', 'CG', 'LYSI', 8.42), ('CE1', 'HIS', 'CD', 'LYSI', 7.84), ('CE1', 'HIS', 'CE', 'LYSI', 6.77), ('CE1', 'HIS', 'NZ', 'LYSI', 6.52)], [('NE2', 'HIS', 'CB', 'LYSI', 10.22), ('NE2', 'HIS', 'CG', 'LYSI', 8.72), ('NE2', 'HIS', 'CD', 'LYSI', 8.35), ('NE2', 'HIS', 'CE', 'LYSI', 7.49), ('NE2', 'HIS', 'NZ', 'LYSI', 7.44)]]}
HIS_ASP = { 
	'distances':
		[[11.18, 9.78, 9.29, 9.32], [11.19, 9.72, 9.3, 9.12], [12.43, 10.96, 10.57, 10.27], [10.32, 8.83, 8.47, 8.16], [12.39, 10.91, 10.6, 10.13], [11.18, 9.69, 9.41, 8.92], [10.88, 10.49, 11.48, 9.3], [11.1, 10.53, 11.42, 9.29], [10.2, 9.52, 10.33, 8.28], [12.31, 11.67, 12.5, 10.43], [11.02, 10.22, 10.91, 8.99], [12.25, 11.49, 12.2, 10.25]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 11.18), ('CB', 'HIS', 'CG', 'ASP', 9.78), ('CB', 'HIS', 'OD1', 'ASP', 9.29), ('CB', 'HIS', 'OD2', 'ASP', 9.32)], [('CG', 'HIS', 'CB', 'ASP', 11.19), ('CG', 'HIS', 'CG', 'ASP', 9.72), ('CG', 'HIS', 'OD1', 'ASP', 9.3), ('CG', 'HIS', 'OD2', 'ASP', 9.12)], [('ND1', 'HIS', 'CB', 'ASP', 12.43), ('ND1', 'HIS', 'CG', 'ASP', 10.96), ('ND1', 'HIS', 'OD1', 'ASP', 10.57), ('ND1', 'HIS', 'OD2', 'ASP', 10.27)], [('CD2', 'HIS', 'CB', 'ASP', 10.32), ('CD2', 'HIS', 'CG', 'ASP', 8.83), ('CD2', 'HIS', 'OD1', 'ASP', 8.47), ('CD2', 'HIS', 'OD2', 'ASP', 8.16)], [('CE1', 'HIS', 'CB', 'ASP', 12.39), ('CE1', 'HIS', 'CG', 'ASP', 10.91), ('CE1', 'HIS', 'OD1', 'ASP', 10.6), ('CE1', 'HIS', 'OD2', 'ASP', 10.13)], [('NE2', 'HIS', 'CB', 'ASP', 11.18), ('NE2', 'HIS', 'CG', 'ASP', 9.69), ('NE2', 'HIS', 'OD1', 'ASP', 9.41), ('NE2', 'HIS', 'OD2', 'ASP', 8.92)], [('CB', 'HIS', 'CB', 'ASP', 10.88), ('CB', 'HIS', 'CG', 'ASP', 10.49), ('CB', 'HIS', 'OD1', 'ASP', 11.48), ('CB', 'HIS', 'OD2', 'ASP', 9.3)], [('CG', 'HIS', 'CB', 'ASP', 11.1), ('CG', 'HIS', 'CG', 'ASP', 10.53), ('CG', 'HIS', 'OD1', 'ASP', 11.42), ('CG', 'HIS', 'OD2', 'ASP', 9.29)], [('ND1', 'HIS', 'CB', 'ASP', 10.2), ('ND1', 'HIS', 'CG', 'ASP', 9.52), ('ND1', 'HIS', 'OD1', 'ASP', 10.33), ('ND1', 'HIS', 'OD2', 'ASP', 8.28)], [('CD2', 'HIS', 'CB', 'ASP', 12.31), ('CD2', 'HIS', 'CG', 'ASP', 11.67), ('CD2', 'HIS', 'OD1', 'ASP', 12.5), ('CD2', 'HIS', 'OD2', 'ASP', 10.43)], [('CE1', 'HIS', 'CB', 'ASP', 11.02), ('CE1', 'HIS', 'CG', 'ASP', 10.22), ('CE1', 'HIS', 'OD1', 'ASP', 10.91), ('CE1', 'HIS', 'OD2', 'ASP', 8.99)], [('NE2', 'HIS', 'CB', 'ASP', 12.25), ('NE2', 'HIS', 'CG', 'ASP', 11.49), ('NE2', 'HIS', 'OD1', 'ASP', 12.2), ('NE2', 'HIS', 'OD2', 'ASP', 10.25)]]}
ARG_CA = { 
	'distances':
		[[10.64], [9.35], [8.85], [7.53], [7.58], [8.82], [6.59]],
	'comparisons':
		[[('CB', 'ARG', 'CA', 'CA', 10.64)], [('CG', 'ARG', 'CA', 'CA', 9.35)], [('CD', 'ARG', 'CA', 'CA', 8.85)], [('NE', 'ARG', 'CA', 'CA', 7.53)], [('CZ', 'ARG', 'CA', 'CA', 7.58)], [('NH1', 'ARG', 'CA', 'CA', 8.82)], [('NH2', 'ARG', 'CA', 'CA', 6.59)]]}
LYS_ASP = { 
	'distances':
		[[11.27, 10.3, 9.48, 10.55], [10.71, 9.66, 8.99, 9.72], [10.53, 9.29, 8.58, 9.23], [10.33, 9.03, 8.52, 8.71], [10.86, 9.44, 8.91, 9.0], [10.97, 10.5, 11.18, 9.62], [10.85, 10.26, 10.97, 9.22], [10.08, 9.28, 9.87, 8.22], [9.0, 8.21, 8.9, 7.05], [8.7, 7.64, 8.15, 6.47]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 11.27), ('CB', 'LYS', 'CG', 'ASP', 10.3), ('CB', 'LYS', 'OD1', 'ASP', 9.48), ('CB', 'LYS', 'OD2', 'ASP', 10.55)], [('CG', 'LYS', 'CB', 'ASP', 10.71), ('CG', 'LYS', 'CG', 'ASP', 9.66), ('CG', 'LYS', 'OD1', 'ASP', 8.99), ('CG', 'LYS', 'OD2', 'ASP', 9.72)], [('CD', 'LYS', 'CB', 'ASP', 10.53), ('CD', 'LYS', 'CG', 'ASP', 9.29), ('CD', 'LYS', 'OD1', 'ASP', 8.58), ('CD', 'LYS', 'OD2', 'ASP', 9.23)], [('CE', 'LYS', 'CB', 'ASP', 10.33), ('CE', 'LYS', 'CG', 'ASP', 9.03), ('CE', 'LYS', 'OD1', 'ASP', 8.52), ('CE', 'LYS', 'OD2', 'ASP', 8.71)], [('NZ', 'LYS', 'CB', 'ASP', 10.86), ('NZ', 'LYS', 'CG', 'ASP', 9.44), ('NZ', 'LYS', 'OD1', 'ASP', 8.91), ('NZ', 'LYS', 'OD2', 'ASP', 9.0)], [('CB', 'LYS', 'CB', 'ASP', 10.97), ('CB', 'LYS', 'CG', 'ASP', 10.5), ('CB', 'LYS', 'OD1', 'ASP', 11.18), ('CB', 'LYS', 'OD2', 'ASP', 9.62)], [('CG', 'LYS', 'CB', 'ASP', 10.85), ('CG', 'LYS', 'CG', 'ASP', 10.26), ('CG', 'LYS', 'OD1', 'ASP', 10.97), ('CG', 'LYS', 'OD2', 'ASP', 9.22)], [('CD', 'LYS', 'CB', 'ASP', 10.08), ('CD', 'LYS', 'CG', 'ASP', 9.28), ('CD', 'LYS', 'OD1', 'ASP', 9.87), ('CD', 'LYS', 'OD2', 'ASP', 8.22)], [('CE', 'LYS', 'CB', 'ASP', 9.0), ('CE', 'LYS', 'CG', 'ASP', 8.21), ('CE', 'LYS', 'OD1', 'ASP', 8.9), ('CE', 'LYS', 'OD2', 'ASP', 7.05)], [('NZ', 'LYS', 'CB', 'ASP', 8.7), ('NZ', 'LYS', 'CG', 'ASP', 7.64), ('NZ', 'LYS', 'OD1', 'ASP', 8.15), ('NZ', 'LYS', 'OD2', 'ASP', 6.47)]]}
HIS_ARG = { 
	'distances':
		[[14.93, 13.54, 12.54, 11.19, 10.65, 11.39, 9.51], [14.61, 13.29, 12.24, 10.94, 10.62, 11.49, 9.55], [15.49, 14.23, 13.1, 11.88, 11.65, 12.52, 10.67], [13.68, 12.4, 11.39, 10.11, 9.94, 10.94, 8.91], [15.14, 13.97, 12.82, 11.68, 11.63, 12.59, 10.74], [14.06, 12.88, 11.81, 10.64, 10.65, 11.7, 9.75], [7.76, 7.47, 6.1, 6.55, 7.35, 7.75, 8.1], [8.61, 8.28, 6.95, 7.18, 8.06, 8.71, 8.59], [8.61, 8.1, 6.85, 6.78, 7.71, 8.6, 8.04], [9.74, 9.53, 8.26, 8.51, 9.4, 10.05, 9.88], [9.73, 9.27, 8.1, 7.97, 8.89, 9.85, 9.09], [10.37, 10.07, 8.85, 8.91, 9.82, 10.65, 10.13]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 14.93), ('CB', 'HIS', 'CG', 'ARG', 13.54), ('CB', 'HIS', 'CD', 'ARG', 12.54), ('CB', 'HIS', 'NE', 'ARG', 11.19), ('CB', 'HIS', 'CZ', 'ARG', 10.65), ('CB', 'HIS', 'NH1', 'ARG', 11.39), ('CB', 'HIS', 'NH2', 'ARG', 9.51)], [('CG', 'HIS', 'CB', 'ARG', 14.61), ('CG', 'HIS', 'CG', 'ARG', 13.29), ('CG', 'HIS', 'CD', 'ARG', 12.24), ('CG', 'HIS', 'NE', 'ARG', 10.94), ('CG', 'HIS', 'CZ', 'ARG', 10.62), ('CG', 'HIS', 'NH1', 'ARG', 11.49), ('CG', 'HIS', 'NH2', 'ARG', 9.55)], [('ND1', 'HIS', 'CB', 'ARG', 15.49), ('ND1', 'HIS', 'CG', 'ARG', 14.23), ('ND1', 'HIS', 'CD', 'ARG', 13.1), ('ND1', 'HIS', 'NE', 'ARG', 11.88), ('ND1', 'HIS', 'CZ', 'ARG', 11.65), ('ND1', 'HIS', 'NH1', 'ARG', 12.52), ('ND1', 'HIS', 'NH2', 'ARG', 10.67)], [('CD2', 'HIS', 'CB', 'ARG', 13.68), ('CD2', 'HIS', 'CG', 'ARG', 12.4), ('CD2', 'HIS', 'CD', 'ARG', 11.39), ('CD2', 'HIS', 'NE', 'ARG', 10.11), ('CD2', 'HIS', 'CZ', 'ARG', 9.94), ('CD2', 'HIS', 'NH1', 'ARG', 10.94), ('CD2', 'HIS', 'NH2', 'ARG', 8.91)], [('CE1', 'HIS', 'CB', 'ARG', 15.14), ('CE1', 'HIS', 'CG', 'ARG', 13.97), ('CE1', 'HIS', 'CD', 'ARG', 12.82), ('CE1', 'HIS', 'NE', 'ARG', 11.68), ('CE1', 'HIS', 'CZ', 'ARG', 11.63), ('CE1', 'HIS', 'NH1', 'ARG', 12.59), ('CE1', 'HIS', 'NH2', 'ARG', 10.74)], [('NE2', 'HIS', 'CB', 'ARG', 14.06), ('NE2', 'HIS', 'CG', 'ARG', 12.88), ('NE2', 'HIS', 'CD', 'ARG', 11.81), ('NE2', 'HIS', 'NE', 'ARG', 10.64), ('NE2', 'HIS', 'CZ', 'ARG', 10.65), ('NE2', 'HIS', 'NH1', 'ARG', 11.7), ('NE2', 'HIS', 'NH2', 'ARG', 9.75)], [('CB', 'HIS', 'CB', 'ARG', 7.76), ('CB', 'HIS', 'CG', 'ARG', 7.47), ('CB', 'HIS', 'CD', 'ARG', 6.1), ('CB', 'HIS', 'NE', 'ARG', 6.55), ('CB', 'HIS', 'CZ', 'ARG', 7.35), ('CB', 'HIS', 'NH1', 'ARG', 7.75), ('CB', 'HIS', 'NH2', 'ARG', 8.1)], [('CG', 'HIS', 'CB', 'ARG', 8.61), ('CG', 'HIS', 'CG', 'ARG', 8.28), ('CG', 'HIS', 'CD', 'ARG', 6.95), ('CG', 'HIS', 'NE', 'ARG', 7.18), ('CG', 'HIS', 'CZ', 'ARG', 8.06), ('CG', 'HIS', 'NH1', 'ARG', 8.71), ('CG', 'HIS', 'NH2', 'ARG', 8.59)], [('ND1', 'HIS', 'CB', 'ARG', 8.61), ('ND1', 'HIS', 'CG', 'ARG', 8.1), ('ND1', 'HIS', 'CD', 'ARG', 6.85), ('ND1', 'HIS', 'NE', 'ARG', 6.78), ('ND1', 'HIS', 'CZ', 'ARG', 7.71), ('ND1', 'HIS', 'NH1', 'ARG', 8.6), ('ND1', 'HIS', 'NH2', 'ARG', 8.04)], [('CD2', 'HIS', 'CB', 'ARG', 9.74), ('CD2', 'HIS', 'CG', 'ARG', 9.53), ('CD2', 'HIS', 'CD', 'ARG', 8.26), ('CD2', 'HIS', 'NE', 'ARG', 8.51), ('CD2', 'HIS', 'CZ', 'ARG', 9.4), ('CD2', 'HIS', 'NH1', 'ARG', 10.05), ('CD2', 'HIS', 'NH2', 'ARG', 9.88)], [('CE1', 'HIS', 'CB', 'ARG', 9.73), ('CE1', 'HIS', 'CG', 'ARG', 9.27), ('CE1', 'HIS', 'CD', 'ARG', 8.1), ('CE1', 'HIS', 'NE', 'ARG', 7.97), ('CE1', 'HIS', 'CZ', 'ARG', 8.89), ('CE1', 'HIS', 'NH1', 'ARG', 9.85), ('CE1', 'HIS', 'NH2', 'ARG', 9.09)], [('NE2', 'HIS', 'CB', 'ARG', 10.37), ('NE2', 'HIS', 'CG', 'ARG', 10.07), ('NE2', 'HIS', 'CD', 'ARG', 8.85), ('NE2', 'HIS', 'NE', 'ARG', 8.91), ('NE2', 'HIS', 'CZ', 'ARG', 9.82), ('NE2', 'HIS', 'NH1', 'ARG', 10.65), ('NE2', 'HIS', 'NH2', 'ARG', 10.13)]]}
HIS_CA = { 
	'distances':
		[[7.93], [7.47], [8.56], [6.37], [8.32], [7.05], [10.19], [9.78], [8.55], [10.67], [8.87], [10.16]],
	'comparisons':
		[[('CB', 'HIS', 'CA', 'CA', 7.93)], [('CG', 'HIS', 'CA', 'CA', 7.47)], [('ND1', 'HIS', 'CA', 'CA', 8.56)], [('CD2', 'HIS', 'CA', 'CA', 6.37)], [('CE1', 'HIS', 'CA', 'CA', 8.32)], [('NE2', 'HIS', 'CA', 'CA', 7.05)], [('CB', 'HIS', 'CA', 'CA', 10.19)], [('CG', 'HIS', 'CA', 'CA', 9.78)], [('ND1', 'HIS', 'CA', 'CA', 8.55)], [('CD2', 'HIS', 'CA', 'CA', 10.67)], [('CE1', 'HIS', 'CA', 'CA', 8.87)], [('NE2', 'HIS', 'CA', 'CA', 10.16)]]}
ASP_LYSI = { 
	'distances':
		[[10.97, 10.85, 10.08, 9.0, 8.7], [10.5, 10.26, 9.28, 8.21, 7.64], [11.18, 10.97, 9.87, 8.9, 8.15], [9.62, 9.22, 8.22, 7.05, 6.47]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYSI', 10.97), ('CB', 'ASP', 'CG', 'LYSI', 10.85), ('CB', 'ASP', 'CD', 'LYSI', 10.08), ('CB', 'ASP', 'CE', 'LYSI', 9.0), ('CB', 'ASP', 'NZ', 'LYSI', 8.7)], [('CG', 'ASP', 'CB', 'LYSI', 10.5), ('CG', 'ASP', 'CG', 'LYSI', 10.26), ('CG', 'ASP', 'CD', 'LYSI', 9.28), ('CG', 'ASP', 'CE', 'LYSI', 8.21), ('CG', 'ASP', 'NZ', 'LYSI', 7.64)], [('OD1', 'ASP', 'CB', 'LYSI', 11.18), ('OD1', 'ASP', 'CG', 'LYSI', 10.97), ('OD1', 'ASP', 'CD', 'LYSI', 9.87), ('OD1', 'ASP', 'CE', 'LYSI', 8.9), ('OD1', 'ASP', 'NZ', 'LYSI', 8.15)], [('OD2', 'ASP', 'CB', 'LYSI', 9.62), ('OD2', 'ASP', 'CG', 'LYSI', 9.22), ('OD2', 'ASP', 'CD', 'LYSI', 8.22), ('OD2', 'ASP', 'CE', 'LYSI', 7.05), ('OD2', 'ASP', 'NZ', 'LYSI', 6.47)]]}
ARG_LYSI = { 
	'distances':
		[[10.38, 9.96, 10.19, 9.08, 9.79], [9.38, 9.03, 9.09, 7.96, 8.61], [8.13, 7.62, 7.69, 6.57, 7.33], [7.66, 7.2, 6.93, 5.73, 6.28], [6.99, 6.85, 6.59, 5.67, 6.29], [6.61, 6.81, 6.91, 6.33, 7.22], [7.14, 7.05, 6.43, 5.58, 5.82]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYSI', 10.38), ('CB', 'ARG', 'CG', 'LYSI', 9.96), ('CB', 'ARG', 'CD', 'LYSI', 10.19), ('CB', 'ARG', 'CE', 'LYSI', 9.08), ('CB', 'ARG', 'NZ', 'LYSI', 9.79)], [('CG', 'ARG', 'CB', 'LYSI', 9.38), ('CG', 'ARG', 'CG', 'LYSI', 9.03), ('CG', 'ARG', 'CD', 'LYSI', 9.09), ('CG', 'ARG', 'CE', 'LYSI', 7.96), ('CG', 'ARG', 'NZ', 'LYSI', 8.61)], [('CD', 'ARG', 'CB', 'LYSI', 8.13), ('CD', 'ARG', 'CG', 'LYSI', 7.62), ('CD', 'ARG', 'CD', 'LYSI', 7.69), ('CD', 'ARG', 'CE', 'LYSI', 6.57), ('CD', 'ARG', 'NZ', 'LYSI', 7.33)], [('NE', 'ARG', 'CB', 'LYSI', 7.66), ('NE', 'ARG', 'CG', 'LYSI', 7.2), ('NE', 'ARG', 'CD', 'LYSI', 6.93), ('NE', 'ARG', 'CE', 'LYSI', 5.73), ('NE', 'ARG', 'NZ', 'LYSI', 6.28)], [('CZ', 'ARG', 'CB', 'LYSI', 6.99), ('CZ', 'ARG', 'CG', 'LYSI', 6.85), ('CZ', 'ARG', 'CD', 'LYSI', 6.59), ('CZ', 'ARG', 'CE', 'LYSI', 5.67), ('CZ', 'ARG', 'NZ', 'LYSI', 6.29)], [('NH1', 'ARG', 'CB', 'LYSI', 6.61), ('NH1', 'ARG', 'CG', 'LYSI', 6.81), ('NH1', 'ARG', 'CD', 'LYSI', 6.91), ('NH1', 'ARG', 'CE', 'LYSI', 6.33), ('NH1', 'ARG', 'NZ', 'LYSI', 7.22)], [('NH2', 'ARG', 'CB', 'LYSI', 7.14), ('NH2', 'ARG', 'CG', 'LYSI', 7.05), ('NH2', 'ARG', 'CD', 'LYSI', 6.43), ('NH2', 'ARG', 'CE', 'LYSI', 5.58), ('NH2', 'ARG', 'NZ', 'LYSI', 5.82)]]}
LYS_LYS = { 
	'distances':
		[[17.19, 16.5, 15.09, 14.07, 12.72], [16.17, 15.38, 13.99, 12.92, 11.57], [15.18, 14.4, 12.96, 12.0, 10.59], [14.2, 13.31, 11.88, 10.9, 9.48], [13.65, 12.76, 11.29, 10.49, 9.01], [17.19, 16.17, 15.18, 14.2, 13.65], [16.5, 15.38, 14.4, 13.31, 12.76], [15.09, 13.99, 12.96, 11.88, 11.29], [14.07, 12.92, 12.0, 10.9, 10.49], [12.72, 11.57, 10.59, 9.48, 9.01]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 17.19), ('CB', 'LYS', 'CG', 'LYS', 16.5), ('CB', 'LYS', 'CD', 'LYS', 15.09), ('CB', 'LYS', 'CE', 'LYS', 14.07), ('CB', 'LYS', 'NZ', 'LYS', 12.72)], [('CG', 'LYS', 'CB', 'LYS', 16.17), ('CG', 'LYS', 'CG', 'LYS', 15.38), ('CG', 'LYS', 'CD', 'LYS', 13.99), ('CG', 'LYS', 'CE', 'LYS', 12.92), ('CG', 'LYS', 'NZ', 'LYS', 11.57)], [('CD', 'LYS', 'CB', 'LYS', 15.18), ('CD', 'LYS', 'CG', 'LYS', 14.4), ('CD', 'LYS', 'CD', 'LYS', 12.96), ('CD', 'LYS', 'CE', 'LYS', 12.0), ('CD', 'LYS', 'NZ', 'LYS', 10.59)], [('CE', 'LYS', 'CB', 'LYS', 14.2), ('CE', 'LYS', 'CG', 'LYS', 13.31), ('CE', 'LYS', 'CD', 'LYS', 11.88), ('CE', 'LYS', 'CE', 'LYS', 10.9), ('CE', 'LYS', 'NZ', 'LYS', 9.48)], [('NZ', 'LYS', 'CB', 'LYS', 13.65), ('NZ', 'LYS', 'CG', 'LYS', 12.76), ('NZ', 'LYS', 'CD', 'LYS', 11.29), ('NZ', 'LYS', 'CE', 'LYS', 10.49), ('NZ', 'LYS', 'NZ', 'LYS', 9.01)], [('CB', 'LYS', 'CB', 'LYS', 17.19), ('CB', 'LYS', 'CG', 'LYS', 16.17), ('CB', 'LYS', 'CD', 'LYS', 15.18), ('CB', 'LYS', 'CE', 'LYS', 14.2), ('CB', 'LYS', 'NZ', 'LYS', 13.65)], [('CG', 'LYS', 'CB', 'LYS', 16.5), ('CG', 'LYS', 'CG', 'LYS', 15.38), ('CG', 'LYS', 'CD', 'LYS', 14.4), ('CG', 'LYS', 'CE', 'LYS', 13.31), ('CG', 'LYS', 'NZ', 'LYS', 12.76)], [('CD', 'LYS', 'CB', 'LYS', 15.09), ('CD', 'LYS', 'CG', 'LYS', 13.99), ('CD', 'LYS', 'CD', 'LYS', 12.96), ('CD', 'LYS', 'CE', 'LYS', 11.88), ('CD', 'LYS', 'NZ', 'LYS', 11.29)], [('CE', 'LYS', 'CB', 'LYS', 14.07), ('CE', 'LYS', 'CG', 'LYS', 12.92), ('CE', 'LYS', 'CD', 'LYS', 12.0), ('CE', 'LYS', 'CE', 'LYS', 10.9), ('CE', 'LYS', 'NZ', 'LYS', 10.49)], [('NZ', 'LYS', 'CB', 'LYS', 12.72), ('NZ', 'LYS', 'CG', 'LYS', 11.57), ('NZ', 'LYS', 'CD', 'LYS', 10.59), ('NZ', 'LYS', 'CE', 'LYS', 9.48), ('NZ', 'LYS', 'NZ', 'LYS', 9.01)]]}
CA_HISI = { 
	'distances':
		[10.19, 9.78, 8.55, 10.67, 8.87, 10.16],
	'comparisons':
		[('CA', 'CA', 'CB', 'HISI', 10.19), ('CA', 'CA', 'CG', 'HISI', 9.78), ('CA', 'CA', 'ND1', 'HISI', 8.55), ('CA', 'CA', 'CD2', 'HISI', 10.67), ('CA', 'CA', 'CE1', 'HISI', 8.87), ('CA', 'CA', 'NE2', 'HISI', 10.16)]}
CA_LYSI = { 
	'distances':
		[10.56, 9.98, 8.67, 7.61, 6.46],
	'comparisons':
		[('CA', 'CA', 'CB', 'LYSI', 10.56), ('CA', 'CA', 'CG', 'LYSI', 9.98), ('CA', 'CA', 'CD', 'LYSI', 8.67), ('CA', 'CA', 'CE', 'LYSI', 7.61), ('CA', 'CA', 'NZ', 'LYSI', 6.46)]}
LYS_CA = { 
	'distances':
		[[8.74], [7.83], [7.09], [6.53], [6.71], [10.56], [9.98], [8.67], [7.61], [6.46]],
	'comparisons':
		[[('CB', 'LYS', 'CA', 'CA', 8.74)], [('CG', 'LYS', 'CA', 'CA', 7.83)], [('CD', 'LYS', 'CA', 'CA', 7.09)], [('CE', 'LYS', 'CA', 'CA', 6.53)], [('NZ', 'LYS', 'CA', 'CA', 6.71)], [('CB', 'LYS', 'CA', 'CA', 10.56)], [('CG', 'LYS', 'CA', 'CA', 9.98)], [('CD', 'LYS', 'CA', 'CA', 8.67)], [('CE', 'LYS', 'CA', 'CA', 7.61)], [('NZ', 'LYS', 'CA', 'CA', 6.46)]]}
ASP_ARG = { 
	'distances':
		[[8.49, 7.21, 7.58, 6.54, 6.37, 7.21, 5.84], [9.15, 7.8, 7.79, 6.52, 6.35, 7.4, 5.49], [10.41, 9.05, 9.0, 7.69, 7.43, 8.44, 6.41], [8.62, 7.24, 6.96, 5.63, 5.61, 6.82, 4.79]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 8.49), ('CB', 'ASP', 'CG', 'ARG', 7.21), ('CB', 'ASP', 'CD', 'ARG', 7.58), ('CB', 'ASP', 'NE', 'ARG', 6.54), ('CB', 'ASP', 'CZ', 'ARG', 6.37), ('CB', 'ASP', 'NH1', 'ARG', 7.21), ('CB', 'ASP', 'NH2', 'ARG', 5.84)], [('CG', 'ASP', 'CB', 'ARG', 9.15), ('CG', 'ASP', 'CG', 'ARG', 7.8), ('CG', 'ASP', 'CD', 'ARG', 7.79), ('CG', 'ASP', 'NE', 'ARG', 6.52), ('CG', 'ASP', 'CZ', 'ARG', 6.35), ('CG', 'ASP', 'NH1', 'ARG', 7.4), ('CG', 'ASP', 'NH2', 'ARG', 5.49)], [('OD1', 'ASP', 'CB', 'ARG', 10.41), ('OD1', 'ASP', 'CG', 'ARG', 9.05), ('OD1', 'ASP', 'CD', 'ARG', 9.0), ('OD1', 'ASP', 'NE', 'ARG', 7.69), ('OD1', 'ASP', 'CZ', 'ARG', 7.43), ('OD1', 'ASP', 'NH1', 'ARG', 8.44), ('OD1', 'ASP', 'NH2', 'ARG', 6.41)], [('OD2', 'ASP', 'CB', 'ARG', 8.62), ('OD2', 'ASP', 'CG', 'ARG', 7.24), ('OD2', 'ASP', 'CD', 'ARG', 6.96), ('OD2', 'ASP', 'NE', 'ARG', 5.63), ('OD2', 'ASP', 'CZ', 'ARG', 5.61), ('OD2', 'ASP', 'NH1', 'ARG', 6.82), ('OD2', 'ASP', 'NH2', 'ARG', 4.79)]]}
ASP_CA = { 
	'distances':
		[[6.31], [4.84], [4.63], [4.36]],
	'comparisons':
		[[('CB', 'ASP', 'CA', 'CA', 6.31)], [('CG', 'ASP', 'CA', 'CA', 4.84)], [('OD1', 'ASP', 'CA', 'CA', 4.63)], [('OD2', 'ASP', 'CA', 'CA', 4.36)]]}
LYS_ARG = { 
	'distances':
		[[16.07, 15.08, 14.92, 13.85, 14.12, 15.37, 13.21], [15.05, 14.1, 13.85, 12.82, 13.18, 14.46, 12.34], [14.9, 13.85, 13.45, 12.33, 12.6, 13.87, 11.67], [14.08, 13.07, 12.53, 11.47, 11.83, 13.12, 10.99], [14.54, 13.45, 12.75, 11.62, 11.88, 13.13, 10.97], [10.38, 9.38, 8.13, 7.66, 6.99, 6.61, 7.14], [9.96, 9.03, 7.62, 7.2, 6.85, 6.81, 7.05], [10.19, 9.09, 7.69, 6.93, 6.59, 6.91, 6.43], [9.08, 7.96, 6.57, 5.73, 5.67, 6.33, 5.58], [9.79, 8.61, 7.33, 6.28, 6.29, 7.22, 5.82]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 16.07), ('CB', 'LYS', 'CG', 'ARG', 15.08), ('CB', 'LYS', 'CD', 'ARG', 14.92), ('CB', 'LYS', 'NE', 'ARG', 13.85), ('CB', 'LYS', 'CZ', 'ARG', 14.12), ('CB', 'LYS', 'NH1', 'ARG', 15.37), ('CB', 'LYS', 'NH2', 'ARG', 13.21)], [('CG', 'LYS', 'CB', 'ARG', 15.05), ('CG', 'LYS', 'CG', 'ARG', 14.1), ('CG', 'LYS', 'CD', 'ARG', 13.85), ('CG', 'LYS', 'NE', 'ARG', 12.82), ('CG', 'LYS', 'CZ', 'ARG', 13.18), ('CG', 'LYS', 'NH1', 'ARG', 14.46), ('CG', 'LYS', 'NH2', 'ARG', 12.34)], [('CD', 'LYS', 'CB', 'ARG', 14.9), ('CD', 'LYS', 'CG', 'ARG', 13.85), ('CD', 'LYS', 'CD', 'ARG', 13.45), ('CD', 'LYS', 'NE', 'ARG', 12.33), ('CD', 'LYS', 'CZ', 'ARG', 12.6), ('CD', 'LYS', 'NH1', 'ARG', 13.87), ('CD', 'LYS', 'NH2', 'ARG', 11.67)], [('CE', 'LYS', 'CB', 'ARG', 14.08), ('CE', 'LYS', 'CG', 'ARG', 13.07), ('CE', 'LYS', 'CD', 'ARG', 12.53), ('CE', 'LYS', 'NE', 'ARG', 11.47), ('CE', 'LYS', 'CZ', 'ARG', 11.83), ('CE', 'LYS', 'NH1', 'ARG', 13.12), ('CE', 'LYS', 'NH2', 'ARG', 10.99)], [('NZ', 'LYS', 'CB', 'ARG', 14.54), ('NZ', 'LYS', 'CG', 'ARG', 13.45), ('NZ', 'LYS', 'CD', 'ARG', 12.75), ('NZ', 'LYS', 'NE', 'ARG', 11.62), ('NZ', 'LYS', 'CZ', 'ARG', 11.88), ('NZ', 'LYS', 'NH1', 'ARG', 13.13), ('NZ', 'LYS', 'NH2', 'ARG', 10.97)], [('CB', 'LYS', 'CB', 'ARG', 10.38), ('CB', 'LYS', 'CG', 'ARG', 9.38), ('CB', 'LYS', 'CD', 'ARG', 8.13), ('CB', 'LYS', 'NE', 'ARG', 7.66), ('CB', 'LYS', 'CZ', 'ARG', 6.99), ('CB', 'LYS', 'NH1', 'ARG', 6.61), ('CB', 'LYS', 'NH2', 'ARG', 7.14)], [('CG', 'LYS', 'CB', 'ARG', 9.96), ('CG', 'LYS', 'CG', 'ARG', 9.03), ('CG', 'LYS', 'CD', 'ARG', 7.62), ('CG', 'LYS', 'NE', 'ARG', 7.2), ('CG', 'LYS', 'CZ', 'ARG', 6.85), ('CG', 'LYS', 'NH1', 'ARG', 6.81), ('CG', 'LYS', 'NH2', 'ARG', 7.05)], [('CD', 'LYS', 'CB', 'ARG', 10.19), ('CD', 'LYS', 'CG', 'ARG', 9.09), ('CD', 'LYS', 'CD', 'ARG', 7.69), ('CD', 'LYS', 'NE', 'ARG', 6.93), ('CD', 'LYS', 'CZ', 'ARG', 6.59), ('CD', 'LYS', 'NH1', 'ARG', 6.91), ('CD', 'LYS', 'NH2', 'ARG', 6.43)], [('CE', 'LYS', 'CB', 'ARG', 9.08), ('CE', 'LYS', 'CG', 'ARG', 7.96), ('CE', 'LYS', 'CD', 'ARG', 6.57), ('CE', 'LYS', 'NE', 'ARG', 5.73), ('CE', 'LYS', 'CZ', 'ARG', 5.67), ('CE', 'LYS', 'NH1', 'ARG', 6.33), ('CE', 'LYS', 'NH2', 'ARG', 5.58)], [('NZ', 'LYS', 'CB', 'ARG', 9.79), ('NZ', 'LYS', 'CG', 'ARG', 8.61), ('NZ', 'LYS', 'CD', 'ARG', 7.33), ('NZ', 'LYS', 'NE', 'ARG', 6.28), ('NZ', 'LYS', 'CZ', 'ARG', 6.29), ('NZ', 'LYS', 'NH1', 'ARG', 7.22), ('NZ', 'LYS', 'NH2', 'ARG', 5.82)]]}
HIS_HIS = { 
	'distances':
		[[12.42, 12.04, 11.22, 12.64, 11.36, 12.21], [11.78, 11.22, 10.32, 11.7, 10.3, 11.13], [12.16, 11.47, 10.64, 11.77, 10.45, 11.13], [11.03, 10.38, 9.37, 10.88, 9.31, 10.24], [11.66, 10.82, 9.92, 11.0, 9.57, 10.24], [10.96, 10.11, 9.09, 10.42, 8.8, 9.63], [12.42, 11.78, 12.16, 11.03, 11.66, 10.96], [12.04, 11.22, 11.47, 10.38, 10.82, 10.11], [11.22, 10.32, 10.64, 9.37, 9.92, 9.09], [12.64, 11.7, 11.77, 10.88, 11.0, 10.42], [11.36, 10.3, 10.45, 9.31, 9.57, 8.8], [12.21, 11.13, 11.13, 10.24, 10.24, 9.63]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 12.42), ('CB', 'HIS', 'CG', 'HIS', 12.04), ('CB', 'HIS', 'ND1', 'HIS', 11.22), ('CB', 'HIS', 'CD2', 'HIS', 12.64), ('CB', 'HIS', 'CE1', 'HIS', 11.36), ('CB', 'HIS', 'NE2', 'HIS', 12.21)], [('CG', 'HIS', 'CB', 'HIS', 11.78), ('CG', 'HIS', 'CG', 'HIS', 11.22), ('CG', 'HIS', 'ND1', 'HIS', 10.32), ('CG', 'HIS', 'CD2', 'HIS', 11.7), ('CG', 'HIS', 'CE1', 'HIS', 10.3), ('CG', 'HIS', 'NE2', 'HIS', 11.13)], [('ND1', 'HIS', 'CB', 'HIS', 12.16), ('ND1', 'HIS', 'CG', 'HIS', 11.47), ('ND1', 'HIS', 'ND1', 'HIS', 10.64), ('ND1', 'HIS', 'CD2', 'HIS', 11.77), ('ND1', 'HIS', 'CE1', 'HIS', 10.45), ('ND1', 'HIS', 'NE2', 'HIS', 11.13)], [('CD2', 'HIS', 'CB', 'HIS', 11.03), ('CD2', 'HIS', 'CG', 'HIS', 10.38), ('CD2', 'HIS', 'ND1', 'HIS', 9.37), ('CD2', 'HIS', 'CD2', 'HIS', 10.88), ('CD2', 'HIS', 'CE1', 'HIS', 9.31), ('CD2', 'HIS', 'NE2', 'HIS', 10.24)], [('CE1', 'HIS', 'CB', 'HIS', 11.66), ('CE1', 'HIS', 'CG', 'HIS', 10.82), ('CE1', 'HIS', 'ND1', 'HIS', 9.92), ('CE1', 'HIS', 'CD2', 'HIS', 11.0), ('CE1', 'HIS', 'CE1', 'HIS', 9.57), ('CE1', 'HIS', 'NE2', 'HIS', 10.24)], [('NE2', 'HIS', 'CB', 'HIS', 10.96), ('NE2', 'HIS', 'CG', 'HIS', 10.11), ('NE2', 'HIS', 'ND1', 'HIS', 9.09), ('NE2', 'HIS', 'CD2', 'HIS', 10.42), ('NE2', 'HIS', 'CE1', 'HIS', 8.8), ('NE2', 'HIS', 'NE2', 'HIS', 9.63)], [('CB', 'HIS', 'CB', 'HIS', 12.42), ('CB', 'HIS', 'CG', 'HIS', 11.78), ('CB', 'HIS', 'ND1', 'HIS', 12.16), ('CB', 'HIS', 'CD2', 'HIS', 11.03), ('CB', 'HIS', 'CE1', 'HIS', 11.66), ('CB', 'HIS', 'NE2', 'HIS', 10.96)], [('CG', 'HIS', 'CB', 'HIS', 12.04), ('CG', 'HIS', 'CG', 'HIS', 11.22), ('CG', 'HIS', 'ND1', 'HIS', 11.47), ('CG', 'HIS', 'CD2', 'HIS', 10.38), ('CG', 'HIS', 'CE1', 'HIS', 10.82), ('CG', 'HIS', 'NE2', 'HIS', 10.11)], [('ND1', 'HIS', 'CB', 'HIS', 11.22), ('ND1', 'HIS', 'CG', 'HIS', 10.32), ('ND1', 'HIS', 'ND1', 'HIS', 10.64), ('ND1', 'HIS', 'CD2', 'HIS', 9.37), ('ND1', 'HIS', 'CE1', 'HIS', 9.92), ('ND1', 'HIS', 'NE2', 'HIS', 9.09)], [('CD2', 'HIS', 'CB', 'HIS', 12.64), ('CD2', 'HIS', 'CG', 'HIS', 11.7), ('CD2', 'HIS', 'ND1', 'HIS', 11.77), ('CD2', 'HIS', 'CD2', 'HIS', 10.88), ('CD2', 'HIS', 'CE1', 'HIS', 11.0), ('CD2', 'HIS', 'NE2', 'HIS', 10.42)], [('CE1', 'HIS', 'CB', 'HIS', 11.36), ('CE1', 'HIS', 'CG', 'HIS', 10.3), ('CE1', 'HIS', 'ND1', 'HIS', 10.45), ('CE1', 'HIS', 'CD2', 'HIS', 9.31), ('CE1', 'HIS', 'CE1', 'HIS', 9.57), ('CE1', 'HIS', 'NE2', 'HIS', 8.8)], [('NE2', 'HIS', 'CB', 'HIS', 12.21), ('NE2', 'HIS', 'CG', 'HIS', 11.13), ('NE2', 'HIS', 'ND1', 'HIS', 11.13), ('NE2', 'HIS', 'CD2', 'HIS', 10.24), ('NE2', 'HIS', 'CE1', 'HIS', 10.24), ('NE2', 'HIS', 'NE2', 'HIS', 9.63)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'M_1hdh_3_1_6_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_LYSI, d, 'M_1hdh_3_1_6_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_ASP, d, 'M_1hdh_3_1_6_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_CA, d, 'M_1hdh_3_1_6_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(LYS_ASP, d, 'M_1hdh_3_1_6_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_ARG, d, 'M_1hdh_3_1_6_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_CA, d, 'M_1hdh_3_1_6_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_LYSI, d, 'M_1hdh_3_1_6_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ARG_LYSI, d, 'M_1hdh_3_1_6_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(LYS_LYS, d, 'M_1hdh_3_1_6_1')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(CA_HISI, d, 'M_1hdh_3_1_6_1')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(CA_LYSI, d, 'M_1hdh_3_1_6_1')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(LYS_CA, d, 'M_1hdh_3_1_6_1')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(ASP_ARG, d, 'M_1hdh_3_1_6_1')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(ASP_CA, d, 'M_1hdh_3_1_6_1')
	if match15 == []:
		 flag = True
		 break
	match16 , totTime16 = cmd.detect(LYS_ARG, d, 'M_1hdh_3_1_6_1')
	if match16 == []:
		 flag = True
		 break
	match17 , totTime17 = cmd.detect(HIS_HIS, d, 'M_1hdh_3_1_6_1')
	if match17 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'HIS_LYSI' :  match2,
		'HIS_ASP' :  match3,
		'ARG_CA' :  match4,
		'LYS_ASP' :  match5,
		'HIS_ARG' :  match6,
		'HIS_CA' :  match7,
		'ASP_LYSI' :  match8,
		'ARG_LYSI' :  match9,
		'LYS_LYS' :  match10,
		'CA_HISI' :  match11,
		'CA_LYSI' :  match12,
		'LYS_CA' :  match13,
		'ASP_ARG' :  match14,
		'ASP_CA' :  match15,
		'LYS_ARG' :  match16,
		'HIS_HIS' :  match17}