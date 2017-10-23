'''
FUNC:A_1qk2_3_2_1_91
PDB:1qk2
EC:3.2.1.91
RESI:tyr,arg,asp,asp
LOCI:a-169,174,175,221;
'''
import motifFunctions as cmd
ASP_ARG = { 
	'distances':
		[[6.72, 6.51, 7.53, 7.38, 8.52, 9.64, 8.73], [6.21, 5.6, 6.37, 6.2, 7.31, 8.38, 7.61], [6.86, 5.92, 6.6, 6.64, 7.71, 8.62, 8.13], [5.63, 5.12, 5.6, 5.13, 6.18, 7.33, 6.41], [9.75, 8.6, 9.29, 9.78, 10.77, 11.36, 11.38], [9.69, 8.77, 9.66, 10.01, 11.09, 11.85, 11.58], [10.63, 9.81, 10.79, 11.18, 12.29, 13.06, 12.78], [8.94, 8.12, 9.02, 9.21, 10.29, 11.17, 10.69]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 6.72), ('CB', 'ASP', 'CG', 'ARG', 6.51), ('CB', 'ASP', 'CD', 'ARG', 7.53), ('CB', 'ASP', 'NE', 'ARG', 7.38), ('CB', 'ASP', 'CZ', 'ARG', 8.52), ('CB', 'ASP', 'NH1', 'ARG', 9.64), ('CB', 'ASP', 'NH2', 'ARG', 8.73)], [('CG', 'ASP', 'CB', 'ARG', 6.21), ('CG', 'ASP', 'CG', 'ARG', 5.6), ('CG', 'ASP', 'CD', 'ARG', 6.37), ('CG', 'ASP', 'NE', 'ARG', 6.2), ('CG', 'ASP', 'CZ', 'ARG', 7.31), ('CG', 'ASP', 'NH1', 'ARG', 8.38), ('CG', 'ASP', 'NH2', 'ARG', 7.61)], [('OD1', 'ASP', 'CB', 'ARG', 6.86), ('OD1', 'ASP', 'CG', 'ARG', 5.92), ('OD1', 'ASP', 'CD', 'ARG', 6.6), ('OD1', 'ASP', 'NE', 'ARG', 6.64), ('OD1', 'ASP', 'CZ', 'ARG', 7.71), ('OD1', 'ASP', 'NH1', 'ARG', 8.62), ('OD1', 'ASP', 'NH2', 'ARG', 8.13)], [('OD2', 'ASP', 'CB', 'ARG', 5.63), ('OD2', 'ASP', 'CG', 'ARG', 5.12), ('OD2', 'ASP', 'CD', 'ARG', 5.6), ('OD2', 'ASP', 'NE', 'ARG', 5.13), ('OD2', 'ASP', 'CZ', 'ARG', 6.18), ('OD2', 'ASP', 'NH1', 'ARG', 7.33), ('OD2', 'ASP', 'NH2', 'ARG', 6.41)], [('CB', 'ASP', 'CB', 'ARG', 9.75), ('CB', 'ASP', 'CG', 'ARG', 8.6), ('CB', 'ASP', 'CD', 'ARG', 9.29), ('CB', 'ASP', 'NE', 'ARG', 9.78), ('CB', 'ASP', 'CZ', 'ARG', 10.77), ('CB', 'ASP', 'NH1', 'ARG', 11.36), ('CB', 'ASP', 'NH2', 'ARG', 11.38)], [('CG', 'ASP', 'CB', 'ARG', 9.69), ('CG', 'ASP', 'CG', 'ARG', 8.77), ('CG', 'ASP', 'CD', 'ARG', 9.66), ('CG', 'ASP', 'NE', 'ARG', 10.01), ('CG', 'ASP', 'CZ', 'ARG', 11.09), ('CG', 'ASP', 'NH1', 'ARG', 11.85), ('CG', 'ASP', 'NH2', 'ARG', 11.58)], [('OD1', 'ASP', 'CB', 'ARG', 10.63), ('OD1', 'ASP', 'CG', 'ARG', 9.81), ('OD1', 'ASP', 'CD', 'ARG', 10.79), ('OD1', 'ASP', 'NE', 'ARG', 11.18), ('OD1', 'ASP', 'CZ', 'ARG', 12.29), ('OD1', 'ASP', 'NH1', 'ARG', 13.06), ('OD1', 'ASP', 'NH2', 'ARG', 12.78)], [('OD2', 'ASP', 'CB', 'ARG', 8.94), ('OD2', 'ASP', 'CG', 'ARG', 8.12), ('OD2', 'ASP', 'CD', 'ARG', 9.02), ('OD2', 'ASP', 'NE', 'ARG', 9.21), ('OD2', 'ASP', 'CZ', 'ARG', 10.29), ('OD2', 'ASP', 'NH1', 'ARG', 11.17), ('OD2', 'ASP', 'NH2', 'ARG', 10.69)]]}
ARG_TYR = { 
	'distances':
		[[9.36, 8.41, 7.87, 8.47, 7.39, 8.04, 7.48, 7.54], [8.11, 7.06, 6.41, 7.22, 5.9, 6.8, 6.12, 6.32], [7.02, 6.03, 5.77, 6.03, 5.51, 5.8, 5.53, 6.07], [7.61, 6.49, 6.47, 6.02, 6.0, 5.49, 5.49, 5.76], [7.46, 6.49, 6.86, 5.74, 6.6, 5.39, 5.89, 6.31], [6.64, 5.99, 6.65, 5.36, 6.78, 5.54, 6.27, 7.03], [8.44, 7.43, 7.87, 6.43, 7.46, 5.87, 6.48, 6.63]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 9.36), ('CB', 'ARG', 'CG', 'TYR', 8.41), ('CB', 'ARG', 'CD1', 'TYR', 7.87), ('CB', 'ARG', 'CD2', 'TYR', 8.47), ('CB', 'ARG', 'CE1', 'TYR', 7.39), ('CB', 'ARG', 'CE2', 'TYR', 8.04), ('CB', 'ARG', 'CZ', 'TYR', 7.48), ('CB', 'ARG', 'OH', 'TYR', 7.54)], [('CG', 'ARG', 'CB', 'TYR', 8.11), ('CG', 'ARG', 'CG', 'TYR', 7.06), ('CG', 'ARG', 'CD1', 'TYR', 6.41), ('CG', 'ARG', 'CD2', 'TYR', 7.22), ('CG', 'ARG', 'CE1', 'TYR', 5.9), ('CG', 'ARG', 'CE2', 'TYR', 6.8), ('CG', 'ARG', 'CZ', 'TYR', 6.12), ('CG', 'ARG', 'OH', 'TYR', 6.32)], [('CD', 'ARG', 'CB', 'TYR', 7.02), ('CD', 'ARG', 'CG', 'TYR', 6.03), ('CD', 'ARG', 'CD1', 'TYR', 5.77), ('CD', 'ARG', 'CD2', 'TYR', 6.03), ('CD', 'ARG', 'CE1', 'TYR', 5.51), ('CD', 'ARG', 'CE2', 'TYR', 5.8), ('CD', 'ARG', 'CZ', 'TYR', 5.53), ('CD', 'ARG', 'OH', 'TYR', 6.07)], [('NE', 'ARG', 'CB', 'TYR', 7.61), ('NE', 'ARG', 'CG', 'TYR', 6.49), ('NE', 'ARG', 'CD1', 'TYR', 6.47), ('NE', 'ARG', 'CD2', 'TYR', 6.02), ('NE', 'ARG', 'CE1', 'TYR', 6.0), ('NE', 'ARG', 'CE2', 'TYR', 5.49), ('NE', 'ARG', 'CZ', 'TYR', 5.49), ('NE', 'ARG', 'OH', 'TYR', 5.76)], [('CZ', 'ARG', 'CB', 'TYR', 7.46), ('CZ', 'ARG', 'CG', 'TYR', 6.49), ('CZ', 'ARG', 'CD1', 'TYR', 6.86), ('CZ', 'ARG', 'CD2', 'TYR', 5.74), ('CZ', 'ARG', 'CE1', 'TYR', 6.6), ('CZ', 'ARG', 'CE2', 'TYR', 5.39), ('CZ', 'ARG', 'CZ', 'TYR', 5.89), ('CZ', 'ARG', 'OH', 'TYR', 6.31)], [('NH1', 'ARG', 'CB', 'TYR', 6.64), ('NH1', 'ARG', 'CG', 'TYR', 5.99), ('NH1', 'ARG', 'CD1', 'TYR', 6.65), ('NH1', 'ARG', 'CD2', 'TYR', 5.36), ('NH1', 'ARG', 'CE1', 'TYR', 6.78), ('NH1', 'ARG', 'CE2', 'TYR', 5.54), ('NH1', 'ARG', 'CZ', 'TYR', 6.27), ('NH1', 'ARG', 'OH', 'TYR', 7.03)], [('NH2', 'ARG', 'CB', 'TYR', 8.44), ('NH2', 'ARG', 'CG', 'TYR', 7.43), ('NH2', 'ARG', 'CD1', 'TYR', 7.87), ('NH2', 'ARG', 'CD2', 'TYR', 6.43), ('NH2', 'ARG', 'CE1', 'TYR', 7.46), ('NH2', 'ARG', 'CE2', 'TYR', 5.87), ('NH2', 'ARG', 'CZ', 'TYR', 6.48), ('NH2', 'ARG', 'OH', 'TYR', 6.63)]]}
ASP_ASP = { 
	'distances':
		[[7.34, 6.5, 7.29, 5.34], [6.86, 6.44, 7.48, 5.36], [5.7, 5.51, 6.66, 4.59], [7.89, 7.63, 8.71, 6.58], [7.34, 6.86, 5.7, 7.89], [6.5, 6.44, 5.51, 7.63], [7.29, 7.48, 6.66, 8.71], [5.34, 5.36, 4.59, 6.58]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.34), ('CB', 'ASP', 'CG', 'ASP', 6.5), ('CB', 'ASP', 'OD1', 'ASP', 7.29), ('CB', 'ASP', 'OD2', 'ASP', 5.34)], [('CG', 'ASP', 'CB', 'ASP', 6.86), ('CG', 'ASP', 'CG', 'ASP', 6.44), ('CG', 'ASP', 'OD1', 'ASP', 7.48), ('CG', 'ASP', 'OD2', 'ASP', 5.36)], [('OD1', 'ASP', 'CB', 'ASP', 5.7), ('OD1', 'ASP', 'CG', 'ASP', 5.51), ('OD1', 'ASP', 'OD1', 'ASP', 6.66), ('OD1', 'ASP', 'OD2', 'ASP', 4.59)], [('OD2', 'ASP', 'CB', 'ASP', 7.89), ('OD2', 'ASP', 'CG', 'ASP', 7.63), ('OD2', 'ASP', 'OD1', 'ASP', 8.71), ('OD2', 'ASP', 'OD2', 'ASP', 6.58)], [('CB', 'ASP', 'CB', 'ASP', 7.34), ('CB', 'ASP', 'CG', 'ASP', 6.86), ('CB', 'ASP', 'OD1', 'ASP', 5.7), ('CB', 'ASP', 'OD2', 'ASP', 7.89)], [('CG', 'ASP', 'CB', 'ASP', 6.5), ('CG', 'ASP', 'CG', 'ASP', 6.44), ('CG', 'ASP', 'OD1', 'ASP', 5.51), ('CG', 'ASP', 'OD2', 'ASP', 7.63)], [('OD1', 'ASP', 'CB', 'ASP', 7.29), ('OD1', 'ASP', 'CG', 'ASP', 7.48), ('OD1', 'ASP', 'OD1', 'ASP', 6.66), ('OD1', 'ASP', 'OD2', 'ASP', 8.71)], [('OD2', 'ASP', 'CB', 'ASP', 5.34), ('OD2', 'ASP', 'CG', 'ASP', 5.36), ('OD2', 'ASP', 'OD1', 'ASP', 4.59), ('OD2', 'ASP', 'OD2', 'ASP', 6.58)]]}
ASP_TYR = { 
	'distances':
		[[11.43, 10.03, 9.13, 9.82, 7.88, 8.7, 7.63, 6.63], [9.99, 8.56, 7.71, 8.31, 6.44, 7.19, 6.11, 5.15], [9.46, 8.02, 7.04, 7.92, 5.71, 6.84, 5.58, 4.65], [9.55, 8.14, 7.52, 7.73, 6.35, 6.61, 5.79, 4.97], [10.33, 9.18, 7.91, 9.56, 6.93, 8.82, 7.49, 7.01], [11.45, 10.2, 8.95, 10.44, 7.82, 9.54, 8.18, 7.43], [12.59, 11.38, 10.11, 11.67, 9.03, 10.79, 9.43, 8.68], [11.34, 9.99, 8.83, 10.07, 7.57, 9.04, 7.71, 6.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 11.43), ('CB', 'ASP', 'CG', 'TYR', 10.03), ('CB', 'ASP', 'CD1', 'TYR', 9.13), ('CB', 'ASP', 'CD2', 'TYR', 9.82), ('CB', 'ASP', 'CE1', 'TYR', 7.88), ('CB', 'ASP', 'CE2', 'TYR', 8.7), ('CB', 'ASP', 'CZ', 'TYR', 7.63), ('CB', 'ASP', 'OH', 'TYR', 6.63)], [('CG', 'ASP', 'CB', 'TYR', 9.99), ('CG', 'ASP', 'CG', 'TYR', 8.56), ('CG', 'ASP', 'CD1', 'TYR', 7.71), ('CG', 'ASP', 'CD2', 'TYR', 8.31), ('CG', 'ASP', 'CE1', 'TYR', 6.44), ('CG', 'ASP', 'CE2', 'TYR', 7.19), ('CG', 'ASP', 'CZ', 'TYR', 6.11), ('CG', 'ASP', 'OH', 'TYR', 5.15)], [('OD1', 'ASP', 'CB', 'TYR', 9.46), ('OD1', 'ASP', 'CG', 'TYR', 8.02), ('OD1', 'ASP', 'CD1', 'TYR', 7.04), ('OD1', 'ASP', 'CD2', 'TYR', 7.92), ('OD1', 'ASP', 'CE1', 'TYR', 5.71), ('OD1', 'ASP', 'CE2', 'TYR', 6.84), ('OD1', 'ASP', 'CZ', 'TYR', 5.58), ('OD1', 'ASP', 'OH', 'TYR', 4.65)], [('OD2', 'ASP', 'CB', 'TYR', 9.55), ('OD2', 'ASP', 'CG', 'TYR', 8.14), ('OD2', 'ASP', 'CD1', 'TYR', 7.52), ('OD2', 'ASP', 'CD2', 'TYR', 7.73), ('OD2', 'ASP', 'CE1', 'TYR', 6.35), ('OD2', 'ASP', 'CE2', 'TYR', 6.61), ('OD2', 'ASP', 'CZ', 'TYR', 5.79), ('OD2', 'ASP', 'OH', 'TYR', 4.97)], [('CB', 'ASP', 'CB', 'TYR', 10.33), ('CB', 'ASP', 'CG', 'TYR', 9.18), ('CB', 'ASP', 'CD1', 'TYR', 7.91), ('CB', 'ASP', 'CD2', 'TYR', 9.56), ('CB', 'ASP', 'CE1', 'TYR', 6.93), ('CB', 'ASP', 'CE2', 'TYR', 8.82), ('CB', 'ASP', 'CZ', 'TYR', 7.49), ('CB', 'ASP', 'OH', 'TYR', 7.01)], [('CG', 'ASP', 'CB', 'TYR', 11.45), ('CG', 'ASP', 'CG', 'TYR', 10.2), ('CG', 'ASP', 'CD1', 'TYR', 8.95), ('CG', 'ASP', 'CD2', 'TYR', 10.44), ('CG', 'ASP', 'CE1', 'TYR', 7.82), ('CG', 'ASP', 'CE2', 'TYR', 9.54), ('CG', 'ASP', 'CZ', 'TYR', 8.18), ('CG', 'ASP', 'OH', 'TYR', 7.43)], [('OD1', 'ASP', 'CB', 'TYR', 12.59), ('OD1', 'ASP', 'CG', 'TYR', 11.38), ('OD1', 'ASP', 'CD1', 'TYR', 10.11), ('OD1', 'ASP', 'CD2', 'TYR', 11.67), ('OD1', 'ASP', 'CE1', 'TYR', 9.03), ('OD1', 'ASP', 'CE2', 'TYR', 10.79), ('OD1', 'ASP', 'CZ', 'TYR', 9.43), ('OD1', 'ASP', 'OH', 'TYR', 8.68)], [('OD2', 'ASP', 'CB', 'TYR', 11.34), ('OD2', 'ASP', 'CG', 'TYR', 9.99), ('OD2', 'ASP', 'CD1', 'TYR', 8.83), ('OD2', 'ASP', 'CD2', 'TYR', 10.07), ('OD2', 'ASP', 'CE1', 'TYR', 7.57), ('OD2', 'ASP', 'CE2', 'TYR', 9.04), ('OD2', 'ASP', 'CZ', 'TYR', 7.71), ('OD2', 'ASP', 'OH', 'TYR', 6.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ARG, d, 'A_1qk2_3_2_1_91')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_TYR, d, 'A_1qk2_3_2_1_91')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'A_1qk2_3_2_1_91')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_TYR, d, 'A_1qk2_3_2_1_91')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ARG' :  match1,
		'ARG_TYR' :  match2,
		'ASP_ASP' :  match3,
		'ASP_TYR' :  match4}