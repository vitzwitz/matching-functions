'''
FUNC:A_1eh5_3_1_2_22
PDB:1eh5
EC:3.1.2.22
RESI:met,ser,gln,asp,his
LOCI:a-41,115,116,233,289;
'''
import motifFunctions as cmd
GLN_HIS = { 
	'distances':
		[[13.35, 11.9, 11.52, 10.86, 10.23, 9.74], [13.48, 12.07, 11.87, 10.91, 10.61, 9.92], [14.17, 12.83, 12.75, 11.62, 11.54, 10.76], [14.07, 12.76, 12.69, 11.6, 11.52, 10.76], [15.04, 13.73, 13.74, 12.48, 12.55, 11.69], [14.95, 13.46, 12.81, 12.58, 11.49, 11.31], [13.92, 12.43, 11.86, 11.51, 10.54, 10.26], [12.84, 11.35, 10.81, 10.42, 9.5, 9.18], [11.53, 10.04, 9.56, 9.08, 8.24, 7.86]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'HIS', 13.35), ('CB', 'GLN', 'CG', 'HIS', 11.9), ('CB', 'GLN', 'ND1', 'HIS', 11.52), ('CB', 'GLN', 'CD2', 'HIS', 10.86), ('CB', 'GLN', 'CE1', 'HIS', 10.23), ('CB', 'GLN', 'NE2', 'HIS', 9.74)], [('CG', 'GLN', 'CB', 'HIS', 13.48), ('CG', 'GLN', 'CG', 'HIS', 12.07), ('CG', 'GLN', 'ND1', 'HIS', 11.87), ('CG', 'GLN', 'CD2', 'HIS', 10.91), ('CG', 'GLN', 'CE1', 'HIS', 10.61), ('CG', 'GLN', 'NE2', 'HIS', 9.92)], [('CD', 'GLN', 'CB', 'HIS', 14.17), ('CD', 'GLN', 'CG', 'HIS', 12.83), ('CD', 'GLN', 'ND1', 'HIS', 12.75), ('CD', 'GLN', 'CD2', 'HIS', 11.62), ('CD', 'GLN', 'CE1', 'HIS', 11.54), ('CD', 'GLN', 'NE2', 'HIS', 10.76)], [('OE1', 'GLN', 'CB', 'HIS', 14.07), ('OE1', 'GLN', 'CG', 'HIS', 12.76), ('OE1', 'GLN', 'ND1', 'HIS', 12.69), ('OE1', 'GLN', 'CD2', 'HIS', 11.6), ('OE1', 'GLN', 'CE1', 'HIS', 11.52), ('OE1', 'GLN', 'NE2', 'HIS', 10.76)], [('NE2', 'GLN', 'CB', 'HIS', 15.04), ('NE2', 'GLN', 'CG', 'HIS', 13.73), ('NE2', 'GLN', 'ND1', 'HIS', 13.74), ('NE2', 'GLN', 'CD2', 'HIS', 12.48), ('NE2', 'GLN', 'CE1', 'HIS', 12.55), ('NE2', 'GLN', 'NE2', 'HIS', 11.69)], [('O', 'GLN', 'CB', 'HIS', 14.95), ('O', 'GLN', 'CG', 'HIS', 13.46), ('O', 'GLN', 'ND1', 'HIS', 12.81), ('O', 'GLN', 'CD2', 'HIS', 12.58), ('O', 'GLN', 'CE1', 'HIS', 11.49), ('O', 'GLN', 'NE2', 'HIS', 11.31)], [('C', 'GLN', 'CB', 'HIS', 13.92), ('C', 'GLN', 'CG', 'HIS', 12.43), ('C', 'GLN', 'ND1', 'HIS', 11.86), ('C', 'GLN', 'CD2', 'HIS', 11.51), ('C', 'GLN', 'CE1', 'HIS', 10.54), ('C', 'GLN', 'NE2', 'HIS', 10.26)], [('CA', 'GLN', 'CB', 'HIS', 12.84), ('CA', 'GLN', 'CG', 'HIS', 11.35), ('CA', 'GLN', 'ND1', 'HIS', 10.81), ('CA', 'GLN', 'CD2', 'HIS', 10.42), ('CA', 'GLN', 'CE1', 'HIS', 9.5), ('CA', 'GLN', 'NE2', 'HIS', 9.18)], [('N', 'GLN', 'CB', 'HIS', 11.53), ('N', 'GLN', 'CG', 'HIS', 10.04), ('N', 'GLN', 'ND1', 'HIS', 9.56), ('N', 'GLN', 'CD2', 'HIS', 9.08), ('N', 'GLN', 'CE1', 'HIS', 8.24), ('N', 'GLN', 'NE2', 'HIS', 7.86)]]}
ASP_HIS = { 
	'distances':
		[[7.04, 7.52, 7.04, 8.78, 8.11, 9.07], [5.8, 6.09, 5.6, 7.31, 6.67, 7.57], [5.58, 5.88, 5.65, 6.96, 6.64, 7.34], [5.53, 5.54, 4.78, 6.76, 5.83, 6.87]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.04), ('CB', 'ASP', 'CG', 'HIS', 7.52), ('CB', 'ASP', 'ND1', 'HIS', 7.04), ('CB', 'ASP', 'CD2', 'HIS', 8.78), ('CB', 'ASP', 'CE1', 'HIS', 8.11), ('CB', 'ASP', 'NE2', 'HIS', 9.07)], [('CG', 'ASP', 'CB', 'HIS', 5.8), ('CG', 'ASP', 'CG', 'HIS', 6.09), ('CG', 'ASP', 'ND1', 'HIS', 5.6), ('CG', 'ASP', 'CD2', 'HIS', 7.31), ('CG', 'ASP', 'CE1', 'HIS', 6.67), ('CG', 'ASP', 'NE2', 'HIS', 7.57)], [('OD1', 'ASP', 'CB', 'HIS', 5.58), ('OD1', 'ASP', 'CG', 'HIS', 5.88), ('OD1', 'ASP', 'ND1', 'HIS', 5.65), ('OD1', 'ASP', 'CD2', 'HIS', 6.96), ('OD1', 'ASP', 'CE1', 'HIS', 6.64), ('OD1', 'ASP', 'NE2', 'HIS', 7.34)], [('OD2', 'ASP', 'CB', 'HIS', 5.53), ('OD2', 'ASP', 'CG', 'HIS', 5.54), ('OD2', 'ASP', 'ND1', 'HIS', 4.78), ('OD2', 'ASP', 'CD2', 'HIS', 6.76), ('OD2', 'ASP', 'CE1', 'HIS', 5.83), ('OD2', 'ASP', 'NE2', 'HIS', 6.87)]]}
SER_MET = { 
	'distances':
		[[7.76, 9.18, 9.56, 9.44, 8.32, 8.65, 7.84, 6.66], [7.27, 8.57, 8.68, 8.38, 8.4, 8.64, 7.72, 6.79]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'MET', 7.76), ('CB', 'SER', 'CG', 'MET', 9.18), ('CB', 'SER', 'SD', 'MET', 9.56), ('CB', 'SER', 'CE', 'MET', 9.44), ('CB', 'SER', 'O', 'MET', 8.32), ('CB', 'SER', 'C', 'MET', 8.65), ('CB', 'SER', 'CA', 'MET', 7.84), ('CB', 'SER', 'N', 'MET', 6.66)], [('OG', 'SER', 'CB', 'MET', 7.27), ('OG', 'SER', 'CG', 'MET', 8.57), ('OG', 'SER', 'SD', 'MET', 8.68), ('OG', 'SER', 'CE', 'MET', 8.38), ('OG', 'SER', 'O', 'MET', 8.4), ('OG', 'SER', 'C', 'MET', 8.64), ('OG', 'SER', 'CA', 'MET', 7.72), ('OG', 'SER', 'N', 'MET', 6.79)]]}
GLN_ASP = { 
	'distances':
		[[15.72, 14.33, 13.97, 13.71], [16.35, 14.91, 14.5, 14.27], [17.13, 15.68, 15.15, 15.14], [16.83, 15.4, 14.79, 14.96], [18.25, 16.77, 16.24, 16.22], [16.85, 15.58, 15.48, 14.78], [16.11, 14.79, 14.66, 13.98], [15.01, 13.66, 13.45, 12.94], [13.97, 12.59, 12.4, 11.82]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'ASP', 15.72), ('CB', 'GLN', 'CG', 'ASP', 14.33), ('CB', 'GLN', 'OD1', 'ASP', 13.97), ('CB', 'GLN', 'OD2', 'ASP', 13.71)], [('CG', 'GLN', 'CB', 'ASP', 16.35), ('CG', 'GLN', 'CG', 'ASP', 14.91), ('CG', 'GLN', 'OD1', 'ASP', 14.5), ('CG', 'GLN', 'OD2', 'ASP', 14.27)], [('CD', 'GLN', 'CB', 'ASP', 17.13), ('CD', 'GLN', 'CG', 'ASP', 15.68), ('CD', 'GLN', 'OD1', 'ASP', 15.15), ('CD', 'GLN', 'OD2', 'ASP', 15.14)], [('OE1', 'GLN', 'CB', 'ASP', 16.83), ('OE1', 'GLN', 'CG', 'ASP', 15.4), ('OE1', 'GLN', 'OD1', 'ASP', 14.79), ('OE1', 'GLN', 'OD2', 'ASP', 14.96)], [('NE2', 'GLN', 'CB', 'ASP', 18.25), ('NE2', 'GLN', 'CG', 'ASP', 16.77), ('NE2', 'GLN', 'OD1', 'ASP', 16.24), ('NE2', 'GLN', 'OD2', 'ASP', 16.22)], [('O', 'GLN', 'CB', 'ASP', 16.85), ('O', 'GLN', 'CG', 'ASP', 15.58), ('O', 'GLN', 'OD1', 'ASP', 15.48), ('O', 'GLN', 'OD2', 'ASP', 14.78)], [('C', 'GLN', 'CB', 'ASP', 16.11), ('C', 'GLN', 'CG', 'ASP', 14.79), ('C', 'GLN', 'OD1', 'ASP', 14.66), ('C', 'GLN', 'OD2', 'ASP', 13.98)], [('CA', 'GLN', 'CB', 'ASP', 15.01), ('CA', 'GLN', 'CG', 'ASP', 13.66), ('CA', 'GLN', 'OD1', 'ASP', 13.45), ('CA', 'GLN', 'OD2', 'ASP', 12.94)], [('N', 'GLN', 'CB', 'ASP', 13.97), ('N', 'GLN', 'CG', 'ASP', 12.59), ('N', 'GLN', 'OD1', 'ASP', 12.4), ('N', 'GLN', 'OD2', 'ASP', 11.82)]]}
MET_ASP = { 
	'distances':
		[[16.15, 14.64, 13.94, 14.25], [16.89, 15.41, 14.6, 15.14], [15.98, 14.54, 13.62, 14.43], [15.93, 14.52, 13.63, 14.4], [16.52, 15.01, 14.39, 14.55], [17.3, 15.78, 15.15, 15.32], [16.96, 15.44, 14.83, 14.94], [16.34, 14.82, 14.33, 14.22]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'ASP', 16.15), ('CB', 'MET', 'CG', 'ASP', 14.64), ('CB', 'MET', 'OD1', 'ASP', 13.94), ('CB', 'MET', 'OD2', 'ASP', 14.25)], [('CG', 'MET', 'CB', 'ASP', 16.89), ('CG', 'MET', 'CG', 'ASP', 15.41), ('CG', 'MET', 'OD1', 'ASP', 14.6), ('CG', 'MET', 'OD2', 'ASP', 15.14)], [('SD', 'MET', 'CB', 'ASP', 15.98), ('SD', 'MET', 'CG', 'ASP', 14.54), ('SD', 'MET', 'OD1', 'ASP', 13.62), ('SD', 'MET', 'OD2', 'ASP', 14.43)], [('CE', 'MET', 'CB', 'ASP', 15.93), ('CE', 'MET', 'CG', 'ASP', 14.52), ('CE', 'MET', 'OD1', 'ASP', 13.63), ('CE', 'MET', 'OD2', 'ASP', 14.4)], [('O', 'MET', 'CB', 'ASP', 16.52), ('O', 'MET', 'CG', 'ASP', 15.01), ('O', 'MET', 'OD1', 'ASP', 14.39), ('O', 'MET', 'OD2', 'ASP', 14.55)], [('C', 'MET', 'CB', 'ASP', 17.3), ('C', 'MET', 'CG', 'ASP', 15.78), ('C', 'MET', 'OD1', 'ASP', 15.15), ('C', 'MET', 'OD2', 'ASP', 15.32)], [('CA', 'MET', 'CB', 'ASP', 16.96), ('CA', 'MET', 'CG', 'ASP', 15.44), ('CA', 'MET', 'OD1', 'ASP', 14.83), ('CA', 'MET', 'OD2', 'ASP', 14.94)], [('N', 'MET', 'CB', 'ASP', 16.34), ('N', 'MET', 'CG', 'ASP', 14.82), ('N', 'MET', 'OD1', 'ASP', 14.33), ('N', 'MET', 'OD2', 'ASP', 14.22)]]}
MET_HIS = { 
	'distances':
		[[12.42, 11.34, 11.71, 10.03, 10.77, 9.65], [13.21, 12.23, 12.7, 10.96, 11.85, 10.71], [12.58, 11.71, 12.21, 10.55, 11.47, 10.4], [13.01, 12.01, 12.29, 10.9, 11.45, 10.53], [12.07, 11.19, 11.86, 9.86, 11.11, 9.83], [13.02, 12.07, 12.63, 10.72, 11.79, 10.55], [13.0, 11.9, 12.29, 10.55, 11.31, 10.16], [12.43, 11.24, 11.52, 9.91, 10.47, 9.38]],
	'comparisons':
		[[('CB', 'MET', 'CB', 'HIS', 12.42), ('CB', 'MET', 'CG', 'HIS', 11.34), ('CB', 'MET', 'ND1', 'HIS', 11.71), ('CB', 'MET', 'CD2', 'HIS', 10.03), ('CB', 'MET', 'CE1', 'HIS', 10.77), ('CB', 'MET', 'NE2', 'HIS', 9.65)], [('CG', 'MET', 'CB', 'HIS', 13.21), ('CG', 'MET', 'CG', 'HIS', 12.23), ('CG', 'MET', 'ND1', 'HIS', 12.7), ('CG', 'MET', 'CD2', 'HIS', 10.96), ('CG', 'MET', 'CE1', 'HIS', 11.85), ('CG', 'MET', 'NE2', 'HIS', 10.71)], [('SD', 'MET', 'CB', 'HIS', 12.58), ('SD', 'MET', 'CG', 'HIS', 11.71), ('SD', 'MET', 'ND1', 'HIS', 12.21), ('SD', 'MET', 'CD2', 'HIS', 10.55), ('SD', 'MET', 'CE1', 'HIS', 11.47), ('SD', 'MET', 'NE2', 'HIS', 10.4)], [('CE', 'MET', 'CB', 'HIS', 13.01), ('CE', 'MET', 'CG', 'HIS', 12.01), ('CE', 'MET', 'ND1', 'HIS', 12.29), ('CE', 'MET', 'CD2', 'HIS', 10.9), ('CE', 'MET', 'CE1', 'HIS', 11.45), ('CE', 'MET', 'NE2', 'HIS', 10.53)], [('O', 'MET', 'CB', 'HIS', 12.07), ('O', 'MET', 'CG', 'HIS', 11.19), ('O', 'MET', 'ND1', 'HIS', 11.86), ('O', 'MET', 'CD2', 'HIS', 9.86), ('O', 'MET', 'CE1', 'HIS', 11.11), ('O', 'MET', 'NE2', 'HIS', 9.83)], [('C', 'MET', 'CB', 'HIS', 13.02), ('C', 'MET', 'CG', 'HIS', 12.07), ('C', 'MET', 'ND1', 'HIS', 12.63), ('C', 'MET', 'CD2', 'HIS', 10.72), ('C', 'MET', 'CE1', 'HIS', 11.79), ('C', 'MET', 'NE2', 'HIS', 10.55)], [('CA', 'MET', 'CB', 'HIS', 13.0), ('CA', 'MET', 'CG', 'HIS', 11.9), ('CA', 'MET', 'ND1', 'HIS', 12.29), ('CA', 'MET', 'CD2', 'HIS', 10.55), ('CA', 'MET', 'CE1', 'HIS', 11.31), ('CA', 'MET', 'NE2', 'HIS', 10.16)], [('N', 'MET', 'CB', 'HIS', 12.43), ('N', 'MET', 'CG', 'HIS', 11.24), ('N', 'MET', 'ND1', 'HIS', 11.52), ('N', 'MET', 'CD2', 'HIS', 9.91), ('N', 'MET', 'CE1', 'HIS', 10.47), ('N', 'MET', 'NE2', 'HIS', 9.38)]]}
GLN_MET = { 
	'distances':
		[[7.33, 8.47, 9.03, 8.06, 9.57, 9.08, 7.6, 6.9], [6.29, 7.5, 8.41, 7.7, 8.34, 7.76, 6.27, 5.57], [5.64, 6.54, 7.52, 6.73, 8.1, 7.31, 5.78, 5.63], [5.63, 6.26, 6.88, 5.81, 8.47, 7.71, 6.23, 6.34], [5.76, 6.52, 7.83, 7.28, 7.89, 6.92, 5.5, 5.53], [10.2, 11.42, 12.12, 11.16, 11.97, 11.52, 10.11, 9.13], [9.26, 10.57, 11.3, 10.48, 10.88, 10.51, 9.15, 8.08], [8.35, 9.62, 10.14, 9.27, 10.2, 9.89, 8.5, 7.54], [7.98, 9.36, 9.84, 9.21, 9.44, 9.34, 8.11, 6.99]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'MET', 7.33), ('CB', 'GLN', 'CG', 'MET', 8.47), ('CB', 'GLN', 'SD', 'MET', 9.03), ('CB', 'GLN', 'CE', 'MET', 8.06), ('CB', 'GLN', 'O', 'MET', 9.57), ('CB', 'GLN', 'C', 'MET', 9.08), ('CB', 'GLN', 'CA', 'MET', 7.6), ('CB', 'GLN', 'N', 'MET', 6.9)], [('CG', 'GLN', 'CB', 'MET', 6.29), ('CG', 'GLN', 'CG', 'MET', 7.5), ('CG', 'GLN', 'SD', 'MET', 8.41), ('CG', 'GLN', 'CE', 'MET', 7.7), ('CG', 'GLN', 'O', 'MET', 8.34), ('CG', 'GLN', 'C', 'MET', 7.76), ('CG', 'GLN', 'CA', 'MET', 6.27), ('CG', 'GLN', 'N', 'MET', 5.57)], [('CD', 'GLN', 'CB', 'MET', 5.64), ('CD', 'GLN', 'CG', 'MET', 6.54), ('CD', 'GLN', 'SD', 'MET', 7.52), ('CD', 'GLN', 'CE', 'MET', 6.73), ('CD', 'GLN', 'O', 'MET', 8.1), ('CD', 'GLN', 'C', 'MET', 7.31), ('CD', 'GLN', 'CA', 'MET', 5.78), ('CD', 'GLN', 'N', 'MET', 5.63)], [('OE1', 'GLN', 'CB', 'MET', 5.63), ('OE1', 'GLN', 'CG', 'MET', 6.26), ('OE1', 'GLN', 'SD', 'MET', 6.88), ('OE1', 'GLN', 'CE', 'MET', 5.81), ('OE1', 'GLN', 'O', 'MET', 8.47), ('OE1', 'GLN', 'C', 'MET', 7.71), ('OE1', 'GLN', 'CA', 'MET', 6.23), ('OE1', 'GLN', 'N', 'MET', 6.34)], [('NE2', 'GLN', 'CB', 'MET', 5.76), ('NE2', 'GLN', 'CG', 'MET', 6.52), ('NE2', 'GLN', 'SD', 'MET', 7.83), ('NE2', 'GLN', 'CE', 'MET', 7.28), ('NE2', 'GLN', 'O', 'MET', 7.89), ('NE2', 'GLN', 'C', 'MET', 6.92), ('NE2', 'GLN', 'CA', 'MET', 5.5), ('NE2', 'GLN', 'N', 'MET', 5.53)], [('O', 'GLN', 'CB', 'MET', 10.2), ('O', 'GLN', 'CG', 'MET', 11.42), ('O', 'GLN', 'SD', 'MET', 12.12), ('O', 'GLN', 'CE', 'MET', 11.16), ('O', 'GLN', 'O', 'MET', 11.97), ('O', 'GLN', 'C', 'MET', 11.52), ('O', 'GLN', 'CA', 'MET', 10.11), ('O', 'GLN', 'N', 'MET', 9.13)], [('C', 'GLN', 'CB', 'MET', 9.26), ('C', 'GLN', 'CG', 'MET', 10.57), ('C', 'GLN', 'SD', 'MET', 11.3), ('C', 'GLN', 'CE', 'MET', 10.48), ('C', 'GLN', 'O', 'MET', 10.88), ('C', 'GLN', 'C', 'MET', 10.51), ('C', 'GLN', 'CA', 'MET', 9.15), ('C', 'GLN', 'N', 'MET', 8.08)], [('CA', 'GLN', 'CB', 'MET', 8.35), ('CA', 'GLN', 'CG', 'MET', 9.62), ('CA', 'GLN', 'SD', 'MET', 10.14), ('CA', 'GLN', 'CE', 'MET', 9.27), ('CA', 'GLN', 'O', 'MET', 10.2), ('CA', 'GLN', 'C', 'MET', 9.89), ('CA', 'GLN', 'CA', 'MET', 8.5), ('CA', 'GLN', 'N', 'MET', 7.54)], [('N', 'GLN', 'CB', 'MET', 7.98), ('N', 'GLN', 'CG', 'MET', 9.36), ('N', 'GLN', 'SD', 'MET', 9.84), ('N', 'GLN', 'CE', 'MET', 9.21), ('N', 'GLN', 'O', 'MET', 9.44), ('N', 'GLN', 'C', 'MET', 9.34), ('N', 'GLN', 'CA', 'MET', 8.11), ('N', 'GLN', 'N', 'MET', 6.99)]]}
SER_HIS = { 
	'distances':
		[[9.31, 7.87, 7.63, 6.81, 6.4, 5.72], [9.2, 7.75, 7.49, 6.69, 6.24, 5.58]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 9.31), ('CB', 'SER', 'CG', 'HIS', 7.87), ('CB', 'SER', 'ND1', 'HIS', 7.63), ('CB', 'SER', 'CD2', 'HIS', 6.81), ('CB', 'SER', 'CE1', 'HIS', 6.4), ('CB', 'SER', 'NE2', 'HIS', 5.72)], [('OG', 'SER', 'CB', 'HIS', 9.2), ('OG', 'SER', 'CG', 'HIS', 7.75), ('OG', 'SER', 'ND1', 'HIS', 7.49), ('OG', 'SER', 'CD2', 'HIS', 6.69), ('OG', 'SER', 'CE1', 'HIS', 6.24), ('OG', 'SER', 'NE2', 'HIS', 5.58)]]}
GLN_SER = { 
	'distances':
		[[6.69, 6.19], [6.65, 6.38], [7.8, 7.33], [8.19, 7.46], [8.62, 8.34], [8.04, 8.07], [6.88, 6.99], [6.04, 5.79], [4.6, 4.54]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'SER', 6.69), ('CB', 'GLN', 'OG', 'SER', 6.19)], [('CG', 'GLN', 'CB', 'SER', 6.65), ('CG', 'GLN', 'OG', 'SER', 6.38)], [('CD', 'GLN', 'CB', 'SER', 7.8), ('CD', 'GLN', 'OG', 'SER', 7.33)], [('OE1', 'GLN', 'CB', 'SER', 8.19), ('OE1', 'GLN', 'OG', 'SER', 7.46)], [('NE2', 'GLN', 'CB', 'SER', 8.62), ('NE2', 'GLN', 'OG', 'SER', 8.34)], [('O', 'GLN', 'CB', 'SER', 8.04), ('O', 'GLN', 'OG', 'SER', 8.07)], [('C', 'GLN', 'CB', 'SER', 6.88), ('C', 'GLN', 'OG', 'SER', 6.99)], [('CA', 'GLN', 'CB', 'SER', 6.04), ('CA', 'GLN', 'OG', 'SER', 5.79)], [('N', 'GLN', 'CB', 'SER', 4.6), ('N', 'GLN', 'OG', 'SER', 4.54)]]}
SER_ASP = { 
	'distances':
		[[12.48, 11.03, 10.85, 10.21], [12.09, 10.63, 10.29, 9.95]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 12.48), ('CB', 'SER', 'CG', 'ASP', 11.03), ('CB', 'SER', 'OD1', 'ASP', 10.85), ('CB', 'SER', 'OD2', 'ASP', 10.21)], [('OG', 'SER', 'CB', 'ASP', 12.09), ('OG', 'SER', 'CG', 'ASP', 10.63), ('OG', 'SER', 'OD1', 'ASP', 10.29), ('OG', 'SER', 'OD2', 'ASP', 9.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_HIS, d, 'A_1eh5_3_1_2_22')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'A_1eh5_3_1_2_22')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_MET, d, 'A_1eh5_3_1_2_22')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLN_ASP, d, 'A_1eh5_3_1_2_22')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(MET_ASP, d, 'A_1eh5_3_1_2_22')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(MET_HIS, d, 'A_1eh5_3_1_2_22')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLN_MET, d, 'A_1eh5_3_1_2_22')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_HIS, d, 'A_1eh5_3_1_2_22')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLN_SER, d, 'A_1eh5_3_1_2_22')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_ASP, d, 'A_1eh5_3_1_2_22')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_HIS' :  match1,
		'ASP_HIS' :  match2,
		'SER_MET' :  match3,
		'GLN_ASP' :  match4,
		'MET_ASP' :  match5,
		'MET_HIS' :  match6,
		'GLN_MET' :  match7,
		'SER_HIS' :  match8,
		'GLN_SER' :  match9,
		'SER_ASP' :  match10}