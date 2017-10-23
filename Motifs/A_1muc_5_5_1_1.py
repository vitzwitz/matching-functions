'''
FUNC:A_1muc_5_5_1_1
PDB:1muc
EC:5.5.1.1
RESI:lys,lys,glu
LOCI:a-167,169,327;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[7.88, 7.99, 6.76, 7.44, 6.81, 10.45, 10.28, 9.29, 9.37], [8.68, 8.48, 7.09, 7.4, 6.43, 11.32, 11.08, 10.16, 10.44], [8.09, 7.61, 6.13, 6.15, 5.02, 10.7, 10.4, 9.6, 10.11], [6.91, 6.38, 4.92, 5.06, 4.14, 9.6, 9.23, 8.41, 9.0], [8.99, 8.34, 6.84, 6.51, 5.17, 11.49, 11.2, 10.51, 11.13], [9.98, 10.18, 8.93, 9.48, 8.72, 12.04, 12.15, 11.35, 11.29], [10.02, 10.31, 9.12, 9.8, 9.09, 12.26, 12.29, 11.34, 11.19], [8.94, 9.25, 8.13, 8.92, 8.33, 11.41, 11.31, 10.24, 10.1], [9.79, 10.02, 8.89, 9.61, 8.91, 12.46, 12.23, 11.06, 10.95], [12.84, 11.43, 11.57, 12.53, 12.96, 15.28, 14.55, 13.05, 12.61], [12.97, 11.54, 11.63, 12.42, 12.81, 15.53, 14.73, 13.23, 12.97], [11.75, 10.34, 10.49, 11.19, 11.66, 14.35, 13.49, 12.01, 11.87], [10.88, 9.52, 9.83, 10.63, 11.26, 13.36, 12.49, 11.02, 10.81], [11.82, 10.42, 10.45, 10.97, 11.35, 14.52, 13.63, 12.18, 12.21], [14.1, 12.61, 12.38, 13.27, 13.35, 16.72, 16.11, 14.59, 14.21], [14.75, 13.29, 13.19, 14.13, 14.31, 17.28, 16.64, 15.12, 14.66], [14.22, 12.81, 12.91, 13.91, 14.27, 16.62, 15.93, 14.43, 13.91], [15.25, 13.86, 14.03, 14.97, 15.38, 17.61, 16.87, 15.37, 14.89]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 7.88), ('CB', 'GLU', 'CG', 'LYS', 7.99), ('CB', 'GLU', 'CD', 'LYS', 6.76), ('CB', 'GLU', 'CE', 'LYS', 7.44), ('CB', 'GLU', 'NZ', 'LYS', 6.81), ('CB', 'GLU', 'O', 'LYS', 10.45), ('CB', 'GLU', 'C', 'LYS', 10.28), ('CB', 'GLU', 'CA', 'LYS', 9.29), ('CB', 'GLU', 'N', 'LYS', 9.37)], [('CG', 'GLU', 'CB', 'LYS', 8.68), ('CG', 'GLU', 'CG', 'LYS', 8.48), ('CG', 'GLU', 'CD', 'LYS', 7.09), ('CG', 'GLU', 'CE', 'LYS', 7.4), ('CG', 'GLU', 'NZ', 'LYS', 6.43), ('CG', 'GLU', 'O', 'LYS', 11.32), ('CG', 'GLU', 'C', 'LYS', 11.08), ('CG', 'GLU', 'CA', 'LYS', 10.16), ('CG', 'GLU', 'N', 'LYS', 10.44)], [('CD', 'GLU', 'CB', 'LYS', 8.09), ('CD', 'GLU', 'CG', 'LYS', 7.61), ('CD', 'GLU', 'CD', 'LYS', 6.13), ('CD', 'GLU', 'CE', 'LYS', 6.15), ('CD', 'GLU', 'NZ', 'LYS', 5.02), ('CD', 'GLU', 'O', 'LYS', 10.7), ('CD', 'GLU', 'C', 'LYS', 10.4), ('CD', 'GLU', 'CA', 'LYS', 9.6), ('CD', 'GLU', 'N', 'LYS', 10.11)], [('OE1', 'GLU', 'CB', 'LYS', 6.91), ('OE1', 'GLU', 'CG', 'LYS', 6.38), ('OE1', 'GLU', 'CD', 'LYS', 4.92), ('OE1', 'GLU', 'CE', 'LYS', 5.06), ('OE1', 'GLU', 'NZ', 'LYS', 4.14), ('OE1', 'GLU', 'O', 'LYS', 9.6), ('OE1', 'GLU', 'C', 'LYS', 9.23), ('OE1', 'GLU', 'CA', 'LYS', 8.41), ('OE1', 'GLU', 'N', 'LYS', 9.0)], [('OE2', 'GLU', 'CB', 'LYS', 8.99), ('OE2', 'GLU', 'CG', 'LYS', 8.34), ('OE2', 'GLU', 'CD', 'LYS', 6.84), ('OE2', 'GLU', 'CE', 'LYS', 6.51), ('OE2', 'GLU', 'NZ', 'LYS', 5.17), ('OE2', 'GLU', 'O', 'LYS', 11.49), ('OE2', 'GLU', 'C', 'LYS', 11.2), ('OE2', 'GLU', 'CA', 'LYS', 10.51), ('OE2', 'GLU', 'N', 'LYS', 11.13)], [('O', 'GLU', 'CB', 'LYS', 9.98), ('O', 'GLU', 'CG', 'LYS', 10.18), ('O', 'GLU', 'CD', 'LYS', 8.93), ('O', 'GLU', 'CE', 'LYS', 9.48), ('O', 'GLU', 'NZ', 'LYS', 8.72), ('O', 'GLU', 'O', 'LYS', 12.04), ('O', 'GLU', 'C', 'LYS', 12.15), ('O', 'GLU', 'CA', 'LYS', 11.35), ('O', 'GLU', 'N', 'LYS', 11.29)], [('C', 'GLU', 'CB', 'LYS', 10.02), ('C', 'GLU', 'CG', 'LYS', 10.31), ('C', 'GLU', 'CD', 'LYS', 9.12), ('C', 'GLU', 'CE', 'LYS', 9.8), ('C', 'GLU', 'NZ', 'LYS', 9.09), ('C', 'GLU', 'O', 'LYS', 12.26), ('C', 'GLU', 'C', 'LYS', 12.29), ('C', 'GLU', 'CA', 'LYS', 11.34), ('C', 'GLU', 'N', 'LYS', 11.19)], [('CA', 'GLU', 'CB', 'LYS', 8.94), ('CA', 'GLU', 'CG', 'LYS', 9.25), ('CA', 'GLU', 'CD', 'LYS', 8.13), ('CA', 'GLU', 'CE', 'LYS', 8.92), ('CA', 'GLU', 'NZ', 'LYS', 8.33), ('CA', 'GLU', 'O', 'LYS', 11.41), ('CA', 'GLU', 'C', 'LYS', 11.31), ('CA', 'GLU', 'CA', 'LYS', 10.24), ('CA', 'GLU', 'N', 'LYS', 10.1)], [('N', 'GLU', 'CB', 'LYS', 9.79), ('N', 'GLU', 'CG', 'LYS', 10.02), ('N', 'GLU', 'CD', 'LYS', 8.89), ('N', 'GLU', 'CE', 'LYS', 9.61), ('N', 'GLU', 'NZ', 'LYS', 8.91), ('N', 'GLU', 'O', 'LYS', 12.46), ('N', 'GLU', 'C', 'LYS', 12.23), ('N', 'GLU', 'CA', 'LYS', 11.06), ('N', 'GLU', 'N', 'LYS', 10.95)], [('CB', 'GLU', 'CB', 'LYS', 12.84), ('CB', 'GLU', 'CG', 'LYS', 11.43), ('CB', 'GLU', 'CD', 'LYS', 11.57), ('CB', 'GLU', 'CE', 'LYS', 12.53), ('CB', 'GLU', 'NZ', 'LYS', 12.96), ('CB', 'GLU', 'O', 'LYS', 15.28), ('CB', 'GLU', 'C', 'LYS', 14.55), ('CB', 'GLU', 'CA', 'LYS', 13.05), ('CB', 'GLU', 'N', 'LYS', 12.61)], [('CG', 'GLU', 'CB', 'LYS', 12.97), ('CG', 'GLU', 'CG', 'LYS', 11.54), ('CG', 'GLU', 'CD', 'LYS', 11.63), ('CG', 'GLU', 'CE', 'LYS', 12.42), ('CG', 'GLU', 'NZ', 'LYS', 12.81), ('CG', 'GLU', 'O', 'LYS', 15.53), ('CG', 'GLU', 'C', 'LYS', 14.73), ('CG', 'GLU', 'CA', 'LYS', 13.23), ('CG', 'GLU', 'N', 'LYS', 12.97)], [('CD', 'GLU', 'CB', 'LYS', 11.75), ('CD', 'GLU', 'CG', 'LYS', 10.34), ('CD', 'GLU', 'CD', 'LYS', 10.49), ('CD', 'GLU', 'CE', 'LYS', 11.19), ('CD', 'GLU', 'NZ', 'LYS', 11.66), ('CD', 'GLU', 'O', 'LYS', 14.35), ('CD', 'GLU', 'C', 'LYS', 13.49), ('CD', 'GLU', 'CA', 'LYS', 12.01), ('CD', 'GLU', 'N', 'LYS', 11.87)], [('OE1', 'GLU', 'CB', 'LYS', 10.88), ('OE1', 'GLU', 'CG', 'LYS', 9.52), ('OE1', 'GLU', 'CD', 'LYS', 9.83), ('OE1', 'GLU', 'CE', 'LYS', 10.63), ('OE1', 'GLU', 'NZ', 'LYS', 11.26), ('OE1', 'GLU', 'O', 'LYS', 13.36), ('OE1', 'GLU', 'C', 'LYS', 12.49), ('OE1', 'GLU', 'CA', 'LYS', 11.02), ('OE1', 'GLU', 'N', 'LYS', 10.81)], [('OE2', 'GLU', 'CB', 'LYS', 11.82), ('OE2', 'GLU', 'CG', 'LYS', 10.42), ('OE2', 'GLU', 'CD', 'LYS', 10.45), ('OE2', 'GLU', 'CE', 'LYS', 10.97), ('OE2', 'GLU', 'NZ', 'LYS', 11.35), ('OE2', 'GLU', 'O', 'LYS', 14.52), ('OE2', 'GLU', 'C', 'LYS', 13.63), ('OE2', 'GLU', 'CA', 'LYS', 12.18), ('OE2', 'GLU', 'N', 'LYS', 12.21)], [('O', 'GLU', 'CB', 'LYS', 14.1), ('O', 'GLU', 'CG', 'LYS', 12.61), ('O', 'GLU', 'CD', 'LYS', 12.38), ('O', 'GLU', 'CE', 'LYS', 13.27), ('O', 'GLU', 'NZ', 'LYS', 13.35), ('O', 'GLU', 'O', 'LYS', 16.72), ('O', 'GLU', 'C', 'LYS', 16.11), ('O', 'GLU', 'CA', 'LYS', 14.59), ('O', 'GLU', 'N', 'LYS', 14.21)], [('C', 'GLU', 'CB', 'LYS', 14.75), ('C', 'GLU', 'CG', 'LYS', 13.29), ('C', 'GLU', 'CD', 'LYS', 13.19), ('C', 'GLU', 'CE', 'LYS', 14.13), ('C', 'GLU', 'NZ', 'LYS', 14.31), ('C', 'GLU', 'O', 'LYS', 17.28), ('C', 'GLU', 'C', 'LYS', 16.64), ('C', 'GLU', 'CA', 'LYS', 15.12), ('C', 'GLU', 'N', 'LYS', 14.66)], [('CA', 'GLU', 'CB', 'LYS', 14.22), ('CA', 'GLU', 'CG', 'LYS', 12.81), ('CA', 'GLU', 'CD', 'LYS', 12.91), ('CA', 'GLU', 'CE', 'LYS', 13.91), ('CA', 'GLU', 'NZ', 'LYS', 14.27), ('CA', 'GLU', 'O', 'LYS', 16.62), ('CA', 'GLU', 'C', 'LYS', 15.93), ('CA', 'GLU', 'CA', 'LYS', 14.43), ('CA', 'GLU', 'N', 'LYS', 13.91)], [('N', 'GLU', 'CB', 'LYS', 15.25), ('N', 'GLU', 'CG', 'LYS', 13.86), ('N', 'GLU', 'CD', 'LYS', 14.03), ('N', 'GLU', 'CE', 'LYS', 14.97), ('N', 'GLU', 'NZ', 'LYS', 15.38), ('N', 'GLU', 'O', 'LYS', 17.61), ('N', 'GLU', 'C', 'LYS', 16.87), ('N', 'GLU', 'CA', 'LYS', 15.37), ('N', 'GLU', 'N', 'LYS', 14.89)]]}
LYS_LYS = { 
	'distances':
		[[8.71, 7.84, 8.76, 10.07, 11.11, 10.21, 9.6, 8.29, 7.35], [7.93, 7.04, 8.07, 9.23, 10.35, 9.62, 8.84, 7.49, 6.81], [8.38, 7.24, 8.02, 9.08, 10.07, 10.47, 9.65, 8.21, 7.76], [7.8, 6.66, 7.44, 8.26, 9.29, 10.07, 9.13, 7.7, 7.59], [8.77, 7.52, 8.03, 8.67, 9.52, 11.24, 10.28, 8.85, 8.89], [7.65, 7.2, 8.11, 9.54, 10.55, 8.46, 8.26, 7.22, 5.88], [7.75, 7.34, 8.44, 9.79, 10.92, 8.51, 8.14, 7.09, 5.8], [8.88, 8.28, 9.34, 10.68, 11.78, 9.86, 9.37, 8.23, 7.08], [9.99, 9.36, 10.29, 11.7, 12.71, 10.9, 10.53, 9.43, 8.18], [8.71, 7.93, 8.38, 7.8, 8.77, 7.65, 7.75, 8.88, 9.99], [7.84, 7.04, 7.24, 6.66, 7.52, 7.2, 7.34, 8.28, 9.36], [8.76, 8.07, 8.02, 7.44, 8.03, 8.11, 8.44, 9.34, 10.29], [10.07, 9.23, 9.08, 8.26, 8.67, 9.54, 9.79, 10.68, 11.7], [11.11, 10.35, 10.07, 9.29, 9.52, 10.55, 10.92, 11.78, 12.71], [10.21, 9.62, 10.47, 10.07, 11.24, 8.46, 8.51, 9.86, 10.9], [9.6, 8.84, 9.65, 9.13, 10.28, 8.26, 8.14, 9.37, 10.53], [8.29, 7.49, 8.21, 7.7, 8.85, 7.22, 7.09, 8.23, 9.43], [7.35, 6.81, 7.76, 7.59, 8.89, 5.88, 5.8, 7.08, 8.18]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 8.71), ('CB', 'LYS', 'CG', 'LYS', 7.84), ('CB', 'LYS', 'CD', 'LYS', 8.76), ('CB', 'LYS', 'CE', 'LYS', 10.07), ('CB', 'LYS', 'NZ', 'LYS', 11.11), ('CB', 'LYS', 'O', 'LYS', 10.21), ('CB', 'LYS', 'C', 'LYS', 9.6), ('CB', 'LYS', 'CA', 'LYS', 8.29), ('CB', 'LYS', 'N', 'LYS', 7.35)], [('CG', 'LYS', 'CB', 'LYS', 7.93), ('CG', 'LYS', 'CG', 'LYS', 7.04), ('CG', 'LYS', 'CD', 'LYS', 8.07), ('CG', 'LYS', 'CE', 'LYS', 9.23), ('CG', 'LYS', 'NZ', 'LYS', 10.35), ('CG', 'LYS', 'O', 'LYS', 9.62), ('CG', 'LYS', 'C', 'LYS', 8.84), ('CG', 'LYS', 'CA', 'LYS', 7.49), ('CG', 'LYS', 'N', 'LYS', 6.81)], [('CD', 'LYS', 'CB', 'LYS', 8.38), ('CD', 'LYS', 'CG', 'LYS', 7.24), ('CD', 'LYS', 'CD', 'LYS', 8.02), ('CD', 'LYS', 'CE', 'LYS', 9.08), ('CD', 'LYS', 'NZ', 'LYS', 10.07), ('CD', 'LYS', 'O', 'LYS', 10.47), ('CD', 'LYS', 'C', 'LYS', 9.65), ('CD', 'LYS', 'CA', 'LYS', 8.21), ('CD', 'LYS', 'N', 'LYS', 7.76)], [('CE', 'LYS', 'CB', 'LYS', 7.8), ('CE', 'LYS', 'CG', 'LYS', 6.66), ('CE', 'LYS', 'CD', 'LYS', 7.44), ('CE', 'LYS', 'CE', 'LYS', 8.26), ('CE', 'LYS', 'NZ', 'LYS', 9.29), ('CE', 'LYS', 'O', 'LYS', 10.07), ('CE', 'LYS', 'C', 'LYS', 9.13), ('CE', 'LYS', 'CA', 'LYS', 7.7), ('CE', 'LYS', 'N', 'LYS', 7.59)], [('NZ', 'LYS', 'CB', 'LYS', 8.77), ('NZ', 'LYS', 'CG', 'LYS', 7.52), ('NZ', 'LYS', 'CD', 'LYS', 8.03), ('NZ', 'LYS', 'CE', 'LYS', 8.67), ('NZ', 'LYS', 'NZ', 'LYS', 9.52), ('NZ', 'LYS', 'O', 'LYS', 11.24), ('NZ', 'LYS', 'C', 'LYS', 10.28), ('NZ', 'LYS', 'CA', 'LYS', 8.85), ('NZ', 'LYS', 'N', 'LYS', 8.89)], [('O', 'LYS', 'CB', 'LYS', 7.65), ('O', 'LYS', 'CG', 'LYS', 7.2), ('O', 'LYS', 'CD', 'LYS', 8.11), ('O', 'LYS', 'CE', 'LYS', 9.54), ('O', 'LYS', 'NZ', 'LYS', 10.55), ('O', 'LYS', 'O', 'LYS', 8.46), ('O', 'LYS', 'C', 'LYS', 8.26), ('O', 'LYS', 'CA', 'LYS', 7.22), ('O', 'LYS', 'N', 'LYS', 5.88)], [('C', 'LYS', 'CB', 'LYS', 7.75), ('C', 'LYS', 'CG', 'LYS', 7.34), ('C', 'LYS', 'CD', 'LYS', 8.44), ('C', 'LYS', 'CE', 'LYS', 9.79), ('C', 'LYS', 'NZ', 'LYS', 10.92), ('C', 'LYS', 'O', 'LYS', 8.51), ('C', 'LYS', 'C', 'LYS', 8.14), ('C', 'LYS', 'CA', 'LYS', 7.09), ('C', 'LYS', 'N', 'LYS', 5.8)], [('CA', 'LYS', 'CB', 'LYS', 8.88), ('CA', 'LYS', 'CG', 'LYS', 8.28), ('CA', 'LYS', 'CD', 'LYS', 9.34), ('CA', 'LYS', 'CE', 'LYS', 10.68), ('CA', 'LYS', 'NZ', 'LYS', 11.78), ('CA', 'LYS', 'O', 'LYS', 9.86), ('CA', 'LYS', 'C', 'LYS', 9.37), ('CA', 'LYS', 'CA', 'LYS', 8.23), ('CA', 'LYS', 'N', 'LYS', 7.08)], [('N', 'LYS', 'CB', 'LYS', 9.99), ('N', 'LYS', 'CG', 'LYS', 9.36), ('N', 'LYS', 'CD', 'LYS', 10.29), ('N', 'LYS', 'CE', 'LYS', 11.7), ('N', 'LYS', 'NZ', 'LYS', 12.71), ('N', 'LYS', 'O', 'LYS', 10.9), ('N', 'LYS', 'C', 'LYS', 10.53), ('N', 'LYS', 'CA', 'LYS', 9.43), ('N', 'LYS', 'N', 'LYS', 8.18)], [('CB', 'LYS', 'CB', 'LYS', 8.71), ('CB', 'LYS', 'CG', 'LYS', 7.93), ('CB', 'LYS', 'CD', 'LYS', 8.38), ('CB', 'LYS', 'CE', 'LYS', 7.8), ('CB', 'LYS', 'NZ', 'LYS', 8.77), ('CB', 'LYS', 'O', 'LYS', 7.65), ('CB', 'LYS', 'C', 'LYS', 7.75), ('CB', 'LYS', 'CA', 'LYS', 8.88), ('CB', 'LYS', 'N', 'LYS', 9.99)], [('CG', 'LYS', 'CB', 'LYS', 7.84), ('CG', 'LYS', 'CG', 'LYS', 7.04), ('CG', 'LYS', 'CD', 'LYS', 7.24), ('CG', 'LYS', 'CE', 'LYS', 6.66), ('CG', 'LYS', 'NZ', 'LYS', 7.52), ('CG', 'LYS', 'O', 'LYS', 7.2), ('CG', 'LYS', 'C', 'LYS', 7.34), ('CG', 'LYS', 'CA', 'LYS', 8.28), ('CG', 'LYS', 'N', 'LYS', 9.36)], [('CD', 'LYS', 'CB', 'LYS', 8.76), ('CD', 'LYS', 'CG', 'LYS', 8.07), ('CD', 'LYS', 'CD', 'LYS', 8.02), ('CD', 'LYS', 'CE', 'LYS', 7.44), ('CD', 'LYS', 'NZ', 'LYS', 8.03), ('CD', 'LYS', 'O', 'LYS', 8.11), ('CD', 'LYS', 'C', 'LYS', 8.44), ('CD', 'LYS', 'CA', 'LYS', 9.34), ('CD', 'LYS', 'N', 'LYS', 10.29)], [('CE', 'LYS', 'CB', 'LYS', 10.07), ('CE', 'LYS', 'CG', 'LYS', 9.23), ('CE', 'LYS', 'CD', 'LYS', 9.08), ('CE', 'LYS', 'CE', 'LYS', 8.26), ('CE', 'LYS', 'NZ', 'LYS', 8.67), ('CE', 'LYS', 'O', 'LYS', 9.54), ('CE', 'LYS', 'C', 'LYS', 9.79), ('CE', 'LYS', 'CA', 'LYS', 10.68), ('CE', 'LYS', 'N', 'LYS', 11.7)], [('NZ', 'LYS', 'CB', 'LYS', 11.11), ('NZ', 'LYS', 'CG', 'LYS', 10.35), ('NZ', 'LYS', 'CD', 'LYS', 10.07), ('NZ', 'LYS', 'CE', 'LYS', 9.29), ('NZ', 'LYS', 'NZ', 'LYS', 9.52), ('NZ', 'LYS', 'O', 'LYS', 10.55), ('NZ', 'LYS', 'C', 'LYS', 10.92), ('NZ', 'LYS', 'CA', 'LYS', 11.78), ('NZ', 'LYS', 'N', 'LYS', 12.71)], [('O', 'LYS', 'CB', 'LYS', 10.21), ('O', 'LYS', 'CG', 'LYS', 9.62), ('O', 'LYS', 'CD', 'LYS', 10.47), ('O', 'LYS', 'CE', 'LYS', 10.07), ('O', 'LYS', 'NZ', 'LYS', 11.24), ('O', 'LYS', 'O', 'LYS', 8.46), ('O', 'LYS', 'C', 'LYS', 8.51), ('O', 'LYS', 'CA', 'LYS', 9.86), ('O', 'LYS', 'N', 'LYS', 10.9)], [('C', 'LYS', 'CB', 'LYS', 9.6), ('C', 'LYS', 'CG', 'LYS', 8.84), ('C', 'LYS', 'CD', 'LYS', 9.65), ('C', 'LYS', 'CE', 'LYS', 9.13), ('C', 'LYS', 'NZ', 'LYS', 10.28), ('C', 'LYS', 'O', 'LYS', 8.26), ('C', 'LYS', 'C', 'LYS', 8.14), ('C', 'LYS', 'CA', 'LYS', 9.37), ('C', 'LYS', 'N', 'LYS', 10.53)], [('CA', 'LYS', 'CB', 'LYS', 8.29), ('CA', 'LYS', 'CG', 'LYS', 7.49), ('CA', 'LYS', 'CD', 'LYS', 8.21), ('CA', 'LYS', 'CE', 'LYS', 7.7), ('CA', 'LYS', 'NZ', 'LYS', 8.85), ('CA', 'LYS', 'O', 'LYS', 7.22), ('CA', 'LYS', 'C', 'LYS', 7.09), ('CA', 'LYS', 'CA', 'LYS', 8.23), ('CA', 'LYS', 'N', 'LYS', 9.43)], [('N', 'LYS', 'CB', 'LYS', 7.35), ('N', 'LYS', 'CG', 'LYS', 6.81), ('N', 'LYS', 'CD', 'LYS', 7.76), ('N', 'LYS', 'CE', 'LYS', 7.59), ('N', 'LYS', 'NZ', 'LYS', 8.89), ('N', 'LYS', 'O', 'LYS', 5.88), ('N', 'LYS', 'C', 'LYS', 5.8), ('N', 'LYS', 'CA', 'LYS', 7.08), ('N', 'LYS', 'N', 'LYS', 8.18)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_1muc_5_5_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_LYS, d, 'A_1muc_5_5_1_1')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'LYS_LYS' :  match2}