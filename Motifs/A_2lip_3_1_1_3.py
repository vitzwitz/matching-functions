'''
FUNC:A_2lip_3_1_1_3
PDB:2lip
EC:3.1.1.3
RESI:leu,ser,gln,asp,his
LOCI:a-17,87,88,264,286;
'''
import motifFunctions as cmd
HIS_ASP = { 
	'distances':
		[[6.45, 5.68, 5.65, 5.7], [7.1, 5.97, 5.86, 5.63], [6.75, 5.4, 5.38, 4.8], [8.45, 7.26, 7.07, 6.84], [7.99, 6.58, 6.49, 5.86], [8.92, 7.58, 7.39, 6.96]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.45), ('CB', 'HIS', 'CG', 'ASP', 5.68), ('CB', 'HIS', 'OD1', 'ASP', 5.65), ('CB', 'HIS', 'OD2', 'ASP', 5.7)], [('CG', 'HIS', 'CB', 'ASP', 7.1), ('CG', 'HIS', 'CG', 'ASP', 5.97), ('CG', 'HIS', 'OD1', 'ASP', 5.86), ('CG', 'HIS', 'OD2', 'ASP', 5.63)], [('ND1', 'HIS', 'CB', 'ASP', 6.75), ('ND1', 'HIS', 'CG', 'ASP', 5.4), ('ND1', 'HIS', 'OD1', 'ASP', 5.38), ('ND1', 'HIS', 'OD2', 'ASP', 4.8)], [('CD2', 'HIS', 'CB', 'ASP', 8.45), ('CD2', 'HIS', 'CG', 'ASP', 7.26), ('CD2', 'HIS', 'OD1', 'ASP', 7.07), ('CD2', 'HIS', 'OD2', 'ASP', 6.84)], [('CE1', 'HIS', 'CB', 'ASP', 7.99), ('CE1', 'HIS', 'CG', 'ASP', 6.58), ('CE1', 'HIS', 'OD1', 'ASP', 6.49), ('CE1', 'HIS', 'OD2', 'ASP', 5.86)], [('NE2', 'HIS', 'CB', 'ASP', 8.92), ('NE2', 'HIS', 'CG', 'ASP', 7.58), ('NE2', 'HIS', 'OD1', 'ASP', 7.39), ('NE2', 'HIS', 'OD2', 'ASP', 6.96)]]}
SER_GLN = { 
	'distances':
		[[6.85, 8.34, 9.29, 10.49, 8.98, 8.17, 6.97, 6.2, 4.76], [6.41, 7.83, 8.66, 9.88, 8.24, 8.38, 7.24, 6.11, 4.81]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLN', 6.85), ('CB', 'SER', 'CG', 'GLN', 8.34), ('CB', 'SER', 'CD', 'GLN', 9.29), ('CB', 'SER', 'OE1', 'GLN', 10.49), ('CB', 'SER', 'NE2', 'GLN', 8.98), ('CB', 'SER', 'O', 'GLN', 8.17), ('CB', 'SER', 'C', 'GLN', 6.97), ('CB', 'SER', 'CA', 'GLN', 6.2), ('CB', 'SER', 'N', 'GLN', 4.76)], [('OG', 'SER', 'CB', 'GLN', 6.41), ('OG', 'SER', 'CG', 'GLN', 7.83), ('OG', 'SER', 'CD', 'GLN', 8.66), ('OG', 'SER', 'OE1', 'GLN', 9.88), ('OG', 'SER', 'NE2', 'GLN', 8.24), ('OG', 'SER', 'O', 'GLN', 8.38), ('OG', 'SER', 'C', 'GLN', 7.24), ('OG', 'SER', 'CA', 'GLN', 6.11), ('OG', 'SER', 'N', 'GLN', 4.81)]]}
ASP_LEU = { 
	'distances':
		[[16.14, 16.04, 14.86, 16.03, 16.66, 17.06, 16.63, 15.73], [14.79, 14.63, 13.42, 14.66, 15.46, 15.8, 15.29, 14.37], [14.24, 13.98, 12.81, 13.9, 15.17, 15.42, 14.85, 14.03], [14.38, 14.25, 12.98, 14.42, 14.89, 15.29, 14.75, 13.74]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LEU', 16.14), ('CB', 'ASP', 'CG', 'LEU', 16.04), ('CB', 'ASP', 'CD1', 'LEU', 14.86), ('CB', 'ASP', 'CD2', 'LEU', 16.03), ('CB', 'ASP', 'O', 'LEU', 16.66), ('CB', 'ASP', 'C', 'LEU', 17.06), ('CB', 'ASP', 'CA', 'LEU', 16.63), ('CB', 'ASP', 'N', 'LEU', 15.73)], [('CG', 'ASP', 'CB', 'LEU', 14.79), ('CG', 'ASP', 'CG', 'LEU', 14.63), ('CG', 'ASP', 'CD1', 'LEU', 13.42), ('CG', 'ASP', 'CD2', 'LEU', 14.66), ('CG', 'ASP', 'O', 'LEU', 15.46), ('CG', 'ASP', 'C', 'LEU', 15.8), ('CG', 'ASP', 'CA', 'LEU', 15.29), ('CG', 'ASP', 'N', 'LEU', 14.37)], [('OD1', 'ASP', 'CB', 'LEU', 14.24), ('OD1', 'ASP', 'CG', 'LEU', 13.98), ('OD1', 'ASP', 'CD1', 'LEU', 12.81), ('OD1', 'ASP', 'CD2', 'LEU', 13.9), ('OD1', 'ASP', 'O', 'LEU', 15.17), ('OD1', 'ASP', 'C', 'LEU', 15.42), ('OD1', 'ASP', 'CA', 'LEU', 14.85), ('OD1', 'ASP', 'N', 'LEU', 14.03)], [('OD2', 'ASP', 'CB', 'LEU', 14.38), ('OD2', 'ASP', 'CG', 'LEU', 14.25), ('OD2', 'ASP', 'CD1', 'LEU', 12.98), ('OD2', 'ASP', 'CD2', 'LEU', 14.42), ('OD2', 'ASP', 'O', 'LEU', 14.89), ('OD2', 'ASP', 'C', 'LEU', 15.29), ('OD2', 'ASP', 'CA', 'LEU', 14.75), ('OD2', 'ASP', 'N', 'LEU', 13.74)]]}
GLN_LEU = { 
	'distances':
		[[7.79, 7.03, 5.98, 8.23, 9.41, 8.98, 7.55, 6.63], [8.58, 7.64, 6.81, 8.71, 10.48, 9.9, 8.43, 7.75], [8.05, 7.07, 6.65, 8.1, 10.16, 9.4, 7.94, 7.6], [8.99, 8.0, 7.75, 8.92, 11.09, 10.28, 8.87, 8.65], [6.78, 5.81, 5.6, 6.89, 9.04, 8.21, 6.74, 6.58], [10.62, 10.06, 9.05, 11.33, 11.5, 11.29, 10.03, 8.94], [9.76, 9.3, 8.21, 10.59, 10.54, 10.4, 9.17, 7.98], [8.89, 8.26, 7.03, 9.43, 10.14, 9.91, 8.58, 7.43], [8.61, 8.15, 6.77, 9.26, 9.63, 9.56, 8.34, 7.06]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'LEU', 7.79), ('CB', 'GLN', 'CG', 'LEU', 7.03), ('CB', 'GLN', 'CD1', 'LEU', 5.98), ('CB', 'GLN', 'CD2', 'LEU', 8.23), ('CB', 'GLN', 'O', 'LEU', 9.41), ('CB', 'GLN', 'C', 'LEU', 8.98), ('CB', 'GLN', 'CA', 'LEU', 7.55), ('CB', 'GLN', 'N', 'LEU', 6.63)], [('CG', 'GLN', 'CB', 'LEU', 8.58), ('CG', 'GLN', 'CG', 'LEU', 7.64), ('CG', 'GLN', 'CD1', 'LEU', 6.81), ('CG', 'GLN', 'CD2', 'LEU', 8.71), ('CG', 'GLN', 'O', 'LEU', 10.48), ('CG', 'GLN', 'C', 'LEU', 9.9), ('CG', 'GLN', 'CA', 'LEU', 8.43), ('CG', 'GLN', 'N', 'LEU', 7.75)], [('CD', 'GLN', 'CB', 'LEU', 8.05), ('CD', 'GLN', 'CG', 'LEU', 7.07), ('CD', 'GLN', 'CD1', 'LEU', 6.65), ('CD', 'GLN', 'CD2', 'LEU', 8.1), ('CD', 'GLN', 'O', 'LEU', 10.16), ('CD', 'GLN', 'C', 'LEU', 9.4), ('CD', 'GLN', 'CA', 'LEU', 7.94), ('CD', 'GLN', 'N', 'LEU', 7.6)], [('OE1', 'GLN', 'CB', 'LEU', 8.99), ('OE1', 'GLN', 'CG', 'LEU', 8.0), ('OE1', 'GLN', 'CD1', 'LEU', 7.75), ('OE1', 'GLN', 'CD2', 'LEU', 8.92), ('OE1', 'GLN', 'O', 'LEU', 11.09), ('OE1', 'GLN', 'C', 'LEU', 10.28), ('OE1', 'GLN', 'CA', 'LEU', 8.87), ('OE1', 'GLN', 'N', 'LEU', 8.65)], [('NE2', 'GLN', 'CB', 'LEU', 6.78), ('NE2', 'GLN', 'CG', 'LEU', 5.81), ('NE2', 'GLN', 'CD1', 'LEU', 5.6), ('NE2', 'GLN', 'CD2', 'LEU', 6.89), ('NE2', 'GLN', 'O', 'LEU', 9.04), ('NE2', 'GLN', 'C', 'LEU', 8.21), ('NE2', 'GLN', 'CA', 'LEU', 6.74), ('NE2', 'GLN', 'N', 'LEU', 6.58)], [('O', 'GLN', 'CB', 'LEU', 10.62), ('O', 'GLN', 'CG', 'LEU', 10.06), ('O', 'GLN', 'CD1', 'LEU', 9.05), ('O', 'GLN', 'CD2', 'LEU', 11.33), ('O', 'GLN', 'O', 'LEU', 11.5), ('O', 'GLN', 'C', 'LEU', 11.29), ('O', 'GLN', 'CA', 'LEU', 10.03), ('O', 'GLN', 'N', 'LEU', 8.94)], [('C', 'GLN', 'CB', 'LEU', 9.76), ('C', 'GLN', 'CG', 'LEU', 9.3), ('C', 'GLN', 'CD1', 'LEU', 8.21), ('C', 'GLN', 'CD2', 'LEU', 10.59), ('C', 'GLN', 'O', 'LEU', 10.54), ('C', 'GLN', 'C', 'LEU', 10.4), ('C', 'GLN', 'CA', 'LEU', 9.17), ('C', 'GLN', 'N', 'LEU', 7.98)], [('CA', 'GLN', 'CB', 'LEU', 8.89), ('CA', 'GLN', 'CG', 'LEU', 8.26), ('CA', 'GLN', 'CD1', 'LEU', 7.03), ('CA', 'GLN', 'CD2', 'LEU', 9.43), ('CA', 'GLN', 'O', 'LEU', 10.14), ('CA', 'GLN', 'C', 'LEU', 9.91), ('CA', 'GLN', 'CA', 'LEU', 8.58), ('CA', 'GLN', 'N', 'LEU', 7.43)], [('N', 'GLN', 'CB', 'LEU', 8.61), ('N', 'GLN', 'CG', 'LEU', 8.15), ('N', 'GLN', 'CD1', 'LEU', 6.77), ('N', 'GLN', 'CD2', 'LEU', 9.26), ('N', 'GLN', 'O', 'LEU', 9.63), ('N', 'GLN', 'C', 'LEU', 9.56), ('N', 'GLN', 'CA', 'LEU', 8.34), ('N', 'GLN', 'N', 'LEU', 7.06)]]}
HIS_LEU = { 
	'distances':
		[[12.27, 12.45, 11.49, 12.47, 12.5, 12.95, 12.73, 11.99], [11.22, 11.32, 10.26, 11.47, 11.57, 11.98, 11.62, 10.79], [11.61, 11.56, 10.34, 11.79, 12.14, 12.5, 11.97, 11.01], [9.92, 10.1, 9.08, 10.33, 10.22, 10.63, 10.28, 9.46], [10.66, 10.55, 9.26, 10.92, 11.26, 11.58, 10.94, 9.9], [9.52, 9.56, 8.37, 9.95, 10.01, 10.35, 9.8, 8.82]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LEU', 12.27), ('CB', 'HIS', 'CG', 'LEU', 12.45), ('CB', 'HIS', 'CD1', 'LEU', 11.49), ('CB', 'HIS', 'CD2', 'LEU', 12.47), ('CB', 'HIS', 'O', 'LEU', 12.5), ('CB', 'HIS', 'C', 'LEU', 12.95), ('CB', 'HIS', 'CA', 'LEU', 12.73), ('CB', 'HIS', 'N', 'LEU', 11.99)], [('CG', 'HIS', 'CB', 'LEU', 11.22), ('CG', 'HIS', 'CG', 'LEU', 11.32), ('CG', 'HIS', 'CD1', 'LEU', 10.26), ('CG', 'HIS', 'CD2', 'LEU', 11.47), ('CG', 'HIS', 'O', 'LEU', 11.57), ('CG', 'HIS', 'C', 'LEU', 11.98), ('CG', 'HIS', 'CA', 'LEU', 11.62), ('CG', 'HIS', 'N', 'LEU', 10.79)], [('ND1', 'HIS', 'CB', 'LEU', 11.61), ('ND1', 'HIS', 'CG', 'LEU', 11.56), ('ND1', 'HIS', 'CD1', 'LEU', 10.34), ('ND1', 'HIS', 'CD2', 'LEU', 11.79), ('ND1', 'HIS', 'O', 'LEU', 12.14), ('ND1', 'HIS', 'C', 'LEU', 12.5), ('ND1', 'HIS', 'CA', 'LEU', 11.97), ('ND1', 'HIS', 'N', 'LEU', 11.01)], [('CD2', 'HIS', 'CB', 'LEU', 9.92), ('CD2', 'HIS', 'CG', 'LEU', 10.1), ('CD2', 'HIS', 'CD1', 'LEU', 9.08), ('CD2', 'HIS', 'CD2', 'LEU', 10.33), ('CD2', 'HIS', 'O', 'LEU', 10.22), ('CD2', 'HIS', 'C', 'LEU', 10.63), ('CD2', 'HIS', 'CA', 'LEU', 10.28), ('CD2', 'HIS', 'N', 'LEU', 9.46)], [('CE1', 'HIS', 'CB', 'LEU', 10.66), ('CE1', 'HIS', 'CG', 'LEU', 10.55), ('CE1', 'HIS', 'CD1', 'LEU', 9.26), ('CE1', 'HIS', 'CD2', 'LEU', 10.92), ('CE1', 'HIS', 'O', 'LEU', 11.26), ('CE1', 'HIS', 'C', 'LEU', 11.58), ('CE1', 'HIS', 'CA', 'LEU', 10.94), ('CE1', 'HIS', 'N', 'LEU', 9.9)], [('NE2', 'HIS', 'CB', 'LEU', 9.52), ('NE2', 'HIS', 'CG', 'LEU', 9.56), ('NE2', 'HIS', 'CD1', 'LEU', 8.37), ('NE2', 'HIS', 'CD2', 'LEU', 9.95), ('NE2', 'HIS', 'O', 'LEU', 10.01), ('NE2', 'HIS', 'C', 'LEU', 10.35), ('NE2', 'HIS', 'CA', 'LEU', 9.8), ('NE2', 'HIS', 'N', 'LEU', 8.82)]]}
HIS_GLN = { 
	'distances':
		[[13.19, 14.53, 15.28, 16.49, 14.68, 14.91, 13.77, 12.76, 11.37], [11.73, 13.08, 13.87, 15.09, 13.33, 13.42, 12.28, 11.28, 9.88], [11.29, 12.6, 13.53, 14.72, 13.13, 12.74, 11.66, 10.67, 9.29], [10.72, 12.11, 12.82, 14.04, 12.2, 12.56, 11.39, 10.39, 9.0], [9.98, 11.3, 12.26, 13.45, 11.89, 11.42, 10.33, 9.34, 7.95], [9.53, 10.91, 11.73, 12.95, 11.22, 11.24, 10.09, 9.08, 7.68]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 13.19), ('CB', 'HIS', 'CG', 'GLN', 14.53), ('CB', 'HIS', 'CD', 'GLN', 15.28), ('CB', 'HIS', 'OE1', 'GLN', 16.49), ('CB', 'HIS', 'NE2', 'GLN', 14.68), ('CB', 'HIS', 'O', 'GLN', 14.91), ('CB', 'HIS', 'C', 'GLN', 13.77), ('CB', 'HIS', 'CA', 'GLN', 12.76), ('CB', 'HIS', 'N', 'GLN', 11.37)], [('CG', 'HIS', 'CB', 'GLN', 11.73), ('CG', 'HIS', 'CG', 'GLN', 13.08), ('CG', 'HIS', 'CD', 'GLN', 13.87), ('CG', 'HIS', 'OE1', 'GLN', 15.09), ('CG', 'HIS', 'NE2', 'GLN', 13.33), ('CG', 'HIS', 'O', 'GLN', 13.42), ('CG', 'HIS', 'C', 'GLN', 12.28), ('CG', 'HIS', 'CA', 'GLN', 11.28), ('CG', 'HIS', 'N', 'GLN', 9.88)], [('ND1', 'HIS', 'CB', 'GLN', 11.29), ('ND1', 'HIS', 'CG', 'GLN', 12.6), ('ND1', 'HIS', 'CD', 'GLN', 13.53), ('ND1', 'HIS', 'OE1', 'GLN', 14.72), ('ND1', 'HIS', 'NE2', 'GLN', 13.13), ('ND1', 'HIS', 'O', 'GLN', 12.74), ('ND1', 'HIS', 'C', 'GLN', 11.66), ('ND1', 'HIS', 'CA', 'GLN', 10.67), ('ND1', 'HIS', 'N', 'GLN', 9.29)], [('CD2', 'HIS', 'CB', 'GLN', 10.72), ('CD2', 'HIS', 'CG', 'GLN', 12.11), ('CD2', 'HIS', 'CD', 'GLN', 12.82), ('CD2', 'HIS', 'OE1', 'GLN', 14.04), ('CD2', 'HIS', 'NE2', 'GLN', 12.2), ('CD2', 'HIS', 'O', 'GLN', 12.56), ('CD2', 'HIS', 'C', 'GLN', 11.39), ('CD2', 'HIS', 'CA', 'GLN', 10.39), ('CD2', 'HIS', 'N', 'GLN', 9.0)], [('CE1', 'HIS', 'CB', 'GLN', 9.98), ('CE1', 'HIS', 'CG', 'GLN', 11.3), ('CE1', 'HIS', 'CD', 'GLN', 12.26), ('CE1', 'HIS', 'OE1', 'GLN', 13.45), ('CE1', 'HIS', 'NE2', 'GLN', 11.89), ('CE1', 'HIS', 'O', 'GLN', 11.42), ('CE1', 'HIS', 'C', 'GLN', 10.33), ('CE1', 'HIS', 'CA', 'GLN', 9.34), ('CE1', 'HIS', 'N', 'GLN', 7.95)], [('NE2', 'HIS', 'CB', 'GLN', 9.53), ('NE2', 'HIS', 'CG', 'GLN', 10.91), ('NE2', 'HIS', 'CD', 'GLN', 11.73), ('NE2', 'HIS', 'OE1', 'GLN', 12.95), ('NE2', 'HIS', 'NE2', 'GLN', 11.22), ('NE2', 'HIS', 'O', 'GLN', 11.24), ('NE2', 'HIS', 'C', 'GLN', 10.09), ('NE2', 'HIS', 'CA', 'GLN', 9.08), ('NE2', 'HIS', 'N', 'GLN', 7.68)]]}
SER_LEU = { 
	'distances':
		[[8.51, 8.47, 7.13, 9.4, 8.89, 9.15, 8.32, 6.99], [7.66, 7.41, 6.0, 8.2, 8.68, 8.74, 7.76, 6.61]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LEU', 8.51), ('CB', 'SER', 'CG', 'LEU', 8.47), ('CB', 'SER', 'CD1', 'LEU', 7.13), ('CB', 'SER', 'CD2', 'LEU', 9.4), ('CB', 'SER', 'O', 'LEU', 8.89), ('CB', 'SER', 'C', 'LEU', 9.15), ('CB', 'SER', 'CA', 'LEU', 8.32), ('CB', 'SER', 'N', 'LEU', 6.99)], [('OG', 'SER', 'CB', 'LEU', 7.66), ('OG', 'SER', 'CG', 'LEU', 7.41), ('OG', 'SER', 'CD1', 'LEU', 6.0), ('OG', 'SER', 'CD2', 'LEU', 8.2), ('OG', 'SER', 'O', 'LEU', 8.68), ('OG', 'SER', 'C', 'LEU', 8.74), ('OG', 'SER', 'CA', 'LEU', 7.76), ('OG', 'SER', 'N', 'LEU', 6.61)]]}
ASP_GLN = { 
	'distances':
		[[15.77, 16.96, 17.98, 19.12, 17.66, 16.96, 15.98, 15.02, 13.72], [14.27, 15.45, 16.46, 17.6, 16.15, 15.52, 14.54, 13.55, 12.25], [13.89, 15.01, 15.95, 17.07, 15.61, 15.36, 14.4, 13.29, 12.04], [13.55, 14.76, 15.83, 16.98, 15.57, 14.61, 13.63, 12.73, 11.41]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 15.77), ('CB', 'ASP', 'CG', 'GLN', 16.96), ('CB', 'ASP', 'CD', 'GLN', 17.98), ('CB', 'ASP', 'OE1', 'GLN', 19.12), ('CB', 'ASP', 'NE2', 'GLN', 17.66), ('CB', 'ASP', 'O', 'GLN', 16.96), ('CB', 'ASP', 'C', 'GLN', 15.98), ('CB', 'ASP', 'CA', 'GLN', 15.02), ('CB', 'ASP', 'N', 'GLN', 13.72)], [('CG', 'ASP', 'CB', 'GLN', 14.27), ('CG', 'ASP', 'CG', 'GLN', 15.45), ('CG', 'ASP', 'CD', 'GLN', 16.46), ('CG', 'ASP', 'OE1', 'GLN', 17.6), ('CG', 'ASP', 'NE2', 'GLN', 16.15), ('CG', 'ASP', 'O', 'GLN', 15.52), ('CG', 'ASP', 'C', 'GLN', 14.54), ('CG', 'ASP', 'CA', 'GLN', 13.55), ('CG', 'ASP', 'N', 'GLN', 12.25)], [('OD1', 'ASP', 'CB', 'GLN', 13.89), ('OD1', 'ASP', 'CG', 'GLN', 15.01), ('OD1', 'ASP', 'CD', 'GLN', 15.95), ('OD1', 'ASP', 'OE1', 'GLN', 17.07), ('OD1', 'ASP', 'NE2', 'GLN', 15.61), ('OD1', 'ASP', 'O', 'GLN', 15.36), ('OD1', 'ASP', 'C', 'GLN', 14.4), ('OD1', 'ASP', 'CA', 'GLN', 13.29), ('OD1', 'ASP', 'N', 'GLN', 12.04)], [('OD2', 'ASP', 'CB', 'GLN', 13.55), ('OD2', 'ASP', 'CG', 'GLN', 14.76), ('OD2', 'ASP', 'CD', 'GLN', 15.83), ('OD2', 'ASP', 'OE1', 'GLN', 16.98), ('OD2', 'ASP', 'NE2', 'GLN', 15.57), ('OD2', 'ASP', 'O', 'GLN', 14.61), ('OD2', 'ASP', 'C', 'GLN', 13.63), ('OD2', 'ASP', 'CA', 'GLN', 12.73), ('OD2', 'ASP', 'N', 'GLN', 11.41)]]}
HIS_SER = { 
	'distances':
		[[8.88, 8.8], [7.42, 7.34], [7.02, 7.03], [6.48, 6.33], [5.72, 5.74], [5.23, 5.12]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'SER', 8.88), ('CB', 'HIS', 'OG', 'SER', 8.8)], [('CG', 'HIS', 'CB', 'SER', 7.42), ('CG', 'HIS', 'OG', 'SER', 7.34)], [('ND1', 'HIS', 'CB', 'SER', 7.02), ('ND1', 'HIS', 'OG', 'SER', 7.03)], [('CD2', 'HIS', 'CB', 'SER', 6.48), ('CD2', 'HIS', 'OG', 'SER', 6.33)], [('CE1', 'HIS', 'CB', 'SER', 5.72), ('CE1', 'HIS', 'OG', 'SER', 5.74)], [('NE2', 'HIS', 'CB', 'SER', 5.23), ('NE2', 'HIS', 'OG', 'SER', 5.12)]]}
ASP_SER = { 
	'distances':
		[[11.64, 11.7], [10.25, 10.24], [10.16, 9.94], [9.39, 9.54]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.64), ('CB', 'ASP', 'OG', 'SER', 11.7)], [('CG', 'ASP', 'CB', 'SER', 10.25), ('CG', 'ASP', 'OG', 'SER', 10.24)], [('OD1', 'ASP', 'CB', 'SER', 10.16), ('OD1', 'ASP', 'OG', 'SER', 9.94)], [('OD2', 'ASP', 'CB', 'SER', 9.39), ('OD2', 'ASP', 'OG', 'SER', 9.54)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_ASP, d, 'A_2lip_3_1_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_GLN, d, 'A_2lip_3_1_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_LEU, d, 'A_2lip_3_1_1_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_LEU, d, 'A_2lip_3_1_1_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_LEU, d, 'A_2lip_3_1_1_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_GLN, d, 'A_2lip_3_1_1_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_LEU, d, 'A_2lip_3_1_1_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_GLN, d, 'A_2lip_3_1_1_3')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(HIS_SER, d, 'A_2lip_3_1_1_3')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASP_SER, d, 'A_2lip_3_1_1_3')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_ASP' :  match1,
		'SER_GLN' :  match2,
		'ASP_LEU' :  match3,
		'GLN_LEU' :  match4,
		'HIS_LEU' :  match5,
		'HIS_GLN' :  match6,
		'SER_LEU' :  match7,
		'ASP_GLN' :  match8,
		'HIS_SER' :  match9,
		'ASP_SER' :  match10}