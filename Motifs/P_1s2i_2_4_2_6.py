'''
FUNC:P_1s2i_2_4_2_6
PDB:1s2i
EC:2.4.2.6
RESI:tyr,asp,asp,glu
LOCI:a-11,75,95,101;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[10.52, 11.04, 11.06, 11.67], [9.12, 9.61, 9.7, 10.19], [8.09, 8.59, 8.57, 9.32], [9.05, 9.48, 9.75, 9.86], [6.79, 7.24, 7.31, 7.94], [7.97, 8.34, 8.73, 8.6], [6.72, 7.08, 7.42, 7.5], [5.73, 5.97, 6.51, 6.22], [16.56, 15.88, 14.73, 16.59], [15.51, 14.73, 13.57, 15.37], [15.94, 15.02, 13.87, 15.57], [14.21, 13.46, 12.33, 14.13], [15.17, 14.15, 13.01, 14.61], [13.31, 12.45, 11.32, 13.03], [13.85, 12.84, 11.72, 13.31], [13.22, 12.1, 11.01, 12.44]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 10.52), ('CB', 'TYR', 'CG', 'ASP', 11.04), ('CB', 'TYR', 'OD1', 'ASP', 11.06), ('CB', 'TYR', 'OD2', 'ASP', 11.67)], [('CG', 'TYR', 'CB', 'ASP', 9.12), ('CG', 'TYR', 'CG', 'ASP', 9.61), ('CG', 'TYR', 'OD1', 'ASP', 9.7), ('CG', 'TYR', 'OD2', 'ASP', 10.19)], [('CD1', 'TYR', 'CB', 'ASP', 8.09), ('CD1', 'TYR', 'CG', 'ASP', 8.59), ('CD1', 'TYR', 'OD1', 'ASP', 8.57), ('CD1', 'TYR', 'OD2', 'ASP', 9.32)], [('CD2', 'TYR', 'CB', 'ASP', 9.05), ('CD2', 'TYR', 'CG', 'ASP', 9.48), ('CD2', 'TYR', 'OD1', 'ASP', 9.75), ('CD2', 'TYR', 'OD2', 'ASP', 9.86)], [('CE1', 'TYR', 'CB', 'ASP', 6.79), ('CE1', 'TYR', 'CG', 'ASP', 7.24), ('CE1', 'TYR', 'OD1', 'ASP', 7.31), ('CE1', 'TYR', 'OD2', 'ASP', 7.94)], [('CE2', 'TYR', 'CB', 'ASP', 7.97), ('CE2', 'TYR', 'CG', 'ASP', 8.34), ('CE2', 'TYR', 'OD1', 'ASP', 8.73), ('CE2', 'TYR', 'OD2', 'ASP', 8.6)], [('CZ', 'TYR', 'CB', 'ASP', 6.72), ('CZ', 'TYR', 'CG', 'ASP', 7.08), ('CZ', 'TYR', 'OD1', 'ASP', 7.42), ('CZ', 'TYR', 'OD2', 'ASP', 7.5)], [('OH', 'TYR', 'CB', 'ASP', 5.73), ('OH', 'TYR', 'CG', 'ASP', 5.97), ('OH', 'TYR', 'OD1', 'ASP', 6.51), ('OH', 'TYR', 'OD2', 'ASP', 6.22)], [('CB', 'TYR', 'CB', 'ASP', 16.56), ('CB', 'TYR', 'CG', 'ASP', 15.88), ('CB', 'TYR', 'OD1', 'ASP', 14.73), ('CB', 'TYR', 'OD2', 'ASP', 16.59)], [('CG', 'TYR', 'CB', 'ASP', 15.51), ('CG', 'TYR', 'CG', 'ASP', 14.73), ('CG', 'TYR', 'OD1', 'ASP', 13.57), ('CG', 'TYR', 'OD2', 'ASP', 15.37)], [('CD1', 'TYR', 'CB', 'ASP', 15.94), ('CD1', 'TYR', 'CG', 'ASP', 15.02), ('CD1', 'TYR', 'OD1', 'ASP', 13.87), ('CD1', 'TYR', 'OD2', 'ASP', 15.57)], [('CD2', 'TYR', 'CB', 'ASP', 14.21), ('CD2', 'TYR', 'CG', 'ASP', 13.46), ('CD2', 'TYR', 'OD1', 'ASP', 12.33), ('CD2', 'TYR', 'OD2', 'ASP', 14.13)], [('CE1', 'TYR', 'CB', 'ASP', 15.17), ('CE1', 'TYR', 'CG', 'ASP', 14.15), ('CE1', 'TYR', 'OD1', 'ASP', 13.01), ('CE1', 'TYR', 'OD2', 'ASP', 14.61)], [('CE2', 'TYR', 'CB', 'ASP', 13.31), ('CE2', 'TYR', 'CG', 'ASP', 12.45), ('CE2', 'TYR', 'OD1', 'ASP', 11.32), ('CE2', 'TYR', 'OD2', 'ASP', 13.03)], [('CZ', 'TYR', 'CB', 'ASP', 13.85), ('CZ', 'TYR', 'CG', 'ASP', 12.84), ('CZ', 'TYR', 'OD1', 'ASP', 11.72), ('CZ', 'TYR', 'OD2', 'ASP', 13.31)], [('OH', 'TYR', 'CB', 'ASP', 13.22), ('OH', 'TYR', 'CG', 'ASP', 12.1), ('OH', 'TYR', 'OD1', 'ASP', 11.01), ('OH', 'TYR', 'OD2', 'ASP', 12.44)]]}
GLU_ASPI = { 
	'distances':
		[[11.52, 10.76, 10.01, 11.13], [11.27, 10.3, 9.54, 10.52], [10.76, 9.7, 8.78, 9.99], [9.91, 8.94, 7.94, 9.4], [11.42, 10.24, 9.29, 10.43]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASPI', 11.52), ('CB', 'GLU', 'CG', 'ASPI', 10.76), ('CB', 'GLU', 'OD1', 'ASPI', 10.01), ('CB', 'GLU', 'OD2', 'ASPI', 11.13)], [('CG', 'GLU', 'CB', 'ASPI', 11.27), ('CG', 'GLU', 'CG', 'ASPI', 10.3), ('CG', 'GLU', 'OD1', 'ASPI', 9.54), ('CG', 'GLU', 'OD2', 'ASPI', 10.52)], [('CD', 'GLU', 'CB', 'ASPI', 10.76), ('CD', 'GLU', 'CG', 'ASPI', 9.7), ('CD', 'GLU', 'OD1', 'ASPI', 8.78), ('CD', 'GLU', 'OD2', 'ASPI', 9.99)], [('OE1', 'GLU', 'CB', 'ASPI', 9.91), ('OE1', 'GLU', 'CG', 'ASPI', 8.94), ('OE1', 'GLU', 'OD1', 'ASPI', 7.94), ('OE1', 'GLU', 'OD2', 'ASPI', 9.4)], [('OE2', 'GLU', 'CB', 'ASPI', 11.42), ('OE2', 'GLU', 'CG', 'ASPI', 10.24), ('OE2', 'GLU', 'OD1', 'ASPI', 9.29), ('OE2', 'GLU', 'OD2', 'ASPI', 10.43)]]}
ASP_ASP = { 
	'distances':
		[[15.2, 13.87, 12.95, 13.86], [14.67, 13.29, 12.35, 13.27], [15.38, 14.02, 13.03, 14.04], [13.67, 12.26, 11.37, 12.16], [15.2, 14.67, 15.38, 13.67], [13.87, 13.29, 14.02, 12.26], [12.95, 12.35, 13.03, 11.37], [13.86, 13.27, 14.04, 12.16]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 15.2), ('CB', 'ASP', 'CG', 'ASP', 13.87), ('CB', 'ASP', 'OD1', 'ASP', 12.95), ('CB', 'ASP', 'OD2', 'ASP', 13.86)], [('CG', 'ASP', 'CB', 'ASP', 14.67), ('CG', 'ASP', 'CG', 'ASP', 13.29), ('CG', 'ASP', 'OD1', 'ASP', 12.35), ('CG', 'ASP', 'OD2', 'ASP', 13.27)], [('OD1', 'ASP', 'CB', 'ASP', 15.38), ('OD1', 'ASP', 'CG', 'ASP', 14.02), ('OD1', 'ASP', 'OD1', 'ASP', 13.03), ('OD1', 'ASP', 'OD2', 'ASP', 14.04)], [('OD2', 'ASP', 'CB', 'ASP', 13.67), ('OD2', 'ASP', 'CG', 'ASP', 12.26), ('OD2', 'ASP', 'OD1', 'ASP', 11.37), ('OD2', 'ASP', 'OD2', 'ASP', 12.16)], [('CB', 'ASP', 'CB', 'ASP', 15.2), ('CB', 'ASP', 'CG', 'ASP', 14.67), ('CB', 'ASP', 'OD1', 'ASP', 15.38), ('CB', 'ASP', 'OD2', 'ASP', 13.67)], [('CG', 'ASP', 'CB', 'ASP', 13.87), ('CG', 'ASP', 'CG', 'ASP', 13.29), ('CG', 'ASP', 'OD1', 'ASP', 14.02), ('CG', 'ASP', 'OD2', 'ASP', 12.26)], [('OD1', 'ASP', 'CB', 'ASP', 12.95), ('OD1', 'ASP', 'CG', 'ASP', 12.35), ('OD1', 'ASP', 'OD1', 'ASP', 13.03), ('OD1', 'ASP', 'OD2', 'ASP', 11.37)], [('OD2', 'ASP', 'CB', 'ASP', 13.86), ('OD2', 'ASP', 'CG', 'ASP', 13.27), ('OD2', 'ASP', 'OD1', 'ASP', 14.04), ('OD2', 'ASP', 'OD2', 'ASP', 12.16)]]}
TYR_GLU = { 
	'distances':
		[[9.73, 10.24, 9.81, 9.74, 9.88], [8.65, 8.96, 8.43, 8.44, 8.42], [9.06, 9.09, 8.48, 8.68, 8.18], [7.47, 7.88, 7.34, 7.22, 7.52], [8.46, 8.22, 7.49, 7.82, 7.01], [6.65, 6.76, 6.05, 6.03, 6.14], [7.26, 6.98, 6.17, 6.44, 5.81], [7.05, 6.37, 5.39, 5.89, 4.69]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'GLU', 9.73), ('CB', 'TYR', 'CG', 'GLU', 10.24), ('CB', 'TYR', 'CD', 'GLU', 9.81), ('CB', 'TYR', 'OE1', 'GLU', 9.74), ('CB', 'TYR', 'OE2', 'GLU', 9.88)], [('CG', 'TYR', 'CB', 'GLU', 8.65), ('CG', 'TYR', 'CG', 'GLU', 8.96), ('CG', 'TYR', 'CD', 'GLU', 8.43), ('CG', 'TYR', 'OE1', 'GLU', 8.44), ('CG', 'TYR', 'OE2', 'GLU', 8.42)], [('CD1', 'TYR', 'CB', 'GLU', 9.06), ('CD1', 'TYR', 'CG', 'GLU', 9.09), ('CD1', 'TYR', 'CD', 'GLU', 8.48), ('CD1', 'TYR', 'OE1', 'GLU', 8.68), ('CD1', 'TYR', 'OE2', 'GLU', 8.18)], [('CD2', 'TYR', 'CB', 'GLU', 7.47), ('CD2', 'TYR', 'CG', 'GLU', 7.88), ('CD2', 'TYR', 'CD', 'GLU', 7.34), ('CD2', 'TYR', 'OE1', 'GLU', 7.22), ('CD2', 'TYR', 'OE2', 'GLU', 7.52)], [('CE1', 'TYR', 'CB', 'GLU', 8.46), ('CE1', 'TYR', 'CG', 'GLU', 8.22), ('CE1', 'TYR', 'CD', 'GLU', 7.49), ('CE1', 'TYR', 'OE1', 'GLU', 7.82), ('CE1', 'TYR', 'OE2', 'GLU', 7.01)], [('CE2', 'TYR', 'CB', 'GLU', 6.65), ('CE2', 'TYR', 'CG', 'GLU', 6.76), ('CE2', 'TYR', 'CD', 'GLU', 6.05), ('CE2', 'TYR', 'OE1', 'GLU', 6.03), ('CE2', 'TYR', 'OE2', 'GLU', 6.14)], [('CZ', 'TYR', 'CB', 'GLU', 7.26), ('CZ', 'TYR', 'CG', 'GLU', 6.98), ('CZ', 'TYR', 'CD', 'GLU', 6.17), ('CZ', 'TYR', 'OE1', 'GLU', 6.44), ('CZ', 'TYR', 'OE2', 'GLU', 5.81)], [('OH', 'TYR', 'CB', 'GLU', 7.05), ('OH', 'TYR', 'CG', 'GLU', 6.37), ('OH', 'TYR', 'CD', 'GLU', 5.39), ('OH', 'TYR', 'OE1', 'GLU', 5.89), ('OH', 'TYR', 'OE2', 'GLU', 4.69)]]}
ASP_GLU = { 
	'distances':
		[[9.23, 8.1, 7.55, 8.51, 6.4], [9.84, 8.61, 7.76, 8.53, 6.52], [10.81, 9.67, 8.71, 9.35, 7.49], [9.58, 8.23, 7.32, 8.05, 6.08], [11.52, 11.27, 10.76, 9.91, 11.42], [10.76, 10.3, 9.7, 8.94, 10.24], [10.01, 9.54, 8.78, 7.94, 9.29], [11.13, 10.52, 9.99, 9.4, 10.43]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 9.23), ('CB', 'ASP', 'CG', 'GLU', 8.1), ('CB', 'ASP', 'CD', 'GLU', 7.55), ('CB', 'ASP', 'OE1', 'GLU', 8.51), ('CB', 'ASP', 'OE2', 'GLU', 6.4)], [('CG', 'ASP', 'CB', 'GLU', 9.84), ('CG', 'ASP', 'CG', 'GLU', 8.61), ('CG', 'ASP', 'CD', 'GLU', 7.76), ('CG', 'ASP', 'OE1', 'GLU', 8.53), ('CG', 'ASP', 'OE2', 'GLU', 6.52)], [('OD1', 'ASP', 'CB', 'GLU', 10.81), ('OD1', 'ASP', 'CG', 'GLU', 9.67), ('OD1', 'ASP', 'CD', 'GLU', 8.71), ('OD1', 'ASP', 'OE1', 'GLU', 9.35), ('OD1', 'ASP', 'OE2', 'GLU', 7.49)], [('OD2', 'ASP', 'CB', 'GLU', 9.58), ('OD2', 'ASP', 'CG', 'GLU', 8.23), ('OD2', 'ASP', 'CD', 'GLU', 7.32), ('OD2', 'ASP', 'OE1', 'GLU', 8.05), ('OD2', 'ASP', 'OE2', 'GLU', 6.08)], [('CB', 'ASP', 'CB', 'GLU', 11.52), ('CB', 'ASP', 'CG', 'GLU', 11.27), ('CB', 'ASP', 'CD', 'GLU', 10.76), ('CB', 'ASP', 'OE1', 'GLU', 9.91), ('CB', 'ASP', 'OE2', 'GLU', 11.42)], [('CG', 'ASP', 'CB', 'GLU', 10.76), ('CG', 'ASP', 'CG', 'GLU', 10.3), ('CG', 'ASP', 'CD', 'GLU', 9.7), ('CG', 'ASP', 'OE1', 'GLU', 8.94), ('CG', 'ASP', 'OE2', 'GLU', 10.24)], [('OD1', 'ASP', 'CB', 'GLU', 10.01), ('OD1', 'ASP', 'CG', 'GLU', 9.54), ('OD1', 'ASP', 'CD', 'GLU', 8.78), ('OD1', 'ASP', 'OE1', 'GLU', 7.94), ('OD1', 'ASP', 'OE2', 'GLU', 9.29)], [('OD2', 'ASP', 'CB', 'GLU', 11.13), ('OD2', 'ASP', 'CG', 'GLU', 10.52), ('OD2', 'ASP', 'CD', 'GLU', 9.99), ('OD2', 'ASP', 'OE1', 'GLU', 9.4), ('OD2', 'ASP', 'OE2', 'GLU', 10.43)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'P_1s2i_2_4_2_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ASPI, d, 'P_1s2i_2_4_2_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'P_1s2i_2_4_2_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(TYR_GLU, d, 'P_1s2i_2_4_2_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLU, d, 'P_1s2i_2_4_2_6')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'GLU_ASPI' :  match2,
		'ASP_ASP' :  match3,
		'TYR_GLU' :  match4,
		'ASP_GLU' :  match5}