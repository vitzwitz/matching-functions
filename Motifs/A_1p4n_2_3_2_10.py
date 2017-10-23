'''
FUNC:A_1p4n_2_3_2_10
PDB:1p4n
EC:2.3.2.10
RESI:lys,asp,arg,glu
LOCI:a-36,108,211,319;
'''
import motifFunctions as cmd
GLU_LYS = { 
	'distances':
		[[19.57, 18.74, 18.54, 17.56, 17.48], [18.73, 17.83, 17.53, 16.49, 16.32], [18.36, 17.51, 17.1, 16.1, 15.82], [19.25, 18.45, 18.01, 17.05, 16.72], [17.26, 16.39, 15.94, 14.93, 14.61]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 19.57), ('CB', 'GLU', 'CG', 'LYS', 18.74), ('CB', 'GLU', 'CD', 'LYS', 18.54), ('CB', 'GLU', 'CE', 'LYS', 17.56), ('CB', 'GLU', 'NZ', 'LYS', 17.48)], [('CG', 'GLU', 'CB', 'LYS', 18.73), ('CG', 'GLU', 'CG', 'LYS', 17.83), ('CG', 'GLU', 'CD', 'LYS', 17.53), ('CG', 'GLU', 'CE', 'LYS', 16.49), ('CG', 'GLU', 'NZ', 'LYS', 16.32)], [('CD', 'GLU', 'CB', 'LYS', 18.36), ('CD', 'GLU', 'CG', 'LYS', 17.51), ('CD', 'GLU', 'CD', 'LYS', 17.1), ('CD', 'GLU', 'CE', 'LYS', 16.1), ('CD', 'GLU', 'NZ', 'LYS', 15.82)], [('OE1', 'GLU', 'CB', 'LYS', 19.25), ('OE1', 'GLU', 'CG', 'LYS', 18.45), ('OE1', 'GLU', 'CD', 'LYS', 18.01), ('OE1', 'GLU', 'CE', 'LYS', 17.05), ('OE1', 'GLU', 'NZ', 'LYS', 16.72)], [('OE2', 'GLU', 'CB', 'LYS', 17.26), ('OE2', 'GLU', 'CG', 'LYS', 16.39), ('OE2', 'GLU', 'CD', 'LYS', 15.94), ('OE2', 'GLU', 'CE', 'LYS', 14.93), ('OE2', 'GLU', 'NZ', 'LYS', 14.61)]]}
ASP_ARG = { 
	'distances':
		[[21.89, 20.47, 19.47, 18.08, 17.43, 18.11, 16.18], [20.53, 19.13, 18.09, 16.72, 16.05, 16.69, 14.82], [19.56, 18.13, 17.15, 15.75, 15.07, 15.73, 13.81], [20.49, 19.13, 18.03, 16.7, 16.02, 16.62, 14.85]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 21.89), ('CB', 'ASP', 'CG', 'ARG', 20.47), ('CB', 'ASP', 'CD', 'ARG', 19.47), ('CB', 'ASP', 'NE', 'ARG', 18.08), ('CB', 'ASP', 'CZ', 'ARG', 17.43), ('CB', 'ASP', 'NH1', 'ARG', 18.11), ('CB', 'ASP', 'NH2', 'ARG', 16.18)], [('CG', 'ASP', 'CB', 'ARG', 20.53), ('CG', 'ASP', 'CG', 'ARG', 19.13), ('CG', 'ASP', 'CD', 'ARG', 18.09), ('CG', 'ASP', 'NE', 'ARG', 16.72), ('CG', 'ASP', 'CZ', 'ARG', 16.05), ('CG', 'ASP', 'NH1', 'ARG', 16.69), ('CG', 'ASP', 'NH2', 'ARG', 14.82)], [('OD1', 'ASP', 'CB', 'ARG', 19.56), ('OD1', 'ASP', 'CG', 'ARG', 18.13), ('OD1', 'ASP', 'CD', 'ARG', 17.15), ('OD1', 'ASP', 'NE', 'ARG', 15.75), ('OD1', 'ASP', 'CZ', 'ARG', 15.07), ('OD1', 'ASP', 'NH1', 'ARG', 15.73), ('OD1', 'ASP', 'NH2', 'ARG', 13.81)], [('OD2', 'ASP', 'CB', 'ARG', 20.49), ('OD2', 'ASP', 'CG', 'ARG', 19.13), ('OD2', 'ASP', 'CD', 'ARG', 18.03), ('OD2', 'ASP', 'NE', 'ARG', 16.7), ('OD2', 'ASP', 'CZ', 'ARG', 16.02), ('OD2', 'ASP', 'NH1', 'ARG', 16.62), ('OD2', 'ASP', 'NH2', 'ARG', 14.85)]]}
GLU_ARG = { 
	'distances':
		[[24.04, 22.55, 21.81, 20.36, 19.53, 20.07, 18.23], [22.68, 21.18, 20.46, 19.01, 18.21, 18.8, 16.9], [21.98, 20.47, 19.84, 18.38, 17.54, 18.08, 16.23], [22.72, 21.2, 20.64, 19.19, 18.32, 18.83, 17.02], [20.74, 19.23, 18.6, 17.15, 16.29, 16.83, 14.98]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 24.04), ('CB', 'GLU', 'CG', 'ARG', 22.55), ('CB', 'GLU', 'CD', 'ARG', 21.81), ('CB', 'GLU', 'NE', 'ARG', 20.36), ('CB', 'GLU', 'CZ', 'ARG', 19.53), ('CB', 'GLU', 'NH1', 'ARG', 20.07), ('CB', 'GLU', 'NH2', 'ARG', 18.23)], [('CG', 'GLU', 'CB', 'ARG', 22.68), ('CG', 'GLU', 'CG', 'ARG', 21.18), ('CG', 'GLU', 'CD', 'ARG', 20.46), ('CG', 'GLU', 'NE', 'ARG', 19.01), ('CG', 'GLU', 'CZ', 'ARG', 18.21), ('CG', 'GLU', 'NH1', 'ARG', 18.8), ('CG', 'GLU', 'NH2', 'ARG', 16.9)], [('CD', 'GLU', 'CB', 'ARG', 21.98), ('CD', 'GLU', 'CG', 'ARG', 20.47), ('CD', 'GLU', 'CD', 'ARG', 19.84), ('CD', 'GLU', 'NE', 'ARG', 18.38), ('CD', 'GLU', 'CZ', 'ARG', 17.54), ('CD', 'GLU', 'NH1', 'ARG', 18.08), ('CD', 'GLU', 'NH2', 'ARG', 16.23)], [('OE1', 'GLU', 'CB', 'ARG', 22.72), ('OE1', 'GLU', 'CG', 'ARG', 21.2), ('OE1', 'GLU', 'CD', 'ARG', 20.64), ('OE1', 'GLU', 'NE', 'ARG', 19.19), ('OE1', 'GLU', 'CZ', 'ARG', 18.32), ('OE1', 'GLU', 'NH1', 'ARG', 18.83), ('OE1', 'GLU', 'NH2', 'ARG', 17.02)], [('OE2', 'GLU', 'CB', 'ARG', 20.74), ('OE2', 'GLU', 'CG', 'ARG', 19.23), ('OE2', 'GLU', 'CD', 'ARG', 18.6), ('OE2', 'GLU', 'NE', 'ARG', 17.15), ('OE2', 'GLU', 'CZ', 'ARG', 16.29), ('OE2', 'GLU', 'NH1', 'ARG', 16.83), ('OE2', 'GLU', 'NH2', 'ARG', 14.98)]]}
ASP_GLU = { 
	'distances':
		[[6.86, 6.33, 7.46, 8.61, 7.44], [7.7, 6.96, 7.77, 9.0, 7.42], [7.74, 6.73, 7.26, 8.51, 6.69], [8.62, 8.04, 8.83, 10.03, 8.45]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 6.86), ('CB', 'ASP', 'CG', 'GLU', 6.33), ('CB', 'ASP', 'CD', 'GLU', 7.46), ('CB', 'ASP', 'OE1', 'GLU', 8.61), ('CB', 'ASP', 'OE2', 'GLU', 7.44)], [('CG', 'ASP', 'CB', 'GLU', 7.7), ('CG', 'ASP', 'CG', 'GLU', 6.96), ('CG', 'ASP', 'CD', 'GLU', 7.77), ('CG', 'ASP', 'OE1', 'GLU', 9.0), ('CG', 'ASP', 'OE2', 'GLU', 7.42)], [('OD1', 'ASP', 'CB', 'GLU', 7.74), ('OD1', 'ASP', 'CG', 'GLU', 6.73), ('OD1', 'ASP', 'CD', 'GLU', 7.26), ('OD1', 'ASP', 'OE1', 'GLU', 8.51), ('OD1', 'ASP', 'OE2', 'GLU', 6.69)], [('OD2', 'ASP', 'CB', 'GLU', 8.62), ('OD2', 'ASP', 'CG', 'GLU', 8.04), ('OD2', 'ASP', 'CD', 'GLU', 8.83), ('OD2', 'ASP', 'OE1', 'GLU', 10.03), ('OD2', 'ASP', 'OE2', 'GLU', 8.45)]]}
ASP_LYS = { 
	'distances':
		[[17.1, 16.06, 16.03, 14.9, 15.06], [15.58, 14.53, 14.51, 13.38, 13.57], [15.13, 14.05, 13.88, 12.71, 12.77], [14.94, 13.91, 14.02, 12.95, 13.3]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 17.1), ('CB', 'ASP', 'CG', 'LYS', 16.06), ('CB', 'ASP', 'CD', 'LYS', 16.03), ('CB', 'ASP', 'CE', 'LYS', 14.9), ('CB', 'ASP', 'NZ', 'LYS', 15.06)], [('CG', 'ASP', 'CB', 'LYS', 15.58), ('CG', 'ASP', 'CG', 'LYS', 14.53), ('CG', 'ASP', 'CD', 'LYS', 14.51), ('CG', 'ASP', 'CE', 'LYS', 13.38), ('CG', 'ASP', 'NZ', 'LYS', 13.57)], [('OD1', 'ASP', 'CB', 'LYS', 15.13), ('OD1', 'ASP', 'CG', 'LYS', 14.05), ('OD1', 'ASP', 'CD', 'LYS', 13.88), ('OD1', 'ASP', 'CE', 'LYS', 12.71), ('OD1', 'ASP', 'NZ', 'LYS', 12.77)], [('OD2', 'ASP', 'CB', 'LYS', 14.94), ('OD2', 'ASP', 'CG', 'LYS', 13.91), ('OD2', 'ASP', 'CD', 'LYS', 14.02), ('OD2', 'ASP', 'CE', 'LYS', 12.95), ('OD2', 'ASP', 'NZ', 'LYS', 13.3)]]}
LYS_ARG = { 
	'distances':
		[[13.0, 12.35, 11.33, 10.95, 10.12, 9.51, 10.14], [12.41, 11.65, 10.51, 9.99, 9.21, 8.83, 9.13], [11.15, 10.29, 9.21, 8.63, 7.77, 7.36, 7.69], [11.01, 10.01, 8.82, 8.0, 7.19, 7.12, 6.86], [9.99, 8.85, 7.75, 6.79, 5.85, 5.87, 5.42]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 13.0), ('CB', 'LYS', 'CG', 'ARG', 12.35), ('CB', 'LYS', 'CD', 'ARG', 11.33), ('CB', 'LYS', 'NE', 'ARG', 10.95), ('CB', 'LYS', 'CZ', 'ARG', 10.12), ('CB', 'LYS', 'NH1', 'ARG', 9.51), ('CB', 'LYS', 'NH2', 'ARG', 10.14)], [('CG', 'LYS', 'CB', 'ARG', 12.41), ('CG', 'LYS', 'CG', 'ARG', 11.65), ('CG', 'LYS', 'CD', 'ARG', 10.51), ('CG', 'LYS', 'NE', 'ARG', 9.99), ('CG', 'LYS', 'CZ', 'ARG', 9.21), ('CG', 'LYS', 'NH1', 'ARG', 8.83), ('CG', 'LYS', 'NH2', 'ARG', 9.13)], [('CD', 'LYS', 'CB', 'ARG', 11.15), ('CD', 'LYS', 'CG', 'ARG', 10.29), ('CD', 'LYS', 'CD', 'ARG', 9.21), ('CD', 'LYS', 'NE', 'ARG', 8.63), ('CD', 'LYS', 'CZ', 'ARG', 7.77), ('CD', 'LYS', 'NH1', 'ARG', 7.36), ('CD', 'LYS', 'NH2', 'ARG', 7.69)], [('CE', 'LYS', 'CB', 'ARG', 11.01), ('CE', 'LYS', 'CG', 'ARG', 10.01), ('CE', 'LYS', 'CD', 'ARG', 8.82), ('CE', 'LYS', 'NE', 'ARG', 8.0), ('CE', 'LYS', 'CZ', 'ARG', 7.19), ('CE', 'LYS', 'NH1', 'ARG', 7.12), ('CE', 'LYS', 'NH2', 'ARG', 6.86)], [('NZ', 'LYS', 'CB', 'ARG', 9.99), ('NZ', 'LYS', 'CG', 'ARG', 8.85), ('NZ', 'LYS', 'CD', 'ARG', 7.75), ('NZ', 'LYS', 'NE', 'ARG', 6.79), ('NZ', 'LYS', 'CZ', 'ARG', 5.85), ('NZ', 'LYS', 'NH1', 'ARG', 5.87), ('NZ', 'LYS', 'NH2', 'ARG', 5.42)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_LYS, d, 'A_1p4n_2_3_2_10')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ARG, d, 'A_1p4n_2_3_2_10')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ARG, d, 'A_1p4n_2_3_2_10')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_GLU, d, 'A_1p4n_2_3_2_10')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_LYS, d, 'A_1p4n_2_3_2_10')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_ARG, d, 'A_1p4n_2_3_2_10')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_LYS' :  match1,
		'ASP_ARG' :  match2,
		'GLU_ARG' :  match3,
		'ASP_GLU' :  match4,
		'ASP_LYS' :  match5,
		'LYS_ARG' :  match6}