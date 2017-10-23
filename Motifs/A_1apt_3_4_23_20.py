'''
FUNC:A_1apt_3_4_23_20
PDB:1apt
EC:3.4.23.20
RESI:asp,ser,asp,thr
LOCI:e-33,36,213,216;
'''
import motifFunctions as cmd
SER_ASPI = { 
	'distances':
		[[7.11, 6.3, 5.28, 7.02, 6.84, 7.71, 8.1, 8.96], [5.99, 5.51, 4.54, 6.49, 6.15, 6.97, 7.11, 7.8], [7.21, 7.06, 6.78, 7.63, 5.21, 6.44, 7.4, 7.97], [7.69, 7.29, 6.73, 7.91, 6.14, 7.31, 8.15, 8.82], [7.38, 6.61, 5.9, 7.1, 6.29, 7.26, 8.01, 8.94], [6.67, 5.78, 5.4, 5.99, 5.37, 6.15, 7.05, 8.15]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASPI', 7.11), ('CB', 'SER', 'CG', 'ASPI', 6.3), ('CB', 'SER', 'OD1', 'ASPI', 5.28), ('CB', 'SER', 'OD2', 'ASPI', 7.02), ('CB', 'SER', 'O', 'ASPI', 6.84), ('CB', 'SER', 'C', 'ASPI', 7.71), ('CB', 'SER', 'CA', 'ASPI', 8.1), ('CB', 'SER', 'N', 'ASPI', 8.96)], [('OG', 'SER', 'CB', 'ASPI', 5.99), ('OG', 'SER', 'CG', 'ASPI', 5.51), ('OG', 'SER', 'OD1', 'ASPI', 4.54), ('OG', 'SER', 'OD2', 'ASPI', 6.49), ('OG', 'SER', 'O', 'ASPI', 6.15), ('OG', 'SER', 'C', 'ASPI', 6.97), ('OG', 'SER', 'CA', 'ASPI', 7.11), ('OG', 'SER', 'N', 'ASPI', 7.8)], [('O', 'SER', 'CB', 'ASPI', 7.21), ('O', 'SER', 'CG', 'ASPI', 7.06), ('O', 'SER', 'OD1', 'ASPI', 6.78), ('O', 'SER', 'OD2', 'ASPI', 7.63), ('O', 'SER', 'O', 'ASPI', 5.21), ('O', 'SER', 'C', 'ASPI', 6.44), ('O', 'SER', 'CA', 'ASPI', 7.4), ('O', 'SER', 'N', 'ASPI', 7.97)], [('C', 'SER', 'CB', 'ASPI', 7.69), ('C', 'SER', 'CG', 'ASPI', 7.29), ('C', 'SER', 'OD1', 'ASPI', 6.73), ('C', 'SER', 'OD2', 'ASPI', 7.91), ('C', 'SER', 'O', 'ASPI', 6.14), ('C', 'SER', 'C', 'ASPI', 7.31), ('C', 'SER', 'CA', 'ASPI', 8.15), ('C', 'SER', 'N', 'ASPI', 8.82)], [('CA', 'SER', 'CB', 'ASPI', 7.38), ('CA', 'SER', 'CG', 'ASPI', 6.61), ('CA', 'SER', 'OD1', 'ASPI', 5.9), ('CA', 'SER', 'OD2', 'ASPI', 7.1), ('CA', 'SER', 'O', 'ASPI', 6.29), ('CA', 'SER', 'C', 'ASPI', 7.26), ('CA', 'SER', 'CA', 'ASPI', 8.01), ('CA', 'SER', 'N', 'ASPI', 8.94)], [('N', 'SER', 'CB', 'ASPI', 6.67), ('N', 'SER', 'CG', 'ASPI', 5.78), ('N', 'SER', 'OD1', 'ASPI', 5.4), ('N', 'SER', 'OD2', 'ASPI', 5.99), ('N', 'SER', 'O', 'ASPI', 5.37), ('N', 'SER', 'C', 'ASPI', 6.15), ('N', 'SER', 'CA', 'ASPI', 7.05), ('N', 'SER', 'N', 'ASPI', 8.15)]]}
ASP_SER = { 
	'distances':
		[[10.88, 11.04, 11.09, 11.35, 10.37, 8.96], [9.59, 9.69, 10.13, 10.32, 9.25, 7.9], [9.01, 8.93, 9.31, 9.62, 8.68, 7.28], [9.36, 9.58, 10.42, 10.42, 9.2, 7.99], [12.43, 12.21, 12.46, 12.93, 12.1, 10.67], [11.78, 11.57, 11.51, 12.05, 11.32, 9.85], [11.34, 11.34, 11.02, 11.49, 10.72, 9.24], [12.57, 12.65, 12.05, 12.54, 11.82, 10.35], [7.11, 5.99, 7.21, 7.69, 7.38, 6.67], [6.3, 5.51, 7.06, 7.29, 6.61, 5.78], [5.28, 4.54, 6.78, 6.73, 5.9, 5.4], [7.02, 6.49, 7.63, 7.91, 7.1, 5.99], [6.84, 6.15, 5.21, 6.14, 6.29, 5.37], [7.71, 6.97, 6.44, 7.31, 7.26, 6.15], [8.1, 7.11, 7.4, 8.15, 8.01, 7.05], [8.96, 7.8, 7.97, 8.82, 8.94, 8.15]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 10.88), ('CB', 'ASP', 'OG', 'SER', 11.04), ('CB', 'ASP', 'O', 'SER', 11.09), ('CB', 'ASP', 'C', 'SER', 11.35), ('CB', 'ASP', 'CA', 'SER', 10.37), ('CB', 'ASP', 'N', 'SER', 8.96)], [('CG', 'ASP', 'CB', 'SER', 9.59), ('CG', 'ASP', 'OG', 'SER', 9.69), ('CG', 'ASP', 'O', 'SER', 10.13), ('CG', 'ASP', 'C', 'SER', 10.32), ('CG', 'ASP', 'CA', 'SER', 9.25), ('CG', 'ASP', 'N', 'SER', 7.9)], [('OD1', 'ASP', 'CB', 'SER', 9.01), ('OD1', 'ASP', 'OG', 'SER', 8.93), ('OD1', 'ASP', 'O', 'SER', 9.31), ('OD1', 'ASP', 'C', 'SER', 9.62), ('OD1', 'ASP', 'CA', 'SER', 8.68), ('OD1', 'ASP', 'N', 'SER', 7.28)], [('OD2', 'ASP', 'CB', 'SER', 9.36), ('OD2', 'ASP', 'OG', 'SER', 9.58), ('OD2', 'ASP', 'O', 'SER', 10.42), ('OD2', 'ASP', 'C', 'SER', 10.42), ('OD2', 'ASP', 'CA', 'SER', 9.2), ('OD2', 'ASP', 'N', 'SER', 7.99)], [('O', 'ASP', 'CB', 'SER', 12.43), ('O', 'ASP', 'OG', 'SER', 12.21), ('O', 'ASP', 'O', 'SER', 12.46), ('O', 'ASP', 'C', 'SER', 12.93), ('O', 'ASP', 'CA', 'SER', 12.1), ('O', 'ASP', 'N', 'SER', 10.67)], [('C', 'ASP', 'CB', 'SER', 11.78), ('C', 'ASP', 'OG', 'SER', 11.57), ('C', 'ASP', 'O', 'SER', 11.51), ('C', 'ASP', 'C', 'SER', 12.05), ('C', 'ASP', 'CA', 'SER', 11.32), ('C', 'ASP', 'N', 'SER', 9.85)], [('CA', 'ASP', 'CB', 'SER', 11.34), ('CA', 'ASP', 'OG', 'SER', 11.34), ('CA', 'ASP', 'O', 'SER', 11.02), ('CA', 'ASP', 'C', 'SER', 11.49), ('CA', 'ASP', 'CA', 'SER', 10.72), ('CA', 'ASP', 'N', 'SER', 9.24)], [('N', 'ASP', 'CB', 'SER', 12.57), ('N', 'ASP', 'OG', 'SER', 12.65), ('N', 'ASP', 'O', 'SER', 12.05), ('N', 'ASP', 'C', 'SER', 12.54), ('N', 'ASP', 'CA', 'SER', 11.82), ('N', 'ASP', 'N', 'SER', 10.35)], [('CB', 'ASP', 'CB', 'SER', 7.11), ('CB', 'ASP', 'OG', 'SER', 5.99), ('CB', 'ASP', 'O', 'SER', 7.21), ('CB', 'ASP', 'C', 'SER', 7.69), ('CB', 'ASP', 'CA', 'SER', 7.38), ('CB', 'ASP', 'N', 'SER', 6.67)], [('CG', 'ASP', 'CB', 'SER', 6.3), ('CG', 'ASP', 'OG', 'SER', 5.51), ('CG', 'ASP', 'O', 'SER', 7.06), ('CG', 'ASP', 'C', 'SER', 7.29), ('CG', 'ASP', 'CA', 'SER', 6.61), ('CG', 'ASP', 'N', 'SER', 5.78)], [('OD1', 'ASP', 'CB', 'SER', 5.28), ('OD1', 'ASP', 'OG', 'SER', 4.54), ('OD1', 'ASP', 'O', 'SER', 6.78), ('OD1', 'ASP', 'C', 'SER', 6.73), ('OD1', 'ASP', 'CA', 'SER', 5.9), ('OD1', 'ASP', 'N', 'SER', 5.4)], [('OD2', 'ASP', 'CB', 'SER', 7.02), ('OD2', 'ASP', 'OG', 'SER', 6.49), ('OD2', 'ASP', 'O', 'SER', 7.63), ('OD2', 'ASP', 'C', 'SER', 7.91), ('OD2', 'ASP', 'CA', 'SER', 7.1), ('OD2', 'ASP', 'N', 'SER', 5.99)], [('O', 'ASP', 'CB', 'SER', 6.84), ('O', 'ASP', 'OG', 'SER', 6.15), ('O', 'ASP', 'O', 'SER', 5.21), ('O', 'ASP', 'C', 'SER', 6.14), ('O', 'ASP', 'CA', 'SER', 6.29), ('O', 'ASP', 'N', 'SER', 5.37)], [('C', 'ASP', 'CB', 'SER', 7.71), ('C', 'ASP', 'OG', 'SER', 6.97), ('C', 'ASP', 'O', 'SER', 6.44), ('C', 'ASP', 'C', 'SER', 7.31), ('C', 'ASP', 'CA', 'SER', 7.26), ('C', 'ASP', 'N', 'SER', 6.15)], [('CA', 'ASP', 'CB', 'SER', 8.1), ('CA', 'ASP', 'OG', 'SER', 7.11), ('CA', 'ASP', 'O', 'SER', 7.4), ('CA', 'ASP', 'C', 'SER', 8.15), ('CA', 'ASP', 'CA', 'SER', 8.01), ('CA', 'ASP', 'N', 'SER', 7.05)], [('N', 'ASP', 'CB', 'SER', 8.96), ('N', 'ASP', 'OG', 'SER', 7.8), ('N', 'ASP', 'O', 'SER', 7.97), ('N', 'ASP', 'C', 'SER', 8.82), ('N', 'ASP', 'CA', 'SER', 8.94), ('N', 'ASP', 'N', 'SER', 8.15)]]}
ASP_ASP = { 
	'distances':
		[[9.51, 8.54, 9.17, 7.32, 9.27, 8.58, 9.07, 10.41], [8.25, 7.16, 7.72, 5.96, 8.34, 7.7, 8.05, 9.45], [7.11, 6.15, 6.89, 4.92, 7.23, 6.5, 6.81, 8.21], [8.56, 7.29, 7.63, 6.19, 8.93, 8.41, 8.65, 10.08], [9.56, 9.02, 9.96, 7.82, 9.91, 8.87, 8.89, 9.95], [9.0, 8.5, 9.48, 7.32, 8.97, 7.95, 8.18, 9.26], [9.35, 8.65, 9.48, 7.45, 8.88, 8.05, 8.59, 9.81], [10.78, 10.11, 10.92, 8.93, 10.06, 9.28, 9.93, 11.09], [9.51, 8.25, 7.11, 8.56, 9.56, 9.0, 9.35, 10.78], [8.54, 7.16, 6.15, 7.29, 9.02, 8.5, 8.65, 10.11], [9.17, 7.72, 6.89, 7.63, 9.96, 9.48, 9.48, 10.92], [7.32, 5.96, 4.92, 6.19, 7.82, 7.32, 7.45, 8.93], [9.27, 8.34, 7.23, 8.93, 9.91, 8.97, 8.88, 10.06], [8.58, 7.7, 6.5, 8.41, 8.87, 7.95, 8.05, 9.28], [9.07, 8.05, 6.81, 8.65, 8.89, 8.18, 8.59, 9.93], [10.41, 9.45, 8.21, 10.08, 9.95, 9.26, 9.81, 11.09]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 9.51), ('CB', 'ASP', 'CG', 'ASP', 8.54), ('CB', 'ASP', 'OD1', 'ASP', 9.17), ('CB', 'ASP', 'OD2', 'ASP', 7.32), ('CB', 'ASP', 'O', 'ASP', 9.27), ('CB', 'ASP', 'C', 'ASP', 8.58), ('CB', 'ASP', 'CA', 'ASP', 9.07), ('CB', 'ASP', 'N', 'ASP', 10.41)], [('CG', 'ASP', 'CB', 'ASP', 8.25), ('CG', 'ASP', 'CG', 'ASP', 7.16), ('CG', 'ASP', 'OD1', 'ASP', 7.72), ('CG', 'ASP', 'OD2', 'ASP', 5.96), ('CG', 'ASP', 'O', 'ASP', 8.34), ('CG', 'ASP', 'C', 'ASP', 7.7), ('CG', 'ASP', 'CA', 'ASP', 8.05), ('CG', 'ASP', 'N', 'ASP', 9.45)], [('OD1', 'ASP', 'CB', 'ASP', 7.11), ('OD1', 'ASP', 'CG', 'ASP', 6.15), ('OD1', 'ASP', 'OD1', 'ASP', 6.89), ('OD1', 'ASP', 'OD2', 'ASP', 4.92), ('OD1', 'ASP', 'O', 'ASP', 7.23), ('OD1', 'ASP', 'C', 'ASP', 6.5), ('OD1', 'ASP', 'CA', 'ASP', 6.81), ('OD1', 'ASP', 'N', 'ASP', 8.21)], [('OD2', 'ASP', 'CB', 'ASP', 8.56), ('OD2', 'ASP', 'CG', 'ASP', 7.29), ('OD2', 'ASP', 'OD1', 'ASP', 7.63), ('OD2', 'ASP', 'OD2', 'ASP', 6.19), ('OD2', 'ASP', 'O', 'ASP', 8.93), ('OD2', 'ASP', 'C', 'ASP', 8.41), ('OD2', 'ASP', 'CA', 'ASP', 8.65), ('OD2', 'ASP', 'N', 'ASP', 10.08)], [('O', 'ASP', 'CB', 'ASP', 9.56), ('O', 'ASP', 'CG', 'ASP', 9.02), ('O', 'ASP', 'OD1', 'ASP', 9.96), ('O', 'ASP', 'OD2', 'ASP', 7.82), ('O', 'ASP', 'O', 'ASP', 9.91), ('O', 'ASP', 'C', 'ASP', 8.87), ('O', 'ASP', 'CA', 'ASP', 8.89), ('O', 'ASP', 'N', 'ASP', 9.95)], [('C', 'ASP', 'CB', 'ASP', 9.0), ('C', 'ASP', 'CG', 'ASP', 8.5), ('C', 'ASP', 'OD1', 'ASP', 9.48), ('C', 'ASP', 'OD2', 'ASP', 7.32), ('C', 'ASP', 'O', 'ASP', 8.97), ('C', 'ASP', 'C', 'ASP', 7.95), ('C', 'ASP', 'CA', 'ASP', 8.18), ('C', 'ASP', 'N', 'ASP', 9.26)], [('CA', 'ASP', 'CB', 'ASP', 9.35), ('CA', 'ASP', 'CG', 'ASP', 8.65), ('CA', 'ASP', 'OD1', 'ASP', 9.48), ('CA', 'ASP', 'OD2', 'ASP', 7.45), ('CA', 'ASP', 'O', 'ASP', 8.88), ('CA', 'ASP', 'C', 'ASP', 8.05), ('CA', 'ASP', 'CA', 'ASP', 8.59), ('CA', 'ASP', 'N', 'ASP', 9.81)], [('N', 'ASP', 'CB', 'ASP', 10.78), ('N', 'ASP', 'CG', 'ASP', 10.11), ('N', 'ASP', 'OD1', 'ASP', 10.92), ('N', 'ASP', 'OD2', 'ASP', 8.93), ('N', 'ASP', 'O', 'ASP', 10.06), ('N', 'ASP', 'C', 'ASP', 9.28), ('N', 'ASP', 'CA', 'ASP', 9.93), ('N', 'ASP', 'N', 'ASP', 11.09)], [('CB', 'ASP', 'CB', 'ASP', 9.51), ('CB', 'ASP', 'CG', 'ASP', 8.25), ('CB', 'ASP', 'OD1', 'ASP', 7.11), ('CB', 'ASP', 'OD2', 'ASP', 8.56), ('CB', 'ASP', 'O', 'ASP', 9.56), ('CB', 'ASP', 'C', 'ASP', 9.0), ('CB', 'ASP', 'CA', 'ASP', 9.35), ('CB', 'ASP', 'N', 'ASP', 10.78)], [('CG', 'ASP', 'CB', 'ASP', 8.54), ('CG', 'ASP', 'CG', 'ASP', 7.16), ('CG', 'ASP', 'OD1', 'ASP', 6.15), ('CG', 'ASP', 'OD2', 'ASP', 7.29), ('CG', 'ASP', 'O', 'ASP', 9.02), ('CG', 'ASP', 'C', 'ASP', 8.5), ('CG', 'ASP', 'CA', 'ASP', 8.65), ('CG', 'ASP', 'N', 'ASP', 10.11)], [('OD1', 'ASP', 'CB', 'ASP', 9.17), ('OD1', 'ASP', 'CG', 'ASP', 7.72), ('OD1', 'ASP', 'OD1', 'ASP', 6.89), ('OD1', 'ASP', 'OD2', 'ASP', 7.63), ('OD1', 'ASP', 'O', 'ASP', 9.96), ('OD1', 'ASP', 'C', 'ASP', 9.48), ('OD1', 'ASP', 'CA', 'ASP', 9.48), ('OD1', 'ASP', 'N', 'ASP', 10.92)], [('OD2', 'ASP', 'CB', 'ASP', 7.32), ('OD2', 'ASP', 'CG', 'ASP', 5.96), ('OD2', 'ASP', 'OD1', 'ASP', 4.92), ('OD2', 'ASP', 'OD2', 'ASP', 6.19), ('OD2', 'ASP', 'O', 'ASP', 7.82), ('OD2', 'ASP', 'C', 'ASP', 7.32), ('OD2', 'ASP', 'CA', 'ASP', 7.45), ('OD2', 'ASP', 'N', 'ASP', 8.93)], [('O', 'ASP', 'CB', 'ASP', 9.27), ('O', 'ASP', 'CG', 'ASP', 8.34), ('O', 'ASP', 'OD1', 'ASP', 7.23), ('O', 'ASP', 'OD2', 'ASP', 8.93), ('O', 'ASP', 'O', 'ASP', 9.91), ('O', 'ASP', 'C', 'ASP', 8.97), ('O', 'ASP', 'CA', 'ASP', 8.88), ('O', 'ASP', 'N', 'ASP', 10.06)], [('C', 'ASP', 'CB', 'ASP', 8.58), ('C', 'ASP', 'CG', 'ASP', 7.7), ('C', 'ASP', 'OD1', 'ASP', 6.5), ('C', 'ASP', 'OD2', 'ASP', 8.41), ('C', 'ASP', 'O', 'ASP', 8.87), ('C', 'ASP', 'C', 'ASP', 7.95), ('C', 'ASP', 'CA', 'ASP', 8.05), ('C', 'ASP', 'N', 'ASP', 9.28)], [('CA', 'ASP', 'CB', 'ASP', 9.07), ('CA', 'ASP', 'CG', 'ASP', 8.05), ('CA', 'ASP', 'OD1', 'ASP', 6.81), ('CA', 'ASP', 'OD2', 'ASP', 8.65), ('CA', 'ASP', 'O', 'ASP', 8.89), ('CA', 'ASP', 'C', 'ASP', 8.18), ('CA', 'ASP', 'CA', 'ASP', 8.59), ('CA', 'ASP', 'N', 'ASP', 9.93)], [('N', 'ASP', 'CB', 'ASP', 10.41), ('N', 'ASP', 'CG', 'ASP', 9.45), ('N', 'ASP', 'OD1', 'ASP', 8.21), ('N', 'ASP', 'OD2', 'ASP', 10.08), ('N', 'ASP', 'O', 'ASP', 9.95), ('N', 'ASP', 'C', 'ASP', 9.26), ('N', 'ASP', 'CA', 'ASP', 9.81), ('N', 'ASP', 'N', 'ASP', 11.09)]]}
THR_SER = { 
	'distances':
		[[12.56, 12.53, 13.82, 13.88, 12.67, 11.51], [11.35, 11.43, 12.86, 12.8, 11.51, 10.45], [13.81, 13.86, 15.24, 15.24, 13.96, 12.86], [14.29, 13.95, 15.03, 15.35, 14.36, 13.09], [13.84, 13.52, 14.89, 15.11, 14.04, 12.86], [12.43, 12.19, 13.66, 13.79, 12.66, 11.53], [11.53, 11.19, 12.48, 12.72, 11.69, 10.5]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'SER', 12.56), ('CB', 'THR', 'OG', 'SER', 12.53), ('CB', 'THR', 'O', 'SER', 13.82), ('CB', 'THR', 'C', 'SER', 13.88), ('CB', 'THR', 'CA', 'SER', 12.67), ('CB', 'THR', 'N', 'SER', 11.51)], [('OG1', 'THR', 'CB', 'SER', 11.35), ('OG1', 'THR', 'OG', 'SER', 11.43), ('OG1', 'THR', 'O', 'SER', 12.86), ('OG1', 'THR', 'C', 'SER', 12.8), ('OG1', 'THR', 'CA', 'SER', 11.51), ('OG1', 'THR', 'N', 'SER', 10.45)], [('CG2', 'THR', 'CB', 'SER', 13.81), ('CG2', 'THR', 'OG', 'SER', 13.86), ('CG2', 'THR', 'O', 'SER', 15.24), ('CG2', 'THR', 'C', 'SER', 15.24), ('CG2', 'THR', 'CA', 'SER', 13.96), ('CG2', 'THR', 'N', 'SER', 12.86)], [('O', 'THR', 'CB', 'SER', 14.29), ('O', 'THR', 'OG', 'SER', 13.95), ('O', 'THR', 'O', 'SER', 15.03), ('O', 'THR', 'C', 'SER', 15.35), ('O', 'THR', 'CA', 'SER', 14.36), ('O', 'THR', 'N', 'SER', 13.09)], [('C', 'THR', 'CB', 'SER', 13.84), ('C', 'THR', 'OG', 'SER', 13.52), ('C', 'THR', 'O', 'SER', 14.89), ('C', 'THR', 'C', 'SER', 15.11), ('C', 'THR', 'CA', 'SER', 14.04), ('C', 'THR', 'N', 'SER', 12.86)], [('CA', 'THR', 'CB', 'SER', 12.43), ('CA', 'THR', 'OG', 'SER', 12.19), ('CA', 'THR', 'O', 'SER', 13.66), ('CA', 'THR', 'C', 'SER', 13.79), ('CA', 'THR', 'CA', 'SER', 12.66), ('CA', 'THR', 'N', 'SER', 11.53)], [('N', 'THR', 'CB', 'SER', 11.53), ('N', 'THR', 'OG', 'SER', 11.19), ('N', 'THR', 'O', 'SER', 12.48), ('N', 'THR', 'C', 'SER', 12.72), ('N', 'THR', 'CA', 'SER', 11.69), ('N', 'THR', 'N', 'SER', 10.5)]]}
ASP_THR = { 
	'distances':
		[[6.44, 6.22, 7.61, 7.76, 8.01, 7.11, 6.5], [6.17, 5.58, 7.53, 7.78, 7.76, 6.59, 5.82], [6.87, 6.35, 8.34, 8.01, 8.03, 6.91, 5.82], [5.76, 4.8, 7.01, 7.97, 7.7, 6.34, 5.87], [6.1, 6.69, 7.32, 5.62, 6.31, 6.07, 5.27], [7.03, 7.33, 8.33, 6.82, 7.44, 7.02, 6.02], [7.39, 7.42, 8.62, 7.89, 8.39, 7.75, 6.89], [8.2, 8.38, 9.22, 8.56, 9.22, 8.75, 8.08], [10.68, 10.05, 12.16, 11.15, 10.92, 9.93, 8.64], [9.71, 8.9, 11.15, 10.63, 10.31, 9.14, 7.95], [10.19, 9.22, 11.57, 11.45, 11.01, 9.73, 8.69], [8.65, 7.9, 10.13, 9.61, 9.35, 8.18, 6.95], [11.82, 11.15, 13.33, 12.43, 12.43, 11.41, 10.07], [11.0, 10.47, 12.53, 11.35, 11.43, 10.51, 9.11], [10.75, 10.3, 12.27, 10.87, 10.86, 10.02, 8.61], [11.95, 11.58, 13.46, 11.76, 11.79, 11.09, 9.67]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 6.44), ('CB', 'ASP', 'OG1', 'THR', 6.22), ('CB', 'ASP', 'CG2', 'THR', 7.61), ('CB', 'ASP', 'O', 'THR', 7.76), ('CB', 'ASP', 'C', 'THR', 8.01), ('CB', 'ASP', 'CA', 'THR', 7.11), ('CB', 'ASP', 'N', 'THR', 6.5)], [('CG', 'ASP', 'CB', 'THR', 6.17), ('CG', 'ASP', 'OG1', 'THR', 5.58), ('CG', 'ASP', 'CG2', 'THR', 7.53), ('CG', 'ASP', 'O', 'THR', 7.78), ('CG', 'ASP', 'C', 'THR', 7.76), ('CG', 'ASP', 'CA', 'THR', 6.59), ('CG', 'ASP', 'N', 'THR', 5.82)], [('OD1', 'ASP', 'CB', 'THR', 6.87), ('OD1', 'ASP', 'OG1', 'THR', 6.35), ('OD1', 'ASP', 'CG2', 'THR', 8.34), ('OD1', 'ASP', 'O', 'THR', 8.01), ('OD1', 'ASP', 'C', 'THR', 8.03), ('OD1', 'ASP', 'CA', 'THR', 6.91), ('OD1', 'ASP', 'N', 'THR', 5.82)], [('OD2', 'ASP', 'CB', 'THR', 5.76), ('OD2', 'ASP', 'OG1', 'THR', 4.8), ('OD2', 'ASP', 'CG2', 'THR', 7.01), ('OD2', 'ASP', 'O', 'THR', 7.97), ('OD2', 'ASP', 'C', 'THR', 7.7), ('OD2', 'ASP', 'CA', 'THR', 6.34), ('OD2', 'ASP', 'N', 'THR', 5.87)], [('O', 'ASP', 'CB', 'THR', 6.1), ('O', 'ASP', 'OG1', 'THR', 6.69), ('O', 'ASP', 'CG2', 'THR', 7.32), ('O', 'ASP', 'O', 'THR', 5.62), ('O', 'ASP', 'C', 'THR', 6.31), ('O', 'ASP', 'CA', 'THR', 6.07), ('O', 'ASP', 'N', 'THR', 5.27)], [('C', 'ASP', 'CB', 'THR', 7.03), ('C', 'ASP', 'OG1', 'THR', 7.33), ('C', 'ASP', 'CG2', 'THR', 8.33), ('C', 'ASP', 'O', 'THR', 6.82), ('C', 'ASP', 'C', 'THR', 7.44), ('C', 'ASP', 'CA', 'THR', 7.02), ('C', 'ASP', 'N', 'THR', 6.02)], [('CA', 'ASP', 'CB', 'THR', 7.39), ('CA', 'ASP', 'OG1', 'THR', 7.42), ('CA', 'ASP', 'CG2', 'THR', 8.62), ('CA', 'ASP', 'O', 'THR', 7.89), ('CA', 'ASP', 'C', 'THR', 8.39), ('CA', 'ASP', 'CA', 'THR', 7.75), ('CA', 'ASP', 'N', 'THR', 6.89)], [('N', 'ASP', 'CB', 'THR', 8.2), ('N', 'ASP', 'OG1', 'THR', 8.38), ('N', 'ASP', 'CG2', 'THR', 9.22), ('N', 'ASP', 'O', 'THR', 8.56), ('N', 'ASP', 'C', 'THR', 9.22), ('N', 'ASP', 'CA', 'THR', 8.75), ('N', 'ASP', 'N', 'THR', 8.08)], [('CB', 'ASP', 'CB', 'THR', 10.68), ('CB', 'ASP', 'OG1', 'THR', 10.05), ('CB', 'ASP', 'CG2', 'THR', 12.16), ('CB', 'ASP', 'O', 'THR', 11.15), ('CB', 'ASP', 'C', 'THR', 10.92), ('CB', 'ASP', 'CA', 'THR', 9.93), ('CB', 'ASP', 'N', 'THR', 8.64)], [('CG', 'ASP', 'CB', 'THR', 9.71), ('CG', 'ASP', 'OG1', 'THR', 8.9), ('CG', 'ASP', 'CG2', 'THR', 11.15), ('CG', 'ASP', 'O', 'THR', 10.63), ('CG', 'ASP', 'C', 'THR', 10.31), ('CG', 'ASP', 'CA', 'THR', 9.14), ('CG', 'ASP', 'N', 'THR', 7.95)], [('OD1', 'ASP', 'CB', 'THR', 10.19), ('OD1', 'ASP', 'OG1', 'THR', 9.22), ('OD1', 'ASP', 'CG2', 'THR', 11.57), ('OD1', 'ASP', 'O', 'THR', 11.45), ('OD1', 'ASP', 'C', 'THR', 11.01), ('OD1', 'ASP', 'CA', 'THR', 9.73), ('OD1', 'ASP', 'N', 'THR', 8.69)], [('OD2', 'ASP', 'CB', 'THR', 8.65), ('OD2', 'ASP', 'OG1', 'THR', 7.9), ('OD2', 'ASP', 'CG2', 'THR', 10.13), ('OD2', 'ASP', 'O', 'THR', 9.61), ('OD2', 'ASP', 'C', 'THR', 9.35), ('OD2', 'ASP', 'CA', 'THR', 8.18), ('OD2', 'ASP', 'N', 'THR', 6.95)], [('O', 'ASP', 'CB', 'THR', 11.82), ('O', 'ASP', 'OG1', 'THR', 11.15), ('O', 'ASP', 'CG2', 'THR', 13.33), ('O', 'ASP', 'O', 'THR', 12.43), ('O', 'ASP', 'C', 'THR', 12.43), ('O', 'ASP', 'CA', 'THR', 11.41), ('O', 'ASP', 'N', 'THR', 10.07)], [('C', 'ASP', 'CB', 'THR', 11.0), ('C', 'ASP', 'OG1', 'THR', 10.47), ('C', 'ASP', 'CG2', 'THR', 12.53), ('C', 'ASP', 'O', 'THR', 11.35), ('C', 'ASP', 'C', 'THR', 11.43), ('C', 'ASP', 'CA', 'THR', 10.51), ('C', 'ASP', 'N', 'THR', 9.11)], [('CA', 'ASP', 'CB', 'THR', 10.75), ('CA', 'ASP', 'OG1', 'THR', 10.3), ('CA', 'ASP', 'CG2', 'THR', 12.27), ('CA', 'ASP', 'O', 'THR', 10.87), ('CA', 'ASP', 'C', 'THR', 10.86), ('CA', 'ASP', 'CA', 'THR', 10.02), ('CA', 'ASP', 'N', 'THR', 8.61)], [('N', 'ASP', 'CB', 'THR', 11.95), ('N', 'ASP', 'OG1', 'THR', 11.58), ('N', 'ASP', 'CG2', 'THR', 13.46), ('N', 'ASP', 'O', 'THR', 11.76), ('N', 'ASP', 'C', 'THR', 11.79), ('N', 'ASP', 'CA', 'THR', 11.09), ('N', 'ASP', 'N', 'THR', 9.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_ASPI, d, 'A_1apt_3_4_23_20')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_SER, d, 'A_1apt_3_4_23_20')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'A_1apt_3_4_23_20')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_SER, d, 'A_1apt_3_4_23_20')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_THR, d, 'A_1apt_3_4_23_20')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_ASPI' :  match1,
		'ASP_SER' :  match2,
		'ASP_ASP' :  match3,
		'THR_SER' :  match4,
		'ASP_THR' :  match5}