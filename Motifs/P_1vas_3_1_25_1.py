'''
FUNC:P_1vas_3_1_25_1
PDB:1vas
EC:3.1.25.1
RESI:thr,arg,gln,arg
LOCI:a-2,22,23,26;
'''
import motifFunctions as cmd
THR_GLN = { 
	'distances':
		[[6.87, 6.96, 6.96, 6.47, 7.85], [7.19, 7.05, 7.28, 7.11, 8.03], [5.89, 6.4, 6.67, 6.18, 7.76], [8.53, 8.5, 7.72, 6.71, 8.37], [7.3, 7.31, 6.62, 5.65, 7.39], [6.85, 6.64, 6.18, 5.56, 6.9], [8.12, 7.65, 7.07, 6.59, 7.51]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLN', 6.87), ('CB', 'THR', 'CG', 'GLN', 6.96), ('CB', 'THR', 'CD', 'GLN', 6.96), ('CB', 'THR', 'OE1', 'GLN', 6.47), ('CB', 'THR', 'NE2', 'GLN', 7.85)], [('OG1', 'THR', 'CB', 'GLN', 7.19), ('OG1', 'THR', 'CG', 'GLN', 7.05), ('OG1', 'THR', 'CD', 'GLN', 7.28), ('OG1', 'THR', 'OE1', 'GLN', 7.11), ('OG1', 'THR', 'NE2', 'GLN', 8.03)], [('CG2', 'THR', 'CB', 'GLN', 5.89), ('CG2', 'THR', 'CG', 'GLN', 6.4), ('CG2', 'THR', 'CD', 'GLN', 6.67), ('CG2', 'THR', 'OE1', 'GLN', 6.18), ('CG2', 'THR', 'NE2', 'GLN', 7.76)], [('O', 'THR', 'CB', 'GLN', 8.53), ('O', 'THR', 'CG', 'GLN', 8.5), ('O', 'THR', 'CD', 'GLN', 7.72), ('O', 'THR', 'OE1', 'GLN', 6.71), ('O', 'THR', 'NE2', 'GLN', 8.37)], [('C', 'THR', 'CB', 'GLN', 7.3), ('C', 'THR', 'CG', 'GLN', 7.31), ('C', 'THR', 'CD', 'GLN', 6.62), ('C', 'THR', 'OE1', 'GLN', 5.65), ('C', 'THR', 'NE2', 'GLN', 7.39)], [('CA', 'THR', 'CB', 'GLN', 6.85), ('CA', 'THR', 'CG', 'GLN', 6.64), ('CA', 'THR', 'CD', 'GLN', 6.18), ('CA', 'THR', 'OE1', 'GLN', 5.56), ('CA', 'THR', 'NE2', 'GLN', 6.9)], [('N', 'THR', 'CB', 'GLN', 8.12), ('N', 'THR', 'CG', 'GLN', 7.65), ('N', 'THR', 'CD', 'GLN', 7.07), ('N', 'THR', 'OE1', 'GLN', 6.59), ('N', 'THR', 'NE2', 'GLN', 7.51)]]}
ARG_GLN = { 
	'distances':
		[[7.55, 7.46, 8.63, 9.62, 8.77], [7.11, 6.66, 7.63, 8.71, 7.56], [8.28, 7.56, 8.4, 9.58, 8.09], [8.15, 7.12, 7.74, 8.98, 7.22], [7.95, 6.79, 7.08, 8.28, 6.36], [7.84, 6.86, 7.03, 8.13, 6.36], [8.22, 6.86, 6.87, 8.05, 5.95], [7.52, 8.06, 9.22, 9.42, 10.14], [7.22, 7.45, 8.71, 9.16, 9.47], [6.75, 6.64, 7.71, 8.19, 8.38], [6.63, 6.13, 7.24, 7.98, 7.67], [6.39, 5.49, 6.34, 7.18, 6.59], [6.18, 5.25, 5.73, 6.35, 6.05], [6.93, 5.8, 6.55, 7.59, 6.47]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLN', 7.55), ('CB', 'ARG', 'CG', 'GLN', 7.46), ('CB', 'ARG', 'CD', 'GLN', 8.63), ('CB', 'ARG', 'OE1', 'GLN', 9.62), ('CB', 'ARG', 'NE2', 'GLN', 8.77)], [('CG', 'ARG', 'CB', 'GLN', 7.11), ('CG', 'ARG', 'CG', 'GLN', 6.66), ('CG', 'ARG', 'CD', 'GLN', 7.63), ('CG', 'ARG', 'OE1', 'GLN', 8.71), ('CG', 'ARG', 'NE2', 'GLN', 7.56)], [('CD', 'ARG', 'CB', 'GLN', 8.28), ('CD', 'ARG', 'CG', 'GLN', 7.56), ('CD', 'ARG', 'CD', 'GLN', 8.4), ('CD', 'ARG', 'OE1', 'GLN', 9.58), ('CD', 'ARG', 'NE2', 'GLN', 8.09)], [('NE', 'ARG', 'CB', 'GLN', 8.15), ('NE', 'ARG', 'CG', 'GLN', 7.12), ('NE', 'ARG', 'CD', 'GLN', 7.74), ('NE', 'ARG', 'OE1', 'GLN', 8.98), ('NE', 'ARG', 'NE2', 'GLN', 7.22)], [('CZ', 'ARG', 'CB', 'GLN', 7.95), ('CZ', 'ARG', 'CG', 'GLN', 6.79), ('CZ', 'ARG', 'CD', 'GLN', 7.08), ('CZ', 'ARG', 'OE1', 'GLN', 8.28), ('CZ', 'ARG', 'NE2', 'GLN', 6.36)], [('NH1', 'ARG', 'CB', 'GLN', 7.84), ('NH1', 'ARG', 'CG', 'GLN', 6.86), ('NH1', 'ARG', 'CD', 'GLN', 7.03), ('NH1', 'ARG', 'OE1', 'GLN', 8.13), ('NH1', 'ARG', 'NE2', 'GLN', 6.36)], [('NH2', 'ARG', 'CB', 'GLN', 8.22), ('NH2', 'ARG', 'CG', 'GLN', 6.86), ('NH2', 'ARG', 'CD', 'GLN', 6.87), ('NH2', 'ARG', 'OE1', 'GLN', 8.05), ('NH2', 'ARG', 'NE2', 'GLN', 5.95)], [('CB', 'ARG', 'CB', 'GLN', 7.52), ('CB', 'ARG', 'CG', 'GLN', 8.06), ('CB', 'ARG', 'CD', 'GLN', 9.22), ('CB', 'ARG', 'OE1', 'GLN', 9.42), ('CB', 'ARG', 'NE2', 'GLN', 10.14)], [('CG', 'ARG', 'CB', 'GLN', 7.22), ('CG', 'ARG', 'CG', 'GLN', 7.45), ('CG', 'ARG', 'CD', 'GLN', 8.71), ('CG', 'ARG', 'OE1', 'GLN', 9.16), ('CG', 'ARG', 'NE2', 'GLN', 9.47)], [('CD', 'ARG', 'CB', 'GLN', 6.75), ('CD', 'ARG', 'CG', 'GLN', 6.64), ('CD', 'ARG', 'CD', 'GLN', 7.71), ('CD', 'ARG', 'OE1', 'GLN', 8.19), ('CD', 'ARG', 'NE2', 'GLN', 8.38)], [('NE', 'ARG', 'CB', 'GLN', 6.63), ('NE', 'ARG', 'CG', 'GLN', 6.13), ('NE', 'ARG', 'CD', 'GLN', 7.24), ('NE', 'ARG', 'OE1', 'GLN', 7.98), ('NE', 'ARG', 'NE2', 'GLN', 7.67)], [('CZ', 'ARG', 'CB', 'GLN', 6.39), ('CZ', 'ARG', 'CG', 'GLN', 5.49), ('CZ', 'ARG', 'CD', 'GLN', 6.34), ('CZ', 'ARG', 'OE1', 'GLN', 7.18), ('CZ', 'ARG', 'NE2', 'GLN', 6.59)], [('NH1', 'ARG', 'CB', 'GLN', 6.18), ('NH1', 'ARG', 'CG', 'GLN', 5.25), ('NH1', 'ARG', 'CD', 'GLN', 5.73), ('NH1', 'ARG', 'OE1', 'GLN', 6.35), ('NH1', 'ARG', 'NE2', 'GLN', 6.05)], [('NH2', 'ARG', 'CB', 'GLN', 6.93), ('NH2', 'ARG', 'CG', 'GLN', 5.8), ('NH2', 'ARG', 'CD', 'GLN', 6.55), ('NH2', 'ARG', 'OE1', 'GLN', 7.59), ('NH2', 'ARG', 'NE2', 'GLN', 6.47)]]}
THR_ARG = { 
	'distances':
		[[11.89, 11.38, 12.16, 11.57, 11.33, 11.65, 10.97], [11.61, 11.13, 11.75, 11.12, 11.02, 11.53, 10.63], [11.03, 10.68, 11.63, 11.23, 11.06, 11.26, 10.92], [13.91, 13.16, 13.95, 13.21, 12.6, 12.68, 12.07], [12.69, 11.97, 12.8, 12.12, 11.56, 11.64, 11.11], [11.95, 11.23, 11.94, 11.21, 10.77, 11.03, 10.28], [12.91, 12.1, 12.63, 11.74, 11.27, 11.66, 10.58], [7.12, 7.5, 6.53, 7.29, 7.09, 6.01, 8.24], [6.48, 6.65, 5.51, 6.3, 6.19, 5.21, 7.41], [6.43, 6.95, 6.3, 7.13, 7.12, 6.28, 8.29], [10.36, 10.73, 9.69, 10.18, 9.6, 8.33, 10.47], [9.4, 9.7, 8.68, 9.12, 8.57, 7.35, 9.46], [8.4, 8.53, 7.38, 7.78, 7.22, 5.96, 8.16], [9.25, 9.28, 7.97, 8.29, 7.6, 6.29, 8.45]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ARG', 11.89), ('CB', 'THR', 'CG', 'ARG', 11.38), ('CB', 'THR', 'CD', 'ARG', 12.16), ('CB', 'THR', 'NE', 'ARG', 11.57), ('CB', 'THR', 'CZ', 'ARG', 11.33), ('CB', 'THR', 'NH1', 'ARG', 11.65), ('CB', 'THR', 'NH2', 'ARG', 10.97)], [('OG1', 'THR', 'CB', 'ARG', 11.61), ('OG1', 'THR', 'CG', 'ARG', 11.13), ('OG1', 'THR', 'CD', 'ARG', 11.75), ('OG1', 'THR', 'NE', 'ARG', 11.12), ('OG1', 'THR', 'CZ', 'ARG', 11.02), ('OG1', 'THR', 'NH1', 'ARG', 11.53), ('OG1', 'THR', 'NH2', 'ARG', 10.63)], [('CG2', 'THR', 'CB', 'ARG', 11.03), ('CG2', 'THR', 'CG', 'ARG', 10.68), ('CG2', 'THR', 'CD', 'ARG', 11.63), ('CG2', 'THR', 'NE', 'ARG', 11.23), ('CG2', 'THR', 'CZ', 'ARG', 11.06), ('CG2', 'THR', 'NH1', 'ARG', 11.26), ('CG2', 'THR', 'NH2', 'ARG', 10.92)], [('O', 'THR', 'CB', 'ARG', 13.91), ('O', 'THR', 'CG', 'ARG', 13.16), ('O', 'THR', 'CD', 'ARG', 13.95), ('O', 'THR', 'NE', 'ARG', 13.21), ('O', 'THR', 'CZ', 'ARG', 12.6), ('O', 'THR', 'NH1', 'ARG', 12.68), ('O', 'THR', 'NH2', 'ARG', 12.07)], [('C', 'THR', 'CB', 'ARG', 12.69), ('C', 'THR', 'CG', 'ARG', 11.97), ('C', 'THR', 'CD', 'ARG', 12.8), ('C', 'THR', 'NE', 'ARG', 12.12), ('C', 'THR', 'CZ', 'ARG', 11.56), ('C', 'THR', 'NH1', 'ARG', 11.64), ('C', 'THR', 'NH2', 'ARG', 11.11)], [('CA', 'THR', 'CB', 'ARG', 11.95), ('CA', 'THR', 'CG', 'ARG', 11.23), ('CA', 'THR', 'CD', 'ARG', 11.94), ('CA', 'THR', 'NE', 'ARG', 11.21), ('CA', 'THR', 'CZ', 'ARG', 10.77), ('CA', 'THR', 'NH1', 'ARG', 11.03), ('CA', 'THR', 'NH2', 'ARG', 10.28)], [('N', 'THR', 'CB', 'ARG', 12.91), ('N', 'THR', 'CG', 'ARG', 12.1), ('N', 'THR', 'CD', 'ARG', 12.63), ('N', 'THR', 'NE', 'ARG', 11.74), ('N', 'THR', 'CZ', 'ARG', 11.27), ('N', 'THR', 'NH1', 'ARG', 11.66), ('N', 'THR', 'NH2', 'ARG', 10.58)], [('CB', 'THR', 'CB', 'ARG', 7.12), ('CB', 'THR', 'CG', 'ARG', 7.5), ('CB', 'THR', 'CD', 'ARG', 6.53), ('CB', 'THR', 'NE', 'ARG', 7.29), ('CB', 'THR', 'CZ', 'ARG', 7.09), ('CB', 'THR', 'NH1', 'ARG', 6.01), ('CB', 'THR', 'NH2', 'ARG', 8.24)], [('OG1', 'THR', 'CB', 'ARG', 6.48), ('OG1', 'THR', 'CG', 'ARG', 6.65), ('OG1', 'THR', 'CD', 'ARG', 5.51), ('OG1', 'THR', 'NE', 'ARG', 6.3), ('OG1', 'THR', 'CZ', 'ARG', 6.19), ('OG1', 'THR', 'NH1', 'ARG', 5.21), ('OG1', 'THR', 'NH2', 'ARG', 7.41)], [('CG2', 'THR', 'CB', 'ARG', 6.43), ('CG2', 'THR', 'CG', 'ARG', 6.95), ('CG2', 'THR', 'CD', 'ARG', 6.3), ('CG2', 'THR', 'NE', 'ARG', 7.13), ('CG2', 'THR', 'CZ', 'ARG', 7.12), ('CG2', 'THR', 'NH1', 'ARG', 6.28), ('CG2', 'THR', 'NH2', 'ARG', 8.29)], [('O', 'THR', 'CB', 'ARG', 10.36), ('O', 'THR', 'CG', 'ARG', 10.73), ('O', 'THR', 'CD', 'ARG', 9.69), ('O', 'THR', 'NE', 'ARG', 10.18), ('O', 'THR', 'CZ', 'ARG', 9.6), ('O', 'THR', 'NH1', 'ARG', 8.33), ('O', 'THR', 'NH2', 'ARG', 10.47)], [('C', 'THR', 'CB', 'ARG', 9.4), ('C', 'THR', 'CG', 'ARG', 9.7), ('C', 'THR', 'CD', 'ARG', 8.68), ('C', 'THR', 'NE', 'ARG', 9.12), ('C', 'THR', 'CZ', 'ARG', 8.57), ('C', 'THR', 'NH1', 'ARG', 7.35), ('C', 'THR', 'NH2', 'ARG', 9.46)], [('CA', 'THR', 'CB', 'ARG', 8.4), ('CA', 'THR', 'CG', 'ARG', 8.53), ('CA', 'THR', 'CD', 'ARG', 7.38), ('CA', 'THR', 'NE', 'ARG', 7.78), ('CA', 'THR', 'CZ', 'ARG', 7.22), ('CA', 'THR', 'NH1', 'ARG', 5.96), ('CA', 'THR', 'NH2', 'ARG', 8.16)], [('N', 'THR', 'CB', 'ARG', 9.25), ('N', 'THR', 'CG', 'ARG', 9.28), ('N', 'THR', 'CD', 'ARG', 7.97), ('N', 'THR', 'NE', 'ARG', 8.29), ('N', 'THR', 'CZ', 'ARG', 7.6), ('N', 'THR', 'NH1', 'ARG', 6.29), ('N', 'THR', 'NH2', 'ARG', 8.45)]]}
ARG_ARG = { 
	'distances':
		[[10.07, 9.03, 9.17, 8.27, 8.35, 9.24, 7.9], [10.33, 9.23, 9.04, 7.98, 7.74, 8.52, 7.11], [11.11, 9.84, 9.54, 8.29, 7.96, 8.85, 7.05], [11.1, 9.79, 9.22, 7.86, 7.26, 8.05, 6.18], [11.56, 10.36, 9.62, 8.32, 7.5, 8.01, 6.46], [12.05, 10.97, 10.31, 9.12, 8.33, 8.72, 7.46], [11.73, 10.54, 9.59, 8.27, 7.25, 7.58, 6.16], [10.07, 10.33, 11.11, 11.1, 11.56, 12.05, 11.73], [9.03, 9.23, 9.84, 9.79, 10.36, 10.97, 10.54], [9.17, 9.04, 9.54, 9.22, 9.62, 10.31, 9.59], [8.27, 7.98, 8.29, 7.86, 8.32, 9.12, 8.27], [8.35, 7.74, 7.96, 7.26, 7.5, 8.33, 7.25], [9.24, 8.52, 8.85, 8.05, 8.01, 8.72, 7.58], [7.9, 7.11, 7.05, 6.18, 6.46, 7.46, 6.16]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 10.07), ('CB', 'ARG', 'CG', 'ARG', 9.03), ('CB', 'ARG', 'CD', 'ARG', 9.17), ('CB', 'ARG', 'NE', 'ARG', 8.27), ('CB', 'ARG', 'CZ', 'ARG', 8.35), ('CB', 'ARG', 'NH1', 'ARG', 9.24), ('CB', 'ARG', 'NH2', 'ARG', 7.9)], [('CG', 'ARG', 'CB', 'ARG', 10.33), ('CG', 'ARG', 'CG', 'ARG', 9.23), ('CG', 'ARG', 'CD', 'ARG', 9.04), ('CG', 'ARG', 'NE', 'ARG', 7.98), ('CG', 'ARG', 'CZ', 'ARG', 7.74), ('CG', 'ARG', 'NH1', 'ARG', 8.52), ('CG', 'ARG', 'NH2', 'ARG', 7.11)], [('CD', 'ARG', 'CB', 'ARG', 11.11), ('CD', 'ARG', 'CG', 'ARG', 9.84), ('CD', 'ARG', 'CD', 'ARG', 9.54), ('CD', 'ARG', 'NE', 'ARG', 8.29), ('CD', 'ARG', 'CZ', 'ARG', 7.96), ('CD', 'ARG', 'NH1', 'ARG', 8.85), ('CD', 'ARG', 'NH2', 'ARG', 7.05)], [('NE', 'ARG', 'CB', 'ARG', 11.1), ('NE', 'ARG', 'CG', 'ARG', 9.79), ('NE', 'ARG', 'CD', 'ARG', 9.22), ('NE', 'ARG', 'NE', 'ARG', 7.86), ('NE', 'ARG', 'CZ', 'ARG', 7.26), ('NE', 'ARG', 'NH1', 'ARG', 8.05), ('NE', 'ARG', 'NH2', 'ARG', 6.18)], [('CZ', 'ARG', 'CB', 'ARG', 11.56), ('CZ', 'ARG', 'CG', 'ARG', 10.36), ('CZ', 'ARG', 'CD', 'ARG', 9.62), ('CZ', 'ARG', 'NE', 'ARG', 8.32), ('CZ', 'ARG', 'CZ', 'ARG', 7.5), ('CZ', 'ARG', 'NH1', 'ARG', 8.01), ('CZ', 'ARG', 'NH2', 'ARG', 6.46)], [('NH1', 'ARG', 'CB', 'ARG', 12.05), ('NH1', 'ARG', 'CG', 'ARG', 10.97), ('NH1', 'ARG', 'CD', 'ARG', 10.31), ('NH1', 'ARG', 'NE', 'ARG', 9.12), ('NH1', 'ARG', 'CZ', 'ARG', 8.33), ('NH1', 'ARG', 'NH1', 'ARG', 8.72), ('NH1', 'ARG', 'NH2', 'ARG', 7.46)], [('NH2', 'ARG', 'CB', 'ARG', 11.73), ('NH2', 'ARG', 'CG', 'ARG', 10.54), ('NH2', 'ARG', 'CD', 'ARG', 9.59), ('NH2', 'ARG', 'NE', 'ARG', 8.27), ('NH2', 'ARG', 'CZ', 'ARG', 7.25), ('NH2', 'ARG', 'NH1', 'ARG', 7.58), ('NH2', 'ARG', 'NH2', 'ARG', 6.16)], [('CB', 'ARG', 'CB', 'ARG', 10.07), ('CB', 'ARG', 'CG', 'ARG', 10.33), ('CB', 'ARG', 'CD', 'ARG', 11.11), ('CB', 'ARG', 'NE', 'ARG', 11.1), ('CB', 'ARG', 'CZ', 'ARG', 11.56), ('CB', 'ARG', 'NH1', 'ARG', 12.05), ('CB', 'ARG', 'NH2', 'ARG', 11.73)], [('CG', 'ARG', 'CB', 'ARG', 9.03), ('CG', 'ARG', 'CG', 'ARG', 9.23), ('CG', 'ARG', 'CD', 'ARG', 9.84), ('CG', 'ARG', 'NE', 'ARG', 9.79), ('CG', 'ARG', 'CZ', 'ARG', 10.36), ('CG', 'ARG', 'NH1', 'ARG', 10.97), ('CG', 'ARG', 'NH2', 'ARG', 10.54)], [('CD', 'ARG', 'CB', 'ARG', 9.17), ('CD', 'ARG', 'CG', 'ARG', 9.04), ('CD', 'ARG', 'CD', 'ARG', 9.54), ('CD', 'ARG', 'NE', 'ARG', 9.22), ('CD', 'ARG', 'CZ', 'ARG', 9.62), ('CD', 'ARG', 'NH1', 'ARG', 10.31), ('CD', 'ARG', 'NH2', 'ARG', 9.59)], [('NE', 'ARG', 'CB', 'ARG', 8.27), ('NE', 'ARG', 'CG', 'ARG', 7.98), ('NE', 'ARG', 'CD', 'ARG', 8.29), ('NE', 'ARG', 'NE', 'ARG', 7.86), ('NE', 'ARG', 'CZ', 'ARG', 8.32), ('NE', 'ARG', 'NH1', 'ARG', 9.12), ('NE', 'ARG', 'NH2', 'ARG', 8.27)], [('CZ', 'ARG', 'CB', 'ARG', 8.35), ('CZ', 'ARG', 'CG', 'ARG', 7.74), ('CZ', 'ARG', 'CD', 'ARG', 7.96), ('CZ', 'ARG', 'NE', 'ARG', 7.26), ('CZ', 'ARG', 'CZ', 'ARG', 7.5), ('CZ', 'ARG', 'NH1', 'ARG', 8.33), ('CZ', 'ARG', 'NH2', 'ARG', 7.25)], [('NH1', 'ARG', 'CB', 'ARG', 9.24), ('NH1', 'ARG', 'CG', 'ARG', 8.52), ('NH1', 'ARG', 'CD', 'ARG', 8.85), ('NH1', 'ARG', 'NE', 'ARG', 8.05), ('NH1', 'ARG', 'CZ', 'ARG', 8.01), ('NH1', 'ARG', 'NH1', 'ARG', 8.72), ('NH1', 'ARG', 'NH2', 'ARG', 7.58)], [('NH2', 'ARG', 'CB', 'ARG', 7.9), ('NH2', 'ARG', 'CG', 'ARG', 7.11), ('NH2', 'ARG', 'CD', 'ARG', 7.05), ('NH2', 'ARG', 'NE', 'ARG', 6.18), ('NH2', 'ARG', 'CZ', 'ARG', 6.46), ('NH2', 'ARG', 'NH1', 'ARG', 7.46), ('NH2', 'ARG', 'NH2', 'ARG', 6.16)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_GLN, d, 'P_1vas_3_1_25_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_GLN, d, 'P_1vas_3_1_25_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_ARG, d, 'P_1vas_3_1_25_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ARG, d, 'P_1vas_3_1_25_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_GLN' :  match1,
		'ARG_GLN' :  match2,
		'THR_ARG' :  match3,
		'ARG_ARG' :  match4}