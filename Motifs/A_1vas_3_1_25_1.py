'''
FUNC:A_1vas_3_1_25_1
PDB:1vas
EC:3.1.25.1
RESI:thr,arg,gln,arg
LOCI:a-2,22,23,26;
'''
import motifFunctions as cmd
THR_ARG = { 
	'distances':
		[[7.12, 7.5, 6.53, 7.29, 7.09, 6.01, 8.24], [6.48, 6.65, 5.51, 6.3, 6.19, 5.21, 7.41], [6.43, 6.95, 6.3, 7.13, 7.12, 6.28, 8.29], [10.36, 10.73, 9.69, 10.18, 9.6, 8.33, 10.47], [9.4, 9.7, 8.68, 9.12, 8.57, 7.35, 9.46], [8.4, 8.53, 7.38, 7.78, 7.22, 5.96, 8.16], [9.25, 9.28, 7.97, 8.29, 7.6, 6.29, 8.45], [11.89, 11.38, 12.16, 11.57, 11.33, 11.65, 10.97], [11.61, 11.13, 11.75, 11.12, 11.02, 11.53, 10.63], [11.03, 10.68, 11.63, 11.23, 11.06, 11.26, 10.92], [13.91, 13.16, 13.95, 13.21, 12.6, 12.68, 12.07], [12.69, 11.97, 12.8, 12.12, 11.56, 11.64, 11.11], [11.95, 11.23, 11.94, 11.21, 10.77, 11.03, 10.28], [12.91, 12.1, 12.63, 11.74, 11.27, 11.66, 10.58]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ARG', 7.12), ('CB', 'THR', 'CG', 'ARG', 7.5), ('CB', 'THR', 'CD', 'ARG', 6.53), ('CB', 'THR', 'NE', 'ARG', 7.29), ('CB', 'THR', 'CZ', 'ARG', 7.09), ('CB', 'THR', 'NH1', 'ARG', 6.01), ('CB', 'THR', 'NH2', 'ARG', 8.24)], [('OG1', 'THR', 'CB', 'ARG', 6.48), ('OG1', 'THR', 'CG', 'ARG', 6.65), ('OG1', 'THR', 'CD', 'ARG', 5.51), ('OG1', 'THR', 'NE', 'ARG', 6.3), ('OG1', 'THR', 'CZ', 'ARG', 6.19), ('OG1', 'THR', 'NH1', 'ARG', 5.21), ('OG1', 'THR', 'NH2', 'ARG', 7.41)], [('CG2', 'THR', 'CB', 'ARG', 6.43), ('CG2', 'THR', 'CG', 'ARG', 6.95), ('CG2', 'THR', 'CD', 'ARG', 6.3), ('CG2', 'THR', 'NE', 'ARG', 7.13), ('CG2', 'THR', 'CZ', 'ARG', 7.12), ('CG2', 'THR', 'NH1', 'ARG', 6.28), ('CG2', 'THR', 'NH2', 'ARG', 8.29)], [('O', 'THR', 'CB', 'ARG', 10.36), ('O', 'THR', 'CG', 'ARG', 10.73), ('O', 'THR', 'CD', 'ARG', 9.69), ('O', 'THR', 'NE', 'ARG', 10.18), ('O', 'THR', 'CZ', 'ARG', 9.6), ('O', 'THR', 'NH1', 'ARG', 8.33), ('O', 'THR', 'NH2', 'ARG', 10.47)], [('C', 'THR', 'CB', 'ARG', 9.4), ('C', 'THR', 'CG', 'ARG', 9.7), ('C', 'THR', 'CD', 'ARG', 8.68), ('C', 'THR', 'NE', 'ARG', 9.12), ('C', 'THR', 'CZ', 'ARG', 8.57), ('C', 'THR', 'NH1', 'ARG', 7.35), ('C', 'THR', 'NH2', 'ARG', 9.46)], [('CA', 'THR', 'CB', 'ARG', 8.4), ('CA', 'THR', 'CG', 'ARG', 8.53), ('CA', 'THR', 'CD', 'ARG', 7.38), ('CA', 'THR', 'NE', 'ARG', 7.78), ('CA', 'THR', 'CZ', 'ARG', 7.22), ('CA', 'THR', 'NH1', 'ARG', 5.96), ('CA', 'THR', 'NH2', 'ARG', 8.16)], [('N', 'THR', 'CB', 'ARG', 9.25), ('N', 'THR', 'CG', 'ARG', 9.28), ('N', 'THR', 'CD', 'ARG', 7.97), ('N', 'THR', 'NE', 'ARG', 8.29), ('N', 'THR', 'CZ', 'ARG', 7.6), ('N', 'THR', 'NH1', 'ARG', 6.29), ('N', 'THR', 'NH2', 'ARG', 8.45)], [('CB', 'THR', 'CB', 'ARG', 11.89), ('CB', 'THR', 'CG', 'ARG', 11.38), ('CB', 'THR', 'CD', 'ARG', 12.16), ('CB', 'THR', 'NE', 'ARG', 11.57), ('CB', 'THR', 'CZ', 'ARG', 11.33), ('CB', 'THR', 'NH1', 'ARG', 11.65), ('CB', 'THR', 'NH2', 'ARG', 10.97)], [('OG1', 'THR', 'CB', 'ARG', 11.61), ('OG1', 'THR', 'CG', 'ARG', 11.13), ('OG1', 'THR', 'CD', 'ARG', 11.75), ('OG1', 'THR', 'NE', 'ARG', 11.12), ('OG1', 'THR', 'CZ', 'ARG', 11.02), ('OG1', 'THR', 'NH1', 'ARG', 11.53), ('OG1', 'THR', 'NH2', 'ARG', 10.63)], [('CG2', 'THR', 'CB', 'ARG', 11.03), ('CG2', 'THR', 'CG', 'ARG', 10.68), ('CG2', 'THR', 'CD', 'ARG', 11.63), ('CG2', 'THR', 'NE', 'ARG', 11.23), ('CG2', 'THR', 'CZ', 'ARG', 11.06), ('CG2', 'THR', 'NH1', 'ARG', 11.26), ('CG2', 'THR', 'NH2', 'ARG', 10.92)], [('O', 'THR', 'CB', 'ARG', 13.91), ('O', 'THR', 'CG', 'ARG', 13.16), ('O', 'THR', 'CD', 'ARG', 13.95), ('O', 'THR', 'NE', 'ARG', 13.21), ('O', 'THR', 'CZ', 'ARG', 12.6), ('O', 'THR', 'NH1', 'ARG', 12.68), ('O', 'THR', 'NH2', 'ARG', 12.07)], [('C', 'THR', 'CB', 'ARG', 12.69), ('C', 'THR', 'CG', 'ARG', 11.97), ('C', 'THR', 'CD', 'ARG', 12.8), ('C', 'THR', 'NE', 'ARG', 12.12), ('C', 'THR', 'CZ', 'ARG', 11.56), ('C', 'THR', 'NH1', 'ARG', 11.64), ('C', 'THR', 'NH2', 'ARG', 11.11)], [('CA', 'THR', 'CB', 'ARG', 11.95), ('CA', 'THR', 'CG', 'ARG', 11.23), ('CA', 'THR', 'CD', 'ARG', 11.94), ('CA', 'THR', 'NE', 'ARG', 11.21), ('CA', 'THR', 'CZ', 'ARG', 10.77), ('CA', 'THR', 'NH1', 'ARG', 11.03), ('CA', 'THR', 'NH2', 'ARG', 10.28)], [('N', 'THR', 'CB', 'ARG', 12.91), ('N', 'THR', 'CG', 'ARG', 12.1), ('N', 'THR', 'CD', 'ARG', 12.63), ('N', 'THR', 'NE', 'ARG', 11.74), ('N', 'THR', 'CZ', 'ARG', 11.27), ('N', 'THR', 'NH1', 'ARG', 11.66), ('N', 'THR', 'NH2', 'ARG', 10.58)]]}
GLN_ARG = { 
	'distances':
		[[7.52, 7.22, 6.75, 6.63, 6.39, 6.18, 6.93], [8.06, 7.45, 6.64, 6.13, 5.49, 5.25, 5.8], [9.22, 8.71, 7.71, 7.24, 6.34, 5.73, 6.55], [9.42, 9.16, 8.19, 7.98, 7.18, 6.35, 7.59], [10.14, 9.47, 8.38, 7.67, 6.59, 6.05, 6.47], [7.55, 7.11, 8.28, 8.15, 7.95, 7.84, 8.22], [7.46, 6.66, 7.56, 7.12, 6.79, 6.86, 6.86], [8.63, 7.63, 8.4, 7.74, 7.08, 7.03, 6.87], [9.62, 8.71, 9.58, 8.98, 8.28, 8.13, 8.05], [8.77, 7.56, 8.09, 7.22, 6.36, 6.36, 5.95]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ARG', 7.52), ('CB', 'GLN', 'CG', 'ARG', 7.22), ('CB', 'GLN', 'CD', 'ARG', 6.75), ('CB', 'GLN', 'NE', 'ARG', 6.63), ('CB', 'GLN', 'CZ', 'ARG', 6.39), ('CB', 'GLN', 'NH1', 'ARG', 6.18), ('CB', 'GLN', 'NH2', 'ARG', 6.93)], [('CG', 'GLN', 'CB', 'ARG', 8.06), ('CG', 'GLN', 'CG', 'ARG', 7.45), ('CG', 'GLN', 'CD', 'ARG', 6.64), ('CG', 'GLN', 'NE', 'ARG', 6.13), ('CG', 'GLN', 'CZ', 'ARG', 5.49), ('CG', 'GLN', 'NH1', 'ARG', 5.25), ('CG', 'GLN', 'NH2', 'ARG', 5.8)], [('CD', 'GLN', 'CB', 'ARG', 9.22), ('CD', 'GLN', 'CG', 'ARG', 8.71), ('CD', 'GLN', 'CD', 'ARG', 7.71), ('CD', 'GLN', 'NE', 'ARG', 7.24), ('CD', 'GLN', 'CZ', 'ARG', 6.34), ('CD', 'GLN', 'NH1', 'ARG', 5.73), ('CD', 'GLN', 'NH2', 'ARG', 6.55)], [('OE1', 'GLN', 'CB', 'ARG', 9.42), ('OE1', 'GLN', 'CG', 'ARG', 9.16), ('OE1', 'GLN', 'CD', 'ARG', 8.19), ('OE1', 'GLN', 'NE', 'ARG', 7.98), ('OE1', 'GLN', 'CZ', 'ARG', 7.18), ('OE1', 'GLN', 'NH1', 'ARG', 6.35), ('OE1', 'GLN', 'NH2', 'ARG', 7.59)], [('NE2', 'GLN', 'CB', 'ARG', 10.14), ('NE2', 'GLN', 'CG', 'ARG', 9.47), ('NE2', 'GLN', 'CD', 'ARG', 8.38), ('NE2', 'GLN', 'NE', 'ARG', 7.67), ('NE2', 'GLN', 'CZ', 'ARG', 6.59), ('NE2', 'GLN', 'NH1', 'ARG', 6.05), ('NE2', 'GLN', 'NH2', 'ARG', 6.47)], [('CB', 'GLN', 'CB', 'ARG', 7.55), ('CB', 'GLN', 'CG', 'ARG', 7.11), ('CB', 'GLN', 'CD', 'ARG', 8.28), ('CB', 'GLN', 'NE', 'ARG', 8.15), ('CB', 'GLN', 'CZ', 'ARG', 7.95), ('CB', 'GLN', 'NH1', 'ARG', 7.84), ('CB', 'GLN', 'NH2', 'ARG', 8.22)], [('CG', 'GLN', 'CB', 'ARG', 7.46), ('CG', 'GLN', 'CG', 'ARG', 6.66), ('CG', 'GLN', 'CD', 'ARG', 7.56), ('CG', 'GLN', 'NE', 'ARG', 7.12), ('CG', 'GLN', 'CZ', 'ARG', 6.79), ('CG', 'GLN', 'NH1', 'ARG', 6.86), ('CG', 'GLN', 'NH2', 'ARG', 6.86)], [('CD', 'GLN', 'CB', 'ARG', 8.63), ('CD', 'GLN', 'CG', 'ARG', 7.63), ('CD', 'GLN', 'CD', 'ARG', 8.4), ('CD', 'GLN', 'NE', 'ARG', 7.74), ('CD', 'GLN', 'CZ', 'ARG', 7.08), ('CD', 'GLN', 'NH1', 'ARG', 7.03), ('CD', 'GLN', 'NH2', 'ARG', 6.87)], [('OE1', 'GLN', 'CB', 'ARG', 9.62), ('OE1', 'GLN', 'CG', 'ARG', 8.71), ('OE1', 'GLN', 'CD', 'ARG', 9.58), ('OE1', 'GLN', 'NE', 'ARG', 8.98), ('OE1', 'GLN', 'CZ', 'ARG', 8.28), ('OE1', 'GLN', 'NH1', 'ARG', 8.13), ('OE1', 'GLN', 'NH2', 'ARG', 8.05)], [('NE2', 'GLN', 'CB', 'ARG', 8.77), ('NE2', 'GLN', 'CG', 'ARG', 7.56), ('NE2', 'GLN', 'CD', 'ARG', 8.09), ('NE2', 'GLN', 'NE', 'ARG', 7.22), ('NE2', 'GLN', 'CZ', 'ARG', 6.36), ('NE2', 'GLN', 'NH1', 'ARG', 6.36), ('NE2', 'GLN', 'NH2', 'ARG', 5.95)]]}
ARG_ARG = { 
	'distances':
		[[10.07, 10.33, 11.11, 11.1, 11.56, 12.05, 11.73], [9.03, 9.23, 9.84, 9.79, 10.36, 10.97, 10.54], [9.17, 9.04, 9.54, 9.22, 9.62, 10.31, 9.59], [8.27, 7.98, 8.29, 7.86, 8.32, 9.12, 8.27], [8.35, 7.74, 7.96, 7.26, 7.5, 8.33, 7.25], [9.24, 8.52, 8.85, 8.05, 8.01, 8.72, 7.58], [7.9, 7.11, 7.05, 6.18, 6.46, 7.46, 6.16], [10.07, 9.03, 9.17, 8.27, 8.35, 9.24, 7.9], [10.33, 9.23, 9.04, 7.98, 7.74, 8.52, 7.11], [11.11, 9.84, 9.54, 8.29, 7.96, 8.85, 7.05], [11.1, 9.79, 9.22, 7.86, 7.26, 8.05, 6.18], [11.56, 10.36, 9.62, 8.32, 7.5, 8.01, 6.46], [12.05, 10.97, 10.31, 9.12, 8.33, 8.72, 7.46], [11.73, 10.54, 9.59, 8.27, 7.25, 7.58, 6.16]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ARG', 10.07), ('CB', 'ARG', 'CG', 'ARG', 10.33), ('CB', 'ARG', 'CD', 'ARG', 11.11), ('CB', 'ARG', 'NE', 'ARG', 11.1), ('CB', 'ARG', 'CZ', 'ARG', 11.56), ('CB', 'ARG', 'NH1', 'ARG', 12.05), ('CB', 'ARG', 'NH2', 'ARG', 11.73)], [('CG', 'ARG', 'CB', 'ARG', 9.03), ('CG', 'ARG', 'CG', 'ARG', 9.23), ('CG', 'ARG', 'CD', 'ARG', 9.84), ('CG', 'ARG', 'NE', 'ARG', 9.79), ('CG', 'ARG', 'CZ', 'ARG', 10.36), ('CG', 'ARG', 'NH1', 'ARG', 10.97), ('CG', 'ARG', 'NH2', 'ARG', 10.54)], [('CD', 'ARG', 'CB', 'ARG', 9.17), ('CD', 'ARG', 'CG', 'ARG', 9.04), ('CD', 'ARG', 'CD', 'ARG', 9.54), ('CD', 'ARG', 'NE', 'ARG', 9.22), ('CD', 'ARG', 'CZ', 'ARG', 9.62), ('CD', 'ARG', 'NH1', 'ARG', 10.31), ('CD', 'ARG', 'NH2', 'ARG', 9.59)], [('NE', 'ARG', 'CB', 'ARG', 8.27), ('NE', 'ARG', 'CG', 'ARG', 7.98), ('NE', 'ARG', 'CD', 'ARG', 8.29), ('NE', 'ARG', 'NE', 'ARG', 7.86), ('NE', 'ARG', 'CZ', 'ARG', 8.32), ('NE', 'ARG', 'NH1', 'ARG', 9.12), ('NE', 'ARG', 'NH2', 'ARG', 8.27)], [('CZ', 'ARG', 'CB', 'ARG', 8.35), ('CZ', 'ARG', 'CG', 'ARG', 7.74), ('CZ', 'ARG', 'CD', 'ARG', 7.96), ('CZ', 'ARG', 'NE', 'ARG', 7.26), ('CZ', 'ARG', 'CZ', 'ARG', 7.5), ('CZ', 'ARG', 'NH1', 'ARG', 8.33), ('CZ', 'ARG', 'NH2', 'ARG', 7.25)], [('NH1', 'ARG', 'CB', 'ARG', 9.24), ('NH1', 'ARG', 'CG', 'ARG', 8.52), ('NH1', 'ARG', 'CD', 'ARG', 8.85), ('NH1', 'ARG', 'NE', 'ARG', 8.05), ('NH1', 'ARG', 'CZ', 'ARG', 8.01), ('NH1', 'ARG', 'NH1', 'ARG', 8.72), ('NH1', 'ARG', 'NH2', 'ARG', 7.58)], [('NH2', 'ARG', 'CB', 'ARG', 7.9), ('NH2', 'ARG', 'CG', 'ARG', 7.11), ('NH2', 'ARG', 'CD', 'ARG', 7.05), ('NH2', 'ARG', 'NE', 'ARG', 6.18), ('NH2', 'ARG', 'CZ', 'ARG', 6.46), ('NH2', 'ARG', 'NH1', 'ARG', 7.46), ('NH2', 'ARG', 'NH2', 'ARG', 6.16)], [('CB', 'ARG', 'CB', 'ARG', 10.07), ('CB', 'ARG', 'CG', 'ARG', 9.03), ('CB', 'ARG', 'CD', 'ARG', 9.17), ('CB', 'ARG', 'NE', 'ARG', 8.27), ('CB', 'ARG', 'CZ', 'ARG', 8.35), ('CB', 'ARG', 'NH1', 'ARG', 9.24), ('CB', 'ARG', 'NH2', 'ARG', 7.9)], [('CG', 'ARG', 'CB', 'ARG', 10.33), ('CG', 'ARG', 'CG', 'ARG', 9.23), ('CG', 'ARG', 'CD', 'ARG', 9.04), ('CG', 'ARG', 'NE', 'ARG', 7.98), ('CG', 'ARG', 'CZ', 'ARG', 7.74), ('CG', 'ARG', 'NH1', 'ARG', 8.52), ('CG', 'ARG', 'NH2', 'ARG', 7.11)], [('CD', 'ARG', 'CB', 'ARG', 11.11), ('CD', 'ARG', 'CG', 'ARG', 9.84), ('CD', 'ARG', 'CD', 'ARG', 9.54), ('CD', 'ARG', 'NE', 'ARG', 8.29), ('CD', 'ARG', 'CZ', 'ARG', 7.96), ('CD', 'ARG', 'NH1', 'ARG', 8.85), ('CD', 'ARG', 'NH2', 'ARG', 7.05)], [('NE', 'ARG', 'CB', 'ARG', 11.1), ('NE', 'ARG', 'CG', 'ARG', 9.79), ('NE', 'ARG', 'CD', 'ARG', 9.22), ('NE', 'ARG', 'NE', 'ARG', 7.86), ('NE', 'ARG', 'CZ', 'ARG', 7.26), ('NE', 'ARG', 'NH1', 'ARG', 8.05), ('NE', 'ARG', 'NH2', 'ARG', 6.18)], [('CZ', 'ARG', 'CB', 'ARG', 11.56), ('CZ', 'ARG', 'CG', 'ARG', 10.36), ('CZ', 'ARG', 'CD', 'ARG', 9.62), ('CZ', 'ARG', 'NE', 'ARG', 8.32), ('CZ', 'ARG', 'CZ', 'ARG', 7.5), ('CZ', 'ARG', 'NH1', 'ARG', 8.01), ('CZ', 'ARG', 'NH2', 'ARG', 6.46)], [('NH1', 'ARG', 'CB', 'ARG', 12.05), ('NH1', 'ARG', 'CG', 'ARG', 10.97), ('NH1', 'ARG', 'CD', 'ARG', 10.31), ('NH1', 'ARG', 'NE', 'ARG', 9.12), ('NH1', 'ARG', 'CZ', 'ARG', 8.33), ('NH1', 'ARG', 'NH1', 'ARG', 8.72), ('NH1', 'ARG', 'NH2', 'ARG', 7.46)], [('NH2', 'ARG', 'CB', 'ARG', 11.73), ('NH2', 'ARG', 'CG', 'ARG', 10.54), ('NH2', 'ARG', 'CD', 'ARG', 9.59), ('NH2', 'ARG', 'NE', 'ARG', 8.27), ('NH2', 'ARG', 'CZ', 'ARG', 7.25), ('NH2', 'ARG', 'NH1', 'ARG', 7.58), ('NH2', 'ARG', 'NH2', 'ARG', 6.16)]]}
GLN_THR = { 
	'distances':
		[[6.87, 7.19, 5.89, 8.53, 7.3, 6.85, 8.12], [6.96, 7.05, 6.4, 8.5, 7.31, 6.64, 7.65], [6.96, 7.28, 6.67, 7.72, 6.62, 6.18, 7.07], [6.47, 7.11, 6.18, 6.71, 5.65, 5.56, 6.59], [7.85, 8.03, 7.76, 8.37, 7.39, 6.9, 7.51]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'THR', 6.87), ('CB', 'GLN', 'OG1', 'THR', 7.19), ('CB', 'GLN', 'CG2', 'THR', 5.89), ('CB', 'GLN', 'O', 'THR', 8.53), ('CB', 'GLN', 'C', 'THR', 7.3), ('CB', 'GLN', 'CA', 'THR', 6.85), ('CB', 'GLN', 'N', 'THR', 8.12)], [('CG', 'GLN', 'CB', 'THR', 6.96), ('CG', 'GLN', 'OG1', 'THR', 7.05), ('CG', 'GLN', 'CG2', 'THR', 6.4), ('CG', 'GLN', 'O', 'THR', 8.5), ('CG', 'GLN', 'C', 'THR', 7.31), ('CG', 'GLN', 'CA', 'THR', 6.64), ('CG', 'GLN', 'N', 'THR', 7.65)], [('CD', 'GLN', 'CB', 'THR', 6.96), ('CD', 'GLN', 'OG1', 'THR', 7.28), ('CD', 'GLN', 'CG2', 'THR', 6.67), ('CD', 'GLN', 'O', 'THR', 7.72), ('CD', 'GLN', 'C', 'THR', 6.62), ('CD', 'GLN', 'CA', 'THR', 6.18), ('CD', 'GLN', 'N', 'THR', 7.07)], [('OE1', 'GLN', 'CB', 'THR', 6.47), ('OE1', 'GLN', 'OG1', 'THR', 7.11), ('OE1', 'GLN', 'CG2', 'THR', 6.18), ('OE1', 'GLN', 'O', 'THR', 6.71), ('OE1', 'GLN', 'C', 'THR', 5.65), ('OE1', 'GLN', 'CA', 'THR', 5.56), ('OE1', 'GLN', 'N', 'THR', 6.59)], [('NE2', 'GLN', 'CB', 'THR', 7.85), ('NE2', 'GLN', 'OG1', 'THR', 8.03), ('NE2', 'GLN', 'CG2', 'THR', 7.76), ('NE2', 'GLN', 'O', 'THR', 8.37), ('NE2', 'GLN', 'C', 'THR', 7.39), ('NE2', 'GLN', 'CA', 'THR', 6.9), ('NE2', 'GLN', 'N', 'THR', 7.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_ARG, d, 'A_1vas_3_1_25_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_ARG, d, 'A_1vas_3_1_25_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ARG, d, 'A_1vas_3_1_25_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_THR, d, 'A_1vas_3_1_25_1')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_ARG' :  match1,
		'GLN_ARG' :  match2,
		'ARG_ARG' :  match3,
		'GLN_THR' :  match4}