'''
FUNC:M_1e7l_3_1_22_4
PDB:1e7l
EC:3.1.22.4
RESI:his,his,glu,zn,his
LOCI:a-41,43,65,1165;b-105;
'''
import motifFunctions as cmd
HIS_ZN = { 
	'distances':
		[[20.57], [19.47], [18.11], [19.59], [17.44], [18.33], [18.08], [18.73], [18.28], [20.0], [19.31], [20.32], [20.68], [19.95], [20.59], [18.72], [19.8], [18.64]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 20.57)], [('CG', 'HIS', 'ZN', 'ZN', 19.47)], [('ND1', 'HIS', 'ZN', 'ZN', 18.11)], [('CD2', 'HIS', 'ZN', 'ZN', 19.59)], [('CE1', 'HIS', 'ZN', 'ZN', 17.44)], [('NE2', 'HIS', 'ZN', 'ZN', 18.33)], [('CB', 'HIS', 'ZN', 'ZN', 18.08)], [('CG', 'HIS', 'ZN', 'ZN', 18.73)], [('ND1', 'HIS', 'ZN', 'ZN', 18.28)], [('CD2', 'HIS', 'ZN', 'ZN', 20.0)], [('CE1', 'HIS', 'ZN', 'ZN', 19.31)], [('NE2', 'HIS', 'ZN', 'ZN', 20.32)], [('CB', 'HIS', 'ZN', 'ZN', 20.68)], [('CG', 'HIS', 'ZN', 'ZN', 19.95)], [('ND1', 'HIS', 'ZN', 'ZN', 20.59)], [('CD2', 'HIS', 'ZN', 'ZN', 18.72)], [('CE1', 'HIS', 'ZN', 'ZN', 19.8)], [('NE2', 'HIS', 'ZN', 'ZN', 18.64)]]}
HIS_HIS = { 
	'distances':
		[[8.88, 7.93, 7.89, 7.37, 7.34, 6.97], [8.17, 7.15, 6.84, 6.84, 6.32, 6.3], [7.75, 6.97, 6.63, 7.01, 6.49, 6.71], [8.22, 7.0, 6.39, 6.69, 5.64, 5.83], [7.56, 6.72, 6.05, 6.99, 5.97, 6.55], [7.86, 6.75, 5.88, 6.82, 5.41, 6.05], [10.83, 10.85, 10.84, 11.19, 11.18, 11.4], [10.18, 9.99, 9.95, 10.17, 10.11, 10.27], [10.25, 10.0, 10.12, 9.97, 10.17, 10.1], [9.78, 9.39, 9.16, 9.57, 9.21, 9.48], [9.92, 9.44, 9.49, 9.26, 9.35, 9.23], [9.63, 9.06, 8.88, 8.99, 8.71, 8.8], [8.88, 8.17, 7.75, 8.22, 7.56, 7.86], [7.93, 7.15, 6.97, 7.0, 6.72, 6.75], [7.89, 6.84, 6.63, 6.39, 6.05, 5.88], [7.37, 6.84, 7.01, 6.69, 6.99, 6.82], [7.34, 6.32, 6.49, 5.64, 5.97, 5.41], [6.97, 6.3, 6.71, 5.83, 6.55, 6.05], [5.61, 5.85, 6.88, 5.81, 7.37, 6.83], [5.41, 5.43, 6.1, 5.62, 6.6, 6.37], [5.95, 5.43, 5.76, 5.37, 5.9, 5.7], [5.48, 5.76, 6.19, 6.37, 6.94, 7.05], [6.29, 5.76, 5.65, 6.02, 5.87, 6.1], [6.05, 5.97, 5.94, 6.59, 6.55, 6.92], [10.83, 10.18, 10.25, 9.78, 9.92, 9.63], [10.85, 9.99, 10.0, 9.39, 9.44, 9.06], [10.84, 9.95, 10.12, 9.16, 9.49, 8.88], [11.19, 10.17, 9.97, 9.57, 9.26, 8.99], [11.18, 10.11, 10.17, 9.21, 9.35, 8.71], [11.4, 10.27, 10.1, 9.48, 9.23, 8.8]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 8.88), ('CB', 'HIS', 'CG', 'HIS', 7.93), ('CB', 'HIS', 'ND1', 'HIS', 7.89), ('CB', 'HIS', 'CD2', 'HIS', 7.37), ('CB', 'HIS', 'CE1', 'HIS', 7.34), ('CB', 'HIS', 'NE2', 'HIS', 6.97)], [('CG', 'HIS', 'CB', 'HIS', 8.17), ('CG', 'HIS', 'CG', 'HIS', 7.15), ('CG', 'HIS', 'ND1', 'HIS', 6.84), ('CG', 'HIS', 'CD2', 'HIS', 6.84), ('CG', 'HIS', 'CE1', 'HIS', 6.32), ('CG', 'HIS', 'NE2', 'HIS', 6.3)], [('ND1', 'HIS', 'CB', 'HIS', 7.75), ('ND1', 'HIS', 'CG', 'HIS', 6.97), ('ND1', 'HIS', 'ND1', 'HIS', 6.63), ('ND1', 'HIS', 'CD2', 'HIS', 7.01), ('ND1', 'HIS', 'CE1', 'HIS', 6.49), ('ND1', 'HIS', 'NE2', 'HIS', 6.71)], [('CD2', 'HIS', 'CB', 'HIS', 8.22), ('CD2', 'HIS', 'CG', 'HIS', 7.0), ('CD2', 'HIS', 'ND1', 'HIS', 6.39), ('CD2', 'HIS', 'CD2', 'HIS', 6.69), ('CD2', 'HIS', 'CE1', 'HIS', 5.64), ('CD2', 'HIS', 'NE2', 'HIS', 5.83)], [('CE1', 'HIS', 'CB', 'HIS', 7.56), ('CE1', 'HIS', 'CG', 'HIS', 6.72), ('CE1', 'HIS', 'ND1', 'HIS', 6.05), ('CE1', 'HIS', 'CD2', 'HIS', 6.99), ('CE1', 'HIS', 'CE1', 'HIS', 5.97), ('CE1', 'HIS', 'NE2', 'HIS', 6.55)], [('NE2', 'HIS', 'CB', 'HIS', 7.86), ('NE2', 'HIS', 'CG', 'HIS', 6.75), ('NE2', 'HIS', 'ND1', 'HIS', 5.88), ('NE2', 'HIS', 'CD2', 'HIS', 6.82), ('NE2', 'HIS', 'CE1', 'HIS', 5.41), ('NE2', 'HIS', 'NE2', 'HIS', 6.05)], [('CB', 'HIS', 'CB', 'HIS', 10.83), ('CB', 'HIS', 'CG', 'HIS', 10.85), ('CB', 'HIS', 'ND1', 'HIS', 10.84), ('CB', 'HIS', 'CD2', 'HIS', 11.19), ('CB', 'HIS', 'CE1', 'HIS', 11.18), ('CB', 'HIS', 'NE2', 'HIS', 11.4)], [('CG', 'HIS', 'CB', 'HIS', 10.18), ('CG', 'HIS', 'CG', 'HIS', 9.99), ('CG', 'HIS', 'ND1', 'HIS', 9.95), ('CG', 'HIS', 'CD2', 'HIS', 10.17), ('CG', 'HIS', 'CE1', 'HIS', 10.11), ('CG', 'HIS', 'NE2', 'HIS', 10.27)], [('ND1', 'HIS', 'CB', 'HIS', 10.25), ('ND1', 'HIS', 'CG', 'HIS', 10.0), ('ND1', 'HIS', 'ND1', 'HIS', 10.12), ('ND1', 'HIS', 'CD2', 'HIS', 9.97), ('ND1', 'HIS', 'CE1', 'HIS', 10.17), ('ND1', 'HIS', 'NE2', 'HIS', 10.1)], [('CD2', 'HIS', 'CB', 'HIS', 9.78), ('CD2', 'HIS', 'CG', 'HIS', 9.39), ('CD2', 'HIS', 'ND1', 'HIS', 9.16), ('CD2', 'HIS', 'CD2', 'HIS', 9.57), ('CD2', 'HIS', 'CE1', 'HIS', 9.21), ('CD2', 'HIS', 'NE2', 'HIS', 9.48)], [('CE1', 'HIS', 'CB', 'HIS', 9.92), ('CE1', 'HIS', 'CG', 'HIS', 9.44), ('CE1', 'HIS', 'ND1', 'HIS', 9.49), ('CE1', 'HIS', 'CD2', 'HIS', 9.26), ('CE1', 'HIS', 'CE1', 'HIS', 9.35), ('CE1', 'HIS', 'NE2', 'HIS', 9.23)], [('NE2', 'HIS', 'CB', 'HIS', 9.63), ('NE2', 'HIS', 'CG', 'HIS', 9.06), ('NE2', 'HIS', 'ND1', 'HIS', 8.88), ('NE2', 'HIS', 'CD2', 'HIS', 8.99), ('NE2', 'HIS', 'CE1', 'HIS', 8.71), ('NE2', 'HIS', 'NE2', 'HIS', 8.8)], [('CB', 'HIS', 'CB', 'HIS', 8.88), ('CB', 'HIS', 'CG', 'HIS', 8.17), ('CB', 'HIS', 'ND1', 'HIS', 7.75), ('CB', 'HIS', 'CD2', 'HIS', 8.22), ('CB', 'HIS', 'CE1', 'HIS', 7.56), ('CB', 'HIS', 'NE2', 'HIS', 7.86)], [('CG', 'HIS', 'CB', 'HIS', 7.93), ('CG', 'HIS', 'CG', 'HIS', 7.15), ('CG', 'HIS', 'ND1', 'HIS', 6.97), ('CG', 'HIS', 'CD2', 'HIS', 7.0), ('CG', 'HIS', 'CE1', 'HIS', 6.72), ('CG', 'HIS', 'NE2', 'HIS', 6.75)], [('ND1', 'HIS', 'CB', 'HIS', 7.89), ('ND1', 'HIS', 'CG', 'HIS', 6.84), ('ND1', 'HIS', 'ND1', 'HIS', 6.63), ('ND1', 'HIS', 'CD2', 'HIS', 6.39), ('ND1', 'HIS', 'CE1', 'HIS', 6.05), ('ND1', 'HIS', 'NE2', 'HIS', 5.88)], [('CD2', 'HIS', 'CB', 'HIS', 7.37), ('CD2', 'HIS', 'CG', 'HIS', 6.84), ('CD2', 'HIS', 'ND1', 'HIS', 7.01), ('CD2', 'HIS', 'CD2', 'HIS', 6.69), ('CD2', 'HIS', 'CE1', 'HIS', 6.99), ('CD2', 'HIS', 'NE2', 'HIS', 6.82)], [('CE1', 'HIS', 'CB', 'HIS', 7.34), ('CE1', 'HIS', 'CG', 'HIS', 6.32), ('CE1', 'HIS', 'ND1', 'HIS', 6.49), ('CE1', 'HIS', 'CD2', 'HIS', 5.64), ('CE1', 'HIS', 'CE1', 'HIS', 5.97), ('CE1', 'HIS', 'NE2', 'HIS', 5.41)], [('NE2', 'HIS', 'CB', 'HIS', 6.97), ('NE2', 'HIS', 'CG', 'HIS', 6.3), ('NE2', 'HIS', 'ND1', 'HIS', 6.71), ('NE2', 'HIS', 'CD2', 'HIS', 5.83), ('NE2', 'HIS', 'CE1', 'HIS', 6.55), ('NE2', 'HIS', 'NE2', 'HIS', 6.05)], [('CB', 'HIS', 'CB', 'HIS', 5.61), ('CB', 'HIS', 'CG', 'HIS', 5.85), ('CB', 'HIS', 'ND1', 'HIS', 6.88), ('CB', 'HIS', 'CD2', 'HIS', 5.81), ('CB', 'HIS', 'CE1', 'HIS', 7.37), ('CB', 'HIS', 'NE2', 'HIS', 6.83)], [('CG', 'HIS', 'CB', 'HIS', 5.41), ('CG', 'HIS', 'CG', 'HIS', 5.43), ('CG', 'HIS', 'ND1', 'HIS', 6.1), ('CG', 'HIS', 'CD2', 'HIS', 5.62), ('CG', 'HIS', 'CE1', 'HIS', 6.6), ('CG', 'HIS', 'NE2', 'HIS', 6.37)], [('ND1', 'HIS', 'CB', 'HIS', 5.95), ('ND1', 'HIS', 'CG', 'HIS', 5.43), ('ND1', 'HIS', 'ND1', 'HIS', 5.76), ('ND1', 'HIS', 'CD2', 'HIS', 5.37), ('ND1', 'HIS', 'CE1', 'HIS', 5.9), ('ND1', 'HIS', 'NE2', 'HIS', 5.7)], [('CD2', 'HIS', 'CB', 'HIS', 5.48), ('CD2', 'HIS', 'CG', 'HIS', 5.76), ('CD2', 'HIS', 'ND1', 'HIS', 6.19), ('CD2', 'HIS', 'CD2', 'HIS', 6.37), ('CD2', 'HIS', 'CE1', 'HIS', 6.94), ('CD2', 'HIS', 'NE2', 'HIS', 7.05)], [('CE1', 'HIS', 'CB', 'HIS', 6.29), ('CE1', 'HIS', 'CG', 'HIS', 5.76), ('CE1', 'HIS', 'ND1', 'HIS', 5.65), ('CE1', 'HIS', 'CD2', 'HIS', 6.02), ('CE1', 'HIS', 'CE1', 'HIS', 5.87), ('CE1', 'HIS', 'NE2', 'HIS', 6.1)], [('NE2', 'HIS', 'CB', 'HIS', 6.05), ('NE2', 'HIS', 'CG', 'HIS', 5.97), ('NE2', 'HIS', 'ND1', 'HIS', 5.94), ('NE2', 'HIS', 'CD2', 'HIS', 6.59), ('NE2', 'HIS', 'CE1', 'HIS', 6.55), ('NE2', 'HIS', 'NE2', 'HIS', 6.92)], [('CB', 'HIS', 'CB', 'HIS', 10.83), ('CB', 'HIS', 'CG', 'HIS', 10.18), ('CB', 'HIS', 'ND1', 'HIS', 10.25), ('CB', 'HIS', 'CD2', 'HIS', 9.78), ('CB', 'HIS', 'CE1', 'HIS', 9.92), ('CB', 'HIS', 'NE2', 'HIS', 9.63)], [('CG', 'HIS', 'CB', 'HIS', 10.85), ('CG', 'HIS', 'CG', 'HIS', 9.99), ('CG', 'HIS', 'ND1', 'HIS', 10.0), ('CG', 'HIS', 'CD2', 'HIS', 9.39), ('CG', 'HIS', 'CE1', 'HIS', 9.44), ('CG', 'HIS', 'NE2', 'HIS', 9.06)], [('ND1', 'HIS', 'CB', 'HIS', 10.84), ('ND1', 'HIS', 'CG', 'HIS', 9.95), ('ND1', 'HIS', 'ND1', 'HIS', 10.12), ('ND1', 'HIS', 'CD2', 'HIS', 9.16), ('ND1', 'HIS', 'CE1', 'HIS', 9.49), ('ND1', 'HIS', 'NE2', 'HIS', 8.88)], [('CD2', 'HIS', 'CB', 'HIS', 11.19), ('CD2', 'HIS', 'CG', 'HIS', 10.17), ('CD2', 'HIS', 'ND1', 'HIS', 9.97), ('CD2', 'HIS', 'CD2', 'HIS', 9.57), ('CD2', 'HIS', 'CE1', 'HIS', 9.26), ('CD2', 'HIS', 'NE2', 'HIS', 8.99)], [('CE1', 'HIS', 'CB', 'HIS', 11.18), ('CE1', 'HIS', 'CG', 'HIS', 10.11), ('CE1', 'HIS', 'ND1', 'HIS', 10.17), ('CE1', 'HIS', 'CD2', 'HIS', 9.21), ('CE1', 'HIS', 'CE1', 'HIS', 9.35), ('CE1', 'HIS', 'NE2', 'HIS', 8.71)], [('NE2', 'HIS', 'CB', 'HIS', 11.4), ('NE2', 'HIS', 'CG', 'HIS', 10.27), ('NE2', 'HIS', 'ND1', 'HIS', 10.1), ('NE2', 'HIS', 'CD2', 'HIS', 9.48), ('NE2', 'HIS', 'CE1', 'HIS', 9.23), ('NE2', 'HIS', 'NE2', 'HIS', 8.8)]]}
HIS_HISI = { 
	'distances':
		[[5.61, 5.41, 5.95, 5.48, 6.29, 6.05], [5.85, 5.43, 5.43, 5.76, 5.76, 5.97], [6.88, 6.1, 5.76, 6.19, 5.65, 5.94], [5.81, 5.62, 5.37, 6.37, 6.02, 6.59], [7.37, 6.6, 5.9, 6.94, 5.87, 6.55], [6.83, 6.37, 5.7, 7.05, 6.1, 6.92]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HISI', 5.61), ('CB', 'HIS', 'CG', 'HISI', 5.41), ('CB', 'HIS', 'ND1', 'HISI', 5.95), ('CB', 'HIS', 'CD2', 'HISI', 5.48), ('CB', 'HIS', 'CE1', 'HISI', 6.29), ('CB', 'HIS', 'NE2', 'HISI', 6.05)], [('CG', 'HIS', 'CB', 'HISI', 5.85), ('CG', 'HIS', 'CG', 'HISI', 5.43), ('CG', 'HIS', 'ND1', 'HISI', 5.43), ('CG', 'HIS', 'CD2', 'HISI', 5.76), ('CG', 'HIS', 'CE1', 'HISI', 5.76), ('CG', 'HIS', 'NE2', 'HISI', 5.97)], [('ND1', 'HIS', 'CB', 'HISI', 6.88), ('ND1', 'HIS', 'CG', 'HISI', 6.1), ('ND1', 'HIS', 'ND1', 'HISI', 5.76), ('ND1', 'HIS', 'CD2', 'HISI', 6.19), ('ND1', 'HIS', 'CE1', 'HISI', 5.65), ('ND1', 'HIS', 'NE2', 'HISI', 5.94)], [('CD2', 'HIS', 'CB', 'HISI', 5.81), ('CD2', 'HIS', 'CG', 'HISI', 5.62), ('CD2', 'HIS', 'ND1', 'HISI', 5.37), ('CD2', 'HIS', 'CD2', 'HISI', 6.37), ('CD2', 'HIS', 'CE1', 'HISI', 6.02), ('CD2', 'HIS', 'NE2', 'HISI', 6.59)], [('CE1', 'HIS', 'CB', 'HISI', 7.37), ('CE1', 'HIS', 'CG', 'HISI', 6.6), ('CE1', 'HIS', 'ND1', 'HISI', 5.9), ('CE1', 'HIS', 'CD2', 'HISI', 6.94), ('CE1', 'HIS', 'CE1', 'HISI', 5.87), ('CE1', 'HIS', 'NE2', 'HISI', 6.55)], [('NE2', 'HIS', 'CB', 'HISI', 6.83), ('NE2', 'HIS', 'CG', 'HISI', 6.37), ('NE2', 'HIS', 'ND1', 'HISI', 5.7), ('NE2', 'HIS', 'CD2', 'HISI', 7.05), ('NE2', 'HIS', 'CE1', 'HISI', 6.1), ('NE2', 'HIS', 'NE2', 'HISI', 6.92)]]}
ZN_HISII = { 
	'distances':
		[20.68, 19.95, 20.59, 18.72, 19.8, 18.64],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'HISII', 20.68), ('ZN', 'ZN', 'CG', 'HISII', 19.95), ('ZN', 'ZN', 'ND1', 'HISII', 20.59), ('ZN', 'ZN', 'CD2', 'HISII', 18.72), ('ZN', 'ZN', 'CE1', 'HISII', 19.8), ('ZN', 'ZN', 'NE2', 'HISII', 18.64)]}
ZN_HISI = { 
	'distances':
		[18.08, 18.73, 18.28, 20.0, 19.31, 20.32],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'HISI', 18.08), ('ZN', 'ZN', 'CG', 'HISI', 18.73), ('ZN', 'ZN', 'ND1', 'HISI', 18.28), ('ZN', 'ZN', 'CD2', 'HISI', 20.0), ('ZN', 'ZN', 'CE1', 'HISI', 19.31), ('ZN', 'ZN', 'NE2', 'HISI', 20.32)]}
GLU_ZN = { 
	'distances':
		[[11.08], [12.07], [11.94], [11.32], [12.76]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 11.08)], [('CG', 'GLU', 'ZN', 'ZN', 12.07)], [('CD', 'GLU', 'ZN', 'ZN', 11.94)], [('OE1', 'GLU', 'ZN', 'ZN', 11.32)], [('OE2', 'GLU', 'ZN', 'ZN', 12.76)]]}
HIS_GLU = { 
	'distances':
		[[12.93, 11.75, 11.15, 11.37, 10.58], [12.12, 11.04, 10.36, 10.42, 9.92], [10.83, 9.74, 9.0, 9.04, 8.56], [12.57, 11.63, 10.92, 10.81, 10.62], [10.56, 9.63, 8.82, 8.64, 8.57], [11.64, 10.79, 10.02, 9.77, 9.84], [13.6, 12.59, 11.22, 10.83, 10.62], [13.76, 12.76, 11.49, 11.1, 10.96], [13.29, 12.41, 11.19, 10.7, 10.83], [14.61, 13.56, 12.37, 12.08, 11.79], [13.92, 13.03, 11.93, 11.49, 11.58], [14.69, 13.7, 12.6, 12.28, 12.13], [16.83, 15.93, 14.58, 14.06, 14.1], [16.28, 15.49, 14.16, 13.53, 13.81], [16.7, 15.96, 14.71, 14.06, 14.43], [15.46, 14.77, 13.42, 12.69, 13.16], [16.19, 15.56, 14.34, 13.6, 14.19], [15.44, 14.85, 13.57, 12.77, 13.44]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 12.93), ('CB', 'HIS', 'CG', 'GLU', 11.75), ('CB', 'HIS', 'CD', 'GLU', 11.15), ('CB', 'HIS', 'OE1', 'GLU', 11.37), ('CB', 'HIS', 'OE2', 'GLU', 10.58)], [('CG', 'HIS', 'CB', 'GLU', 12.12), ('CG', 'HIS', 'CG', 'GLU', 11.04), ('CG', 'HIS', 'CD', 'GLU', 10.36), ('CG', 'HIS', 'OE1', 'GLU', 10.42), ('CG', 'HIS', 'OE2', 'GLU', 9.92)], [('ND1', 'HIS', 'CB', 'GLU', 10.83), ('ND1', 'HIS', 'CG', 'GLU', 9.74), ('ND1', 'HIS', 'CD', 'GLU', 9.0), ('ND1', 'HIS', 'OE1', 'GLU', 9.04), ('ND1', 'HIS', 'OE2', 'GLU', 8.56)], [('CD2', 'HIS', 'CB', 'GLU', 12.57), ('CD2', 'HIS', 'CG', 'GLU', 11.63), ('CD2', 'HIS', 'CD', 'GLU', 10.92), ('CD2', 'HIS', 'OE1', 'GLU', 10.81), ('CD2', 'HIS', 'OE2', 'GLU', 10.62)], [('CE1', 'HIS', 'CB', 'GLU', 10.56), ('CE1', 'HIS', 'CG', 'GLU', 9.63), ('CE1', 'HIS', 'CD', 'GLU', 8.82), ('CE1', 'HIS', 'OE1', 'GLU', 8.64), ('CE1', 'HIS', 'OE2', 'GLU', 8.57)], [('NE2', 'HIS', 'CB', 'GLU', 11.64), ('NE2', 'HIS', 'CG', 'GLU', 10.79), ('NE2', 'HIS', 'CD', 'GLU', 10.02), ('NE2', 'HIS', 'OE1', 'GLU', 9.77), ('NE2', 'HIS', 'OE2', 'GLU', 9.84)], [('CB', 'HIS', 'CB', 'GLU', 13.6), ('CB', 'HIS', 'CG', 'GLU', 12.59), ('CB', 'HIS', 'CD', 'GLU', 11.22), ('CB', 'HIS', 'OE1', 'GLU', 10.83), ('CB', 'HIS', 'OE2', 'GLU', 10.62)], [('CG', 'HIS', 'CB', 'GLU', 13.76), ('CG', 'HIS', 'CG', 'GLU', 12.76), ('CG', 'HIS', 'CD', 'GLU', 11.49), ('CG', 'HIS', 'OE1', 'GLU', 11.1), ('CG', 'HIS', 'OE2', 'GLU', 10.96)], [('ND1', 'HIS', 'CB', 'GLU', 13.29), ('ND1', 'HIS', 'CG', 'GLU', 12.41), ('ND1', 'HIS', 'CD', 'GLU', 11.19), ('ND1', 'HIS', 'OE1', 'GLU', 10.7), ('ND1', 'HIS', 'OE2', 'GLU', 10.83)], [('CD2', 'HIS', 'CB', 'GLU', 14.61), ('CD2', 'HIS', 'CG', 'GLU', 13.56), ('CD2', 'HIS', 'CD', 'GLU', 12.37), ('CD2', 'HIS', 'OE1', 'GLU', 12.08), ('CD2', 'HIS', 'OE2', 'GLU', 11.79)], [('CE1', 'HIS', 'CB', 'GLU', 13.92), ('CE1', 'HIS', 'CG', 'GLU', 13.03), ('CE1', 'HIS', 'CD', 'GLU', 11.93), ('CE1', 'HIS', 'OE1', 'GLU', 11.49), ('CE1', 'HIS', 'OE2', 'GLU', 11.58)], [('NE2', 'HIS', 'CB', 'GLU', 14.69), ('NE2', 'HIS', 'CG', 'GLU', 13.7), ('NE2', 'HIS', 'CD', 'GLU', 12.6), ('NE2', 'HIS', 'OE1', 'GLU', 12.28), ('NE2', 'HIS', 'OE2', 'GLU', 12.13)], [('CB', 'HIS', 'CB', 'GLU', 16.83), ('CB', 'HIS', 'CG', 'GLU', 15.93), ('CB', 'HIS', 'CD', 'GLU', 14.58), ('CB', 'HIS', 'OE1', 'GLU', 14.06), ('CB', 'HIS', 'OE2', 'GLU', 14.1)], [('CG', 'HIS', 'CB', 'GLU', 16.28), ('CG', 'HIS', 'CG', 'GLU', 15.49), ('CG', 'HIS', 'CD', 'GLU', 14.16), ('CG', 'HIS', 'OE1', 'GLU', 13.53), ('CG', 'HIS', 'OE2', 'GLU', 13.81)], [('ND1', 'HIS', 'CB', 'GLU', 16.7), ('ND1', 'HIS', 'CG', 'GLU', 15.96), ('ND1', 'HIS', 'CD', 'GLU', 14.71), ('ND1', 'HIS', 'OE1', 'GLU', 14.06), ('ND1', 'HIS', 'OE2', 'GLU', 14.43)], [('CD2', 'HIS', 'CB', 'GLU', 15.46), ('CD2', 'HIS', 'CG', 'GLU', 14.77), ('CD2', 'HIS', 'CD', 'GLU', 13.42), ('CD2', 'HIS', 'OE1', 'GLU', 12.69), ('CD2', 'HIS', 'OE2', 'GLU', 13.16)], [('CE1', 'HIS', 'CB', 'GLU', 16.19), ('CE1', 'HIS', 'CG', 'GLU', 15.56), ('CE1', 'HIS', 'CD', 'GLU', 14.34), ('CE1', 'HIS', 'OE1', 'GLU', 13.6), ('CE1', 'HIS', 'OE2', 'GLU', 14.19)], [('NE2', 'HIS', 'CB', 'GLU', 15.44), ('NE2', 'HIS', 'CG', 'GLU', 14.85), ('NE2', 'HIS', 'CD', 'GLU', 13.57), ('NE2', 'HIS', 'OE1', 'GLU', 12.77), ('NE2', 'HIS', 'OE2', 'GLU', 13.44)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ZN, d, 'M_1e7l_3_1_22_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_HIS, d, 'M_1e7l_3_1_22_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_HISI, d, 'M_1e7l_3_1_22_4')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ZN_HISII, d, 'M_1e7l_3_1_22_4')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ZN_HISI, d, 'M_1e7l_3_1_22_4')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_ZN, d, 'M_1e7l_3_1_22_4')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_GLU, d, 'M_1e7l_3_1_22_4')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ZN' :  match1,
		'HIS_HIS' :  match2,
		'HIS_HISI' :  match3,
		'ZN_HISII' :  match4,
		'ZN_HISI' :  match5,
		'GLU_ZN' :  match6,
		'HIS_GLU' :  match7}