'''
FUNC:P_1pfk_2_7_1_11
PDB:1pfk
EC:2.7.1.11
RESI:gly,arg,thr,asp,arg
LOCI:a-11,72,125,127,171;
'''
import motifFunctions as cmd
THR_ASP = { 
	'distances':
		[[6.75, 7.15, 7.94, 7.09, 8.59, 7.44, 6.9, 6.05], [5.57, 5.75, 6.5, 5.72, 7.84, 6.75, 5.88, 5.1], [6.72, 7.52, 8.44, 7.55, 7.99, 6.9, 6.79, 6.25], [7.37, 8.12, 8.54, 8.66, 7.98, 6.74, 6.57, 5.44], [7.11, 7.57, 7.94, 8.0, 8.32, 7.06, 6.51, 5.21], [7.64, 7.97, 8.5, 8.08, 9.26, 8.02, 7.43, 6.25], [8.94, 9.37, 9.94, 9.46, 10.28, 9.04, 8.66, 7.51]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 6.75), ('CB', 'THR', 'CG', 'ASP', 7.15), ('CB', 'THR', 'OD1', 'ASP', 7.94), ('CB', 'THR', 'OD2', 'ASP', 7.09), ('CB', 'THR', 'O', 'ASP', 8.59), ('CB', 'THR', 'C', 'ASP', 7.44), ('CB', 'THR', 'CA', 'ASP', 6.9), ('CB', 'THR', 'N', 'ASP', 6.05)], [('OG1', 'THR', 'CB', 'ASP', 5.57), ('OG1', 'THR', 'CG', 'ASP', 5.75), ('OG1', 'THR', 'OD1', 'ASP', 6.5), ('OG1', 'THR', 'OD2', 'ASP', 5.72), ('OG1', 'THR', 'O', 'ASP', 7.84), ('OG1', 'THR', 'C', 'ASP', 6.75), ('OG1', 'THR', 'CA', 'ASP', 5.88), ('OG1', 'THR', 'N', 'ASP', 5.1)], [('CG2', 'THR', 'CB', 'ASP', 6.72), ('CG2', 'THR', 'CG', 'ASP', 7.52), ('CG2', 'THR', 'OD1', 'ASP', 8.44), ('CG2', 'THR', 'OD2', 'ASP', 7.55), ('CG2', 'THR', 'O', 'ASP', 7.99), ('CG2', 'THR', 'C', 'ASP', 6.9), ('CG2', 'THR', 'CA', 'ASP', 6.79), ('CG2', 'THR', 'N', 'ASP', 6.25)], [('O', 'THR', 'CB', 'ASP', 7.37), ('O', 'THR', 'CG', 'ASP', 8.12), ('O', 'THR', 'OD1', 'ASP', 8.54), ('O', 'THR', 'OD2', 'ASP', 8.66), ('O', 'THR', 'O', 'ASP', 7.98), ('O', 'THR', 'C', 'ASP', 6.74), ('O', 'THR', 'CA', 'ASP', 6.57), ('O', 'THR', 'N', 'ASP', 5.44)], [('C', 'THR', 'CB', 'ASP', 7.11), ('C', 'THR', 'CG', 'ASP', 7.57), ('C', 'THR', 'OD1', 'ASP', 7.94), ('C', 'THR', 'OD2', 'ASP', 8.0), ('C', 'THR', 'O', 'ASP', 8.32), ('C', 'THR', 'C', 'ASP', 7.06), ('C', 'THR', 'CA', 'ASP', 6.51), ('C', 'THR', 'N', 'ASP', 5.21)], [('CA', 'THR', 'CB', 'ASP', 7.64), ('CA', 'THR', 'CG', 'ASP', 7.97), ('CA', 'THR', 'OD1', 'ASP', 8.5), ('CA', 'THR', 'OD2', 'ASP', 8.08), ('CA', 'THR', 'O', 'ASP', 9.26), ('CA', 'THR', 'C', 'ASP', 8.02), ('CA', 'THR', 'CA', 'ASP', 7.43), ('CA', 'THR', 'N', 'ASP', 6.25)], [('N', 'THR', 'CB', 'ASP', 8.94), ('N', 'THR', 'CG', 'ASP', 9.37), ('N', 'THR', 'OD1', 'ASP', 9.94), ('N', 'THR', 'OD2', 'ASP', 9.46), ('N', 'THR', 'O', 'ASP', 10.28), ('N', 'THR', 'C', 'ASP', 9.04), ('N', 'THR', 'CA', 'ASP', 8.66), ('N', 'THR', 'N', 'ASP', 7.51)]]}
ARG_ARG = { 
	'distances':
		[[16.85, 16.22, 14.84, 13.84, 12.56, 12.06, 11.85, 20.22, 19.3, 18.24, 18.79], [15.54, 14.89, 13.48, 12.56, 11.28, 10.69, 10.68, 18.96, 18.01, 16.97, 17.5], [14.39, 13.73, 12.37, 11.35, 10.08, 9.64, 9.38, 17.73, 16.82, 15.79, 16.39], [13.58, 13.07, 11.71, 10.66, 9.35, 8.9, 8.63, 16.97, 16.07, 14.94, 15.45], [12.59, 12.14, 10.75, 9.79, 8.46, 7.85, 7.91, 16.08, 15.14, 13.98, 14.41], [12.24, 11.7, 10.24, 9.45, 8.15, 7.35, 7.83, 15.79, 14.77, 13.69, 14.12], [12.13, 11.86, 10.52, 9.54, 8.22, 7.64, 7.66, 15.62, 14.71, 13.46, 13.78], [20.14, 19.5, 18.12, 17.13, 15.85, 15.35, 15.12, 23.5, 22.59, 21.53, 22.07], [19.29, 18.61, 17.21, 16.28, 15.01, 14.45, 14.35, 22.68, 21.74, 20.71, 21.26], [18.0, 17.39, 15.97, 15.05, 13.76, 13.15, 13.14, 21.45, 20.49, 19.42, 19.91], [18.45, 17.95, 16.52, 15.61, 14.29, 13.63, 13.7, 21.95, 20.99, 19.85, 20.23], [16.85, 15.54, 14.39, 13.58, 12.59, 12.24, 12.13, 20.14, 19.29, 18.0, 18.45], [16.22, 14.89, 13.73, 13.07, 12.14, 11.7, 11.86, 19.5, 18.61, 17.39, 17.95], [14.84, 13.48, 12.37, 11.71, 10.75, 10.24, 10.52, 18.12, 17.21, 15.97, 16.52], [13.84, 12.56, 11.35, 10.66, 9.79, 9.45, 9.54, 17.13, 16.28, 15.05, 15.61], [12.56, 11.28, 10.08, 9.35, 8.46, 8.15, 8.22, 15.85, 15.01, 13.76, 14.29], [12.06, 10.69, 9.64, 8.9, 7.85, 7.35, 7.64, 15.35, 14.45, 13.15, 13.63], [11.85, 10.68, 9.38, 8.63, 7.91, 7.83, 7.66, 15.12, 14.35, 13.14, 13.7], [20.22, 18.96, 17.73, 16.97, 16.08, 15.79, 15.62, 23.5, 22.68, 21.45, 21.95], [19.3, 18.01, 16.82, 16.07, 15.14, 14.77, 14.71, 22.59, 21.74, 20.49, 20.99], [18.24, 16.97, 15.79, 14.94, 13.98, 13.69, 13.46, 21.53, 20.71, 19.42, 19.85], [18.79, 17.5, 16.39, 15.45, 14.41, 14.12, 13.78, 22.07, 21.26, 19.91, 20.23]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 16.85), ('CB', 'ARG', 'CG', 'ARG', 16.22), ('CB', 'ARG', 'CD', 'ARG', 14.84), ('CB', 'ARG', 'NE', 'ARG', 13.84), ('CB', 'ARG', 'CZ', 'ARG', 12.56), ('CB', 'ARG', 'NH1', 'ARG', 12.06), ('CB', 'ARG', 'NH2', 'ARG', 11.85), ('CB', 'ARG', 'O', 'ARG', 20.22), ('CB', 'ARG', 'C', 'ARG', 19.3), ('CB', 'ARG', 'CA', 'ARG', 18.24), ('CB', 'ARG', 'N', 'ARG', 18.79)], [('CG', 'ARG', 'CB', 'ARG', 15.54), ('CG', 'ARG', 'CG', 'ARG', 14.89), ('CG', 'ARG', 'CD', 'ARG', 13.48), ('CG', 'ARG', 'NE', 'ARG', 12.56), ('CG', 'ARG', 'CZ', 'ARG', 11.28), ('CG', 'ARG', 'NH1', 'ARG', 10.69), ('CG', 'ARG', 'NH2', 'ARG', 10.68), ('CG', 'ARG', 'O', 'ARG', 18.96), ('CG', 'ARG', 'C', 'ARG', 18.01), ('CG', 'ARG', 'CA', 'ARG', 16.97), ('CG', 'ARG', 'N', 'ARG', 17.5)], [('CD', 'ARG', 'CB', 'ARG', 14.39), ('CD', 'ARG', 'CG', 'ARG', 13.73), ('CD', 'ARG', 'CD', 'ARG', 12.37), ('CD', 'ARG', 'NE', 'ARG', 11.35), ('CD', 'ARG', 'CZ', 'ARG', 10.08), ('CD', 'ARG', 'NH1', 'ARG', 9.64), ('CD', 'ARG', 'NH2', 'ARG', 9.38), ('CD', 'ARG', 'O', 'ARG', 17.73), ('CD', 'ARG', 'C', 'ARG', 16.82), ('CD', 'ARG', 'CA', 'ARG', 15.79), ('CD', 'ARG', 'N', 'ARG', 16.39)], [('NE', 'ARG', 'CB', 'ARG', 13.58), ('NE', 'ARG', 'CG', 'ARG', 13.07), ('NE', 'ARG', 'CD', 'ARG', 11.71), ('NE', 'ARG', 'NE', 'ARG', 10.66), ('NE', 'ARG', 'CZ', 'ARG', 9.35), ('NE', 'ARG', 'NH1', 'ARG', 8.9), ('NE', 'ARG', 'NH2', 'ARG', 8.63), ('NE', 'ARG', 'O', 'ARG', 16.97), ('NE', 'ARG', 'C', 'ARG', 16.07), ('NE', 'ARG', 'CA', 'ARG', 14.94), ('NE', 'ARG', 'N', 'ARG', 15.45)], [('CZ', 'ARG', 'CB', 'ARG', 12.59), ('CZ', 'ARG', 'CG', 'ARG', 12.14), ('CZ', 'ARG', 'CD', 'ARG', 10.75), ('CZ', 'ARG', 'NE', 'ARG', 9.79), ('CZ', 'ARG', 'CZ', 'ARG', 8.46), ('CZ', 'ARG', 'NH1', 'ARG', 7.85), ('CZ', 'ARG', 'NH2', 'ARG', 7.91), ('CZ', 'ARG', 'O', 'ARG', 16.08), ('CZ', 'ARG', 'C', 'ARG', 15.14), ('CZ', 'ARG', 'CA', 'ARG', 13.98), ('CZ', 'ARG', 'N', 'ARG', 14.41)], [('NH1', 'ARG', 'CB', 'ARG', 12.24), ('NH1', 'ARG', 'CG', 'ARG', 11.7), ('NH1', 'ARG', 'CD', 'ARG', 10.24), ('NH1', 'ARG', 'NE', 'ARG', 9.45), ('NH1', 'ARG', 'CZ', 'ARG', 8.15), ('NH1', 'ARG', 'NH1', 'ARG', 7.35), ('NH1', 'ARG', 'NH2', 'ARG', 7.83), ('NH1', 'ARG', 'O', 'ARG', 15.79), ('NH1', 'ARG', 'C', 'ARG', 14.77), ('NH1', 'ARG', 'CA', 'ARG', 13.69), ('NH1', 'ARG', 'N', 'ARG', 14.12)], [('NH2', 'ARG', 'CB', 'ARG', 12.13), ('NH2', 'ARG', 'CG', 'ARG', 11.86), ('NH2', 'ARG', 'CD', 'ARG', 10.52), ('NH2', 'ARG', 'NE', 'ARG', 9.54), ('NH2', 'ARG', 'CZ', 'ARG', 8.22), ('NH2', 'ARG', 'NH1', 'ARG', 7.64), ('NH2', 'ARG', 'NH2', 'ARG', 7.66), ('NH2', 'ARG', 'O', 'ARG', 15.62), ('NH2', 'ARG', 'C', 'ARG', 14.71), ('NH2', 'ARG', 'CA', 'ARG', 13.46), ('NH2', 'ARG', 'N', 'ARG', 13.78)], [('O', 'ARG', 'CB', 'ARG', 20.14), ('O', 'ARG', 'CG', 'ARG', 19.5), ('O', 'ARG', 'CD', 'ARG', 18.12), ('O', 'ARG', 'NE', 'ARG', 17.13), ('O', 'ARG', 'CZ', 'ARG', 15.85), ('O', 'ARG', 'NH1', 'ARG', 15.35), ('O', 'ARG', 'NH2', 'ARG', 15.12), ('O', 'ARG', 'O', 'ARG', 23.5), ('O', 'ARG', 'C', 'ARG', 22.59), ('O', 'ARG', 'CA', 'ARG', 21.53), ('O', 'ARG', 'N', 'ARG', 22.07)], [('C', 'ARG', 'CB', 'ARG', 19.29), ('C', 'ARG', 'CG', 'ARG', 18.61), ('C', 'ARG', 'CD', 'ARG', 17.21), ('C', 'ARG', 'NE', 'ARG', 16.28), ('C', 'ARG', 'CZ', 'ARG', 15.01), ('C', 'ARG', 'NH1', 'ARG', 14.45), ('C', 'ARG', 'NH2', 'ARG', 14.35), ('C', 'ARG', 'O', 'ARG', 22.68), ('C', 'ARG', 'C', 'ARG', 21.74), ('C', 'ARG', 'CA', 'ARG', 20.71), ('C', 'ARG', 'N', 'ARG', 21.26)], [('CA', 'ARG', 'CB', 'ARG', 18.0), ('CA', 'ARG', 'CG', 'ARG', 17.39), ('CA', 'ARG', 'CD', 'ARG', 15.97), ('CA', 'ARG', 'NE', 'ARG', 15.05), ('CA', 'ARG', 'CZ', 'ARG', 13.76), ('CA', 'ARG', 'NH1', 'ARG', 13.15), ('CA', 'ARG', 'NH2', 'ARG', 13.14), ('CA', 'ARG', 'O', 'ARG', 21.45), ('CA', 'ARG', 'C', 'ARG', 20.49), ('CA', 'ARG', 'CA', 'ARG', 19.42), ('CA', 'ARG', 'N', 'ARG', 19.91)], [('N', 'ARG', 'CB', 'ARG', 18.45), ('N', 'ARG', 'CG', 'ARG', 17.95), ('N', 'ARG', 'CD', 'ARG', 16.52), ('N', 'ARG', 'NE', 'ARG', 15.61), ('N', 'ARG', 'CZ', 'ARG', 14.29), ('N', 'ARG', 'NH1', 'ARG', 13.63), ('N', 'ARG', 'NH2', 'ARG', 13.7), ('N', 'ARG', 'O', 'ARG', 21.95), ('N', 'ARG', 'C', 'ARG', 20.99), ('N', 'ARG', 'CA', 'ARG', 19.85), ('N', 'ARG', 'N', 'ARG', 20.23)], [('CB', 'ARG', 'CB', 'ARG', 16.85), ('CB', 'ARG', 'CG', 'ARG', 15.54), ('CB', 'ARG', 'CD', 'ARG', 14.39), ('CB', 'ARG', 'NE', 'ARG', 13.58), ('CB', 'ARG', 'CZ', 'ARG', 12.59), ('CB', 'ARG', 'NH1', 'ARG', 12.24), ('CB', 'ARG', 'NH2', 'ARG', 12.13), ('CB', 'ARG', 'O', 'ARG', 20.14), ('CB', 'ARG', 'C', 'ARG', 19.29), ('CB', 'ARG', 'CA', 'ARG', 18.0), ('CB', 'ARG', 'N', 'ARG', 18.45)], [('CG', 'ARG', 'CB', 'ARG', 16.22), ('CG', 'ARG', 'CG', 'ARG', 14.89), ('CG', 'ARG', 'CD', 'ARG', 13.73), ('CG', 'ARG', 'NE', 'ARG', 13.07), ('CG', 'ARG', 'CZ', 'ARG', 12.14), ('CG', 'ARG', 'NH1', 'ARG', 11.7), ('CG', 'ARG', 'NH2', 'ARG', 11.86), ('CG', 'ARG', 'O', 'ARG', 19.5), ('CG', 'ARG', 'C', 'ARG', 18.61), ('CG', 'ARG', 'CA', 'ARG', 17.39), ('CG', 'ARG', 'N', 'ARG', 17.95)], [('CD', 'ARG', 'CB', 'ARG', 14.84), ('CD', 'ARG', 'CG', 'ARG', 13.48), ('CD', 'ARG', 'CD', 'ARG', 12.37), ('CD', 'ARG', 'NE', 'ARG', 11.71), ('CD', 'ARG', 'CZ', 'ARG', 10.75), ('CD', 'ARG', 'NH1', 'ARG', 10.24), ('CD', 'ARG', 'NH2', 'ARG', 10.52), ('CD', 'ARG', 'O', 'ARG', 18.12), ('CD', 'ARG', 'C', 'ARG', 17.21), ('CD', 'ARG', 'CA', 'ARG', 15.97), ('CD', 'ARG', 'N', 'ARG', 16.52)], [('NE', 'ARG', 'CB', 'ARG', 13.84), ('NE', 'ARG', 'CG', 'ARG', 12.56), ('NE', 'ARG', 'CD', 'ARG', 11.35), ('NE', 'ARG', 'NE', 'ARG', 10.66), ('NE', 'ARG', 'CZ', 'ARG', 9.79), ('NE', 'ARG', 'NH1', 'ARG', 9.45), ('NE', 'ARG', 'NH2', 'ARG', 9.54), ('NE', 'ARG', 'O', 'ARG', 17.13), ('NE', 'ARG', 'C', 'ARG', 16.28), ('NE', 'ARG', 'CA', 'ARG', 15.05), ('NE', 'ARG', 'N', 'ARG', 15.61)], [('CZ', 'ARG', 'CB', 'ARG', 12.56), ('CZ', 'ARG', 'CG', 'ARG', 11.28), ('CZ', 'ARG', 'CD', 'ARG', 10.08), ('CZ', 'ARG', 'NE', 'ARG', 9.35), ('CZ', 'ARG', 'CZ', 'ARG', 8.46), ('CZ', 'ARG', 'NH1', 'ARG', 8.15), ('CZ', 'ARG', 'NH2', 'ARG', 8.22), ('CZ', 'ARG', 'O', 'ARG', 15.85), ('CZ', 'ARG', 'C', 'ARG', 15.01), ('CZ', 'ARG', 'CA', 'ARG', 13.76), ('CZ', 'ARG', 'N', 'ARG', 14.29)], [('NH1', 'ARG', 'CB', 'ARG', 12.06), ('NH1', 'ARG', 'CG', 'ARG', 10.69), ('NH1', 'ARG', 'CD', 'ARG', 9.64), ('NH1', 'ARG', 'NE', 'ARG', 8.9), ('NH1', 'ARG', 'CZ', 'ARG', 7.85), ('NH1', 'ARG', 'NH1', 'ARG', 7.35), ('NH1', 'ARG', 'NH2', 'ARG', 7.64), ('NH1', 'ARG', 'O', 'ARG', 15.35), ('NH1', 'ARG', 'C', 'ARG', 14.45), ('NH1', 'ARG', 'CA', 'ARG', 13.15), ('NH1', 'ARG', 'N', 'ARG', 13.63)], [('NH2', 'ARG', 'CB', 'ARG', 11.85), ('NH2', 'ARG', 'CG', 'ARG', 10.68), ('NH2', 'ARG', 'CD', 'ARG', 9.38), ('NH2', 'ARG', 'NE', 'ARG', 8.63), ('NH2', 'ARG', 'CZ', 'ARG', 7.91), ('NH2', 'ARG', 'NH1', 'ARG', 7.83), ('NH2', 'ARG', 'NH2', 'ARG', 7.66), ('NH2', 'ARG', 'O', 'ARG', 15.12), ('NH2', 'ARG', 'C', 'ARG', 14.35), ('NH2', 'ARG', 'CA', 'ARG', 13.14), ('NH2', 'ARG', 'N', 'ARG', 13.7)], [('O', 'ARG', 'CB', 'ARG', 20.22), ('O', 'ARG', 'CG', 'ARG', 18.96), ('O', 'ARG', 'CD', 'ARG', 17.73), ('O', 'ARG', 'NE', 'ARG', 16.97), ('O', 'ARG', 'CZ', 'ARG', 16.08), ('O', 'ARG', 'NH1', 'ARG', 15.79), ('O', 'ARG', 'NH2', 'ARG', 15.62), ('O', 'ARG', 'O', 'ARG', 23.5), ('O', 'ARG', 'C', 'ARG', 22.68), ('O', 'ARG', 'CA', 'ARG', 21.45), ('O', 'ARG', 'N', 'ARG', 21.95)], [('C', 'ARG', 'CB', 'ARG', 19.3), ('C', 'ARG', 'CG', 'ARG', 18.01), ('C', 'ARG', 'CD', 'ARG', 16.82), ('C', 'ARG', 'NE', 'ARG', 16.07), ('C', 'ARG', 'CZ', 'ARG', 15.14), ('C', 'ARG', 'NH1', 'ARG', 14.77), ('C', 'ARG', 'NH2', 'ARG', 14.71), ('C', 'ARG', 'O', 'ARG', 22.59), ('C', 'ARG', 'C', 'ARG', 21.74), ('C', 'ARG', 'CA', 'ARG', 20.49), ('C', 'ARG', 'N', 'ARG', 20.99)], [('CA', 'ARG', 'CB', 'ARG', 18.24), ('CA', 'ARG', 'CG', 'ARG', 16.97), ('CA', 'ARG', 'CD', 'ARG', 15.79), ('CA', 'ARG', 'NE', 'ARG', 14.94), ('CA', 'ARG', 'CZ', 'ARG', 13.98), ('CA', 'ARG', 'NH1', 'ARG', 13.69), ('CA', 'ARG', 'NH2', 'ARG', 13.46), ('CA', 'ARG', 'O', 'ARG', 21.53), ('CA', 'ARG', 'C', 'ARG', 20.71), ('CA', 'ARG', 'CA', 'ARG', 19.42), ('CA', 'ARG', 'N', 'ARG', 19.85)], [('N', 'ARG', 'CB', 'ARG', 18.79), ('N', 'ARG', 'CG', 'ARG', 17.5), ('N', 'ARG', 'CD', 'ARG', 16.39), ('N', 'ARG', 'NE', 'ARG', 15.45), ('N', 'ARG', 'CZ', 'ARG', 14.41), ('N', 'ARG', 'NH1', 'ARG', 14.12), ('N', 'ARG', 'NH2', 'ARG', 13.78), ('N', 'ARG', 'O', 'ARG', 22.07), ('N', 'ARG', 'C', 'ARG', 21.26), ('N', 'ARG', 'CA', 'ARG', 19.91), ('N', 'ARG', 'N', 'ARG', 20.23)]]}
ARG_ASP = { 
	'distances':
		[[17.8, 16.88, 17.31, 15.75, 20.74, 20.0, 18.91, 18.44], [16.34, 15.47, 15.95, 14.32, 19.26, 18.54, 17.47, 17.03], [15.66, 14.71, 15.15, 13.54, 18.61, 17.96, 16.86, 16.51], [14.84, 13.8, 14.14, 12.67, 17.83, 17.17, 15.99, 15.6], [13.56, 12.53, 12.88, 11.42, 16.56, 15.87, 14.68, 14.27], [12.84, 11.93, 12.42, 10.79, 15.79, 15.08, 13.98, 13.6], [13.13, 12.0, 12.22, 10.96, 16.15, 15.45, 14.18, 13.72], [20.93, 20.06, 20.49, 18.94, 23.85, 23.06, 21.99, 21.43], [19.95, 19.13, 19.61, 18.0, 22.84, 22.05, 21.03, 20.5], [18.55, 17.7, 18.16, 16.6, 21.45, 20.65, 19.6, 19.04], [18.76, 17.89, 18.28, 16.85, 21.68, 20.83, 19.72, 19.06], [7.6, 6.65, 6.68, 6.26, 9.44, 9.69, 8.81, 9.65], [8.08, 7.28, 7.62, 6.62, 9.98, 10.21, 9.45, 10.31], [7.82, 6.94, 7.43, 5.99, 10.14, 10.16, 9.29, 9.95], [8.97, 7.91, 8.25, 6.89, 11.45, 11.39, 10.4, 10.9], [9.33, 8.21, 8.56, 7.08, 12.04, 11.82, 10.74, 11.04], [8.74, 7.67, 8.16, 6.46, 11.58, 11.22, 10.12, 10.28], [10.61, 9.42, 9.67, 8.32, 13.34, 13.11, 11.98, 12.22], [9.94, 9.4, 9.23, 9.44, 10.58, 11.3, 10.8, 11.95], [8.82, 8.28, 8.22, 8.25, 9.67, 10.31, 9.78, 10.92], [8.22, 7.39, 7.2, 7.31, 9.57, 10.01, 9.22, 10.19], [7.56, 6.73, 6.28, 6.97, 8.74, 9.17, 8.32, 9.25]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 17.8), ('CB', 'ARG', 'CG', 'ASP', 16.88), ('CB', 'ARG', 'OD1', 'ASP', 17.31), ('CB', 'ARG', 'OD2', 'ASP', 15.75), ('CB', 'ARG', 'O', 'ASP', 20.74), ('CB', 'ARG', 'C', 'ASP', 20.0), ('CB', 'ARG', 'CA', 'ASP', 18.91), ('CB', 'ARG', 'N', 'ASP', 18.44)], [('CG', 'ARG', 'CB', 'ASP', 16.34), ('CG', 'ARG', 'CG', 'ASP', 15.47), ('CG', 'ARG', 'OD1', 'ASP', 15.95), ('CG', 'ARG', 'OD2', 'ASP', 14.32), ('CG', 'ARG', 'O', 'ASP', 19.26), ('CG', 'ARG', 'C', 'ASP', 18.54), ('CG', 'ARG', 'CA', 'ASP', 17.47), ('CG', 'ARG', 'N', 'ASP', 17.03)], [('CD', 'ARG', 'CB', 'ASP', 15.66), ('CD', 'ARG', 'CG', 'ASP', 14.71), ('CD', 'ARG', 'OD1', 'ASP', 15.15), ('CD', 'ARG', 'OD2', 'ASP', 13.54), ('CD', 'ARG', 'O', 'ASP', 18.61), ('CD', 'ARG', 'C', 'ASP', 17.96), ('CD', 'ARG', 'CA', 'ASP', 16.86), ('CD', 'ARG', 'N', 'ASP', 16.51)], [('NE', 'ARG', 'CB', 'ASP', 14.84), ('NE', 'ARG', 'CG', 'ASP', 13.8), ('NE', 'ARG', 'OD1', 'ASP', 14.14), ('NE', 'ARG', 'OD2', 'ASP', 12.67), ('NE', 'ARG', 'O', 'ASP', 17.83), ('NE', 'ARG', 'C', 'ASP', 17.17), ('NE', 'ARG', 'CA', 'ASP', 15.99), ('NE', 'ARG', 'N', 'ASP', 15.6)], [('CZ', 'ARG', 'CB', 'ASP', 13.56), ('CZ', 'ARG', 'CG', 'ASP', 12.53), ('CZ', 'ARG', 'OD1', 'ASP', 12.88), ('CZ', 'ARG', 'OD2', 'ASP', 11.42), ('CZ', 'ARG', 'O', 'ASP', 16.56), ('CZ', 'ARG', 'C', 'ASP', 15.87), ('CZ', 'ARG', 'CA', 'ASP', 14.68), ('CZ', 'ARG', 'N', 'ASP', 14.27)], [('NH1', 'ARG', 'CB', 'ASP', 12.84), ('NH1', 'ARG', 'CG', 'ASP', 11.93), ('NH1', 'ARG', 'OD1', 'ASP', 12.42), ('NH1', 'ARG', 'OD2', 'ASP', 10.79), ('NH1', 'ARG', 'O', 'ASP', 15.79), ('NH1', 'ARG', 'C', 'ASP', 15.08), ('NH1', 'ARG', 'CA', 'ASP', 13.98), ('NH1', 'ARG', 'N', 'ASP', 13.6)], [('NH2', 'ARG', 'CB', 'ASP', 13.13), ('NH2', 'ARG', 'CG', 'ASP', 12.0), ('NH2', 'ARG', 'OD1', 'ASP', 12.22), ('NH2', 'ARG', 'OD2', 'ASP', 10.96), ('NH2', 'ARG', 'O', 'ASP', 16.15), ('NH2', 'ARG', 'C', 'ASP', 15.45), ('NH2', 'ARG', 'CA', 'ASP', 14.18), ('NH2', 'ARG', 'N', 'ASP', 13.72)], [('O', 'ARG', 'CB', 'ASP', 20.93), ('O', 'ARG', 'CG', 'ASP', 20.06), ('O', 'ARG', 'OD1', 'ASP', 20.49), ('O', 'ARG', 'OD2', 'ASP', 18.94), ('O', 'ARG', 'O', 'ASP', 23.85), ('O', 'ARG', 'C', 'ASP', 23.06), ('O', 'ARG', 'CA', 'ASP', 21.99), ('O', 'ARG', 'N', 'ASP', 21.43)], [('C', 'ARG', 'CB', 'ASP', 19.95), ('C', 'ARG', 'CG', 'ASP', 19.13), ('C', 'ARG', 'OD1', 'ASP', 19.61), ('C', 'ARG', 'OD2', 'ASP', 18.0), ('C', 'ARG', 'O', 'ASP', 22.84), ('C', 'ARG', 'C', 'ASP', 22.05), ('C', 'ARG', 'CA', 'ASP', 21.03), ('C', 'ARG', 'N', 'ASP', 20.5)], [('CA', 'ARG', 'CB', 'ASP', 18.55), ('CA', 'ARG', 'CG', 'ASP', 17.7), ('CA', 'ARG', 'OD1', 'ASP', 18.16), ('CA', 'ARG', 'OD2', 'ASP', 16.6), ('CA', 'ARG', 'O', 'ASP', 21.45), ('CA', 'ARG', 'C', 'ASP', 20.65), ('CA', 'ARG', 'CA', 'ASP', 19.6), ('CA', 'ARG', 'N', 'ASP', 19.04)], [('N', 'ARG', 'CB', 'ASP', 18.76), ('N', 'ARG', 'CG', 'ASP', 17.89), ('N', 'ARG', 'OD1', 'ASP', 18.28), ('N', 'ARG', 'OD2', 'ASP', 16.85), ('N', 'ARG', 'O', 'ASP', 21.68), ('N', 'ARG', 'C', 'ASP', 20.83), ('N', 'ARG', 'CA', 'ASP', 19.72), ('N', 'ARG', 'N', 'ASP', 19.06)], [('CB', 'ARG', 'CB', 'ASP', 7.6), ('CB', 'ARG', 'CG', 'ASP', 6.65), ('CB', 'ARG', 'OD1', 'ASP', 6.68), ('CB', 'ARG', 'OD2', 'ASP', 6.26), ('CB', 'ARG', 'O', 'ASP', 9.44), ('CB', 'ARG', 'C', 'ASP', 9.69), ('CB', 'ARG', 'CA', 'ASP', 8.81), ('CB', 'ARG', 'N', 'ASP', 9.65)], [('CG', 'ARG', 'CB', 'ASP', 8.08), ('CG', 'ARG', 'CG', 'ASP', 7.28), ('CG', 'ARG', 'OD1', 'ASP', 7.62), ('CG', 'ARG', 'OD2', 'ASP', 6.62), ('CG', 'ARG', 'O', 'ASP', 9.98), ('CG', 'ARG', 'C', 'ASP', 10.21), ('CG', 'ARG', 'CA', 'ASP', 9.45), ('CG', 'ARG', 'N', 'ASP', 10.31)], [('CD', 'ARG', 'CB', 'ASP', 7.82), ('CD', 'ARG', 'CG', 'ASP', 6.94), ('CD', 'ARG', 'OD1', 'ASP', 7.43), ('CD', 'ARG', 'OD2', 'ASP', 5.99), ('CD', 'ARG', 'O', 'ASP', 10.14), ('CD', 'ARG', 'C', 'ASP', 10.16), ('CD', 'ARG', 'CA', 'ASP', 9.29), ('CD', 'ARG', 'N', 'ASP', 9.95)], [('NE', 'ARG', 'CB', 'ASP', 8.97), ('NE', 'ARG', 'CG', 'ASP', 7.91), ('NE', 'ARG', 'OD1', 'ASP', 8.25), ('NE', 'ARG', 'OD2', 'ASP', 6.89), ('NE', 'ARG', 'O', 'ASP', 11.45), ('NE', 'ARG', 'C', 'ASP', 11.39), ('NE', 'ARG', 'CA', 'ASP', 10.4), ('NE', 'ARG', 'N', 'ASP', 10.9)], [('CZ', 'ARG', 'CB', 'ASP', 9.33), ('CZ', 'ARG', 'CG', 'ASP', 8.21), ('CZ', 'ARG', 'OD1', 'ASP', 8.56), ('CZ', 'ARG', 'OD2', 'ASP', 7.08), ('CZ', 'ARG', 'O', 'ASP', 12.04), ('CZ', 'ARG', 'C', 'ASP', 11.82), ('CZ', 'ARG', 'CA', 'ASP', 10.74), ('CZ', 'ARG', 'N', 'ASP', 11.04)], [('NH1', 'ARG', 'CB', 'ASP', 8.74), ('NH1', 'ARG', 'CG', 'ASP', 7.67), ('NH1', 'ARG', 'OD1', 'ASP', 8.16), ('NH1', 'ARG', 'OD2', 'ASP', 6.46), ('NH1', 'ARG', 'O', 'ASP', 11.58), ('NH1', 'ARG', 'C', 'ASP', 11.22), ('NH1', 'ARG', 'CA', 'ASP', 10.12), ('NH1', 'ARG', 'N', 'ASP', 10.28)], [('NH2', 'ARG', 'CB', 'ASP', 10.61), ('NH2', 'ARG', 'CG', 'ASP', 9.42), ('NH2', 'ARG', 'OD1', 'ASP', 9.67), ('NH2', 'ARG', 'OD2', 'ASP', 8.32), ('NH2', 'ARG', 'O', 'ASP', 13.34), ('NH2', 'ARG', 'C', 'ASP', 13.11), ('NH2', 'ARG', 'CA', 'ASP', 11.98), ('NH2', 'ARG', 'N', 'ASP', 12.22)], [('O', 'ARG', 'CB', 'ASP', 9.94), ('O', 'ARG', 'CG', 'ASP', 9.4), ('O', 'ARG', 'OD1', 'ASP', 9.23), ('O', 'ARG', 'OD2', 'ASP', 9.44), ('O', 'ARG', 'O', 'ASP', 10.58), ('O', 'ARG', 'C', 'ASP', 11.3), ('O', 'ARG', 'CA', 'ASP', 10.8), ('O', 'ARG', 'N', 'ASP', 11.95)], [('C', 'ARG', 'CB', 'ASP', 8.82), ('C', 'ARG', 'CG', 'ASP', 8.28), ('C', 'ARG', 'OD1', 'ASP', 8.22), ('C', 'ARG', 'OD2', 'ASP', 8.25), ('C', 'ARG', 'O', 'ASP', 9.67), ('C', 'ARG', 'C', 'ASP', 10.31), ('C', 'ARG', 'CA', 'ASP', 9.78), ('C', 'ARG', 'N', 'ASP', 10.92)], [('CA', 'ARG', 'CB', 'ASP', 8.22), ('CA', 'ARG', 'CG', 'ASP', 7.39), ('CA', 'ARG', 'OD1', 'ASP', 7.2), ('CA', 'ARG', 'OD2', 'ASP', 7.31), ('CA', 'ARG', 'O', 'ASP', 9.57), ('CA', 'ARG', 'C', 'ASP', 10.01), ('CA', 'ARG', 'CA', 'ASP', 9.22), ('CA', 'ARG', 'N', 'ASP', 10.19)], [('N', 'ARG', 'CB', 'ASP', 7.56), ('N', 'ARG', 'CG', 'ASP', 6.73), ('N', 'ARG', 'OD1', 'ASP', 6.28), ('N', 'ARG', 'OD2', 'ASP', 6.97), ('N', 'ARG', 'O', 'ASP', 8.74), ('N', 'ARG', 'C', 'ASP', 9.17), ('N', 'ARG', 'CA', 'ASP', 8.32), ('N', 'ARG', 'N', 'ASP', 9.25)]]}
GLY_ASP = { 
	'distances':
		[[10.83, 10.35, 10.67, 9.88, 13.32, 12.18, 11.14, 10.03], [11.35, 10.68, 10.9, 10.16, 13.97, 12.89, 11.74, 10.66], [11.25, 10.44, 10.68, 9.73, 14.07, 13.07, 11.86, 10.95], [11.55, 10.83, 11.25, 9.99, 14.37, 13.4, 12.29, 11.49]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 10.83), ('O', 'GLY', 'CG', 'ASP', 10.35), ('O', 'GLY', 'OD1', 'ASP', 10.67), ('O', 'GLY', 'OD2', 'ASP', 9.88), ('O', 'GLY', 'O', 'ASP', 13.32), ('O', 'GLY', 'C', 'ASP', 12.18), ('O', 'GLY', 'CA', 'ASP', 11.14), ('O', 'GLY', 'N', 'ASP', 10.03)], [('C', 'GLY', 'CB', 'ASP', 11.35), ('C', 'GLY', 'CG', 'ASP', 10.68), ('C', 'GLY', 'OD1', 'ASP', 10.9), ('C', 'GLY', 'OD2', 'ASP', 10.16), ('C', 'GLY', 'O', 'ASP', 13.97), ('C', 'GLY', 'C', 'ASP', 12.89), ('C', 'GLY', 'CA', 'ASP', 11.74), ('C', 'GLY', 'N', 'ASP', 10.66)], [('CA', 'GLY', 'CB', 'ASP', 11.25), ('CA', 'GLY', 'CG', 'ASP', 10.44), ('CA', 'GLY', 'OD1', 'ASP', 10.68), ('CA', 'GLY', 'OD2', 'ASP', 9.73), ('CA', 'GLY', 'O', 'ASP', 14.07), ('CA', 'GLY', 'C', 'ASP', 13.07), ('CA', 'GLY', 'CA', 'ASP', 11.86), ('CA', 'GLY', 'N', 'ASP', 10.95)], [('N', 'GLY', 'CB', 'ASP', 11.55), ('N', 'GLY', 'CG', 'ASP', 10.83), ('N', 'GLY', 'OD1', 'ASP', 11.25), ('N', 'GLY', 'OD2', 'ASP', 9.99), ('N', 'GLY', 'O', 'ASP', 14.37), ('N', 'GLY', 'C', 'ASP', 13.4), ('N', 'GLY', 'CA', 'ASP', 12.29), ('N', 'GLY', 'N', 'ASP', 11.49)]]}
GLY_ARG = { 
	'distances':
		[[12.39, 11.27, 11.41, 10.57, 9.4, 8.88, 9.01, 14.77, 13.96, 12.51, 12.12], [11.68, 10.63, 10.74, 9.79, 8.66, 8.34, 8.14, 14.07, 13.32, 11.85, 11.38], [10.47, 9.37, 9.34, 8.33, 7.17, 6.9, 6.63, 13.08, 12.32, 10.81, 10.46], [9.57, 8.37, 8.45, 7.66, 6.52, 5.97, 6.37, 12.21, 11.34, 9.86, 9.67], [13.51, 13.62, 12.34, 12.32, 11.39, 10.15, 11.87, 17.05, 15.92, 14.73, 14.37], [13.48, 13.62, 12.33, 12.15, 11.13, 9.97, 11.47, 17.05, 15.97, 14.7, 14.38], [12.67, 12.71, 11.37, 11.03, 9.93, 8.8, 10.14, 16.3, 15.23, 13.96, 13.78], [12.87, 12.71, 11.29, 10.94, 9.79, 8.61, 9.99, 16.55, 15.44, 14.25, 14.22]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ARG', 12.39), ('O', 'GLY', 'CG', 'ARG', 11.27), ('O', 'GLY', 'CD', 'ARG', 11.41), ('O', 'GLY', 'NE', 'ARG', 10.57), ('O', 'GLY', 'CZ', 'ARG', 9.4), ('O', 'GLY', 'NH1', 'ARG', 8.88), ('O', 'GLY', 'NH2', 'ARG', 9.01), ('O', 'GLY', 'O', 'ARG', 14.77), ('O', 'GLY', 'C', 'ARG', 13.96), ('O', 'GLY', 'CA', 'ARG', 12.51), ('O', 'GLY', 'N', 'ARG', 12.12)], [('C', 'GLY', 'CB', 'ARG', 11.68), ('C', 'GLY', 'CG', 'ARG', 10.63), ('C', 'GLY', 'CD', 'ARG', 10.74), ('C', 'GLY', 'NE', 'ARG', 9.79), ('C', 'GLY', 'CZ', 'ARG', 8.66), ('C', 'GLY', 'NH1', 'ARG', 8.34), ('C', 'GLY', 'NH2', 'ARG', 8.14), ('C', 'GLY', 'O', 'ARG', 14.07), ('C', 'GLY', 'C', 'ARG', 13.32), ('C', 'GLY', 'CA', 'ARG', 11.85), ('C', 'GLY', 'N', 'ARG', 11.38)], [('CA', 'GLY', 'CB', 'ARG', 10.47), ('CA', 'GLY', 'CG', 'ARG', 9.37), ('CA', 'GLY', 'CD', 'ARG', 9.34), ('CA', 'GLY', 'NE', 'ARG', 8.33), ('CA', 'GLY', 'CZ', 'ARG', 7.17), ('CA', 'GLY', 'NH1', 'ARG', 6.9), ('CA', 'GLY', 'NH2', 'ARG', 6.63), ('CA', 'GLY', 'O', 'ARG', 13.08), ('CA', 'GLY', 'C', 'ARG', 12.32), ('CA', 'GLY', 'CA', 'ARG', 10.81), ('CA', 'GLY', 'N', 'ARG', 10.46)], [('N', 'GLY', 'CB', 'ARG', 9.57), ('N', 'GLY', 'CG', 'ARG', 8.37), ('N', 'GLY', 'CD', 'ARG', 8.45), ('N', 'GLY', 'NE', 'ARG', 7.66), ('N', 'GLY', 'CZ', 'ARG', 6.52), ('N', 'GLY', 'NH1', 'ARG', 5.97), ('N', 'GLY', 'NH2', 'ARG', 6.37), ('N', 'GLY', 'O', 'ARG', 12.21), ('N', 'GLY', 'C', 'ARG', 11.34), ('N', 'GLY', 'CA', 'ARG', 9.86), ('N', 'GLY', 'N', 'ARG', 9.67)], [('O', 'GLY', 'CB', 'ARG', 13.51), ('O', 'GLY', 'CG', 'ARG', 13.62), ('O', 'GLY', 'CD', 'ARG', 12.34), ('O', 'GLY', 'NE', 'ARG', 12.32), ('O', 'GLY', 'CZ', 'ARG', 11.39), ('O', 'GLY', 'NH1', 'ARG', 10.15), ('O', 'GLY', 'NH2', 'ARG', 11.87), ('O', 'GLY', 'O', 'ARG', 17.05), ('O', 'GLY', 'C', 'ARG', 15.92), ('O', 'GLY', 'CA', 'ARG', 14.73), ('O', 'GLY', 'N', 'ARG', 14.37)], [('C', 'GLY', 'CB', 'ARG', 13.48), ('C', 'GLY', 'CG', 'ARG', 13.62), ('C', 'GLY', 'CD', 'ARG', 12.33), ('C', 'GLY', 'NE', 'ARG', 12.15), ('C', 'GLY', 'CZ', 'ARG', 11.13), ('C', 'GLY', 'NH1', 'ARG', 9.97), ('C', 'GLY', 'NH2', 'ARG', 11.47), ('C', 'GLY', 'O', 'ARG', 17.05), ('C', 'GLY', 'C', 'ARG', 15.97), ('C', 'GLY', 'CA', 'ARG', 14.7), ('C', 'GLY', 'N', 'ARG', 14.38)], [('CA', 'GLY', 'CB', 'ARG', 12.67), ('CA', 'GLY', 'CG', 'ARG', 12.71), ('CA', 'GLY', 'CD', 'ARG', 11.37), ('CA', 'GLY', 'NE', 'ARG', 11.03), ('CA', 'GLY', 'CZ', 'ARG', 9.93), ('CA', 'GLY', 'NH1', 'ARG', 8.8), ('CA', 'GLY', 'NH2', 'ARG', 10.14), ('CA', 'GLY', 'O', 'ARG', 16.3), ('CA', 'GLY', 'C', 'ARG', 15.23), ('CA', 'GLY', 'CA', 'ARG', 13.96), ('CA', 'GLY', 'N', 'ARG', 13.78)], [('N', 'GLY', 'CB', 'ARG', 12.87), ('N', 'GLY', 'CG', 'ARG', 12.71), ('N', 'GLY', 'CD', 'ARG', 11.29), ('N', 'GLY', 'NE', 'ARG', 10.94), ('N', 'GLY', 'CZ', 'ARG', 9.79), ('N', 'GLY', 'NH1', 'ARG', 8.61), ('N', 'GLY', 'NH2', 'ARG', 9.99), ('N', 'GLY', 'O', 'ARG', 16.55), ('N', 'GLY', 'C', 'ARG', 15.44), ('N', 'GLY', 'CA', 'ARG', 14.25), ('N', 'GLY', 'N', 'ARG', 14.22)]]}
GLY_THR = { 
	'distances':
		[[7.29, 7.55, 8.7, 9.15, 8.06, 6.87, 7.1], [8.27, 8.31, 9.72, 10.13, 8.98, 7.9, 8.27], [8.69, 8.52, 10.11, 10.9, 9.73, 8.65, 9.2], [8.77, 8.76, 10.05, 11.31, 10.21, 8.98, 9.4]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'THR', 7.29), ('O', 'GLY', 'OG1', 'THR', 7.55), ('O', 'GLY', 'CG2', 'THR', 8.7), ('O', 'GLY', 'O', 'THR', 9.15), ('O', 'GLY', 'C', 'THR', 8.06), ('O', 'GLY', 'CA', 'THR', 6.87), ('O', 'GLY', 'N', 'THR', 7.1)], [('C', 'GLY', 'CB', 'THR', 8.27), ('C', 'GLY', 'OG1', 'THR', 8.31), ('C', 'GLY', 'CG2', 'THR', 9.72), ('C', 'GLY', 'O', 'THR', 10.13), ('C', 'GLY', 'C', 'THR', 8.98), ('C', 'GLY', 'CA', 'THR', 7.9), ('C', 'GLY', 'N', 'THR', 8.27)], [('CA', 'GLY', 'CB', 'THR', 8.69), ('CA', 'GLY', 'OG1', 'THR', 8.52), ('CA', 'GLY', 'CG2', 'THR', 10.11), ('CA', 'GLY', 'O', 'THR', 10.9), ('CA', 'GLY', 'C', 'THR', 9.73), ('CA', 'GLY', 'CA', 'THR', 8.65), ('CA', 'GLY', 'N', 'THR', 9.2)], [('N', 'GLY', 'CB', 'THR', 8.77), ('N', 'GLY', 'OG1', 'THR', 8.76), ('N', 'GLY', 'CG2', 'THR', 10.05), ('N', 'GLY', 'O', 'THR', 11.31), ('N', 'GLY', 'C', 'THR', 10.21), ('N', 'GLY', 'CA', 'THR', 8.98), ('N', 'GLY', 'N', 'THR', 9.4)]]}
ARG_THR = { 
	'distances':
		[[15.87, 15.76, 16.89, 18.7, 17.65, 16.4, 16.75], [14.45, 14.33, 15.43, 17.33, 16.3, 15.04, 15.43], [14.25, 13.96, 15.22, 17.14, 16.1, 14.93, 15.47], [13.56, 13.18, 14.64, 16.34, 15.25, 14.16, 14.79], [12.26, 11.85, 13.36, 15.02, 13.92, 12.85, 13.53], [11.34, 11.02, 12.35, 14.21, 13.18, 12.04, 12.66], [12.02, 11.49, 13.23, 14.61, 13.47, 12.51, 13.27], [18.63, 18.67, 19.64, 21.39, 20.37, 19.04, 19.22], [17.61, 17.68, 18.57, 20.42, 19.42, 18.07, 18.24], [16.23, 16.25, 17.24, 19.01, 17.99, 16.66, 16.88], [16.26, 16.31, 17.37, 18.91, 17.85, 16.54, 16.72], [11.31, 9.97, 11.6, 12.74, 12.16, 12.33, 13.71], [11.41, 10.19, 11.61, 13.16, 12.6, 12.59, 13.9], [10.46, 9.31, 10.79, 12.51, 11.86, 11.68, 12.94], [11.19, 10.04, 11.69, 13.38, 12.62, 12.33, 13.58], [10.87, 9.8, 11.52, 13.25, 12.39, 11.95, 13.15], [9.69, 8.71, 10.41, 12.21, 11.33, 10.77, 11.92], [11.95, 10.91, 12.69, 14.38, 13.46, 12.95, 14.13], [14.34, 13.02, 14.39, 15.25, 14.89, 15.33, 16.71], [13.14, 11.84, 13.18, 14.16, 13.79, 14.17, 15.53], [12.35, 10.98, 12.58, 13.46, 12.96, 13.3, 14.7], [11.87, 10.46, 12.13, 12.63, 12.16, 12.67, 14.09]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'THR', 15.87), ('CB', 'ARG', 'OG1', 'THR', 15.76), ('CB', 'ARG', 'CG2', 'THR', 16.89), ('CB', 'ARG', 'O', 'THR', 18.7), ('CB', 'ARG', 'C', 'THR', 17.65), ('CB', 'ARG', 'CA', 'THR', 16.4), ('CB', 'ARG', 'N', 'THR', 16.75)], [('CG', 'ARG', 'CB', 'THR', 14.45), ('CG', 'ARG', 'OG1', 'THR', 14.33), ('CG', 'ARG', 'CG2', 'THR', 15.43), ('CG', 'ARG', 'O', 'THR', 17.33), ('CG', 'ARG', 'C', 'THR', 16.3), ('CG', 'ARG', 'CA', 'THR', 15.04), ('CG', 'ARG', 'N', 'THR', 15.43)], [('CD', 'ARG', 'CB', 'THR', 14.25), ('CD', 'ARG', 'OG1', 'THR', 13.96), ('CD', 'ARG', 'CG2', 'THR', 15.22), ('CD', 'ARG', 'O', 'THR', 17.14), ('CD', 'ARG', 'C', 'THR', 16.1), ('CD', 'ARG', 'CA', 'THR', 14.93), ('CD', 'ARG', 'N', 'THR', 15.47)], [('NE', 'ARG', 'CB', 'THR', 13.56), ('NE', 'ARG', 'OG1', 'THR', 13.18), ('NE', 'ARG', 'CG2', 'THR', 14.64), ('NE', 'ARG', 'O', 'THR', 16.34), ('NE', 'ARG', 'C', 'THR', 15.25), ('NE', 'ARG', 'CA', 'THR', 14.16), ('NE', 'ARG', 'N', 'THR', 14.79)], [('CZ', 'ARG', 'CB', 'THR', 12.26), ('CZ', 'ARG', 'OG1', 'THR', 11.85), ('CZ', 'ARG', 'CG2', 'THR', 13.36), ('CZ', 'ARG', 'O', 'THR', 15.02), ('CZ', 'ARG', 'C', 'THR', 13.92), ('CZ', 'ARG', 'CA', 'THR', 12.85), ('CZ', 'ARG', 'N', 'THR', 13.53)], [('NH1', 'ARG', 'CB', 'THR', 11.34), ('NH1', 'ARG', 'OG1', 'THR', 11.02), ('NH1', 'ARG', 'CG2', 'THR', 12.35), ('NH1', 'ARG', 'O', 'THR', 14.21), ('NH1', 'ARG', 'C', 'THR', 13.18), ('NH1', 'ARG', 'CA', 'THR', 12.04), ('NH1', 'ARG', 'N', 'THR', 12.66)], [('NH2', 'ARG', 'CB', 'THR', 12.02), ('NH2', 'ARG', 'OG1', 'THR', 11.49), ('NH2', 'ARG', 'CG2', 'THR', 13.23), ('NH2', 'ARG', 'O', 'THR', 14.61), ('NH2', 'ARG', 'C', 'THR', 13.47), ('NH2', 'ARG', 'CA', 'THR', 12.51), ('NH2', 'ARG', 'N', 'THR', 13.27)], [('O', 'ARG', 'CB', 'THR', 18.63), ('O', 'ARG', 'OG1', 'THR', 18.67), ('O', 'ARG', 'CG2', 'THR', 19.64), ('O', 'ARG', 'O', 'THR', 21.39), ('O', 'ARG', 'C', 'THR', 20.37), ('O', 'ARG', 'CA', 'THR', 19.04), ('O', 'ARG', 'N', 'THR', 19.22)], [('C', 'ARG', 'CB', 'THR', 17.61), ('C', 'ARG', 'OG1', 'THR', 17.68), ('C', 'ARG', 'CG2', 'THR', 18.57), ('C', 'ARG', 'O', 'THR', 20.42), ('C', 'ARG', 'C', 'THR', 19.42), ('C', 'ARG', 'CA', 'THR', 18.07), ('C', 'ARG', 'N', 'THR', 18.24)], [('CA', 'ARG', 'CB', 'THR', 16.23), ('CA', 'ARG', 'OG1', 'THR', 16.25), ('CA', 'ARG', 'CG2', 'THR', 17.24), ('CA', 'ARG', 'O', 'THR', 19.01), ('CA', 'ARG', 'C', 'THR', 17.99), ('CA', 'ARG', 'CA', 'THR', 16.66), ('CA', 'ARG', 'N', 'THR', 16.88)], [('N', 'ARG', 'CB', 'THR', 16.26), ('N', 'ARG', 'OG1', 'THR', 16.31), ('N', 'ARG', 'CG2', 'THR', 17.37), ('N', 'ARG', 'O', 'THR', 18.91), ('N', 'ARG', 'C', 'THR', 17.85), ('N', 'ARG', 'CA', 'THR', 16.54), ('N', 'ARG', 'N', 'THR', 16.72)], [('CB', 'ARG', 'CB', 'THR', 11.31), ('CB', 'ARG', 'OG1', 'THR', 9.97), ('CB', 'ARG', 'CG2', 'THR', 11.6), ('CB', 'ARG', 'O', 'THR', 12.74), ('CB', 'ARG', 'C', 'THR', 12.16), ('CB', 'ARG', 'CA', 'THR', 12.33), ('CB', 'ARG', 'N', 'THR', 13.71)], [('CG', 'ARG', 'CB', 'THR', 11.41), ('CG', 'ARG', 'OG1', 'THR', 10.19), ('CG', 'ARG', 'CG2', 'THR', 11.61), ('CG', 'ARG', 'O', 'THR', 13.16), ('CG', 'ARG', 'C', 'THR', 12.6), ('CG', 'ARG', 'CA', 'THR', 12.59), ('CG', 'ARG', 'N', 'THR', 13.9)], [('CD', 'ARG', 'CB', 'THR', 10.46), ('CD', 'ARG', 'OG1', 'THR', 9.31), ('CD', 'ARG', 'CG2', 'THR', 10.79), ('CD', 'ARG', 'O', 'THR', 12.51), ('CD', 'ARG', 'C', 'THR', 11.86), ('CD', 'ARG', 'CA', 'THR', 11.68), ('CD', 'ARG', 'N', 'THR', 12.94)], [('NE', 'ARG', 'CB', 'THR', 11.19), ('NE', 'ARG', 'OG1', 'THR', 10.04), ('NE', 'ARG', 'CG2', 'THR', 11.69), ('NE', 'ARG', 'O', 'THR', 13.38), ('NE', 'ARG', 'C', 'THR', 12.62), ('NE', 'ARG', 'CA', 'THR', 12.33), ('NE', 'ARG', 'N', 'THR', 13.58)], [('CZ', 'ARG', 'CB', 'THR', 10.87), ('CZ', 'ARG', 'OG1', 'THR', 9.8), ('CZ', 'ARG', 'CG2', 'THR', 11.52), ('CZ', 'ARG', 'O', 'THR', 13.25), ('CZ', 'ARG', 'C', 'THR', 12.39), ('CZ', 'ARG', 'CA', 'THR', 11.95), ('CZ', 'ARG', 'N', 'THR', 13.15)], [('NH1', 'ARG', 'CB', 'THR', 9.69), ('NH1', 'ARG', 'OG1', 'THR', 8.71), ('NH1', 'ARG', 'CG2', 'THR', 10.41), ('NH1', 'ARG', 'O', 'THR', 12.21), ('NH1', 'ARG', 'C', 'THR', 11.33), ('NH1', 'ARG', 'CA', 'THR', 10.77), ('NH1', 'ARG', 'N', 'THR', 11.92)], [('NH2', 'ARG', 'CB', 'THR', 11.95), ('NH2', 'ARG', 'OG1', 'THR', 10.91), ('NH2', 'ARG', 'CG2', 'THR', 12.69), ('NH2', 'ARG', 'O', 'THR', 14.38), ('NH2', 'ARG', 'C', 'THR', 13.46), ('NH2', 'ARG', 'CA', 'THR', 12.95), ('NH2', 'ARG', 'N', 'THR', 14.13)], [('O', 'ARG', 'CB', 'THR', 14.34), ('O', 'ARG', 'OG1', 'THR', 13.02), ('O', 'ARG', 'CG2', 'THR', 14.39), ('O', 'ARG', 'O', 'THR', 15.25), ('O', 'ARG', 'C', 'THR', 14.89), ('O', 'ARG', 'CA', 'THR', 15.33), ('O', 'ARG', 'N', 'THR', 16.71)], [('C', 'ARG', 'CB', 'THR', 13.14), ('C', 'ARG', 'OG1', 'THR', 11.84), ('C', 'ARG', 'CG2', 'THR', 13.18), ('C', 'ARG', 'O', 'THR', 14.16), ('C', 'ARG', 'C', 'THR', 13.79), ('C', 'ARG', 'CA', 'THR', 14.17), ('C', 'ARG', 'N', 'THR', 15.53)], [('CA', 'ARG', 'CB', 'THR', 12.35), ('CA', 'ARG', 'OG1', 'THR', 10.98), ('CA', 'ARG', 'CG2', 'THR', 12.58), ('CA', 'ARG', 'O', 'THR', 13.46), ('CA', 'ARG', 'C', 'THR', 12.96), ('CA', 'ARG', 'CA', 'THR', 13.3), ('CA', 'ARG', 'N', 'THR', 14.7)], [('N', 'ARG', 'CB', 'THR', 11.87), ('N', 'ARG', 'OG1', 'THR', 10.46), ('N', 'ARG', 'CG2', 'THR', 12.13), ('N', 'ARG', 'O', 'THR', 12.63), ('N', 'ARG', 'C', 'THR', 12.16), ('N', 'ARG', 'CA', 'THR', 12.67), ('N', 'ARG', 'N', 'THR', 14.09)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_ASP, d, 'P_1pfk_2_7_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_ARG, d, 'P_1pfk_2_7_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASP, d, 'P_1pfk_2_7_1_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_ASP, d, 'P_1pfk_2_7_1_11')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_ARG, d, 'P_1pfk_2_7_1_11')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLY_THR, d, 'P_1pfk_2_7_1_11')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ARG_THR, d, 'P_1pfk_2_7_1_11')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_ASP' :  match1,
		'ARG_ARG' :  match2,
		'ARG_ASP' :  match3,
		'GLY_ASP' :  match4,
		'GLY_ARG' :  match5,
		'GLY_THR' :  match6,
		'ARG_THR' :  match7}