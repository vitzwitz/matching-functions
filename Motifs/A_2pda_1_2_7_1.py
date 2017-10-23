'''
FUNC:A_2pda_1_2_7_1
PDB:2pda
EC:1.2.7.1
RESI:thr,glu,arg,asn
LOCI:a-31,64,114,996;
'''
import motifFunctions as cmd
ARG_GLU = { 
	'distances':
		[[14.27, 13.62, 13.09, 12.38, 13.5, 16.38, 16.42, 15.76, 16.19], [14.43, 13.66, 12.99, 12.33, 13.25, 16.69, 16.61, 15.9, 16.17], [13.51, 12.74, 11.94, 11.22, 12.15, 15.94, 15.77, 14.95, 15.14], [13.63, 12.71, 11.83, 11.22, 11.87, 16.11, 15.84, 15.0, 15.05], [13.07, 12.13, 11.12, 10.52, 11.06, 15.68, 15.3, 14.39, 14.32], [12.31, 11.47, 10.39, 9.67, 10.41, 15.02, 14.63, 13.63, 13.56], [13.38, 12.32, 11.27, 10.8, 11.04, 15.98, 15.51, 14.62, 14.42], [14.93, 14.14, 13.87, 13.44, 14.22, 16.64, 16.76, 16.38, 16.86], [15.52, 14.75, 14.37, 13.85, 14.7, 17.38, 17.47, 16.99, 17.43], [15.32, 14.68, 14.27, 13.61, 14.69, 17.26, 17.38, 16.82, 17.31], [15.04, 14.51, 14.24, 13.58, 14.79, 16.79, 17.02, 16.54, 17.16]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 14.27), ('CB', 'ARG', 'CG', 'GLU', 13.62), ('CB', 'ARG', 'CD', 'GLU', 13.09), ('CB', 'ARG', 'OE1', 'GLU', 12.38), ('CB', 'ARG', 'OE2', 'GLU', 13.5), ('CB', 'ARG', 'O', 'GLU', 16.38), ('CB', 'ARG', 'C', 'GLU', 16.42), ('CB', 'ARG', 'CA', 'GLU', 15.76), ('CB', 'ARG', 'N', 'GLU', 16.19)], [('CG', 'ARG', 'CB', 'GLU', 14.43), ('CG', 'ARG', 'CG', 'GLU', 13.66), ('CG', 'ARG', 'CD', 'GLU', 12.99), ('CG', 'ARG', 'OE1', 'GLU', 12.33), ('CG', 'ARG', 'OE2', 'GLU', 13.25), ('CG', 'ARG', 'O', 'GLU', 16.69), ('CG', 'ARG', 'C', 'GLU', 16.61), ('CG', 'ARG', 'CA', 'GLU', 15.9), ('CG', 'ARG', 'N', 'GLU', 16.17)], [('CD', 'ARG', 'CB', 'GLU', 13.51), ('CD', 'ARG', 'CG', 'GLU', 12.74), ('CD', 'ARG', 'CD', 'GLU', 11.94), ('CD', 'ARG', 'OE1', 'GLU', 11.22), ('CD', 'ARG', 'OE2', 'GLU', 12.15), ('CD', 'ARG', 'O', 'GLU', 15.94), ('CD', 'ARG', 'C', 'GLU', 15.77), ('CD', 'ARG', 'CA', 'GLU', 14.95), ('CD', 'ARG', 'N', 'GLU', 15.14)], [('NE', 'ARG', 'CB', 'GLU', 13.63), ('NE', 'ARG', 'CG', 'GLU', 12.71), ('NE', 'ARG', 'CD', 'GLU', 11.83), ('NE', 'ARG', 'OE1', 'GLU', 11.22), ('NE', 'ARG', 'OE2', 'GLU', 11.87), ('NE', 'ARG', 'O', 'GLU', 16.11), ('NE', 'ARG', 'C', 'GLU', 15.84), ('NE', 'ARG', 'CA', 'GLU', 15.0), ('NE', 'ARG', 'N', 'GLU', 15.05)], [('CZ', 'ARG', 'CB', 'GLU', 13.07), ('CZ', 'ARG', 'CG', 'GLU', 12.13), ('CZ', 'ARG', 'CD', 'GLU', 11.12), ('CZ', 'ARG', 'OE1', 'GLU', 10.52), ('CZ', 'ARG', 'OE2', 'GLU', 11.06), ('CZ', 'ARG', 'O', 'GLU', 15.68), ('CZ', 'ARG', 'C', 'GLU', 15.3), ('CZ', 'ARG', 'CA', 'GLU', 14.39), ('CZ', 'ARG', 'N', 'GLU', 14.32)], [('NH1', 'ARG', 'CB', 'GLU', 12.31), ('NH1', 'ARG', 'CG', 'GLU', 11.47), ('NH1', 'ARG', 'CD', 'GLU', 10.39), ('NH1', 'ARG', 'OE1', 'GLU', 9.67), ('NH1', 'ARG', 'OE2', 'GLU', 10.41), ('NH1', 'ARG', 'O', 'GLU', 15.02), ('NH1', 'ARG', 'C', 'GLU', 14.63), ('NH1', 'ARG', 'CA', 'GLU', 13.63), ('NH1', 'ARG', 'N', 'GLU', 13.56)], [('NH2', 'ARG', 'CB', 'GLU', 13.38), ('NH2', 'ARG', 'CG', 'GLU', 12.32), ('NH2', 'ARG', 'CD', 'GLU', 11.27), ('NH2', 'ARG', 'OE1', 'GLU', 10.8), ('NH2', 'ARG', 'OE2', 'GLU', 11.04), ('NH2', 'ARG', 'O', 'GLU', 15.98), ('NH2', 'ARG', 'C', 'GLU', 15.51), ('NH2', 'ARG', 'CA', 'GLU', 14.62), ('NH2', 'ARG', 'N', 'GLU', 14.42)], [('O', 'ARG', 'CB', 'GLU', 14.93), ('O', 'ARG', 'CG', 'GLU', 14.14), ('O', 'ARG', 'CD', 'GLU', 13.87), ('O', 'ARG', 'OE1', 'GLU', 13.44), ('O', 'ARG', 'OE2', 'GLU', 14.22), ('O', 'ARG', 'O', 'GLU', 16.64), ('O', 'ARG', 'C', 'GLU', 16.76), ('O', 'ARG', 'CA', 'GLU', 16.38), ('O', 'ARG', 'N', 'GLU', 16.86)], [('C', 'ARG', 'CB', 'GLU', 15.52), ('C', 'ARG', 'CG', 'GLU', 14.75), ('C', 'ARG', 'CD', 'GLU', 14.37), ('C', 'ARG', 'OE1', 'GLU', 13.85), ('C', 'ARG', 'OE2', 'GLU', 14.7), ('C', 'ARG', 'O', 'GLU', 17.38), ('C', 'ARG', 'C', 'GLU', 17.47), ('C', 'ARG', 'CA', 'GLU', 16.99), ('C', 'ARG', 'N', 'GLU', 17.43)], [('CA', 'ARG', 'CB', 'GLU', 15.32), ('CA', 'ARG', 'CG', 'GLU', 14.68), ('CA', 'ARG', 'CD', 'GLU', 14.27), ('CA', 'ARG', 'OE1', 'GLU', 13.61), ('CA', 'ARG', 'OE2', 'GLU', 14.69), ('CA', 'ARG', 'O', 'GLU', 17.26), ('CA', 'ARG', 'C', 'GLU', 17.38), ('CA', 'ARG', 'CA', 'GLU', 16.82), ('CA', 'ARG', 'N', 'GLU', 17.31)], [('N', 'ARG', 'CB', 'GLU', 15.04), ('N', 'ARG', 'CG', 'GLU', 14.51), ('N', 'ARG', 'CD', 'GLU', 14.24), ('N', 'ARG', 'OE1', 'GLU', 13.58), ('N', 'ARG', 'OE2', 'GLU', 14.79), ('N', 'ARG', 'O', 'GLU', 16.79), ('N', 'ARG', 'C', 'GLU', 17.02), ('N', 'ARG', 'CA', 'GLU', 16.54), ('N', 'ARG', 'N', 'GLU', 17.16)]]}
ASN_GLU = { 
	'distances':
		[[17.48, 16.88, 15.38, 14.82, 14.83, 20.34, 19.45, 18.07, 17.23], [17.43, 16.76, 15.26, 14.67, 14.75, 20.34, 19.49, 18.14, 17.38], [18.46, 17.78, 16.29, 15.66, 15.81, 21.38, 20.57, 19.21, 18.5], [16.33, 15.6, 14.11, 13.54, 13.59, 19.24, 18.4, 17.08, 16.35], [17.88, 17.45, 15.97, 15.17, 15.69, 20.81, 20.07, 18.63, 18.03], [17.34, 16.92, 15.44, 14.69, 15.11, 20.24, 19.45, 18.0, 17.33], [18.02, 17.53, 16.04, 15.39, 15.59, 20.88, 20.01, 18.59, 17.8], [18.21, 17.79, 16.31, 15.71, 15.83, 21.01, 20.1, 18.66, 17.81]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 17.48), ('CB', 'ASN', 'CG', 'GLU', 16.88), ('CB', 'ASN', 'CD', 'GLU', 15.38), ('CB', 'ASN', 'OE1', 'GLU', 14.82), ('CB', 'ASN', 'OE2', 'GLU', 14.83), ('CB', 'ASN', 'O', 'GLU', 20.34), ('CB', 'ASN', 'C', 'GLU', 19.45), ('CB', 'ASN', 'CA', 'GLU', 18.07), ('CB', 'ASN', 'N', 'GLU', 17.23)], [('CG', 'ASN', 'CB', 'GLU', 17.43), ('CG', 'ASN', 'CG', 'GLU', 16.76), ('CG', 'ASN', 'CD', 'GLU', 15.26), ('CG', 'ASN', 'OE1', 'GLU', 14.67), ('CG', 'ASN', 'OE2', 'GLU', 14.75), ('CG', 'ASN', 'O', 'GLU', 20.34), ('CG', 'ASN', 'C', 'GLU', 19.49), ('CG', 'ASN', 'CA', 'GLU', 18.14), ('CG', 'ASN', 'N', 'GLU', 17.38)], [('OD1', 'ASN', 'CB', 'GLU', 18.46), ('OD1', 'ASN', 'CG', 'GLU', 17.78), ('OD1', 'ASN', 'CD', 'GLU', 16.29), ('OD1', 'ASN', 'OE1', 'GLU', 15.66), ('OD1', 'ASN', 'OE2', 'GLU', 15.81), ('OD1', 'ASN', 'O', 'GLU', 21.38), ('OD1', 'ASN', 'C', 'GLU', 20.57), ('OD1', 'ASN', 'CA', 'GLU', 19.21), ('OD1', 'ASN', 'N', 'GLU', 18.5)], [('ND2', 'ASN', 'CB', 'GLU', 16.33), ('ND2', 'ASN', 'CG', 'GLU', 15.6), ('ND2', 'ASN', 'CD', 'GLU', 14.11), ('ND2', 'ASN', 'OE1', 'GLU', 13.54), ('ND2', 'ASN', 'OE2', 'GLU', 13.59), ('ND2', 'ASN', 'O', 'GLU', 19.24), ('ND2', 'ASN', 'C', 'GLU', 18.4), ('ND2', 'ASN', 'CA', 'GLU', 17.08), ('ND2', 'ASN', 'N', 'GLU', 16.35)], [('O', 'ASN', 'CB', 'GLU', 17.88), ('O', 'ASN', 'CG', 'GLU', 17.45), ('O', 'ASN', 'CD', 'GLU', 15.97), ('O', 'ASN', 'OE1', 'GLU', 15.17), ('O', 'ASN', 'OE2', 'GLU', 15.69), ('O', 'ASN', 'O', 'GLU', 20.81), ('O', 'ASN', 'C', 'GLU', 20.07), ('O', 'ASN', 'CA', 'GLU', 18.63), ('O', 'ASN', 'N', 'GLU', 18.03)], [('C', 'ASN', 'CB', 'GLU', 17.34), ('C', 'ASN', 'CG', 'GLU', 16.92), ('C', 'ASN', 'CD', 'GLU', 15.44), ('C', 'ASN', 'OE1', 'GLU', 14.69), ('C', 'ASN', 'OE2', 'GLU', 15.11), ('C', 'ASN', 'O', 'GLU', 20.24), ('C', 'ASN', 'C', 'GLU', 19.45), ('C', 'ASN', 'CA', 'GLU', 18.0), ('C', 'ASN', 'N', 'GLU', 17.33)], [('CA', 'ASN', 'CB', 'GLU', 18.02), ('CA', 'ASN', 'CG', 'GLU', 17.53), ('CA', 'ASN', 'CD', 'GLU', 16.04), ('CA', 'ASN', 'OE1', 'GLU', 15.39), ('CA', 'ASN', 'OE2', 'GLU', 15.59), ('CA', 'ASN', 'O', 'GLU', 20.88), ('CA', 'ASN', 'C', 'GLU', 20.01), ('CA', 'ASN', 'CA', 'GLU', 18.59), ('CA', 'ASN', 'N', 'GLU', 17.8)], [('N', 'ASN', 'CB', 'GLU', 18.21), ('N', 'ASN', 'CG', 'GLU', 17.79), ('N', 'ASN', 'CD', 'GLU', 16.31), ('N', 'ASN', 'OE1', 'GLU', 15.71), ('N', 'ASN', 'OE2', 'GLU', 15.83), ('N', 'ASN', 'O', 'GLU', 21.01), ('N', 'ASN', 'C', 'GLU', 20.1), ('N', 'ASN', 'CA', 'GLU', 18.66), ('N', 'ASN', 'N', 'GLU', 17.81)]]}
ARG_ASN = { 
	'distances':
		[[16.98, 15.84, 16.04, 14.75, 16.02, 16.46, 17.55, 18.7], [15.96, 14.77, 14.94, 13.65, 15.16, 15.61, 16.61, 17.8], [14.58, 13.44, 13.68, 12.31, 13.84, 14.23, 15.23, 16.39], [13.85, 12.67, 12.94, 11.5, 13.41, 13.76, 14.62, 15.79], [12.66, 11.54, 11.89, 10.32, 12.4, 12.67, 13.49, 14.62], [12.08, 11.05, 11.47, 9.84, 11.67, 11.89, 12.8, 13.88], [12.27, 11.14, 11.51, 9.89, 12.37, 12.58, 13.23, 14.35], [19.19, 18.03, 18.28, 16.85, 18.6, 18.98, 19.93, 21.06], [18.71, 17.51, 17.68, 16.38, 17.98, 18.43, 19.41, 20.6], [18.4, 17.22, 17.37, 16.14, 17.42, 17.9, 18.98, 20.16], [19.36, 18.24, 18.44, 17.15, 18.31, 18.76, 19.88, 21.02]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASN', 16.98), ('CB', 'ARG', 'CG', 'ASN', 15.84), ('CB', 'ARG', 'OD1', 'ASN', 16.04), ('CB', 'ARG', 'ND2', 'ASN', 14.75), ('CB', 'ARG', 'O', 'ASN', 16.02), ('CB', 'ARG', 'C', 'ASN', 16.46), ('CB', 'ARG', 'CA', 'ASN', 17.55), ('CB', 'ARG', 'N', 'ASN', 18.7)], [('CG', 'ARG', 'CB', 'ASN', 15.96), ('CG', 'ARG', 'CG', 'ASN', 14.77), ('CG', 'ARG', 'OD1', 'ASN', 14.94), ('CG', 'ARG', 'ND2', 'ASN', 13.65), ('CG', 'ARG', 'O', 'ASN', 15.16), ('CG', 'ARG', 'C', 'ASN', 15.61), ('CG', 'ARG', 'CA', 'ASN', 16.61), ('CG', 'ARG', 'N', 'ASN', 17.8)], [('CD', 'ARG', 'CB', 'ASN', 14.58), ('CD', 'ARG', 'CG', 'ASN', 13.44), ('CD', 'ARG', 'OD1', 'ASN', 13.68), ('CD', 'ARG', 'ND2', 'ASN', 12.31), ('CD', 'ARG', 'O', 'ASN', 13.84), ('CD', 'ARG', 'C', 'ASN', 14.23), ('CD', 'ARG', 'CA', 'ASN', 15.23), ('CD', 'ARG', 'N', 'ASN', 16.39)], [('NE', 'ARG', 'CB', 'ASN', 13.85), ('NE', 'ARG', 'CG', 'ASN', 12.67), ('NE', 'ARG', 'OD1', 'ASN', 12.94), ('NE', 'ARG', 'ND2', 'ASN', 11.5), ('NE', 'ARG', 'O', 'ASN', 13.41), ('NE', 'ARG', 'C', 'ASN', 13.76), ('NE', 'ARG', 'CA', 'ASN', 14.62), ('NE', 'ARG', 'N', 'ASN', 15.79)], [('CZ', 'ARG', 'CB', 'ASN', 12.66), ('CZ', 'ARG', 'CG', 'ASN', 11.54), ('CZ', 'ARG', 'OD1', 'ASN', 11.89), ('CZ', 'ARG', 'ND2', 'ASN', 10.32), ('CZ', 'ARG', 'O', 'ASN', 12.4), ('CZ', 'ARG', 'C', 'ASN', 12.67), ('CZ', 'ARG', 'CA', 'ASN', 13.49), ('CZ', 'ARG', 'N', 'ASN', 14.62)], [('NH1', 'ARG', 'CB', 'ASN', 12.08), ('NH1', 'ARG', 'CG', 'ASN', 11.05), ('NH1', 'ARG', 'OD1', 'ASN', 11.47), ('NH1', 'ARG', 'ND2', 'ASN', 9.84), ('NH1', 'ARG', 'O', 'ASN', 11.67), ('NH1', 'ARG', 'C', 'ASN', 11.89), ('NH1', 'ARG', 'CA', 'ASN', 12.8), ('NH1', 'ARG', 'N', 'ASN', 13.88)], [('NH2', 'ARG', 'CB', 'ASN', 12.27), ('NH2', 'ARG', 'CG', 'ASN', 11.14), ('NH2', 'ARG', 'OD1', 'ASN', 11.51), ('NH2', 'ARG', 'ND2', 'ASN', 9.89), ('NH2', 'ARG', 'O', 'ASN', 12.37), ('NH2', 'ARG', 'C', 'ASN', 12.58), ('NH2', 'ARG', 'CA', 'ASN', 13.23), ('NH2', 'ARG', 'N', 'ASN', 14.35)], [('O', 'ARG', 'CB', 'ASN', 19.19), ('O', 'ARG', 'CG', 'ASN', 18.03), ('O', 'ARG', 'OD1', 'ASN', 18.28), ('O', 'ARG', 'ND2', 'ASN', 16.85), ('O', 'ARG', 'O', 'ASN', 18.6), ('O', 'ARG', 'C', 'ASN', 18.98), ('O', 'ARG', 'CA', 'ASN', 19.93), ('O', 'ARG', 'N', 'ASN', 21.06)], [('C', 'ARG', 'CB', 'ASN', 18.71), ('C', 'ARG', 'CG', 'ASN', 17.51), ('C', 'ARG', 'OD1', 'ASN', 17.68), ('C', 'ARG', 'ND2', 'ASN', 16.38), ('C', 'ARG', 'O', 'ASN', 17.98), ('C', 'ARG', 'C', 'ASN', 18.43), ('C', 'ARG', 'CA', 'ASN', 19.41), ('C', 'ARG', 'N', 'ASN', 20.6)], [('CA', 'ARG', 'CB', 'ASN', 18.4), ('CA', 'ARG', 'CG', 'ASN', 17.22), ('CA', 'ARG', 'OD1', 'ASN', 17.37), ('CA', 'ARG', 'ND2', 'ASN', 16.14), ('CA', 'ARG', 'O', 'ASN', 17.42), ('CA', 'ARG', 'C', 'ASN', 17.9), ('CA', 'ARG', 'CA', 'ASN', 18.98), ('CA', 'ARG', 'N', 'ASN', 20.16)], [('N', 'ARG', 'CB', 'ASN', 19.36), ('N', 'ARG', 'CG', 'ASN', 18.24), ('N', 'ARG', 'OD1', 'ASN', 18.44), ('N', 'ARG', 'ND2', 'ASN', 17.15), ('N', 'ARG', 'O', 'ASN', 18.31), ('N', 'ARG', 'C', 'ASN', 18.76), ('N', 'ARG', 'CA', 'ASN', 19.88), ('N', 'ARG', 'N', 'ASN', 21.02)]]}
THR_GLU = { 
	'distances':
		[[14.36, 13.9, 12.67, 11.65, 12.81, 17.22, 16.82, 15.56, 15.48], [14.53, 14.1, 12.78, 11.78, 12.83, 17.45, 16.96, 15.64, 15.43], [15.67, 15.24, 14.06, 13.01, 14.24, 18.49, 18.14, 16.91, 16.87], [12.54, 12.02, 11.01, 10.02, 11.31, 15.23, 14.99, 13.9, 14.03], [13.09, 12.69, 11.67, 10.61, 12.03, 15.8, 15.57, 14.43, 14.58], [13.21, 12.86, 11.72, 10.62, 12.01, 16.02, 15.69, 14.45, 14.48], [11.93, 11.57, 10.37, 9.28, 10.62, 14.79, 14.4, 13.12, 13.08]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLU', 14.36), ('CB', 'THR', 'CG', 'GLU', 13.9), ('CB', 'THR', 'CD', 'GLU', 12.67), ('CB', 'THR', 'OE1', 'GLU', 11.65), ('CB', 'THR', 'OE2', 'GLU', 12.81), ('CB', 'THR', 'O', 'GLU', 17.22), ('CB', 'THR', 'C', 'GLU', 16.82), ('CB', 'THR', 'CA', 'GLU', 15.56), ('CB', 'THR', 'N', 'GLU', 15.48)], [('OG1', 'THR', 'CB', 'GLU', 14.53), ('OG1', 'THR', 'CG', 'GLU', 14.1), ('OG1', 'THR', 'CD', 'GLU', 12.78), ('OG1', 'THR', 'OE1', 'GLU', 11.78), ('OG1', 'THR', 'OE2', 'GLU', 12.83), ('OG1', 'THR', 'O', 'GLU', 17.45), ('OG1', 'THR', 'C', 'GLU', 16.96), ('OG1', 'THR', 'CA', 'GLU', 15.64), ('OG1', 'THR', 'N', 'GLU', 15.43)], [('CG2', 'THR', 'CB', 'GLU', 15.67), ('CG2', 'THR', 'CG', 'GLU', 15.24), ('CG2', 'THR', 'CD', 'GLU', 14.06), ('CG2', 'THR', 'OE1', 'GLU', 13.01), ('CG2', 'THR', 'OE2', 'GLU', 14.24), ('CG2', 'THR', 'O', 'GLU', 18.49), ('CG2', 'THR', 'C', 'GLU', 18.14), ('CG2', 'THR', 'CA', 'GLU', 16.91), ('CG2', 'THR', 'N', 'GLU', 16.87)], [('O', 'THR', 'CB', 'GLU', 12.54), ('O', 'THR', 'CG', 'GLU', 12.02), ('O', 'THR', 'CD', 'GLU', 11.01), ('O', 'THR', 'OE1', 'GLU', 10.02), ('O', 'THR', 'OE2', 'GLU', 11.31), ('O', 'THR', 'O', 'GLU', 15.23), ('O', 'THR', 'C', 'GLU', 14.99), ('O', 'THR', 'CA', 'GLU', 13.9), ('O', 'THR', 'N', 'GLU', 14.03)], [('C', 'THR', 'CB', 'GLU', 13.09), ('C', 'THR', 'CG', 'GLU', 12.69), ('C', 'THR', 'CD', 'GLU', 11.67), ('C', 'THR', 'OE1', 'GLU', 10.61), ('C', 'THR', 'OE2', 'GLU', 12.03), ('C', 'THR', 'O', 'GLU', 15.8), ('C', 'THR', 'C', 'GLU', 15.57), ('C', 'THR', 'CA', 'GLU', 14.43), ('C', 'THR', 'N', 'GLU', 14.58)], [('CA', 'THR', 'CB', 'GLU', 13.21), ('CA', 'THR', 'CG', 'GLU', 12.86), ('CA', 'THR', 'CD', 'GLU', 11.72), ('CA', 'THR', 'OE1', 'GLU', 10.62), ('CA', 'THR', 'OE2', 'GLU', 12.01), ('CA', 'THR', 'O', 'GLU', 16.02), ('CA', 'THR', 'C', 'GLU', 15.69), ('CA', 'THR', 'CA', 'GLU', 14.45), ('CA', 'THR', 'N', 'GLU', 14.48)], [('N', 'THR', 'CB', 'GLU', 11.93), ('N', 'THR', 'CG', 'GLU', 11.57), ('N', 'THR', 'CD', 'GLU', 10.37), ('N', 'THR', 'OE1', 'GLU', 9.28), ('N', 'THR', 'OE2', 'GLU', 10.62), ('N', 'THR', 'O', 'GLU', 14.79), ('N', 'THR', 'C', 'GLU', 14.4), ('N', 'THR', 'CA', 'GLU', 13.12), ('N', 'THR', 'N', 'GLU', 13.08)]]}
ARG_THR = { 
	'distances':
		[[9.36, 10.72, 9.48, 6.69, 7.39, 8.9, 9.35], [8.79, 10.09, 8.97, 6.35, 7.2, 8.59, 9.01], [7.53, 8.77, 7.93, 5.04, 6.03, 7.32, 7.62], [7.68, 8.75, 8.22, 5.63, 6.71, 7.74, 7.87], [7.1, 7.98, 7.88, 5.4, 6.5, 7.25, 7.15], [6.16, 7.0, 7.14, 4.38, 5.49, 6.11, 5.87], [7.86, 8.52, 8.69, 6.58, 7.65, 8.19, 7.96], [12.22, 13.51, 12.45, 9.47, 10.34, 11.8, 12.04], [11.56, 12.89, 11.66, 8.99, 9.78, 11.25, 11.64], [10.77, 12.15, 10.76, 8.2, 8.83, 10.35, 10.86], [11.53, 12.92, 11.56, 8.81, 9.37, 10.9, 11.36]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'THR', 9.36), ('CB', 'ARG', 'OG1', 'THR', 10.72), ('CB', 'ARG', 'CG2', 'THR', 9.48), ('CB', 'ARG', 'O', 'THR', 6.69), ('CB', 'ARG', 'C', 'THR', 7.39), ('CB', 'ARG', 'CA', 'THR', 8.9), ('CB', 'ARG', 'N', 'THR', 9.35)], [('CG', 'ARG', 'CB', 'THR', 8.79), ('CG', 'ARG', 'OG1', 'THR', 10.09), ('CG', 'ARG', 'CG2', 'THR', 8.97), ('CG', 'ARG', 'O', 'THR', 6.35), ('CG', 'ARG', 'C', 'THR', 7.2), ('CG', 'ARG', 'CA', 'THR', 8.59), ('CG', 'ARG', 'N', 'THR', 9.01)], [('CD', 'ARG', 'CB', 'THR', 7.53), ('CD', 'ARG', 'OG1', 'THR', 8.77), ('CD', 'ARG', 'CG2', 'THR', 7.93), ('CD', 'ARG', 'O', 'THR', 5.04), ('CD', 'ARG', 'C', 'THR', 6.03), ('CD', 'ARG', 'CA', 'THR', 7.32), ('CD', 'ARG', 'N', 'THR', 7.62)], [('NE', 'ARG', 'CB', 'THR', 7.68), ('NE', 'ARG', 'OG1', 'THR', 8.75), ('NE', 'ARG', 'CG2', 'THR', 8.22), ('NE', 'ARG', 'O', 'THR', 5.63), ('NE', 'ARG', 'C', 'THR', 6.71), ('NE', 'ARG', 'CA', 'THR', 7.74), ('NE', 'ARG', 'N', 'THR', 7.87)], [('CZ', 'ARG', 'CB', 'THR', 7.1), ('CZ', 'ARG', 'OG1', 'THR', 7.98), ('CZ', 'ARG', 'CG2', 'THR', 7.88), ('CZ', 'ARG', 'O', 'THR', 5.4), ('CZ', 'ARG', 'C', 'THR', 6.5), ('CZ', 'ARG', 'CA', 'THR', 7.25), ('CZ', 'ARG', 'N', 'THR', 7.15)], [('NH1', 'ARG', 'CB', 'THR', 6.16), ('NH1', 'ARG', 'OG1', 'THR', 7.0), ('NH1', 'ARG', 'CG2', 'THR', 7.14), ('NH1', 'ARG', 'O', 'THR', 4.38), ('NH1', 'ARG', 'C', 'THR', 5.49), ('NH1', 'ARG', 'CA', 'THR', 6.11), ('NH1', 'ARG', 'N', 'THR', 5.87)], [('NH2', 'ARG', 'CB', 'THR', 7.86), ('NH2', 'ARG', 'OG1', 'THR', 8.52), ('NH2', 'ARG', 'CG2', 'THR', 8.69), ('NH2', 'ARG', 'O', 'THR', 6.58), ('NH2', 'ARG', 'C', 'THR', 7.65), ('NH2', 'ARG', 'CA', 'THR', 8.19), ('NH2', 'ARG', 'N', 'THR', 7.96)], [('O', 'ARG', 'CB', 'THR', 12.22), ('O', 'ARG', 'OG1', 'THR', 13.51), ('O', 'ARG', 'CG2', 'THR', 12.45), ('O', 'ARG', 'O', 'THR', 9.47), ('O', 'ARG', 'C', 'THR', 10.34), ('O', 'ARG', 'CA', 'THR', 11.8), ('O', 'ARG', 'N', 'THR', 12.04)], [('C', 'ARG', 'CB', 'THR', 11.56), ('C', 'ARG', 'OG1', 'THR', 12.89), ('C', 'ARG', 'CG2', 'THR', 11.66), ('C', 'ARG', 'O', 'THR', 8.99), ('C', 'ARG', 'C', 'THR', 9.78), ('C', 'ARG', 'CA', 'THR', 11.25), ('C', 'ARG', 'N', 'THR', 11.64)], [('CA', 'ARG', 'CB', 'THR', 10.77), ('CA', 'ARG', 'OG1', 'THR', 12.15), ('CA', 'ARG', 'CG2', 'THR', 10.76), ('CA', 'ARG', 'O', 'THR', 8.2), ('CA', 'ARG', 'C', 'THR', 8.83), ('CA', 'ARG', 'CA', 'THR', 10.35), ('CA', 'ARG', 'N', 'THR', 10.86)], [('N', 'ARG', 'CB', 'THR', 11.53), ('N', 'ARG', 'OG1', 'THR', 12.92), ('N', 'ARG', 'CG2', 'THR', 11.56), ('N', 'ARG', 'O', 'THR', 8.81), ('N', 'ARG', 'C', 'THR', 9.37), ('N', 'ARG', 'CA', 'THR', 10.9), ('N', 'ARG', 'N', 'THR', 11.36)]]}
THR_ASN = { 
	'distances':
		[[10.35, 9.37, 9.52, 8.6, 8.69, 9.21, 10.5, 11.66], [9.06, 8.18, 8.38, 7.51, 7.33, 7.8, 9.13, 10.25], [11.07, 10.01, 9.95, 9.4, 9.05, 9.76, 11.1, 12.32], [12.66, 11.7, 12.02, 10.67, 11.53, 11.86, 13.04, 14.11], [12.57, 11.64, 11.9, 10.73, 11.11, 11.51, 12.79, 13.85], [11.32, 10.49, 10.78, 9.67, 9.73, 10.1, 11.43, 12.45], [10.89, 10.2, 10.69, 9.28, 9.69, 9.84, 11.09, 11.99]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASN', 10.35), ('CB', 'THR', 'CG', 'ASN', 9.37), ('CB', 'THR', 'OD1', 'ASN', 9.52), ('CB', 'THR', 'ND2', 'ASN', 8.6), ('CB', 'THR', 'O', 'ASN', 8.69), ('CB', 'THR', 'C', 'ASN', 9.21), ('CB', 'THR', 'CA', 'ASN', 10.5), ('CB', 'THR', 'N', 'ASN', 11.66)], [('OG1', 'THR', 'CB', 'ASN', 9.06), ('OG1', 'THR', 'CG', 'ASN', 8.18), ('OG1', 'THR', 'OD1', 'ASN', 8.38), ('OG1', 'THR', 'ND2', 'ASN', 7.51), ('OG1', 'THR', 'O', 'ASN', 7.33), ('OG1', 'THR', 'C', 'ASN', 7.8), ('OG1', 'THR', 'CA', 'ASN', 9.13), ('OG1', 'THR', 'N', 'ASN', 10.25)], [('CG2', 'THR', 'CB', 'ASN', 11.07), ('CG2', 'THR', 'CG', 'ASN', 10.01), ('CG2', 'THR', 'OD1', 'ASN', 9.95), ('CG2', 'THR', 'ND2', 'ASN', 9.4), ('CG2', 'THR', 'O', 'ASN', 9.05), ('CG2', 'THR', 'C', 'ASN', 9.76), ('CG2', 'THR', 'CA', 'ASN', 11.1), ('CG2', 'THR', 'N', 'ASN', 12.32)], [('O', 'THR', 'CB', 'ASN', 12.66), ('O', 'THR', 'CG', 'ASN', 11.7), ('O', 'THR', 'OD1', 'ASN', 12.02), ('O', 'THR', 'ND2', 'ASN', 10.67), ('O', 'THR', 'O', 'ASN', 11.53), ('O', 'THR', 'C', 'ASN', 11.86), ('O', 'THR', 'CA', 'ASN', 13.04), ('O', 'THR', 'N', 'ASN', 14.11)], [('C', 'THR', 'CB', 'ASN', 12.57), ('C', 'THR', 'CG', 'ASN', 11.64), ('C', 'THR', 'OD1', 'ASN', 11.9), ('C', 'THR', 'ND2', 'ASN', 10.73), ('C', 'THR', 'O', 'ASN', 11.11), ('C', 'THR', 'C', 'ASN', 11.51), ('C', 'THR', 'CA', 'ASN', 12.79), ('C', 'THR', 'N', 'ASN', 13.85)], [('CA', 'THR', 'CB', 'ASN', 11.32), ('CA', 'THR', 'CG', 'ASN', 10.49), ('CA', 'THR', 'OD1', 'ASN', 10.78), ('CA', 'THR', 'ND2', 'ASN', 9.67), ('CA', 'THR', 'O', 'ASN', 9.73), ('CA', 'THR', 'C', 'ASN', 10.1), ('CA', 'THR', 'CA', 'ASN', 11.43), ('CA', 'THR', 'N', 'ASN', 12.45)], [('N', 'THR', 'CB', 'ASN', 10.89), ('N', 'THR', 'CG', 'ASN', 10.2), ('N', 'THR', 'OD1', 'ASN', 10.69), ('N', 'THR', 'ND2', 'ASN', 9.28), ('N', 'THR', 'O', 'ASN', 9.69), ('N', 'THR', 'C', 'ASN', 9.84), ('N', 'THR', 'CA', 'ASN', 11.09), ('N', 'THR', 'N', 'ASN', 11.99)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_GLU, d, 'A_2pda_1_2_7_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLU, d, 'A_2pda_1_2_7_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASN, d, 'A_2pda_1_2_7_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_GLU, d, 'A_2pda_1_2_7_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_THR, d, 'A_2pda_1_2_7_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_ASN, d, 'A_2pda_1_2_7_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_GLU' :  match1,
		'ASN_GLU' :  match2,
		'ARG_ASN' :  match3,
		'THR_GLU' :  match4,
		'ARG_THR' :  match5,
		'THR_ASN' :  match6}