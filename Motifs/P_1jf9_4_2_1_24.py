'''
FUNC:P_1jf9_4_2_1_24
PDB:1jf9
EC:4.2.1.24
RESI:his,asp,lys
LOCI:a-124,200,226;
'''
import motifFunctions as cmd
HIS_LYS = { 
	'distances':
		[[13.68, 12.72, 11.26, 10.66, 9.26, 16.29, 16.09, 15.07, 15.38], [12.99, 11.9, 10.5, 9.74, 8.3, 15.69, 15.42, 14.3, 14.53], [13.35, 12.21, 10.85, 10.06, 8.58, 16.16, 15.79, 14.59, 14.67], [12.09, 10.92, 9.59, 8.68, 7.31, 14.74, 14.51, 13.35, 13.64], [12.77, 11.53, 10.27, 9.32, 7.88, 15.6, 15.19, 13.91, 13.93], [11.96, 10.69, 9.45, 8.41, 7.02, 14.71, 14.38, 13.11, 13.26], [16.48, 15.55, 14.07, 13.53, 12.07, 19.18, 18.88, 17.86, 18.01], [16.01, 14.99, 13.55, 12.88, 11.43, 18.69, 18.43, 17.36, 17.55], [15.17, 14.2, 12.75, 12.1, 10.71, 17.75, 17.58, 16.56, 16.88], [15.68, 14.83, 13.34, 12.84, 11.5, 18.15, 18.04, 17.13, 17.52]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 13.68), ('CB', 'HIS', 'CG', 'LYS', 12.72), ('CB', 'HIS', 'CD', 'LYS', 11.26), ('CB', 'HIS', 'CE', 'LYS', 10.66), ('CB', 'HIS', 'NZ', 'LYS', 9.26), ('CB', 'HIS', 'O', 'LYS', 16.29), ('CB', 'HIS', 'C', 'LYS', 16.09), ('CB', 'HIS', 'CA', 'LYS', 15.07), ('CB', 'HIS', 'N', 'LYS', 15.38)], [('CG', 'HIS', 'CB', 'LYS', 12.99), ('CG', 'HIS', 'CG', 'LYS', 11.9), ('CG', 'HIS', 'CD', 'LYS', 10.5), ('CG', 'HIS', 'CE', 'LYS', 9.74), ('CG', 'HIS', 'NZ', 'LYS', 8.3), ('CG', 'HIS', 'O', 'LYS', 15.69), ('CG', 'HIS', 'C', 'LYS', 15.42), ('CG', 'HIS', 'CA', 'LYS', 14.3), ('CG', 'HIS', 'N', 'LYS', 14.53)], [('ND1', 'HIS', 'CB', 'LYS', 13.35), ('ND1', 'HIS', 'CG', 'LYS', 12.21), ('ND1', 'HIS', 'CD', 'LYS', 10.85), ('ND1', 'HIS', 'CE', 'LYS', 10.06), ('ND1', 'HIS', 'NZ', 'LYS', 8.58), ('ND1', 'HIS', 'O', 'LYS', 16.16), ('ND1', 'HIS', 'C', 'LYS', 15.79), ('ND1', 'HIS', 'CA', 'LYS', 14.59), ('ND1', 'HIS', 'N', 'LYS', 14.67)], [('CD2', 'HIS', 'CB', 'LYS', 12.09), ('CD2', 'HIS', 'CG', 'LYS', 10.92), ('CD2', 'HIS', 'CD', 'LYS', 9.59), ('CD2', 'HIS', 'CE', 'LYS', 8.68), ('CD2', 'HIS', 'NZ', 'LYS', 7.31), ('CD2', 'HIS', 'O', 'LYS', 14.74), ('CD2', 'HIS', 'C', 'LYS', 14.51), ('CD2', 'HIS', 'CA', 'LYS', 13.35), ('CD2', 'HIS', 'N', 'LYS', 13.64)], [('CE1', 'HIS', 'CB', 'LYS', 12.77), ('CE1', 'HIS', 'CG', 'LYS', 11.53), ('CE1', 'HIS', 'CD', 'LYS', 10.27), ('CE1', 'HIS', 'CE', 'LYS', 9.32), ('CE1', 'HIS', 'NZ', 'LYS', 7.88), ('CE1', 'HIS', 'O', 'LYS', 15.6), ('CE1', 'HIS', 'C', 'LYS', 15.19), ('CE1', 'HIS', 'CA', 'LYS', 13.91), ('CE1', 'HIS', 'N', 'LYS', 13.93)], [('NE2', 'HIS', 'CB', 'LYS', 11.96), ('NE2', 'HIS', 'CG', 'LYS', 10.69), ('NE2', 'HIS', 'CD', 'LYS', 9.45), ('NE2', 'HIS', 'CE', 'LYS', 8.41), ('NE2', 'HIS', 'NZ', 'LYS', 7.02), ('NE2', 'HIS', 'O', 'LYS', 14.71), ('NE2', 'HIS', 'C', 'LYS', 14.38), ('NE2', 'HIS', 'CA', 'LYS', 13.11), ('NE2', 'HIS', 'N', 'LYS', 13.26)], [('O', 'HIS', 'CB', 'LYS', 16.48), ('O', 'HIS', 'CG', 'LYS', 15.55), ('O', 'HIS', 'CD', 'LYS', 14.07), ('O', 'HIS', 'CE', 'LYS', 13.53), ('O', 'HIS', 'NZ', 'LYS', 12.07), ('O', 'HIS', 'O', 'LYS', 19.18), ('O', 'HIS', 'C', 'LYS', 18.88), ('O', 'HIS', 'CA', 'LYS', 17.86), ('O', 'HIS', 'N', 'LYS', 18.01)], [('C', 'HIS', 'CB', 'LYS', 16.01), ('C', 'HIS', 'CG', 'LYS', 14.99), ('C', 'HIS', 'CD', 'LYS', 13.55), ('C', 'HIS', 'CE', 'LYS', 12.88), ('C', 'HIS', 'NZ', 'LYS', 11.43), ('C', 'HIS', 'O', 'LYS', 18.69), ('C', 'HIS', 'C', 'LYS', 18.43), ('C', 'HIS', 'CA', 'LYS', 17.36), ('C', 'HIS', 'N', 'LYS', 17.55)], [('CA', 'HIS', 'CB', 'LYS', 15.17), ('CA', 'HIS', 'CG', 'LYS', 14.2), ('CA', 'HIS', 'CD', 'LYS', 12.75), ('CA', 'HIS', 'CE', 'LYS', 12.1), ('CA', 'HIS', 'NZ', 'LYS', 10.71), ('CA', 'HIS', 'O', 'LYS', 17.75), ('CA', 'HIS', 'C', 'LYS', 17.58), ('CA', 'HIS', 'CA', 'LYS', 16.56), ('CA', 'HIS', 'N', 'LYS', 16.88)], [('N', 'HIS', 'CB', 'LYS', 15.68), ('N', 'HIS', 'CG', 'LYS', 14.83), ('N', 'HIS', 'CD', 'LYS', 13.34), ('N', 'HIS', 'CE', 'LYS', 12.84), ('N', 'HIS', 'NZ', 'LYS', 11.5), ('N', 'HIS', 'O', 'LYS', 18.15), ('N', 'HIS', 'C', 'LYS', 18.04), ('N', 'HIS', 'CA', 'LYS', 17.13), ('N', 'HIS', 'N', 'LYS', 17.52)]]}
HIS_ASP = { 
	'distances':
		[[8.6, 7.56, 8.14, 6.36, 10.15, 10.37, 10.02, 11.03], [9.44, 8.21, 8.56, 7.05, 10.95, 11.06, 10.76, 11.9], [9.88, 8.65, 8.99, 7.49, 11.67, 11.62, 11.18, 12.33], [10.19, 8.85, 8.99, 7.82, 11.35, 11.51, 11.41, 12.63], [10.81, 9.48, 9.63, 8.41, 12.44, 12.35, 12.01, 13.25], [10.96, 9.57, 9.61, 8.57, 12.25, 12.27, 12.12, 13.4], [9.15, 8.59, 9.54, 7.39, 11.42, 11.48, 10.65, 11.32], [9.74, 9.0, 9.82, 7.74, 11.78, 11.91, 11.24, 12.03], [9.37, 8.56, 9.31, 7.33, 11.04, 11.33, 10.86, 11.7], [8.75, 8.19, 9.09, 7.06, 10.34, 10.73, 10.26, 10.93]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 8.6), ('CB', 'HIS', 'CG', 'ASP', 7.56), ('CB', 'HIS', 'OD1', 'ASP', 8.14), ('CB', 'HIS', 'OD2', 'ASP', 6.36), ('CB', 'HIS', 'O', 'ASP', 10.15), ('CB', 'HIS', 'C', 'ASP', 10.37), ('CB', 'HIS', 'CA', 'ASP', 10.02), ('CB', 'HIS', 'N', 'ASP', 11.03)], [('CG', 'HIS', 'CB', 'ASP', 9.44), ('CG', 'HIS', 'CG', 'ASP', 8.21), ('CG', 'HIS', 'OD1', 'ASP', 8.56), ('CG', 'HIS', 'OD2', 'ASP', 7.05), ('CG', 'HIS', 'O', 'ASP', 10.95), ('CG', 'HIS', 'C', 'ASP', 11.06), ('CG', 'HIS', 'CA', 'ASP', 10.76), ('CG', 'HIS', 'N', 'ASP', 11.9)], [('ND1', 'HIS', 'CB', 'ASP', 9.88), ('ND1', 'HIS', 'CG', 'ASP', 8.65), ('ND1', 'HIS', 'OD1', 'ASP', 8.99), ('ND1', 'HIS', 'OD2', 'ASP', 7.49), ('ND1', 'HIS', 'O', 'ASP', 11.67), ('ND1', 'HIS', 'C', 'ASP', 11.62), ('ND1', 'HIS', 'CA', 'ASP', 11.18), ('ND1', 'HIS', 'N', 'ASP', 12.33)], [('CD2', 'HIS', 'CB', 'ASP', 10.19), ('CD2', 'HIS', 'CG', 'ASP', 8.85), ('CD2', 'HIS', 'OD1', 'ASP', 8.99), ('CD2', 'HIS', 'OD2', 'ASP', 7.82), ('CD2', 'HIS', 'O', 'ASP', 11.35), ('CD2', 'HIS', 'C', 'ASP', 11.51), ('CD2', 'HIS', 'CA', 'ASP', 11.41), ('CD2', 'HIS', 'N', 'ASP', 12.63)], [('CE1', 'HIS', 'CB', 'ASP', 10.81), ('CE1', 'HIS', 'CG', 'ASP', 9.48), ('CE1', 'HIS', 'OD1', 'ASP', 9.63), ('CE1', 'HIS', 'OD2', 'ASP', 8.41), ('CE1', 'HIS', 'O', 'ASP', 12.44), ('CE1', 'HIS', 'C', 'ASP', 12.35), ('CE1', 'HIS', 'CA', 'ASP', 12.01), ('CE1', 'HIS', 'N', 'ASP', 13.25)], [('NE2', 'HIS', 'CB', 'ASP', 10.96), ('NE2', 'HIS', 'CG', 'ASP', 9.57), ('NE2', 'HIS', 'OD1', 'ASP', 9.61), ('NE2', 'HIS', 'OD2', 'ASP', 8.57), ('NE2', 'HIS', 'O', 'ASP', 12.25), ('NE2', 'HIS', 'C', 'ASP', 12.27), ('NE2', 'HIS', 'CA', 'ASP', 12.12), ('NE2', 'HIS', 'N', 'ASP', 13.4)], [('O', 'HIS', 'CB', 'ASP', 9.15), ('O', 'HIS', 'CG', 'ASP', 8.59), ('O', 'HIS', 'OD1', 'ASP', 9.54), ('O', 'HIS', 'OD2', 'ASP', 7.39), ('O', 'HIS', 'O', 'ASP', 11.42), ('O', 'HIS', 'C', 'ASP', 11.48), ('O', 'HIS', 'CA', 'ASP', 10.65), ('O', 'HIS', 'N', 'ASP', 11.32)], [('C', 'HIS', 'CB', 'ASP', 9.74), ('C', 'HIS', 'CG', 'ASP', 9.0), ('C', 'HIS', 'OD1', 'ASP', 9.82), ('C', 'HIS', 'OD2', 'ASP', 7.74), ('C', 'HIS', 'O', 'ASP', 11.78), ('C', 'HIS', 'C', 'ASP', 11.91), ('C', 'HIS', 'CA', 'ASP', 11.24), ('C', 'HIS', 'N', 'ASP', 12.03)], [('CA', 'HIS', 'CB', 'ASP', 9.37), ('CA', 'HIS', 'CG', 'ASP', 8.56), ('CA', 'HIS', 'OD1', 'ASP', 9.31), ('CA', 'HIS', 'OD2', 'ASP', 7.33), ('CA', 'HIS', 'O', 'ASP', 11.04), ('CA', 'HIS', 'C', 'ASP', 11.33), ('CA', 'HIS', 'CA', 'ASP', 10.86), ('CA', 'HIS', 'N', 'ASP', 11.7)], [('N', 'HIS', 'CB', 'ASP', 8.75), ('N', 'HIS', 'CG', 'ASP', 8.19), ('N', 'HIS', 'OD1', 'ASP', 9.09), ('N', 'HIS', 'OD2', 'ASP', 7.06), ('N', 'HIS', 'O', 'ASP', 10.34), ('N', 'HIS', 'C', 'ASP', 10.73), ('N', 'HIS', 'CA', 'ASP', 10.26), ('N', 'HIS', 'N', 'ASP', 10.93)]]}
ASP_LYS = { 
	'distances':
		[[13.71, 13.51, 12.06, 12.49, 11.44, 15.91, 15.66, 15.17, 15.4], [12.5, 12.19, 10.72, 11.06, 9.96, 14.85, 14.57, 13.97, 14.18], [11.38, 11.15, 9.72, 10.21, 9.22, 13.7, 13.39, 12.83, 13.04], [12.76, 12.28, 10.76, 10.89, 9.66, 15.24, 14.95, 14.23, 14.44], [12.81, 12.91, 11.61, 12.31, 11.58, 14.54, 14.48, 14.27, 14.73], [12.68, 12.8, 11.5, 12.26, 11.51, 14.51, 14.33, 14.1, 14.43], [13.6, 13.59, 12.24, 12.87, 11.96, 15.63, 15.37, 15.02, 15.23], [14.95, 15.0, 13.66, 14.32, 13.42, 16.86, 16.63, 16.36, 16.59]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.71), ('CB', 'ASP', 'CG', 'LYS', 13.51), ('CB', 'ASP', 'CD', 'LYS', 12.06), ('CB', 'ASP', 'CE', 'LYS', 12.49), ('CB', 'ASP', 'NZ', 'LYS', 11.44), ('CB', 'ASP', 'O', 'LYS', 15.91), ('CB', 'ASP', 'C', 'LYS', 15.66), ('CB', 'ASP', 'CA', 'LYS', 15.17), ('CB', 'ASP', 'N', 'LYS', 15.4)], [('CG', 'ASP', 'CB', 'LYS', 12.5), ('CG', 'ASP', 'CG', 'LYS', 12.19), ('CG', 'ASP', 'CD', 'LYS', 10.72), ('CG', 'ASP', 'CE', 'LYS', 11.06), ('CG', 'ASP', 'NZ', 'LYS', 9.96), ('CG', 'ASP', 'O', 'LYS', 14.85), ('CG', 'ASP', 'C', 'LYS', 14.57), ('CG', 'ASP', 'CA', 'LYS', 13.97), ('CG', 'ASP', 'N', 'LYS', 14.18)], [('OD1', 'ASP', 'CB', 'LYS', 11.38), ('OD1', 'ASP', 'CG', 'LYS', 11.15), ('OD1', 'ASP', 'CD', 'LYS', 9.72), ('OD1', 'ASP', 'CE', 'LYS', 10.21), ('OD1', 'ASP', 'NZ', 'LYS', 9.22), ('OD1', 'ASP', 'O', 'LYS', 13.7), ('OD1', 'ASP', 'C', 'LYS', 13.39), ('OD1', 'ASP', 'CA', 'LYS', 12.83), ('OD1', 'ASP', 'N', 'LYS', 13.04)], [('OD2', 'ASP', 'CB', 'LYS', 12.76), ('OD2', 'ASP', 'CG', 'LYS', 12.28), ('OD2', 'ASP', 'CD', 'LYS', 10.76), ('OD2', 'ASP', 'CE', 'LYS', 10.89), ('OD2', 'ASP', 'NZ', 'LYS', 9.66), ('OD2', 'ASP', 'O', 'LYS', 15.24), ('OD2', 'ASP', 'C', 'LYS', 14.95), ('OD2', 'ASP', 'CA', 'LYS', 14.23), ('OD2', 'ASP', 'N', 'LYS', 14.44)], [('O', 'ASP', 'CB', 'LYS', 12.81), ('O', 'ASP', 'CG', 'LYS', 12.91), ('O', 'ASP', 'CD', 'LYS', 11.61), ('O', 'ASP', 'CE', 'LYS', 12.31), ('O', 'ASP', 'NZ', 'LYS', 11.58), ('O', 'ASP', 'O', 'LYS', 14.54), ('O', 'ASP', 'C', 'LYS', 14.48), ('O', 'ASP', 'CA', 'LYS', 14.27), ('O', 'ASP', 'N', 'LYS', 14.73)], [('C', 'ASP', 'CB', 'LYS', 12.68), ('C', 'ASP', 'CG', 'LYS', 12.8), ('C', 'ASP', 'CD', 'LYS', 11.5), ('C', 'ASP', 'CE', 'LYS', 12.26), ('C', 'ASP', 'NZ', 'LYS', 11.51), ('C', 'ASP', 'O', 'LYS', 14.51), ('C', 'ASP', 'C', 'LYS', 14.33), ('C', 'ASP', 'CA', 'LYS', 14.1), ('C', 'ASP', 'N', 'LYS', 14.43)], [('CA', 'ASP', 'CB', 'LYS', 13.6), ('CA', 'ASP', 'CG', 'LYS', 13.59), ('CA', 'ASP', 'CD', 'LYS', 12.24), ('CA', 'ASP', 'CE', 'LYS', 12.87), ('CA', 'ASP', 'NZ', 'LYS', 11.96), ('CA', 'ASP', 'O', 'LYS', 15.63), ('CA', 'ASP', 'C', 'LYS', 15.37), ('CA', 'ASP', 'CA', 'LYS', 15.02), ('CA', 'ASP', 'N', 'LYS', 15.23)], [('N', 'ASP', 'CB', 'LYS', 14.95), ('N', 'ASP', 'CG', 'LYS', 15.0), ('N', 'ASP', 'CD', 'LYS', 13.66), ('N', 'ASP', 'CE', 'LYS', 14.32), ('N', 'ASP', 'NZ', 'LYS', 13.42), ('N', 'ASP', 'O', 'LYS', 16.86), ('N', 'ASP', 'C', 'LYS', 16.63), ('N', 'ASP', 'CA', 'LYS', 16.36), ('N', 'ASP', 'N', 'LYS', 16.59)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_LYS, d, 'P_1jf9_4_2_1_24')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'P_1jf9_4_2_1_24')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_LYS, d, 'P_1jf9_4_2_1_24')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_LYS' :  match1,
		'HIS_ASP' :  match2,
		'ASP_LYS' :  match3}