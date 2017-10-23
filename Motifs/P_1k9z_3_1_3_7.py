'''
FUNC:P_1k9z_3_1_3_7
PDB:1k9z
EC:3.1.3.7
RESI:asp,thr,asp
LOCI:a-49,147,294;
'''
import motifFunctions as cmd
ASP_ASP = { 
	'distances':
		[[15.52, 14.35, 13.21, 14.59, 16.82, 16.51, 15.27, 15.1], [15.01, 13.8, 12.67, 14.01, 16.31, 16.1, 14.87, 14.85], [15.94, 14.72, 13.6, 14.89, 17.2, 17.06, 15.85, 15.91], [13.82, 12.62, 11.49, 12.83, 15.14, 14.95, 13.72, 13.76], [16.56, 15.59, 14.43, 16.03, 17.56, 17.12, 15.99, 15.61], [16.9, 15.86, 14.7, 16.23, 17.99, 17.61, 16.44, 16.13], [16.26, 15.18, 14.0, 15.55, 17.31, 17.02, 15.87, 15.7], [17.41, 16.33, 15.14, 16.68, 18.4, 18.19, 17.06, 16.97], [15.52, 15.01, 15.94, 13.82, 16.56, 16.9, 16.26, 17.41], [14.35, 13.8, 14.72, 12.62, 15.59, 15.86, 15.18, 16.33], [13.21, 12.67, 13.6, 11.49, 14.43, 14.7, 14.0, 15.14], [14.59, 14.01, 14.89, 12.83, 16.03, 16.23, 15.55, 16.68], [16.82, 16.31, 17.2, 15.14, 17.56, 17.99, 17.31, 18.4], [16.51, 16.1, 17.06, 14.95, 17.12, 17.61, 17.02, 18.19], [15.27, 14.87, 15.85, 13.72, 15.99, 16.44, 15.87, 17.06], [15.1, 14.85, 15.91, 13.76, 15.61, 16.13, 15.7, 16.97]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 15.52), ('CB', 'ASP', 'CG', 'ASP', 14.35), ('CB', 'ASP', 'OD1', 'ASP', 13.21), ('CB', 'ASP', 'OD2', 'ASP', 14.59), ('CB', 'ASP', 'O', 'ASP', 16.82), ('CB', 'ASP', 'C', 'ASP', 16.51), ('CB', 'ASP', 'CA', 'ASP', 15.27), ('CB', 'ASP', 'N', 'ASP', 15.1)], [('CG', 'ASP', 'CB', 'ASP', 15.01), ('CG', 'ASP', 'CG', 'ASP', 13.8), ('CG', 'ASP', 'OD1', 'ASP', 12.67), ('CG', 'ASP', 'OD2', 'ASP', 14.01), ('CG', 'ASP', 'O', 'ASP', 16.31), ('CG', 'ASP', 'C', 'ASP', 16.1), ('CG', 'ASP', 'CA', 'ASP', 14.87), ('CG', 'ASP', 'N', 'ASP', 14.85)], [('OD1', 'ASP', 'CB', 'ASP', 15.94), ('OD1', 'ASP', 'CG', 'ASP', 14.72), ('OD1', 'ASP', 'OD1', 'ASP', 13.6), ('OD1', 'ASP', 'OD2', 'ASP', 14.89), ('OD1', 'ASP', 'O', 'ASP', 17.2), ('OD1', 'ASP', 'C', 'ASP', 17.06), ('OD1', 'ASP', 'CA', 'ASP', 15.85), ('OD1', 'ASP', 'N', 'ASP', 15.91)], [('OD2', 'ASP', 'CB', 'ASP', 13.82), ('OD2', 'ASP', 'CG', 'ASP', 12.62), ('OD2', 'ASP', 'OD1', 'ASP', 11.49), ('OD2', 'ASP', 'OD2', 'ASP', 12.83), ('OD2', 'ASP', 'O', 'ASP', 15.14), ('OD2', 'ASP', 'C', 'ASP', 14.95), ('OD2', 'ASP', 'CA', 'ASP', 13.72), ('OD2', 'ASP', 'N', 'ASP', 13.76)], [('O', 'ASP', 'CB', 'ASP', 16.56), ('O', 'ASP', 'CG', 'ASP', 15.59), ('O', 'ASP', 'OD1', 'ASP', 14.43), ('O', 'ASP', 'OD2', 'ASP', 16.03), ('O', 'ASP', 'O', 'ASP', 17.56), ('O', 'ASP', 'C', 'ASP', 17.12), ('O', 'ASP', 'CA', 'ASP', 15.99), ('O', 'ASP', 'N', 'ASP', 15.61)], [('C', 'ASP', 'CB', 'ASP', 16.9), ('C', 'ASP', 'CG', 'ASP', 15.86), ('C', 'ASP', 'OD1', 'ASP', 14.7), ('C', 'ASP', 'OD2', 'ASP', 16.23), ('C', 'ASP', 'O', 'ASP', 17.99), ('C', 'ASP', 'C', 'ASP', 17.61), ('C', 'ASP', 'CA', 'ASP', 16.44), ('C', 'ASP', 'N', 'ASP', 16.13)], [('CA', 'ASP', 'CB', 'ASP', 16.26), ('CA', 'ASP', 'CG', 'ASP', 15.18), ('CA', 'ASP', 'OD1', 'ASP', 14.0), ('CA', 'ASP', 'OD2', 'ASP', 15.55), ('CA', 'ASP', 'O', 'ASP', 17.31), ('CA', 'ASP', 'C', 'ASP', 17.02), ('CA', 'ASP', 'CA', 'ASP', 15.87), ('CA', 'ASP', 'N', 'ASP', 15.7)], [('N', 'ASP', 'CB', 'ASP', 17.41), ('N', 'ASP', 'CG', 'ASP', 16.33), ('N', 'ASP', 'OD1', 'ASP', 15.14), ('N', 'ASP', 'OD2', 'ASP', 16.68), ('N', 'ASP', 'O', 'ASP', 18.4), ('N', 'ASP', 'C', 'ASP', 18.19), ('N', 'ASP', 'CA', 'ASP', 17.06), ('N', 'ASP', 'N', 'ASP', 16.97)], [('CB', 'ASP', 'CB', 'ASP', 15.52), ('CB', 'ASP', 'CG', 'ASP', 15.01), ('CB', 'ASP', 'OD1', 'ASP', 15.94), ('CB', 'ASP', 'OD2', 'ASP', 13.82), ('CB', 'ASP', 'O', 'ASP', 16.56), ('CB', 'ASP', 'C', 'ASP', 16.9), ('CB', 'ASP', 'CA', 'ASP', 16.26), ('CB', 'ASP', 'N', 'ASP', 17.41)], [('CG', 'ASP', 'CB', 'ASP', 14.35), ('CG', 'ASP', 'CG', 'ASP', 13.8), ('CG', 'ASP', 'OD1', 'ASP', 14.72), ('CG', 'ASP', 'OD2', 'ASP', 12.62), ('CG', 'ASP', 'O', 'ASP', 15.59), ('CG', 'ASP', 'C', 'ASP', 15.86), ('CG', 'ASP', 'CA', 'ASP', 15.18), ('CG', 'ASP', 'N', 'ASP', 16.33)], [('OD1', 'ASP', 'CB', 'ASP', 13.21), ('OD1', 'ASP', 'CG', 'ASP', 12.67), ('OD1', 'ASP', 'OD1', 'ASP', 13.6), ('OD1', 'ASP', 'OD2', 'ASP', 11.49), ('OD1', 'ASP', 'O', 'ASP', 14.43), ('OD1', 'ASP', 'C', 'ASP', 14.7), ('OD1', 'ASP', 'CA', 'ASP', 14.0), ('OD1', 'ASP', 'N', 'ASP', 15.14)], [('OD2', 'ASP', 'CB', 'ASP', 14.59), ('OD2', 'ASP', 'CG', 'ASP', 14.01), ('OD2', 'ASP', 'OD1', 'ASP', 14.89), ('OD2', 'ASP', 'OD2', 'ASP', 12.83), ('OD2', 'ASP', 'O', 'ASP', 16.03), ('OD2', 'ASP', 'C', 'ASP', 16.23), ('OD2', 'ASP', 'CA', 'ASP', 15.55), ('OD2', 'ASP', 'N', 'ASP', 16.68)], [('O', 'ASP', 'CB', 'ASP', 16.82), ('O', 'ASP', 'CG', 'ASP', 16.31), ('O', 'ASP', 'OD1', 'ASP', 17.2), ('O', 'ASP', 'OD2', 'ASP', 15.14), ('O', 'ASP', 'O', 'ASP', 17.56), ('O', 'ASP', 'C', 'ASP', 17.99), ('O', 'ASP', 'CA', 'ASP', 17.31), ('O', 'ASP', 'N', 'ASP', 18.4)], [('C', 'ASP', 'CB', 'ASP', 16.51), ('C', 'ASP', 'CG', 'ASP', 16.1), ('C', 'ASP', 'OD1', 'ASP', 17.06), ('C', 'ASP', 'OD2', 'ASP', 14.95), ('C', 'ASP', 'O', 'ASP', 17.12), ('C', 'ASP', 'C', 'ASP', 17.61), ('C', 'ASP', 'CA', 'ASP', 17.02), ('C', 'ASP', 'N', 'ASP', 18.19)], [('CA', 'ASP', 'CB', 'ASP', 15.27), ('CA', 'ASP', 'CG', 'ASP', 14.87), ('CA', 'ASP', 'OD1', 'ASP', 15.85), ('CA', 'ASP', 'OD2', 'ASP', 13.72), ('CA', 'ASP', 'O', 'ASP', 15.99), ('CA', 'ASP', 'C', 'ASP', 16.44), ('CA', 'ASP', 'CA', 'ASP', 15.87), ('CA', 'ASP', 'N', 'ASP', 17.06)], [('N', 'ASP', 'CB', 'ASP', 15.1), ('N', 'ASP', 'CG', 'ASP', 14.85), ('N', 'ASP', 'OD1', 'ASP', 15.91), ('N', 'ASP', 'OD2', 'ASP', 13.76), ('N', 'ASP', 'O', 'ASP', 15.61), ('N', 'ASP', 'C', 'ASP', 16.13), ('N', 'ASP', 'CA', 'ASP', 15.7), ('N', 'ASP', 'N', 'ASP', 16.97)]]}
ASP_THR = { 
	'distances':
		[[8.08, 7.11, 7.58, 10.31, 10.16, 8.98, 9.59], [6.62, 5.76, 6.11, 8.81, 8.65, 7.5, 8.21], [6.52, 6.02, 5.64, 8.21, 8.26, 7.32, 8.28], [5.81, 4.71, 5.69, 8.34, 7.99, 6.7, 7.21], [11.1, 9.96, 10.76, 13.22, 13.07, 11.78, 12.17], [10.44, 9.42, 9.94, 12.44, 12.37, 11.17, 11.72], [9.04, 8.09, 8.54, 10.92, 10.88, 9.69, 10.29], [9.25, 8.54, 8.51, 10.65, 10.81, 9.8, 10.59], [13.35, 12.58, 14.78, 15.55, 14.36, 13.41, 12.08], [12.09, 11.33, 13.49, 14.42, 13.23, 12.27, 11.01], [11.15, 10.31, 12.54, 13.55, 12.38, 11.33, 10.09], [12.11, 11.44, 13.48, 14.48, 13.27, 12.4, 11.2], [14.71, 13.95, 16.18, 16.51, 15.39, 14.45, 13.03], [14.79, 13.93, 16.21, 16.81, 15.68, 14.66, 13.29], [13.64, 12.74, 15.04, 15.86, 14.71, 13.65, 12.33], [14.08, 13.06, 15.4, 16.52, 15.39, 14.24, 13.0]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 8.08), ('CB', 'ASP', 'OG1', 'THR', 7.11), ('CB', 'ASP', 'CG2', 'THR', 7.58), ('CB', 'ASP', 'O', 'THR', 10.31), ('CB', 'ASP', 'C', 'THR', 10.16), ('CB', 'ASP', 'CA', 'THR', 8.98), ('CB', 'ASP', 'N', 'THR', 9.59)], [('CG', 'ASP', 'CB', 'THR', 6.62), ('CG', 'ASP', 'OG1', 'THR', 5.76), ('CG', 'ASP', 'CG2', 'THR', 6.11), ('CG', 'ASP', 'O', 'THR', 8.81), ('CG', 'ASP', 'C', 'THR', 8.65), ('CG', 'ASP', 'CA', 'THR', 7.5), ('CG', 'ASP', 'N', 'THR', 8.21)], [('OD1', 'ASP', 'CB', 'THR', 6.52), ('OD1', 'ASP', 'OG1', 'THR', 6.02), ('OD1', 'ASP', 'CG2', 'THR', 5.64), ('OD1', 'ASP', 'O', 'THR', 8.21), ('OD1', 'ASP', 'C', 'THR', 8.26), ('OD1', 'ASP', 'CA', 'THR', 7.32), ('OD1', 'ASP', 'N', 'THR', 8.28)], [('OD2', 'ASP', 'CB', 'THR', 5.81), ('OD2', 'ASP', 'OG1', 'THR', 4.71), ('OD2', 'ASP', 'CG2', 'THR', 5.69), ('OD2', 'ASP', 'O', 'THR', 8.34), ('OD2', 'ASP', 'C', 'THR', 7.99), ('OD2', 'ASP', 'CA', 'THR', 6.7), ('OD2', 'ASP', 'N', 'THR', 7.21)], [('O', 'ASP', 'CB', 'THR', 11.1), ('O', 'ASP', 'OG1', 'THR', 9.96), ('O', 'ASP', 'CG2', 'THR', 10.76), ('O', 'ASP', 'O', 'THR', 13.22), ('O', 'ASP', 'C', 'THR', 13.07), ('O', 'ASP', 'CA', 'THR', 11.78), ('O', 'ASP', 'N', 'THR', 12.17)], [('C', 'ASP', 'CB', 'THR', 10.44), ('C', 'ASP', 'OG1', 'THR', 9.42), ('C', 'ASP', 'CG2', 'THR', 9.94), ('C', 'ASP', 'O', 'THR', 12.44), ('C', 'ASP', 'C', 'THR', 12.37), ('C', 'ASP', 'CA', 'THR', 11.17), ('C', 'ASP', 'N', 'THR', 11.72)], [('CA', 'ASP', 'CB', 'THR', 9.04), ('CA', 'ASP', 'OG1', 'THR', 8.09), ('CA', 'ASP', 'CG2', 'THR', 8.54), ('CA', 'ASP', 'O', 'THR', 10.92), ('CA', 'ASP', 'C', 'THR', 10.88), ('CA', 'ASP', 'CA', 'THR', 9.69), ('CA', 'ASP', 'N', 'THR', 10.29)], [('N', 'ASP', 'CB', 'THR', 9.25), ('N', 'ASP', 'OG1', 'THR', 8.54), ('N', 'ASP', 'CG2', 'THR', 8.51), ('N', 'ASP', 'O', 'THR', 10.65), ('N', 'ASP', 'C', 'THR', 10.81), ('N', 'ASP', 'CA', 'THR', 9.8), ('N', 'ASP', 'N', 'THR', 10.59)], [('CB', 'ASP', 'CB', 'THR', 13.35), ('CB', 'ASP', 'OG1', 'THR', 12.58), ('CB', 'ASP', 'CG2', 'THR', 14.78), ('CB', 'ASP', 'O', 'THR', 15.55), ('CB', 'ASP', 'C', 'THR', 14.36), ('CB', 'ASP', 'CA', 'THR', 13.41), ('CB', 'ASP', 'N', 'THR', 12.08)], [('CG', 'ASP', 'CB', 'THR', 12.09), ('CG', 'ASP', 'OG1', 'THR', 11.33), ('CG', 'ASP', 'CG2', 'THR', 13.49), ('CG', 'ASP', 'O', 'THR', 14.42), ('CG', 'ASP', 'C', 'THR', 13.23), ('CG', 'ASP', 'CA', 'THR', 12.27), ('CG', 'ASP', 'N', 'THR', 11.01)], [('OD1', 'ASP', 'CB', 'THR', 11.15), ('OD1', 'ASP', 'OG1', 'THR', 10.31), ('OD1', 'ASP', 'CG2', 'THR', 12.54), ('OD1', 'ASP', 'O', 'THR', 13.55), ('OD1', 'ASP', 'C', 'THR', 12.38), ('OD1', 'ASP', 'CA', 'THR', 11.33), ('OD1', 'ASP', 'N', 'THR', 10.09)], [('OD2', 'ASP', 'CB', 'THR', 12.11), ('OD2', 'ASP', 'OG1', 'THR', 11.44), ('OD2', 'ASP', 'CG2', 'THR', 13.48), ('OD2', 'ASP', 'O', 'THR', 14.48), ('OD2', 'ASP', 'C', 'THR', 13.27), ('OD2', 'ASP', 'CA', 'THR', 12.4), ('OD2', 'ASP', 'N', 'THR', 11.2)], [('O', 'ASP', 'CB', 'THR', 14.71), ('O', 'ASP', 'OG1', 'THR', 13.95), ('O', 'ASP', 'CG2', 'THR', 16.18), ('O', 'ASP', 'O', 'THR', 16.51), ('O', 'ASP', 'C', 'THR', 15.39), ('O', 'ASP', 'CA', 'THR', 14.45), ('O', 'ASP', 'N', 'THR', 13.03)], [('C', 'ASP', 'CB', 'THR', 14.79), ('C', 'ASP', 'OG1', 'THR', 13.93), ('C', 'ASP', 'CG2', 'THR', 16.21), ('C', 'ASP', 'O', 'THR', 16.81), ('C', 'ASP', 'C', 'THR', 15.68), ('C', 'ASP', 'CA', 'THR', 14.66), ('C', 'ASP', 'N', 'THR', 13.29)], [('CA', 'ASP', 'CB', 'THR', 13.64), ('CA', 'ASP', 'OG1', 'THR', 12.74), ('CA', 'ASP', 'CG2', 'THR', 15.04), ('CA', 'ASP', 'O', 'THR', 15.86), ('CA', 'ASP', 'C', 'THR', 14.71), ('CA', 'ASP', 'CA', 'THR', 13.65), ('CA', 'ASP', 'N', 'THR', 12.33)], [('N', 'ASP', 'CB', 'THR', 14.08), ('N', 'ASP', 'OG1', 'THR', 13.06), ('N', 'ASP', 'CG2', 'THR', 15.4), ('N', 'ASP', 'O', 'THR', 16.52), ('N', 'ASP', 'C', 'THR', 15.39), ('N', 'ASP', 'CA', 'THR', 14.24), ('N', 'ASP', 'N', 'THR', 13.0)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ASP, d, 'P_1k9z_3_1_3_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_THR, d, 'P_1k9z_3_1_3_7')
	if match2 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ASP' :  match1,
		'ASP_THR' :  match2}