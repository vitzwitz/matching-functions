'''
FUNC:M_1o8a_3_4_15_1
PDB:1o8a
EC:3.4.15.1
RESI:his,ala,glu,his,tyr,zn
LOCI:a-353,354,384,513,523,701;
'''
import motifFunctions as cmd
HIS_ALA = { 
	'distances':
		[[7.75], [7.49], [7.92], [7.27], [7.96], [7.58], [13.99], [12.64], [11.92], [12.0], [10.8], [10.82]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ALA', 7.75)], [('CG', 'HIS', 'CB', 'ALA', 7.49)], [('ND1', 'HIS', 'CB', 'ALA', 7.92)], [('CD2', 'HIS', 'CB', 'ALA', 7.27)], [('CE1', 'HIS', 'CB', 'ALA', 7.96)], [('NE2', 'HIS', 'CB', 'ALA', 7.58)], [('CB', 'HIS', 'CB', 'ALA', 13.99)], [('CG', 'HIS', 'CB', 'ALA', 12.64)], [('ND1', 'HIS', 'CB', 'ALA', 11.92)], [('CD2', 'HIS', 'CB', 'ALA', 12.0)], [('CE1', 'HIS', 'CB', 'ALA', 10.8)], [('NE2', 'HIS', 'CB', 'ALA', 10.82)]]}
HIS_ZN = { 
	'distances':
		[[12.18], [11.09], [11.39], [9.83], [10.43], [9.38], [12.31], [11.0], [11.09], [9.72], [9.94], [8.98]],
	'comparisons':
		[[('CB', 'HIS', 'ZN', 'ZN', 12.18)], [('CG', 'HIS', 'ZN', 'ZN', 11.09)], [('ND1', 'HIS', 'ZN', 'ZN', 11.39)], [('CD2', 'HIS', 'ZN', 'ZN', 9.83)], [('CE1', 'HIS', 'ZN', 'ZN', 10.43)], [('NE2', 'HIS', 'ZN', 'ZN', 9.38)], [('CB', 'HIS', 'ZN', 'ZN', 12.31)], [('CG', 'HIS', 'ZN', 'ZN', 11.0)], [('ND1', 'HIS', 'ZN', 'ZN', 11.09)], [('CD2', 'HIS', 'ZN', 'ZN', 9.72)], [('CE1', 'HIS', 'ZN', 'ZN', 9.94)], [('NE2', 'HIS', 'ZN', 'ZN', 8.98)]]}
ALA_HISI = { 
	'distances':
		[13.99, 12.64, 11.92, 12.0, 10.8, 10.82],
	'comparisons':
		[('CB', 'ALA', 'CB', 'HISI', 13.99), ('CB', 'ALA', 'CG', 'HISI', 12.64), ('CB', 'ALA', 'ND1', 'HISI', 11.92), ('CB', 'ALA', 'CD2', 'HISI', 12.0), ('CB', 'ALA', 'CE1', 'HISI', 10.8), ('CB', 'ALA', 'NE2', 'HISI', 10.82)]}
HIS_HIS = { 
	'distances':
		[[10.68, 9.79, 9.03, 9.79, 8.56, 9.04], [9.63, 8.6, 7.78, 8.54, 7.17, 7.67], [9.43, 8.36, 7.31, 8.44, 6.71, 7.47], [9.09, 7.93, 7.27, 7.63, 6.5, 6.73], [8.77, 7.55, 6.47, 7.51, 5.66, 6.4], [8.53, 7.23, 6.42, 6.92, 5.46, 5.81], [10.68, 9.63, 9.43, 9.09, 8.77, 8.53], [9.79, 8.6, 8.36, 7.93, 7.55, 7.23], [9.03, 7.78, 7.31, 7.27, 6.47, 6.42], [9.79, 8.54, 8.44, 7.63, 7.51, 6.92], [8.56, 7.17, 6.71, 6.5, 5.66, 5.46], [9.04, 7.67, 7.47, 6.73, 6.4, 5.81]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 10.68), ('CB', 'HIS', 'CG', 'HIS', 9.79), ('CB', 'HIS', 'ND1', 'HIS', 9.03), ('CB', 'HIS', 'CD2', 'HIS', 9.79), ('CB', 'HIS', 'CE1', 'HIS', 8.56), ('CB', 'HIS', 'NE2', 'HIS', 9.04)], [('CG', 'HIS', 'CB', 'HIS', 9.63), ('CG', 'HIS', 'CG', 'HIS', 8.6), ('CG', 'HIS', 'ND1', 'HIS', 7.78), ('CG', 'HIS', 'CD2', 'HIS', 8.54), ('CG', 'HIS', 'CE1', 'HIS', 7.17), ('CG', 'HIS', 'NE2', 'HIS', 7.67)], [('ND1', 'HIS', 'CB', 'HIS', 9.43), ('ND1', 'HIS', 'CG', 'HIS', 8.36), ('ND1', 'HIS', 'ND1', 'HIS', 7.31), ('ND1', 'HIS', 'CD2', 'HIS', 8.44), ('ND1', 'HIS', 'CE1', 'HIS', 6.71), ('ND1', 'HIS', 'NE2', 'HIS', 7.47)], [('CD2', 'HIS', 'CB', 'HIS', 9.09), ('CD2', 'HIS', 'CG', 'HIS', 7.93), ('CD2', 'HIS', 'ND1', 'HIS', 7.27), ('CD2', 'HIS', 'CD2', 'HIS', 7.63), ('CD2', 'HIS', 'CE1', 'HIS', 6.5), ('CD2', 'HIS', 'NE2', 'HIS', 6.73)], [('CE1', 'HIS', 'CB', 'HIS', 8.77), ('CE1', 'HIS', 'CG', 'HIS', 7.55), ('CE1', 'HIS', 'ND1', 'HIS', 6.47), ('CE1', 'HIS', 'CD2', 'HIS', 7.51), ('CE1', 'HIS', 'CE1', 'HIS', 5.66), ('CE1', 'HIS', 'NE2', 'HIS', 6.4)], [('NE2', 'HIS', 'CB', 'HIS', 8.53), ('NE2', 'HIS', 'CG', 'HIS', 7.23), ('NE2', 'HIS', 'ND1', 'HIS', 6.42), ('NE2', 'HIS', 'CD2', 'HIS', 6.92), ('NE2', 'HIS', 'CE1', 'HIS', 5.46), ('NE2', 'HIS', 'NE2', 'HIS', 5.81)], [('CB', 'HIS', 'CB', 'HIS', 10.68), ('CB', 'HIS', 'CG', 'HIS', 9.63), ('CB', 'HIS', 'ND1', 'HIS', 9.43), ('CB', 'HIS', 'CD2', 'HIS', 9.09), ('CB', 'HIS', 'CE1', 'HIS', 8.77), ('CB', 'HIS', 'NE2', 'HIS', 8.53)], [('CG', 'HIS', 'CB', 'HIS', 9.79), ('CG', 'HIS', 'CG', 'HIS', 8.6), ('CG', 'HIS', 'ND1', 'HIS', 8.36), ('CG', 'HIS', 'CD2', 'HIS', 7.93), ('CG', 'HIS', 'CE1', 'HIS', 7.55), ('CG', 'HIS', 'NE2', 'HIS', 7.23)], [('ND1', 'HIS', 'CB', 'HIS', 9.03), ('ND1', 'HIS', 'CG', 'HIS', 7.78), ('ND1', 'HIS', 'ND1', 'HIS', 7.31), ('ND1', 'HIS', 'CD2', 'HIS', 7.27), ('ND1', 'HIS', 'CE1', 'HIS', 6.47), ('ND1', 'HIS', 'NE2', 'HIS', 6.42)], [('CD2', 'HIS', 'CB', 'HIS', 9.79), ('CD2', 'HIS', 'CG', 'HIS', 8.54), ('CD2', 'HIS', 'ND1', 'HIS', 8.44), ('CD2', 'HIS', 'CD2', 'HIS', 7.63), ('CD2', 'HIS', 'CE1', 'HIS', 7.51), ('CD2', 'HIS', 'NE2', 'HIS', 6.92)], [('CE1', 'HIS', 'CB', 'HIS', 8.56), ('CE1', 'HIS', 'CG', 'HIS', 7.17), ('CE1', 'HIS', 'ND1', 'HIS', 6.71), ('CE1', 'HIS', 'CD2', 'HIS', 6.5), ('CE1', 'HIS', 'CE1', 'HIS', 5.66), ('CE1', 'HIS', 'NE2', 'HIS', 5.46)], [('NE2', 'HIS', 'CB', 'HIS', 9.04), ('NE2', 'HIS', 'CG', 'HIS', 7.67), ('NE2', 'HIS', 'ND1', 'HIS', 7.47), ('NE2', 'HIS', 'CD2', 'HIS', 6.73), ('NE2', 'HIS', 'CE1', 'HIS', 6.4), ('NE2', 'HIS', 'NE2', 'HIS', 5.81)]]}
ALA_ZN = { 
	'distances':
		[9.6],
	'comparisons':
		[('CB', 'ALA', 'ZN', 'ZN', 9.6)]}
GLU_TYR = { 
	'distances':
		[[15.65, 14.57, 15.02, 13.22, 14.25, 12.3, 12.88, 12.24], [14.82, 13.7, 14.08, 12.39, 13.27, 11.43, 11.93, 11.26], [13.9, 12.69, 12.96, 11.41, 12.06, 10.33, 10.72, 9.95], [14.33, 13.07, 13.28, 11.8, 12.31, 10.66, 10.96, 10.09], [12.88, 11.65, 11.89, 10.41, 11.0, 9.33, 9.68, 8.93]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'TYR', 15.65), ('CB', 'GLU', 'CG', 'TYR', 14.57), ('CB', 'GLU', 'CD1', 'TYR', 15.02), ('CB', 'GLU', 'CD2', 'TYR', 13.22), ('CB', 'GLU', 'CE1', 'TYR', 14.25), ('CB', 'GLU', 'CE2', 'TYR', 12.3), ('CB', 'GLU', 'CZ', 'TYR', 12.88), ('CB', 'GLU', 'OH', 'TYR', 12.24)], [('CG', 'GLU', 'CB', 'TYR', 14.82), ('CG', 'GLU', 'CG', 'TYR', 13.7), ('CG', 'GLU', 'CD1', 'TYR', 14.08), ('CG', 'GLU', 'CD2', 'TYR', 12.39), ('CG', 'GLU', 'CE1', 'TYR', 13.27), ('CG', 'GLU', 'CE2', 'TYR', 11.43), ('CG', 'GLU', 'CZ', 'TYR', 11.93), ('CG', 'GLU', 'OH', 'TYR', 11.26)], [('CD', 'GLU', 'CB', 'TYR', 13.9), ('CD', 'GLU', 'CG', 'TYR', 12.69), ('CD', 'GLU', 'CD1', 'TYR', 12.96), ('CD', 'GLU', 'CD2', 'TYR', 11.41), ('CD', 'GLU', 'CE1', 'TYR', 12.06), ('CD', 'GLU', 'CE2', 'TYR', 10.33), ('CD', 'GLU', 'CZ', 'TYR', 10.72), ('CD', 'GLU', 'OH', 'TYR', 9.95)], [('OE1', 'GLU', 'CB', 'TYR', 14.33), ('OE1', 'GLU', 'CG', 'TYR', 13.07), ('OE1', 'GLU', 'CD1', 'TYR', 13.28), ('OE1', 'GLU', 'CD2', 'TYR', 11.8), ('OE1', 'GLU', 'CE1', 'TYR', 12.31), ('OE1', 'GLU', 'CE2', 'TYR', 10.66), ('OE1', 'GLU', 'CZ', 'TYR', 10.96), ('OE1', 'GLU', 'OH', 'TYR', 10.09)], [('OE2', 'GLU', 'CB', 'TYR', 12.88), ('OE2', 'GLU', 'CG', 'TYR', 11.65), ('OE2', 'GLU', 'CD1', 'TYR', 11.89), ('OE2', 'GLU', 'CD2', 'TYR', 10.41), ('OE2', 'GLU', 'CE1', 'TYR', 11.0), ('OE2', 'GLU', 'CE2', 'TYR', 9.33), ('OE2', 'GLU', 'CZ', 'TYR', 9.68), ('OE2', 'GLU', 'OH', 'TYR', 8.93)]]}
ALA_TYR = { 
	'distances':
		[14.86, 13.64, 13.71, 12.59, 12.78, 11.54, 11.66, 10.85],
	'comparisons':
		[('CB', 'ALA', 'CB', 'TYR', 14.86), ('CB', 'ALA', 'CG', 'TYR', 13.64), ('CB', 'ALA', 'CD1', 'TYR', 13.71), ('CB', 'ALA', 'CD2', 'TYR', 12.59), ('CB', 'ALA', 'CE1', 'TYR', 12.78), ('CB', 'ALA', 'CE2', 'TYR', 11.54), ('CB', 'ALA', 'CZ', 'TYR', 11.66), ('CB', 'ALA', 'OH', 'TYR', 10.85)]}
TYR_ZN = { 
	'distances':
		[[9.64], [8.45], [8.84], [7.16], [8.12], [6.14], [6.76], [6.38]],
	'comparisons':
		[[('CB', 'TYR', 'ZN', 'ZN', 9.64)], [('CG', 'TYR', 'ZN', 'ZN', 8.45)], [('CD1', 'TYR', 'ZN', 'ZN', 8.84)], [('CD2', 'TYR', 'ZN', 'ZN', 7.16)], [('CE1', 'TYR', 'ZN', 'ZN', 8.12)], [('CE2', 'TYR', 'ZN', 'ZN', 6.14)], [('CZ', 'TYR', 'ZN', 'ZN', 6.76)], [('OH', 'TYR', 'ZN', 'ZN', 6.38)]]}
HIS_TYR = { 
	'distances':
		[[15.36, 14.03, 13.46, 13.52, 12.34, 12.41, 11.77, 10.77], [13.88, 12.57, 12.02, 12.08, 10.94, 11.01, 10.38, 9.46], [13.4, 12.19, 11.68, 11.79, 10.73, 10.85, 10.28, 9.55], [12.88, 11.51, 10.98, 10.97, 9.83, 9.83, 9.19, 8.2], [12.09, 10.89, 10.43, 10.49, 9.52, 9.6, 9.07, 8.43], [11.7, 10.39, 9.91, 9.89, 8.86, 8.85, 8.28, 7.46], [10.63, 9.6, 8.31, 10.15, 7.54, 9.58, 8.29, 8.02], [9.78, 8.64, 7.45, 9.02, 6.56, 8.36, 7.12, 6.8], [9.97, 8.87, 7.85, 9.15, 7.05, 8.53, 7.45, 7.17], [9.08, 7.79, 6.64, 8.01, 5.54, 7.22, 5.92, 5.48], [9.44, 8.25, 7.4, 8.31, 6.52, 7.58, 6.64, 6.3], [8.86, 7.53, 6.62, 7.52, 5.53, 6.65, 5.55, 5.08]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 15.36), ('CB', 'HIS', 'CG', 'TYR', 14.03), ('CB', 'HIS', 'CD1', 'TYR', 13.46), ('CB', 'HIS', 'CD2', 'TYR', 13.52), ('CB', 'HIS', 'CE1', 'TYR', 12.34), ('CB', 'HIS', 'CE2', 'TYR', 12.41), ('CB', 'HIS', 'CZ', 'TYR', 11.77), ('CB', 'HIS', 'OH', 'TYR', 10.77)], [('CG', 'HIS', 'CB', 'TYR', 13.88), ('CG', 'HIS', 'CG', 'TYR', 12.57), ('CG', 'HIS', 'CD1', 'TYR', 12.02), ('CG', 'HIS', 'CD2', 'TYR', 12.08), ('CG', 'HIS', 'CE1', 'TYR', 10.94), ('CG', 'HIS', 'CE2', 'TYR', 11.01), ('CG', 'HIS', 'CZ', 'TYR', 10.38), ('CG', 'HIS', 'OH', 'TYR', 9.46)], [('ND1', 'HIS', 'CB', 'TYR', 13.4), ('ND1', 'HIS', 'CG', 'TYR', 12.19), ('ND1', 'HIS', 'CD1', 'TYR', 11.68), ('ND1', 'HIS', 'CD2', 'TYR', 11.79), ('ND1', 'HIS', 'CE1', 'TYR', 10.73), ('ND1', 'HIS', 'CE2', 'TYR', 10.85), ('ND1', 'HIS', 'CZ', 'TYR', 10.28), ('ND1', 'HIS', 'OH', 'TYR', 9.55)], [('CD2', 'HIS', 'CB', 'TYR', 12.88), ('CD2', 'HIS', 'CG', 'TYR', 11.51), ('CD2', 'HIS', 'CD1', 'TYR', 10.98), ('CD2', 'HIS', 'CD2', 'TYR', 10.97), ('CD2', 'HIS', 'CE1', 'TYR', 9.83), ('CD2', 'HIS', 'CE2', 'TYR', 9.83), ('CD2', 'HIS', 'CZ', 'TYR', 9.19), ('CD2', 'HIS', 'OH', 'TYR', 8.2)], [('CE1', 'HIS', 'CB', 'TYR', 12.09), ('CE1', 'HIS', 'CG', 'TYR', 10.89), ('CE1', 'HIS', 'CD1', 'TYR', 10.43), ('CE1', 'HIS', 'CD2', 'TYR', 10.49), ('CE1', 'HIS', 'CE1', 'TYR', 9.52), ('CE1', 'HIS', 'CE2', 'TYR', 9.6), ('CE1', 'HIS', 'CZ', 'TYR', 9.07), ('CE1', 'HIS', 'OH', 'TYR', 8.43)], [('NE2', 'HIS', 'CB', 'TYR', 11.7), ('NE2', 'HIS', 'CG', 'TYR', 10.39), ('NE2', 'HIS', 'CD1', 'TYR', 9.91), ('NE2', 'HIS', 'CD2', 'TYR', 9.89), ('NE2', 'HIS', 'CE1', 'TYR', 8.86), ('NE2', 'HIS', 'CE2', 'TYR', 8.85), ('NE2', 'HIS', 'CZ', 'TYR', 8.28), ('NE2', 'HIS', 'OH', 'TYR', 7.46)], [('CB', 'HIS', 'CB', 'TYR', 10.63), ('CB', 'HIS', 'CG', 'TYR', 9.6), ('CB', 'HIS', 'CD1', 'TYR', 8.31), ('CB', 'HIS', 'CD2', 'TYR', 10.15), ('CB', 'HIS', 'CE1', 'TYR', 7.54), ('CB', 'HIS', 'CE2', 'TYR', 9.58), ('CB', 'HIS', 'CZ', 'TYR', 8.29), ('CB', 'HIS', 'OH', 'TYR', 8.02)], [('CG', 'HIS', 'CB', 'TYR', 9.78), ('CG', 'HIS', 'CG', 'TYR', 8.64), ('CG', 'HIS', 'CD1', 'TYR', 7.45), ('CG', 'HIS', 'CD2', 'TYR', 9.02), ('CG', 'HIS', 'CE1', 'TYR', 6.56), ('CG', 'HIS', 'CE2', 'TYR', 8.36), ('CG', 'HIS', 'CZ', 'TYR', 7.12), ('CG', 'HIS', 'OH', 'TYR', 6.8)], [('ND1', 'HIS', 'CB', 'TYR', 9.97), ('ND1', 'HIS', 'CG', 'TYR', 8.87), ('ND1', 'HIS', 'CD1', 'TYR', 7.85), ('ND1', 'HIS', 'CD2', 'TYR', 9.15), ('ND1', 'HIS', 'CE1', 'TYR', 7.05), ('ND1', 'HIS', 'CE2', 'TYR', 8.53), ('ND1', 'HIS', 'CZ', 'TYR', 7.45), ('ND1', 'HIS', 'OH', 'TYR', 7.17)], [('CD2', 'HIS', 'CB', 'TYR', 9.08), ('CD2', 'HIS', 'CG', 'TYR', 7.79), ('CD2', 'HIS', 'CD1', 'TYR', 6.64), ('CD2', 'HIS', 'CD2', 'TYR', 8.01), ('CD2', 'HIS', 'CE1', 'TYR', 5.54), ('CD2', 'HIS', 'CE2', 'TYR', 7.22), ('CD2', 'HIS', 'CZ', 'TYR', 5.92), ('CD2', 'HIS', 'OH', 'TYR', 5.48)], [('CE1', 'HIS', 'CB', 'TYR', 9.44), ('CE1', 'HIS', 'CG', 'TYR', 8.25), ('CE1', 'HIS', 'CD1', 'TYR', 7.4), ('CE1', 'HIS', 'CD2', 'TYR', 8.31), ('CE1', 'HIS', 'CE1', 'TYR', 6.52), ('CE1', 'HIS', 'CE2', 'TYR', 7.58), ('CE1', 'HIS', 'CZ', 'TYR', 6.64), ('CE1', 'HIS', 'OH', 'TYR', 6.3)], [('NE2', 'HIS', 'CB', 'TYR', 8.86), ('NE2', 'HIS', 'CG', 'TYR', 7.53), ('NE2', 'HIS', 'CD1', 'TYR', 6.62), ('NE2', 'HIS', 'CD2', 'TYR', 7.52), ('NE2', 'HIS', 'CE1', 'TYR', 5.53), ('NE2', 'HIS', 'CE2', 'TYR', 6.65), ('NE2', 'HIS', 'CZ', 'TYR', 5.55), ('NE2', 'HIS', 'OH', 'TYR', 5.08)]]}
ZN_HISI = { 
	'distances':
		[12.31, 11.0, 11.09, 9.72, 9.94, 8.98],
	'comparisons':
		[('ZN', 'ZN', 'CB', 'HISI', 12.31), ('ZN', 'ZN', 'CG', 'HISI', 11.0), ('ZN', 'ZN', 'ND1', 'HISI', 11.09), ('ZN', 'ZN', 'CD2', 'HISI', 9.72), ('ZN', 'ZN', 'CE1', 'HISI', 9.94), ('ZN', 'ZN', 'NE2', 'HISI', 8.98)]}
GLU_ZN = { 
	'distances':
		[[8.66], [8.13], [6.98], [7.03], [6.39]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.66)], [('CG', 'GLU', 'ZN', 'ZN', 8.13)], [('CD', 'GLU', 'ZN', 'ZN', 6.98)], [('OE1', 'GLU', 'ZN', 'ZN', 7.03)], [('OE2', 'GLU', 'ZN', 'ZN', 6.39)]]}
GLU_HIS = { 
	'distances':
		[[12.73, 12.33, 12.86, 11.61, 12.52, 11.75], [11.32, 10.87, 11.35, 10.19, 11.03, 10.31], [10.56, 10.03, 10.6, 9.19, 10.2, 9.33], [10.93, 10.48, 11.2, 9.58, 10.84, 9.85], [9.8, 9.11, 9.58, 8.22, 9.08, 8.22], [17.21, 15.82, 15.46, 14.77, 14.21, 13.72], [15.97, 14.56, 14.13, 13.58, 12.87, 12.48], [14.7, 13.32, 12.99, 12.29, 11.76, 11.26], [14.89, 13.57, 13.38, 12.5, 12.2, 11.59], [13.6, 12.19, 11.82, 11.19, 10.57, 10.11]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 12.73), ('CB', 'GLU', 'CG', 'HIS', 12.33), ('CB', 'GLU', 'ND1', 'HIS', 12.86), ('CB', 'GLU', 'CD2', 'HIS', 11.61), ('CB', 'GLU', 'CE1', 'HIS', 12.52), ('CB', 'GLU', 'NE2', 'HIS', 11.75)], [('CG', 'GLU', 'CB', 'HIS', 11.32), ('CG', 'GLU', 'CG', 'HIS', 10.87), ('CG', 'GLU', 'ND1', 'HIS', 11.35), ('CG', 'GLU', 'CD2', 'HIS', 10.19), ('CG', 'GLU', 'CE1', 'HIS', 11.03), ('CG', 'GLU', 'NE2', 'HIS', 10.31)], [('CD', 'GLU', 'CB', 'HIS', 10.56), ('CD', 'GLU', 'CG', 'HIS', 10.03), ('CD', 'GLU', 'ND1', 'HIS', 10.6), ('CD', 'GLU', 'CD2', 'HIS', 9.19), ('CD', 'GLU', 'CE1', 'HIS', 10.2), ('CD', 'GLU', 'NE2', 'HIS', 9.33)], [('OE1', 'GLU', 'CB', 'HIS', 10.93), ('OE1', 'GLU', 'CG', 'HIS', 10.48), ('OE1', 'GLU', 'ND1', 'HIS', 11.2), ('OE1', 'GLU', 'CD2', 'HIS', 9.58), ('OE1', 'GLU', 'CE1', 'HIS', 10.84), ('OE1', 'GLU', 'NE2', 'HIS', 9.85)], [('OE2', 'GLU', 'CB', 'HIS', 9.8), ('OE2', 'GLU', 'CG', 'HIS', 9.11), ('OE2', 'GLU', 'ND1', 'HIS', 9.58), ('OE2', 'GLU', 'CD2', 'HIS', 8.22), ('OE2', 'GLU', 'CE1', 'HIS', 9.08), ('OE2', 'GLU', 'NE2', 'HIS', 8.22)], [('CB', 'GLU', 'CB', 'HIS', 17.21), ('CB', 'GLU', 'CG', 'HIS', 15.82), ('CB', 'GLU', 'ND1', 'HIS', 15.46), ('CB', 'GLU', 'CD2', 'HIS', 14.77), ('CB', 'GLU', 'CE1', 'HIS', 14.21), ('CB', 'GLU', 'NE2', 'HIS', 13.72)], [('CG', 'GLU', 'CB', 'HIS', 15.97), ('CG', 'GLU', 'CG', 'HIS', 14.56), ('CG', 'GLU', 'ND1', 'HIS', 14.13), ('CG', 'GLU', 'CD2', 'HIS', 13.58), ('CG', 'GLU', 'CE1', 'HIS', 12.87), ('CG', 'GLU', 'NE2', 'HIS', 12.48)], [('CD', 'GLU', 'CB', 'HIS', 14.7), ('CD', 'GLU', 'CG', 'HIS', 13.32), ('CD', 'GLU', 'ND1', 'HIS', 12.99), ('CD', 'GLU', 'CD2', 'HIS', 12.29), ('CD', 'GLU', 'CE1', 'HIS', 11.76), ('CD', 'GLU', 'NE2', 'HIS', 11.26)], [('OE1', 'GLU', 'CB', 'HIS', 14.89), ('OE1', 'GLU', 'CG', 'HIS', 13.57), ('OE1', 'GLU', 'ND1', 'HIS', 13.38), ('OE1', 'GLU', 'CD2', 'HIS', 12.5), ('OE1', 'GLU', 'CE1', 'HIS', 12.2), ('OE1', 'GLU', 'NE2', 'HIS', 11.59)], [('OE2', 'GLU', 'CB', 'HIS', 13.6), ('OE2', 'GLU', 'CG', 'HIS', 12.19), ('OE2', 'GLU', 'ND1', 'HIS', 11.82), ('OE2', 'GLU', 'CD2', 'HIS', 11.19), ('OE2', 'GLU', 'CE1', 'HIS', 10.57), ('OE2', 'GLU', 'NE2', 'HIS', 10.11)]]}
GLU_ALA = { 
	'distances':
		[[7.45], [6.0], [5.92], [6.77], [5.5]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ALA', 7.45)], [('CG', 'GLU', 'CB', 'ALA', 6.0)], [('CD', 'GLU', 'CB', 'ALA', 5.92)], [('OE1', 'GLU', 'CB', 'ALA', 6.77)], [('OE2', 'GLU', 'CB', 'ALA', 5.5)]]}
TYR_HISI = { 
	'distances':
		[[10.63, 9.78, 9.97, 9.08, 9.44, 8.86], [9.6, 8.64, 8.87, 7.79, 8.25, 7.53], [8.31, 7.45, 7.85, 6.64, 7.4, 6.62], [10.15, 9.02, 9.15, 8.01, 8.31, 7.52], [7.54, 6.56, 7.05, 5.54, 6.52, 5.53], [9.58, 8.36, 8.53, 7.22, 7.58, 6.65], [8.29, 7.12, 7.45, 5.92, 6.64, 5.55], [8.02, 6.8, 7.17, 5.48, 6.3, 5.08]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HISI', 10.63), ('CB', 'TYR', 'CG', 'HISI', 9.78), ('CB', 'TYR', 'ND1', 'HISI', 9.97), ('CB', 'TYR', 'CD2', 'HISI', 9.08), ('CB', 'TYR', 'CE1', 'HISI', 9.44), ('CB', 'TYR', 'NE2', 'HISI', 8.86)], [('CG', 'TYR', 'CB', 'HISI', 9.6), ('CG', 'TYR', 'CG', 'HISI', 8.64), ('CG', 'TYR', 'ND1', 'HISI', 8.87), ('CG', 'TYR', 'CD2', 'HISI', 7.79), ('CG', 'TYR', 'CE1', 'HISI', 8.25), ('CG', 'TYR', 'NE2', 'HISI', 7.53)], [('CD1', 'TYR', 'CB', 'HISI', 8.31), ('CD1', 'TYR', 'CG', 'HISI', 7.45), ('CD1', 'TYR', 'ND1', 'HISI', 7.85), ('CD1', 'TYR', 'CD2', 'HISI', 6.64), ('CD1', 'TYR', 'CE1', 'HISI', 7.4), ('CD1', 'TYR', 'NE2', 'HISI', 6.62)], [('CD2', 'TYR', 'CB', 'HISI', 10.15), ('CD2', 'TYR', 'CG', 'HISI', 9.02), ('CD2', 'TYR', 'ND1', 'HISI', 9.15), ('CD2', 'TYR', 'CD2', 'HISI', 8.01), ('CD2', 'TYR', 'CE1', 'HISI', 8.31), ('CD2', 'TYR', 'NE2', 'HISI', 7.52)], [('CE1', 'TYR', 'CB', 'HISI', 7.54), ('CE1', 'TYR', 'CG', 'HISI', 6.56), ('CE1', 'TYR', 'ND1', 'HISI', 7.05), ('CE1', 'TYR', 'CD2', 'HISI', 5.54), ('CE1', 'TYR', 'CE1', 'HISI', 6.52), ('CE1', 'TYR', 'NE2', 'HISI', 5.53)], [('CE2', 'TYR', 'CB', 'HISI', 9.58), ('CE2', 'TYR', 'CG', 'HISI', 8.36), ('CE2', 'TYR', 'ND1', 'HISI', 8.53), ('CE2', 'TYR', 'CD2', 'HISI', 7.22), ('CE2', 'TYR', 'CE1', 'HISI', 7.58), ('CE2', 'TYR', 'NE2', 'HISI', 6.65)], [('CZ', 'TYR', 'CB', 'HISI', 8.29), ('CZ', 'TYR', 'CG', 'HISI', 7.12), ('CZ', 'TYR', 'ND1', 'HISI', 7.45), ('CZ', 'TYR', 'CD2', 'HISI', 5.92), ('CZ', 'TYR', 'CE1', 'HISI', 6.64), ('CZ', 'TYR', 'NE2', 'HISI', 5.55)], [('OH', 'TYR', 'CB', 'HISI', 8.02), ('OH', 'TYR', 'CG', 'HISI', 6.8), ('OH', 'TYR', 'ND1', 'HISI', 7.17), ('OH', 'TYR', 'CD2', 'HISI', 5.48), ('OH', 'TYR', 'CE1', 'HISI', 6.3), ('OH', 'TYR', 'NE2', 'HISI', 5.08)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ALA, d, 'M_1o8a_3_4_15_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ZN, d, 'M_1o8a_3_4_15_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_HISI, d, 'M_1o8a_3_4_15_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_HIS, d, 'M_1o8a_3_4_15_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ALA_ZN, d, 'M_1o8a_3_4_15_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_TYR, d, 'M_1o8a_3_4_15_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ALA_TYR, d, 'M_1o8a_3_4_15_1')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(TYR_ZN, d, 'M_1o8a_3_4_15_1')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_TYR, d, 'M_1o8a_3_4_15_1')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ZN_HISI, d, 'M_1o8a_3_4_15_1')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(GLU_ZN, d, 'M_1o8a_3_4_15_1')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(GLU_HIS, d, 'M_1o8a_3_4_15_1')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(GLU_ALA, d, 'M_1o8a_3_4_15_1')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(TYR_HISI, d, 'M_1o8a_3_4_15_1')
	if match14 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ALA' :  match1,
		'HIS_ZN' :  match2,
		'ALA_HISI' :  match3,
		'HIS_HIS' :  match4,
		'ALA_ZN' :  match5,
		'GLU_TYR' :  match6,
		'ALA_TYR' :  match7,
		'TYR_ZN' :  match8,
		'HIS_TYR' :  match9,
		'ZN_HISI' :  match10,
		'GLU_ZN' :  match11,
		'GLU_HIS' :  match12,
		'GLU_ALA' :  match13,
		'TYR_HISI' :  match14}