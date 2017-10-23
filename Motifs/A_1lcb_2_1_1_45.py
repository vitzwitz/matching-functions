'''
FUNC:A_1lcb_2_1_1_45
PDB:1lcb
EC:2.1.1.45
RESI:glu,cys,ser,asp,asp,his
LOCI:a-60,198,219,221,257,259;
'''
import motifFunctions as cmd
ASP_ASP = { 
	'distances':
		[[11.41, 10.93, 10.26, 11.47], [12.67, 12.04, 11.28, 12.53], [12.75, 12.02, 11.14, 12.52], [13.69, 13.08, 12.37, 13.51], [11.41, 12.67, 12.75, 13.69], [10.93, 12.04, 12.02, 13.08], [10.26, 11.28, 11.14, 12.37], [11.47, 12.53, 12.52, 13.51]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 11.41), ('CB', 'ASP', 'CG', 'ASP', 10.93), ('CB', 'ASP', 'OD1', 'ASP', 10.26), ('CB', 'ASP', 'OD2', 'ASP', 11.47)], [('CG', 'ASP', 'CB', 'ASP', 12.67), ('CG', 'ASP', 'CG', 'ASP', 12.04), ('CG', 'ASP', 'OD1', 'ASP', 11.28), ('CG', 'ASP', 'OD2', 'ASP', 12.53)], [('OD1', 'ASP', 'CB', 'ASP', 12.75), ('OD1', 'ASP', 'CG', 'ASP', 12.02), ('OD1', 'ASP', 'OD1', 'ASP', 11.14), ('OD1', 'ASP', 'OD2', 'ASP', 12.52)], [('OD2', 'ASP', 'CB', 'ASP', 13.69), ('OD2', 'ASP', 'CG', 'ASP', 13.08), ('OD2', 'ASP', 'OD1', 'ASP', 12.37), ('OD2', 'ASP', 'OD2', 'ASP', 13.51)], [('CB', 'ASP', 'CB', 'ASP', 11.41), ('CB', 'ASP', 'CG', 'ASP', 12.67), ('CB', 'ASP', 'OD1', 'ASP', 12.75), ('CB', 'ASP', 'OD2', 'ASP', 13.69)], [('CG', 'ASP', 'CB', 'ASP', 10.93), ('CG', 'ASP', 'CG', 'ASP', 12.04), ('CG', 'ASP', 'OD1', 'ASP', 12.02), ('CG', 'ASP', 'OD2', 'ASP', 13.08)], [('OD1', 'ASP', 'CB', 'ASP', 10.26), ('OD1', 'ASP', 'CG', 'ASP', 11.28), ('OD1', 'ASP', 'OD1', 'ASP', 11.14), ('OD1', 'ASP', 'OD2', 'ASP', 12.37)], [('OD2', 'ASP', 'CB', 'ASP', 11.47), ('OD2', 'ASP', 'CG', 'ASP', 12.53), ('OD2', 'ASP', 'OD1', 'ASP', 12.52), ('OD2', 'ASP', 'OD2', 'ASP', 13.51)]]}
HIS_ASPI = { 
	'distances':
		[[7.46, 6.47, 5.32, 7.15], [7.62, 6.69, 5.78, 7.24], [6.93, 6.23, 5.61, 6.77], [8.85, 7.85, 6.98, 8.22], [7.85, 7.17, 6.7, 7.51], [8.89, 8.01, 7.37, 8.3]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASPI', 7.46), ('CB', 'HIS', 'CG', 'ASPI', 6.47), ('CB', 'HIS', 'OD1', 'ASPI', 5.32), ('CB', 'HIS', 'OD2', 'ASPI', 7.15)], [('CG', 'HIS', 'CB', 'ASPI', 7.62), ('CG', 'HIS', 'CG', 'ASPI', 6.69), ('CG', 'HIS', 'OD1', 'ASPI', 5.78), ('CG', 'HIS', 'OD2', 'ASPI', 7.24)], [('ND1', 'HIS', 'CB', 'ASPI', 6.93), ('ND1', 'HIS', 'CG', 'ASPI', 6.23), ('ND1', 'HIS', 'OD1', 'ASPI', 5.61), ('ND1', 'HIS', 'OD2', 'ASPI', 6.77)], [('CD2', 'HIS', 'CB', 'ASPI', 8.85), ('CD2', 'HIS', 'CG', 'ASPI', 7.85), ('CD2', 'HIS', 'OD1', 'ASPI', 6.98), ('CD2', 'HIS', 'OD2', 'ASPI', 8.22)], [('CE1', 'HIS', 'CB', 'ASPI', 7.85), ('CE1', 'HIS', 'CG', 'ASPI', 7.17), ('CE1', 'HIS', 'OD1', 'ASPI', 6.7), ('CE1', 'HIS', 'OD2', 'ASPI', 7.51)], [('NE2', 'HIS', 'CB', 'ASPI', 8.89), ('NE2', 'HIS', 'CG', 'ASPI', 8.01), ('NE2', 'HIS', 'OD1', 'ASPI', 7.37), ('NE2', 'HIS', 'OD2', 'ASPI', 8.3)]]}
HIS_GLU = { 
	'distances':
		[[23.38, 22.25, 20.91, 20.28, 20.6], [22.2, 21.06, 19.7, 19.12, 19.32], [21.51, 20.31, 18.98, 18.46, 18.59], [21.85, 20.75, 19.34, 18.77, 18.92], [20.73, 19.54, 18.19, 17.71, 17.72], [20.97, 19.84, 18.44, 17.93, 17.96]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 23.38), ('CB', 'HIS', 'CG', 'GLU', 22.25), ('CB', 'HIS', 'CD', 'GLU', 20.91), ('CB', 'HIS', 'OE1', 'GLU', 20.28), ('CB', 'HIS', 'OE2', 'GLU', 20.6)], [('CG', 'HIS', 'CB', 'GLU', 22.2), ('CG', 'HIS', 'CG', 'GLU', 21.06), ('CG', 'HIS', 'CD', 'GLU', 19.7), ('CG', 'HIS', 'OE1', 'GLU', 19.12), ('CG', 'HIS', 'OE2', 'GLU', 19.32)], [('ND1', 'HIS', 'CB', 'GLU', 21.51), ('ND1', 'HIS', 'CG', 'GLU', 20.31), ('ND1', 'HIS', 'CD', 'GLU', 18.98), ('ND1', 'HIS', 'OE1', 'GLU', 18.46), ('ND1', 'HIS', 'OE2', 'GLU', 18.59)], [('CD2', 'HIS', 'CB', 'GLU', 21.85), ('CD2', 'HIS', 'CG', 'GLU', 20.75), ('CD2', 'HIS', 'CD', 'GLU', 19.34), ('CD2', 'HIS', 'OE1', 'GLU', 18.77), ('CD2', 'HIS', 'OE2', 'GLU', 18.92)], [('CE1', 'HIS', 'CB', 'GLU', 20.73), ('CE1', 'HIS', 'CG', 'GLU', 19.54), ('CE1', 'HIS', 'CD', 'GLU', 18.19), ('CE1', 'HIS', 'OE1', 'GLU', 17.71), ('CE1', 'HIS', 'OE2', 'GLU', 17.72)], [('NE2', 'HIS', 'CB', 'GLU', 20.97), ('NE2', 'HIS', 'CG', 'GLU', 19.84), ('NE2', 'HIS', 'CD', 'GLU', 18.44), ('NE2', 'HIS', 'OE1', 'GLU', 17.93), ('NE2', 'HIS', 'OE2', 'GLU', 17.96)]]}
SER_GLU = { 
	'distances':
		[[19.33, 17.92, 16.82, 16.57, 16.36], [19.04, 17.68, 16.49, 16.21, 15.99]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 19.33), ('CB', 'SER', 'CG', 'GLU', 17.92), ('CB', 'SER', 'CD', 'GLU', 16.82), ('CB', 'SER', 'OE1', 'GLU', 16.57), ('CB', 'SER', 'OE2', 'GLU', 16.36)], [('OG', 'SER', 'CB', 'GLU', 19.04), ('OG', 'SER', 'CG', 'GLU', 17.68), ('OG', 'SER', 'CD', 'GLU', 16.49), ('OG', 'SER', 'OE1', 'GLU', 16.21), ('OG', 'SER', 'OE2', 'GLU', 15.99)]]}
ASP_HIS = { 
	'distances':
		[[7.91, 6.73, 6.72, 6.04, 6.08, 5.59], [8.63, 7.57, 7.83, 6.62, 7.18, 6.37], [8.22, 7.37, 7.91, 6.39, 7.45, 6.48], [9.81, 8.68, 8.85, 7.67, 8.06, 7.27], [7.46, 7.62, 6.93, 8.85, 7.85, 8.89], [6.47, 6.69, 6.23, 7.85, 7.17, 8.01], [5.32, 5.78, 5.61, 6.98, 6.7, 7.37], [7.15, 7.24, 6.77, 8.22, 7.51, 8.3]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.91), ('CB', 'ASP', 'CG', 'HIS', 6.73), ('CB', 'ASP', 'ND1', 'HIS', 6.72), ('CB', 'ASP', 'CD2', 'HIS', 6.04), ('CB', 'ASP', 'CE1', 'HIS', 6.08), ('CB', 'ASP', 'NE2', 'HIS', 5.59)], [('CG', 'ASP', 'CB', 'HIS', 8.63), ('CG', 'ASP', 'CG', 'HIS', 7.57), ('CG', 'ASP', 'ND1', 'HIS', 7.83), ('CG', 'ASP', 'CD2', 'HIS', 6.62), ('CG', 'ASP', 'CE1', 'HIS', 7.18), ('CG', 'ASP', 'NE2', 'HIS', 6.37)], [('OD1', 'ASP', 'CB', 'HIS', 8.22), ('OD1', 'ASP', 'CG', 'HIS', 7.37), ('OD1', 'ASP', 'ND1', 'HIS', 7.91), ('OD1', 'ASP', 'CD2', 'HIS', 6.39), ('OD1', 'ASP', 'CE1', 'HIS', 7.45), ('OD1', 'ASP', 'NE2', 'HIS', 6.48)], [('OD2', 'ASP', 'CB', 'HIS', 9.81), ('OD2', 'ASP', 'CG', 'HIS', 8.68), ('OD2', 'ASP', 'ND1', 'HIS', 8.85), ('OD2', 'ASP', 'CD2', 'HIS', 7.67), ('OD2', 'ASP', 'CE1', 'HIS', 8.06), ('OD2', 'ASP', 'NE2', 'HIS', 7.27)], [('CB', 'ASP', 'CB', 'HIS', 7.46), ('CB', 'ASP', 'CG', 'HIS', 7.62), ('CB', 'ASP', 'ND1', 'HIS', 6.93), ('CB', 'ASP', 'CD2', 'HIS', 8.85), ('CB', 'ASP', 'CE1', 'HIS', 7.85), ('CB', 'ASP', 'NE2', 'HIS', 8.89)], [('CG', 'ASP', 'CB', 'HIS', 6.47), ('CG', 'ASP', 'CG', 'HIS', 6.69), ('CG', 'ASP', 'ND1', 'HIS', 6.23), ('CG', 'ASP', 'CD2', 'HIS', 7.85), ('CG', 'ASP', 'CE1', 'HIS', 7.17), ('CG', 'ASP', 'NE2', 'HIS', 8.01)], [('OD1', 'ASP', 'CB', 'HIS', 5.32), ('OD1', 'ASP', 'CG', 'HIS', 5.78), ('OD1', 'ASP', 'ND1', 'HIS', 5.61), ('OD1', 'ASP', 'CD2', 'HIS', 6.98), ('OD1', 'ASP', 'CE1', 'HIS', 6.7), ('OD1', 'ASP', 'NE2', 'HIS', 7.37)], [('OD2', 'ASP', 'CB', 'HIS', 7.15), ('OD2', 'ASP', 'CG', 'HIS', 7.24), ('OD2', 'ASP', 'ND1', 'HIS', 6.77), ('OD2', 'ASP', 'CD2', 'HIS', 8.22), ('OD2', 'ASP', 'CE1', 'HIS', 7.51), ('OD2', 'ASP', 'NE2', 'HIS', 8.3)]]}
CYS_SER = { 
	'distances':
		[[6.78, 7.18], [5.5, 5.53]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'SER', 6.78), ('CB', 'CYS', 'OG', 'SER', 7.18)], [('SG', 'CYS', 'CB', 'SER', 5.5), ('SG', 'CYS', 'OG', 'SER', 5.53)]]}
GLU_ASPI = { 
	'distances':
		[[24.31, 24.72, 24.62, 25.28], [22.96, 23.41, 23.36, 23.95], [21.83, 22.21, 22.12, 22.74], [21.41, 21.77, 21.62, 22.35], [21.51, 21.83, 21.76, 22.3]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASPI', 24.31), ('CB', 'GLU', 'CG', 'ASPI', 24.72), ('CB', 'GLU', 'OD1', 'ASPI', 24.62), ('CB', 'GLU', 'OD2', 'ASPI', 25.28)], [('CG', 'GLU', 'CB', 'ASPI', 22.96), ('CG', 'GLU', 'CG', 'ASPI', 23.41), ('CG', 'GLU', 'OD1', 'ASPI', 23.36), ('CG', 'GLU', 'OD2', 'ASPI', 23.95)], [('CD', 'GLU', 'CB', 'ASPI', 21.83), ('CD', 'GLU', 'CG', 'ASPI', 22.21), ('CD', 'GLU', 'OD1', 'ASPI', 22.12), ('CD', 'GLU', 'OD2', 'ASPI', 22.74)], [('OE1', 'GLU', 'CB', 'ASPI', 21.41), ('OE1', 'GLU', 'CG', 'ASPI', 21.77), ('OE1', 'GLU', 'OD1', 'ASPI', 21.62), ('OE1', 'GLU', 'OD2', 'ASPI', 22.35)], [('OE2', 'GLU', 'CB', 'ASPI', 21.51), ('OE2', 'GLU', 'CG', 'ASPI', 21.83), ('OE2', 'GLU', 'OD1', 'ASPI', 21.76), ('OE2', 'GLU', 'OD2', 'ASPI', 22.3)]]}
ASP_GLU = { 
	'distances':
		[[18.07, 17.07, 15.63, 14.98, 15.26], [18.32, 17.44, 15.95, 15.27, 15.57], [19.37, 18.52, 17.04, 16.31, 16.69], [17.6, 16.77, 15.26, 14.6, 14.83], [24.31, 22.96, 21.83, 21.41, 21.51], [24.72, 23.41, 22.21, 21.77, 21.83], [24.62, 23.36, 22.12, 21.62, 21.76], [25.28, 23.95, 22.74, 22.35, 22.3]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 18.07), ('CB', 'ASP', 'CG', 'GLU', 17.07), ('CB', 'ASP', 'CD', 'GLU', 15.63), ('CB', 'ASP', 'OE1', 'GLU', 14.98), ('CB', 'ASP', 'OE2', 'GLU', 15.26)], [('CG', 'ASP', 'CB', 'GLU', 18.32), ('CG', 'ASP', 'CG', 'GLU', 17.44), ('CG', 'ASP', 'CD', 'GLU', 15.95), ('CG', 'ASP', 'OE1', 'GLU', 15.27), ('CG', 'ASP', 'OE2', 'GLU', 15.57)], [('OD1', 'ASP', 'CB', 'GLU', 19.37), ('OD1', 'ASP', 'CG', 'GLU', 18.52), ('OD1', 'ASP', 'CD', 'GLU', 17.04), ('OD1', 'ASP', 'OE1', 'GLU', 16.31), ('OD1', 'ASP', 'OE2', 'GLU', 16.69)], [('OD2', 'ASP', 'CB', 'GLU', 17.6), ('OD2', 'ASP', 'CG', 'GLU', 16.77), ('OD2', 'ASP', 'CD', 'GLU', 15.26), ('OD2', 'ASP', 'OE1', 'GLU', 14.6), ('OD2', 'ASP', 'OE2', 'GLU', 14.83)], [('CB', 'ASP', 'CB', 'GLU', 24.31), ('CB', 'ASP', 'CG', 'GLU', 22.96), ('CB', 'ASP', 'CD', 'GLU', 21.83), ('CB', 'ASP', 'OE1', 'GLU', 21.41), ('CB', 'ASP', 'OE2', 'GLU', 21.51)], [('CG', 'ASP', 'CB', 'GLU', 24.72), ('CG', 'ASP', 'CG', 'GLU', 23.41), ('CG', 'ASP', 'CD', 'GLU', 22.21), ('CG', 'ASP', 'OE1', 'GLU', 21.77), ('CG', 'ASP', 'OE2', 'GLU', 21.83)], [('OD1', 'ASP', 'CB', 'GLU', 24.62), ('OD1', 'ASP', 'CG', 'GLU', 23.36), ('OD1', 'ASP', 'CD', 'GLU', 22.12), ('OD1', 'ASP', 'OE1', 'GLU', 21.62), ('OD1', 'ASP', 'OE2', 'GLU', 21.76)], [('OD2', 'ASP', 'CB', 'GLU', 25.28), ('OD2', 'ASP', 'CG', 'GLU', 23.95), ('OD2', 'ASP', 'CD', 'GLU', 22.74), ('OD2', 'ASP', 'OE1', 'GLU', 22.35), ('OD2', 'ASP', 'OE2', 'GLU', 22.3)]]}
CYS_ASP = { 
	'distances':
		[[10.85, 12.16, 13.19, 12.29], [9.33, 10.64, 11.66, 10.82], [12.06, 12.74, 13.1, 13.14], [10.98, 11.45, 11.73, 11.79]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 10.85), ('CB', 'CYS', 'CG', 'ASP', 12.16), ('CB', 'CYS', 'OD1', 'ASP', 13.19), ('CB', 'CYS', 'OD2', 'ASP', 12.29)], [('SG', 'CYS', 'CB', 'ASP', 9.33), ('SG', 'CYS', 'CG', 'ASP', 10.64), ('SG', 'CYS', 'OD1', 'ASP', 11.66), ('SG', 'CYS', 'OD2', 'ASP', 10.82)], [('CB', 'CYS', 'CB', 'ASP', 12.06), ('CB', 'CYS', 'CG', 'ASP', 12.74), ('CB', 'CYS', 'OD1', 'ASP', 13.1), ('CB', 'CYS', 'OD2', 'ASP', 13.14)], [('SG', 'CYS', 'CB', 'ASP', 10.98), ('SG', 'CYS', 'CG', 'ASP', 11.45), ('SG', 'CYS', 'OD1', 'ASP', 11.73), ('SG', 'CYS', 'OD2', 'ASP', 11.79)]]}
SER_ASP = { 
	'distances':
		[[9.23, 10.68, 11.38, 11.25], [8.05, 9.43, 10.16, 9.97], [7.58, 8.07, 8.53, 8.37], [8.0, 8.15, 8.39, 8.41]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 9.23), ('CB', 'SER', 'CG', 'ASP', 10.68), ('CB', 'SER', 'OD1', 'ASP', 11.38), ('CB', 'SER', 'OD2', 'ASP', 11.25)], [('OG', 'SER', 'CB', 'ASP', 8.05), ('OG', 'SER', 'CG', 'ASP', 9.43), ('OG', 'SER', 'OD1', 'ASP', 10.16), ('OG', 'SER', 'OD2', 'ASP', 9.97)], [('CB', 'SER', 'CB', 'ASP', 7.58), ('CB', 'SER', 'CG', 'ASP', 8.07), ('CB', 'SER', 'OD1', 'ASP', 8.53), ('CB', 'SER', 'OD2', 'ASP', 8.37)], [('OG', 'SER', 'CB', 'ASP', 8.0), ('OG', 'SER', 'CG', 'ASP', 8.15), ('OG', 'SER', 'OD1', 'ASP', 8.39), ('OG', 'SER', 'OD2', 'ASP', 8.41)]]}
CYS_GLU = { 
	'distances':
		[[15.14, 13.65, 12.75, 12.69, 12.35], [15.95, 14.52, 13.45, 13.3, 12.96]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 15.14), ('CB', 'CYS', 'CG', 'GLU', 13.65), ('CB', 'CYS', 'CD', 'GLU', 12.75), ('CB', 'CYS', 'OE1', 'GLU', 12.69), ('CB', 'CYS', 'OE2', 'GLU', 12.35)], [('SG', 'CYS', 'CB', 'GLU', 15.95), ('SG', 'CYS', 'CG', 'GLU', 14.52), ('SG', 'CYS', 'CD', 'GLU', 13.45), ('SG', 'CYS', 'OE1', 'GLU', 13.3), ('SG', 'CYS', 'OE2', 'GLU', 12.96)]]}
CYS_HIS = { 
	'distances':
		[[13.4, 12.25, 11.02, 12.49, 10.47, 11.45], [11.88, 10.63, 9.41, 10.78, 8.75, 9.69]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 13.4), ('CB', 'CYS', 'CG', 'HIS', 12.25), ('CB', 'CYS', 'ND1', 'HIS', 11.02), ('CB', 'CYS', 'CD2', 'HIS', 12.49), ('CB', 'CYS', 'CE1', 'HIS', 10.47), ('CB', 'CYS', 'NE2', 'HIS', 11.45)], [('SG', 'CYS', 'CB', 'HIS', 11.88), ('SG', 'CYS', 'CG', 'HIS', 10.63), ('SG', 'CYS', 'ND1', 'HIS', 9.41), ('SG', 'CYS', 'CD2', 'HIS', 10.78), ('SG', 'CYS', 'CE1', 'HIS', 8.75), ('SG', 'CYS', 'NE2', 'HIS', 9.69)]]}
SER_HIS = { 
	'distances':
		[[9.48, 8.43, 7.09, 8.97, 6.81, 8.07], [8.82, 7.59, 6.28, 7.9, 5.71, 6.88]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.48), ('CB', 'SER', 'CG', 'HIS', 8.43), ('CB', 'SER', 'ND1', 'HIS', 7.09), ('CB', 'SER', 'CD2', 'HIS', 8.97), ('CB', 'SER', 'CE1', 'HIS', 6.81), ('CB', 'SER', 'NE2', 'HIS', 8.07)], [('OG', 'SER', 'CB', 'HIS', 8.82), ('OG', 'SER', 'CG', 'HIS', 7.59), ('OG', 'SER', 'ND1', 'HIS', 6.28), ('OG', 'SER', 'CD2', 'HIS', 7.9), ('OG', 'SER', 'CE1', 'HIS', 5.71), ('OG', 'SER', 'NE2', 'HIS', 6.88)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASP, d, 'A_1lcb_2_1_1_45')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASPI, d, 'A_1lcb_2_1_1_45')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_GLU, d, 'A_1lcb_2_1_1_45')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_GLU, d, 'A_1lcb_2_1_1_45')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_HIS, d, 'A_1lcb_2_1_1_45')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_SER, d, 'A_1lcb_2_1_1_45')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLU_ASPI, d, 'A_1lcb_2_1_1_45')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_GLU, d, 'A_1lcb_2_1_1_45')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(CYS_ASP, d, 'A_1lcb_2_1_1_45')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'A_1lcb_2_1_1_45')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(CYS_GLU, d, 'A_1lcb_2_1_1_45')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(CYS_HIS, d, 'A_1lcb_2_1_1_45')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(SER_HIS, d, 'A_1lcb_2_1_1_45')
	if match13 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASP' :  match1,
		'HIS_ASPI' :  match2,
		'HIS_GLU' :  match3,
		'SER_GLU' :  match4,
		'ASP_HIS' :  match5,
		'CYS_SER' :  match6,
		'GLU_ASPI' :  match7,
		'ASP_GLU' :  match8,
		'CYS_ASP' :  match9,
		'SER_ASP' :  match10,
		'CYS_GLU' :  match11,
		'CYS_HIS' :  match12,
		'SER_HIS' :  match13}