'''
FUNC:M_1gog_1_1_3_9
PDB:1gog
EC:1.1.3.9
RESI:cys,tyr,trp,tyr,cu
LOCI:a-228,272,290,495,700;
'''
import motifFunctions as cmd
CU_TYRI = { 
	'distances':
		[8.96, 7.49, 6.88, 7.09, 5.59, 5.87, 4.94, 3.91],
	'comparisons':
		[('CU', 'CU', 'CB', 'TYRI', 8.96), ('CU', 'CU', 'CG', 'TYRI', 7.49), ('CU', 'CU', 'CD1', 'TYRI', 6.88), ('CU', 'CU', 'CD2', 'TYRI', 7.09), ('CU', 'CU', 'CE1', 'TYRI', 5.59), ('CU', 'CU', 'CE2', 'TYRI', 5.87), ('CU', 'CU', 'CZ', 'TYRI', 4.94), ('CU', 'CU', 'OH', 'TYRI', 3.91)]}
TRP_CU = { 
	'distances':
		[[9.28], [8.28], [7.78], [8.1], [7.26], [7.44], [8.81], [7.54], [8.85], [8.28]],
	'comparisons':
		[[('CB', 'TRP', 'CU', 'CU', 9.28)], [('CG', 'TRP', 'CU', 'CU', 8.28)], [('CD1', 'TRP', 'CU', 'CU', 7.78)], [('CD2', 'TRP', 'CU', 'CU', 8.1)], [('NE1', 'TRP', 'CU', 'CU', 7.26)], [('CE2', 'TRP', 'CU', 'CU', 7.44)], [('CE3', 'TRP', 'CU', 'CU', 8.81)], [('CZ2', 'TRP', 'CU', 'CU', 7.54)], [('CZ3', 'TRP', 'CU', 'CU', 8.85)], [('CH2', 'TRP', 'CU', 'CU', 8.28)]]}
TYR_CYS = { 
	'distances':
		[[14.07, 12.4], [12.67, 10.97], [12.29, 10.65], [12.02, 10.27], [11.13, 9.49], [10.79, 9.02], [10.34, 8.61], [9.29, 7.56], [7.3, 7.34], [6.46, 6.1], [5.08, 4.83], [7.41, 6.6], [4.84, 3.78], [7.32, 6.09], [6.17, 4.75], [6.58, 4.85]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'CYS', 14.07), ('CB', 'TYR', 'SG', 'CYS', 12.4)], [('CG', 'TYR', 'CB', 'CYS', 12.67), ('CG', 'TYR', 'SG', 'CYS', 10.97)], [('CD1', 'TYR', 'CB', 'CYS', 12.29), ('CD1', 'TYR', 'SG', 'CYS', 10.65)], [('CD2', 'TYR', 'CB', 'CYS', 12.02), ('CD2', 'TYR', 'SG', 'CYS', 10.27)], [('CE1', 'TYR', 'CB', 'CYS', 11.13), ('CE1', 'TYR', 'SG', 'CYS', 9.49)], [('CE2', 'TYR', 'CB', 'CYS', 10.79), ('CE2', 'TYR', 'SG', 'CYS', 9.02)], [('CZ', 'TYR', 'CB', 'CYS', 10.34), ('CZ', 'TYR', 'SG', 'CYS', 8.61)], [('OH', 'TYR', 'CB', 'CYS', 9.29), ('OH', 'TYR', 'SG', 'CYS', 7.56)], [('CB', 'TYR', 'CB', 'CYS', 7.3), ('CB', 'TYR', 'SG', 'CYS', 7.34)], [('CG', 'TYR', 'CB', 'CYS', 6.46), ('CG', 'TYR', 'SG', 'CYS', 6.1)], [('CD1', 'TYR', 'CB', 'CYS', 5.08), ('CD1', 'TYR', 'SG', 'CYS', 4.83)], [('CD2', 'TYR', 'CB', 'CYS', 7.41), ('CD2', 'TYR', 'SG', 'CYS', 6.6)], [('CE1', 'TYR', 'CB', 'CYS', 4.84), ('CE1', 'TYR', 'SG', 'CYS', 3.78)], [('CE2', 'TYR', 'CB', 'CYS', 7.32), ('CE2', 'TYR', 'SG', 'CYS', 6.09)], [('CZ', 'TYR', 'CB', 'CYS', 6.17), ('CZ', 'TYR', 'SG', 'CYS', 4.75)], [('OH', 'TYR', 'CB', 'CYS', 6.58), ('OH', 'TYR', 'SG', 'CYS', 4.85)]]}
TYR_TYR = { 
	'distances':
		[[14.34, 13.11, 13.09, 12.18, 12.11, 11.05, 11.05, 10.25], [12.95, 11.69, 11.65, 10.75, 10.65, 9.58, 9.57, 8.76], [11.98, 10.81, 10.92, 9.83, 10.07, 8.77, 8.96, 8.36], [12.79, 11.43, 11.26, 10.54, 10.12, 9.26, 9.06, 8.07], [10.65, 9.46, 9.61, 8.46, 8.79, 7.4, 7.63, 7.13], [11.54, 10.14, 9.96, 9.25, 8.8, 7.93, 7.7, 6.68], [10.44, 9.11, 9.09, 8.14, 8.08, 6.9, 6.9, 6.14], [9.28, 7.91, 7.89, 6.92, 6.88, 5.62, 5.62, 4.91], [14.34, 12.95, 11.98, 12.79, 10.65, 11.54, 10.44, 9.28], [13.11, 11.69, 10.81, 11.43, 9.46, 10.14, 9.11, 7.91], [13.09, 11.65, 10.92, 11.26, 9.61, 9.96, 9.09, 7.89], [12.18, 10.75, 9.83, 10.54, 8.46, 9.25, 8.14, 6.92], [12.11, 10.65, 10.07, 10.12, 8.79, 8.8, 8.08, 6.88], [11.05, 9.58, 8.77, 9.26, 7.4, 7.93, 6.9, 5.62], [11.05, 9.57, 8.96, 9.06, 7.63, 7.7, 6.9, 5.62], [10.25, 8.76, 8.36, 8.07, 7.13, 6.68, 6.14, 4.91]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TYR', 14.34), ('CB', 'TYR', 'CG', 'TYR', 13.11), ('CB', 'TYR', 'CD1', 'TYR', 13.09), ('CB', 'TYR', 'CD2', 'TYR', 12.18), ('CB', 'TYR', 'CE1', 'TYR', 12.11), ('CB', 'TYR', 'CE2', 'TYR', 11.05), ('CB', 'TYR', 'CZ', 'TYR', 11.05), ('CB', 'TYR', 'OH', 'TYR', 10.25)], [('CG', 'TYR', 'CB', 'TYR', 12.95), ('CG', 'TYR', 'CG', 'TYR', 11.69), ('CG', 'TYR', 'CD1', 'TYR', 11.65), ('CG', 'TYR', 'CD2', 'TYR', 10.75), ('CG', 'TYR', 'CE1', 'TYR', 10.65), ('CG', 'TYR', 'CE2', 'TYR', 9.58), ('CG', 'TYR', 'CZ', 'TYR', 9.57), ('CG', 'TYR', 'OH', 'TYR', 8.76)], [('CD1', 'TYR', 'CB', 'TYR', 11.98), ('CD1', 'TYR', 'CG', 'TYR', 10.81), ('CD1', 'TYR', 'CD1', 'TYR', 10.92), ('CD1', 'TYR', 'CD2', 'TYR', 9.83), ('CD1', 'TYR', 'CE1', 'TYR', 10.07), ('CD1', 'TYR', 'CE2', 'TYR', 8.77), ('CD1', 'TYR', 'CZ', 'TYR', 8.96), ('CD1', 'TYR', 'OH', 'TYR', 8.36)], [('CD2', 'TYR', 'CB', 'TYR', 12.79), ('CD2', 'TYR', 'CG', 'TYR', 11.43), ('CD2', 'TYR', 'CD1', 'TYR', 11.26), ('CD2', 'TYR', 'CD2', 'TYR', 10.54), ('CD2', 'TYR', 'CE1', 'TYR', 10.12), ('CD2', 'TYR', 'CE2', 'TYR', 9.26), ('CD2', 'TYR', 'CZ', 'TYR', 9.06), ('CD2', 'TYR', 'OH', 'TYR', 8.07)], [('CE1', 'TYR', 'CB', 'TYR', 10.65), ('CE1', 'TYR', 'CG', 'TYR', 9.46), ('CE1', 'TYR', 'CD1', 'TYR', 9.61), ('CE1', 'TYR', 'CD2', 'TYR', 8.46), ('CE1', 'TYR', 'CE1', 'TYR', 8.79), ('CE1', 'TYR', 'CE2', 'TYR', 7.4), ('CE1', 'TYR', 'CZ', 'TYR', 7.63), ('CE1', 'TYR', 'OH', 'TYR', 7.13)], [('CE2', 'TYR', 'CB', 'TYR', 11.54), ('CE2', 'TYR', 'CG', 'TYR', 10.14), ('CE2', 'TYR', 'CD1', 'TYR', 9.96), ('CE2', 'TYR', 'CD2', 'TYR', 9.25), ('CE2', 'TYR', 'CE1', 'TYR', 8.8), ('CE2', 'TYR', 'CE2', 'TYR', 7.93), ('CE2', 'TYR', 'CZ', 'TYR', 7.7), ('CE2', 'TYR', 'OH', 'TYR', 6.68)], [('CZ', 'TYR', 'CB', 'TYR', 10.44), ('CZ', 'TYR', 'CG', 'TYR', 9.11), ('CZ', 'TYR', 'CD1', 'TYR', 9.09), ('CZ', 'TYR', 'CD2', 'TYR', 8.14), ('CZ', 'TYR', 'CE1', 'TYR', 8.08), ('CZ', 'TYR', 'CE2', 'TYR', 6.9), ('CZ', 'TYR', 'CZ', 'TYR', 6.9), ('CZ', 'TYR', 'OH', 'TYR', 6.14)], [('OH', 'TYR', 'CB', 'TYR', 9.28), ('OH', 'TYR', 'CG', 'TYR', 7.91), ('OH', 'TYR', 'CD1', 'TYR', 7.89), ('OH', 'TYR', 'CD2', 'TYR', 6.92), ('OH', 'TYR', 'CE1', 'TYR', 6.88), ('OH', 'TYR', 'CE2', 'TYR', 5.62), ('OH', 'TYR', 'CZ', 'TYR', 5.62), ('OH', 'TYR', 'OH', 'TYR', 4.91)], [('CB', 'TYR', 'CB', 'TYR', 14.34), ('CB', 'TYR', 'CG', 'TYR', 12.95), ('CB', 'TYR', 'CD1', 'TYR', 11.98), ('CB', 'TYR', 'CD2', 'TYR', 12.79), ('CB', 'TYR', 'CE1', 'TYR', 10.65), ('CB', 'TYR', 'CE2', 'TYR', 11.54), ('CB', 'TYR', 'CZ', 'TYR', 10.44), ('CB', 'TYR', 'OH', 'TYR', 9.28)], [('CG', 'TYR', 'CB', 'TYR', 13.11), ('CG', 'TYR', 'CG', 'TYR', 11.69), ('CG', 'TYR', 'CD1', 'TYR', 10.81), ('CG', 'TYR', 'CD2', 'TYR', 11.43), ('CG', 'TYR', 'CE1', 'TYR', 9.46), ('CG', 'TYR', 'CE2', 'TYR', 10.14), ('CG', 'TYR', 'CZ', 'TYR', 9.11), ('CG', 'TYR', 'OH', 'TYR', 7.91)], [('CD1', 'TYR', 'CB', 'TYR', 13.09), ('CD1', 'TYR', 'CG', 'TYR', 11.65), ('CD1', 'TYR', 'CD1', 'TYR', 10.92), ('CD1', 'TYR', 'CD2', 'TYR', 11.26), ('CD1', 'TYR', 'CE1', 'TYR', 9.61), ('CD1', 'TYR', 'CE2', 'TYR', 9.96), ('CD1', 'TYR', 'CZ', 'TYR', 9.09), ('CD1', 'TYR', 'OH', 'TYR', 7.89)], [('CD2', 'TYR', 'CB', 'TYR', 12.18), ('CD2', 'TYR', 'CG', 'TYR', 10.75), ('CD2', 'TYR', 'CD1', 'TYR', 9.83), ('CD2', 'TYR', 'CD2', 'TYR', 10.54), ('CD2', 'TYR', 'CE1', 'TYR', 8.46), ('CD2', 'TYR', 'CE2', 'TYR', 9.25), ('CD2', 'TYR', 'CZ', 'TYR', 8.14), ('CD2', 'TYR', 'OH', 'TYR', 6.92)], [('CE1', 'TYR', 'CB', 'TYR', 12.11), ('CE1', 'TYR', 'CG', 'TYR', 10.65), ('CE1', 'TYR', 'CD1', 'TYR', 10.07), ('CE1', 'TYR', 'CD2', 'TYR', 10.12), ('CE1', 'TYR', 'CE1', 'TYR', 8.79), ('CE1', 'TYR', 'CE2', 'TYR', 8.8), ('CE1', 'TYR', 'CZ', 'TYR', 8.08), ('CE1', 'TYR', 'OH', 'TYR', 6.88)], [('CE2', 'TYR', 'CB', 'TYR', 11.05), ('CE2', 'TYR', 'CG', 'TYR', 9.58), ('CE2', 'TYR', 'CD1', 'TYR', 8.77), ('CE2', 'TYR', 'CD2', 'TYR', 9.26), ('CE2', 'TYR', 'CE1', 'TYR', 7.4), ('CE2', 'TYR', 'CE2', 'TYR', 7.93), ('CE2', 'TYR', 'CZ', 'TYR', 6.9), ('CE2', 'TYR', 'OH', 'TYR', 5.62)], [('CZ', 'TYR', 'CB', 'TYR', 11.05), ('CZ', 'TYR', 'CG', 'TYR', 9.57), ('CZ', 'TYR', 'CD1', 'TYR', 8.96), ('CZ', 'TYR', 'CD2', 'TYR', 9.06), ('CZ', 'TYR', 'CE1', 'TYR', 7.63), ('CZ', 'TYR', 'CE2', 'TYR', 7.7), ('CZ', 'TYR', 'CZ', 'TYR', 6.9), ('CZ', 'TYR', 'OH', 'TYR', 5.62)], [('OH', 'TYR', 'CB', 'TYR', 10.25), ('OH', 'TYR', 'CG', 'TYR', 8.76), ('OH', 'TYR', 'CD1', 'TYR', 8.36), ('OH', 'TYR', 'CD2', 'TYR', 8.07), ('OH', 'TYR', 'CE1', 'TYR', 7.13), ('OH', 'TYR', 'CE2', 'TYR', 6.68), ('OH', 'TYR', 'CZ', 'TYR', 6.14), ('OH', 'TYR', 'OH', 'TYR', 4.91)]]}
TRP_CYS = { 
	'distances':
		[[7.28, 7.23], [6.76, 6.38], [7.52, 6.7], [6.01, 5.77], [7.39, 6.37], [6.51, 5.77], [5.53, 5.9], [6.58, 5.88], [5.57, 5.95], [6.12, 5.95]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'CYS', 7.28), ('CB', 'TRP', 'SG', 'CYS', 7.23)], [('CG', 'TRP', 'CB', 'CYS', 6.76), ('CG', 'TRP', 'SG', 'CYS', 6.38)], [('CD1', 'TRP', 'CB', 'CYS', 7.52), ('CD1', 'TRP', 'SG', 'CYS', 6.7)], [('CD2', 'TRP', 'CB', 'CYS', 6.01), ('CD2', 'TRP', 'SG', 'CYS', 5.77)], [('NE1', 'TRP', 'CB', 'CYS', 7.39), ('NE1', 'TRP', 'SG', 'CYS', 6.37)], [('CE2', 'TRP', 'CB', 'CYS', 6.51), ('CE2', 'TRP', 'SG', 'CYS', 5.77)], [('CE3', 'TRP', 'CB', 'CYS', 5.53), ('CE3', 'TRP', 'SG', 'CYS', 5.9)], [('CZ2', 'TRP', 'CB', 'CYS', 6.58), ('CZ2', 'TRP', 'SG', 'CYS', 5.88)], [('CZ3', 'TRP', 'CB', 'CYS', 5.57), ('CZ3', 'TRP', 'SG', 'CYS', 5.95)], [('CH2', 'TRP', 'CB', 'CYS', 6.12), ('CH2', 'TRP', 'SG', 'CYS', 5.95)]]}
TYR_CU = { 
	'distances':
		[[8.92], [7.5], [7.33], [6.76], [6.32], [5.55], [5.29], [4.59], [8.96], [7.49], [6.88], [7.09], [5.59], [5.87], [4.94], [3.91]],
	'comparisons':
		[[('CB', 'TYR', 'CU', 'CU', 8.92)], [('CG', 'TYR', 'CU', 'CU', 7.5)], [('CD1', 'TYR', 'CU', 'CU', 7.33)], [('CD2', 'TYR', 'CU', 'CU', 6.76)], [('CE1', 'TYR', 'CU', 'CU', 6.32)], [('CE2', 'TYR', 'CU', 'CU', 5.55)], [('CZ', 'TYR', 'CU', 'CU', 5.29)], [('OH', 'TYR', 'CU', 'CU', 4.59)], [('CB', 'TYR', 'CU', 'CU', 8.96)], [('CG', 'TYR', 'CU', 'CU', 7.49)], [('CD1', 'TYR', 'CU', 'CU', 6.88)], [('CD2', 'TYR', 'CU', 'CU', 7.09)], [('CE1', 'TYR', 'CU', 'CU', 5.59)], [('CE2', 'TYR', 'CU', 'CU', 5.87)], [('CZ', 'TYR', 'CU', 'CU', 4.94)], [('OH', 'TYR', 'CU', 'CU', 3.91)]]}
CYS_CU = { 
	'distances':
		[[7.26], [5.51]],
	'comparisons':
		[[('CB', 'CYS', 'CU', 'CU', 7.26)], [('SG', 'CYS', 'CU', 'CU', 5.51)]]}
TYR_TRP = { 
	'distances':
		[[15.29, 14.45, 13.52, 14.62, 13.11, 13.78, 15.57, 13.92, 15.66, 14.89], [13.8, 12.94, 12.02, 13.11, 11.62, 12.29, 14.08, 12.47, 14.2, 13.45], [13.1, 12.38, 11.51, 12.71, 11.3, 12.03, 13.71, 12.38, 13.98, 13.37], [13.27, 12.28, 11.34, 12.33, 10.79, 11.4, 13.27, 11.46, 13.29, 12.44], [11.73, 11.05, 10.2, 11.42, 10.06, 10.81, 12.44, 11.25, 12.79, 12.25], [11.85, 10.85, 9.91, 10.91, 9.36, 9.99, 11.89, 10.12, 11.95, 11.14], [11.06, 10.21, 9.31, 10.45, 9.0, 9.7, 11.47, 10.05, 11.72, 11.07], [9.7, 8.84, 7.96, 9.13, 7.7, 8.43, 10.19, 8.89, 10.52, 9.94], [5.67, 6.46, 7.1, 7.33, 8.15, 8.26, 7.75, 9.38, 8.95, 9.66], [5.44, 5.73, 6.15, 6.48, 7.01, 7.18, 7.09, 8.25, 8.16, 8.66], [5.63, 5.56, 6.13, 5.86, 6.68, 6.53, 6.24, 7.39, 7.13, 7.63], [5.78, 5.85, 5.78, 6.8, 6.66, 7.19, 7.71, 8.33, 8.76, 9.02], [6.17, 5.57, 5.8, 5.58, 5.95, 5.81, 6.12, 6.49, 6.73, 6.89], [6.38, 5.96, 5.52, 6.68, 6.04, 6.68, 7.72, 7.69, 8.56, 8.54], [6.49, 5.77, 5.49, 6.05, 5.62, 5.93, 6.95, 6.72, 7.56, 7.46], [7.44, 6.43, 5.89, 6.43, 5.54, 5.87, 7.35, 6.35, 7.67, 7.23]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TRP', 15.29), ('CB', 'TYR', 'CG', 'TRP', 14.45), ('CB', 'TYR', 'CD1', 'TRP', 13.52), ('CB', 'TYR', 'CD2', 'TRP', 14.62), ('CB', 'TYR', 'NE1', 'TRP', 13.11), ('CB', 'TYR', 'CE2', 'TRP', 13.78), ('CB', 'TYR', 'CE3', 'TRP', 15.57), ('CB', 'TYR', 'CZ2', 'TRP', 13.92), ('CB', 'TYR', 'CZ3', 'TRP', 15.66), ('CB', 'TYR', 'CH2', 'TRP', 14.89)], [('CG', 'TYR', 'CB', 'TRP', 13.8), ('CG', 'TYR', 'CG', 'TRP', 12.94), ('CG', 'TYR', 'CD1', 'TRP', 12.02), ('CG', 'TYR', 'CD2', 'TRP', 13.11), ('CG', 'TYR', 'NE1', 'TRP', 11.62), ('CG', 'TYR', 'CE2', 'TRP', 12.29), ('CG', 'TYR', 'CE3', 'TRP', 14.08), ('CG', 'TYR', 'CZ2', 'TRP', 12.47), ('CG', 'TYR', 'CZ3', 'TRP', 14.2), ('CG', 'TYR', 'CH2', 'TRP', 13.45)], [('CD1', 'TYR', 'CB', 'TRP', 13.1), ('CD1', 'TYR', 'CG', 'TRP', 12.38), ('CD1', 'TYR', 'CD1', 'TRP', 11.51), ('CD1', 'TYR', 'CD2', 'TRP', 12.71), ('CD1', 'TYR', 'NE1', 'TRP', 11.3), ('CD1', 'TYR', 'CE2', 'TRP', 12.03), ('CD1', 'TYR', 'CE3', 'TRP', 13.71), ('CD1', 'TYR', 'CZ2', 'TRP', 12.38), ('CD1', 'TYR', 'CZ3', 'TRP', 13.98), ('CD1', 'TYR', 'CH2', 'TRP', 13.37)], [('CD2', 'TYR', 'CB', 'TRP', 13.27), ('CD2', 'TYR', 'CG', 'TRP', 12.28), ('CD2', 'TYR', 'CD1', 'TRP', 11.34), ('CD2', 'TYR', 'CD2', 'TRP', 12.33), ('CD2', 'TYR', 'NE1', 'TRP', 10.79), ('CD2', 'TYR', 'CE2', 'TRP', 11.4), ('CD2', 'TYR', 'CE3', 'TRP', 13.27), ('CD2', 'TYR', 'CZ2', 'TRP', 11.46), ('CD2', 'TYR', 'CZ3', 'TRP', 13.29), ('CD2', 'TYR', 'CH2', 'TRP', 12.44)], [('CE1', 'TYR', 'CB', 'TRP', 11.73), ('CE1', 'TYR', 'CG', 'TRP', 11.05), ('CE1', 'TYR', 'CD1', 'TRP', 10.2), ('CE1', 'TYR', 'CD2', 'TRP', 11.42), ('CE1', 'TYR', 'NE1', 'TRP', 10.06), ('CE1', 'TYR', 'CE2', 'TRP', 10.81), ('CE1', 'TYR', 'CE3', 'TRP', 12.44), ('CE1', 'TYR', 'CZ2', 'TRP', 11.25), ('CE1', 'TYR', 'CZ3', 'TRP', 12.79), ('CE1', 'TYR', 'CH2', 'TRP', 12.25)], [('CE2', 'TYR', 'CB', 'TRP', 11.85), ('CE2', 'TYR', 'CG', 'TRP', 10.85), ('CE2', 'TYR', 'CD1', 'TRP', 9.91), ('CE2', 'TYR', 'CD2', 'TRP', 10.91), ('CE2', 'TYR', 'NE1', 'TRP', 9.36), ('CE2', 'TYR', 'CE2', 'TRP', 9.99), ('CE2', 'TYR', 'CE3', 'TRP', 11.89), ('CE2', 'TYR', 'CZ2', 'TRP', 10.12), ('CE2', 'TYR', 'CZ3', 'TRP', 11.95), ('CE2', 'TYR', 'CH2', 'TRP', 11.14)], [('CZ', 'TYR', 'CB', 'TRP', 11.06), ('CZ', 'TYR', 'CG', 'TRP', 10.21), ('CZ', 'TYR', 'CD1', 'TRP', 9.31), ('CZ', 'TYR', 'CD2', 'TRP', 10.45), ('CZ', 'TYR', 'NE1', 'TRP', 9.0), ('CZ', 'TYR', 'CE2', 'TRP', 9.7), ('CZ', 'TYR', 'CE3', 'TRP', 11.47), ('CZ', 'TYR', 'CZ2', 'TRP', 10.05), ('CZ', 'TYR', 'CZ3', 'TRP', 11.72), ('CZ', 'TYR', 'CH2', 'TRP', 11.07)], [('OH', 'TYR', 'CB', 'TRP', 9.7), ('OH', 'TYR', 'CG', 'TRP', 8.84), ('OH', 'TYR', 'CD1', 'TRP', 7.96), ('OH', 'TYR', 'CD2', 'TRP', 9.13), ('OH', 'TYR', 'NE1', 'TRP', 7.7), ('OH', 'TYR', 'CE2', 'TRP', 8.43), ('OH', 'TYR', 'CE3', 'TRP', 10.19), ('OH', 'TYR', 'CZ2', 'TRP', 8.89), ('OH', 'TYR', 'CZ3', 'TRP', 10.52), ('OH', 'TYR', 'CH2', 'TRP', 9.94)], [('CB', 'TYR', 'CB', 'TRP', 5.67), ('CB', 'TYR', 'CG', 'TRP', 6.46), ('CB', 'TYR', 'CD1', 'TRP', 7.1), ('CB', 'TYR', 'CD2', 'TRP', 7.33), ('CB', 'TYR', 'NE1', 'TRP', 8.15), ('CB', 'TYR', 'CE2', 'TRP', 8.26), ('CB', 'TYR', 'CE3', 'TRP', 7.75), ('CB', 'TYR', 'CZ2', 'TRP', 9.38), ('CB', 'TYR', 'CZ3', 'TRP', 8.95), ('CB', 'TYR', 'CH2', 'TRP', 9.66)], [('CG', 'TYR', 'CB', 'TRP', 5.44), ('CG', 'TYR', 'CG', 'TRP', 5.73), ('CG', 'TYR', 'CD1', 'TRP', 6.15), ('CG', 'TYR', 'CD2', 'TRP', 6.48), ('CG', 'TYR', 'NE1', 'TRP', 7.01), ('CG', 'TYR', 'CE2', 'TRP', 7.18), ('CG', 'TYR', 'CE3', 'TRP', 7.09), ('CG', 'TYR', 'CZ2', 'TRP', 8.25), ('CG', 'TYR', 'CZ3', 'TRP', 8.16), ('CG', 'TYR', 'CH2', 'TRP', 8.66)], [('CD1', 'TYR', 'CB', 'TRP', 5.63), ('CD1', 'TYR', 'CG', 'TRP', 5.56), ('CD1', 'TYR', 'CD1', 'TRP', 6.13), ('CD1', 'TYR', 'CD2', 'TRP', 5.86), ('CD1', 'TYR', 'NE1', 'TRP', 6.68), ('CD1', 'TYR', 'CE2', 'TRP', 6.53), ('CD1', 'TYR', 'CE3', 'TRP', 6.24), ('CD1', 'TYR', 'CZ2', 'TRP', 7.39), ('CD1', 'TYR', 'CZ3', 'TRP', 7.13), ('CD1', 'TYR', 'CH2', 'TRP', 7.63)], [('CD2', 'TYR', 'CB', 'TRP', 5.78), ('CD2', 'TYR', 'CG', 'TRP', 5.85), ('CD2', 'TYR', 'CD1', 'TRP', 5.78), ('CD2', 'TYR', 'CD2', 'TRP', 6.8), ('CD2', 'TYR', 'NE1', 'TRP', 6.66), ('CD2', 'TYR', 'CE2', 'TRP', 7.19), ('CD2', 'TYR', 'CE3', 'TRP', 7.71), ('CD2', 'TYR', 'CZ2', 'TRP', 8.33), ('CD2', 'TYR', 'CZ3', 'TRP', 8.76), ('CD2', 'TYR', 'CH2', 'TRP', 9.02)], [('CE1', 'TYR', 'CB', 'TRP', 6.17), ('CE1', 'TYR', 'CG', 'TRP', 5.57), ('CE1', 'TYR', 'CD1', 'TRP', 5.8), ('CE1', 'TYR', 'CD2', 'TRP', 5.58), ('CE1', 'TYR', 'NE1', 'TRP', 5.95), ('CE1', 'TYR', 'CE2', 'TRP', 5.81), ('CE1', 'TYR', 'CE3', 'TRP', 6.12), ('CE1', 'TYR', 'CZ2', 'TRP', 6.49), ('CE1', 'TYR', 'CZ3', 'TRP', 6.73), ('CE1', 'TYR', 'CH2', 'TRP', 6.89)], [('CE2', 'TYR', 'CB', 'TRP', 6.38), ('CE2', 'TYR', 'CG', 'TRP', 5.96), ('CE2', 'TYR', 'CD1', 'TRP', 5.52), ('CE2', 'TYR', 'CD2', 'TRP', 6.68), ('CE2', 'TYR', 'NE1', 'TRP', 6.04), ('CE2', 'TYR', 'CE2', 'TRP', 6.68), ('CE2', 'TYR', 'CE3', 'TRP', 7.72), ('CE2', 'TYR', 'CZ2', 'TRP', 7.69), ('CE2', 'TYR', 'CZ3', 'TRP', 8.56), ('CE2', 'TYR', 'CH2', 'TRP', 8.54)], [('CZ', 'TYR', 'CB', 'TRP', 6.49), ('CZ', 'TYR', 'CG', 'TRP', 5.77), ('CZ', 'TYR', 'CD1', 'TRP', 5.49), ('CZ', 'TYR', 'CD2', 'TRP', 6.05), ('CZ', 'TYR', 'NE1', 'TRP', 5.62), ('CZ', 'TYR', 'CE2', 'TRP', 5.93), ('CZ', 'TYR', 'CE3', 'TRP', 6.95), ('CZ', 'TYR', 'CZ2', 'TRP', 6.72), ('CZ', 'TYR', 'CZ3', 'TRP', 7.56), ('CZ', 'TYR', 'CH2', 'TRP', 7.46)], [('OH', 'TYR', 'CB', 'TRP', 7.44), ('OH', 'TYR', 'CG', 'TRP', 6.43), ('OH', 'TYR', 'CD1', 'TRP', 5.89), ('OH', 'TYR', 'CD2', 'TRP', 6.43), ('OH', 'TYR', 'NE1', 'TRP', 5.54), ('OH', 'TYR', 'CE2', 'TRP', 5.87), ('OH', 'TYR', 'CE3', 'TRP', 7.35), ('OH', 'TYR', 'CZ2', 'TRP', 6.35), ('OH', 'TYR', 'CZ3', 'TRP', 7.67), ('OH', 'TYR', 'CH2', 'TRP', 7.23)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CU_TYRI, d, 'M_1gog_1_1_3_9')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TRP_CU, d, 'M_1gog_1_1_3_9')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_CYS, d, 'M_1gog_1_1_3_9')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_TYR, d, 'M_1gog_1_1_3_9')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(TRP_CYS, d, 'M_1gog_1_1_3_9')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_CU, d, 'M_1gog_1_1_3_9')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(CYS_CU, d, 'M_1gog_1_1_3_9')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(TYR_TRP, d, 'M_1gog_1_1_3_9')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CU_TYRI' :  match1,
		'TRP_CU' :  match2,
		'TYR_CYS' :  match3,
		'TYR_TYR' :  match4,
		'TRP_CYS' :  match5,
		'TYR_CU' :  match6,
		'CYS_CU' :  match7,
		'TYR_TRP' :  match8}