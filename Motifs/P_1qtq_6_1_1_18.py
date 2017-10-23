'''
FUNC:P_1qtq_6_1_1_18
PDB:1qtq
EC:6.1.1.18
RESI:glu,arg,lys
LOCI:a-34,260,270;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[9.34, 8.74, 7.69, 6.79, 5.87, 12.13, 11.55, 10.84, 11.24], [9.85, 9.46, 8.36, 7.7, 6.87, 12.36, 11.87, 11.36, 11.87], [9.34, 9.2, 8.25, 7.84, 6.92, 11.67, 11.15, 10.8, 11.29], [8.67, 8.56, 7.8, 7.41, 6.31, 11.09, 10.46, 10.09, 10.44], [9.86, 9.87, 8.91, 8.68, 7.87, 11.88, 11.46, 11.28, 11.86], [8.17, 7.3, 5.94, 4.96, 4.87, 10.88, 10.51, 9.66, 10.31], [9.25, 8.44, 7.1, 6.14, 5.86, 11.92, 11.54, 10.75, 11.38], [9.84, 9.04, 7.87, 6.78, 6.13, 12.69, 12.17, 11.35, 11.8], [9.77, 8.77, 7.73, 6.43, 5.75, 12.79, 12.19, 11.21, 11.53]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 9.34), ('CB', 'GLU', 'CG', 'LYS', 8.74), ('CB', 'GLU', 'CD', 'LYS', 7.69), ('CB', 'GLU', 'CE', 'LYS', 6.79), ('CB', 'GLU', 'NZ', 'LYS', 5.87), ('CB', 'GLU', 'O', 'LYS', 12.13), ('CB', 'GLU', 'C', 'LYS', 11.55), ('CB', 'GLU', 'CA', 'LYS', 10.84), ('CB', 'GLU', 'N', 'LYS', 11.24)], [('CG', 'GLU', 'CB', 'LYS', 9.85), ('CG', 'GLU', 'CG', 'LYS', 9.46), ('CG', 'GLU', 'CD', 'LYS', 8.36), ('CG', 'GLU', 'CE', 'LYS', 7.7), ('CG', 'GLU', 'NZ', 'LYS', 6.87), ('CG', 'GLU', 'O', 'LYS', 12.36), ('CG', 'GLU', 'C', 'LYS', 11.87), ('CG', 'GLU', 'CA', 'LYS', 11.36), ('CG', 'GLU', 'N', 'LYS', 11.87)], [('CD', 'GLU', 'CB', 'LYS', 9.34), ('CD', 'GLU', 'CG', 'LYS', 9.2), ('CD', 'GLU', 'CD', 'LYS', 8.25), ('CD', 'GLU', 'CE', 'LYS', 7.84), ('CD', 'GLU', 'NZ', 'LYS', 6.92), ('CD', 'GLU', 'O', 'LYS', 11.67), ('CD', 'GLU', 'C', 'LYS', 11.15), ('CD', 'GLU', 'CA', 'LYS', 10.8), ('CD', 'GLU', 'N', 'LYS', 11.29)], [('OE1', 'GLU', 'CB', 'LYS', 8.67), ('OE1', 'GLU', 'CG', 'LYS', 8.56), ('OE1', 'GLU', 'CD', 'LYS', 7.8), ('OE1', 'GLU', 'CE', 'LYS', 7.41), ('OE1', 'GLU', 'NZ', 'LYS', 6.31), ('OE1', 'GLU', 'O', 'LYS', 11.09), ('OE1', 'GLU', 'C', 'LYS', 10.46), ('OE1', 'GLU', 'CA', 'LYS', 10.09), ('OE1', 'GLU', 'N', 'LYS', 10.44)], [('OE2', 'GLU', 'CB', 'LYS', 9.86), ('OE2', 'GLU', 'CG', 'LYS', 9.87), ('OE2', 'GLU', 'CD', 'LYS', 8.91), ('OE2', 'GLU', 'CE', 'LYS', 8.68), ('OE2', 'GLU', 'NZ', 'LYS', 7.87), ('OE2', 'GLU', 'O', 'LYS', 11.88), ('OE2', 'GLU', 'C', 'LYS', 11.46), ('OE2', 'GLU', 'CA', 'LYS', 11.28), ('OE2', 'GLU', 'N', 'LYS', 11.86)], [('O', 'GLU', 'CB', 'LYS', 8.17), ('O', 'GLU', 'CG', 'LYS', 7.3), ('O', 'GLU', 'CD', 'LYS', 5.94), ('O', 'GLU', 'CE', 'LYS', 4.96), ('O', 'GLU', 'NZ', 'LYS', 4.87), ('O', 'GLU', 'O', 'LYS', 10.88), ('O', 'GLU', 'C', 'LYS', 10.51), ('O', 'GLU', 'CA', 'LYS', 9.66), ('O', 'GLU', 'N', 'LYS', 10.31)], [('C', 'GLU', 'CB', 'LYS', 9.25), ('C', 'GLU', 'CG', 'LYS', 8.44), ('C', 'GLU', 'CD', 'LYS', 7.1), ('C', 'GLU', 'CE', 'LYS', 6.14), ('C', 'GLU', 'NZ', 'LYS', 5.86), ('C', 'GLU', 'O', 'LYS', 11.92), ('C', 'GLU', 'C', 'LYS', 11.54), ('C', 'GLU', 'CA', 'LYS', 10.75), ('C', 'GLU', 'N', 'LYS', 11.38)], [('CA', 'GLU', 'CB', 'LYS', 9.84), ('CA', 'GLU', 'CG', 'LYS', 9.04), ('CA', 'GLU', 'CD', 'LYS', 7.87), ('CA', 'GLU', 'CE', 'LYS', 6.78), ('CA', 'GLU', 'NZ', 'LYS', 6.13), ('CA', 'GLU', 'O', 'LYS', 12.69), ('CA', 'GLU', 'C', 'LYS', 12.17), ('CA', 'GLU', 'CA', 'LYS', 11.35), ('CA', 'GLU', 'N', 'LYS', 11.8)], [('N', 'GLU', 'CB', 'LYS', 9.77), ('N', 'GLU', 'CG', 'LYS', 8.77), ('N', 'GLU', 'CD', 'LYS', 7.73), ('N', 'GLU', 'CE', 'LYS', 6.43), ('N', 'GLU', 'NZ', 'LYS', 5.75), ('N', 'GLU', 'O', 'LYS', 12.79), ('N', 'GLU', 'C', 'LYS', 12.19), ('N', 'GLU', 'CA', 'LYS', 11.21), ('N', 'GLU', 'N', 'LYS', 11.53)]]}
GLU_ARG = { 
	'distances':
		[[15.83, 16.39, 15.35, 14.71, 13.41, 12.58, 13.06, 19.04, 17.9, 16.94, 17.71], [17.12, 17.59, 16.49, 15.84, 14.54, 13.7, 14.17, 20.36, 19.24, 18.28, 19.03], [16.99, 17.33, 16.14, 15.48, 14.18, 13.35, 13.81, 20.26, 19.18, 18.23, 18.97], [15.9, 16.19, 14.96, 14.33, 13.03, 12.19, 12.7, 19.18, 18.13, 17.17, 17.89], [18.08, 18.36, 17.12, 16.46, 15.16, 14.35, 14.76, 21.34, 20.28, 19.35, 20.08], [16.0, 16.68, 15.77, 14.89, 13.59, 13.03, 12.97, 18.95, 17.77, 17.02, 18.0], [16.7, 17.39, 16.46, 15.66, 14.36, 13.71, 13.82, 19.72, 18.53, 17.71, 18.63], [16.17, 16.85, 15.92, 15.24, 13.96, 13.18, 13.57, 19.28, 18.1, 17.17, 17.99], [15.05, 15.82, 14.98, 14.33, 13.08, 12.31, 12.72, 18.11, 16.92, 15.99, 16.81]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 15.83), ('CB', 'GLU', 'CG', 'ARG', 16.39), ('CB', 'GLU', 'CD', 'ARG', 15.35), ('CB', 'GLU', 'NE', 'ARG', 14.71), ('CB', 'GLU', 'CZ', 'ARG', 13.41), ('CB', 'GLU', 'NH1', 'ARG', 12.58), ('CB', 'GLU', 'NH2', 'ARG', 13.06), ('CB', 'GLU', 'O', 'ARG', 19.04), ('CB', 'GLU', 'C', 'ARG', 17.9), ('CB', 'GLU', 'CA', 'ARG', 16.94), ('CB', 'GLU', 'N', 'ARG', 17.71)], [('CG', 'GLU', 'CB', 'ARG', 17.12), ('CG', 'GLU', 'CG', 'ARG', 17.59), ('CG', 'GLU', 'CD', 'ARG', 16.49), ('CG', 'GLU', 'NE', 'ARG', 15.84), ('CG', 'GLU', 'CZ', 'ARG', 14.54), ('CG', 'GLU', 'NH1', 'ARG', 13.7), ('CG', 'GLU', 'NH2', 'ARG', 14.17), ('CG', 'GLU', 'O', 'ARG', 20.36), ('CG', 'GLU', 'C', 'ARG', 19.24), ('CG', 'GLU', 'CA', 'ARG', 18.28), ('CG', 'GLU', 'N', 'ARG', 19.03)], [('CD', 'GLU', 'CB', 'ARG', 16.99), ('CD', 'GLU', 'CG', 'ARG', 17.33), ('CD', 'GLU', 'CD', 'ARG', 16.14), ('CD', 'GLU', 'NE', 'ARG', 15.48), ('CD', 'GLU', 'CZ', 'ARG', 14.18), ('CD', 'GLU', 'NH1', 'ARG', 13.35), ('CD', 'GLU', 'NH2', 'ARG', 13.81), ('CD', 'GLU', 'O', 'ARG', 20.26), ('CD', 'GLU', 'C', 'ARG', 19.18), ('CD', 'GLU', 'CA', 'ARG', 18.23), ('CD', 'GLU', 'N', 'ARG', 18.97)], [('OE1', 'GLU', 'CB', 'ARG', 15.9), ('OE1', 'GLU', 'CG', 'ARG', 16.19), ('OE1', 'GLU', 'CD', 'ARG', 14.96), ('OE1', 'GLU', 'NE', 'ARG', 14.33), ('OE1', 'GLU', 'CZ', 'ARG', 13.03), ('OE1', 'GLU', 'NH1', 'ARG', 12.19), ('OE1', 'GLU', 'NH2', 'ARG', 12.7), ('OE1', 'GLU', 'O', 'ARG', 19.18), ('OE1', 'GLU', 'C', 'ARG', 18.13), ('OE1', 'GLU', 'CA', 'ARG', 17.17), ('OE1', 'GLU', 'N', 'ARG', 17.89)], [('OE2', 'GLU', 'CB', 'ARG', 18.08), ('OE2', 'GLU', 'CG', 'ARG', 18.36), ('OE2', 'GLU', 'CD', 'ARG', 17.12), ('OE2', 'GLU', 'NE', 'ARG', 16.46), ('OE2', 'GLU', 'CZ', 'ARG', 15.16), ('OE2', 'GLU', 'NH1', 'ARG', 14.35), ('OE2', 'GLU', 'NH2', 'ARG', 14.76), ('OE2', 'GLU', 'O', 'ARG', 21.34), ('OE2', 'GLU', 'C', 'ARG', 20.28), ('OE2', 'GLU', 'CA', 'ARG', 19.35), ('OE2', 'GLU', 'N', 'ARG', 20.08)], [('O', 'GLU', 'CB', 'ARG', 16.0), ('O', 'GLU', 'CG', 'ARG', 16.68), ('O', 'GLU', 'CD', 'ARG', 15.77), ('O', 'GLU', 'NE', 'ARG', 14.89), ('O', 'GLU', 'CZ', 'ARG', 13.59), ('O', 'GLU', 'NH1', 'ARG', 13.03), ('O', 'GLU', 'NH2', 'ARG', 12.97), ('O', 'GLU', 'O', 'ARG', 18.95), ('O', 'GLU', 'C', 'ARG', 17.77), ('O', 'GLU', 'CA', 'ARG', 17.02), ('O', 'GLU', 'N', 'ARG', 18.0)], [('C', 'GLU', 'CB', 'ARG', 16.7), ('C', 'GLU', 'CG', 'ARG', 17.39), ('C', 'GLU', 'CD', 'ARG', 16.46), ('C', 'GLU', 'NE', 'ARG', 15.66), ('C', 'GLU', 'CZ', 'ARG', 14.36), ('C', 'GLU', 'NH1', 'ARG', 13.71), ('C', 'GLU', 'NH2', 'ARG', 13.82), ('C', 'GLU', 'O', 'ARG', 19.72), ('C', 'GLU', 'C', 'ARG', 18.53), ('C', 'GLU', 'CA', 'ARG', 17.71), ('C', 'GLU', 'N', 'ARG', 18.63)], [('CA', 'GLU', 'CB', 'ARG', 16.17), ('CA', 'GLU', 'CG', 'ARG', 16.85), ('CA', 'GLU', 'CD', 'ARG', 15.92), ('CA', 'GLU', 'NE', 'ARG', 15.24), ('CA', 'GLU', 'CZ', 'ARG', 13.96), ('CA', 'GLU', 'NH1', 'ARG', 13.18), ('CA', 'GLU', 'NH2', 'ARG', 13.57), ('CA', 'GLU', 'O', 'ARG', 19.28), ('CA', 'GLU', 'C', 'ARG', 18.1), ('CA', 'GLU', 'CA', 'ARG', 17.17), ('CA', 'GLU', 'N', 'ARG', 17.99)], [('N', 'GLU', 'CB', 'ARG', 15.05), ('N', 'GLU', 'CG', 'ARG', 15.82), ('N', 'GLU', 'CD', 'ARG', 14.98), ('N', 'GLU', 'NE', 'ARG', 14.33), ('N', 'GLU', 'CZ', 'ARG', 13.08), ('N', 'GLU', 'NH1', 'ARG', 12.31), ('N', 'GLU', 'NH2', 'ARG', 12.72), ('N', 'GLU', 'O', 'ARG', 18.11), ('N', 'GLU', 'C', 'ARG', 16.92), ('N', 'GLU', 'CA', 'ARG', 15.99), ('N', 'GLU', 'N', 'ARG', 16.81)]]}
ARG_LYS = { 
	'distances':
		[[13.35, 12.75, 13.79, 13.32, 12.73, 15.35, 14.24, 13.16, 11.87], [13.55, 13.12, 14.25, 13.91, 13.27, 15.34, 14.21, 13.27, 11.9], [12.46, 12.13, 13.28, 13.0, 12.28, 14.25, 13.09, 12.21, 10.84], [11.21, 10.89, 12.09, 11.9, 11.28, 12.93, 11.79, 10.89, 9.51], [10.03, 9.68, 10.84, 10.63, 9.98, 11.93, 10.77, 9.82, 8.48], [10.08, 9.69, 10.73, 10.4, 9.56, 12.22, 11.02, 10.07, 8.81], [8.95, 8.61, 9.86, 9.76, 9.25, 10.77, 9.65, 8.65, 7.31], [15.9, 15.31, 16.44, 16.06, 15.66, 17.55, 16.54, 15.49, 14.18], [14.94, 14.28, 15.37, 14.93, 14.53, 16.73, 15.71, 14.6, 13.33], [14.63, 13.94, 14.95, 14.41, 13.88, 16.64, 15.56, 14.44, 13.17], [15.78, 15.13, 16.12, 15.55, 14.92, 17.8, 16.7, 15.62, 14.33]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 13.35), ('CB', 'ARG', 'CG', 'LYS', 12.75), ('CB', 'ARG', 'CD', 'LYS', 13.79), ('CB', 'ARG', 'CE', 'LYS', 13.32), ('CB', 'ARG', 'NZ', 'LYS', 12.73), ('CB', 'ARG', 'O', 'LYS', 15.35), ('CB', 'ARG', 'C', 'LYS', 14.24), ('CB', 'ARG', 'CA', 'LYS', 13.16), ('CB', 'ARG', 'N', 'LYS', 11.87)], [('CG', 'ARG', 'CB', 'LYS', 13.55), ('CG', 'ARG', 'CG', 'LYS', 13.12), ('CG', 'ARG', 'CD', 'LYS', 14.25), ('CG', 'ARG', 'CE', 'LYS', 13.91), ('CG', 'ARG', 'NZ', 'LYS', 13.27), ('CG', 'ARG', 'O', 'LYS', 15.34), ('CG', 'ARG', 'C', 'LYS', 14.21), ('CG', 'ARG', 'CA', 'LYS', 13.27), ('CG', 'ARG', 'N', 'LYS', 11.9)], [('CD', 'ARG', 'CB', 'LYS', 12.46), ('CD', 'ARG', 'CG', 'LYS', 12.13), ('CD', 'ARG', 'CD', 'LYS', 13.28), ('CD', 'ARG', 'CE', 'LYS', 13.0), ('CD', 'ARG', 'NZ', 'LYS', 12.28), ('CD', 'ARG', 'O', 'LYS', 14.25), ('CD', 'ARG', 'C', 'LYS', 13.09), ('CD', 'ARG', 'CA', 'LYS', 12.21), ('CD', 'ARG', 'N', 'LYS', 10.84)], [('NE', 'ARG', 'CB', 'LYS', 11.21), ('NE', 'ARG', 'CG', 'LYS', 10.89), ('NE', 'ARG', 'CD', 'LYS', 12.09), ('NE', 'ARG', 'CE', 'LYS', 11.9), ('NE', 'ARG', 'NZ', 'LYS', 11.28), ('NE', 'ARG', 'O', 'LYS', 12.93), ('NE', 'ARG', 'C', 'LYS', 11.79), ('NE', 'ARG', 'CA', 'LYS', 10.89), ('NE', 'ARG', 'N', 'LYS', 9.51)], [('CZ', 'ARG', 'CB', 'LYS', 10.03), ('CZ', 'ARG', 'CG', 'LYS', 9.68), ('CZ', 'ARG', 'CD', 'LYS', 10.84), ('CZ', 'ARG', 'CE', 'LYS', 10.63), ('CZ', 'ARG', 'NZ', 'LYS', 9.98), ('CZ', 'ARG', 'O', 'LYS', 11.93), ('CZ', 'ARG', 'C', 'LYS', 10.77), ('CZ', 'ARG', 'CA', 'LYS', 9.82), ('CZ', 'ARG', 'N', 'LYS', 8.48)], [('NH1', 'ARG', 'CB', 'LYS', 10.08), ('NH1', 'ARG', 'CG', 'LYS', 9.69), ('NH1', 'ARG', 'CD', 'LYS', 10.73), ('NH1', 'ARG', 'CE', 'LYS', 10.4), ('NH1', 'ARG', 'NZ', 'LYS', 9.56), ('NH1', 'ARG', 'O', 'LYS', 12.22), ('NH1', 'ARG', 'C', 'LYS', 11.02), ('NH1', 'ARG', 'CA', 'LYS', 10.07), ('NH1', 'ARG', 'N', 'LYS', 8.81)], [('NH2', 'ARG', 'CB', 'LYS', 8.95), ('NH2', 'ARG', 'CG', 'LYS', 8.61), ('NH2', 'ARG', 'CD', 'LYS', 9.86), ('NH2', 'ARG', 'CE', 'LYS', 9.76), ('NH2', 'ARG', 'NZ', 'LYS', 9.25), ('NH2', 'ARG', 'O', 'LYS', 10.77), ('NH2', 'ARG', 'C', 'LYS', 9.65), ('NH2', 'ARG', 'CA', 'LYS', 8.65), ('NH2', 'ARG', 'N', 'LYS', 7.31)], [('O', 'ARG', 'CB', 'LYS', 15.9), ('O', 'ARG', 'CG', 'LYS', 15.31), ('O', 'ARG', 'CD', 'LYS', 16.44), ('O', 'ARG', 'CE', 'LYS', 16.06), ('O', 'ARG', 'NZ', 'LYS', 15.66), ('O', 'ARG', 'O', 'LYS', 17.55), ('O', 'ARG', 'C', 'LYS', 16.54), ('O', 'ARG', 'CA', 'LYS', 15.49), ('O', 'ARG', 'N', 'LYS', 14.18)], [('C', 'ARG', 'CB', 'LYS', 14.94), ('C', 'ARG', 'CG', 'LYS', 14.28), ('C', 'ARG', 'CD', 'LYS', 15.37), ('C', 'ARG', 'CE', 'LYS', 14.93), ('C', 'ARG', 'NZ', 'LYS', 14.53), ('C', 'ARG', 'O', 'LYS', 16.73), ('C', 'ARG', 'C', 'LYS', 15.71), ('C', 'ARG', 'CA', 'LYS', 14.6), ('C', 'ARG', 'N', 'LYS', 13.33)], [('CA', 'ARG', 'CB', 'LYS', 14.63), ('CA', 'ARG', 'CG', 'LYS', 13.94), ('CA', 'ARG', 'CD', 'LYS', 14.95), ('CA', 'ARG', 'CE', 'LYS', 14.41), ('CA', 'ARG', 'NZ', 'LYS', 13.88), ('CA', 'ARG', 'O', 'LYS', 16.64), ('CA', 'ARG', 'C', 'LYS', 15.56), ('CA', 'ARG', 'CA', 'LYS', 14.44), ('CA', 'ARG', 'N', 'LYS', 13.17)], [('N', 'ARG', 'CB', 'LYS', 15.78), ('N', 'ARG', 'CG', 'LYS', 15.13), ('N', 'ARG', 'CD', 'LYS', 16.12), ('N', 'ARG', 'CE', 'LYS', 15.55), ('N', 'ARG', 'NZ', 'LYS', 14.92), ('N', 'ARG', 'O', 'LYS', 17.8), ('N', 'ARG', 'C', 'LYS', 16.7), ('N', 'ARG', 'CA', 'LYS', 15.62), ('N', 'ARG', 'N', 'LYS', 14.33)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'P_1qtq_6_1_1_18')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ARG, d, 'P_1qtq_6_1_1_18')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_LYS, d, 'P_1qtq_6_1_1_18')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'GLU_ARG' :  match2,
		'ARG_LYS' :  match3}