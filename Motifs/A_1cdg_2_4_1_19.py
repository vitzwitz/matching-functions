'''
FUNC:A_1cdg_2_4_1_19
PDB:1cdg
EC:2.4.1.19
RESI:arg,asp,glu,his,asp
LOCI:a-227,229,257,327,328;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[7.38, 7.13, 6.67, 7.8], [6.9, 6.42, 6.13, 6.82], [7.16, 6.86, 6.91, 7.0], [6.64, 5.78, 5.37, 6.03], [7.07, 6.56, 6.75, 6.38], [6.76, 5.88, 5.86, 5.7], [12.66, 12.2, 11.1, 13.19], [11.33, 10.92, 9.82, 11.98], [11.29, 11.08, 10.02, 12.23], [10.19, 9.68, 8.53, 10.69], [10.14, 9.97, 8.92, 11.16], [9.37, 9.0, 7.88, 10.12]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.38), ('CB', 'HIS', 'CG', 'ASP', 7.13), ('CB', 'HIS', 'OD1', 'ASP', 6.67), ('CB', 'HIS', 'OD2', 'ASP', 7.8)], [('CG', 'HIS', 'CB', 'ASP', 6.9), ('CG', 'HIS', 'CG', 'ASP', 6.42), ('CG', 'HIS', 'OD1', 'ASP', 6.13), ('CG', 'HIS', 'OD2', 'ASP', 6.82)], [('ND1', 'HIS', 'CB', 'ASP', 7.16), ('ND1', 'HIS', 'CG', 'ASP', 6.86), ('ND1', 'HIS', 'OD1', 'ASP', 6.91), ('ND1', 'HIS', 'OD2', 'ASP', 7.0)], [('CD2', 'HIS', 'CB', 'ASP', 6.64), ('CD2', 'HIS', 'CG', 'ASP', 5.78), ('CD2', 'HIS', 'OD1', 'ASP', 5.37), ('CD2', 'HIS', 'OD2', 'ASP', 6.03)], [('CE1', 'HIS', 'CB', 'ASP', 7.07), ('CE1', 'HIS', 'CG', 'ASP', 6.56), ('CE1', 'HIS', 'OD1', 'ASP', 6.75), ('CE1', 'HIS', 'OD2', 'ASP', 6.38)], [('NE2', 'HIS', 'CB', 'ASP', 6.76), ('NE2', 'HIS', 'CG', 'ASP', 5.88), ('NE2', 'HIS', 'OD1', 'ASP', 5.86), ('NE2', 'HIS', 'OD2', 'ASP', 5.7)], [('CB', 'HIS', 'CB', 'ASP', 12.66), ('CB', 'HIS', 'CG', 'ASP', 12.2), ('CB', 'HIS', 'OD1', 'ASP', 11.1), ('CB', 'HIS', 'OD2', 'ASP', 13.19)], [('CG', 'HIS', 'CB', 'ASP', 11.33), ('CG', 'HIS', 'CG', 'ASP', 10.92), ('CG', 'HIS', 'OD1', 'ASP', 9.82), ('CG', 'HIS', 'OD2', 'ASP', 11.98)], [('ND1', 'HIS', 'CB', 'ASP', 11.29), ('ND1', 'HIS', 'CG', 'ASP', 11.08), ('ND1', 'HIS', 'OD1', 'ASP', 10.02), ('ND1', 'HIS', 'OD2', 'ASP', 12.23)], [('CD2', 'HIS', 'CB', 'ASP', 10.19), ('CD2', 'HIS', 'CG', 'ASP', 9.68), ('CD2', 'HIS', 'OD1', 'ASP', 8.53), ('CD2', 'HIS', 'OD2', 'ASP', 10.69)], [('CE1', 'HIS', 'CB', 'ASP', 10.14), ('CE1', 'HIS', 'CG', 'ASP', 9.97), ('CE1', 'HIS', 'OD1', 'ASP', 8.92), ('CE1', 'HIS', 'OD2', 'ASP', 11.16)], [('NE2', 'HIS', 'CB', 'ASP', 9.37), ('NE2', 'HIS', 'CG', 'ASP', 9.0), ('NE2', 'HIS', 'OD1', 'ASP', 7.88), ('NE2', 'HIS', 'OD2', 'ASP', 10.12)]]}
ASP_ARG = { 
	'distances':
		[[14.54, 13.32, 12.37, 11.75, 10.66, 9.98, 10.46], [13.82, 12.69, 11.63, 10.9, 9.72, 9.04, 9.42], [14.13, 13.11, 12.04, 11.16, 9.94, 9.39, 9.43], [13.01, 11.83, 10.71, 10.08, 8.9, 8.09, 8.77], [9.13, 9.02, 7.69, 7.04, 6.43, 6.39, 6.4], [10.37, 10.11, 8.72, 7.95, 7.06, 6.82, 6.83], [10.47, 10.02, 8.59, 7.75, 6.65, 6.27, 6.34], [11.47, 11.29, 9.91, 9.19, 8.35, 8.1, 8.1]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 14.54), ('CB', 'ASP', 'CG', 'ARG', 13.32), ('CB', 'ASP', 'CD', 'ARG', 12.37), ('CB', 'ASP', 'NE', 'ARG', 11.75), ('CB', 'ASP', 'CZ', 'ARG', 10.66), ('CB', 'ASP', 'NH1', 'ARG', 9.98), ('CB', 'ASP', 'NH2', 'ARG', 10.46)], [('CG', 'ASP', 'CB', 'ARG', 13.82), ('CG', 'ASP', 'CG', 'ARG', 12.69), ('CG', 'ASP', 'CD', 'ARG', 11.63), ('CG', 'ASP', 'NE', 'ARG', 10.9), ('CG', 'ASP', 'CZ', 'ARG', 9.72), ('CG', 'ASP', 'NH1', 'ARG', 9.04), ('CG', 'ASP', 'NH2', 'ARG', 9.42)], [('OD1', 'ASP', 'CB', 'ARG', 14.13), ('OD1', 'ASP', 'CG', 'ARG', 13.11), ('OD1', 'ASP', 'CD', 'ARG', 12.04), ('OD1', 'ASP', 'NE', 'ARG', 11.16), ('OD1', 'ASP', 'CZ', 'ARG', 9.94), ('OD1', 'ASP', 'NH1', 'ARG', 9.39), ('OD1', 'ASP', 'NH2', 'ARG', 9.43)], [('OD2', 'ASP', 'CB', 'ARG', 13.01), ('OD2', 'ASP', 'CG', 'ARG', 11.83), ('OD2', 'ASP', 'CD', 'ARG', 10.71), ('OD2', 'ASP', 'NE', 'ARG', 10.08), ('OD2', 'ASP', 'CZ', 'ARG', 8.9), ('OD2', 'ASP', 'NH1', 'ARG', 8.09), ('OD2', 'ASP', 'NH2', 'ARG', 8.77)], [('CB', 'ASP', 'CB', 'ARG', 9.13), ('CB', 'ASP', 'CG', 'ARG', 9.02), ('CB', 'ASP', 'CD', 'ARG', 7.69), ('CB', 'ASP', 'NE', 'ARG', 7.04), ('CB', 'ASP', 'CZ', 'ARG', 6.43), ('CB', 'ASP', 'NH1', 'ARG', 6.39), ('CB', 'ASP', 'NH2', 'ARG', 6.4)], [('CG', 'ASP', 'CB', 'ARG', 10.37), ('CG', 'ASP', 'CG', 'ARG', 10.11), ('CG', 'ASP', 'CD', 'ARG', 8.72), ('CG', 'ASP', 'NE', 'ARG', 7.95), ('CG', 'ASP', 'CZ', 'ARG', 7.06), ('CG', 'ASP', 'NH1', 'ARG', 6.82), ('CG', 'ASP', 'NH2', 'ARG', 6.83)], [('OD1', 'ASP', 'CB', 'ARG', 10.47), ('OD1', 'ASP', 'CG', 'ARG', 10.02), ('OD1', 'ASP', 'CD', 'ARG', 8.59), ('OD1', 'ASP', 'NE', 'ARG', 7.75), ('OD1', 'ASP', 'CZ', 'ARG', 6.65), ('OD1', 'ASP', 'NH1', 'ARG', 6.27), ('OD1', 'ASP', 'NH2', 'ARG', 6.34)], [('OD2', 'ASP', 'CB', 'ARG', 11.47), ('OD2', 'ASP', 'CG', 'ARG', 11.29), ('OD2', 'ASP', 'CD', 'ARG', 9.91), ('OD2', 'ASP', 'NE', 'ARG', 9.19), ('OD2', 'ASP', 'CZ', 'ARG', 8.35), ('OD2', 'ASP', 'NH1', 'ARG', 8.1), ('OD2', 'ASP', 'NH2', 'ARG', 8.1)]]}
ASP_GLU = { 
	'distances':
		[[9.86, 8.61, 7.33, 7.51, 6.32], [9.15, 7.99, 6.62, 6.63, 5.81], [9.86, 8.83, 7.42, 7.22, 6.8], [7.93, 6.74, 5.4, 5.53, 4.59], [7.78, 8.68, 8.68, 7.94, 9.79], [7.93, 8.51, 8.36, 7.69, 9.33], [7.38, 7.72, 7.36, 6.67, 8.25], [8.94, 9.46, 9.38, 8.82, 10.28]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 9.86), ('CB', 'ASP', 'CG', 'GLU', 8.61), ('CB', 'ASP', 'CD', 'GLU', 7.33), ('CB', 'ASP', 'OE1', 'GLU', 7.51), ('CB', 'ASP', 'OE2', 'GLU', 6.32)], [('CG', 'ASP', 'CB', 'GLU', 9.15), ('CG', 'ASP', 'CG', 'GLU', 7.99), ('CG', 'ASP', 'CD', 'GLU', 6.62), ('CG', 'ASP', 'OE1', 'GLU', 6.63), ('CG', 'ASP', 'OE2', 'GLU', 5.81)], [('OD1', 'ASP', 'CB', 'GLU', 9.86), ('OD1', 'ASP', 'CG', 'GLU', 8.83), ('OD1', 'ASP', 'CD', 'GLU', 7.42), ('OD1', 'ASP', 'OE1', 'GLU', 7.22), ('OD1', 'ASP', 'OE2', 'GLU', 6.8)], [('OD2', 'ASP', 'CB', 'GLU', 7.93), ('OD2', 'ASP', 'CG', 'GLU', 6.74), ('OD2', 'ASP', 'CD', 'GLU', 5.4), ('OD2', 'ASP', 'OE1', 'GLU', 5.53), ('OD2', 'ASP', 'OE2', 'GLU', 4.59)], [('CB', 'ASP', 'CB', 'GLU', 7.78), ('CB', 'ASP', 'CG', 'GLU', 8.68), ('CB', 'ASP', 'CD', 'GLU', 8.68), ('CB', 'ASP', 'OE1', 'GLU', 7.94), ('CB', 'ASP', 'OE2', 'GLU', 9.79)], [('CG', 'ASP', 'CB', 'GLU', 7.93), ('CG', 'ASP', 'CG', 'GLU', 8.51), ('CG', 'ASP', 'CD', 'GLU', 8.36), ('CG', 'ASP', 'OE1', 'GLU', 7.69), ('CG', 'ASP', 'OE2', 'GLU', 9.33)], [('OD1', 'ASP', 'CB', 'GLU', 7.38), ('OD1', 'ASP', 'CG', 'GLU', 7.72), ('OD1', 'ASP', 'CD', 'GLU', 7.36), ('OD1', 'ASP', 'OE1', 'GLU', 6.67), ('OD1', 'ASP', 'OE2', 'GLU', 8.25)], [('OD2', 'ASP', 'CB', 'GLU', 8.94), ('OD2', 'ASP', 'CG', 'GLU', 9.46), ('OD2', 'ASP', 'CD', 'GLU', 9.38), ('OD2', 'ASP', 'OE1', 'GLU', 8.82), ('OD2', 'ASP', 'OE2', 'GLU', 10.28)]]}
GLU_ARG = { 
	'distances':
		[[9.26, 8.05, 6.72, 6.97, 6.36, 5.11, 7.33], [10.53, 9.25, 7.96, 8.04, 7.23, 5.95, 7.99], [10.58, 9.32, 8.06, 7.83, 6.83, 5.66, 7.32], [9.76, 8.58, 7.32, 6.86, 5.76, 4.7, 6.11], [11.68, 10.37, 9.19, 8.94, 7.93, 6.82, 8.3]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 9.26), ('CB', 'GLU', 'CG', 'ARG', 8.05), ('CB', 'GLU', 'CD', 'ARG', 6.72), ('CB', 'GLU', 'NE', 'ARG', 6.97), ('CB', 'GLU', 'CZ', 'ARG', 6.36), ('CB', 'GLU', 'NH1', 'ARG', 5.11), ('CB', 'GLU', 'NH2', 'ARG', 7.33)], [('CG', 'GLU', 'CB', 'ARG', 10.53), ('CG', 'GLU', 'CG', 'ARG', 9.25), ('CG', 'GLU', 'CD', 'ARG', 7.96), ('CG', 'GLU', 'NE', 'ARG', 8.04), ('CG', 'GLU', 'CZ', 'ARG', 7.23), ('CG', 'GLU', 'NH1', 'ARG', 5.95), ('CG', 'GLU', 'NH2', 'ARG', 7.99)], [('CD', 'GLU', 'CB', 'ARG', 10.58), ('CD', 'GLU', 'CG', 'ARG', 9.32), ('CD', 'GLU', 'CD', 'ARG', 8.06), ('CD', 'GLU', 'NE', 'ARG', 7.83), ('CD', 'GLU', 'CZ', 'ARG', 6.83), ('CD', 'GLU', 'NH1', 'ARG', 5.66), ('CD', 'GLU', 'NH2', 'ARG', 7.32)], [('OE1', 'GLU', 'CB', 'ARG', 9.76), ('OE1', 'GLU', 'CG', 'ARG', 8.58), ('OE1', 'GLU', 'CD', 'ARG', 7.32), ('OE1', 'GLU', 'NE', 'ARG', 6.86), ('OE1', 'GLU', 'CZ', 'ARG', 5.76), ('OE1', 'GLU', 'NH1', 'ARG', 4.7), ('OE1', 'GLU', 'NH2', 'ARG', 6.11)], [('OE2', 'GLU', 'CB', 'ARG', 11.68), ('OE2', 'GLU', 'CG', 'ARG', 10.37), ('OE2', 'GLU', 'CD', 'ARG', 9.19), ('OE2', 'GLU', 'NE', 'ARG', 8.94), ('OE2', 'GLU', 'CZ', 'ARG', 7.93), ('OE2', 'GLU', 'NH1', 'ARG', 6.82), ('OE2', 'GLU', 'NH2', 'ARG', 8.3)]]}
HIS_ARG = { 
	'distances':
		[[13.19, 12.42, 11.88, 10.81, 9.96, 10.1, 9.16], [11.92, 11.09, 10.47, 9.42, 8.52, 8.6, 7.78], [11.01, 10.1, 9.6, 8.67, 7.93, 8.03, 7.4], [11.65, 10.83, 10.01, 8.91, 7.85, 7.82, 7.06], [10.12, 9.13, 8.48, 7.58, 6.74, 6.73, 6.34], [10.52, 9.6, 8.73, 7.72, 6.65, 6.53, 6.06]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ARG', 13.19), ('CB', 'HIS', 'CG', 'ARG', 12.42), ('CB', 'HIS', 'CD', 'ARG', 11.88), ('CB', 'HIS', 'NE', 'ARG', 10.81), ('CB', 'HIS', 'CZ', 'ARG', 9.96), ('CB', 'HIS', 'NH1', 'ARG', 10.1), ('CB', 'HIS', 'NH2', 'ARG', 9.16)], [('CG', 'HIS', 'CB', 'ARG', 11.92), ('CG', 'HIS', 'CG', 'ARG', 11.09), ('CG', 'HIS', 'CD', 'ARG', 10.47), ('CG', 'HIS', 'NE', 'ARG', 9.42), ('CG', 'HIS', 'CZ', 'ARG', 8.52), ('CG', 'HIS', 'NH1', 'ARG', 8.6), ('CG', 'HIS', 'NH2', 'ARG', 7.78)], [('ND1', 'HIS', 'CB', 'ARG', 11.01), ('ND1', 'HIS', 'CG', 'ARG', 10.1), ('ND1', 'HIS', 'CD', 'ARG', 9.6), ('ND1', 'HIS', 'NE', 'ARG', 8.67), ('ND1', 'HIS', 'CZ', 'ARG', 7.93), ('ND1', 'HIS', 'NH1', 'ARG', 8.03), ('ND1', 'HIS', 'NH2', 'ARG', 7.4)], [('CD2', 'HIS', 'CB', 'ARG', 11.65), ('CD2', 'HIS', 'CG', 'ARG', 10.83), ('CD2', 'HIS', 'CD', 'ARG', 10.01), ('CD2', 'HIS', 'NE', 'ARG', 8.91), ('CD2', 'HIS', 'CZ', 'ARG', 7.85), ('CD2', 'HIS', 'NH1', 'ARG', 7.82), ('CD2', 'HIS', 'NH2', 'ARG', 7.06)], [('CE1', 'HIS', 'CB', 'ARG', 10.12), ('CE1', 'HIS', 'CG', 'ARG', 9.13), ('CE1', 'HIS', 'CD', 'ARG', 8.48), ('CE1', 'HIS', 'NE', 'ARG', 7.58), ('CE1', 'HIS', 'CZ', 'ARG', 6.74), ('CE1', 'HIS', 'NH1', 'ARG', 6.73), ('CE1', 'HIS', 'NH2', 'ARG', 6.34)], [('NE2', 'HIS', 'CB', 'ARG', 10.52), ('NE2', 'HIS', 'CG', 'ARG', 9.6), ('NE2', 'HIS', 'CD', 'ARG', 8.73), ('NE2', 'HIS', 'NE', 'ARG', 7.72), ('NE2', 'HIS', 'CZ', 'ARG', 6.65), ('NE2', 'HIS', 'NH1', 'ARG', 6.53), ('NE2', 'HIS', 'NH2', 'ARG', 6.06)]]}
ARG_ASPI = { 
	'distances':
		[[9.13, 10.37, 10.47, 11.47], [9.02, 10.11, 10.02, 11.29], [7.69, 8.72, 8.59, 9.91], [7.04, 7.95, 7.75, 9.19], [6.43, 7.06, 6.65, 8.35], [6.39, 6.82, 6.27, 8.1], [6.4, 6.83, 6.34, 8.1]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASPI', 9.13), ('CB', 'ARG', 'CG', 'ASPI', 10.37), ('CB', 'ARG', 'OD1', 'ASPI', 10.47), ('CB', 'ARG', 'OD2', 'ASPI', 11.47)], [('CG', 'ARG', 'CB', 'ASPI', 9.02), ('CG', 'ARG', 'CG', 'ASPI', 10.11), ('CG', 'ARG', 'OD1', 'ASPI', 10.02), ('CG', 'ARG', 'OD2', 'ASPI', 11.29)], [('CD', 'ARG', 'CB', 'ASPI', 7.69), ('CD', 'ARG', 'CG', 'ASPI', 8.72), ('CD', 'ARG', 'OD1', 'ASPI', 8.59), ('CD', 'ARG', 'OD2', 'ASPI', 9.91)], [('NE', 'ARG', 'CB', 'ASPI', 7.04), ('NE', 'ARG', 'CG', 'ASPI', 7.95), ('NE', 'ARG', 'OD1', 'ASPI', 7.75), ('NE', 'ARG', 'OD2', 'ASPI', 9.19)], [('CZ', 'ARG', 'CB', 'ASPI', 6.43), ('CZ', 'ARG', 'CG', 'ASPI', 7.06), ('CZ', 'ARG', 'OD1', 'ASPI', 6.65), ('CZ', 'ARG', 'OD2', 'ASPI', 8.35)], [('NH1', 'ARG', 'CB', 'ASPI', 6.39), ('NH1', 'ARG', 'CG', 'ASPI', 6.82), ('NH1', 'ARG', 'OD1', 'ASPI', 6.27), ('NH1', 'ARG', 'OD2', 'ASPI', 8.1)], [('NH2', 'ARG', 'CB', 'ASPI', 6.4), ('NH2', 'ARG', 'CG', 'ASPI', 6.83), ('NH2', 'ARG', 'OD1', 'ASPI', 6.34), ('NH2', 'ARG', 'OD2', 'ASPI', 8.1)]]}
HIS_GLU = { 
	'distances':
		[[11.84, 11.3, 9.83, 9.07, 9.59], [10.37, 9.89, 8.45, 7.62, 8.33], [9.78, 9.4, 8.04, 7.22, 8.01], [9.53, 9.05, 7.6, 6.72, 7.57], [8.47, 8.17, 6.84, 5.94, 6.97], [8.25, 7.87, 6.47, 5.5, 6.63]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 11.84), ('CB', 'HIS', 'CG', 'GLU', 11.3), ('CB', 'HIS', 'CD', 'GLU', 9.83), ('CB', 'HIS', 'OE1', 'GLU', 9.07), ('CB', 'HIS', 'OE2', 'GLU', 9.59)], [('CG', 'HIS', 'CB', 'GLU', 10.37), ('CG', 'HIS', 'CG', 'GLU', 9.89), ('CG', 'HIS', 'CD', 'GLU', 8.45), ('CG', 'HIS', 'OE1', 'GLU', 7.62), ('CG', 'HIS', 'OE2', 'GLU', 8.33)], [('ND1', 'HIS', 'CB', 'GLU', 9.78), ('ND1', 'HIS', 'CG', 'GLU', 9.4), ('ND1', 'HIS', 'CD', 'GLU', 8.04), ('ND1', 'HIS', 'OE1', 'GLU', 7.22), ('ND1', 'HIS', 'OE2', 'GLU', 8.01)], [('CD2', 'HIS', 'CB', 'GLU', 9.53), ('CD2', 'HIS', 'CG', 'GLU', 9.05), ('CD2', 'HIS', 'CD', 'GLU', 7.6), ('CD2', 'HIS', 'OE1', 'GLU', 6.72), ('CD2', 'HIS', 'OE2', 'GLU', 7.57)], [('CE1', 'HIS', 'CB', 'GLU', 8.47), ('CE1', 'HIS', 'CG', 'GLU', 8.17), ('CE1', 'HIS', 'CD', 'GLU', 6.84), ('CE1', 'HIS', 'OE1', 'GLU', 5.94), ('CE1', 'HIS', 'OE2', 'GLU', 6.97)], [('NE2', 'HIS', 'CB', 'GLU', 8.25), ('NE2', 'HIS', 'CG', 'GLU', 7.87), ('NE2', 'HIS', 'CD', 'GLU', 6.47), ('NE2', 'HIS', 'OE1', 'GLU', 5.5), ('NE2', 'HIS', 'OE2', 'GLU', 6.63)]]}
ASP_ASP = { 
	'distances':
		[[12.75, 11.99, 10.72, 12.85], [11.44, 10.61, 9.33, 11.44], [11.36, 10.43, 9.15, 11.18], [10.6, 9.84, 8.59, 10.71], [12.75, 11.44, 11.36, 10.6], [11.99, 10.61, 10.43, 9.84], [10.72, 9.33, 9.15, 8.59], [12.85, 11.44, 11.18, 10.71]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 12.75), ('CB', 'ASP', 'CG', 'ASP', 11.99), ('CB', 'ASP', 'OD1', 'ASP', 10.72), ('CB', 'ASP', 'OD2', 'ASP', 12.85)], [('CG', 'ASP', 'CB', 'ASP', 11.44), ('CG', 'ASP', 'CG', 'ASP', 10.61), ('CG', 'ASP', 'OD1', 'ASP', 9.33), ('CG', 'ASP', 'OD2', 'ASP', 11.44)], [('OD1', 'ASP', 'CB', 'ASP', 11.36), ('OD1', 'ASP', 'CG', 'ASP', 10.43), ('OD1', 'ASP', 'OD1', 'ASP', 9.15), ('OD1', 'ASP', 'OD2', 'ASP', 11.18)], [('OD2', 'ASP', 'CB', 'ASP', 10.6), ('OD2', 'ASP', 'CG', 'ASP', 9.84), ('OD2', 'ASP', 'OD1', 'ASP', 8.59), ('OD2', 'ASP', 'OD2', 'ASP', 10.71)], [('CB', 'ASP', 'CB', 'ASP', 12.75), ('CB', 'ASP', 'CG', 'ASP', 11.44), ('CB', 'ASP', 'OD1', 'ASP', 11.36), ('CB', 'ASP', 'OD2', 'ASP', 10.6)], [('CG', 'ASP', 'CB', 'ASP', 11.99), ('CG', 'ASP', 'CG', 'ASP', 10.61), ('CG', 'ASP', 'OD1', 'ASP', 10.43), ('CG', 'ASP', 'OD2', 'ASP', 9.84)], [('OD1', 'ASP', 'CB', 'ASP', 10.72), ('OD1', 'ASP', 'CG', 'ASP', 9.33), ('OD1', 'ASP', 'OD1', 'ASP', 9.15), ('OD1', 'ASP', 'OD2', 'ASP', 8.59)], [('OD2', 'ASP', 'CB', 'ASP', 12.85), ('OD2', 'ASP', 'CG', 'ASP', 11.44), ('OD2', 'ASP', 'OD1', 'ASP', 11.18), ('OD2', 'ASP', 'OD2', 'ASP', 10.71)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_1cdg_2_4_1_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ARG, d, 'A_1cdg_2_4_1_19')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'A_1cdg_2_4_1_19')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ARG, d, 'A_1cdg_2_4_1_19')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_ARG, d, 'A_1cdg_2_4_1_19')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_ASPI, d, 'A_1cdg_2_4_1_19')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_GLU, d, 'A_1cdg_2_4_1_19')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_ASP, d, 'A_1cdg_2_4_1_19')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'ASP_ARG' :  match2,
		'ASP_GLU' :  match3,
		'GLU_ARG' :  match4,
		'HIS_ARG' :  match5,
		'ARG_ASPI' :  match6,
		'HIS_GLU' :  match7,
		'ASP_ASP' :  match8}