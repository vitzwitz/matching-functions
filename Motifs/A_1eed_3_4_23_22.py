'''
FUNC:A_1eed_3_4_23_22
PDB:1eed
EC:3.4.23.22
RESI:asp,ser,asp,thr
LOCI:p-32,35,215,218;
'''
import motifFunctions as cmd
SER_ASPI = { 
	'distances':
		[[6.98, 6.17, 6.86, 5.3, 6.93, 7.6, 7.98, 8.98], [5.83, 5.42, 6.4, 4.63, 6.28, 6.91, 7.0, 7.82], [7.16, 7.14, 7.67, 7.02, 5.28, 6.44, 7.45, 7.98], [7.47, 7.22, 7.84, 6.81, 6.14, 7.21, 8.04, 8.7], [7.3, 6.6, 7.09, 6.02, 6.39, 7.23, 7.97, 8.94], [6.67, 5.88, 6.06, 5.64, 5.43, 6.11, 7.03, 8.15]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASPI', 6.98), ('CB', 'SER', 'CG', 'ASPI', 6.17), ('CB', 'SER', 'OD1', 'ASPI', 6.86), ('CB', 'SER', 'OD2', 'ASPI', 5.3), ('CB', 'SER', 'O', 'ASPI', 6.93), ('CB', 'SER', 'C', 'ASPI', 7.6), ('CB', 'SER', 'CA', 'ASPI', 7.98), ('CB', 'SER', 'N', 'ASPI', 8.98)], [('OG', 'SER', 'CB', 'ASPI', 5.83), ('OG', 'SER', 'CG', 'ASPI', 5.42), ('OG', 'SER', 'OD1', 'ASPI', 6.4), ('OG', 'SER', 'OD2', 'ASPI', 4.63), ('OG', 'SER', 'O', 'ASPI', 6.28), ('OG', 'SER', 'C', 'ASPI', 6.91), ('OG', 'SER', 'CA', 'ASPI', 7.0), ('OG', 'SER', 'N', 'ASPI', 7.82)], [('O', 'SER', 'CB', 'ASPI', 7.16), ('O', 'SER', 'CG', 'ASPI', 7.14), ('O', 'SER', 'OD1', 'ASPI', 7.67), ('O', 'SER', 'OD2', 'ASPI', 7.02), ('O', 'SER', 'O', 'ASPI', 5.28), ('O', 'SER', 'C', 'ASPI', 6.44), ('O', 'SER', 'CA', 'ASPI', 7.45), ('O', 'SER', 'N', 'ASPI', 7.98)], [('C', 'SER', 'CB', 'ASPI', 7.47), ('C', 'SER', 'CG', 'ASPI', 7.22), ('C', 'SER', 'OD1', 'ASPI', 7.84), ('C', 'SER', 'OD2', 'ASPI', 6.81), ('C', 'SER', 'O', 'ASPI', 6.14), ('C', 'SER', 'C', 'ASPI', 7.21), ('C', 'SER', 'CA', 'ASPI', 8.04), ('C', 'SER', 'N', 'ASPI', 8.7)], [('CA', 'SER', 'CB', 'ASPI', 7.3), ('CA', 'SER', 'CG', 'ASPI', 6.6), ('CA', 'SER', 'OD1', 'ASPI', 7.09), ('CA', 'SER', 'OD2', 'ASPI', 6.02), ('CA', 'SER', 'O', 'ASPI', 6.39), ('CA', 'SER', 'C', 'ASPI', 7.23), ('CA', 'SER', 'CA', 'ASPI', 7.97), ('CA', 'SER', 'N', 'ASPI', 8.94)], [('N', 'SER', 'CB', 'ASPI', 6.67), ('N', 'SER', 'CG', 'ASPI', 5.88), ('N', 'SER', 'OD1', 'ASPI', 6.06), ('N', 'SER', 'OD2', 'ASPI', 5.64), ('N', 'SER', 'O', 'ASPI', 5.43), ('N', 'SER', 'C', 'ASPI', 6.11), ('N', 'SER', 'CA', 'ASPI', 7.03), ('N', 'SER', 'N', 'ASPI', 8.15)]]}
ASP_ASP = { 
	'distances':
		[[9.7, 8.66, 7.46, 9.2, 9.41, 8.72, 9.14, 10.48], [8.51, 7.34, 6.16, 7.81, 8.57, 7.89, 8.16, 9.6], [7.36, 6.31, 5.1, 6.94, 7.52, 6.76, 6.95, 8.38], [8.78, 7.43, 6.36, 7.67, 9.13, 8.54, 8.7, 10.21], [9.66, 9.04, 7.85, 9.87, 9.88, 8.86, 8.84, 9.9], [9.09, 8.53, 7.35, 9.41, 8.91, 7.94, 8.15, 9.21], [9.52, 8.77, 7.58, 9.51, 8.93, 8.16, 8.67, 9.84], [10.84, 10.13, 8.96, 10.87, 9.98, 9.27, 9.9, 10.97], [9.7, 8.51, 7.36, 8.78, 9.66, 9.09, 9.52, 10.84], [8.66, 7.34, 6.31, 7.43, 9.04, 8.53, 8.77, 10.13], [7.46, 6.16, 5.1, 6.36, 7.85, 7.35, 7.58, 8.96], [9.2, 7.81, 6.94, 7.67, 9.87, 9.41, 9.51, 10.87], [9.41, 8.57, 7.52, 9.13, 9.88, 8.91, 8.93, 9.98], [8.72, 7.89, 6.76, 8.54, 8.86, 7.94, 8.16, 9.27], [9.14, 8.16, 6.95, 8.7, 8.84, 8.15, 8.67, 9.9], [10.48, 9.6, 8.38, 10.21, 9.9, 9.21, 9.84, 10.97]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 9.7), ('CB', 'ASP', 'CG', 'ASP', 8.66), ('CB', 'ASP', 'OD1', 'ASP', 7.46), ('CB', 'ASP', 'OD2', 'ASP', 9.2), ('CB', 'ASP', 'O', 'ASP', 9.41), ('CB', 'ASP', 'C', 'ASP', 8.72), ('CB', 'ASP', 'CA', 'ASP', 9.14), ('CB', 'ASP', 'N', 'ASP', 10.48)], [('CG', 'ASP', 'CB', 'ASP', 8.51), ('CG', 'ASP', 'CG', 'ASP', 7.34), ('CG', 'ASP', 'OD1', 'ASP', 6.16), ('CG', 'ASP', 'OD2', 'ASP', 7.81), ('CG', 'ASP', 'O', 'ASP', 8.57), ('CG', 'ASP', 'C', 'ASP', 7.89), ('CG', 'ASP', 'CA', 'ASP', 8.16), ('CG', 'ASP', 'N', 'ASP', 9.6)], [('OD1', 'ASP', 'CB', 'ASP', 7.36), ('OD1', 'ASP', 'CG', 'ASP', 6.31), ('OD1', 'ASP', 'OD1', 'ASP', 5.1), ('OD1', 'ASP', 'OD2', 'ASP', 6.94), ('OD1', 'ASP', 'O', 'ASP', 7.52), ('OD1', 'ASP', 'C', 'ASP', 6.76), ('OD1', 'ASP', 'CA', 'ASP', 6.95), ('OD1', 'ASP', 'N', 'ASP', 8.38)], [('OD2', 'ASP', 'CB', 'ASP', 8.78), ('OD2', 'ASP', 'CG', 'ASP', 7.43), ('OD2', 'ASP', 'OD1', 'ASP', 6.36), ('OD2', 'ASP', 'OD2', 'ASP', 7.67), ('OD2', 'ASP', 'O', 'ASP', 9.13), ('OD2', 'ASP', 'C', 'ASP', 8.54), ('OD2', 'ASP', 'CA', 'ASP', 8.7), ('OD2', 'ASP', 'N', 'ASP', 10.21)], [('O', 'ASP', 'CB', 'ASP', 9.66), ('O', 'ASP', 'CG', 'ASP', 9.04), ('O', 'ASP', 'OD1', 'ASP', 7.85), ('O', 'ASP', 'OD2', 'ASP', 9.87), ('O', 'ASP', 'O', 'ASP', 9.88), ('O', 'ASP', 'C', 'ASP', 8.86), ('O', 'ASP', 'CA', 'ASP', 8.84), ('O', 'ASP', 'N', 'ASP', 9.9)], [('C', 'ASP', 'CB', 'ASP', 9.09), ('C', 'ASP', 'CG', 'ASP', 8.53), ('C', 'ASP', 'OD1', 'ASP', 7.35), ('C', 'ASP', 'OD2', 'ASP', 9.41), ('C', 'ASP', 'O', 'ASP', 8.91), ('C', 'ASP', 'C', 'ASP', 7.94), ('C', 'ASP', 'CA', 'ASP', 8.15), ('C', 'ASP', 'N', 'ASP', 9.21)], [('CA', 'ASP', 'CB', 'ASP', 9.52), ('CA', 'ASP', 'CG', 'ASP', 8.77), ('CA', 'ASP', 'OD1', 'ASP', 7.58), ('CA', 'ASP', 'OD2', 'ASP', 9.51), ('CA', 'ASP', 'O', 'ASP', 8.93), ('CA', 'ASP', 'C', 'ASP', 8.16), ('CA', 'ASP', 'CA', 'ASP', 8.67), ('CA', 'ASP', 'N', 'ASP', 9.84)], [('N', 'ASP', 'CB', 'ASP', 10.84), ('N', 'ASP', 'CG', 'ASP', 10.13), ('N', 'ASP', 'OD1', 'ASP', 8.96), ('N', 'ASP', 'OD2', 'ASP', 10.87), ('N', 'ASP', 'O', 'ASP', 9.98), ('N', 'ASP', 'C', 'ASP', 9.27), ('N', 'ASP', 'CA', 'ASP', 9.9), ('N', 'ASP', 'N', 'ASP', 10.97)], [('CB', 'ASP', 'CB', 'ASP', 9.7), ('CB', 'ASP', 'CG', 'ASP', 8.51), ('CB', 'ASP', 'OD1', 'ASP', 7.36), ('CB', 'ASP', 'OD2', 'ASP', 8.78), ('CB', 'ASP', 'O', 'ASP', 9.66), ('CB', 'ASP', 'C', 'ASP', 9.09), ('CB', 'ASP', 'CA', 'ASP', 9.52), ('CB', 'ASP', 'N', 'ASP', 10.84)], [('CG', 'ASP', 'CB', 'ASP', 8.66), ('CG', 'ASP', 'CG', 'ASP', 7.34), ('CG', 'ASP', 'OD1', 'ASP', 6.31), ('CG', 'ASP', 'OD2', 'ASP', 7.43), ('CG', 'ASP', 'O', 'ASP', 9.04), ('CG', 'ASP', 'C', 'ASP', 8.53), ('CG', 'ASP', 'CA', 'ASP', 8.77), ('CG', 'ASP', 'N', 'ASP', 10.13)], [('OD1', 'ASP', 'CB', 'ASP', 7.46), ('OD1', 'ASP', 'CG', 'ASP', 6.16), ('OD1', 'ASP', 'OD1', 'ASP', 5.1), ('OD1', 'ASP', 'OD2', 'ASP', 6.36), ('OD1', 'ASP', 'O', 'ASP', 7.85), ('OD1', 'ASP', 'C', 'ASP', 7.35), ('OD1', 'ASP', 'CA', 'ASP', 7.58), ('OD1', 'ASP', 'N', 'ASP', 8.96)], [('OD2', 'ASP', 'CB', 'ASP', 9.2), ('OD2', 'ASP', 'CG', 'ASP', 7.81), ('OD2', 'ASP', 'OD1', 'ASP', 6.94), ('OD2', 'ASP', 'OD2', 'ASP', 7.67), ('OD2', 'ASP', 'O', 'ASP', 9.87), ('OD2', 'ASP', 'C', 'ASP', 9.41), ('OD2', 'ASP', 'CA', 'ASP', 9.51), ('OD2', 'ASP', 'N', 'ASP', 10.87)], [('O', 'ASP', 'CB', 'ASP', 9.41), ('O', 'ASP', 'CG', 'ASP', 8.57), ('O', 'ASP', 'OD1', 'ASP', 7.52), ('O', 'ASP', 'OD2', 'ASP', 9.13), ('O', 'ASP', 'O', 'ASP', 9.88), ('O', 'ASP', 'C', 'ASP', 8.91), ('O', 'ASP', 'CA', 'ASP', 8.93), ('O', 'ASP', 'N', 'ASP', 9.98)], [('C', 'ASP', 'CB', 'ASP', 8.72), ('C', 'ASP', 'CG', 'ASP', 7.89), ('C', 'ASP', 'OD1', 'ASP', 6.76), ('C', 'ASP', 'OD2', 'ASP', 8.54), ('C', 'ASP', 'O', 'ASP', 8.86), ('C', 'ASP', 'C', 'ASP', 7.94), ('C', 'ASP', 'CA', 'ASP', 8.16), ('C', 'ASP', 'N', 'ASP', 9.27)], [('CA', 'ASP', 'CB', 'ASP', 9.14), ('CA', 'ASP', 'CG', 'ASP', 8.16), ('CA', 'ASP', 'OD1', 'ASP', 6.95), ('CA', 'ASP', 'OD2', 'ASP', 8.7), ('CA', 'ASP', 'O', 'ASP', 8.84), ('CA', 'ASP', 'C', 'ASP', 8.15), ('CA', 'ASP', 'CA', 'ASP', 8.67), ('CA', 'ASP', 'N', 'ASP', 9.9)], [('N', 'ASP', 'CB', 'ASP', 10.48), ('N', 'ASP', 'CG', 'ASP', 9.6), ('N', 'ASP', 'OD1', 'ASP', 8.38), ('N', 'ASP', 'OD2', 'ASP', 10.21), ('N', 'ASP', 'O', 'ASP', 9.9), ('N', 'ASP', 'C', 'ASP', 9.21), ('N', 'ASP', 'CA', 'ASP', 9.84), ('N', 'ASP', 'N', 'ASP', 10.97)]]}
ASP_SER = { 
	'distances':
		[[10.8, 11.12, 11.22, 11.5, 10.49, 9.08], [9.57, 9.84, 10.34, 10.51, 9.43, 8.1], [8.98, 9.05, 9.57, 9.82, 8.87, 7.5], [9.33, 9.71, 10.58, 10.59, 9.35, 8.19], [12.23, 12.14, 12.44, 12.88, 12.07, 10.64], [11.56, 11.49, 11.45, 11.97, 11.25, 9.77], [11.2, 11.36, 11.06, 11.54, 10.75, 9.24], [12.36, 12.6, 12.01, 12.54, 11.8, 10.28], [6.98, 5.83, 7.16, 7.47, 7.3, 6.67], [6.17, 5.42, 7.14, 7.22, 6.6, 5.88], [6.86, 6.4, 7.67, 7.84, 7.09, 6.06], [5.3, 4.63, 7.02, 6.81, 6.02, 5.64], [6.93, 6.28, 5.28, 6.14, 6.39, 5.43], [7.6, 6.91, 6.44, 7.21, 7.23, 6.11], [7.98, 7.0, 7.45, 8.04, 7.97, 7.03], [8.98, 7.82, 7.98, 8.7, 8.94, 8.15]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 10.8), ('CB', 'ASP', 'OG', 'SER', 11.12), ('CB', 'ASP', 'O', 'SER', 11.22), ('CB', 'ASP', 'C', 'SER', 11.5), ('CB', 'ASP', 'CA', 'SER', 10.49), ('CB', 'ASP', 'N', 'SER', 9.08)], [('CG', 'ASP', 'CB', 'SER', 9.57), ('CG', 'ASP', 'OG', 'SER', 9.84), ('CG', 'ASP', 'O', 'SER', 10.34), ('CG', 'ASP', 'C', 'SER', 10.51), ('CG', 'ASP', 'CA', 'SER', 9.43), ('CG', 'ASP', 'N', 'SER', 8.1)], [('OD1', 'ASP', 'CB', 'SER', 8.98), ('OD1', 'ASP', 'OG', 'SER', 9.05), ('OD1', 'ASP', 'O', 'SER', 9.57), ('OD1', 'ASP', 'C', 'SER', 9.82), ('OD1', 'ASP', 'CA', 'SER', 8.87), ('OD1', 'ASP', 'N', 'SER', 7.5)], [('OD2', 'ASP', 'CB', 'SER', 9.33), ('OD2', 'ASP', 'OG', 'SER', 9.71), ('OD2', 'ASP', 'O', 'SER', 10.58), ('OD2', 'ASP', 'C', 'SER', 10.59), ('OD2', 'ASP', 'CA', 'SER', 9.35), ('OD2', 'ASP', 'N', 'SER', 8.19)], [('O', 'ASP', 'CB', 'SER', 12.23), ('O', 'ASP', 'OG', 'SER', 12.14), ('O', 'ASP', 'O', 'SER', 12.44), ('O', 'ASP', 'C', 'SER', 12.88), ('O', 'ASP', 'CA', 'SER', 12.07), ('O', 'ASP', 'N', 'SER', 10.64)], [('C', 'ASP', 'CB', 'SER', 11.56), ('C', 'ASP', 'OG', 'SER', 11.49), ('C', 'ASP', 'O', 'SER', 11.45), ('C', 'ASP', 'C', 'SER', 11.97), ('C', 'ASP', 'CA', 'SER', 11.25), ('C', 'ASP', 'N', 'SER', 9.77)], [('CA', 'ASP', 'CB', 'SER', 11.2), ('CA', 'ASP', 'OG', 'SER', 11.36), ('CA', 'ASP', 'O', 'SER', 11.06), ('CA', 'ASP', 'C', 'SER', 11.54), ('CA', 'ASP', 'CA', 'SER', 10.75), ('CA', 'ASP', 'N', 'SER', 9.24)], [('N', 'ASP', 'CB', 'SER', 12.36), ('N', 'ASP', 'OG', 'SER', 12.6), ('N', 'ASP', 'O', 'SER', 12.01), ('N', 'ASP', 'C', 'SER', 12.54), ('N', 'ASP', 'CA', 'SER', 11.8), ('N', 'ASP', 'N', 'SER', 10.28)], [('CB', 'ASP', 'CB', 'SER', 6.98), ('CB', 'ASP', 'OG', 'SER', 5.83), ('CB', 'ASP', 'O', 'SER', 7.16), ('CB', 'ASP', 'C', 'SER', 7.47), ('CB', 'ASP', 'CA', 'SER', 7.3), ('CB', 'ASP', 'N', 'SER', 6.67)], [('CG', 'ASP', 'CB', 'SER', 6.17), ('CG', 'ASP', 'OG', 'SER', 5.42), ('CG', 'ASP', 'O', 'SER', 7.14), ('CG', 'ASP', 'C', 'SER', 7.22), ('CG', 'ASP', 'CA', 'SER', 6.6), ('CG', 'ASP', 'N', 'SER', 5.88)], [('OD1', 'ASP', 'CB', 'SER', 6.86), ('OD1', 'ASP', 'OG', 'SER', 6.4), ('OD1', 'ASP', 'O', 'SER', 7.67), ('OD1', 'ASP', 'C', 'SER', 7.84), ('OD1', 'ASP', 'CA', 'SER', 7.09), ('OD1', 'ASP', 'N', 'SER', 6.06)], [('OD2', 'ASP', 'CB', 'SER', 5.3), ('OD2', 'ASP', 'OG', 'SER', 4.63), ('OD2', 'ASP', 'O', 'SER', 7.02), ('OD2', 'ASP', 'C', 'SER', 6.81), ('OD2', 'ASP', 'CA', 'SER', 6.02), ('OD2', 'ASP', 'N', 'SER', 5.64)], [('O', 'ASP', 'CB', 'SER', 6.93), ('O', 'ASP', 'OG', 'SER', 6.28), ('O', 'ASP', 'O', 'SER', 5.28), ('O', 'ASP', 'C', 'SER', 6.14), ('O', 'ASP', 'CA', 'SER', 6.39), ('O', 'ASP', 'N', 'SER', 5.43)], [('C', 'ASP', 'CB', 'SER', 7.6), ('C', 'ASP', 'OG', 'SER', 6.91), ('C', 'ASP', 'O', 'SER', 6.44), ('C', 'ASP', 'C', 'SER', 7.21), ('C', 'ASP', 'CA', 'SER', 7.23), ('C', 'ASP', 'N', 'SER', 6.11)], [('CA', 'ASP', 'CB', 'SER', 7.98), ('CA', 'ASP', 'OG', 'SER', 7.0), ('CA', 'ASP', 'O', 'SER', 7.45), ('CA', 'ASP', 'C', 'SER', 8.04), ('CA', 'ASP', 'CA', 'SER', 7.97), ('CA', 'ASP', 'N', 'SER', 7.03)], [('N', 'ASP', 'CB', 'SER', 8.98), ('N', 'ASP', 'OG', 'SER', 7.82), ('N', 'ASP', 'O', 'SER', 7.98), ('N', 'ASP', 'C', 'SER', 8.7), ('N', 'ASP', 'CA', 'SER', 8.94), ('N', 'ASP', 'N', 'SER', 8.15)]]}
THR_SER = { 
	'distances':
		[[12.36, 12.48, 13.76, 13.8, 12.61, 11.49], [11.23, 11.46, 12.91, 12.83, 11.55, 10.54], [13.57, 13.76, 15.15, 15.13, 13.88, 12.82], [14.1, 13.88, 15.0, 15.27, 14.32, 13.08], [13.74, 13.54, 14.94, 15.1, 14.07, 12.93], [12.39, 12.28, 13.79, 13.86, 12.77, 11.68], [11.41, 11.18, 12.51, 12.68, 11.7, 10.55]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'SER', 12.36), ('CB', 'THR', 'OG', 'SER', 12.48), ('CB', 'THR', 'O', 'SER', 13.76), ('CB', 'THR', 'C', 'SER', 13.8), ('CB', 'THR', 'CA', 'SER', 12.61), ('CB', 'THR', 'N', 'SER', 11.49)], [('OG1', 'THR', 'CB', 'SER', 11.23), ('OG1', 'THR', 'OG', 'SER', 11.46), ('OG1', 'THR', 'O', 'SER', 12.91), ('OG1', 'THR', 'C', 'SER', 12.83), ('OG1', 'THR', 'CA', 'SER', 11.55), ('OG1', 'THR', 'N', 'SER', 10.54)], [('CG2', 'THR', 'CB', 'SER', 13.57), ('CG2', 'THR', 'OG', 'SER', 13.76), ('CG2', 'THR', 'O', 'SER', 15.15), ('CG2', 'THR', 'C', 'SER', 15.13), ('CG2', 'THR', 'CA', 'SER', 13.88), ('CG2', 'THR', 'N', 'SER', 12.82)], [('O', 'THR', 'CB', 'SER', 14.1), ('O', 'THR', 'OG', 'SER', 13.88), ('O', 'THR', 'O', 'SER', 15.0), ('O', 'THR', 'C', 'SER', 15.27), ('O', 'THR', 'CA', 'SER', 14.32), ('O', 'THR', 'N', 'SER', 13.08)], [('C', 'THR', 'CB', 'SER', 13.74), ('C', 'THR', 'OG', 'SER', 13.54), ('C', 'THR', 'O', 'SER', 14.94), ('C', 'THR', 'C', 'SER', 15.1), ('C', 'THR', 'CA', 'SER', 14.07), ('C', 'THR', 'N', 'SER', 12.93)], [('CA', 'THR', 'CB', 'SER', 12.39), ('CA', 'THR', 'OG', 'SER', 12.28), ('CA', 'THR', 'O', 'SER', 13.79), ('CA', 'THR', 'C', 'SER', 13.86), ('CA', 'THR', 'CA', 'SER', 12.77), ('CA', 'THR', 'N', 'SER', 11.68)], [('N', 'THR', 'CB', 'SER', 11.41), ('N', 'THR', 'OG', 'SER', 11.18), ('N', 'THR', 'O', 'SER', 12.51), ('N', 'THR', 'C', 'SER', 12.68), ('N', 'THR', 'CA', 'SER', 11.7), ('N', 'THR', 'N', 'SER', 10.55)]]}
THR_ASP = { 
	'distances':
		[[6.13, 5.85, 6.45, 5.53, 5.92, 6.84, 7.16, 7.97], [6.07, 5.41, 6.06, 4.66, 6.64, 7.28, 7.34, 8.29], [7.32, 7.21, 7.92, 6.75, 7.17, 8.17, 8.41, 9.03], [7.59, 7.58, 7.72, 7.83, 5.55, 6.79, 7.82, 8.46], [7.8, 7.57, 7.73, 7.57, 6.2, 7.37, 8.28, 9.06], [7.01, 6.5, 6.69, 6.3, 6.05, 7.04, 7.74, 8.7], [6.36, 5.68, 5.53, 5.79, 5.16, 5.94, 6.82, 7.95], [10.77, 9.67, 8.62, 10.04, 11.79, 10.92, 10.61, 11.93], [10.23, 8.94, 7.97, 9.14, 11.26, 10.51, 10.27, 11.69], [12.2, 11.06, 10.06, 11.35, 13.28, 12.43, 12.11, 13.41], [11.26, 10.62, 9.6, 11.31, 12.42, 11.33, 10.79, 11.76], [11.13, 10.38, 9.42, 10.95, 12.51, 11.46, 10.85, 11.9], [10.18, 9.25, 8.3, 9.71, 11.57, 10.61, 10.05, 11.24], [8.8, 7.99, 6.99, 8.6, 10.12, 9.12, 8.55, 9.73]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 6.13), ('CB', 'THR', 'CG', 'ASP', 5.85), ('CB', 'THR', 'OD1', 'ASP', 6.45), ('CB', 'THR', 'OD2', 'ASP', 5.53), ('CB', 'THR', 'O', 'ASP', 5.92), ('CB', 'THR', 'C', 'ASP', 6.84), ('CB', 'THR', 'CA', 'ASP', 7.16), ('CB', 'THR', 'N', 'ASP', 7.97)], [('OG1', 'THR', 'CB', 'ASP', 6.07), ('OG1', 'THR', 'CG', 'ASP', 5.41), ('OG1', 'THR', 'OD1', 'ASP', 6.06), ('OG1', 'THR', 'OD2', 'ASP', 4.66), ('OG1', 'THR', 'O', 'ASP', 6.64), ('OG1', 'THR', 'C', 'ASP', 7.28), ('OG1', 'THR', 'CA', 'ASP', 7.34), ('OG1', 'THR', 'N', 'ASP', 8.29)], [('CG2', 'THR', 'CB', 'ASP', 7.32), ('CG2', 'THR', 'CG', 'ASP', 7.21), ('CG2', 'THR', 'OD1', 'ASP', 7.92), ('CG2', 'THR', 'OD2', 'ASP', 6.75), ('CG2', 'THR', 'O', 'ASP', 7.17), ('CG2', 'THR', 'C', 'ASP', 8.17), ('CG2', 'THR', 'CA', 'ASP', 8.41), ('CG2', 'THR', 'N', 'ASP', 9.03)], [('O', 'THR', 'CB', 'ASP', 7.59), ('O', 'THR', 'CG', 'ASP', 7.58), ('O', 'THR', 'OD1', 'ASP', 7.72), ('O', 'THR', 'OD2', 'ASP', 7.83), ('O', 'THR', 'O', 'ASP', 5.55), ('O', 'THR', 'C', 'ASP', 6.79), ('O', 'THR', 'CA', 'ASP', 7.82), ('O', 'THR', 'N', 'ASP', 8.46)], [('C', 'THR', 'CB', 'ASP', 7.8), ('C', 'THR', 'CG', 'ASP', 7.57), ('C', 'THR', 'OD1', 'ASP', 7.73), ('C', 'THR', 'OD2', 'ASP', 7.57), ('C', 'THR', 'O', 'ASP', 6.2), ('C', 'THR', 'C', 'ASP', 7.37), ('C', 'THR', 'CA', 'ASP', 8.28), ('C', 'THR', 'N', 'ASP', 9.06)], [('CA', 'THR', 'CB', 'ASP', 7.01), ('CA', 'THR', 'CG', 'ASP', 6.5), ('CA', 'THR', 'OD1', 'ASP', 6.69), ('CA', 'THR', 'OD2', 'ASP', 6.3), ('CA', 'THR', 'O', 'ASP', 6.05), ('CA', 'THR', 'C', 'ASP', 7.04), ('CA', 'THR', 'CA', 'ASP', 7.74), ('CA', 'THR', 'N', 'ASP', 8.7)], [('N', 'THR', 'CB', 'ASP', 6.36), ('N', 'THR', 'CG', 'ASP', 5.68), ('N', 'THR', 'OD1', 'ASP', 5.53), ('N', 'THR', 'OD2', 'ASP', 5.79), ('N', 'THR', 'O', 'ASP', 5.16), ('N', 'THR', 'C', 'ASP', 5.94), ('N', 'THR', 'CA', 'ASP', 6.82), ('N', 'THR', 'N', 'ASP', 7.95)], [('CB', 'THR', 'CB', 'ASP', 10.77), ('CB', 'THR', 'CG', 'ASP', 9.67), ('CB', 'THR', 'OD1', 'ASP', 8.62), ('CB', 'THR', 'OD2', 'ASP', 10.04), ('CB', 'THR', 'O', 'ASP', 11.79), ('CB', 'THR', 'C', 'ASP', 10.92), ('CB', 'THR', 'CA', 'ASP', 10.61), ('CB', 'THR', 'N', 'ASP', 11.93)], [('OG1', 'THR', 'CB', 'ASP', 10.23), ('OG1', 'THR', 'CG', 'ASP', 8.94), ('OG1', 'THR', 'OD1', 'ASP', 7.97), ('OG1', 'THR', 'OD2', 'ASP', 9.14), ('OG1', 'THR', 'O', 'ASP', 11.26), ('OG1', 'THR', 'C', 'ASP', 10.51), ('OG1', 'THR', 'CA', 'ASP', 10.27), ('OG1', 'THR', 'N', 'ASP', 11.69)], [('CG2', 'THR', 'CB', 'ASP', 12.2), ('CG2', 'THR', 'CG', 'ASP', 11.06), ('CG2', 'THR', 'OD1', 'ASP', 10.06), ('CG2', 'THR', 'OD2', 'ASP', 11.35), ('CG2', 'THR', 'O', 'ASP', 13.28), ('CG2', 'THR', 'C', 'ASP', 12.43), ('CG2', 'THR', 'CA', 'ASP', 12.11), ('CG2', 'THR', 'N', 'ASP', 13.41)], [('O', 'THR', 'CB', 'ASP', 11.26), ('O', 'THR', 'CG', 'ASP', 10.62), ('O', 'THR', 'OD1', 'ASP', 9.6), ('O', 'THR', 'OD2', 'ASP', 11.31), ('O', 'THR', 'O', 'ASP', 12.42), ('O', 'THR', 'C', 'ASP', 11.33), ('O', 'THR', 'CA', 'ASP', 10.79), ('O', 'THR', 'N', 'ASP', 11.76)], [('C', 'THR', 'CB', 'ASP', 11.13), ('C', 'THR', 'CG', 'ASP', 10.38), ('C', 'THR', 'OD1', 'ASP', 9.42), ('C', 'THR', 'OD2', 'ASP', 10.95), ('C', 'THR', 'O', 'ASP', 12.51), ('C', 'THR', 'C', 'ASP', 11.46), ('C', 'THR', 'CA', 'ASP', 10.85), ('C', 'THR', 'N', 'ASP', 11.9)], [('CA', 'THR', 'CB', 'ASP', 10.18), ('CA', 'THR', 'CG', 'ASP', 9.25), ('CA', 'THR', 'OD1', 'ASP', 8.3), ('CA', 'THR', 'OD2', 'ASP', 9.71), ('CA', 'THR', 'O', 'ASP', 11.57), ('CA', 'THR', 'C', 'ASP', 10.61), ('CA', 'THR', 'CA', 'ASP', 10.05), ('CA', 'THR', 'N', 'ASP', 11.24)], [('N', 'THR', 'CB', 'ASP', 8.8), ('N', 'THR', 'CG', 'ASP', 7.99), ('N', 'THR', 'OD1', 'ASP', 6.99), ('N', 'THR', 'OD2', 'ASP', 8.6), ('N', 'THR', 'O', 'ASP', 10.12), ('N', 'THR', 'C', 'ASP', 9.12), ('N', 'THR', 'CA', 'ASP', 8.55), ('N', 'THR', 'N', 'ASP', 9.73)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_ASPI, d, 'A_1eed_3_4_23_22')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'A_1eed_3_4_23_22')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_SER, d, 'A_1eed_3_4_23_22')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_SER, d, 'A_1eed_3_4_23_22')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(THR_ASP, d, 'A_1eed_3_4_23_22')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_ASPI' :  match1,
		'ASP_ASP' :  match2,
		'ASP_SER' :  match3,
		'THR_SER' :  match4,
		'THR_ASP' :  match5}