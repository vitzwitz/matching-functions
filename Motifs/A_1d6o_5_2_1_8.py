'''
FUNC:A_1d6o_5_2_1_8
PDB:1d6o
EC:5.2.1.8
RESI:asp,ile,tyr
LOCI:a-37,56,82;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[13.86, 14.42, 15.52, 13.84], [12.62, 13.08, 14.19, 12.45], [11.63, 12.18, 13.34, 11.57], [12.61, 12.89, 13.95, 12.18], [10.57, 11.01, 12.18, 10.32], [11.65, 11.81, 12.85, 11.01], [10.58, 10.8, 11.91, 10.0], [9.77, 9.82, 10.91, 8.91]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 13.86), ('CB', 'TYR', 'CG', 'ASP', 14.42), ('CB', 'TYR', 'OD1', 'ASP', 15.52), ('CB', 'TYR', 'OD2', 'ASP', 13.84)], [('CG', 'TYR', 'CB', 'ASP', 12.62), ('CG', 'TYR', 'CG', 'ASP', 13.08), ('CG', 'TYR', 'OD1', 'ASP', 14.19), ('CG', 'TYR', 'OD2', 'ASP', 12.45)], [('CD1', 'TYR', 'CB', 'ASP', 11.63), ('CD1', 'TYR', 'CG', 'ASP', 12.18), ('CD1', 'TYR', 'OD1', 'ASP', 13.34), ('CD1', 'TYR', 'OD2', 'ASP', 11.57)], [('CD2', 'TYR', 'CB', 'ASP', 12.61), ('CD2', 'TYR', 'CG', 'ASP', 12.89), ('CD2', 'TYR', 'OD1', 'ASP', 13.95), ('CD2', 'TYR', 'OD2', 'ASP', 12.18)], [('CE1', 'TYR', 'CB', 'ASP', 10.57), ('CE1', 'TYR', 'CG', 'ASP', 11.01), ('CE1', 'TYR', 'OD1', 'ASP', 12.18), ('CE1', 'TYR', 'OD2', 'ASP', 10.32)], [('CE2', 'TYR', 'CB', 'ASP', 11.65), ('CE2', 'TYR', 'CG', 'ASP', 11.81), ('CE2', 'TYR', 'OD1', 'ASP', 12.85), ('CE2', 'TYR', 'OD2', 'ASP', 11.01)], [('CZ', 'TYR', 'CB', 'ASP', 10.58), ('CZ', 'TYR', 'CG', 'ASP', 10.8), ('CZ', 'TYR', 'OD1', 'ASP', 11.91), ('CZ', 'TYR', 'OD2', 'ASP', 10.0)], [('OH', 'TYR', 'CB', 'ASP', 9.77), ('OH', 'TYR', 'CG', 'ASP', 9.82), ('OH', 'TYR', 'OD1', 'ASP', 10.91), ('OH', 'TYR', 'OD2', 'ASP', 8.91)]]}
ILE_ASP = { 
	'distances':
		[[13.55, 13.68, 14.86, 12.69], [12.72, 12.89, 14.08, 11.93], [12.81, 12.93, 14.1, 11.95], [12.02, 12.38, 13.61, 11.54], [15.57, 15.51, 16.61, 14.43], [15.55, 15.53, 16.66, 14.46], [14.44, 14.4, 15.52, 13.32], [13.78, 13.59, 14.65, 12.45]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'ASP', 13.55), ('CB', 'ILE', 'CG', 'ASP', 13.68), ('CB', 'ILE', 'OD1', 'ASP', 14.86), ('CB', 'ILE', 'OD2', 'ASP', 12.69)], [('CG1', 'ILE', 'CB', 'ASP', 12.72), ('CG1', 'ILE', 'CG', 'ASP', 12.89), ('CG1', 'ILE', 'OD1', 'ASP', 14.08), ('CG1', 'ILE', 'OD2', 'ASP', 11.93)], [('CG2', 'ILE', 'CB', 'ASP', 12.81), ('CG2', 'ILE', 'CG', 'ASP', 12.93), ('CG2', 'ILE', 'OD1', 'ASP', 14.1), ('CG2', 'ILE', 'OD2', 'ASP', 11.95)], [('CD1', 'ILE', 'CB', 'ASP', 12.02), ('CD1', 'ILE', 'CG', 'ASP', 12.38), ('CD1', 'ILE', 'OD1', 'ASP', 13.61), ('CD1', 'ILE', 'OD2', 'ASP', 11.54)], [('O', 'ILE', 'CB', 'ASP', 15.57), ('O', 'ILE', 'CG', 'ASP', 15.51), ('O', 'ILE', 'OD1', 'ASP', 16.61), ('O', 'ILE', 'OD2', 'ASP', 14.43)], [('C', 'ILE', 'CB', 'ASP', 15.55), ('C', 'ILE', 'CG', 'ASP', 15.53), ('C', 'ILE', 'OD1', 'ASP', 16.66), ('C', 'ILE', 'OD2', 'ASP', 14.46)], [('CA', 'ILE', 'CB', 'ASP', 14.44), ('CA', 'ILE', 'CG', 'ASP', 14.4), ('CA', 'ILE', 'OD1', 'ASP', 15.52), ('CA', 'ILE', 'OD2', 'ASP', 13.32)], [('N', 'ILE', 'CB', 'ASP', 13.78), ('N', 'ILE', 'CG', 'ASP', 13.59), ('N', 'ILE', 'OD1', 'ASP', 14.65), ('N', 'ILE', 'OD2', 'ASP', 12.45)]]}
ILE_TYR = { 
	'distances':
		[[8.93, 8.04, 7.53, 8.09, 7.03, 7.64, 7.1, 7.16], [9.7, 8.72, 7.91, 8.89, 7.23, 8.32, 7.46, 7.31], [7.77, 6.73, 6.32, 6.63, 5.77, 6.12, 5.65, 5.83], [9.09, 8.16, 7.14, 8.59, 6.53, 8.13, 7.11, 7.12], [12.18, 11.35, 10.86, 11.29, 10.28, 10.75, 10.23, 9.99], [11.14, 10.38, 10.01, 10.31, 9.55, 9.88, 9.49, 9.41], [10.04, 9.15, 8.82, 8.96, 8.27, 8.43, 8.07, 7.95], [10.78, 9.7, 9.32, 9.34, 8.52, 8.55, 8.1, 7.67]],
	'comparisons':
		[[('CB', 'ILE', 'CB', 'TYR', 8.93), ('CB', 'ILE', 'CG', 'TYR', 8.04), ('CB', 'ILE', 'CD1', 'TYR', 7.53), ('CB', 'ILE', 'CD2', 'TYR', 8.09), ('CB', 'ILE', 'CE1', 'TYR', 7.03), ('CB', 'ILE', 'CE2', 'TYR', 7.64), ('CB', 'ILE', 'CZ', 'TYR', 7.1), ('CB', 'ILE', 'OH', 'TYR', 7.16)], [('CG1', 'ILE', 'CB', 'TYR', 9.7), ('CG1', 'ILE', 'CG', 'TYR', 8.72), ('CG1', 'ILE', 'CD1', 'TYR', 7.91), ('CG1', 'ILE', 'CD2', 'TYR', 8.89), ('CG1', 'ILE', 'CE1', 'TYR', 7.23), ('CG1', 'ILE', 'CE2', 'TYR', 8.32), ('CG1', 'ILE', 'CZ', 'TYR', 7.46), ('CG1', 'ILE', 'OH', 'TYR', 7.31)], [('CG2', 'ILE', 'CB', 'TYR', 7.77), ('CG2', 'ILE', 'CG', 'TYR', 6.73), ('CG2', 'ILE', 'CD1', 'TYR', 6.32), ('CG2', 'ILE', 'CD2', 'TYR', 6.63), ('CG2', 'ILE', 'CE1', 'TYR', 5.77), ('CG2', 'ILE', 'CE2', 'TYR', 6.12), ('CG2', 'ILE', 'CZ', 'TYR', 5.65), ('CG2', 'ILE', 'OH', 'TYR', 5.83)], [('CD1', 'ILE', 'CB', 'TYR', 9.09), ('CD1', 'ILE', 'CG', 'TYR', 8.16), ('CD1', 'ILE', 'CD1', 'TYR', 7.14), ('CD1', 'ILE', 'CD2', 'TYR', 8.59), ('CD1', 'ILE', 'CE1', 'TYR', 6.53), ('CD1', 'ILE', 'CE2', 'TYR', 8.13), ('CD1', 'ILE', 'CZ', 'TYR', 7.11), ('CD1', 'ILE', 'OH', 'TYR', 7.12)], [('O', 'ILE', 'CB', 'TYR', 12.18), ('O', 'ILE', 'CG', 'TYR', 11.35), ('O', 'ILE', 'CD1', 'TYR', 10.86), ('O', 'ILE', 'CD2', 'TYR', 11.29), ('O', 'ILE', 'CE1', 'TYR', 10.28), ('O', 'ILE', 'CE2', 'TYR', 10.75), ('O', 'ILE', 'CZ', 'TYR', 10.23), ('O', 'ILE', 'OH', 'TYR', 9.99)], [('C', 'ILE', 'CB', 'TYR', 11.14), ('C', 'ILE', 'CG', 'TYR', 10.38), ('C', 'ILE', 'CD1', 'TYR', 10.01), ('C', 'ILE', 'CD2', 'TYR', 10.31), ('C', 'ILE', 'CE1', 'TYR', 9.55), ('C', 'ILE', 'CE2', 'TYR', 9.88), ('C', 'ILE', 'CZ', 'TYR', 9.49), ('C', 'ILE', 'OH', 'TYR', 9.41)], [('CA', 'ILE', 'CB', 'TYR', 10.04), ('CA', 'ILE', 'CG', 'TYR', 9.15), ('CA', 'ILE', 'CD1', 'TYR', 8.82), ('CA', 'ILE', 'CD2', 'TYR', 8.96), ('CA', 'ILE', 'CE1', 'TYR', 8.27), ('CA', 'ILE', 'CE2', 'TYR', 8.43), ('CA', 'ILE', 'CZ', 'TYR', 8.07), ('CA', 'ILE', 'OH', 'TYR', 7.95)], [('N', 'ILE', 'CB', 'TYR', 10.78), ('N', 'ILE', 'CG', 'TYR', 9.7), ('N', 'ILE', 'CD1', 'TYR', 9.32), ('N', 'ILE', 'CD2', 'TYR', 9.34), ('N', 'ILE', 'CE1', 'TYR', 8.52), ('N', 'ILE', 'CE2', 'TYR', 8.55), ('N', 'ILE', 'CZ', 'TYR', 8.1), ('N', 'ILE', 'OH', 'TYR', 7.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'A_1d6o_5_2_1_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ILE_ASP, d, 'A_1d6o_5_2_1_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ILE_TYR, d, 'A_1d6o_5_2_1_8')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'ILE_ASP' :  match2,
		'ILE_TYR' :  match3}