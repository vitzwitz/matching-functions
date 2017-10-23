'''
FUNC:A_2jxr_3_4_23_25
PDB:2jxr
EC:3.4.23.25
RESI:asp,thr,asp,thr
LOCI:a-32,33,215,218;
'''
import motifFunctions as cmd
ASP_THRI = { 
	'distances':
		[[7.89, 8.17, 8.23, 8.0, 6.82, 6.58, 5.4], [7.8, 7.85, 8.45, 7.41, 6.29, 6.48, 5.52], [7.05, 6.87, 7.8, 6.75, 5.62, 5.89, 5.01], [8.79, 8.85, 9.54, 7.95, 6.97, 7.4, 6.61], [5.99, 6.79, 6.45, 5.98, 4.98, 4.54, 4.02], [5.53, 6.14, 5.85, 6.13, 4.95, 4.23, 3.14], [6.74, 7.15, 6.84, 7.48, 6.26, 5.59, 4.26], [7.54, 8.09, 7.28, 8.61, 7.43, 6.53, 5.24]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THRI', 7.89), ('CB', 'ASP', 'OG1', 'THRI', 8.17), ('CB', 'ASP', 'CG2', 'THRI', 8.23), ('CB', 'ASP', 'O', 'THRI', 8.0), ('CB', 'ASP', 'C', 'THRI', 6.82), ('CB', 'ASP', 'CA', 'THRI', 6.58), ('CB', 'ASP', 'N', 'THRI', 5.4)], [('CG', 'ASP', 'CB', 'THRI', 7.8), ('CG', 'ASP', 'OG1', 'THRI', 7.85), ('CG', 'ASP', 'CG2', 'THRI', 8.45), ('CG', 'ASP', 'O', 'THRI', 7.41), ('CG', 'ASP', 'C', 'THRI', 6.29), ('CG', 'ASP', 'CA', 'THRI', 6.48), ('CG', 'ASP', 'N', 'THRI', 5.52)], [('OD1', 'ASP', 'CB', 'THRI', 7.05), ('OD1', 'ASP', 'OG1', 'THRI', 6.87), ('OD1', 'ASP', 'CG2', 'THRI', 7.8), ('OD1', 'ASP', 'O', 'THRI', 6.75), ('OD1', 'ASP', 'C', 'THRI', 5.62), ('OD1', 'ASP', 'CA', 'THRI', 5.89), ('OD1', 'ASP', 'N', 'THRI', 5.01)], [('OD2', 'ASP', 'CB', 'THRI', 8.79), ('OD2', 'ASP', 'OG1', 'THRI', 8.85), ('OD2', 'ASP', 'CG2', 'THRI', 9.54), ('OD2', 'ASP', 'O', 'THRI', 7.95), ('OD2', 'ASP', 'C', 'THRI', 6.97), ('OD2', 'ASP', 'CA', 'THRI', 7.4), ('OD2', 'ASP', 'N', 'THRI', 6.61)], [('O', 'ASP', 'CB', 'THRI', 5.99), ('O', 'ASP', 'OG1', 'THRI', 6.79), ('O', 'ASP', 'CG2', 'THRI', 6.45), ('O', 'ASP', 'O', 'THRI', 5.98), ('O', 'ASP', 'C', 'THRI', 4.98), ('O', 'ASP', 'CA', 'THRI', 4.54), ('O', 'ASP', 'N', 'THRI', 4.02)], [('C', 'ASP', 'CB', 'THRI', 5.53), ('C', 'ASP', 'OG1', 'THRI', 6.14), ('C', 'ASP', 'CG2', 'THRI', 5.85), ('C', 'ASP', 'O', 'THRI', 6.13), ('C', 'ASP', 'C', 'THRI', 4.95), ('C', 'ASP', 'CA', 'THRI', 4.23), ('C', 'ASP', 'N', 'THRI', 3.14)], [('CA', 'ASP', 'CB', 'THRI', 6.74), ('CA', 'ASP', 'OG1', 'THRI', 7.15), ('CA', 'ASP', 'CG2', 'THRI', 6.84), ('CA', 'ASP', 'O', 'THRI', 7.48), ('CA', 'ASP', 'C', 'THRI', 6.26), ('CA', 'ASP', 'CA', 'THRI', 5.59), ('CA', 'ASP', 'N', 'THRI', 4.26)], [('N', 'ASP', 'CB', 'THRI', 7.54), ('N', 'ASP', 'OG1', 'THRI', 8.09), ('N', 'ASP', 'CG2', 'THRI', 7.28), ('N', 'ASP', 'O', 'THRI', 8.61), ('N', 'ASP', 'C', 'THRI', 7.43), ('N', 'ASP', 'CA', 'THRI', 6.53), ('N', 'ASP', 'N', 'THRI', 5.24)]]}
ASP_ASP = { 
	'distances':
		[[9.34, 8.34, 7.11, 9.0, 9.3, 8.59, 9.06, 10.31], [8.15, 7.03, 5.83, 7.6, 8.32, 7.67, 8.07, 9.39], [6.97, 5.94, 4.7, 6.64, 7.18, 6.48, 6.84, 8.17], [8.64, 7.36, 6.28, 7.68, 8.98, 8.46, 8.81, 10.17], [9.61, 9.01, 7.84, 9.93, 9.98, 8.96, 9.05, 9.98], [8.93, 8.36, 7.16, 9.34, 8.97, 7.98, 8.26, 9.23], [9.29, 8.54, 7.31, 9.4, 8.95, 8.14, 8.69, 9.81], [10.7, 9.96, 8.73, 10.79, 10.13, 9.37, 10.02, 11.1], [9.34, 8.15, 6.97, 8.64, 9.61, 8.93, 9.29, 10.7], [8.34, 7.03, 5.94, 7.36, 9.01, 8.36, 8.54, 9.96], [7.11, 5.83, 4.7, 6.28, 7.84, 7.16, 7.31, 8.73], [9.0, 7.6, 6.64, 7.68, 9.93, 9.34, 9.4, 10.79], [9.3, 8.32, 7.18, 8.98, 9.98, 8.97, 8.95, 10.13], [8.59, 7.67, 6.48, 8.46, 8.96, 7.98, 8.14, 9.37], [9.06, 8.07, 6.84, 8.81, 9.05, 8.26, 8.69, 10.02], [10.31, 9.39, 8.17, 10.17, 9.98, 9.23, 9.81, 11.1]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 9.34), ('CB', 'ASP', 'CG', 'ASP', 8.34), ('CB', 'ASP', 'OD1', 'ASP', 7.11), ('CB', 'ASP', 'OD2', 'ASP', 9.0), ('CB', 'ASP', 'O', 'ASP', 9.3), ('CB', 'ASP', 'C', 'ASP', 8.59), ('CB', 'ASP', 'CA', 'ASP', 9.06), ('CB', 'ASP', 'N', 'ASP', 10.31)], [('CG', 'ASP', 'CB', 'ASP', 8.15), ('CG', 'ASP', 'CG', 'ASP', 7.03), ('CG', 'ASP', 'OD1', 'ASP', 5.83), ('CG', 'ASP', 'OD2', 'ASP', 7.6), ('CG', 'ASP', 'O', 'ASP', 8.32), ('CG', 'ASP', 'C', 'ASP', 7.67), ('CG', 'ASP', 'CA', 'ASP', 8.07), ('CG', 'ASP', 'N', 'ASP', 9.39)], [('OD1', 'ASP', 'CB', 'ASP', 6.97), ('OD1', 'ASP', 'CG', 'ASP', 5.94), ('OD1', 'ASP', 'OD1', 'ASP', 4.7), ('OD1', 'ASP', 'OD2', 'ASP', 6.64), ('OD1', 'ASP', 'O', 'ASP', 7.18), ('OD1', 'ASP', 'C', 'ASP', 6.48), ('OD1', 'ASP', 'CA', 'ASP', 6.84), ('OD1', 'ASP', 'N', 'ASP', 8.17)], [('OD2', 'ASP', 'CB', 'ASP', 8.64), ('OD2', 'ASP', 'CG', 'ASP', 7.36), ('OD2', 'ASP', 'OD1', 'ASP', 6.28), ('OD2', 'ASP', 'OD2', 'ASP', 7.68), ('OD2', 'ASP', 'O', 'ASP', 8.98), ('OD2', 'ASP', 'C', 'ASP', 8.46), ('OD2', 'ASP', 'CA', 'ASP', 8.81), ('OD2', 'ASP', 'N', 'ASP', 10.17)], [('O', 'ASP', 'CB', 'ASP', 9.61), ('O', 'ASP', 'CG', 'ASP', 9.01), ('O', 'ASP', 'OD1', 'ASP', 7.84), ('O', 'ASP', 'OD2', 'ASP', 9.93), ('O', 'ASP', 'O', 'ASP', 9.98), ('O', 'ASP', 'C', 'ASP', 8.96), ('O', 'ASP', 'CA', 'ASP', 9.05), ('O', 'ASP', 'N', 'ASP', 9.98)], [('C', 'ASP', 'CB', 'ASP', 8.93), ('C', 'ASP', 'CG', 'ASP', 8.36), ('C', 'ASP', 'OD1', 'ASP', 7.16), ('C', 'ASP', 'OD2', 'ASP', 9.34), ('C', 'ASP', 'O', 'ASP', 8.97), ('C', 'ASP', 'C', 'ASP', 7.98), ('C', 'ASP', 'CA', 'ASP', 8.26), ('C', 'ASP', 'N', 'ASP', 9.23)], [('CA', 'ASP', 'CB', 'ASP', 9.29), ('CA', 'ASP', 'CG', 'ASP', 8.54), ('CA', 'ASP', 'OD1', 'ASP', 7.31), ('CA', 'ASP', 'OD2', 'ASP', 9.4), ('CA', 'ASP', 'O', 'ASP', 8.95), ('CA', 'ASP', 'C', 'ASP', 8.14), ('CA', 'ASP', 'CA', 'ASP', 8.69), ('CA', 'ASP', 'N', 'ASP', 9.81)], [('N', 'ASP', 'CB', 'ASP', 10.7), ('N', 'ASP', 'CG', 'ASP', 9.96), ('N', 'ASP', 'OD1', 'ASP', 8.73), ('N', 'ASP', 'OD2', 'ASP', 10.79), ('N', 'ASP', 'O', 'ASP', 10.13), ('N', 'ASP', 'C', 'ASP', 9.37), ('N', 'ASP', 'CA', 'ASP', 10.02), ('N', 'ASP', 'N', 'ASP', 11.1)], [('CB', 'ASP', 'CB', 'ASP', 9.34), ('CB', 'ASP', 'CG', 'ASP', 8.15), ('CB', 'ASP', 'OD1', 'ASP', 6.97), ('CB', 'ASP', 'OD2', 'ASP', 8.64), ('CB', 'ASP', 'O', 'ASP', 9.61), ('CB', 'ASP', 'C', 'ASP', 8.93), ('CB', 'ASP', 'CA', 'ASP', 9.29), ('CB', 'ASP', 'N', 'ASP', 10.7)], [('CG', 'ASP', 'CB', 'ASP', 8.34), ('CG', 'ASP', 'CG', 'ASP', 7.03), ('CG', 'ASP', 'OD1', 'ASP', 5.94), ('CG', 'ASP', 'OD2', 'ASP', 7.36), ('CG', 'ASP', 'O', 'ASP', 9.01), ('CG', 'ASP', 'C', 'ASP', 8.36), ('CG', 'ASP', 'CA', 'ASP', 8.54), ('CG', 'ASP', 'N', 'ASP', 9.96)], [('OD1', 'ASP', 'CB', 'ASP', 7.11), ('OD1', 'ASP', 'CG', 'ASP', 5.83), ('OD1', 'ASP', 'OD1', 'ASP', 4.7), ('OD1', 'ASP', 'OD2', 'ASP', 6.28), ('OD1', 'ASP', 'O', 'ASP', 7.84), ('OD1', 'ASP', 'C', 'ASP', 7.16), ('OD1', 'ASP', 'CA', 'ASP', 7.31), ('OD1', 'ASP', 'N', 'ASP', 8.73)], [('OD2', 'ASP', 'CB', 'ASP', 9.0), ('OD2', 'ASP', 'CG', 'ASP', 7.6), ('OD2', 'ASP', 'OD1', 'ASP', 6.64), ('OD2', 'ASP', 'OD2', 'ASP', 7.68), ('OD2', 'ASP', 'O', 'ASP', 9.93), ('OD2', 'ASP', 'C', 'ASP', 9.34), ('OD2', 'ASP', 'CA', 'ASP', 9.4), ('OD2', 'ASP', 'N', 'ASP', 10.79)], [('O', 'ASP', 'CB', 'ASP', 9.3), ('O', 'ASP', 'CG', 'ASP', 8.32), ('O', 'ASP', 'OD1', 'ASP', 7.18), ('O', 'ASP', 'OD2', 'ASP', 8.98), ('O', 'ASP', 'O', 'ASP', 9.98), ('O', 'ASP', 'C', 'ASP', 8.97), ('O', 'ASP', 'CA', 'ASP', 8.95), ('O', 'ASP', 'N', 'ASP', 10.13)], [('C', 'ASP', 'CB', 'ASP', 8.59), ('C', 'ASP', 'CG', 'ASP', 7.67), ('C', 'ASP', 'OD1', 'ASP', 6.48), ('C', 'ASP', 'OD2', 'ASP', 8.46), ('C', 'ASP', 'O', 'ASP', 8.96), ('C', 'ASP', 'C', 'ASP', 7.98), ('C', 'ASP', 'CA', 'ASP', 8.14), ('C', 'ASP', 'N', 'ASP', 9.37)], [('CA', 'ASP', 'CB', 'ASP', 9.06), ('CA', 'ASP', 'CG', 'ASP', 8.07), ('CA', 'ASP', 'OD1', 'ASP', 6.84), ('CA', 'ASP', 'OD2', 'ASP', 8.81), ('CA', 'ASP', 'O', 'ASP', 9.05), ('CA', 'ASP', 'C', 'ASP', 8.26), ('CA', 'ASP', 'CA', 'ASP', 8.69), ('CA', 'ASP', 'N', 'ASP', 10.02)], [('N', 'ASP', 'CB', 'ASP', 10.31), ('N', 'ASP', 'CG', 'ASP', 9.39), ('N', 'ASP', 'OD1', 'ASP', 8.17), ('N', 'ASP', 'OD2', 'ASP', 10.17), ('N', 'ASP', 'O', 'ASP', 9.98), ('N', 'ASP', 'C', 'ASP', 9.23), ('N', 'ASP', 'CA', 'ASP', 9.81), ('N', 'ASP', 'N', 'ASP', 11.1)]]}
THR_THR = { 
	'distances':
		[[11.17, 9.98, 11.9, 11.05, 10.42, 10.93, 10.41], [10.53, 9.42, 11.42, 10.05, 9.46, 10.14, 9.7], [12.58, 11.37, 13.35, 12.31, 11.75, 12.34, 11.87], [11.65, 10.45, 11.94, 12.4, 11.62, 11.66, 10.94], [12.04, 10.89, 12.44, 12.53, 11.72, 11.88, 11.11], [11.21, 10.11, 11.76, 11.4, 10.6, 10.9, 10.17], [9.96, 8.95, 10.44, 10.35, 9.46, 9.62, 8.8], [11.17, 10.53, 12.58, 11.65, 12.04, 11.21, 9.96], [9.98, 9.42, 11.37, 10.45, 10.89, 10.11, 8.95], [11.9, 11.42, 13.35, 11.94, 12.44, 11.76, 10.44], [11.05, 10.05, 12.31, 12.4, 12.53, 11.4, 10.35], [10.42, 9.46, 11.75, 11.62, 11.72, 10.6, 9.46], [10.93, 10.14, 12.34, 11.66, 11.88, 10.9, 9.62], [10.41, 9.7, 11.87, 10.94, 11.11, 10.17, 8.8]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'THR', 11.17), ('CB', 'THR', 'OG1', 'THR', 9.98), ('CB', 'THR', 'CG2', 'THR', 11.9), ('CB', 'THR', 'O', 'THR', 11.05), ('CB', 'THR', 'C', 'THR', 10.42), ('CB', 'THR', 'CA', 'THR', 10.93), ('CB', 'THR', 'N', 'THR', 10.41)], [('OG1', 'THR', 'CB', 'THR', 10.53), ('OG1', 'THR', 'OG1', 'THR', 9.42), ('OG1', 'THR', 'CG2', 'THR', 11.42), ('OG1', 'THR', 'O', 'THR', 10.05), ('OG1', 'THR', 'C', 'THR', 9.46), ('OG1', 'THR', 'CA', 'THR', 10.14), ('OG1', 'THR', 'N', 'THR', 9.7)], [('CG2', 'THR', 'CB', 'THR', 12.58), ('CG2', 'THR', 'OG1', 'THR', 11.37), ('CG2', 'THR', 'CG2', 'THR', 13.35), ('CG2', 'THR', 'O', 'THR', 12.31), ('CG2', 'THR', 'C', 'THR', 11.75), ('CG2', 'THR', 'CA', 'THR', 12.34), ('CG2', 'THR', 'N', 'THR', 11.87)], [('O', 'THR', 'CB', 'THR', 11.65), ('O', 'THR', 'OG1', 'THR', 10.45), ('O', 'THR', 'CG2', 'THR', 11.94), ('O', 'THR', 'O', 'THR', 12.4), ('O', 'THR', 'C', 'THR', 11.62), ('O', 'THR', 'CA', 'THR', 11.66), ('O', 'THR', 'N', 'THR', 10.94)], [('C', 'THR', 'CB', 'THR', 12.04), ('C', 'THR', 'OG1', 'THR', 10.89), ('C', 'THR', 'CG2', 'THR', 12.44), ('C', 'THR', 'O', 'THR', 12.53), ('C', 'THR', 'C', 'THR', 11.72), ('C', 'THR', 'CA', 'THR', 11.88), ('C', 'THR', 'N', 'THR', 11.11)], [('CA', 'THR', 'CB', 'THR', 11.21), ('CA', 'THR', 'OG1', 'THR', 10.11), ('CA', 'THR', 'CG2', 'THR', 11.76), ('CA', 'THR', 'O', 'THR', 11.4), ('CA', 'THR', 'C', 'THR', 10.6), ('CA', 'THR', 'CA', 'THR', 10.9), ('CA', 'THR', 'N', 'THR', 10.17)], [('N', 'THR', 'CB', 'THR', 9.96), ('N', 'THR', 'OG1', 'THR', 8.95), ('N', 'THR', 'CG2', 'THR', 10.44), ('N', 'THR', 'O', 'THR', 10.35), ('N', 'THR', 'C', 'THR', 9.46), ('N', 'THR', 'CA', 'THR', 9.62), ('N', 'THR', 'N', 'THR', 8.8)], [('CB', 'THR', 'CB', 'THR', 11.17), ('CB', 'THR', 'OG1', 'THR', 10.53), ('CB', 'THR', 'CG2', 'THR', 12.58), ('CB', 'THR', 'O', 'THR', 11.65), ('CB', 'THR', 'C', 'THR', 12.04), ('CB', 'THR', 'CA', 'THR', 11.21), ('CB', 'THR', 'N', 'THR', 9.96)], [('OG1', 'THR', 'CB', 'THR', 9.98), ('OG1', 'THR', 'OG1', 'THR', 9.42), ('OG1', 'THR', 'CG2', 'THR', 11.37), ('OG1', 'THR', 'O', 'THR', 10.45), ('OG1', 'THR', 'C', 'THR', 10.89), ('OG1', 'THR', 'CA', 'THR', 10.11), ('OG1', 'THR', 'N', 'THR', 8.95)], [('CG2', 'THR', 'CB', 'THR', 11.9), ('CG2', 'THR', 'OG1', 'THR', 11.42), ('CG2', 'THR', 'CG2', 'THR', 13.35), ('CG2', 'THR', 'O', 'THR', 11.94), ('CG2', 'THR', 'C', 'THR', 12.44), ('CG2', 'THR', 'CA', 'THR', 11.76), ('CG2', 'THR', 'N', 'THR', 10.44)], [('O', 'THR', 'CB', 'THR', 11.05), ('O', 'THR', 'OG1', 'THR', 10.05), ('O', 'THR', 'CG2', 'THR', 12.31), ('O', 'THR', 'O', 'THR', 12.4), ('O', 'THR', 'C', 'THR', 12.53), ('O', 'THR', 'CA', 'THR', 11.4), ('O', 'THR', 'N', 'THR', 10.35)], [('C', 'THR', 'CB', 'THR', 10.42), ('C', 'THR', 'OG1', 'THR', 9.46), ('C', 'THR', 'CG2', 'THR', 11.75), ('C', 'THR', 'O', 'THR', 11.62), ('C', 'THR', 'C', 'THR', 11.72), ('C', 'THR', 'CA', 'THR', 10.6), ('C', 'THR', 'N', 'THR', 9.46)], [('CA', 'THR', 'CB', 'THR', 10.93), ('CA', 'THR', 'OG1', 'THR', 10.14), ('CA', 'THR', 'CG2', 'THR', 12.34), ('CA', 'THR', 'O', 'THR', 11.66), ('CA', 'THR', 'C', 'THR', 11.88), ('CA', 'THR', 'CA', 'THR', 10.9), ('CA', 'THR', 'N', 'THR', 9.62)], [('N', 'THR', 'CB', 'THR', 10.41), ('N', 'THR', 'OG1', 'THR', 9.7), ('N', 'THR', 'CG2', 'THR', 11.87), ('N', 'THR', 'O', 'THR', 10.94), ('N', 'THR', 'C', 'THR', 11.11), ('N', 'THR', 'CA', 'THR', 10.17), ('N', 'THR', 'N', 'THR', 8.8)]]}
THR_ASP = { 
	'distances':
		[[6.25, 6.08, 6.68, 5.74, 6.32, 7.04, 7.33, 8.13], [5.73, 5.22, 5.84, 4.6, 6.59, 6.99, 7.01, 7.93], [7.41, 7.34, 8.06, 6.8, 7.59, 8.39, 8.58, 9.2], [7.58, 7.77, 8.07, 8.02, 5.85, 6.98, 7.93, 8.6], [7.84, 7.79, 8.07, 7.83, 6.59, 7.59, 8.42, 9.22], [6.95, 6.64, 6.9, 6.55, 6.33, 7.11, 7.75, 8.71], [6.4, 5.93, 5.9, 6.15, 5.58, 6.16, 6.95, 8.11], [10.35, 9.3, 8.38, 9.63, 11.66, 10.86, 10.63, 11.73], [9.58, 8.38, 7.48, 8.6, 10.77, 10.09, 9.97, 11.18], [11.68, 10.59, 9.73, 10.8, 13.06, 12.29, 12.05, 13.16], [11.09, 10.46, 9.56, 11.11, 12.52, 11.48, 11.03, 11.82], [10.85, 10.13, 9.32, 10.64, 12.49, 11.52, 11.0, 11.83], [9.78, 8.91, 8.1, 9.33, 11.4, 10.51, 10.06, 11.02], [8.49, 7.73, 6.89, 8.31, 10.08, 9.13, 8.65, 9.59], [7.42, 7.26, 6.55, 8.31, 7.97, 6.74, 6.42, 7.05], [6.11, 6.16, 5.63, 7.28, 6.64, 5.4, 4.99, 5.64], [8.41, 8.33, 7.55, 9.47, 8.32, 7.16, 7.2, 7.78], [7.3, 6.8, 6.3, 7.4, 9.04, 7.87, 7.02, 7.67], [6.99, 6.31, 5.55, 7.02, 8.42, 7.26, 6.67, 7.59], [7.58, 7.03, 6.11, 7.95, 8.35, 7.16, 6.89, 7.82], [7.66, 6.95, 5.84, 7.9, 8.0, 6.93, 7.02, 8.17], [7.89, 7.8, 7.05, 8.79, 5.99, 5.53, 6.74, 7.54], [8.17, 7.85, 6.87, 8.85, 6.79, 6.14, 7.15, 8.09], [8.23, 8.45, 7.8, 9.54, 6.45, 5.85, 6.84, 7.28], [8.0, 7.41, 6.75, 7.95, 5.98, 6.13, 7.48, 8.61], [6.82, 6.29, 5.62, 6.97, 4.98, 4.95, 6.26, 7.43], [6.58, 6.48, 5.89, 7.4, 4.54, 4.23, 5.59, 6.53], [5.4, 5.52, 5.01, 6.61, 4.02, 3.14, 4.26, 5.24]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 6.25), ('CB', 'THR', 'CG', 'ASP', 6.08), ('CB', 'THR', 'OD1', 'ASP', 6.68), ('CB', 'THR', 'OD2', 'ASP', 5.74), ('CB', 'THR', 'O', 'ASP', 6.32), ('CB', 'THR', 'C', 'ASP', 7.04), ('CB', 'THR', 'CA', 'ASP', 7.33), ('CB', 'THR', 'N', 'ASP', 8.13)], [('OG1', 'THR', 'CB', 'ASP', 5.73), ('OG1', 'THR', 'CG', 'ASP', 5.22), ('OG1', 'THR', 'OD1', 'ASP', 5.84), ('OG1', 'THR', 'OD2', 'ASP', 4.6), ('OG1', 'THR', 'O', 'ASP', 6.59), ('OG1', 'THR', 'C', 'ASP', 6.99), ('OG1', 'THR', 'CA', 'ASP', 7.01), ('OG1', 'THR', 'N', 'ASP', 7.93)], [('CG2', 'THR', 'CB', 'ASP', 7.41), ('CG2', 'THR', 'CG', 'ASP', 7.34), ('CG2', 'THR', 'OD1', 'ASP', 8.06), ('CG2', 'THR', 'OD2', 'ASP', 6.8), ('CG2', 'THR', 'O', 'ASP', 7.59), ('CG2', 'THR', 'C', 'ASP', 8.39), ('CG2', 'THR', 'CA', 'ASP', 8.58), ('CG2', 'THR', 'N', 'ASP', 9.2)], [('O', 'THR', 'CB', 'ASP', 7.58), ('O', 'THR', 'CG', 'ASP', 7.77), ('O', 'THR', 'OD1', 'ASP', 8.07), ('O', 'THR', 'OD2', 'ASP', 8.02), ('O', 'THR', 'O', 'ASP', 5.85), ('O', 'THR', 'C', 'ASP', 6.98), ('O', 'THR', 'CA', 'ASP', 7.93), ('O', 'THR', 'N', 'ASP', 8.6)], [('C', 'THR', 'CB', 'ASP', 7.84), ('C', 'THR', 'CG', 'ASP', 7.79), ('C', 'THR', 'OD1', 'ASP', 8.07), ('C', 'THR', 'OD2', 'ASP', 7.83), ('C', 'THR', 'O', 'ASP', 6.59), ('C', 'THR', 'C', 'ASP', 7.59), ('C', 'THR', 'CA', 'ASP', 8.42), ('C', 'THR', 'N', 'ASP', 9.22)], [('CA', 'THR', 'CB', 'ASP', 6.95), ('CA', 'THR', 'CG', 'ASP', 6.64), ('CA', 'THR', 'OD1', 'ASP', 6.9), ('CA', 'THR', 'OD2', 'ASP', 6.55), ('CA', 'THR', 'O', 'ASP', 6.33), ('CA', 'THR', 'C', 'ASP', 7.11), ('CA', 'THR', 'CA', 'ASP', 7.75), ('CA', 'THR', 'N', 'ASP', 8.71)], [('N', 'THR', 'CB', 'ASP', 6.4), ('N', 'THR', 'CG', 'ASP', 5.93), ('N', 'THR', 'OD1', 'ASP', 5.9), ('N', 'THR', 'OD2', 'ASP', 6.15), ('N', 'THR', 'O', 'ASP', 5.58), ('N', 'THR', 'C', 'ASP', 6.16), ('N', 'THR', 'CA', 'ASP', 6.95), ('N', 'THR', 'N', 'ASP', 8.11)], [('CB', 'THR', 'CB', 'ASP', 10.35), ('CB', 'THR', 'CG', 'ASP', 9.3), ('CB', 'THR', 'OD1', 'ASP', 8.38), ('CB', 'THR', 'OD2', 'ASP', 9.63), ('CB', 'THR', 'O', 'ASP', 11.66), ('CB', 'THR', 'C', 'ASP', 10.86), ('CB', 'THR', 'CA', 'ASP', 10.63), ('CB', 'THR', 'N', 'ASP', 11.73)], [('OG1', 'THR', 'CB', 'ASP', 9.58), ('OG1', 'THR', 'CG', 'ASP', 8.38), ('OG1', 'THR', 'OD1', 'ASP', 7.48), ('OG1', 'THR', 'OD2', 'ASP', 8.6), ('OG1', 'THR', 'O', 'ASP', 10.77), ('OG1', 'THR', 'C', 'ASP', 10.09), ('OG1', 'THR', 'CA', 'ASP', 9.97), ('OG1', 'THR', 'N', 'ASP', 11.18)], [('CG2', 'THR', 'CB', 'ASP', 11.68), ('CG2', 'THR', 'CG', 'ASP', 10.59), ('CG2', 'THR', 'OD1', 'ASP', 9.73), ('CG2', 'THR', 'OD2', 'ASP', 10.8), ('CG2', 'THR', 'O', 'ASP', 13.06), ('CG2', 'THR', 'C', 'ASP', 12.29), ('CG2', 'THR', 'CA', 'ASP', 12.05), ('CG2', 'THR', 'N', 'ASP', 13.16)], [('O', 'THR', 'CB', 'ASP', 11.09), ('O', 'THR', 'CG', 'ASP', 10.46), ('O', 'THR', 'OD1', 'ASP', 9.56), ('O', 'THR', 'OD2', 'ASP', 11.11), ('O', 'THR', 'O', 'ASP', 12.52), ('O', 'THR', 'C', 'ASP', 11.48), ('O', 'THR', 'CA', 'ASP', 11.03), ('O', 'THR', 'N', 'ASP', 11.82)], [('C', 'THR', 'CB', 'ASP', 10.85), ('C', 'THR', 'CG', 'ASP', 10.13), ('C', 'THR', 'OD1', 'ASP', 9.32), ('C', 'THR', 'OD2', 'ASP', 10.64), ('C', 'THR', 'O', 'ASP', 12.49), ('C', 'THR', 'C', 'ASP', 11.52), ('C', 'THR', 'CA', 'ASP', 11.0), ('C', 'THR', 'N', 'ASP', 11.83)], [('CA', 'THR', 'CB', 'ASP', 9.78), ('CA', 'THR', 'CG', 'ASP', 8.91), ('CA', 'THR', 'OD1', 'ASP', 8.1), ('CA', 'THR', 'OD2', 'ASP', 9.33), ('CA', 'THR', 'O', 'ASP', 11.4), ('CA', 'THR', 'C', 'ASP', 10.51), ('CA', 'THR', 'CA', 'ASP', 10.06), ('CA', 'THR', 'N', 'ASP', 11.02)], [('N', 'THR', 'CB', 'ASP', 8.49), ('N', 'THR', 'CG', 'ASP', 7.73), ('N', 'THR', 'OD1', 'ASP', 6.89), ('N', 'THR', 'OD2', 'ASP', 8.31), ('N', 'THR', 'O', 'ASP', 10.08), ('N', 'THR', 'C', 'ASP', 9.13), ('N', 'THR', 'CA', 'ASP', 8.65), ('N', 'THR', 'N', 'ASP', 9.59)], [('CB', 'THR', 'CB', 'ASP', 7.42), ('CB', 'THR', 'CG', 'ASP', 7.26), ('CB', 'THR', 'OD1', 'ASP', 6.55), ('CB', 'THR', 'OD2', 'ASP', 8.31), ('CB', 'THR', 'O', 'ASP', 7.97), ('CB', 'THR', 'C', 'ASP', 6.74), ('CB', 'THR', 'CA', 'ASP', 6.42), ('CB', 'THR', 'N', 'ASP', 7.05)], [('OG1', 'THR', 'CB', 'ASP', 6.11), ('OG1', 'THR', 'CG', 'ASP', 6.16), ('OG1', 'THR', 'OD1', 'ASP', 5.63), ('OG1', 'THR', 'OD2', 'ASP', 7.28), ('OG1', 'THR', 'O', 'ASP', 6.64), ('OG1', 'THR', 'C', 'ASP', 5.4), ('OG1', 'THR', 'CA', 'ASP', 4.99), ('OG1', 'THR', 'N', 'ASP', 5.64)], [('CG2', 'THR', 'CB', 'ASP', 8.41), ('CG2', 'THR', 'CG', 'ASP', 8.33), ('CG2', 'THR', 'OD1', 'ASP', 7.55), ('CG2', 'THR', 'OD2', 'ASP', 9.47), ('CG2', 'THR', 'O', 'ASP', 8.32), ('CG2', 'THR', 'C', 'ASP', 7.16), ('CG2', 'THR', 'CA', 'ASP', 7.2), ('CG2', 'THR', 'N', 'ASP', 7.78)], [('O', 'THR', 'CB', 'ASP', 7.3), ('O', 'THR', 'CG', 'ASP', 6.8), ('O', 'THR', 'OD1', 'ASP', 6.3), ('O', 'THR', 'OD2', 'ASP', 7.4), ('O', 'THR', 'O', 'ASP', 9.04), ('O', 'THR', 'C', 'ASP', 7.87), ('O', 'THR', 'CA', 'ASP', 7.02), ('O', 'THR', 'N', 'ASP', 7.67)], [('C', 'THR', 'CB', 'ASP', 6.99), ('C', 'THR', 'CG', 'ASP', 6.31), ('C', 'THR', 'OD1', 'ASP', 5.55), ('C', 'THR', 'OD2', 'ASP', 7.02), ('C', 'THR', 'O', 'ASP', 8.42), ('C', 'THR', 'C', 'ASP', 7.26), ('C', 'THR', 'CA', 'ASP', 6.67), ('C', 'THR', 'N', 'ASP', 7.59)], [('CA', 'THR', 'CB', 'ASP', 7.58), ('CA', 'THR', 'CG', 'ASP', 7.03), ('CA', 'THR', 'OD1', 'ASP', 6.11), ('CA', 'THR', 'OD2', 'ASP', 7.95), ('CA', 'THR', 'O', 'ASP', 8.35), ('CA', 'THR', 'C', 'ASP', 7.16), ('CA', 'THR', 'CA', 'ASP', 6.89), ('CA', 'THR', 'N', 'ASP', 7.82)], [('N', 'THR', 'CB', 'ASP', 7.66), ('N', 'THR', 'CG', 'ASP', 6.95), ('N', 'THR', 'OD1', 'ASP', 5.84), ('N', 'THR', 'OD2', 'ASP', 7.9), ('N', 'THR', 'O', 'ASP', 8.0), ('N', 'THR', 'C', 'ASP', 6.93), ('N', 'THR', 'CA', 'ASP', 7.02), ('N', 'THR', 'N', 'ASP', 8.17)], [('CB', 'THR', 'CB', 'ASP', 7.89), ('CB', 'THR', 'CG', 'ASP', 7.8), ('CB', 'THR', 'OD1', 'ASP', 7.05), ('CB', 'THR', 'OD2', 'ASP', 8.79), ('CB', 'THR', 'O', 'ASP', 5.99), ('CB', 'THR', 'C', 'ASP', 5.53), ('CB', 'THR', 'CA', 'ASP', 6.74), ('CB', 'THR', 'N', 'ASP', 7.54)], [('OG1', 'THR', 'CB', 'ASP', 8.17), ('OG1', 'THR', 'CG', 'ASP', 7.85), ('OG1', 'THR', 'OD1', 'ASP', 6.87), ('OG1', 'THR', 'OD2', 'ASP', 8.85), ('OG1', 'THR', 'O', 'ASP', 6.79), ('OG1', 'THR', 'C', 'ASP', 6.14), ('OG1', 'THR', 'CA', 'ASP', 7.15), ('OG1', 'THR', 'N', 'ASP', 8.09)], [('CG2', 'THR', 'CB', 'ASP', 8.23), ('CG2', 'THR', 'CG', 'ASP', 8.45), ('CG2', 'THR', 'OD1', 'ASP', 7.8), ('CG2', 'THR', 'OD2', 'ASP', 9.54), ('CG2', 'THR', 'O', 'ASP', 6.45), ('CG2', 'THR', 'C', 'ASP', 5.85), ('CG2', 'THR', 'CA', 'ASP', 6.84), ('CG2', 'THR', 'N', 'ASP', 7.28)], [('O', 'THR', 'CB', 'ASP', 8.0), ('O', 'THR', 'CG', 'ASP', 7.41), ('O', 'THR', 'OD1', 'ASP', 6.75), ('O', 'THR', 'OD2', 'ASP', 7.95), ('O', 'THR', 'O', 'ASP', 5.98), ('O', 'THR', 'C', 'ASP', 6.13), ('O', 'THR', 'CA', 'ASP', 7.48), ('O', 'THR', 'N', 'ASP', 8.61)], [('C', 'THR', 'CB', 'ASP', 6.82), ('C', 'THR', 'CG', 'ASP', 6.29), ('C', 'THR', 'OD1', 'ASP', 5.62), ('C', 'THR', 'OD2', 'ASP', 6.97), ('C', 'THR', 'O', 'ASP', 4.98), ('C', 'THR', 'C', 'ASP', 4.95), ('C', 'THR', 'CA', 'ASP', 6.26), ('C', 'THR', 'N', 'ASP', 7.43)], [('CA', 'THR', 'CB', 'ASP', 6.58), ('CA', 'THR', 'CG', 'ASP', 6.48), ('CA', 'THR', 'OD1', 'ASP', 5.89), ('CA', 'THR', 'OD2', 'ASP', 7.4), ('CA', 'THR', 'O', 'ASP', 4.54), ('CA', 'THR', 'C', 'ASP', 4.23), ('CA', 'THR', 'CA', 'ASP', 5.59), ('CA', 'THR', 'N', 'ASP', 6.53)], [('N', 'THR', 'CB', 'ASP', 5.4), ('N', 'THR', 'CG', 'ASP', 5.52), ('N', 'THR', 'OD1', 'ASP', 5.01), ('N', 'THR', 'OD2', 'ASP', 6.61), ('N', 'THR', 'O', 'ASP', 4.02), ('N', 'THR', 'C', 'ASP', 3.14), ('N', 'THR', 'CA', 'ASP', 4.26), ('N', 'THR', 'N', 'ASP', 5.24)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_THRI, d, 'A_2jxr_3_4_23_25')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'A_2jxr_3_4_23_25')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_THR, d, 'A_2jxr_3_4_23_25')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(THR_ASP, d, 'A_2jxr_3_4_23_25')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_THRI' :  match1,
		'ASP_ASP' :  match2,
		'THR_THR' :  match3,
		'THR_ASP' :  match4}