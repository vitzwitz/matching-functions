'''
FUNC:A_1bsj_3_5_1_88
PDB:1bsj
EC:3.5.1.88
RESI:gly,gln,leu,glu
LOCI:a-45,50,91,133;
'''
import motifFunctions as cmd
GLU_GLN = { 
	'distances':
		[[10.91, 9.87, 9.13, 8.06, 9.91, 13.95, 13.02, 11.83, 11.26], [10.75, 9.75, 8.77, 7.66, 9.38, 13.81, 12.97, 11.85, 11.47], [9.46, 8.43, 7.35, 6.28, 7.89, 12.53, 11.76, 10.64, 10.42], [8.36, 7.37, 6.42, 5.3, 7.15, 11.43, 10.62, 9.49, 9.2], [9.7, 8.64, 7.39, 6.45, 7.66, 12.73, 12.09, 10.99, 10.95], [10.16, 9.07, 8.92, 8.14, 9.94, 13.01, 12.0, 10.66, 9.81], [10.94, 9.77, 9.43, 8.58, 10.33, 13.88, 12.91, 11.57, 10.81], [10.61, 9.41, 8.79, 7.88, 9.55, 13.66, 12.77, 11.46, 10.89], [11.54, 10.25, 9.52, 8.69, 10.09, 14.62, 13.8, 12.45, 12.0]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLN', 10.91), ('CB', 'GLU', 'CG', 'GLN', 9.87), ('CB', 'GLU', 'CD', 'GLN', 9.13), ('CB', 'GLU', 'OE1', 'GLN', 8.06), ('CB', 'GLU', 'NE2', 'GLN', 9.91), ('CB', 'GLU', 'O', 'GLN', 13.95), ('CB', 'GLU', 'C', 'GLN', 13.02), ('CB', 'GLU', 'CA', 'GLN', 11.83), ('CB', 'GLU', 'N', 'GLN', 11.26)], [('CG', 'GLU', 'CB', 'GLN', 10.75), ('CG', 'GLU', 'CG', 'GLN', 9.75), ('CG', 'GLU', 'CD', 'GLN', 8.77), ('CG', 'GLU', 'OE1', 'GLN', 7.66), ('CG', 'GLU', 'NE2', 'GLN', 9.38), ('CG', 'GLU', 'O', 'GLN', 13.81), ('CG', 'GLU', 'C', 'GLN', 12.97), ('CG', 'GLU', 'CA', 'GLN', 11.85), ('CG', 'GLU', 'N', 'GLN', 11.47)], [('CD', 'GLU', 'CB', 'GLN', 9.46), ('CD', 'GLU', 'CG', 'GLN', 8.43), ('CD', 'GLU', 'CD', 'GLN', 7.35), ('CD', 'GLU', 'OE1', 'GLN', 6.28), ('CD', 'GLU', 'NE2', 'GLN', 7.89), ('CD', 'GLU', 'O', 'GLN', 12.53), ('CD', 'GLU', 'C', 'GLN', 11.76), ('CD', 'GLU', 'CA', 'GLN', 10.64), ('CD', 'GLU', 'N', 'GLN', 10.42)], [('OE1', 'GLU', 'CB', 'GLN', 8.36), ('OE1', 'GLU', 'CG', 'GLN', 7.37), ('OE1', 'GLU', 'CD', 'GLN', 6.42), ('OE1', 'GLU', 'OE1', 'GLN', 5.3), ('OE1', 'GLU', 'NE2', 'GLN', 7.15), ('OE1', 'GLU', 'O', 'GLN', 11.43), ('OE1', 'GLU', 'C', 'GLN', 10.62), ('OE1', 'GLU', 'CA', 'GLN', 9.49), ('OE1', 'GLU', 'N', 'GLN', 9.2)], [('OE2', 'GLU', 'CB', 'GLN', 9.7), ('OE2', 'GLU', 'CG', 'GLN', 8.64), ('OE2', 'GLU', 'CD', 'GLN', 7.39), ('OE2', 'GLU', 'OE1', 'GLN', 6.45), ('OE2', 'GLU', 'NE2', 'GLN', 7.66), ('OE2', 'GLU', 'O', 'GLN', 12.73), ('OE2', 'GLU', 'C', 'GLN', 12.09), ('OE2', 'GLU', 'CA', 'GLN', 10.99), ('OE2', 'GLU', 'N', 'GLN', 10.95)], [('O', 'GLU', 'CB', 'GLN', 10.16), ('O', 'GLU', 'CG', 'GLN', 9.07), ('O', 'GLU', 'CD', 'GLN', 8.92), ('O', 'GLU', 'OE1', 'GLN', 8.14), ('O', 'GLU', 'NE2', 'GLN', 9.94), ('O', 'GLU', 'O', 'GLN', 13.01), ('O', 'GLU', 'C', 'GLN', 12.0), ('O', 'GLU', 'CA', 'GLN', 10.66), ('O', 'GLU', 'N', 'GLN', 9.81)], [('C', 'GLU', 'CB', 'GLN', 10.94), ('C', 'GLU', 'CG', 'GLN', 9.77), ('C', 'GLU', 'CD', 'GLN', 9.43), ('C', 'GLU', 'OE1', 'GLN', 8.58), ('C', 'GLU', 'NE2', 'GLN', 10.33), ('C', 'GLU', 'O', 'GLN', 13.88), ('C', 'GLU', 'C', 'GLN', 12.91), ('C', 'GLU', 'CA', 'GLN', 11.57), ('C', 'GLU', 'N', 'GLN', 10.81)], [('CA', 'GLU', 'CB', 'GLN', 10.61), ('CA', 'GLU', 'CG', 'GLN', 9.41), ('CA', 'GLU', 'CD', 'GLN', 8.79), ('CA', 'GLU', 'OE1', 'GLN', 7.88), ('CA', 'GLU', 'NE2', 'GLN', 9.55), ('CA', 'GLU', 'O', 'GLN', 13.66), ('CA', 'GLU', 'C', 'GLN', 12.77), ('CA', 'GLU', 'CA', 'GLN', 11.46), ('CA', 'GLU', 'N', 'GLN', 10.89)], [('N', 'GLU', 'CB', 'GLN', 11.54), ('N', 'GLU', 'CG', 'GLN', 10.25), ('N', 'GLU', 'CD', 'GLN', 9.52), ('N', 'GLU', 'OE1', 'GLN', 8.69), ('N', 'GLU', 'NE2', 'GLN', 10.09), ('N', 'GLU', 'O', 'GLN', 14.62), ('N', 'GLU', 'C', 'GLN', 13.8), ('N', 'GLU', 'CA', 'GLN', 12.45), ('N', 'GLU', 'N', 'GLN', 12.0)]]}
GLY_GLN = { 
	'distances':
		[[9.21, 8.8, 7.4, 6.56, 7.38, 11.73, 11.26, 10.67, 10.96], [9.64, 9.19, 7.87, 6.86, 8.08, 12.27, 11.67, 11.03, 11.13], [11.11, 10.58, 9.24, 8.21, 9.42, 13.78, 13.18, 12.49, 12.54], [11.8, 11.29, 9.87, 8.97, 9.82, 14.36, 13.87, 13.25, 13.45]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLN', 9.21), ('O', 'GLY', 'CG', 'GLN', 8.8), ('O', 'GLY', 'CD', 'GLN', 7.4), ('O', 'GLY', 'OE1', 'GLN', 6.56), ('O', 'GLY', 'NE2', 'GLN', 7.38), ('O', 'GLY', 'O', 'GLN', 11.73), ('O', 'GLY', 'C', 'GLN', 11.26), ('O', 'GLY', 'CA', 'GLN', 10.67), ('O', 'GLY', 'N', 'GLN', 10.96)], [('C', 'GLY', 'CB', 'GLN', 9.64), ('C', 'GLY', 'CG', 'GLN', 9.19), ('C', 'GLY', 'CD', 'GLN', 7.87), ('C', 'GLY', 'OE1', 'GLN', 6.86), ('C', 'GLY', 'NE2', 'GLN', 8.08), ('C', 'GLY', 'O', 'GLN', 12.27), ('C', 'GLY', 'C', 'GLN', 11.67), ('C', 'GLY', 'CA', 'GLN', 11.03), ('C', 'GLY', 'N', 'GLN', 11.13)], [('CA', 'GLY', 'CB', 'GLN', 11.11), ('CA', 'GLY', 'CG', 'GLN', 10.58), ('CA', 'GLY', 'CD', 'GLN', 9.24), ('CA', 'GLY', 'OE1', 'GLN', 8.21), ('CA', 'GLY', 'NE2', 'GLN', 9.42), ('CA', 'GLY', 'O', 'GLN', 13.78), ('CA', 'GLY', 'C', 'GLN', 13.18), ('CA', 'GLY', 'CA', 'GLN', 12.49), ('CA', 'GLY', 'N', 'GLN', 12.54)], [('N', 'GLY', 'CB', 'GLN', 11.8), ('N', 'GLY', 'CG', 'GLN', 11.29), ('N', 'GLY', 'CD', 'GLN', 9.87), ('N', 'GLY', 'OE1', 'GLN', 8.97), ('N', 'GLY', 'NE2', 'GLN', 9.82), ('N', 'GLY', 'O', 'GLN', 14.36), ('N', 'GLY', 'C', 'GLN', 13.87), ('N', 'GLY', 'CA', 'GLN', 13.25), ('N', 'GLY', 'N', 'GLN', 13.45)]]}
GLY_GLU = { 
	'distances':
		[[8.37, 7.08, 6.1, 6.24, 5.64, 10.42, 10.28, 9.02, 9.45], [7.54, 6.26, 5.55, 5.77, 5.33, 9.8, 9.62, 8.39, 8.9], [7.57, 6.16, 5.88, 6.48, 5.57, 10.26, 9.88, 8.58, 8.89], [8.79, 7.31, 6.93, 7.6, 6.33, 11.5, 11.07, 9.69, 9.82]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'GLU', 8.37), ('O', 'GLY', 'CG', 'GLU', 7.08), ('O', 'GLY', 'CD', 'GLU', 6.1), ('O', 'GLY', 'OE1', 'GLU', 6.24), ('O', 'GLY', 'OE2', 'GLU', 5.64), ('O', 'GLY', 'O', 'GLU', 10.42), ('O', 'GLY', 'C', 'GLU', 10.28), ('O', 'GLY', 'CA', 'GLU', 9.02), ('O', 'GLY', 'N', 'GLU', 9.45)], [('C', 'GLY', 'CB', 'GLU', 7.54), ('C', 'GLY', 'CG', 'GLU', 6.26), ('C', 'GLY', 'CD', 'GLU', 5.55), ('C', 'GLY', 'OE1', 'GLU', 5.77), ('C', 'GLY', 'OE2', 'GLU', 5.33), ('C', 'GLY', 'O', 'GLU', 9.8), ('C', 'GLY', 'C', 'GLU', 9.62), ('C', 'GLY', 'CA', 'GLU', 8.39), ('C', 'GLY', 'N', 'GLU', 8.9)], [('CA', 'GLY', 'CB', 'GLU', 7.57), ('CA', 'GLY', 'CG', 'GLU', 6.16), ('CA', 'GLY', 'CD', 'GLU', 5.88), ('CA', 'GLY', 'OE1', 'GLU', 6.48), ('CA', 'GLY', 'OE2', 'GLU', 5.57), ('CA', 'GLY', 'O', 'GLU', 10.26), ('CA', 'GLY', 'C', 'GLU', 9.88), ('CA', 'GLY', 'CA', 'GLU', 8.58), ('CA', 'GLY', 'N', 'GLU', 8.89)], [('N', 'GLY', 'CB', 'GLU', 8.79), ('N', 'GLY', 'CG', 'GLU', 7.31), ('N', 'GLY', 'CD', 'GLU', 6.93), ('N', 'GLY', 'OE1', 'GLU', 7.6), ('N', 'GLY', 'OE2', 'GLU', 6.33), ('N', 'GLY', 'O', 'GLU', 11.5), ('N', 'GLY', 'C', 'GLU', 11.07), ('N', 'GLY', 'CA', 'GLU', 9.69), ('N', 'GLY', 'N', 'GLU', 9.82)]]}
GLU_LEU = { 
	'distances':
		[[13.19, 13.1, 12.64, 14.54, 15.42, 14.22, 13.59, 12.57], [12.24, 12.0, 11.52, 13.38, 14.65, 13.45, 12.67, 11.65], [10.77, 10.61, 10.18, 12.03, 13.15, 11.95, 11.2, 10.2], [10.43, 10.44, 9.95, 11.92, 12.72, 11.55, 10.93, 10.04], [10.09, 9.83, 9.53, 11.19, 12.5, 11.29, 10.43, 9.36], [13.9, 14.21, 13.85, 15.73, 15.58, 14.44, 14.18, 13.24], [14.08, 14.29, 13.97, 15.78, 15.86, 14.68, 14.31, 13.27], [13.04, 13.12, 12.83, 14.58, 14.98, 13.77, 13.27, 12.19], [13.3, 13.33, 13.19, 14.73, 15.16, 13.93, 13.38, 12.18]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LEU', 13.19), ('CB', 'GLU', 'CG', 'LEU', 13.1), ('CB', 'GLU', 'CD1', 'LEU', 12.64), ('CB', 'GLU', 'CD2', 'LEU', 14.54), ('CB', 'GLU', 'O', 'LEU', 15.42), ('CB', 'GLU', 'C', 'LEU', 14.22), ('CB', 'GLU', 'CA', 'LEU', 13.59), ('CB', 'GLU', 'N', 'LEU', 12.57)], [('CG', 'GLU', 'CB', 'LEU', 12.24), ('CG', 'GLU', 'CG', 'LEU', 12.0), ('CG', 'GLU', 'CD1', 'LEU', 11.52), ('CG', 'GLU', 'CD2', 'LEU', 13.38), ('CG', 'GLU', 'O', 'LEU', 14.65), ('CG', 'GLU', 'C', 'LEU', 13.45), ('CG', 'GLU', 'CA', 'LEU', 12.67), ('CG', 'GLU', 'N', 'LEU', 11.65)], [('CD', 'GLU', 'CB', 'LEU', 10.77), ('CD', 'GLU', 'CG', 'LEU', 10.61), ('CD', 'GLU', 'CD1', 'LEU', 10.18), ('CD', 'GLU', 'CD2', 'LEU', 12.03), ('CD', 'GLU', 'O', 'LEU', 13.15), ('CD', 'GLU', 'C', 'LEU', 11.95), ('CD', 'GLU', 'CA', 'LEU', 11.2), ('CD', 'GLU', 'N', 'LEU', 10.2)], [('OE1', 'GLU', 'CB', 'LEU', 10.43), ('OE1', 'GLU', 'CG', 'LEU', 10.44), ('OE1', 'GLU', 'CD1', 'LEU', 9.95), ('OE1', 'GLU', 'CD2', 'LEU', 11.92), ('OE1', 'GLU', 'O', 'LEU', 12.72), ('OE1', 'GLU', 'C', 'LEU', 11.55), ('OE1', 'GLU', 'CA', 'LEU', 10.93), ('OE1', 'GLU', 'N', 'LEU', 10.04)], [('OE2', 'GLU', 'CB', 'LEU', 10.09), ('OE2', 'GLU', 'CG', 'LEU', 9.83), ('OE2', 'GLU', 'CD1', 'LEU', 9.53), ('OE2', 'GLU', 'CD2', 'LEU', 11.19), ('OE2', 'GLU', 'O', 'LEU', 12.5), ('OE2', 'GLU', 'C', 'LEU', 11.29), ('OE2', 'GLU', 'CA', 'LEU', 10.43), ('OE2', 'GLU', 'N', 'LEU', 9.36)], [('O', 'GLU', 'CB', 'LEU', 13.9), ('O', 'GLU', 'CG', 'LEU', 14.21), ('O', 'GLU', 'CD1', 'LEU', 13.85), ('O', 'GLU', 'CD2', 'LEU', 15.73), ('O', 'GLU', 'O', 'LEU', 15.58), ('O', 'GLU', 'C', 'LEU', 14.44), ('O', 'GLU', 'CA', 'LEU', 14.18), ('O', 'GLU', 'N', 'LEU', 13.24)], [('C', 'GLU', 'CB', 'LEU', 14.08), ('C', 'GLU', 'CG', 'LEU', 14.29), ('C', 'GLU', 'CD1', 'LEU', 13.97), ('C', 'GLU', 'CD2', 'LEU', 15.78), ('C', 'GLU', 'O', 'LEU', 15.86), ('C', 'GLU', 'C', 'LEU', 14.68), ('C', 'GLU', 'CA', 'LEU', 14.31), ('C', 'GLU', 'N', 'LEU', 13.27)], [('CA', 'GLU', 'CB', 'LEU', 13.04), ('CA', 'GLU', 'CG', 'LEU', 13.12), ('CA', 'GLU', 'CD1', 'LEU', 12.83), ('CA', 'GLU', 'CD2', 'LEU', 14.58), ('CA', 'GLU', 'O', 'LEU', 14.98), ('CA', 'GLU', 'C', 'LEU', 13.77), ('CA', 'GLU', 'CA', 'LEU', 13.27), ('CA', 'GLU', 'N', 'LEU', 12.19)], [('N', 'GLU', 'CB', 'LEU', 13.3), ('N', 'GLU', 'CG', 'LEU', 13.33), ('N', 'GLU', 'CD1', 'LEU', 13.19), ('N', 'GLU', 'CD2', 'LEU', 14.73), ('N', 'GLU', 'O', 'LEU', 15.16), ('N', 'GLU', 'C', 'LEU', 13.93), ('N', 'GLU', 'CA', 'LEU', 13.38), ('N', 'GLU', 'N', 'LEU', 12.18)]]}
GLN_LEU = { 
	'distances':
		[[8.22, 9.17, 8.77, 10.52, 9.31, 8.62, 8.91, 8.97], [8.17, 9.1, 8.87, 10.54, 9.28, 8.41, 8.64, 8.41], [7.27, 7.99, 7.74, 9.49, 8.89, 7.89, 7.8, 7.41], [7.88, 8.34, 7.91, 9.87, 9.86, 8.82, 8.51, 8.01], [6.05, 6.87, 6.85, 8.35, 7.67, 6.62, 6.49, 6.12], [9.31, 10.44, 10.08, 11.47, 9.57, 9.35, 10.02, 10.56], [9.7, 10.73, 10.25, 11.89, 10.3, 9.92, 10.46, 10.83], [9.48, 10.53, 10.16, 11.81, 10.15, 9.59, 10.09, 10.23], [10.67, 11.62, 11.16, 12.97, 11.5, 10.87, 11.29, 11.29]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'LEU', 8.22), ('CB', 'GLN', 'CG', 'LEU', 9.17), ('CB', 'GLN', 'CD1', 'LEU', 8.77), ('CB', 'GLN', 'CD2', 'LEU', 10.52), ('CB', 'GLN', 'O', 'LEU', 9.31), ('CB', 'GLN', 'C', 'LEU', 8.62), ('CB', 'GLN', 'CA', 'LEU', 8.91), ('CB', 'GLN', 'N', 'LEU', 8.97)], [('CG', 'GLN', 'CB', 'LEU', 8.17), ('CG', 'GLN', 'CG', 'LEU', 9.1), ('CG', 'GLN', 'CD1', 'LEU', 8.87), ('CG', 'GLN', 'CD2', 'LEU', 10.54), ('CG', 'GLN', 'O', 'LEU', 9.28), ('CG', 'GLN', 'C', 'LEU', 8.41), ('CG', 'GLN', 'CA', 'LEU', 8.64), ('CG', 'GLN', 'N', 'LEU', 8.41)], [('CD', 'GLN', 'CB', 'LEU', 7.27), ('CD', 'GLN', 'CG', 'LEU', 7.99), ('CD', 'GLN', 'CD1', 'LEU', 7.74), ('CD', 'GLN', 'CD2', 'LEU', 9.49), ('CD', 'GLN', 'O', 'LEU', 8.89), ('CD', 'GLN', 'C', 'LEU', 7.89), ('CD', 'GLN', 'CA', 'LEU', 7.8), ('CD', 'GLN', 'N', 'LEU', 7.41)], [('OE1', 'GLN', 'CB', 'LEU', 7.88), ('OE1', 'GLN', 'CG', 'LEU', 8.34), ('OE1', 'GLN', 'CD1', 'LEU', 7.91), ('OE1', 'GLN', 'CD2', 'LEU', 9.87), ('OE1', 'GLN', 'O', 'LEU', 9.86), ('OE1', 'GLN', 'C', 'LEU', 8.82), ('OE1', 'GLN', 'CA', 'LEU', 8.51), ('OE1', 'GLN', 'N', 'LEU', 8.01)], [('NE2', 'GLN', 'CB', 'LEU', 6.05), ('NE2', 'GLN', 'CG', 'LEU', 6.87), ('NE2', 'GLN', 'CD1', 'LEU', 6.85), ('NE2', 'GLN', 'CD2', 'LEU', 8.35), ('NE2', 'GLN', 'O', 'LEU', 7.67), ('NE2', 'GLN', 'C', 'LEU', 6.62), ('NE2', 'GLN', 'CA', 'LEU', 6.49), ('NE2', 'GLN', 'N', 'LEU', 6.12)], [('O', 'GLN', 'CB', 'LEU', 9.31), ('O', 'GLN', 'CG', 'LEU', 10.44), ('O', 'GLN', 'CD1', 'LEU', 10.08), ('O', 'GLN', 'CD2', 'LEU', 11.47), ('O', 'GLN', 'O', 'LEU', 9.57), ('O', 'GLN', 'C', 'LEU', 9.35), ('O', 'GLN', 'CA', 'LEU', 10.02), ('O', 'GLN', 'N', 'LEU', 10.56)], [('C', 'GLN', 'CB', 'LEU', 9.7), ('C', 'GLN', 'CG', 'LEU', 10.73), ('C', 'GLN', 'CD1', 'LEU', 10.25), ('C', 'GLN', 'CD2', 'LEU', 11.89), ('C', 'GLN', 'O', 'LEU', 10.3), ('C', 'GLN', 'C', 'LEU', 9.92), ('C', 'GLN', 'CA', 'LEU', 10.46), ('C', 'GLN', 'N', 'LEU', 10.83)], [('CA', 'GLN', 'CB', 'LEU', 9.48), ('CA', 'GLN', 'CG', 'LEU', 10.53), ('CA', 'GLN', 'CD1', 'LEU', 10.16), ('CA', 'GLN', 'CD2', 'LEU', 11.81), ('CA', 'GLN', 'O', 'LEU', 10.15), ('CA', 'GLN', 'C', 'LEU', 9.59), ('CA', 'GLN', 'CA', 'LEU', 10.09), ('CA', 'GLN', 'N', 'LEU', 10.23)], [('N', 'GLN', 'CB', 'LEU', 10.67), ('N', 'GLN', 'CG', 'LEU', 11.62), ('N', 'GLN', 'CD1', 'LEU', 11.16), ('N', 'GLN', 'CD2', 'LEU', 12.97), ('N', 'GLN', 'O', 'LEU', 11.5), ('N', 'GLN', 'C', 'LEU', 10.87), ('N', 'GLN', 'CA', 'LEU', 11.29), ('N', 'GLN', 'N', 'LEU', 11.29)]]}
GLY_LEU = { 
	'distances':
		[[8.34, 7.63, 6.76, 8.85, 11.4, 10.38, 9.26, 8.7], [9.5, 8.84, 7.95, 10.07, 12.51, 11.47, 10.4, 9.78], [10.62, 9.82, 9.01, 10.92, 13.65, 12.59, 11.43, 10.71], [10.33, 9.32, 8.59, 10.25, 13.39, 12.38, 11.09, 10.39]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'LEU', 8.34), ('O', 'GLY', 'CG', 'LEU', 7.63), ('O', 'GLY', 'CD1', 'LEU', 6.76), ('O', 'GLY', 'CD2', 'LEU', 8.85), ('O', 'GLY', 'O', 'LEU', 11.4), ('O', 'GLY', 'C', 'LEU', 10.38), ('O', 'GLY', 'CA', 'LEU', 9.26), ('O', 'GLY', 'N', 'LEU', 8.7)], [('C', 'GLY', 'CB', 'LEU', 9.5), ('C', 'GLY', 'CG', 'LEU', 8.84), ('C', 'GLY', 'CD1', 'LEU', 7.95), ('C', 'GLY', 'CD2', 'LEU', 10.07), ('C', 'GLY', 'O', 'LEU', 12.51), ('C', 'GLY', 'C', 'LEU', 11.47), ('C', 'GLY', 'CA', 'LEU', 10.4), ('C', 'GLY', 'N', 'LEU', 9.78)], [('CA', 'GLY', 'CB', 'LEU', 10.62), ('CA', 'GLY', 'CG', 'LEU', 9.82), ('CA', 'GLY', 'CD1', 'LEU', 9.01), ('CA', 'GLY', 'CD2', 'LEU', 10.92), ('CA', 'GLY', 'O', 'LEU', 13.65), ('CA', 'GLY', 'C', 'LEU', 12.59), ('CA', 'GLY', 'CA', 'LEU', 11.43), ('CA', 'GLY', 'N', 'LEU', 10.71)], [('N', 'GLY', 'CB', 'LEU', 10.33), ('N', 'GLY', 'CG', 'LEU', 9.32), ('N', 'GLY', 'CD1', 'LEU', 8.59), ('N', 'GLY', 'CD2', 'LEU', 10.25), ('N', 'GLY', 'O', 'LEU', 13.39), ('N', 'GLY', 'C', 'LEU', 12.38), ('N', 'GLY', 'CA', 'LEU', 11.09), ('N', 'GLY', 'N', 'LEU', 10.39)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLN, d, 'A_1bsj_3_5_1_88')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLY_GLN, d, 'A_1bsj_3_5_1_88')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_GLU, d, 'A_1bsj_3_5_1_88')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_LEU, d, 'A_1bsj_3_5_1_88')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLN_LEU, d, 'A_1bsj_3_5_1_88')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLY_LEU, d, 'A_1bsj_3_5_1_88')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLN' :  match1,
		'GLY_GLN' :  match2,
		'GLY_GLU' :  match3,
		'GLU_LEU' :  match4,
		'GLN_LEU' :  match5,
		'GLY_LEU' :  match6}