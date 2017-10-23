'''
FUNC:A_5enl_4_2_1_11
PDB:5enl
EC:4.2.1.11
RESI:glu,glu,lys,his
LOCI:a-168,211,345,373;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[10.36, 9.53, 10.08, 9.52, 10.75, 12.34, 11.33, 10.39, 11.23], [10.79, 9.75, 10.08, 9.26, 10.34, 13.03, 12.08, 10.99, 11.73], [12.1, 11.03, 11.26, 10.35, 11.3, 14.36, 13.42, 12.35, 13.09], [10.34, 9.14, 9.32, 8.34, 9.33, 12.76, 11.88, 10.66, 11.28], [12.49, 11.29, 11.35, 10.26, 11.06, 14.91, 14.03, 12.85, 13.5], [11.5, 10.22, 10.24, 9.09, 9.87, 14.01, 13.16, 11.92, 12.48], [7.5, 6.43, 6.71, 6.12, 7.37, 9.92, 9.12, 7.98, 8.83], [8.19, 7.33, 7.75, 7.29, 8.54, 10.37, 9.49, 8.5, 9.47], [8.91, 8.15, 8.83, 8.45, 9.79, 10.85, 9.83, 8.89, 9.75], [8.58, 7.7, 8.5, 8.08, 9.47, 10.59, 9.54, 8.44, 9.04]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 10.36), ('CB', 'HIS', 'CG', 'LYS', 9.53), ('CB', 'HIS', 'CD', 'LYS', 10.08), ('CB', 'HIS', 'CE', 'LYS', 9.52), ('CB', 'HIS', 'NZ', 'LYS', 10.75), ('CB', 'HIS', 'O', 'LYS', 12.34), ('CB', 'HIS', 'C', 'LYS', 11.33), ('CB', 'HIS', 'CA', 'LYS', 10.39), ('CB', 'HIS', 'N', 'LYS', 11.23)], [('CG', 'HIS', 'CB', 'LYS', 10.79), ('CG', 'HIS', 'CG', 'LYS', 9.75), ('CG', 'HIS', 'CD', 'LYS', 10.08), ('CG', 'HIS', 'CE', 'LYS', 9.26), ('CG', 'HIS', 'NZ', 'LYS', 10.34), ('CG', 'HIS', 'O', 'LYS', 13.03), ('CG', 'HIS', 'C', 'LYS', 12.08), ('CG', 'HIS', 'CA', 'LYS', 10.99), ('CG', 'HIS', 'N', 'LYS', 11.73)], [('ND1', 'HIS', 'CB', 'LYS', 12.1), ('ND1', 'HIS', 'CG', 'LYS', 11.03), ('ND1', 'HIS', 'CD', 'LYS', 11.26), ('ND1', 'HIS', 'CE', 'LYS', 10.35), ('ND1', 'HIS', 'NZ', 'LYS', 11.3), ('ND1', 'HIS', 'O', 'LYS', 14.36), ('ND1', 'HIS', 'C', 'LYS', 13.42), ('ND1', 'HIS', 'CA', 'LYS', 12.35), ('ND1', 'HIS', 'N', 'LYS', 13.09)], [('CD2', 'HIS', 'CB', 'LYS', 10.34), ('CD2', 'HIS', 'CG', 'LYS', 9.14), ('CD2', 'HIS', 'CD', 'LYS', 9.32), ('CD2', 'HIS', 'CE', 'LYS', 8.34), ('CD2', 'HIS', 'NZ', 'LYS', 9.33), ('CD2', 'HIS', 'O', 'LYS', 12.76), ('CD2', 'HIS', 'C', 'LYS', 11.88), ('CD2', 'HIS', 'CA', 'LYS', 10.66), ('CD2', 'HIS', 'N', 'LYS', 11.28)], [('CE1', 'HIS', 'CB', 'LYS', 12.49), ('CE1', 'HIS', 'CG', 'LYS', 11.29), ('CE1', 'HIS', 'CD', 'LYS', 11.35), ('CE1', 'HIS', 'CE', 'LYS', 10.26), ('CE1', 'HIS', 'NZ', 'LYS', 11.06), ('CE1', 'HIS', 'O', 'LYS', 14.91), ('CE1', 'HIS', 'C', 'LYS', 14.03), ('CE1', 'HIS', 'CA', 'LYS', 12.85), ('CE1', 'HIS', 'N', 'LYS', 13.5)], [('NE2', 'HIS', 'CB', 'LYS', 11.5), ('NE2', 'HIS', 'CG', 'LYS', 10.22), ('NE2', 'HIS', 'CD', 'LYS', 10.24), ('NE2', 'HIS', 'CE', 'LYS', 9.09), ('NE2', 'HIS', 'NZ', 'LYS', 9.87), ('NE2', 'HIS', 'O', 'LYS', 14.01), ('NE2', 'HIS', 'C', 'LYS', 13.16), ('NE2', 'HIS', 'CA', 'LYS', 11.92), ('NE2', 'HIS', 'N', 'LYS', 12.48)], [('O', 'HIS', 'CB', 'LYS', 7.5), ('O', 'HIS', 'CG', 'LYS', 6.43), ('O', 'HIS', 'CD', 'LYS', 6.71), ('O', 'HIS', 'CE', 'LYS', 6.12), ('O', 'HIS', 'NZ', 'LYS', 7.37), ('O', 'HIS', 'O', 'LYS', 9.92), ('O', 'HIS', 'C', 'LYS', 9.12), ('O', 'HIS', 'CA', 'LYS', 7.98), ('O', 'HIS', 'N', 'LYS', 8.83)], [('C', 'HIS', 'CB', 'LYS', 8.19), ('C', 'HIS', 'CG', 'LYS', 7.33), ('C', 'HIS', 'CD', 'LYS', 7.75), ('C', 'HIS', 'CE', 'LYS', 7.29), ('C', 'HIS', 'NZ', 'LYS', 8.54), ('C', 'HIS', 'O', 'LYS', 10.37), ('C', 'HIS', 'C', 'LYS', 9.49), ('C', 'HIS', 'CA', 'LYS', 8.5), ('C', 'HIS', 'N', 'LYS', 9.47)], [('CA', 'HIS', 'CB', 'LYS', 8.91), ('CA', 'HIS', 'CG', 'LYS', 8.15), ('CA', 'HIS', 'CD', 'LYS', 8.83), ('CA', 'HIS', 'CE', 'LYS', 8.45), ('CA', 'HIS', 'NZ', 'LYS', 9.79), ('CA', 'HIS', 'O', 'LYS', 10.85), ('CA', 'HIS', 'C', 'LYS', 9.83), ('CA', 'HIS', 'CA', 'LYS', 8.89), ('CA', 'HIS', 'N', 'LYS', 9.75)], [('N', 'HIS', 'CB', 'LYS', 8.58), ('N', 'HIS', 'CG', 'LYS', 7.7), ('N', 'HIS', 'CD', 'LYS', 8.5), ('N', 'HIS', 'CE', 'LYS', 8.08), ('N', 'HIS', 'NZ', 'LYS', 9.47), ('N', 'HIS', 'O', 'LYS', 10.59), ('N', 'HIS', 'C', 'LYS', 9.54), ('N', 'HIS', 'CA', 'LYS', 8.44), ('N', 'HIS', 'N', 'LYS', 9.04)]]}
GLU_LYS = { 
	'distances':
		[[15.77, 14.53, 14.24, 13.0, 13.37, 18.29, 17.52, 16.37, 17.09], [14.56, 13.34, 12.96, 11.73, 12.06, 17.1, 16.39, 15.26, 16.03], [13.66, 12.35, 11.9, 10.59, 10.84, 16.28, 15.61, 14.4, 15.07], [13.95, 12.58, 12.2, 10.83, 11.1, 16.61, 15.9, 14.62, 15.16], [12.82, 11.53, 10.97, 9.67, 9.83, 15.45, 14.86, 13.68, 14.4], [17.78, 16.6, 16.53, 15.36, 15.91, 20.16, 19.27, 18.17, 18.87], [17.89, 16.72, 16.54, 15.35, 15.81, 20.31, 19.48, 18.39, 19.14], [16.72, 15.56, 15.31, 14.14, 14.55, 19.15, 18.37, 17.3, 18.11], [17.25, 16.1, 15.71, 14.54, 14.81, 19.69, 18.98, 17.94, 18.8], [16.83, 15.33, 14.68, 13.17, 12.9, 19.58, 19.05, 17.6, 17.67], [15.76, 14.27, 13.53, 12.01, 11.66, 18.52, 18.04, 16.61, 16.76], [14.32, 12.83, 12.15, 10.63, 10.39, 17.08, 16.57, 15.14, 15.31], [14.11, 12.61, 12.08, 10.59, 10.52, 16.84, 16.26, 14.8, 14.89], [13.5, 12.02, 11.25, 9.73, 9.44, 16.27, 15.8, 14.41, 14.66], [18.77, 17.27, 16.67, 15.2, 14.86, 21.44, 20.94, 19.45, 19.29], [18.91, 17.4, 16.79, 15.29, 14.98, 21.62, 21.09, 19.61, 19.55], [18.26, 16.76, 16.05, 14.54, 14.16, 21.01, 20.51, 19.06, 19.1], [18.35, 16.86, 16.03, 14.54, 13.99, 21.08, 20.68, 19.24, 19.26]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 15.77), ('CB', 'GLU', 'CG', 'LYS', 14.53), ('CB', 'GLU', 'CD', 'LYS', 14.24), ('CB', 'GLU', 'CE', 'LYS', 13.0), ('CB', 'GLU', 'NZ', 'LYS', 13.37), ('CB', 'GLU', 'O', 'LYS', 18.29), ('CB', 'GLU', 'C', 'LYS', 17.52), ('CB', 'GLU', 'CA', 'LYS', 16.37), ('CB', 'GLU', 'N', 'LYS', 17.09)], [('CG', 'GLU', 'CB', 'LYS', 14.56), ('CG', 'GLU', 'CG', 'LYS', 13.34), ('CG', 'GLU', 'CD', 'LYS', 12.96), ('CG', 'GLU', 'CE', 'LYS', 11.73), ('CG', 'GLU', 'NZ', 'LYS', 12.06), ('CG', 'GLU', 'O', 'LYS', 17.1), ('CG', 'GLU', 'C', 'LYS', 16.39), ('CG', 'GLU', 'CA', 'LYS', 15.26), ('CG', 'GLU', 'N', 'LYS', 16.03)], [('CD', 'GLU', 'CB', 'LYS', 13.66), ('CD', 'GLU', 'CG', 'LYS', 12.35), ('CD', 'GLU', 'CD', 'LYS', 11.9), ('CD', 'GLU', 'CE', 'LYS', 10.59), ('CD', 'GLU', 'NZ', 'LYS', 10.84), ('CD', 'GLU', 'O', 'LYS', 16.28), ('CD', 'GLU', 'C', 'LYS', 15.61), ('CD', 'GLU', 'CA', 'LYS', 14.4), ('CD', 'GLU', 'N', 'LYS', 15.07)], [('OE1', 'GLU', 'CB', 'LYS', 13.95), ('OE1', 'GLU', 'CG', 'LYS', 12.58), ('OE1', 'GLU', 'CD', 'LYS', 12.2), ('OE1', 'GLU', 'CE', 'LYS', 10.83), ('OE1', 'GLU', 'NZ', 'LYS', 11.1), ('OE1', 'GLU', 'O', 'LYS', 16.61), ('OE1', 'GLU', 'C', 'LYS', 15.9), ('OE1', 'GLU', 'CA', 'LYS', 14.62), ('OE1', 'GLU', 'N', 'LYS', 15.16)], [('OE2', 'GLU', 'CB', 'LYS', 12.82), ('OE2', 'GLU', 'CG', 'LYS', 11.53), ('OE2', 'GLU', 'CD', 'LYS', 10.97), ('OE2', 'GLU', 'CE', 'LYS', 9.67), ('OE2', 'GLU', 'NZ', 'LYS', 9.83), ('OE2', 'GLU', 'O', 'LYS', 15.45), ('OE2', 'GLU', 'C', 'LYS', 14.86), ('OE2', 'GLU', 'CA', 'LYS', 13.68), ('OE2', 'GLU', 'N', 'LYS', 14.4)], [('O', 'GLU', 'CB', 'LYS', 17.78), ('O', 'GLU', 'CG', 'LYS', 16.6), ('O', 'GLU', 'CD', 'LYS', 16.53), ('O', 'GLU', 'CE', 'LYS', 15.36), ('O', 'GLU', 'NZ', 'LYS', 15.91), ('O', 'GLU', 'O', 'LYS', 20.16), ('O', 'GLU', 'C', 'LYS', 19.27), ('O', 'GLU', 'CA', 'LYS', 18.17), ('O', 'GLU', 'N', 'LYS', 18.87)], [('C', 'GLU', 'CB', 'LYS', 17.89), ('C', 'GLU', 'CG', 'LYS', 16.72), ('C', 'GLU', 'CD', 'LYS', 16.54), ('C', 'GLU', 'CE', 'LYS', 15.35), ('C', 'GLU', 'NZ', 'LYS', 15.81), ('C', 'GLU', 'O', 'LYS', 20.31), ('C', 'GLU', 'C', 'LYS', 19.48), ('C', 'GLU', 'CA', 'LYS', 18.39), ('C', 'GLU', 'N', 'LYS', 19.14)], [('CA', 'GLU', 'CB', 'LYS', 16.72), ('CA', 'GLU', 'CG', 'LYS', 15.56), ('CA', 'GLU', 'CD', 'LYS', 15.31), ('CA', 'GLU', 'CE', 'LYS', 14.14), ('CA', 'GLU', 'NZ', 'LYS', 14.55), ('CA', 'GLU', 'O', 'LYS', 19.15), ('CA', 'GLU', 'C', 'LYS', 18.37), ('CA', 'GLU', 'CA', 'LYS', 17.3), ('CA', 'GLU', 'N', 'LYS', 18.11)], [('N', 'GLU', 'CB', 'LYS', 17.25), ('N', 'GLU', 'CG', 'LYS', 16.1), ('N', 'GLU', 'CD', 'LYS', 15.71), ('N', 'GLU', 'CE', 'LYS', 14.54), ('N', 'GLU', 'NZ', 'LYS', 14.81), ('N', 'GLU', 'O', 'LYS', 19.69), ('N', 'GLU', 'C', 'LYS', 18.98), ('N', 'GLU', 'CA', 'LYS', 17.94), ('N', 'GLU', 'N', 'LYS', 18.8)], [('CB', 'GLU', 'CB', 'LYS', 16.83), ('CB', 'GLU', 'CG', 'LYS', 15.33), ('CB', 'GLU', 'CD', 'LYS', 14.68), ('CB', 'GLU', 'CE', 'LYS', 13.17), ('CB', 'GLU', 'NZ', 'LYS', 12.9), ('CB', 'GLU', 'O', 'LYS', 19.58), ('CB', 'GLU', 'C', 'LYS', 19.05), ('CB', 'GLU', 'CA', 'LYS', 17.6), ('CB', 'GLU', 'N', 'LYS', 17.67)], [('CG', 'GLU', 'CB', 'LYS', 15.76), ('CG', 'GLU', 'CG', 'LYS', 14.27), ('CG', 'GLU', 'CD', 'LYS', 13.53), ('CG', 'GLU', 'CE', 'LYS', 12.01), ('CG', 'GLU', 'NZ', 'LYS', 11.66), ('CG', 'GLU', 'O', 'LYS', 18.52), ('CG', 'GLU', 'C', 'LYS', 18.04), ('CG', 'GLU', 'CA', 'LYS', 16.61), ('CG', 'GLU', 'N', 'LYS', 16.76)], [('CD', 'GLU', 'CB', 'LYS', 14.32), ('CD', 'GLU', 'CG', 'LYS', 12.83), ('CD', 'GLU', 'CD', 'LYS', 12.15), ('CD', 'GLU', 'CE', 'LYS', 10.63), ('CD', 'GLU', 'NZ', 'LYS', 10.39), ('CD', 'GLU', 'O', 'LYS', 17.08), ('CD', 'GLU', 'C', 'LYS', 16.57), ('CD', 'GLU', 'CA', 'LYS', 15.14), ('CD', 'GLU', 'N', 'LYS', 15.31)], [('OE1', 'GLU', 'CB', 'LYS', 14.11), ('OE1', 'GLU', 'CG', 'LYS', 12.61), ('OE1', 'GLU', 'CD', 'LYS', 12.08), ('OE1', 'GLU', 'CE', 'LYS', 10.59), ('OE1', 'GLU', 'NZ', 'LYS', 10.52), ('OE1', 'GLU', 'O', 'LYS', 16.84), ('OE1', 'GLU', 'C', 'LYS', 16.26), ('OE1', 'GLU', 'CA', 'LYS', 14.8), ('OE1', 'GLU', 'N', 'LYS', 14.89)], [('OE2', 'GLU', 'CB', 'LYS', 13.5), ('OE2', 'GLU', 'CG', 'LYS', 12.02), ('OE2', 'GLU', 'CD', 'LYS', 11.25), ('OE2', 'GLU', 'CE', 'LYS', 9.73), ('OE2', 'GLU', 'NZ', 'LYS', 9.44), ('OE2', 'GLU', 'O', 'LYS', 16.27), ('OE2', 'GLU', 'C', 'LYS', 15.8), ('OE2', 'GLU', 'CA', 'LYS', 14.41), ('OE2', 'GLU', 'N', 'LYS', 14.66)], [('O', 'GLU', 'CB', 'LYS', 18.77), ('O', 'GLU', 'CG', 'LYS', 17.27), ('O', 'GLU', 'CD', 'LYS', 16.67), ('O', 'GLU', 'CE', 'LYS', 15.2), ('O', 'GLU', 'NZ', 'LYS', 14.86), ('O', 'GLU', 'O', 'LYS', 21.44), ('O', 'GLU', 'C', 'LYS', 20.94), ('O', 'GLU', 'CA', 'LYS', 19.45), ('O', 'GLU', 'N', 'LYS', 19.29)], [('C', 'GLU', 'CB', 'LYS', 18.91), ('C', 'GLU', 'CG', 'LYS', 17.4), ('C', 'GLU', 'CD', 'LYS', 16.79), ('C', 'GLU', 'CE', 'LYS', 15.29), ('C', 'GLU', 'NZ', 'LYS', 14.98), ('C', 'GLU', 'O', 'LYS', 21.62), ('C', 'GLU', 'C', 'LYS', 21.09), ('C', 'GLU', 'CA', 'LYS', 19.61), ('C', 'GLU', 'N', 'LYS', 19.55)], [('CA', 'GLU', 'CB', 'LYS', 18.26), ('CA', 'GLU', 'CG', 'LYS', 16.76), ('CA', 'GLU', 'CD', 'LYS', 16.05), ('CA', 'GLU', 'CE', 'LYS', 14.54), ('CA', 'GLU', 'NZ', 'LYS', 14.16), ('CA', 'GLU', 'O', 'LYS', 21.01), ('CA', 'GLU', 'C', 'LYS', 20.51), ('CA', 'GLU', 'CA', 'LYS', 19.06), ('CA', 'GLU', 'N', 'LYS', 19.1)], [('N', 'GLU', 'CB', 'LYS', 18.35), ('N', 'GLU', 'CG', 'LYS', 16.86), ('N', 'GLU', 'CD', 'LYS', 16.03), ('N', 'GLU', 'CE', 'LYS', 14.54), ('N', 'GLU', 'NZ', 'LYS', 13.99), ('N', 'GLU', 'O', 'LYS', 21.08), ('N', 'GLU', 'C', 'LYS', 20.68), ('N', 'GLU', 'CA', 'LYS', 19.24), ('N', 'GLU', 'N', 'LYS', 19.26)]]}
GLU_GLU = { 
	'distances':
		[[9.67, 9.2, 8.7, 8.82, 8.53, 12.5, 11.6, 10.72, 11.65], [9.71, 8.96, 8.27, 8.53, 7.83, 12.67, 11.85, 10.85, 11.59], [8.63, 7.76, 6.91, 7.18, 6.4, 11.62, 10.9, 9.89, 10.56], [7.72, 7.02, 6.17, 6.23, 5.94, 10.61, 9.92, 9.03, 9.84], [9.06, 7.97, 7.02, 7.44, 6.22, 12.06, 11.43, 10.32, 10.8], [11.41, 11.32, 10.95, 10.82, 11.04, 13.86, 12.9, 12.31, 13.47], [11.36, 11.16, 10.87, 10.91, 10.86, 13.95, 12.93, 12.2, 13.26], [11.05, 10.61, 10.19, 10.35, 9.99, 13.83, 12.87, 11.98, 12.91], [11.34, 10.8, 10.51, 10.88, 10.22, 14.19, 13.17, 12.15, 12.94], [9.67, 9.71, 8.63, 7.72, 9.06, 11.41, 11.36, 11.05, 11.34], [9.2, 8.96, 7.76, 7.02, 7.97, 11.32, 11.16, 10.61, 10.8], [8.7, 8.27, 6.91, 6.17, 7.02, 10.95, 10.87, 10.19, 10.51], [8.82, 8.53, 7.18, 6.23, 7.44, 10.82, 10.91, 10.35, 10.88], [8.53, 7.83, 6.4, 5.94, 6.22, 11.04, 10.86, 9.99, 10.22], [12.5, 12.67, 11.62, 10.61, 12.06, 13.86, 13.95, 13.83, 14.19], [11.6, 11.85, 10.9, 9.92, 11.43, 12.9, 12.93, 12.87, 13.17], [10.72, 10.85, 9.89, 9.03, 10.32, 12.31, 12.2, 11.98, 12.15], [11.65, 11.59, 10.56, 9.84, 10.8, 13.47, 13.26, 12.91, 12.94]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 9.67), ('CB', 'GLU', 'CG', 'GLU', 9.2), ('CB', 'GLU', 'CD', 'GLU', 8.7), ('CB', 'GLU', 'OE1', 'GLU', 8.82), ('CB', 'GLU', 'OE2', 'GLU', 8.53), ('CB', 'GLU', 'O', 'GLU', 12.5), ('CB', 'GLU', 'C', 'GLU', 11.6), ('CB', 'GLU', 'CA', 'GLU', 10.72), ('CB', 'GLU', 'N', 'GLU', 11.65)], [('CG', 'GLU', 'CB', 'GLU', 9.71), ('CG', 'GLU', 'CG', 'GLU', 8.96), ('CG', 'GLU', 'CD', 'GLU', 8.27), ('CG', 'GLU', 'OE1', 'GLU', 8.53), ('CG', 'GLU', 'OE2', 'GLU', 7.83), ('CG', 'GLU', 'O', 'GLU', 12.67), ('CG', 'GLU', 'C', 'GLU', 11.85), ('CG', 'GLU', 'CA', 'GLU', 10.85), ('CG', 'GLU', 'N', 'GLU', 11.59)], [('CD', 'GLU', 'CB', 'GLU', 8.63), ('CD', 'GLU', 'CG', 'GLU', 7.76), ('CD', 'GLU', 'CD', 'GLU', 6.91), ('CD', 'GLU', 'OE1', 'GLU', 7.18), ('CD', 'GLU', 'OE2', 'GLU', 6.4), ('CD', 'GLU', 'O', 'GLU', 11.62), ('CD', 'GLU', 'C', 'GLU', 10.9), ('CD', 'GLU', 'CA', 'GLU', 9.89), ('CD', 'GLU', 'N', 'GLU', 10.56)], [('OE1', 'GLU', 'CB', 'GLU', 7.72), ('OE1', 'GLU', 'CG', 'GLU', 7.02), ('OE1', 'GLU', 'CD', 'GLU', 6.17), ('OE1', 'GLU', 'OE1', 'GLU', 6.23), ('OE1', 'GLU', 'OE2', 'GLU', 5.94), ('OE1', 'GLU', 'O', 'GLU', 10.61), ('OE1', 'GLU', 'C', 'GLU', 9.92), ('OE1', 'GLU', 'CA', 'GLU', 9.03), ('OE1', 'GLU', 'N', 'GLU', 9.84)], [('OE2', 'GLU', 'CB', 'GLU', 9.06), ('OE2', 'GLU', 'CG', 'GLU', 7.97), ('OE2', 'GLU', 'CD', 'GLU', 7.02), ('OE2', 'GLU', 'OE1', 'GLU', 7.44), ('OE2', 'GLU', 'OE2', 'GLU', 6.22), ('OE2', 'GLU', 'O', 'GLU', 12.06), ('OE2', 'GLU', 'C', 'GLU', 11.43), ('OE2', 'GLU', 'CA', 'GLU', 10.32), ('OE2', 'GLU', 'N', 'GLU', 10.8)], [('O', 'GLU', 'CB', 'GLU', 11.41), ('O', 'GLU', 'CG', 'GLU', 11.32), ('O', 'GLU', 'CD', 'GLU', 10.95), ('O', 'GLU', 'OE1', 'GLU', 10.82), ('O', 'GLU', 'OE2', 'GLU', 11.04), ('O', 'GLU', 'O', 'GLU', 13.86), ('O', 'GLU', 'C', 'GLU', 12.9), ('O', 'GLU', 'CA', 'GLU', 12.31), ('O', 'GLU', 'N', 'GLU', 13.47)], [('C', 'GLU', 'CB', 'GLU', 11.36), ('C', 'GLU', 'CG', 'GLU', 11.16), ('C', 'GLU', 'CD', 'GLU', 10.87), ('C', 'GLU', 'OE1', 'GLU', 10.91), ('C', 'GLU', 'OE2', 'GLU', 10.86), ('C', 'GLU', 'O', 'GLU', 13.95), ('C', 'GLU', 'C', 'GLU', 12.93), ('C', 'GLU', 'CA', 'GLU', 12.2), ('C', 'GLU', 'N', 'GLU', 13.26)], [('CA', 'GLU', 'CB', 'GLU', 11.05), ('CA', 'GLU', 'CG', 'GLU', 10.61), ('CA', 'GLU', 'CD', 'GLU', 10.19), ('CA', 'GLU', 'OE1', 'GLU', 10.35), ('CA', 'GLU', 'OE2', 'GLU', 9.99), ('CA', 'GLU', 'O', 'GLU', 13.83), ('CA', 'GLU', 'C', 'GLU', 12.87), ('CA', 'GLU', 'CA', 'GLU', 11.98), ('CA', 'GLU', 'N', 'GLU', 12.91)], [('N', 'GLU', 'CB', 'GLU', 11.34), ('N', 'GLU', 'CG', 'GLU', 10.8), ('N', 'GLU', 'CD', 'GLU', 10.51), ('N', 'GLU', 'OE1', 'GLU', 10.88), ('N', 'GLU', 'OE2', 'GLU', 10.22), ('N', 'GLU', 'O', 'GLU', 14.19), ('N', 'GLU', 'C', 'GLU', 13.17), ('N', 'GLU', 'CA', 'GLU', 12.15), ('N', 'GLU', 'N', 'GLU', 12.94)], [('CB', 'GLU', 'CB', 'GLU', 9.67), ('CB', 'GLU', 'CG', 'GLU', 9.71), ('CB', 'GLU', 'CD', 'GLU', 8.63), ('CB', 'GLU', 'OE1', 'GLU', 7.72), ('CB', 'GLU', 'OE2', 'GLU', 9.06), ('CB', 'GLU', 'O', 'GLU', 11.41), ('CB', 'GLU', 'C', 'GLU', 11.36), ('CB', 'GLU', 'CA', 'GLU', 11.05), ('CB', 'GLU', 'N', 'GLU', 11.34)], [('CG', 'GLU', 'CB', 'GLU', 9.2), ('CG', 'GLU', 'CG', 'GLU', 8.96), ('CG', 'GLU', 'CD', 'GLU', 7.76), ('CG', 'GLU', 'OE1', 'GLU', 7.02), ('CG', 'GLU', 'OE2', 'GLU', 7.97), ('CG', 'GLU', 'O', 'GLU', 11.32), ('CG', 'GLU', 'C', 'GLU', 11.16), ('CG', 'GLU', 'CA', 'GLU', 10.61), ('CG', 'GLU', 'N', 'GLU', 10.8)], [('CD', 'GLU', 'CB', 'GLU', 8.7), ('CD', 'GLU', 'CG', 'GLU', 8.27), ('CD', 'GLU', 'CD', 'GLU', 6.91), ('CD', 'GLU', 'OE1', 'GLU', 6.17), ('CD', 'GLU', 'OE2', 'GLU', 7.02), ('CD', 'GLU', 'O', 'GLU', 10.95), ('CD', 'GLU', 'C', 'GLU', 10.87), ('CD', 'GLU', 'CA', 'GLU', 10.19), ('CD', 'GLU', 'N', 'GLU', 10.51)], [('OE1', 'GLU', 'CB', 'GLU', 8.82), ('OE1', 'GLU', 'CG', 'GLU', 8.53), ('OE1', 'GLU', 'CD', 'GLU', 7.18), ('OE1', 'GLU', 'OE1', 'GLU', 6.23), ('OE1', 'GLU', 'OE2', 'GLU', 7.44), ('OE1', 'GLU', 'O', 'GLU', 10.82), ('OE1', 'GLU', 'C', 'GLU', 10.91), ('OE1', 'GLU', 'CA', 'GLU', 10.35), ('OE1', 'GLU', 'N', 'GLU', 10.88)], [('OE2', 'GLU', 'CB', 'GLU', 8.53), ('OE2', 'GLU', 'CG', 'GLU', 7.83), ('OE2', 'GLU', 'CD', 'GLU', 6.4), ('OE2', 'GLU', 'OE1', 'GLU', 5.94), ('OE2', 'GLU', 'OE2', 'GLU', 6.22), ('OE2', 'GLU', 'O', 'GLU', 11.04), ('OE2', 'GLU', 'C', 'GLU', 10.86), ('OE2', 'GLU', 'CA', 'GLU', 9.99), ('OE2', 'GLU', 'N', 'GLU', 10.22)], [('O', 'GLU', 'CB', 'GLU', 12.5), ('O', 'GLU', 'CG', 'GLU', 12.67), ('O', 'GLU', 'CD', 'GLU', 11.62), ('O', 'GLU', 'OE1', 'GLU', 10.61), ('O', 'GLU', 'OE2', 'GLU', 12.06), ('O', 'GLU', 'O', 'GLU', 13.86), ('O', 'GLU', 'C', 'GLU', 13.95), ('O', 'GLU', 'CA', 'GLU', 13.83), ('O', 'GLU', 'N', 'GLU', 14.19)], [('C', 'GLU', 'CB', 'GLU', 11.6), ('C', 'GLU', 'CG', 'GLU', 11.85), ('C', 'GLU', 'CD', 'GLU', 10.9), ('C', 'GLU', 'OE1', 'GLU', 9.92), ('C', 'GLU', 'OE2', 'GLU', 11.43), ('C', 'GLU', 'O', 'GLU', 12.9), ('C', 'GLU', 'C', 'GLU', 12.93), ('C', 'GLU', 'CA', 'GLU', 12.87), ('C', 'GLU', 'N', 'GLU', 13.17)], [('CA', 'GLU', 'CB', 'GLU', 10.72), ('CA', 'GLU', 'CG', 'GLU', 10.85), ('CA', 'GLU', 'CD', 'GLU', 9.89), ('CA', 'GLU', 'OE1', 'GLU', 9.03), ('CA', 'GLU', 'OE2', 'GLU', 10.32), ('CA', 'GLU', 'O', 'GLU', 12.31), ('CA', 'GLU', 'C', 'GLU', 12.2), ('CA', 'GLU', 'CA', 'GLU', 11.98), ('CA', 'GLU', 'N', 'GLU', 12.15)], [('N', 'GLU', 'CB', 'GLU', 11.65), ('N', 'GLU', 'CG', 'GLU', 11.59), ('N', 'GLU', 'CD', 'GLU', 10.56), ('N', 'GLU', 'OE1', 'GLU', 9.84), ('N', 'GLU', 'OE2', 'GLU', 10.8), ('N', 'GLU', 'O', 'GLU', 13.47), ('N', 'GLU', 'C', 'GLU', 13.26), ('N', 'GLU', 'CA', 'GLU', 12.91), ('N', 'GLU', 'N', 'GLU', 12.94)]]}
LYS_GLUI = { 
	'distances':
		[[16.83, 15.76, 14.32, 14.11, 13.5, 18.77, 18.91, 18.26, 18.35], [15.33, 14.27, 12.83, 12.61, 12.02, 17.27, 17.4, 16.76, 16.86], [14.68, 13.53, 12.15, 12.08, 11.25, 16.67, 16.79, 16.05, 16.03], [13.17, 12.01, 10.63, 10.59, 9.73, 15.2, 15.29, 14.54, 14.54], [12.9, 11.66, 10.39, 10.52, 9.44, 14.86, 14.98, 14.16, 13.99], [19.58, 18.52, 17.08, 16.84, 16.27, 21.44, 21.62, 21.01, 21.08], [19.05, 18.04, 16.57, 16.26, 15.8, 20.94, 21.09, 20.51, 20.68], [17.6, 16.61, 15.14, 14.8, 14.41, 19.45, 19.61, 19.06, 19.24], [17.67, 16.76, 15.31, 14.89, 14.66, 19.29, 19.55, 19.1, 19.26]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLUI', 16.83), ('CB', 'LYS', 'CG', 'GLUI', 15.76), ('CB', 'LYS', 'CD', 'GLUI', 14.32), ('CB', 'LYS', 'OE1', 'GLUI', 14.11), ('CB', 'LYS', 'OE2', 'GLUI', 13.5), ('CB', 'LYS', 'O', 'GLUI', 18.77), ('CB', 'LYS', 'C', 'GLUI', 18.91), ('CB', 'LYS', 'CA', 'GLUI', 18.26), ('CB', 'LYS', 'N', 'GLUI', 18.35)], [('CG', 'LYS', 'CB', 'GLUI', 15.33), ('CG', 'LYS', 'CG', 'GLUI', 14.27), ('CG', 'LYS', 'CD', 'GLUI', 12.83), ('CG', 'LYS', 'OE1', 'GLUI', 12.61), ('CG', 'LYS', 'OE2', 'GLUI', 12.02), ('CG', 'LYS', 'O', 'GLUI', 17.27), ('CG', 'LYS', 'C', 'GLUI', 17.4), ('CG', 'LYS', 'CA', 'GLUI', 16.76), ('CG', 'LYS', 'N', 'GLUI', 16.86)], [('CD', 'LYS', 'CB', 'GLUI', 14.68), ('CD', 'LYS', 'CG', 'GLUI', 13.53), ('CD', 'LYS', 'CD', 'GLUI', 12.15), ('CD', 'LYS', 'OE1', 'GLUI', 12.08), ('CD', 'LYS', 'OE2', 'GLUI', 11.25), ('CD', 'LYS', 'O', 'GLUI', 16.67), ('CD', 'LYS', 'C', 'GLUI', 16.79), ('CD', 'LYS', 'CA', 'GLUI', 16.05), ('CD', 'LYS', 'N', 'GLUI', 16.03)], [('CE', 'LYS', 'CB', 'GLUI', 13.17), ('CE', 'LYS', 'CG', 'GLUI', 12.01), ('CE', 'LYS', 'CD', 'GLUI', 10.63), ('CE', 'LYS', 'OE1', 'GLUI', 10.59), ('CE', 'LYS', 'OE2', 'GLUI', 9.73), ('CE', 'LYS', 'O', 'GLUI', 15.2), ('CE', 'LYS', 'C', 'GLUI', 15.29), ('CE', 'LYS', 'CA', 'GLUI', 14.54), ('CE', 'LYS', 'N', 'GLUI', 14.54)], [('NZ', 'LYS', 'CB', 'GLUI', 12.9), ('NZ', 'LYS', 'CG', 'GLUI', 11.66), ('NZ', 'LYS', 'CD', 'GLUI', 10.39), ('NZ', 'LYS', 'OE1', 'GLUI', 10.52), ('NZ', 'LYS', 'OE2', 'GLUI', 9.44), ('NZ', 'LYS', 'O', 'GLUI', 14.86), ('NZ', 'LYS', 'C', 'GLUI', 14.98), ('NZ', 'LYS', 'CA', 'GLUI', 14.16), ('NZ', 'LYS', 'N', 'GLUI', 13.99)], [('O', 'LYS', 'CB', 'GLUI', 19.58), ('O', 'LYS', 'CG', 'GLUI', 18.52), ('O', 'LYS', 'CD', 'GLUI', 17.08), ('O', 'LYS', 'OE1', 'GLUI', 16.84), ('O', 'LYS', 'OE2', 'GLUI', 16.27), ('O', 'LYS', 'O', 'GLUI', 21.44), ('O', 'LYS', 'C', 'GLUI', 21.62), ('O', 'LYS', 'CA', 'GLUI', 21.01), ('O', 'LYS', 'N', 'GLUI', 21.08)], [('C', 'LYS', 'CB', 'GLUI', 19.05), ('C', 'LYS', 'CG', 'GLUI', 18.04), ('C', 'LYS', 'CD', 'GLUI', 16.57), ('C', 'LYS', 'OE1', 'GLUI', 16.26), ('C', 'LYS', 'OE2', 'GLUI', 15.8), ('C', 'LYS', 'O', 'GLUI', 20.94), ('C', 'LYS', 'C', 'GLUI', 21.09), ('C', 'LYS', 'CA', 'GLUI', 20.51), ('C', 'LYS', 'N', 'GLUI', 20.68)], [('CA', 'LYS', 'CB', 'GLUI', 17.6), ('CA', 'LYS', 'CG', 'GLUI', 16.61), ('CA', 'LYS', 'CD', 'GLUI', 15.14), ('CA', 'LYS', 'OE1', 'GLUI', 14.8), ('CA', 'LYS', 'OE2', 'GLUI', 14.41), ('CA', 'LYS', 'O', 'GLUI', 19.45), ('CA', 'LYS', 'C', 'GLUI', 19.61), ('CA', 'LYS', 'CA', 'GLUI', 19.06), ('CA', 'LYS', 'N', 'GLUI', 19.24)], [('N', 'LYS', 'CB', 'GLUI', 17.67), ('N', 'LYS', 'CG', 'GLUI', 16.76), ('N', 'LYS', 'CD', 'GLUI', 15.31), ('N', 'LYS', 'OE1', 'GLUI', 14.89), ('N', 'LYS', 'OE2', 'GLUI', 14.66), ('N', 'LYS', 'O', 'GLUI', 19.29), ('N', 'LYS', 'C', 'GLUI', 19.55), ('N', 'LYS', 'CA', 'GLUI', 19.1), ('N', 'LYS', 'N', 'GLUI', 19.26)]]}
HIS_GLU = { 
	'distances':
		[[9.26, 8.66, 8.49, 8.71, 8.49, 10.25, 10.65, 9.85, 10.85], [8.03, 7.44, 7.13, 7.24, 7.23, 9.26, 9.63, 8.82, 9.84], [6.87, 6.49, 6.46, 6.56, 6.84, 7.9, 8.3, 7.57, 8.68], [8.01, 7.29, 6.62, 6.6, 6.61, 9.6, 9.92, 9.04, 9.99], [5.99, 5.63, 5.37, 5.27, 5.93, 7.38, 7.73, 6.98, 8.08], [6.8, 6.19, 5.45, 5.27, 5.71, 8.52, 8.81, 7.97, 8.94], [10.41, 9.32, 8.59, 8.9, 8.01, 12.28, 12.43, 11.33, 12.0], [10.17, 9.17, 8.67, 9.06, 8.21, 11.82, 12.0, 10.93, 11.66], [10.42, 9.66, 9.28, 9.5, 9.06, 11.65, 12.0, 11.12, 12.03], [10.92, 10.22, 9.63, 9.64, 9.47, 12.15, 12.59, 11.79, 12.77], [13.67, 12.96, 11.61, 11.17, 11.11, 16.14, 15.77, 15.18, 15.94], [12.19, 11.5, 10.17, 9.74, 9.73, 14.69, 14.3, 13.69, 14.47], [11.81, 11.2, 9.99, 9.6, 9.63, 14.38, 13.87, 13.25, 14.12], [11.14, 10.4, 9.01, 8.57, 8.56, 13.6, 13.28, 12.67, 13.38], [10.48, 9.89, 8.73, 8.35, 8.44, 13.08, 12.55, 11.91, 12.79], [10.01, 9.32, 8.02, 7.61, 7.65, 12.57, 12.15, 11.51, 12.29], [13.02, 12.03, 10.57, 10.31, 9.81, 15.44, 15.25, 14.54, 14.97], [13.64, 12.7, 11.26, 10.99, 10.54, 16.13, 15.87, 15.16, 15.68], [14.13, 13.34, 11.91, 11.47, 11.34, 16.51, 16.26, 15.67, 16.32], [13.71, 13.0, 11.54, 10.96, 11.07, 15.88, 15.73, 15.26, 15.92]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 9.26), ('CB', 'HIS', 'CG', 'GLU', 8.66), ('CB', 'HIS', 'CD', 'GLU', 8.49), ('CB', 'HIS', 'OE1', 'GLU', 8.71), ('CB', 'HIS', 'OE2', 'GLU', 8.49), ('CB', 'HIS', 'O', 'GLU', 10.25), ('CB', 'HIS', 'C', 'GLU', 10.65), ('CB', 'HIS', 'CA', 'GLU', 9.85), ('CB', 'HIS', 'N', 'GLU', 10.85)], [('CG', 'HIS', 'CB', 'GLU', 8.03), ('CG', 'HIS', 'CG', 'GLU', 7.44), ('CG', 'HIS', 'CD', 'GLU', 7.13), ('CG', 'HIS', 'OE1', 'GLU', 7.24), ('CG', 'HIS', 'OE2', 'GLU', 7.23), ('CG', 'HIS', 'O', 'GLU', 9.26), ('CG', 'HIS', 'C', 'GLU', 9.63), ('CG', 'HIS', 'CA', 'GLU', 8.82), ('CG', 'HIS', 'N', 'GLU', 9.84)], [('ND1', 'HIS', 'CB', 'GLU', 6.87), ('ND1', 'HIS', 'CG', 'GLU', 6.49), ('ND1', 'HIS', 'CD', 'GLU', 6.46), ('ND1', 'HIS', 'OE1', 'GLU', 6.56), ('ND1', 'HIS', 'OE2', 'GLU', 6.84), ('ND1', 'HIS', 'O', 'GLU', 7.9), ('ND1', 'HIS', 'C', 'GLU', 8.3), ('ND1', 'HIS', 'CA', 'GLU', 7.57), ('ND1', 'HIS', 'N', 'GLU', 8.68)], [('CD2', 'HIS', 'CB', 'GLU', 8.01), ('CD2', 'HIS', 'CG', 'GLU', 7.29), ('CD2', 'HIS', 'CD', 'GLU', 6.62), ('CD2', 'HIS', 'OE1', 'GLU', 6.6), ('CD2', 'HIS', 'OE2', 'GLU', 6.61), ('CD2', 'HIS', 'O', 'GLU', 9.6), ('CD2', 'HIS', 'C', 'GLU', 9.92), ('CD2', 'HIS', 'CA', 'GLU', 9.04), ('CD2', 'HIS', 'N', 'GLU', 9.99)], [('CE1', 'HIS', 'CB', 'GLU', 5.99), ('CE1', 'HIS', 'CG', 'GLU', 5.63), ('CE1', 'HIS', 'CD', 'GLU', 5.37), ('CE1', 'HIS', 'OE1', 'GLU', 5.27), ('CE1', 'HIS', 'OE2', 'GLU', 5.93), ('CE1', 'HIS', 'O', 'GLU', 7.38), ('CE1', 'HIS', 'C', 'GLU', 7.73), ('CE1', 'HIS', 'CA', 'GLU', 6.98), ('CE1', 'HIS', 'N', 'GLU', 8.08)], [('NE2', 'HIS', 'CB', 'GLU', 6.8), ('NE2', 'HIS', 'CG', 'GLU', 6.19), ('NE2', 'HIS', 'CD', 'GLU', 5.45), ('NE2', 'HIS', 'OE1', 'GLU', 5.27), ('NE2', 'HIS', 'OE2', 'GLU', 5.71), ('NE2', 'HIS', 'O', 'GLU', 8.52), ('NE2', 'HIS', 'C', 'GLU', 8.81), ('NE2', 'HIS', 'CA', 'GLU', 7.97), ('NE2', 'HIS', 'N', 'GLU', 8.94)], [('O', 'HIS', 'CB', 'GLU', 10.41), ('O', 'HIS', 'CG', 'GLU', 9.32), ('O', 'HIS', 'CD', 'GLU', 8.59), ('O', 'HIS', 'OE1', 'GLU', 8.9), ('O', 'HIS', 'OE2', 'GLU', 8.01), ('O', 'HIS', 'O', 'GLU', 12.28), ('O', 'HIS', 'C', 'GLU', 12.43), ('O', 'HIS', 'CA', 'GLU', 11.33), ('O', 'HIS', 'N', 'GLU', 12.0)], [('C', 'HIS', 'CB', 'GLU', 10.17), ('C', 'HIS', 'CG', 'GLU', 9.17), ('C', 'HIS', 'CD', 'GLU', 8.67), ('C', 'HIS', 'OE1', 'GLU', 9.06), ('C', 'HIS', 'OE2', 'GLU', 8.21), ('C', 'HIS', 'O', 'GLU', 11.82), ('C', 'HIS', 'C', 'GLU', 12.0), ('C', 'HIS', 'CA', 'GLU', 10.93), ('C', 'HIS', 'N', 'GLU', 11.66)], [('CA', 'HIS', 'CB', 'GLU', 10.42), ('CA', 'HIS', 'CG', 'GLU', 9.66), ('CA', 'HIS', 'CD', 'GLU', 9.28), ('CA', 'HIS', 'OE1', 'GLU', 9.5), ('CA', 'HIS', 'OE2', 'GLU', 9.06), ('CA', 'HIS', 'O', 'GLU', 11.65), ('CA', 'HIS', 'C', 'GLU', 12.0), ('CA', 'HIS', 'CA', 'GLU', 11.12), ('CA', 'HIS', 'N', 'GLU', 12.03)], [('N', 'HIS', 'CB', 'GLU', 10.92), ('N', 'HIS', 'CG', 'GLU', 10.22), ('N', 'HIS', 'CD', 'GLU', 9.63), ('N', 'HIS', 'OE1', 'GLU', 9.64), ('N', 'HIS', 'OE2', 'GLU', 9.47), ('N', 'HIS', 'O', 'GLU', 12.15), ('N', 'HIS', 'C', 'GLU', 12.59), ('N', 'HIS', 'CA', 'GLU', 11.79), ('N', 'HIS', 'N', 'GLU', 12.77)], [('CB', 'HIS', 'CB', 'GLU', 13.67), ('CB', 'HIS', 'CG', 'GLU', 12.96), ('CB', 'HIS', 'CD', 'GLU', 11.61), ('CB', 'HIS', 'OE1', 'GLU', 11.17), ('CB', 'HIS', 'OE2', 'GLU', 11.11), ('CB', 'HIS', 'O', 'GLU', 16.14), ('CB', 'HIS', 'C', 'GLU', 15.77), ('CB', 'HIS', 'CA', 'GLU', 15.18), ('CB', 'HIS', 'N', 'GLU', 15.94)], [('CG', 'HIS', 'CB', 'GLU', 12.19), ('CG', 'HIS', 'CG', 'GLU', 11.5), ('CG', 'HIS', 'CD', 'GLU', 10.17), ('CG', 'HIS', 'OE1', 'GLU', 9.74), ('CG', 'HIS', 'OE2', 'GLU', 9.73), ('CG', 'HIS', 'O', 'GLU', 14.69), ('CG', 'HIS', 'C', 'GLU', 14.3), ('CG', 'HIS', 'CA', 'GLU', 13.69), ('CG', 'HIS', 'N', 'GLU', 14.47)], [('ND1', 'HIS', 'CB', 'GLU', 11.81), ('ND1', 'HIS', 'CG', 'GLU', 11.2), ('ND1', 'HIS', 'CD', 'GLU', 9.99), ('ND1', 'HIS', 'OE1', 'GLU', 9.6), ('ND1', 'HIS', 'OE2', 'GLU', 9.63), ('ND1', 'HIS', 'O', 'GLU', 14.38), ('ND1', 'HIS', 'C', 'GLU', 13.87), ('ND1', 'HIS', 'CA', 'GLU', 13.25), ('ND1', 'HIS', 'N', 'GLU', 14.12)], [('CD2', 'HIS', 'CB', 'GLU', 11.14), ('CD2', 'HIS', 'CG', 'GLU', 10.4), ('CD2', 'HIS', 'CD', 'GLU', 9.01), ('CD2', 'HIS', 'OE1', 'GLU', 8.57), ('CD2', 'HIS', 'OE2', 'GLU', 8.56), ('CD2', 'HIS', 'O', 'GLU', 13.6), ('CD2', 'HIS', 'C', 'GLU', 13.28), ('CD2', 'HIS', 'CA', 'GLU', 12.67), ('CD2', 'HIS', 'N', 'GLU', 13.38)], [('CE1', 'HIS', 'CB', 'GLU', 10.48), ('CE1', 'HIS', 'CG', 'GLU', 9.89), ('CE1', 'HIS', 'CD', 'GLU', 8.73), ('CE1', 'HIS', 'OE1', 'GLU', 8.35), ('CE1', 'HIS', 'OE2', 'GLU', 8.44), ('CE1', 'HIS', 'O', 'GLU', 13.08), ('CE1', 'HIS', 'C', 'GLU', 12.55), ('CE1', 'HIS', 'CA', 'GLU', 11.91), ('CE1', 'HIS', 'N', 'GLU', 12.79)], [('NE2', 'HIS', 'CB', 'GLU', 10.01), ('NE2', 'HIS', 'CG', 'GLU', 9.32), ('NE2', 'HIS', 'CD', 'GLU', 8.02), ('NE2', 'HIS', 'OE1', 'GLU', 7.61), ('NE2', 'HIS', 'OE2', 'GLU', 7.65), ('NE2', 'HIS', 'O', 'GLU', 12.57), ('NE2', 'HIS', 'C', 'GLU', 12.15), ('NE2', 'HIS', 'CA', 'GLU', 11.51), ('NE2', 'HIS', 'N', 'GLU', 12.29)], [('O', 'HIS', 'CB', 'GLU', 13.02), ('O', 'HIS', 'CG', 'GLU', 12.03), ('O', 'HIS', 'CD', 'GLU', 10.57), ('O', 'HIS', 'OE1', 'GLU', 10.31), ('O', 'HIS', 'OE2', 'GLU', 9.81), ('O', 'HIS', 'O', 'GLU', 15.44), ('O', 'HIS', 'C', 'GLU', 15.25), ('O', 'HIS', 'CA', 'GLU', 14.54), ('O', 'HIS', 'N', 'GLU', 14.97)], [('C', 'HIS', 'CB', 'GLU', 13.64), ('C', 'HIS', 'CG', 'GLU', 12.7), ('C', 'HIS', 'CD', 'GLU', 11.26), ('C', 'HIS', 'OE1', 'GLU', 10.99), ('C', 'HIS', 'OE2', 'GLU', 10.54), ('C', 'HIS', 'O', 'GLU', 16.13), ('C', 'HIS', 'C', 'GLU', 15.87), ('C', 'HIS', 'CA', 'GLU', 15.16), ('C', 'HIS', 'N', 'GLU', 15.68)], [('CA', 'HIS', 'CB', 'GLU', 14.13), ('CA', 'HIS', 'CG', 'GLU', 13.34), ('CA', 'HIS', 'CD', 'GLU', 11.91), ('CA', 'HIS', 'OE1', 'GLU', 11.47), ('CA', 'HIS', 'OE2', 'GLU', 11.34), ('CA', 'HIS', 'O', 'GLU', 16.51), ('CA', 'HIS', 'C', 'GLU', 16.26), ('CA', 'HIS', 'CA', 'GLU', 15.67), ('CA', 'HIS', 'N', 'GLU', 16.32)], [('N', 'HIS', 'CB', 'GLU', 13.71), ('N', 'HIS', 'CG', 'GLU', 13.0), ('N', 'HIS', 'CD', 'GLU', 11.54), ('N', 'HIS', 'OE1', 'GLU', 10.96), ('N', 'HIS', 'OE2', 'GLU', 11.07), ('N', 'HIS', 'O', 'GLU', 15.88), ('N', 'HIS', 'C', 'GLU', 15.73), ('N', 'HIS', 'CA', 'GLU', 15.26), ('N', 'HIS', 'N', 'GLU', 15.92)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'A_5enl_4_2_1_11')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LYS, d, 'A_5enl_4_2_1_11')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_GLU, d, 'A_5enl_4_2_1_11')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_GLUI, d, 'A_5enl_4_2_1_11')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_GLU, d, 'A_5enl_4_2_1_11')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'GLU_LYS' :  match2,
		'GLU_GLU' :  match3,
		'LYS_GLUI' :  match4,
		'HIS_GLU' :  match5}