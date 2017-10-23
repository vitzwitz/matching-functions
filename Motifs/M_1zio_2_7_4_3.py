'''
FUNC:M_1zio_2_7_4_3
PDB:1zio
EC:2.7.4.3
RESI:lys,arg,arg,asp,asp,arg,mg
LOCI:a-13,127,160,162,163,171,220;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[16.96, 15.72, 15.82, 14.75], [17.03, 15.89, 16.11, 14.88], [16.6, 15.51, 15.84, 14.43], [15.09, 14.0, 14.36, 12.91], [14.4, 13.38, 13.77, 12.34], [16.75, 15.31, 14.49, 15.09], [16.97, 15.59, 14.68, 15.5], [17.11, 15.75, 14.76, 15.75], [15.83, 14.47, 13.46, 14.52], [14.86, 13.56, 12.51, 13.68]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 16.96), ('CB', 'LYS', 'CG', 'ASP', 15.72), ('CB', 'LYS', 'OD1', 'ASP', 15.82), ('CB', 'LYS', 'OD2', 'ASP', 14.75)], [('CG', 'LYS', 'CB', 'ASP', 17.03), ('CG', 'LYS', 'CG', 'ASP', 15.89), ('CG', 'LYS', 'OD1', 'ASP', 16.11), ('CG', 'LYS', 'OD2', 'ASP', 14.88)], [('CD', 'LYS', 'CB', 'ASP', 16.6), ('CD', 'LYS', 'CG', 'ASP', 15.51), ('CD', 'LYS', 'OD1', 'ASP', 15.84), ('CD', 'LYS', 'OD2', 'ASP', 14.43)], [('CE', 'LYS', 'CB', 'ASP', 15.09), ('CE', 'LYS', 'CG', 'ASP', 14.0), ('CE', 'LYS', 'OD1', 'ASP', 14.36), ('CE', 'LYS', 'OD2', 'ASP', 12.91)], [('NZ', 'LYS', 'CB', 'ASP', 14.4), ('NZ', 'LYS', 'CG', 'ASP', 13.38), ('NZ', 'LYS', 'OD1', 'ASP', 13.77), ('NZ', 'LYS', 'OD2', 'ASP', 12.34)], [('CB', 'LYS', 'CB', 'ASP', 16.75), ('CB', 'LYS', 'CG', 'ASP', 15.31), ('CB', 'LYS', 'OD1', 'ASP', 14.49), ('CB', 'LYS', 'OD2', 'ASP', 15.09)], [('CG', 'LYS', 'CB', 'ASP', 16.97), ('CG', 'LYS', 'CG', 'ASP', 15.59), ('CG', 'LYS', 'OD1', 'ASP', 14.68), ('CG', 'LYS', 'OD2', 'ASP', 15.5)], [('CD', 'LYS', 'CB', 'ASP', 17.11), ('CD', 'LYS', 'CG', 'ASP', 15.75), ('CD', 'LYS', 'OD1', 'ASP', 14.76), ('CD', 'LYS', 'OD2', 'ASP', 15.75)], [('CE', 'LYS', 'CB', 'ASP', 15.83), ('CE', 'LYS', 'CG', 'ASP', 14.47), ('CE', 'LYS', 'OD1', 'ASP', 13.46), ('CE', 'LYS', 'OD2', 'ASP', 14.52)], [('NZ', 'LYS', 'CB', 'ASP', 14.86), ('NZ', 'LYS', 'CG', 'ASP', 13.56), ('NZ', 'LYS', 'OD1', 'ASP', 12.51), ('NZ', 'LYS', 'OD2', 'ASP', 13.68)]]}
ASP_MG = { 
	'distances':
		[[13.2], [11.78], [11.64], [10.94], [13.18], [11.66], [10.99], [11.26]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 13.2)], [('CG', 'ASP', 'MG', 'MG', 11.78)], [('OD1', 'ASP', 'MG', 'MG', 11.64)], [('OD2', 'ASP', 'MG', 'MG', 10.94)], [('CB', 'ASP', 'MG', 'MG', 13.18)], [('CG', 'ASP', 'MG', 'MG', 11.66)], [('OD1', 'ASP', 'MG', 'MG', 10.99)], [('OD2', 'ASP', 'MG', 'MG', 11.26)]]}
MG_ARGII = { 
	'distances':
		[12.02, 11.3, 9.76, 9.27, 8.05, 7.02, 8.07],
	'comparisons':
		[('MG', 'MG', 'CB', 'ARGII', 12.02), ('MG', 'MG', 'CG', 'ARGII', 11.3), ('MG', 'MG', 'CD', 'ARGII', 9.76), ('MG', 'MG', 'NE', 'ARGII', 9.27), ('MG', 'MG', 'CZ', 'ARGII', 8.05), ('MG', 'MG', 'NH1', 'ARGII', 7.02), ('MG', 'MG', 'NH2', 'ARGII', 8.07)]}
ASP_ASP = { 
	'distances':
		[[7.74, 7.66, 7.15, 8.47], [7.5, 7.03, 6.46, 7.66], [6.92, 6.4, 6.09, 6.83], [8.27, 7.59, 6.81, 8.17], [7.74, 7.5, 6.92, 8.27], [7.66, 7.03, 6.4, 7.59], [7.15, 6.46, 6.09, 6.81], [8.47, 7.66, 6.83, 8.17]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.74), ('CB', 'ASP', 'CG', 'ASP', 7.66), ('CB', 'ASP', 'OD1', 'ASP', 7.15), ('CB', 'ASP', 'OD2', 'ASP', 8.47)], [('CG', 'ASP', 'CB', 'ASP', 7.5), ('CG', 'ASP', 'CG', 'ASP', 7.03), ('CG', 'ASP', 'OD1', 'ASP', 6.46), ('CG', 'ASP', 'OD2', 'ASP', 7.66)], [('OD1', 'ASP', 'CB', 'ASP', 6.92), ('OD1', 'ASP', 'CG', 'ASP', 6.4), ('OD1', 'ASP', 'OD1', 'ASP', 6.09), ('OD1', 'ASP', 'OD2', 'ASP', 6.83)], [('OD2', 'ASP', 'CB', 'ASP', 8.27), ('OD2', 'ASP', 'CG', 'ASP', 7.59), ('OD2', 'ASP', 'OD1', 'ASP', 6.81), ('OD2', 'ASP', 'OD2', 'ASP', 8.17)], [('CB', 'ASP', 'CB', 'ASP', 7.74), ('CB', 'ASP', 'CG', 'ASP', 7.5), ('CB', 'ASP', 'OD1', 'ASP', 6.92), ('CB', 'ASP', 'OD2', 'ASP', 8.27)], [('CG', 'ASP', 'CB', 'ASP', 7.66), ('CG', 'ASP', 'CG', 'ASP', 7.03), ('CG', 'ASP', 'OD1', 'ASP', 6.4), ('CG', 'ASP', 'OD2', 'ASP', 7.59)], [('OD1', 'ASP', 'CB', 'ASP', 7.15), ('OD1', 'ASP', 'CG', 'ASP', 6.46), ('OD1', 'ASP', 'OD1', 'ASP', 6.09), ('OD1', 'ASP', 'OD2', 'ASP', 6.81)], [('OD2', 'ASP', 'CB', 'ASP', 8.47), ('OD2', 'ASP', 'CG', 'ASP', 7.66), ('OD2', 'ASP', 'OD1', 'ASP', 6.83), ('OD2', 'ASP', 'OD2', 'ASP', 8.17)]]}
ARG_ARGI = { 
	'distances':
		[[12.99, 12.07, 10.58, 10.2, 9.2, 8.37, 9.27], [13.2, 12.21, 10.78, 10.28, 9.35, 8.76, 9.28], [12.69, 11.81, 10.42, 9.68, 8.68, 8.3, 8.36], [11.29, 10.41, 9.05, 8.27, 7.32, 7.06, 7.0], [10.89, 10.13, 8.87, 7.87, 6.93, 6.99, 6.33], [11.86, 11.21, 10.0, 8.88, 7.92, 8.08, 7.1], [9.7, 8.96, 7.78, 6.7, 5.9, 6.23, 5.27]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARGI', 12.99), ('CB', 'ARG', 'CG', 'ARGI', 12.07), ('CB', 'ARG', 'CD', 'ARGI', 10.58), ('CB', 'ARG', 'NE', 'ARGI', 10.2), ('CB', 'ARG', 'CZ', 'ARGI', 9.2), ('CB', 'ARG', 'NH1', 'ARGI', 8.37), ('CB', 'ARG', 'NH2', 'ARGI', 9.27)], [('CG', 'ARG', 'CB', 'ARGI', 13.2), ('CG', 'ARG', 'CG', 'ARGI', 12.21), ('CG', 'ARG', 'CD', 'ARGI', 10.78), ('CG', 'ARG', 'NE', 'ARGI', 10.28), ('CG', 'ARG', 'CZ', 'ARGI', 9.35), ('CG', 'ARG', 'NH1', 'ARGI', 8.76), ('CG', 'ARG', 'NH2', 'ARGI', 9.28)], [('CD', 'ARG', 'CB', 'ARGI', 12.69), ('CD', 'ARG', 'CG', 'ARGI', 11.81), ('CD', 'ARG', 'CD', 'ARGI', 10.42), ('CD', 'ARG', 'NE', 'ARGI', 9.68), ('CD', 'ARG', 'CZ', 'ARGI', 8.68), ('CD', 'ARG', 'NH1', 'ARGI', 8.3), ('CD', 'ARG', 'NH2', 'ARGI', 8.36)], [('NE', 'ARG', 'CB', 'ARGI', 11.29), ('NE', 'ARG', 'CG', 'ARGI', 10.41), ('NE', 'ARG', 'CD', 'ARGI', 9.05), ('NE', 'ARG', 'NE', 'ARGI', 8.27), ('NE', 'ARG', 'CZ', 'ARGI', 7.32), ('NE', 'ARG', 'NH1', 'ARGI', 7.06), ('NE', 'ARG', 'NH2', 'ARGI', 7.0)], [('CZ', 'ARG', 'CB', 'ARGI', 10.89), ('CZ', 'ARG', 'CG', 'ARGI', 10.13), ('CZ', 'ARG', 'CD', 'ARGI', 8.87), ('CZ', 'ARG', 'NE', 'ARGI', 7.87), ('CZ', 'ARG', 'CZ', 'ARGI', 6.93), ('CZ', 'ARG', 'NH1', 'ARGI', 6.99), ('CZ', 'ARG', 'NH2', 'ARGI', 6.33)], [('NH1', 'ARG', 'CB', 'ARGI', 11.86), ('NH1', 'ARG', 'CG', 'ARGI', 11.21), ('NH1', 'ARG', 'CD', 'ARGI', 10.0), ('NH1', 'ARG', 'NE', 'ARGI', 8.88), ('NH1', 'ARG', 'CZ', 'ARGI', 7.92), ('NH1', 'ARG', 'NH1', 'ARGI', 8.08), ('NH1', 'ARG', 'NH2', 'ARGI', 7.1)], [('NH2', 'ARG', 'CB', 'ARGI', 9.7), ('NH2', 'ARG', 'CG', 'ARGI', 8.96), ('NH2', 'ARG', 'CD', 'ARGI', 7.78), ('NH2', 'ARG', 'NE', 'ARGI', 6.7), ('NH2', 'ARG', 'CZ', 'ARGI', 5.9), ('NH2', 'ARG', 'NH1', 'ARGI', 6.23), ('NH2', 'ARG', 'NH2', 'ARGI', 5.27)]]}
ARG_ARG = { 
	'distances':
		[[14.49, 14.36, 12.98, 12.25, 10.94, 10.16, 10.58], [14.99, 14.75, 13.33, 12.51, 11.18, 10.49, 10.7], [14.25, 14.03, 12.64, 11.68, 10.35, 9.84, 9.7], [12.93, 12.63, 11.23, 10.28, 8.96, 8.43, 8.36], [12.06, 11.81, 10.47, 9.4, 8.09, 7.78, 7.32], [12.51, 12.38, 11.14, 9.94, 8.68, 8.59, 7.72], [10.9, 10.56, 9.21, 8.15, 6.85, 6.56, 6.14], [8.74, 9.67, 9.27, 9.61, 9.89, 9.86, 10.55], [8.2, 8.92, 8.45, 8.99, 9.28, 9.07, 10.12], [8.04, 8.5, 7.72, 8.13, 8.19, 7.83, 9.01], [7.04, 7.5, 6.66, 6.86, 6.93, 6.78, 7.68], [7.45, 7.67, 6.57, 6.43, 6.17, 5.96, 6.75], [8.66, 8.71, 7.46, 7.29, 6.76, 6.24, 7.24], [6.97, 7.14, 6.04, 5.53, 5.23, 5.38, 5.62], [14.49, 14.99, 14.25, 12.93, 12.06, 12.51, 10.9], [14.36, 14.75, 14.03, 12.63, 11.81, 12.38, 10.56], [12.98, 13.33, 12.64, 11.23, 10.47, 11.14, 9.21], [12.25, 12.51, 11.68, 10.28, 9.4, 9.94, 8.15], [10.94, 11.18, 10.35, 8.96, 8.09, 8.68, 6.85], [10.16, 10.49, 9.84, 8.43, 7.78, 8.59, 6.56], [10.58, 10.7, 9.7, 8.36, 7.32, 7.72, 6.14], [12.99, 13.2, 12.69, 11.29, 10.89, 11.86, 9.7], [12.07, 12.21, 11.81, 10.41, 10.13, 11.21, 8.96], [10.58, 10.78, 10.42, 9.05, 8.87, 10.0, 7.78], [10.2, 10.28, 9.68, 8.27, 7.87, 8.88, 6.7], [9.2, 9.35, 8.68, 7.32, 6.93, 7.92, 5.9], [8.37, 8.76, 8.3, 7.06, 6.99, 8.08, 6.23], [9.27, 9.28, 8.36, 7.0, 6.33, 7.1, 5.27], [8.74, 8.2, 8.04, 7.04, 7.45, 8.66, 6.97], [9.67, 8.92, 8.5, 7.5, 7.67, 8.71, 7.14], [9.27, 8.45, 7.72, 6.66, 6.57, 7.46, 6.04], [9.61, 8.99, 8.13, 6.86, 6.43, 7.29, 5.53], [9.89, 9.28, 8.19, 6.93, 6.17, 6.76, 5.23], [9.86, 9.07, 7.83, 6.78, 5.96, 6.24, 5.38], [10.55, 10.12, 9.01, 7.68, 6.75, 7.24, 5.62]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 14.49), ('CB', 'ARG', 'CG', 'ARG', 14.36), ('CB', 'ARG', 'CD', 'ARG', 12.98), ('CB', 'ARG', 'NE', 'ARG', 12.25), ('CB', 'ARG', 'CZ', 'ARG', 10.94), ('CB', 'ARG', 'NH1', 'ARG', 10.16), ('CB', 'ARG', 'NH2', 'ARG', 10.58)], [('CG', 'ARG', 'CB', 'ARG', 14.99), ('CG', 'ARG', 'CG', 'ARG', 14.75), ('CG', 'ARG', 'CD', 'ARG', 13.33), ('CG', 'ARG', 'NE', 'ARG', 12.51), ('CG', 'ARG', 'CZ', 'ARG', 11.18), ('CG', 'ARG', 'NH1', 'ARG', 10.49), ('CG', 'ARG', 'NH2', 'ARG', 10.7)], [('CD', 'ARG', 'CB', 'ARG', 14.25), ('CD', 'ARG', 'CG', 'ARG', 14.03), ('CD', 'ARG', 'CD', 'ARG', 12.64), ('CD', 'ARG', 'NE', 'ARG', 11.68), ('CD', 'ARG', 'CZ', 'ARG', 10.35), ('CD', 'ARG', 'NH1', 'ARG', 9.84), ('CD', 'ARG', 'NH2', 'ARG', 9.7)], [('NE', 'ARG', 'CB', 'ARG', 12.93), ('NE', 'ARG', 'CG', 'ARG', 12.63), ('NE', 'ARG', 'CD', 'ARG', 11.23), ('NE', 'ARG', 'NE', 'ARG', 10.28), ('NE', 'ARG', 'CZ', 'ARG', 8.96), ('NE', 'ARG', 'NH1', 'ARG', 8.43), ('NE', 'ARG', 'NH2', 'ARG', 8.36)], [('CZ', 'ARG', 'CB', 'ARG', 12.06), ('CZ', 'ARG', 'CG', 'ARG', 11.81), ('CZ', 'ARG', 'CD', 'ARG', 10.47), ('CZ', 'ARG', 'NE', 'ARG', 9.4), ('CZ', 'ARG', 'CZ', 'ARG', 8.09), ('CZ', 'ARG', 'NH1', 'ARG', 7.78), ('CZ', 'ARG', 'NH2', 'ARG', 7.32)], [('NH1', 'ARG', 'CB', 'ARG', 12.51), ('NH1', 'ARG', 'CG', 'ARG', 12.38), ('NH1', 'ARG', 'CD', 'ARG', 11.14), ('NH1', 'ARG', 'NE', 'ARG', 9.94), ('NH1', 'ARG', 'CZ', 'ARG', 8.68), ('NH1', 'ARG', 'NH1', 'ARG', 8.59), ('NH1', 'ARG', 'NH2', 'ARG', 7.72)], [('NH2', 'ARG', 'CB', 'ARG', 10.9), ('NH2', 'ARG', 'CG', 'ARG', 10.56), ('NH2', 'ARG', 'CD', 'ARG', 9.21), ('NH2', 'ARG', 'NE', 'ARG', 8.15), ('NH2', 'ARG', 'CZ', 'ARG', 6.85), ('NH2', 'ARG', 'NH1', 'ARG', 6.56), ('NH2', 'ARG', 'NH2', 'ARG', 6.14)], [('CB', 'ARG', 'CB', 'ARG', 8.74), ('CB', 'ARG', 'CG', 'ARG', 9.67), ('CB', 'ARG', 'CD', 'ARG', 9.27), ('CB', 'ARG', 'NE', 'ARG', 9.61), ('CB', 'ARG', 'CZ', 'ARG', 9.89), ('CB', 'ARG', 'NH1', 'ARG', 9.86), ('CB', 'ARG', 'NH2', 'ARG', 10.55)], [('CG', 'ARG', 'CB', 'ARG', 8.2), ('CG', 'ARG', 'CG', 'ARG', 8.92), ('CG', 'ARG', 'CD', 'ARG', 8.45), ('CG', 'ARG', 'NE', 'ARG', 8.99), ('CG', 'ARG', 'CZ', 'ARG', 9.28), ('CG', 'ARG', 'NH1', 'ARG', 9.07), ('CG', 'ARG', 'NH2', 'ARG', 10.12)], [('CD', 'ARG', 'CB', 'ARG', 8.04), ('CD', 'ARG', 'CG', 'ARG', 8.5), ('CD', 'ARG', 'CD', 'ARG', 7.72), ('CD', 'ARG', 'NE', 'ARG', 8.13), ('CD', 'ARG', 'CZ', 'ARG', 8.19), ('CD', 'ARG', 'NH1', 'ARG', 7.83), ('CD', 'ARG', 'NH2', 'ARG', 9.01)], [('NE', 'ARG', 'CB', 'ARG', 7.04), ('NE', 'ARG', 'CG', 'ARG', 7.5), ('NE', 'ARG', 'CD', 'ARG', 6.66), ('NE', 'ARG', 'NE', 'ARG', 6.86), ('NE', 'ARG', 'CZ', 'ARG', 6.93), ('NE', 'ARG', 'NH1', 'ARG', 6.78), ('NE', 'ARG', 'NH2', 'ARG', 7.68)], [('CZ', 'ARG', 'CB', 'ARG', 7.45), ('CZ', 'ARG', 'CG', 'ARG', 7.67), ('CZ', 'ARG', 'CD', 'ARG', 6.57), ('CZ', 'ARG', 'NE', 'ARG', 6.43), ('CZ', 'ARG', 'CZ', 'ARG', 6.17), ('CZ', 'ARG', 'NH1', 'ARG', 5.96), ('CZ', 'ARG', 'NH2', 'ARG', 6.75)], [('NH1', 'ARG', 'CB', 'ARG', 8.66), ('NH1', 'ARG', 'CG', 'ARG', 8.71), ('NH1', 'ARG', 'CD', 'ARG', 7.46), ('NH1', 'ARG', 'NE', 'ARG', 7.29), ('NH1', 'ARG', 'CZ', 'ARG', 6.76), ('NH1', 'ARG', 'NH1', 'ARG', 6.24), ('NH1', 'ARG', 'NH2', 'ARG', 7.24)], [('NH2', 'ARG', 'CB', 'ARG', 6.97), ('NH2', 'ARG', 'CG', 'ARG', 7.14), ('NH2', 'ARG', 'CD', 'ARG', 6.04), ('NH2', 'ARG', 'NE', 'ARG', 5.53), ('NH2', 'ARG', 'CZ', 'ARG', 5.23), ('NH2', 'ARG', 'NH1', 'ARG', 5.38), ('NH2', 'ARG', 'NH2', 'ARG', 5.62)], [('CB', 'ARG', 'CB', 'ARG', 14.49), ('CB', 'ARG', 'CG', 'ARG', 14.99), ('CB', 'ARG', 'CD', 'ARG', 14.25), ('CB', 'ARG', 'NE', 'ARG', 12.93), ('CB', 'ARG', 'CZ', 'ARG', 12.06), ('CB', 'ARG', 'NH1', 'ARG', 12.51), ('CB', 'ARG', 'NH2', 'ARG', 10.9)], [('CG', 'ARG', 'CB', 'ARG', 14.36), ('CG', 'ARG', 'CG', 'ARG', 14.75), ('CG', 'ARG', 'CD', 'ARG', 14.03), ('CG', 'ARG', 'NE', 'ARG', 12.63), ('CG', 'ARG', 'CZ', 'ARG', 11.81), ('CG', 'ARG', 'NH1', 'ARG', 12.38), ('CG', 'ARG', 'NH2', 'ARG', 10.56)], [('CD', 'ARG', 'CB', 'ARG', 12.98), ('CD', 'ARG', 'CG', 'ARG', 13.33), ('CD', 'ARG', 'CD', 'ARG', 12.64), ('CD', 'ARG', 'NE', 'ARG', 11.23), ('CD', 'ARG', 'CZ', 'ARG', 10.47), ('CD', 'ARG', 'NH1', 'ARG', 11.14), ('CD', 'ARG', 'NH2', 'ARG', 9.21)], [('NE', 'ARG', 'CB', 'ARG', 12.25), ('NE', 'ARG', 'CG', 'ARG', 12.51), ('NE', 'ARG', 'CD', 'ARG', 11.68), ('NE', 'ARG', 'NE', 'ARG', 10.28), ('NE', 'ARG', 'CZ', 'ARG', 9.4), ('NE', 'ARG', 'NH1', 'ARG', 9.94), ('NE', 'ARG', 'NH2', 'ARG', 8.15)], [('CZ', 'ARG', 'CB', 'ARG', 10.94), ('CZ', 'ARG', 'CG', 'ARG', 11.18), ('CZ', 'ARG', 'CD', 'ARG', 10.35), ('CZ', 'ARG', 'NE', 'ARG', 8.96), ('CZ', 'ARG', 'CZ', 'ARG', 8.09), ('CZ', 'ARG', 'NH1', 'ARG', 8.68), ('CZ', 'ARG', 'NH2', 'ARG', 6.85)], [('NH1', 'ARG', 'CB', 'ARG', 10.16), ('NH1', 'ARG', 'CG', 'ARG', 10.49), ('NH1', 'ARG', 'CD', 'ARG', 9.84), ('NH1', 'ARG', 'NE', 'ARG', 8.43), ('NH1', 'ARG', 'CZ', 'ARG', 7.78), ('NH1', 'ARG', 'NH1', 'ARG', 8.59), ('NH1', 'ARG', 'NH2', 'ARG', 6.56)], [('NH2', 'ARG', 'CB', 'ARG', 10.58), ('NH2', 'ARG', 'CG', 'ARG', 10.7), ('NH2', 'ARG', 'CD', 'ARG', 9.7), ('NH2', 'ARG', 'NE', 'ARG', 8.36), ('NH2', 'ARG', 'CZ', 'ARG', 7.32), ('NH2', 'ARG', 'NH1', 'ARG', 7.72), ('NH2', 'ARG', 'NH2', 'ARG', 6.14)], [('CB', 'ARG', 'CB', 'ARG', 12.99), ('CB', 'ARG', 'CG', 'ARG', 13.2), ('CB', 'ARG', 'CD', 'ARG', 12.69), ('CB', 'ARG', 'NE', 'ARG', 11.29), ('CB', 'ARG', 'CZ', 'ARG', 10.89), ('CB', 'ARG', 'NH1', 'ARG', 11.86), ('CB', 'ARG', 'NH2', 'ARG', 9.7)], [('CG', 'ARG', 'CB', 'ARG', 12.07), ('CG', 'ARG', 'CG', 'ARG', 12.21), ('CG', 'ARG', 'CD', 'ARG', 11.81), ('CG', 'ARG', 'NE', 'ARG', 10.41), ('CG', 'ARG', 'CZ', 'ARG', 10.13), ('CG', 'ARG', 'NH1', 'ARG', 11.21), ('CG', 'ARG', 'NH2', 'ARG', 8.96)], [('CD', 'ARG', 'CB', 'ARG', 10.58), ('CD', 'ARG', 'CG', 'ARG', 10.78), ('CD', 'ARG', 'CD', 'ARG', 10.42), ('CD', 'ARG', 'NE', 'ARG', 9.05), ('CD', 'ARG', 'CZ', 'ARG', 8.87), ('CD', 'ARG', 'NH1', 'ARG', 10.0), ('CD', 'ARG', 'NH2', 'ARG', 7.78)], [('NE', 'ARG', 'CB', 'ARG', 10.2), ('NE', 'ARG', 'CG', 'ARG', 10.28), ('NE', 'ARG', 'CD', 'ARG', 9.68), ('NE', 'ARG', 'NE', 'ARG', 8.27), ('NE', 'ARG', 'CZ', 'ARG', 7.87), ('NE', 'ARG', 'NH1', 'ARG', 8.88), ('NE', 'ARG', 'NH2', 'ARG', 6.7)], [('CZ', 'ARG', 'CB', 'ARG', 9.2), ('CZ', 'ARG', 'CG', 'ARG', 9.35), ('CZ', 'ARG', 'CD', 'ARG', 8.68), ('CZ', 'ARG', 'NE', 'ARG', 7.32), ('CZ', 'ARG', 'CZ', 'ARG', 6.93), ('CZ', 'ARG', 'NH1', 'ARG', 7.92), ('CZ', 'ARG', 'NH2', 'ARG', 5.9)], [('NH1', 'ARG', 'CB', 'ARG', 8.37), ('NH1', 'ARG', 'CG', 'ARG', 8.76), ('NH1', 'ARG', 'CD', 'ARG', 8.3), ('NH1', 'ARG', 'NE', 'ARG', 7.06), ('NH1', 'ARG', 'CZ', 'ARG', 6.99), ('NH1', 'ARG', 'NH1', 'ARG', 8.08), ('NH1', 'ARG', 'NH2', 'ARG', 6.23)], [('NH2', 'ARG', 'CB', 'ARG', 9.27), ('NH2', 'ARG', 'CG', 'ARG', 9.28), ('NH2', 'ARG', 'CD', 'ARG', 8.36), ('NH2', 'ARG', 'NE', 'ARG', 7.0), ('NH2', 'ARG', 'CZ', 'ARG', 6.33), ('NH2', 'ARG', 'NH1', 'ARG', 7.1), ('NH2', 'ARG', 'NH2', 'ARG', 5.27)], [('CB', 'ARG', 'CB', 'ARG', 8.74), ('CB', 'ARG', 'CG', 'ARG', 8.2), ('CB', 'ARG', 'CD', 'ARG', 8.04), ('CB', 'ARG', 'NE', 'ARG', 7.04), ('CB', 'ARG', 'CZ', 'ARG', 7.45), ('CB', 'ARG', 'NH1', 'ARG', 8.66), ('CB', 'ARG', 'NH2', 'ARG', 6.97)], [('CG', 'ARG', 'CB', 'ARG', 9.67), ('CG', 'ARG', 'CG', 'ARG', 8.92), ('CG', 'ARG', 'CD', 'ARG', 8.5), ('CG', 'ARG', 'NE', 'ARG', 7.5), ('CG', 'ARG', 'CZ', 'ARG', 7.67), ('CG', 'ARG', 'NH1', 'ARG', 8.71), ('CG', 'ARG', 'NH2', 'ARG', 7.14)], [('CD', 'ARG', 'CB', 'ARG', 9.27), ('CD', 'ARG', 'CG', 'ARG', 8.45), ('CD', 'ARG', 'CD', 'ARG', 7.72), ('CD', 'ARG', 'NE', 'ARG', 6.66), ('CD', 'ARG', 'CZ', 'ARG', 6.57), ('CD', 'ARG', 'NH1', 'ARG', 7.46), ('CD', 'ARG', 'NH2', 'ARG', 6.04)], [('NE', 'ARG', 'CB', 'ARG', 9.61), ('NE', 'ARG', 'CG', 'ARG', 8.99), ('NE', 'ARG', 'CD', 'ARG', 8.13), ('NE', 'ARG', 'NE', 'ARG', 6.86), ('NE', 'ARG', 'CZ', 'ARG', 6.43), ('NE', 'ARG', 'NH1', 'ARG', 7.29), ('NE', 'ARG', 'NH2', 'ARG', 5.53)], [('CZ', 'ARG', 'CB', 'ARG', 9.89), ('CZ', 'ARG', 'CG', 'ARG', 9.28), ('CZ', 'ARG', 'CD', 'ARG', 8.19), ('CZ', 'ARG', 'NE', 'ARG', 6.93), ('CZ', 'ARG', 'CZ', 'ARG', 6.17), ('CZ', 'ARG', 'NH1', 'ARG', 6.76), ('CZ', 'ARG', 'NH2', 'ARG', 5.23)], [('NH1', 'ARG', 'CB', 'ARG', 9.86), ('NH1', 'ARG', 'CG', 'ARG', 9.07), ('NH1', 'ARG', 'CD', 'ARG', 7.83), ('NH1', 'ARG', 'NE', 'ARG', 6.78), ('NH1', 'ARG', 'CZ', 'ARG', 5.96), ('NH1', 'ARG', 'NH1', 'ARG', 6.24), ('NH1', 'ARG', 'NH2', 'ARG', 5.38)], [('NH2', 'ARG', 'CB', 'ARG', 10.55), ('NH2', 'ARG', 'CG', 'ARG', 10.12), ('NH2', 'ARG', 'CD', 'ARG', 9.01), ('NH2', 'ARG', 'NE', 'ARG', 7.68), ('NH2', 'ARG', 'CZ', 'ARG', 6.75), ('NH2', 'ARG', 'NH1', 'ARG', 7.24), ('NH2', 'ARG', 'NH2', 'ARG', 5.62)]]}
ARG_MG = { 
	'distances':
		[[12.03], [11.3], [9.79], [9.36], [8.23], [7.29], [8.29], [13.5], [13.4], [12.6], [11.17], [10.42], [11.11], [9.12], [12.02], [11.3], [9.76], [9.27], [8.05], [7.02], [8.07]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 12.03)], [('CG', 'ARG', 'MG', 'MG', 11.3)], [('CD', 'ARG', 'MG', 'MG', 9.79)], [('NE', 'ARG', 'MG', 'MG', 9.36)], [('CZ', 'ARG', 'MG', 'MG', 8.23)], [('NH1', 'ARG', 'MG', 'MG', 7.29)], [('NH2', 'ARG', 'MG', 'MG', 8.29)], [('CB', 'ARG', 'MG', 'MG', 13.5)], [('CG', 'ARG', 'MG', 'MG', 13.4)], [('CD', 'ARG', 'MG', 'MG', 12.6)], [('NE', 'ARG', 'MG', 'MG', 11.17)], [('CZ', 'ARG', 'MG', 'MG', 10.42)], [('NH1', 'ARG', 'MG', 'MG', 11.11)], [('NH2', 'ARG', 'MG', 'MG', 9.12)], [('CB', 'ARG', 'MG', 'MG', 12.02)], [('CG', 'ARG', 'MG', 'MG', 11.3)], [('CD', 'ARG', 'MG', 'MG', 9.76)], [('NE', 'ARG', 'MG', 'MG', 9.27)], [('CZ', 'ARG', 'MG', 'MG', 8.05)], [('NH1', 'ARG', 'MG', 'MG', 7.02)], [('NH2', 'ARG', 'MG', 'MG', 8.07)]]}
ARG_ASP = { 
	'distances':
		[[12.54, 11.71, 10.96, 12.04], [12.56, 11.58, 10.72, 11.87], [12.08, 10.96, 10.17, 11.08], [10.64, 9.52, 8.78, 9.63], [10.26, 9.05, 8.46, 8.96], [11.27, 10.01, 9.51, 9.76], [9.01, 7.81, 7.32, 7.68], [7.52, 6.92, 7.56, 6.18], [8.0, 7.18, 7.83, 6.17], [8.19, 7.06, 7.43, 6.06], [7.12, 5.82, 6.07, 4.9], [7.52, 6.07, 5.91, 5.43], [8.8, 7.35, 7.07, 6.76], [6.94, 5.43, 4.97, 5.1], [8.58, 8.89, 9.96, 8.33], [7.23, 7.66, 8.8, 7.15], [6.09, 6.39, 7.45, 5.98], [6.53, 6.31, 7.25, 5.63], [6.52, 6.0, 6.68, 5.43], [6.03, 5.66, 6.15, 5.52], [7.44, 6.61, 7.1, 5.87], [11.05, 10.75, 9.62, 11.79], [10.48, 10.21, 9.13, 11.25], [9.02, 8.72, 7.65, 9.75], [8.91, 8.3, 7.12, 9.2], [7.9, 7.13, 5.91, 7.97], [6.63, 6.03, 4.87, 7.01], [8.36, 7.32, 6.09, 7.94], [7.82, 6.95, 5.72, 7.72], [7.93, 6.82, 5.61, 7.41], [8.17, 6.83, 5.78, 7.08], [7.15, 5.7, 4.88, 5.74], [7.69, 6.18, 5.7, 5.81], [9.02, 7.5, 6.99, 7.07], [7.17, 5.72, 5.66, 5.01], [6.16, 5.66, 6.34, 5.15], [7.47, 6.74, 7.13, 6.21], [7.76, 6.66, 6.79, 6.07], [7.54, 6.36, 6.12, 6.12], [8.32, 7.0, 6.49, 6.8], [9.21, 7.8, 7.37, 7.38], [8.57, 7.3, 6.52, 7.4]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 12.54), ('CB', 'ARG', 'CG', 'ASP', 11.71), ('CB', 'ARG', 'OD1', 'ASP', 10.96), ('CB', 'ARG', 'OD2', 'ASP', 12.04)], [('CG', 'ARG', 'CB', 'ASP', 12.56), ('CG', 'ARG', 'CG', 'ASP', 11.58), ('CG', 'ARG', 'OD1', 'ASP', 10.72), ('CG', 'ARG', 'OD2', 'ASP', 11.87)], [('CD', 'ARG', 'CB', 'ASP', 12.08), ('CD', 'ARG', 'CG', 'ASP', 10.96), ('CD', 'ARG', 'OD1', 'ASP', 10.17), ('CD', 'ARG', 'OD2', 'ASP', 11.08)], [('NE', 'ARG', 'CB', 'ASP', 10.64), ('NE', 'ARG', 'CG', 'ASP', 9.52), ('NE', 'ARG', 'OD1', 'ASP', 8.78), ('NE', 'ARG', 'OD2', 'ASP', 9.63)], [('CZ', 'ARG', 'CB', 'ASP', 10.26), ('CZ', 'ARG', 'CG', 'ASP', 9.05), ('CZ', 'ARG', 'OD1', 'ASP', 8.46), ('CZ', 'ARG', 'OD2', 'ASP', 8.96)], [('NH1', 'ARG', 'CB', 'ASP', 11.27), ('NH1', 'ARG', 'CG', 'ASP', 10.01), ('NH1', 'ARG', 'OD1', 'ASP', 9.51), ('NH1', 'ARG', 'OD2', 'ASP', 9.76)], [('NH2', 'ARG', 'CB', 'ASP', 9.01), ('NH2', 'ARG', 'CG', 'ASP', 7.81), ('NH2', 'ARG', 'OD1', 'ASP', 7.32), ('NH2', 'ARG', 'OD2', 'ASP', 7.68)], [('CB', 'ARG', 'CB', 'ASP', 7.52), ('CB', 'ARG', 'CG', 'ASP', 6.92), ('CB', 'ARG', 'OD1', 'ASP', 7.56), ('CB', 'ARG', 'OD2', 'ASP', 6.18)], [('CG', 'ARG', 'CB', 'ASP', 8.0), ('CG', 'ARG', 'CG', 'ASP', 7.18), ('CG', 'ARG', 'OD1', 'ASP', 7.83), ('CG', 'ARG', 'OD2', 'ASP', 6.17)], [('CD', 'ARG', 'CB', 'ASP', 8.19), ('CD', 'ARG', 'CG', 'ASP', 7.06), ('CD', 'ARG', 'OD1', 'ASP', 7.43), ('CD', 'ARG', 'OD2', 'ASP', 6.06)], [('NE', 'ARG', 'CB', 'ASP', 7.12), ('NE', 'ARG', 'CG', 'ASP', 5.82), ('NE', 'ARG', 'OD1', 'ASP', 6.07), ('NE', 'ARG', 'OD2', 'ASP', 4.9)], [('CZ', 'ARG', 'CB', 'ASP', 7.52), ('CZ', 'ARG', 'CG', 'ASP', 6.07), ('CZ', 'ARG', 'OD1', 'ASP', 5.91), ('CZ', 'ARG', 'OD2', 'ASP', 5.43)], [('NH1', 'ARG', 'CB', 'ASP', 8.8), ('NH1', 'ARG', 'CG', 'ASP', 7.35), ('NH1', 'ARG', 'OD1', 'ASP', 7.07), ('NH1', 'ARG', 'OD2', 'ASP', 6.76)], [('NH2', 'ARG', 'CB', 'ASP', 6.94), ('NH2', 'ARG', 'CG', 'ASP', 5.43), ('NH2', 'ARG', 'OD1', 'ASP', 4.97), ('NH2', 'ARG', 'OD2', 'ASP', 5.1)], [('CB', 'ARG', 'CB', 'ASP', 8.58), ('CB', 'ARG', 'CG', 'ASP', 8.89), ('CB', 'ARG', 'OD1', 'ASP', 9.96), ('CB', 'ARG', 'OD2', 'ASP', 8.33)], [('CG', 'ARG', 'CB', 'ASP', 7.23), ('CG', 'ARG', 'CG', 'ASP', 7.66), ('CG', 'ARG', 'OD1', 'ASP', 8.8), ('CG', 'ARG', 'OD2', 'ASP', 7.15)], [('CD', 'ARG', 'CB', 'ASP', 6.09), ('CD', 'ARG', 'CG', 'ASP', 6.39), ('CD', 'ARG', 'OD1', 'ASP', 7.45), ('CD', 'ARG', 'OD2', 'ASP', 5.98)], [('NE', 'ARG', 'CB', 'ASP', 6.53), ('NE', 'ARG', 'CG', 'ASP', 6.31), ('NE', 'ARG', 'OD1', 'ASP', 7.25), ('NE', 'ARG', 'OD2', 'ASP', 5.63)], [('CZ', 'ARG', 'CB', 'ASP', 6.52), ('CZ', 'ARG', 'CG', 'ASP', 6.0), ('CZ', 'ARG', 'OD1', 'ASP', 6.68), ('CZ', 'ARG', 'OD2', 'ASP', 5.43)], [('NH1', 'ARG', 'CB', 'ASP', 6.03), ('NH1', 'ARG', 'CG', 'ASP', 5.66), ('NH1', 'ARG', 'OD1', 'ASP', 6.15), ('NH1', 'ARG', 'OD2', 'ASP', 5.52)], [('NH2', 'ARG', 'CB', 'ASP', 7.44), ('NH2', 'ARG', 'CG', 'ASP', 6.61), ('NH2', 'ARG', 'OD1', 'ASP', 7.1), ('NH2', 'ARG', 'OD2', 'ASP', 5.87)], [('CB', 'ARG', 'CB', 'ASP', 11.05), ('CB', 'ARG', 'CG', 'ASP', 10.75), ('CB', 'ARG', 'OD1', 'ASP', 9.62), ('CB', 'ARG', 'OD2', 'ASP', 11.79)], [('CG', 'ARG', 'CB', 'ASP', 10.48), ('CG', 'ARG', 'CG', 'ASP', 10.21), ('CG', 'ARG', 'OD1', 'ASP', 9.13), ('CG', 'ARG', 'OD2', 'ASP', 11.25)], [('CD', 'ARG', 'CB', 'ASP', 9.02), ('CD', 'ARG', 'CG', 'ASP', 8.72), ('CD', 'ARG', 'OD1', 'ASP', 7.65), ('CD', 'ARG', 'OD2', 'ASP', 9.75)], [('NE', 'ARG', 'CB', 'ASP', 8.91), ('NE', 'ARG', 'CG', 'ASP', 8.3), ('NE', 'ARG', 'OD1', 'ASP', 7.12), ('NE', 'ARG', 'OD2', 'ASP', 9.2)], [('CZ', 'ARG', 'CB', 'ASP', 7.9), ('CZ', 'ARG', 'CG', 'ASP', 7.13), ('CZ', 'ARG', 'OD1', 'ASP', 5.91), ('CZ', 'ARG', 'OD2', 'ASP', 7.97)], [('NH1', 'ARG', 'CB', 'ASP', 6.63), ('NH1', 'ARG', 'CG', 'ASP', 6.03), ('NH1', 'ARG', 'OD1', 'ASP', 4.87), ('NH1', 'ARG', 'OD2', 'ASP', 7.01)], [('NH2', 'ARG', 'CB', 'ASP', 8.36), ('NH2', 'ARG', 'CG', 'ASP', 7.32), ('NH2', 'ARG', 'OD1', 'ASP', 6.09), ('NH2', 'ARG', 'OD2', 'ASP', 7.94)], [('CB', 'ARG', 'CB', 'ASP', 7.82), ('CB', 'ARG', 'CG', 'ASP', 6.95), ('CB', 'ARG', 'OD1', 'ASP', 5.72), ('CB', 'ARG', 'OD2', 'ASP', 7.72)], [('CG', 'ARG', 'CB', 'ASP', 7.93), ('CG', 'ARG', 'CG', 'ASP', 6.82), ('CG', 'ARG', 'OD1', 'ASP', 5.61), ('CG', 'ARG', 'OD2', 'ASP', 7.41)], [('CD', 'ARG', 'CB', 'ASP', 8.17), ('CD', 'ARG', 'CG', 'ASP', 6.83), ('CD', 'ARG', 'OD1', 'ASP', 5.78), ('CD', 'ARG', 'OD2', 'ASP', 7.08)], [('NE', 'ARG', 'CB', 'ASP', 7.15), ('NE', 'ARG', 'CG', 'ASP', 5.7), ('NE', 'ARG', 'OD1', 'ASP', 4.88), ('NE', 'ARG', 'OD2', 'ASP', 5.74)], [('CZ', 'ARG', 'CB', 'ASP', 7.69), ('CZ', 'ARG', 'CG', 'ASP', 6.18), ('CZ', 'ARG', 'OD1', 'ASP', 5.7), ('CZ', 'ARG', 'OD2', 'ASP', 5.81)], [('NH1', 'ARG', 'CB', 'ASP', 9.02), ('NH1', 'ARG', 'CG', 'ASP', 7.5), ('NH1', 'ARG', 'OD1', 'ASP', 6.99), ('NH1', 'ARG', 'OD2', 'ASP', 7.07)], [('NH2', 'ARG', 'CB', 'ASP', 7.17), ('NH2', 'ARG', 'CG', 'ASP', 5.72), ('NH2', 'ARG', 'OD1', 'ASP', 5.66), ('NH2', 'ARG', 'OD2', 'ASP', 5.01)], [('CB', 'ARG', 'CB', 'ASP', 6.16), ('CB', 'ARG', 'CG', 'ASP', 5.66), ('CB', 'ARG', 'OD1', 'ASP', 6.34), ('CB', 'ARG', 'OD2', 'ASP', 5.15)], [('CG', 'ARG', 'CB', 'ASP', 7.47), ('CG', 'ARG', 'CG', 'ASP', 6.74), ('CG', 'ARG', 'OD1', 'ASP', 7.13), ('CG', 'ARG', 'OD2', 'ASP', 6.21)], [('CD', 'ARG', 'CB', 'ASP', 7.76), ('CD', 'ARG', 'CG', 'ASP', 6.66), ('CD', 'ARG', 'OD1', 'ASP', 6.79), ('CD', 'ARG', 'OD2', 'ASP', 6.07)], [('NE', 'ARG', 'CB', 'ASP', 7.54), ('NE', 'ARG', 'CG', 'ASP', 6.36), ('NE', 'ARG', 'OD1', 'ASP', 6.12), ('NE', 'ARG', 'OD2', 'ASP', 6.12)], [('CZ', 'ARG', 'CB', 'ASP', 8.32), ('CZ', 'ARG', 'CG', 'ASP', 7.0), ('CZ', 'ARG', 'OD1', 'ASP', 6.49), ('CZ', 'ARG', 'OD2', 'ASP', 6.8)], [('NH1', 'ARG', 'CB', 'ASP', 9.21), ('NH1', 'ARG', 'CG', 'ASP', 7.8), ('NH1', 'ARG', 'OD1', 'ASP', 7.37), ('NH1', 'ARG', 'OD2', 'ASP', 7.38)], [('NH2', 'ARG', 'CB', 'ASP', 8.57), ('NH2', 'ARG', 'CG', 'ASP', 7.3), ('NH2', 'ARG', 'OD1', 'ASP', 6.52), ('NH2', 'ARG', 'OD2', 'ASP', 7.4)]]}
MG_ASPI = { 
	'distances':
		[13.18, 11.66, 10.99, 11.26],
	'comparisons':
		[('MG', 'MG', 'CB', 'ASPI', 13.18), ('MG', 'MG', 'CG', 'ASPI', 11.66), ('MG', 'MG', 'OD1', 'ASPI', 10.99), ('MG', 'MG', 'OD2', 'ASPI', 11.26)]}
ASP_ARGII = { 
	'distances':
		[[7.82, 7.93, 8.17, 7.15, 7.69, 9.02, 7.17], [6.95, 6.82, 6.83, 5.7, 6.18, 7.5, 5.72], [5.72, 5.61, 5.78, 4.88, 5.7, 6.99, 5.66], [7.72, 7.41, 7.08, 5.74, 5.81, 7.07, 5.01], [6.16, 7.47, 7.76, 7.54, 8.32, 9.21, 8.57], [5.66, 6.74, 6.66, 6.36, 7.0, 7.8, 7.3], [6.34, 7.13, 6.79, 6.12, 6.49, 7.37, 6.52], [5.15, 6.21, 6.07, 6.12, 6.8, 7.38, 7.4]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARGII', 7.82), ('CB', 'ASP', 'CG', 'ARGII', 7.93), ('CB', 'ASP', 'CD', 'ARGII', 8.17), ('CB', 'ASP', 'NE', 'ARGII', 7.15), ('CB', 'ASP', 'CZ', 'ARGII', 7.69), ('CB', 'ASP', 'NH1', 'ARGII', 9.02), ('CB', 'ASP', 'NH2', 'ARGII', 7.17)], [('CG', 'ASP', 'CB', 'ARGII', 6.95), ('CG', 'ASP', 'CG', 'ARGII', 6.82), ('CG', 'ASP', 'CD', 'ARGII', 6.83), ('CG', 'ASP', 'NE', 'ARGII', 5.7), ('CG', 'ASP', 'CZ', 'ARGII', 6.18), ('CG', 'ASP', 'NH1', 'ARGII', 7.5), ('CG', 'ASP', 'NH2', 'ARGII', 5.72)], [('OD1', 'ASP', 'CB', 'ARGII', 5.72), ('OD1', 'ASP', 'CG', 'ARGII', 5.61), ('OD1', 'ASP', 'CD', 'ARGII', 5.78), ('OD1', 'ASP', 'NE', 'ARGII', 4.88), ('OD1', 'ASP', 'CZ', 'ARGII', 5.7), ('OD1', 'ASP', 'NH1', 'ARGII', 6.99), ('OD1', 'ASP', 'NH2', 'ARGII', 5.66)], [('OD2', 'ASP', 'CB', 'ARGII', 7.72), ('OD2', 'ASP', 'CG', 'ARGII', 7.41), ('OD2', 'ASP', 'CD', 'ARGII', 7.08), ('OD2', 'ASP', 'NE', 'ARGII', 5.74), ('OD2', 'ASP', 'CZ', 'ARGII', 5.81), ('OD2', 'ASP', 'NH1', 'ARGII', 7.07), ('OD2', 'ASP', 'NH2', 'ARGII', 5.01)], [('CB', 'ASP', 'CB', 'ARGII', 6.16), ('CB', 'ASP', 'CG', 'ARGII', 7.47), ('CB', 'ASP', 'CD', 'ARGII', 7.76), ('CB', 'ASP', 'NE', 'ARGII', 7.54), ('CB', 'ASP', 'CZ', 'ARGII', 8.32), ('CB', 'ASP', 'NH1', 'ARGII', 9.21), ('CB', 'ASP', 'NH2', 'ARGII', 8.57)], [('CG', 'ASP', 'CB', 'ARGII', 5.66), ('CG', 'ASP', 'CG', 'ARGII', 6.74), ('CG', 'ASP', 'CD', 'ARGII', 6.66), ('CG', 'ASP', 'NE', 'ARGII', 6.36), ('CG', 'ASP', 'CZ', 'ARGII', 7.0), ('CG', 'ASP', 'NH1', 'ARGII', 7.8), ('CG', 'ASP', 'NH2', 'ARGII', 7.3)], [('OD1', 'ASP', 'CB', 'ARGII', 6.34), ('OD1', 'ASP', 'CG', 'ARGII', 7.13), ('OD1', 'ASP', 'CD', 'ARGII', 6.79), ('OD1', 'ASP', 'NE', 'ARGII', 6.12), ('OD1', 'ASP', 'CZ', 'ARGII', 6.49), ('OD1', 'ASP', 'NH1', 'ARGII', 7.37), ('OD1', 'ASP', 'NH2', 'ARGII', 6.52)], [('OD2', 'ASP', 'CB', 'ARGII', 5.15), ('OD2', 'ASP', 'CG', 'ARGII', 6.21), ('OD2', 'ASP', 'CD', 'ARGII', 6.07), ('OD2', 'ASP', 'NE', 'ARGII', 6.12), ('OD2', 'ASP', 'CZ', 'ARGII', 6.8), ('OD2', 'ASP', 'NH1', 'ARGII', 7.38), ('OD2', 'ASP', 'NH2', 'ARGII', 7.4)]]}
MG_ARGI = { 
	'distances':
		[13.5, 13.4, 12.6, 11.17, 10.42, 11.11, 9.12],
	'comparisons':
		[('MG', 'MG', 'CB', 'ARGI', 13.5), ('MG', 'MG', 'CG', 'ARGI', 13.4), ('MG', 'MG', 'CD', 'ARGI', 12.6), ('MG', 'MG', 'NE', 'ARGI', 11.17), ('MG', 'MG', 'CZ', 'ARGI', 10.42), ('MG', 'MG', 'NH1', 'ARGI', 11.11), ('MG', 'MG', 'NH2', 'ARGI', 9.12)]}
ASP_ARGI = { 
	'distances':
		[[8.58, 7.23, 6.09, 6.53, 6.52, 6.03, 7.44], [8.89, 7.66, 6.39, 6.31, 6.0, 5.66, 6.61], [9.96, 8.8, 7.45, 7.25, 6.68, 6.15, 7.1], [8.33, 7.15, 5.98, 5.63, 5.43, 5.52, 5.87], [11.05, 10.48, 9.02, 8.91, 7.9, 6.63, 8.36], [10.75, 10.21, 8.72, 8.3, 7.13, 6.03, 7.32], [9.62, 9.13, 7.65, 7.12, 5.91, 4.87, 6.09], [11.79, 11.25, 9.75, 9.2, 7.97, 7.01, 7.94]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARGI', 8.58), ('CB', 'ASP', 'CG', 'ARGI', 7.23), ('CB', 'ASP', 'CD', 'ARGI', 6.09), ('CB', 'ASP', 'NE', 'ARGI', 6.53), ('CB', 'ASP', 'CZ', 'ARGI', 6.52), ('CB', 'ASP', 'NH1', 'ARGI', 6.03), ('CB', 'ASP', 'NH2', 'ARGI', 7.44)], [('CG', 'ASP', 'CB', 'ARGI', 8.89), ('CG', 'ASP', 'CG', 'ARGI', 7.66), ('CG', 'ASP', 'CD', 'ARGI', 6.39), ('CG', 'ASP', 'NE', 'ARGI', 6.31), ('CG', 'ASP', 'CZ', 'ARGI', 6.0), ('CG', 'ASP', 'NH1', 'ARGI', 5.66), ('CG', 'ASP', 'NH2', 'ARGI', 6.61)], [('OD1', 'ASP', 'CB', 'ARGI', 9.96), ('OD1', 'ASP', 'CG', 'ARGI', 8.8), ('OD1', 'ASP', 'CD', 'ARGI', 7.45), ('OD1', 'ASP', 'NE', 'ARGI', 7.25), ('OD1', 'ASP', 'CZ', 'ARGI', 6.68), ('OD1', 'ASP', 'NH1', 'ARGI', 6.15), ('OD1', 'ASP', 'NH2', 'ARGI', 7.1)], [('OD2', 'ASP', 'CB', 'ARGI', 8.33), ('OD2', 'ASP', 'CG', 'ARGI', 7.15), ('OD2', 'ASP', 'CD', 'ARGI', 5.98), ('OD2', 'ASP', 'NE', 'ARGI', 5.63), ('OD2', 'ASP', 'CZ', 'ARGI', 5.43), ('OD2', 'ASP', 'NH1', 'ARGI', 5.52), ('OD2', 'ASP', 'NH2', 'ARGI', 5.87)], [('CB', 'ASP', 'CB', 'ARGI', 11.05), ('CB', 'ASP', 'CG', 'ARGI', 10.48), ('CB', 'ASP', 'CD', 'ARGI', 9.02), ('CB', 'ASP', 'NE', 'ARGI', 8.91), ('CB', 'ASP', 'CZ', 'ARGI', 7.9), ('CB', 'ASP', 'NH1', 'ARGI', 6.63), ('CB', 'ASP', 'NH2', 'ARGI', 8.36)], [('CG', 'ASP', 'CB', 'ARGI', 10.75), ('CG', 'ASP', 'CG', 'ARGI', 10.21), ('CG', 'ASP', 'CD', 'ARGI', 8.72), ('CG', 'ASP', 'NE', 'ARGI', 8.3), ('CG', 'ASP', 'CZ', 'ARGI', 7.13), ('CG', 'ASP', 'NH1', 'ARGI', 6.03), ('CG', 'ASP', 'NH2', 'ARGI', 7.32)], [('OD1', 'ASP', 'CB', 'ARGI', 9.62), ('OD1', 'ASP', 'CG', 'ARGI', 9.13), ('OD1', 'ASP', 'CD', 'ARGI', 7.65), ('OD1', 'ASP', 'NE', 'ARGI', 7.12), ('OD1', 'ASP', 'CZ', 'ARGI', 5.91), ('OD1', 'ASP', 'NH1', 'ARGI', 4.87), ('OD1', 'ASP', 'NH2', 'ARGI', 6.09)], [('OD2', 'ASP', 'CB', 'ARGI', 11.79), ('OD2', 'ASP', 'CG', 'ARGI', 11.25), ('OD2', 'ASP', 'CD', 'ARGI', 9.75), ('OD2', 'ASP', 'NE', 'ARGI', 9.2), ('OD2', 'ASP', 'CZ', 'ARGI', 7.97), ('OD2', 'ASP', 'NH1', 'ARGI', 7.01), ('OD2', 'ASP', 'NH2', 'ARGI', 7.94)]]}
LYS_ARG = { 
	'distances':
		[[14.97, 14.57, 13.16, 12.97, 11.84, 10.66, 12.02], [15.46, 15.22, 13.84, 13.55, 12.38, 11.27, 12.44], [16.15, 15.91, 14.49, 14.04, 12.8, 11.79, 12.68], [15.26, 15.01, 13.58, 13.0, 11.71, 10.81, 11.47], [14.35, 14.25, 12.88, 12.26, 10.98, 10.13, 10.71], [15.18, 15.59, 15.19, 13.75, 13.25, 14.14, 11.96], [14.57, 15.12, 14.87, 13.48, 13.09, 14.05, 11.87], [13.93, 14.46, 14.34, 12.98, 12.75, 13.83, 11.58], [12.63, 13.07, 12.91, 11.54, 11.33, 12.43, 10.16], [11.58, 12.14, 11.96, 10.61, 10.37, 11.44, 9.23], [16.49, 15.96, 14.44, 13.79, 12.52, 11.7, 12.22], [17.06, 16.61, 15.11, 14.33, 13.05, 12.37, 12.57], [17.14, 16.62, 15.13, 14.24, 12.93, 12.35, 12.32], [15.81, 15.28, 13.81, 12.86, 11.54, 11.04, 10.86], [15.23, 14.85, 13.42, 12.41, 11.14, 10.77, 10.41]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 14.97), ('CB', 'LYS', 'CG', 'ARG', 14.57), ('CB', 'LYS', 'CD', 'ARG', 13.16), ('CB', 'LYS', 'NE', 'ARG', 12.97), ('CB', 'LYS', 'CZ', 'ARG', 11.84), ('CB', 'LYS', 'NH1', 'ARG', 10.66), ('CB', 'LYS', 'NH2', 'ARG', 12.02)], [('CG', 'LYS', 'CB', 'ARG', 15.46), ('CG', 'LYS', 'CG', 'ARG', 15.22), ('CG', 'LYS', 'CD', 'ARG', 13.84), ('CG', 'LYS', 'NE', 'ARG', 13.55), ('CG', 'LYS', 'CZ', 'ARG', 12.38), ('CG', 'LYS', 'NH1', 'ARG', 11.27), ('CG', 'LYS', 'NH2', 'ARG', 12.44)], [('CD', 'LYS', 'CB', 'ARG', 16.15), ('CD', 'LYS', 'CG', 'ARG', 15.91), ('CD', 'LYS', 'CD', 'ARG', 14.49), ('CD', 'LYS', 'NE', 'ARG', 14.04), ('CD', 'LYS', 'CZ', 'ARG', 12.8), ('CD', 'LYS', 'NH1', 'ARG', 11.79), ('CD', 'LYS', 'NH2', 'ARG', 12.68)], [('CE', 'LYS', 'CB', 'ARG', 15.26), ('CE', 'LYS', 'CG', 'ARG', 15.01), ('CE', 'LYS', 'CD', 'ARG', 13.58), ('CE', 'LYS', 'NE', 'ARG', 13.0), ('CE', 'LYS', 'CZ', 'ARG', 11.71), ('CE', 'LYS', 'NH1', 'ARG', 10.81), ('CE', 'LYS', 'NH2', 'ARG', 11.47)], [('NZ', 'LYS', 'CB', 'ARG', 14.35), ('NZ', 'LYS', 'CG', 'ARG', 14.25), ('NZ', 'LYS', 'CD', 'ARG', 12.88), ('NZ', 'LYS', 'NE', 'ARG', 12.26), ('NZ', 'LYS', 'CZ', 'ARG', 10.98), ('NZ', 'LYS', 'NH1', 'ARG', 10.13), ('NZ', 'LYS', 'NH2', 'ARG', 10.71)], [('CB', 'LYS', 'CB', 'ARG', 15.18), ('CB', 'LYS', 'CG', 'ARG', 15.59), ('CB', 'LYS', 'CD', 'ARG', 15.19), ('CB', 'LYS', 'NE', 'ARG', 13.75), ('CB', 'LYS', 'CZ', 'ARG', 13.25), ('CB', 'LYS', 'NH1', 'ARG', 14.14), ('CB', 'LYS', 'NH2', 'ARG', 11.96)], [('CG', 'LYS', 'CB', 'ARG', 14.57), ('CG', 'LYS', 'CG', 'ARG', 15.12), ('CG', 'LYS', 'CD', 'ARG', 14.87), ('CG', 'LYS', 'NE', 'ARG', 13.48), ('CG', 'LYS', 'CZ', 'ARG', 13.09), ('CG', 'LYS', 'NH1', 'ARG', 14.05), ('CG', 'LYS', 'NH2', 'ARG', 11.87)], [('CD', 'LYS', 'CB', 'ARG', 13.93), ('CD', 'LYS', 'CG', 'ARG', 14.46), ('CD', 'LYS', 'CD', 'ARG', 14.34), ('CD', 'LYS', 'NE', 'ARG', 12.98), ('CD', 'LYS', 'CZ', 'ARG', 12.75), ('CD', 'LYS', 'NH1', 'ARG', 13.83), ('CD', 'LYS', 'NH2', 'ARG', 11.58)], [('CE', 'LYS', 'CB', 'ARG', 12.63), ('CE', 'LYS', 'CG', 'ARG', 13.07), ('CE', 'LYS', 'CD', 'ARG', 12.91), ('CE', 'LYS', 'NE', 'ARG', 11.54), ('CE', 'LYS', 'CZ', 'ARG', 11.33), ('CE', 'LYS', 'NH1', 'ARG', 12.43), ('CE', 'LYS', 'NH2', 'ARG', 10.16)], [('NZ', 'LYS', 'CB', 'ARG', 11.58), ('NZ', 'LYS', 'CG', 'ARG', 12.14), ('NZ', 'LYS', 'CD', 'ARG', 11.96), ('NZ', 'LYS', 'NE', 'ARG', 10.61), ('NZ', 'LYS', 'CZ', 'ARG', 10.37), ('NZ', 'LYS', 'NH1', 'ARG', 11.44), ('NZ', 'LYS', 'NH2', 'ARG', 9.23)], [('CB', 'LYS', 'CB', 'ARG', 16.49), ('CB', 'LYS', 'CG', 'ARG', 15.96), ('CB', 'LYS', 'CD', 'ARG', 14.44), ('CB', 'LYS', 'NE', 'ARG', 13.79), ('CB', 'LYS', 'CZ', 'ARG', 12.52), ('CB', 'LYS', 'NH1', 'ARG', 11.7), ('CB', 'LYS', 'NH2', 'ARG', 12.22)], [('CG', 'LYS', 'CB', 'ARG', 17.06), ('CG', 'LYS', 'CG', 'ARG', 16.61), ('CG', 'LYS', 'CD', 'ARG', 15.11), ('CG', 'LYS', 'NE', 'ARG', 14.33), ('CG', 'LYS', 'CZ', 'ARG', 13.05), ('CG', 'LYS', 'NH1', 'ARG', 12.37), ('CG', 'LYS', 'NH2', 'ARG', 12.57)], [('CD', 'LYS', 'CB', 'ARG', 17.14), ('CD', 'LYS', 'CG', 'ARG', 16.62), ('CD', 'LYS', 'CD', 'ARG', 15.13), ('CD', 'LYS', 'NE', 'ARG', 14.24), ('CD', 'LYS', 'CZ', 'ARG', 12.93), ('CD', 'LYS', 'NH1', 'ARG', 12.35), ('CD', 'LYS', 'NH2', 'ARG', 12.32)], [('CE', 'LYS', 'CB', 'ARG', 15.81), ('CE', 'LYS', 'CG', 'ARG', 15.28), ('CE', 'LYS', 'CD', 'ARG', 13.81), ('CE', 'LYS', 'NE', 'ARG', 12.86), ('CE', 'LYS', 'CZ', 'ARG', 11.54), ('CE', 'LYS', 'NH1', 'ARG', 11.04), ('CE', 'LYS', 'NH2', 'ARG', 10.86)], [('NZ', 'LYS', 'CB', 'ARG', 15.23), ('NZ', 'LYS', 'CG', 'ARG', 14.85), ('NZ', 'LYS', 'CD', 'ARG', 13.42), ('NZ', 'LYS', 'NE', 'ARG', 12.41), ('NZ', 'LYS', 'CZ', 'ARG', 11.14), ('NZ', 'LYS', 'NH1', 'ARG', 10.77), ('NZ', 'LYS', 'NH2', 'ARG', 10.41)]]}
LYS_MG = { 
	'distances':
		[[6.91], [7.89], [8.08], [7.16], [7.41]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 6.91)], [('CG', 'LYS', 'MG', 'MG', 7.89)], [('CD', 'LYS', 'MG', 'MG', 8.08)], [('CE', 'LYS', 'MG', 'MG', 7.16)], [('NZ', 'LYS', 'MG', 'MG', 7.41)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'M_1zio_2_7_4_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_MG, d, 'M_1zio_2_7_4_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(MG_ARGII, d, 'M_1zio_2_7_4_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ASP, d, 'M_1zio_2_7_4_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_ARGI, d, 'M_1zio_2_7_4_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_ARG, d, 'M_1zio_2_7_4_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ARG_MG, d, 'M_1zio_2_7_4_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ARG_ASP, d, 'M_1zio_2_7_4_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(MG_ASPI, d, 'M_1zio_2_7_4_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASP_ARGII, d, 'M_1zio_2_7_4_3')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(MG_ARGI, d, 'M_1zio_2_7_4_3')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(ASP_ARGI, d, 'M_1zio_2_7_4_3')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(LYS_ARG, d, 'M_1zio_2_7_4_3')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(LYS_MG, d, 'M_1zio_2_7_4_3')
	if match14 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'ASP_MG' :  match2,
		'MG_ARGII' :  match3,
		'ASP_ASP' :  match4,
		'ARG_ARGI' :  match5,
		'ARG_ARG' :  match6,
		'ARG_MG' :  match7,
		'ARG_ASP' :  match8,
		'MG_ASPI' :  match9,
		'ASP_ARGII' :  match10,
		'MG_ARGI' :  match11,
		'ASP_ARGI' :  match12,
		'LYS_ARG' :  match13,
		'LYS_MG' :  match14}