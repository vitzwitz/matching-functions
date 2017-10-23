'''
FUNC:P_1cf3_1_1_3_4
PDB:1cf3
EC:1.1.3.4
RESI:glu,his,his
LOCI:a-412,516,559;
'''
import motifFunctions as cmd
HIS_HIS = { 
	'distances':
		[[9.53, 9.63, 9.09, 10.43, 9.61, 10.44, 9.85, 8.74, 8.59, 9.3], [8.08, 8.2, 7.66, 9.06, 8.26, 9.12, 8.6, 7.44, 7.22, 8.03], [7.23, 7.24, 6.82, 7.98, 7.35, 8.06, 7.82, 6.68, 6.27, 6.91], [7.51, 7.72, 7.12, 8.74, 7.87, 8.83, 8.21, 7.0, 6.85, 7.89], [5.97, 6.02, 5.6, 6.87, 6.27, 7.02, 6.87, 5.68, 5.15, 5.97], [6.15, 6.34, 5.79, 7.39, 6.62, 7.54, 7.11, 5.88, 5.56, 6.65], [11.4, 11.74, 11.4, 12.56, 12.02, 12.74, 11.01, 10.06, 10.26, 10.85], [11.56, 11.86, 11.38, 12.74, 12.0, 12.84, 11.42, 10.4, 10.55, 11.29], [10.52, 10.72, 10.13, 11.63, 10.73, 11.65, 10.75, 9.64, 9.65, 10.49], [11.25, 11.29, 10.53, 12.16, 11.0, 12.01, 11.83, 10.67, 10.52, 11.39], [9.53, 8.08, 7.23, 7.51, 5.97, 6.15, 11.4, 11.56, 10.52, 11.25], [9.63, 8.2, 7.24, 7.72, 6.02, 6.34, 11.74, 11.86, 10.72, 11.29], [9.09, 7.66, 6.82, 7.12, 5.6, 5.79, 11.4, 11.38, 10.13, 10.53], [10.43, 9.06, 7.98, 8.74, 6.87, 7.39, 12.56, 12.74, 11.63, 12.16], [9.61, 8.26, 7.35, 7.87, 6.27, 6.62, 12.02, 12.0, 10.73, 11.0], [10.44, 9.12, 8.06, 8.83, 7.02, 7.54, 12.74, 12.84, 11.65, 12.01], [9.85, 8.6, 7.82, 8.21, 6.87, 7.11, 11.01, 11.42, 10.75, 11.83], [8.74, 7.44, 6.68, 7.0, 5.68, 5.88, 10.06, 10.4, 9.64, 10.67], [8.59, 7.22, 6.27, 6.85, 5.15, 5.56, 10.26, 10.55, 9.65, 10.52], [9.3, 8.03, 6.91, 7.89, 5.97, 6.65, 10.85, 11.29, 10.49, 11.39]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 9.53), ('CB', 'HIS', 'CG', 'HIS', 9.63), ('CB', 'HIS', 'ND1', 'HIS', 9.09), ('CB', 'HIS', 'CD2', 'HIS', 10.43), ('CB', 'HIS', 'CE1', 'HIS', 9.61), ('CB', 'HIS', 'NE2', 'HIS', 10.44), ('CB', 'HIS', 'O', 'HIS', 9.85), ('CB', 'HIS', 'C', 'HIS', 8.74), ('CB', 'HIS', 'CA', 'HIS', 8.59), ('CB', 'HIS', 'N', 'HIS', 9.3)], [('CG', 'HIS', 'CB', 'HIS', 8.08), ('CG', 'HIS', 'CG', 'HIS', 8.2), ('CG', 'HIS', 'ND1', 'HIS', 7.66), ('CG', 'HIS', 'CD2', 'HIS', 9.06), ('CG', 'HIS', 'CE1', 'HIS', 8.26), ('CG', 'HIS', 'NE2', 'HIS', 9.12), ('CG', 'HIS', 'O', 'HIS', 8.6), ('CG', 'HIS', 'C', 'HIS', 7.44), ('CG', 'HIS', 'CA', 'HIS', 7.22), ('CG', 'HIS', 'N', 'HIS', 8.03)], [('ND1', 'HIS', 'CB', 'HIS', 7.23), ('ND1', 'HIS', 'CG', 'HIS', 7.24), ('ND1', 'HIS', 'ND1', 'HIS', 6.82), ('ND1', 'HIS', 'CD2', 'HIS', 7.98), ('ND1', 'HIS', 'CE1', 'HIS', 7.35), ('ND1', 'HIS', 'NE2', 'HIS', 8.06), ('ND1', 'HIS', 'O', 'HIS', 7.82), ('ND1', 'HIS', 'C', 'HIS', 6.68), ('ND1', 'HIS', 'CA', 'HIS', 6.27), ('ND1', 'HIS', 'N', 'HIS', 6.91)], [('CD2', 'HIS', 'CB', 'HIS', 7.51), ('CD2', 'HIS', 'CG', 'HIS', 7.72), ('CD2', 'HIS', 'ND1', 'HIS', 7.12), ('CD2', 'HIS', 'CD2', 'HIS', 8.74), ('CD2', 'HIS', 'CE1', 'HIS', 7.87), ('CD2', 'HIS', 'NE2', 'HIS', 8.83), ('CD2', 'HIS', 'O', 'HIS', 8.21), ('CD2', 'HIS', 'C', 'HIS', 7.0), ('CD2', 'HIS', 'CA', 'HIS', 6.85), ('CD2', 'HIS', 'N', 'HIS', 7.89)], [('CE1', 'HIS', 'CB', 'HIS', 5.97), ('CE1', 'HIS', 'CG', 'HIS', 6.02), ('CE1', 'HIS', 'ND1', 'HIS', 5.6), ('CE1', 'HIS', 'CD2', 'HIS', 6.87), ('CE1', 'HIS', 'CE1', 'HIS', 6.27), ('CE1', 'HIS', 'NE2', 'HIS', 7.02), ('CE1', 'HIS', 'O', 'HIS', 6.87), ('CE1', 'HIS', 'C', 'HIS', 5.68), ('CE1', 'HIS', 'CA', 'HIS', 5.15), ('CE1', 'HIS', 'N', 'HIS', 5.97)], [('NE2', 'HIS', 'CB', 'HIS', 6.15), ('NE2', 'HIS', 'CG', 'HIS', 6.34), ('NE2', 'HIS', 'ND1', 'HIS', 5.79), ('NE2', 'HIS', 'CD2', 'HIS', 7.39), ('NE2', 'HIS', 'CE1', 'HIS', 6.62), ('NE2', 'HIS', 'NE2', 'HIS', 7.54), ('NE2', 'HIS', 'O', 'HIS', 7.11), ('NE2', 'HIS', 'C', 'HIS', 5.88), ('NE2', 'HIS', 'CA', 'HIS', 5.56), ('NE2', 'HIS', 'N', 'HIS', 6.65)], [('O', 'HIS', 'CB', 'HIS', 11.4), ('O', 'HIS', 'CG', 'HIS', 11.74), ('O', 'HIS', 'ND1', 'HIS', 11.4), ('O', 'HIS', 'CD2', 'HIS', 12.56), ('O', 'HIS', 'CE1', 'HIS', 12.02), ('O', 'HIS', 'NE2', 'HIS', 12.74), ('O', 'HIS', 'O', 'HIS', 11.01), ('O', 'HIS', 'C', 'HIS', 10.06), ('O', 'HIS', 'CA', 'HIS', 10.26), ('O', 'HIS', 'N', 'HIS', 10.85)], [('C', 'HIS', 'CB', 'HIS', 11.56), ('C', 'HIS', 'CG', 'HIS', 11.86), ('C', 'HIS', 'ND1', 'HIS', 11.38), ('C', 'HIS', 'CD2', 'HIS', 12.74), ('C', 'HIS', 'CE1', 'HIS', 12.0), ('C', 'HIS', 'NE2', 'HIS', 12.84), ('C', 'HIS', 'O', 'HIS', 11.42), ('C', 'HIS', 'C', 'HIS', 10.4), ('C', 'HIS', 'CA', 'HIS', 10.55), ('C', 'HIS', 'N', 'HIS', 11.29)], [('CA', 'HIS', 'CB', 'HIS', 10.52), ('CA', 'HIS', 'CG', 'HIS', 10.72), ('CA', 'HIS', 'ND1', 'HIS', 10.13), ('CA', 'HIS', 'CD2', 'HIS', 11.63), ('CA', 'HIS', 'CE1', 'HIS', 10.73), ('CA', 'HIS', 'NE2', 'HIS', 11.65), ('CA', 'HIS', 'O', 'HIS', 10.75), ('CA', 'HIS', 'C', 'HIS', 9.64), ('CA', 'HIS', 'CA', 'HIS', 9.65), ('CA', 'HIS', 'N', 'HIS', 10.49)], [('N', 'HIS', 'CB', 'HIS', 11.25), ('N', 'HIS', 'CG', 'HIS', 11.29), ('N', 'HIS', 'ND1', 'HIS', 10.53), ('N', 'HIS', 'CD2', 'HIS', 12.16), ('N', 'HIS', 'CE1', 'HIS', 11.0), ('N', 'HIS', 'NE2', 'HIS', 12.01), ('N', 'HIS', 'O', 'HIS', 11.83), ('N', 'HIS', 'C', 'HIS', 10.67), ('N', 'HIS', 'CA', 'HIS', 10.52), ('N', 'HIS', 'N', 'HIS', 11.39)], [('CB', 'HIS', 'CB', 'HIS', 9.53), ('CB', 'HIS', 'CG', 'HIS', 8.08), ('CB', 'HIS', 'ND1', 'HIS', 7.23), ('CB', 'HIS', 'CD2', 'HIS', 7.51), ('CB', 'HIS', 'CE1', 'HIS', 5.97), ('CB', 'HIS', 'NE2', 'HIS', 6.15), ('CB', 'HIS', 'O', 'HIS', 11.4), ('CB', 'HIS', 'C', 'HIS', 11.56), ('CB', 'HIS', 'CA', 'HIS', 10.52), ('CB', 'HIS', 'N', 'HIS', 11.25)], [('CG', 'HIS', 'CB', 'HIS', 9.63), ('CG', 'HIS', 'CG', 'HIS', 8.2), ('CG', 'HIS', 'ND1', 'HIS', 7.24), ('CG', 'HIS', 'CD2', 'HIS', 7.72), ('CG', 'HIS', 'CE1', 'HIS', 6.02), ('CG', 'HIS', 'NE2', 'HIS', 6.34), ('CG', 'HIS', 'O', 'HIS', 11.74), ('CG', 'HIS', 'C', 'HIS', 11.86), ('CG', 'HIS', 'CA', 'HIS', 10.72), ('CG', 'HIS', 'N', 'HIS', 11.29)], [('ND1', 'HIS', 'CB', 'HIS', 9.09), ('ND1', 'HIS', 'CG', 'HIS', 7.66), ('ND1', 'HIS', 'ND1', 'HIS', 6.82), ('ND1', 'HIS', 'CD2', 'HIS', 7.12), ('ND1', 'HIS', 'CE1', 'HIS', 5.6), ('ND1', 'HIS', 'NE2', 'HIS', 5.79), ('ND1', 'HIS', 'O', 'HIS', 11.4), ('ND1', 'HIS', 'C', 'HIS', 11.38), ('ND1', 'HIS', 'CA', 'HIS', 10.13), ('ND1', 'HIS', 'N', 'HIS', 10.53)], [('CD2', 'HIS', 'CB', 'HIS', 10.43), ('CD2', 'HIS', 'CG', 'HIS', 9.06), ('CD2', 'HIS', 'ND1', 'HIS', 7.98), ('CD2', 'HIS', 'CD2', 'HIS', 8.74), ('CD2', 'HIS', 'CE1', 'HIS', 6.87), ('CD2', 'HIS', 'NE2', 'HIS', 7.39), ('CD2', 'HIS', 'O', 'HIS', 12.56), ('CD2', 'HIS', 'C', 'HIS', 12.74), ('CD2', 'HIS', 'CA', 'HIS', 11.63), ('CD2', 'HIS', 'N', 'HIS', 12.16)], [('CE1', 'HIS', 'CB', 'HIS', 9.61), ('CE1', 'HIS', 'CG', 'HIS', 8.26), ('CE1', 'HIS', 'ND1', 'HIS', 7.35), ('CE1', 'HIS', 'CD2', 'HIS', 7.87), ('CE1', 'HIS', 'CE1', 'HIS', 6.27), ('CE1', 'HIS', 'NE2', 'HIS', 6.62), ('CE1', 'HIS', 'O', 'HIS', 12.02), ('CE1', 'HIS', 'C', 'HIS', 12.0), ('CE1', 'HIS', 'CA', 'HIS', 10.73), ('CE1', 'HIS', 'N', 'HIS', 11.0)], [('NE2', 'HIS', 'CB', 'HIS', 10.44), ('NE2', 'HIS', 'CG', 'HIS', 9.12), ('NE2', 'HIS', 'ND1', 'HIS', 8.06), ('NE2', 'HIS', 'CD2', 'HIS', 8.83), ('NE2', 'HIS', 'CE1', 'HIS', 7.02), ('NE2', 'HIS', 'NE2', 'HIS', 7.54), ('NE2', 'HIS', 'O', 'HIS', 12.74), ('NE2', 'HIS', 'C', 'HIS', 12.84), ('NE2', 'HIS', 'CA', 'HIS', 11.65), ('NE2', 'HIS', 'N', 'HIS', 12.01)], [('O', 'HIS', 'CB', 'HIS', 9.85), ('O', 'HIS', 'CG', 'HIS', 8.6), ('O', 'HIS', 'ND1', 'HIS', 7.82), ('O', 'HIS', 'CD2', 'HIS', 8.21), ('O', 'HIS', 'CE1', 'HIS', 6.87), ('O', 'HIS', 'NE2', 'HIS', 7.11), ('O', 'HIS', 'O', 'HIS', 11.01), ('O', 'HIS', 'C', 'HIS', 11.42), ('O', 'HIS', 'CA', 'HIS', 10.75), ('O', 'HIS', 'N', 'HIS', 11.83)], [('C', 'HIS', 'CB', 'HIS', 8.74), ('C', 'HIS', 'CG', 'HIS', 7.44), ('C', 'HIS', 'ND1', 'HIS', 6.68), ('C', 'HIS', 'CD2', 'HIS', 7.0), ('C', 'HIS', 'CE1', 'HIS', 5.68), ('C', 'HIS', 'NE2', 'HIS', 5.88), ('C', 'HIS', 'O', 'HIS', 10.06), ('C', 'HIS', 'C', 'HIS', 10.4), ('C', 'HIS', 'CA', 'HIS', 9.64), ('C', 'HIS', 'N', 'HIS', 10.67)], [('CA', 'HIS', 'CB', 'HIS', 8.59), ('CA', 'HIS', 'CG', 'HIS', 7.22), ('CA', 'HIS', 'ND1', 'HIS', 6.27), ('CA', 'HIS', 'CD2', 'HIS', 6.85), ('CA', 'HIS', 'CE1', 'HIS', 5.15), ('CA', 'HIS', 'NE2', 'HIS', 5.56), ('CA', 'HIS', 'O', 'HIS', 10.26), ('CA', 'HIS', 'C', 'HIS', 10.55), ('CA', 'HIS', 'CA', 'HIS', 9.65), ('CA', 'HIS', 'N', 'HIS', 10.52)], [('N', 'HIS', 'CB', 'HIS', 9.3), ('N', 'HIS', 'CG', 'HIS', 8.03), ('N', 'HIS', 'ND1', 'HIS', 6.91), ('N', 'HIS', 'CD2', 'HIS', 7.89), ('N', 'HIS', 'CE1', 'HIS', 5.97), ('N', 'HIS', 'NE2', 'HIS', 6.65), ('N', 'HIS', 'O', 'HIS', 10.85), ('N', 'HIS', 'C', 'HIS', 11.29), ('N', 'HIS', 'CA', 'HIS', 10.49), ('N', 'HIS', 'N', 'HIS', 11.39)]]}
HIS_GLU = { 
	'distances':
		[[11.79, 12.23, 11.31, 10.26, 11.75, 13.0, 13.5, 12.99, 12.86], [11.07, 11.34, 10.3, 9.26, 10.62, 12.49, 12.89, 12.37, 12.4], [9.82, 10.09, 9.05, 7.97, 9.45, 11.42, 11.75, 11.14, 11.2], [11.56, 11.64, 10.48, 9.52, 10.63, 13.02, 13.39, 12.93, 13.11], [9.59, 9.65, 8.46, 7.44, 8.69, 11.37, 11.59, 11.01, 11.25], [10.7, 10.64, 9.4, 8.46, 9.47, 12.36, 12.62, 12.12, 12.43], [13.75, 14.33, 13.48, 12.34, 14.02, 15.04, 15.53, 14.87, 14.55], [14.12, 14.63, 13.75, 12.66, 14.21, 15.26, 15.81, 15.26, 15.0], [13.27, 13.67, 12.73, 11.7, 13.09, 14.38, 14.92, 14.46, 14.33], [13.47, 13.88, 13.0, 12.06, 13.34, 14.26, 14.91, 14.6, 14.47], [9.69, 9.0, 7.52, 6.92, 7.14, 12.13, 11.85, 11.2, 11.98], [8.5, 7.71, 6.21, 5.75, 5.73, 10.81, 10.54, 10.0, 10.87], [8.45, 7.68, 6.21, 5.81, 5.68, 10.41, 10.28, 9.93, 10.79], [7.53, 6.61, 5.14, 4.84, 4.59, 9.93, 9.54, 8.98, 9.94], [7.46, 6.6, 5.18, 4.99, 4.55, 9.26, 9.13, 8.89, 9.84], [6.83, 5.82, 4.36, 4.3, 3.64, 8.92, 8.61, 8.25, 9.29], [11.38, 10.95, 9.61, 8.77, 9.53, 14.11, 13.78, 12.83, 13.38], [10.89, 10.51, 9.14, 8.25, 9.07, 13.48, 13.25, 12.38, 12.9], [9.51, 9.07, 7.66, 6.81, 7.56, 12.06, 11.82, 11.01, 11.62], [8.77, 8.36, 7.06, 6.18, 7.1, 11.53, 11.17, 10.22, 10.8]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 11.79), ('CB', 'HIS', 'CG', 'GLU', 12.23), ('CB', 'HIS', 'CD', 'GLU', 11.31), ('CB', 'HIS', 'OE1', 'GLU', 10.26), ('CB', 'HIS', 'OE2', 'GLU', 11.75), ('CB', 'HIS', 'O', 'GLU', 13.0), ('CB', 'HIS', 'C', 'GLU', 13.5), ('CB', 'HIS', 'CA', 'GLU', 12.99), ('CB', 'HIS', 'N', 'GLU', 12.86)], [('CG', 'HIS', 'CB', 'GLU', 11.07), ('CG', 'HIS', 'CG', 'GLU', 11.34), ('CG', 'HIS', 'CD', 'GLU', 10.3), ('CG', 'HIS', 'OE1', 'GLU', 9.26), ('CG', 'HIS', 'OE2', 'GLU', 10.62), ('CG', 'HIS', 'O', 'GLU', 12.49), ('CG', 'HIS', 'C', 'GLU', 12.89), ('CG', 'HIS', 'CA', 'GLU', 12.37), ('CG', 'HIS', 'N', 'GLU', 12.4)], [('ND1', 'HIS', 'CB', 'GLU', 9.82), ('ND1', 'HIS', 'CG', 'GLU', 10.09), ('ND1', 'HIS', 'CD', 'GLU', 9.05), ('ND1', 'HIS', 'OE1', 'GLU', 7.97), ('ND1', 'HIS', 'OE2', 'GLU', 9.45), ('ND1', 'HIS', 'O', 'GLU', 11.42), ('ND1', 'HIS', 'C', 'GLU', 11.75), ('ND1', 'HIS', 'CA', 'GLU', 11.14), ('ND1', 'HIS', 'N', 'GLU', 11.2)], [('CD2', 'HIS', 'CB', 'GLU', 11.56), ('CD2', 'HIS', 'CG', 'GLU', 11.64), ('CD2', 'HIS', 'CD', 'GLU', 10.48), ('CD2', 'HIS', 'OE1', 'GLU', 9.52), ('CD2', 'HIS', 'OE2', 'GLU', 10.63), ('CD2', 'HIS', 'O', 'GLU', 13.02), ('CD2', 'HIS', 'C', 'GLU', 13.39), ('CD2', 'HIS', 'CA', 'GLU', 12.93), ('CD2', 'HIS', 'N', 'GLU', 13.11)], [('CE1', 'HIS', 'CB', 'GLU', 9.59), ('CE1', 'HIS', 'CG', 'GLU', 9.65), ('CE1', 'HIS', 'CD', 'GLU', 8.46), ('CE1', 'HIS', 'OE1', 'GLU', 7.44), ('CE1', 'HIS', 'OE2', 'GLU', 8.69), ('CE1', 'HIS', 'O', 'GLU', 11.37), ('CE1', 'HIS', 'C', 'GLU', 11.59), ('CE1', 'HIS', 'CA', 'GLU', 11.01), ('CE1', 'HIS', 'N', 'GLU', 11.25)], [('NE2', 'HIS', 'CB', 'GLU', 10.7), ('NE2', 'HIS', 'CG', 'GLU', 10.64), ('NE2', 'HIS', 'CD', 'GLU', 9.4), ('NE2', 'HIS', 'OE1', 'GLU', 8.46), ('NE2', 'HIS', 'OE2', 'GLU', 9.47), ('NE2', 'HIS', 'O', 'GLU', 12.36), ('NE2', 'HIS', 'C', 'GLU', 12.62), ('NE2', 'HIS', 'CA', 'GLU', 12.12), ('NE2', 'HIS', 'N', 'GLU', 12.43)], [('O', 'HIS', 'CB', 'GLU', 13.75), ('O', 'HIS', 'CG', 'GLU', 14.33), ('O', 'HIS', 'CD', 'GLU', 13.48), ('O', 'HIS', 'OE1', 'GLU', 12.34), ('O', 'HIS', 'OE2', 'GLU', 14.02), ('O', 'HIS', 'O', 'GLU', 15.04), ('O', 'HIS', 'C', 'GLU', 15.53), ('O', 'HIS', 'CA', 'GLU', 14.87), ('O', 'HIS', 'N', 'GLU', 14.55)], [('C', 'HIS', 'CB', 'GLU', 14.12), ('C', 'HIS', 'CG', 'GLU', 14.63), ('C', 'HIS', 'CD', 'GLU', 13.75), ('C', 'HIS', 'OE1', 'GLU', 12.66), ('C', 'HIS', 'OE2', 'GLU', 14.21), ('C', 'HIS', 'O', 'GLU', 15.26), ('C', 'HIS', 'C', 'GLU', 15.81), ('C', 'HIS', 'CA', 'GLU', 15.26), ('C', 'HIS', 'N', 'GLU', 15.0)], [('CA', 'HIS', 'CB', 'GLU', 13.27), ('CA', 'HIS', 'CG', 'GLU', 13.67), ('CA', 'HIS', 'CD', 'GLU', 12.73), ('CA', 'HIS', 'OE1', 'GLU', 11.7), ('CA', 'HIS', 'OE2', 'GLU', 13.09), ('CA', 'HIS', 'O', 'GLU', 14.38), ('CA', 'HIS', 'C', 'GLU', 14.92), ('CA', 'HIS', 'CA', 'GLU', 14.46), ('CA', 'HIS', 'N', 'GLU', 14.33)], [('N', 'HIS', 'CB', 'GLU', 13.47), ('N', 'HIS', 'CG', 'GLU', 13.88), ('N', 'HIS', 'CD', 'GLU', 13.0), ('N', 'HIS', 'OE1', 'GLU', 12.06), ('N', 'HIS', 'OE2', 'GLU', 13.34), ('N', 'HIS', 'O', 'GLU', 14.26), ('N', 'HIS', 'C', 'GLU', 14.91), ('N', 'HIS', 'CA', 'GLU', 14.6), ('N', 'HIS', 'N', 'GLU', 14.47)], [('CB', 'HIS', 'CB', 'GLU', 9.69), ('CB', 'HIS', 'CG', 'GLU', 9.0), ('CB', 'HIS', 'CD', 'GLU', 7.52), ('CB', 'HIS', 'OE1', 'GLU', 6.92), ('CB', 'HIS', 'OE2', 'GLU', 7.14), ('CB', 'HIS', 'O', 'GLU', 12.13), ('CB', 'HIS', 'C', 'GLU', 11.85), ('CB', 'HIS', 'CA', 'GLU', 11.2), ('CB', 'HIS', 'N', 'GLU', 11.98)], [('CG', 'HIS', 'CB', 'GLU', 8.5), ('CG', 'HIS', 'CG', 'GLU', 7.71), ('CG', 'HIS', 'CD', 'GLU', 6.21), ('CG', 'HIS', 'OE1', 'GLU', 5.75), ('CG', 'HIS', 'OE2', 'GLU', 5.73), ('CG', 'HIS', 'O', 'GLU', 10.81), ('CG', 'HIS', 'C', 'GLU', 10.54), ('CG', 'HIS', 'CA', 'GLU', 10.0), ('CG', 'HIS', 'N', 'GLU', 10.87)], [('ND1', 'HIS', 'CB', 'GLU', 8.45), ('ND1', 'HIS', 'CG', 'GLU', 7.68), ('ND1', 'HIS', 'CD', 'GLU', 6.21), ('ND1', 'HIS', 'OE1', 'GLU', 5.81), ('ND1', 'HIS', 'OE2', 'GLU', 5.68), ('ND1', 'HIS', 'O', 'GLU', 10.41), ('ND1', 'HIS', 'C', 'GLU', 10.28), ('ND1', 'HIS', 'CA', 'GLU', 9.93), ('ND1', 'HIS', 'N', 'GLU', 10.79)], [('CD2', 'HIS', 'CB', 'GLU', 7.53), ('CD2', 'HIS', 'CG', 'GLU', 6.61), ('CD2', 'HIS', 'CD', 'GLU', 5.14), ('CD2', 'HIS', 'OE1', 'GLU', 4.84), ('CD2', 'HIS', 'OE2', 'GLU', 4.59), ('CD2', 'HIS', 'O', 'GLU', 9.93), ('CD2', 'HIS', 'C', 'GLU', 9.54), ('CD2', 'HIS', 'CA', 'GLU', 8.98), ('CD2', 'HIS', 'N', 'GLU', 9.94)], [('CE1', 'HIS', 'CB', 'GLU', 7.46), ('CE1', 'HIS', 'CG', 'GLU', 6.6), ('CE1', 'HIS', 'CD', 'GLU', 5.18), ('CE1', 'HIS', 'OE1', 'GLU', 4.99), ('CE1', 'HIS', 'OE2', 'GLU', 4.55), ('CE1', 'HIS', 'O', 'GLU', 9.26), ('CE1', 'HIS', 'C', 'GLU', 9.13), ('CE1', 'HIS', 'CA', 'GLU', 8.89), ('CE1', 'HIS', 'N', 'GLU', 9.84)], [('NE2', 'HIS', 'CB', 'GLU', 6.83), ('NE2', 'HIS', 'CG', 'GLU', 5.82), ('NE2', 'HIS', 'CD', 'GLU', 4.36), ('NE2', 'HIS', 'OE1', 'GLU', 4.3), ('NE2', 'HIS', 'OE2', 'GLU', 3.64), ('NE2', 'HIS', 'O', 'GLU', 8.92), ('NE2', 'HIS', 'C', 'GLU', 8.61), ('NE2', 'HIS', 'CA', 'GLU', 8.25), ('NE2', 'HIS', 'N', 'GLU', 9.29)], [('O', 'HIS', 'CB', 'GLU', 11.38), ('O', 'HIS', 'CG', 'GLU', 10.95), ('O', 'HIS', 'CD', 'GLU', 9.61), ('O', 'HIS', 'OE1', 'GLU', 8.77), ('O', 'HIS', 'OE2', 'GLU', 9.53), ('O', 'HIS', 'O', 'GLU', 14.11), ('O', 'HIS', 'C', 'GLU', 13.78), ('O', 'HIS', 'CA', 'GLU', 12.83), ('O', 'HIS', 'N', 'GLU', 13.38)], [('C', 'HIS', 'CB', 'GLU', 10.89), ('C', 'HIS', 'CG', 'GLU', 10.51), ('C', 'HIS', 'CD', 'GLU', 9.14), ('C', 'HIS', 'OE1', 'GLU', 8.25), ('C', 'HIS', 'OE2', 'GLU', 9.07), ('C', 'HIS', 'O', 'GLU', 13.48), ('C', 'HIS', 'C', 'GLU', 13.25), ('C', 'HIS', 'CA', 'GLU', 12.38), ('C', 'HIS', 'N', 'GLU', 12.9)], [('CA', 'HIS', 'CB', 'GLU', 9.51), ('CA', 'HIS', 'CG', 'GLU', 9.07), ('CA', 'HIS', 'CD', 'GLU', 7.66), ('CA', 'HIS', 'OE1', 'GLU', 6.81), ('CA', 'HIS', 'OE2', 'GLU', 7.56), ('CA', 'HIS', 'O', 'GLU', 12.06), ('CA', 'HIS', 'C', 'GLU', 11.82), ('CA', 'HIS', 'CA', 'GLU', 11.01), ('CA', 'HIS', 'N', 'GLU', 11.62)], [('N', 'HIS', 'CB', 'GLU', 8.77), ('N', 'HIS', 'CG', 'GLU', 8.36), ('N', 'HIS', 'CD', 'GLU', 7.06), ('N', 'HIS', 'OE1', 'GLU', 6.18), ('N', 'HIS', 'OE2', 'GLU', 7.1), ('N', 'HIS', 'O', 'GLU', 11.53), ('N', 'HIS', 'C', 'GLU', 11.17), ('N', 'HIS', 'CA', 'GLU', 10.22), ('N', 'HIS', 'N', 'GLU', 10.8)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_HIS, d, 'P_1cf3_1_1_3_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_GLU, d, 'P_1cf3_1_1_3_4')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_HIS' :  match1,
		'HIS_GLU' :  match2}