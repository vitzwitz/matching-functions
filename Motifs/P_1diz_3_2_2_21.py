'''
FUNC:P_1diz_3_2_2_21
PDB:1diz
EC:3.2.2.21
RESI:tyr,asp,trp
LOCI:a-222,238,272;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[8.83, 8.76, 7.95, 9.74], [8.96, 8.62, 7.72, 9.46], [8.72, 8.3, 7.52, 9.0], [9.67, 9.17, 8.14, 9.99], [9.22, 8.57, 7.75, 9.1], [10.12, 9.42, 8.36, 10.09], [9.91, 9.13, 8.17, 9.66], [10.64, 9.7, 8.76, 10.08]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 8.83), ('CB', 'TYR', 'CG', 'ASP', 8.76), ('CB', 'TYR', 'OD1', 'ASP', 7.95), ('CB', 'TYR', 'OD2', 'ASP', 9.74)], [('CG', 'TYR', 'CB', 'ASP', 8.96), ('CG', 'TYR', 'CG', 'ASP', 8.62), ('CG', 'TYR', 'OD1', 'ASP', 7.72), ('CG', 'TYR', 'OD2', 'ASP', 9.46)], [('CD1', 'TYR', 'CB', 'ASP', 8.72), ('CD1', 'TYR', 'CG', 'ASP', 8.3), ('CD1', 'TYR', 'OD1', 'ASP', 7.52), ('CD1', 'TYR', 'OD2', 'ASP', 9.0)], [('CD2', 'TYR', 'CB', 'ASP', 9.67), ('CD2', 'TYR', 'CG', 'ASP', 9.17), ('CD2', 'TYR', 'OD1', 'ASP', 8.14), ('CD2', 'TYR', 'OD2', 'ASP', 9.99)], [('CE1', 'TYR', 'CB', 'ASP', 9.22), ('CE1', 'TYR', 'CG', 'ASP', 8.57), ('CE1', 'TYR', 'OD1', 'ASP', 7.75), ('CE1', 'TYR', 'OD2', 'ASP', 9.1)], [('CE2', 'TYR', 'CB', 'ASP', 10.12), ('CE2', 'TYR', 'CG', 'ASP', 9.42), ('CE2', 'TYR', 'OD1', 'ASP', 8.36), ('CE2', 'TYR', 'OD2', 'ASP', 10.09)], [('CZ', 'TYR', 'CB', 'ASP', 9.91), ('CZ', 'TYR', 'CG', 'ASP', 9.13), ('CZ', 'TYR', 'OD1', 'ASP', 8.17), ('CZ', 'TYR', 'OD2', 'ASP', 9.66)], [('OH', 'TYR', 'CB', 'ASP', 10.64), ('OH', 'TYR', 'CG', 'ASP', 9.7), ('OH', 'TYR', 'OD1', 'ASP', 8.76), ('OH', 'TYR', 'OD2', 'ASP', 10.08)]]}
TYR_TRP = { 
	'distances':
		[[12.6, 11.34, 11.43, 9.98, 10.23, 9.22, 9.48, 7.82, 8.12, 7.19], [11.8, 10.63, 10.83, 9.23, 9.72, 8.61, 8.61, 7.25, 7.24, 6.45], [10.62, 9.52, 9.85, 8.1, 8.83, 7.62, 7.37, 6.32, 5.98, 5.34], [12.39, 11.25, 11.47, 9.88, 10.38, 9.29, 9.25, 7.97, 7.92, 7.19], [10.06, 9.08, 9.56, 7.67, 8.66, 7.4, 6.8, 6.22, 5.45, 5.1], [11.93, 10.9, 11.23, 9.54, 10.25, 9.12, 8.82, 7.91, 7.55, 7.03], [10.78, 9.84, 10.3, 8.47, 9.42, 8.21, 7.64, 7.09, 6.38, 6.06], [10.56, 9.77, 10.35, 8.48, 9.62, 8.41, 7.57, 7.47, 6.47, 6.42]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'TRP', 12.6), ('CB', 'TYR', 'CG', 'TRP', 11.34), ('CB', 'TYR', 'CD1', 'TRP', 11.43), ('CB', 'TYR', 'CD2', 'TRP', 9.98), ('CB', 'TYR', 'NE1', 'TRP', 10.23), ('CB', 'TYR', 'CE2', 'TRP', 9.22), ('CB', 'TYR', 'CE3', 'TRP', 9.48), ('CB', 'TYR', 'CZ2', 'TRP', 7.82), ('CB', 'TYR', 'CZ3', 'TRP', 8.12), ('CB', 'TYR', 'CH2', 'TRP', 7.19)], [('CG', 'TYR', 'CB', 'TRP', 11.8), ('CG', 'TYR', 'CG', 'TRP', 10.63), ('CG', 'TYR', 'CD1', 'TRP', 10.83), ('CG', 'TYR', 'CD2', 'TRP', 9.23), ('CG', 'TYR', 'NE1', 'TRP', 9.72), ('CG', 'TYR', 'CE2', 'TRP', 8.61), ('CG', 'TYR', 'CE3', 'TRP', 8.61), ('CG', 'TYR', 'CZ2', 'TRP', 7.25), ('CG', 'TYR', 'CZ3', 'TRP', 7.24), ('CG', 'TYR', 'CH2', 'TRP', 6.45)], [('CD1', 'TYR', 'CB', 'TRP', 10.62), ('CD1', 'TYR', 'CG', 'TRP', 9.52), ('CD1', 'TYR', 'CD1', 'TRP', 9.85), ('CD1', 'TYR', 'CD2', 'TRP', 8.1), ('CD1', 'TYR', 'NE1', 'TRP', 8.83), ('CD1', 'TYR', 'CE2', 'TRP', 7.62), ('CD1', 'TYR', 'CE3', 'TRP', 7.37), ('CD1', 'TYR', 'CZ2', 'TRP', 6.32), ('CD1', 'TYR', 'CZ3', 'TRP', 5.98), ('CD1', 'TYR', 'CH2', 'TRP', 5.34)], [('CD2', 'TYR', 'CB', 'TRP', 12.39), ('CD2', 'TYR', 'CG', 'TRP', 11.25), ('CD2', 'TYR', 'CD1', 'TRP', 11.47), ('CD2', 'TYR', 'CD2', 'TRP', 9.88), ('CD2', 'TYR', 'NE1', 'TRP', 10.38), ('CD2', 'TYR', 'CE2', 'TRP', 9.29), ('CD2', 'TYR', 'CE3', 'TRP', 9.25), ('CD2', 'TYR', 'CZ2', 'TRP', 7.97), ('CD2', 'TYR', 'CZ3', 'TRP', 7.92), ('CD2', 'TYR', 'CH2', 'TRP', 7.19)], [('CE1', 'TYR', 'CB', 'TRP', 10.06), ('CE1', 'TYR', 'CG', 'TRP', 9.08), ('CE1', 'TYR', 'CD1', 'TRP', 9.56), ('CE1', 'TYR', 'CD2', 'TRP', 7.67), ('CE1', 'TYR', 'NE1', 'TRP', 8.66), ('CE1', 'TYR', 'CE2', 'TRP', 7.4), ('CE1', 'TYR', 'CE3', 'TRP', 6.8), ('CE1', 'TYR', 'CZ2', 'TRP', 6.22), ('CE1', 'TYR', 'CZ3', 'TRP', 5.45), ('CE1', 'TYR', 'CH2', 'TRP', 5.1)], [('CE2', 'TYR', 'CB', 'TRP', 11.93), ('CE2', 'TYR', 'CG', 'TRP', 10.9), ('CE2', 'TYR', 'CD1', 'TRP', 11.23), ('CE2', 'TYR', 'CD2', 'TRP', 9.54), ('CE2', 'TYR', 'NE1', 'TRP', 10.25), ('CE2', 'TYR', 'CE2', 'TRP', 9.12), ('CE2', 'TYR', 'CE3', 'TRP', 8.82), ('CE2', 'TYR', 'CZ2', 'TRP', 7.91), ('CE2', 'TYR', 'CZ3', 'TRP', 7.55), ('CE2', 'TYR', 'CH2', 'TRP', 7.03)], [('CZ', 'TYR', 'CB', 'TRP', 10.78), ('CZ', 'TYR', 'CG', 'TRP', 9.84), ('CZ', 'TYR', 'CD1', 'TRP', 10.3), ('CZ', 'TYR', 'CD2', 'TRP', 8.47), ('CZ', 'TYR', 'NE1', 'TRP', 9.42), ('CZ', 'TYR', 'CE2', 'TRP', 8.21), ('CZ', 'TYR', 'CE3', 'TRP', 7.64), ('CZ', 'TYR', 'CZ2', 'TRP', 7.09), ('CZ', 'TYR', 'CZ3', 'TRP', 6.38), ('CZ', 'TYR', 'CH2', 'TRP', 6.06)], [('OH', 'TYR', 'CB', 'TRP', 10.56), ('OH', 'TYR', 'CG', 'TRP', 9.77), ('OH', 'TYR', 'CD1', 'TRP', 10.35), ('OH', 'TYR', 'CD2', 'TRP', 8.48), ('OH', 'TYR', 'NE1', 'TRP', 9.62), ('OH', 'TYR', 'CE2', 'TRP', 8.41), ('OH', 'TYR', 'CE3', 'TRP', 7.57), ('OH', 'TYR', 'CZ2', 'TRP', 7.47), ('OH', 'TYR', 'CZ3', 'TRP', 6.47), ('OH', 'TYR', 'CH2', 'TRP', 6.42)]]}
ASP_TRP = { 
	'distances':
		[[9.16, 7.67, 6.7, 7.22, 5.44, 5.82, 8.09, 5.38, 7.79, 6.53], [8.3, 6.82, 5.9, 6.35, 4.62, 4.96, 7.24, 4.59, 6.99, 5.79], [8.75, 7.28, 6.54, 6.61, 5.24, 5.26, 7.29, 4.6, 6.84, 5.57], [7.4, 5.98, 4.92, 5.77, 3.78, 4.46, 6.84, 4.54, 6.87, 5.86]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TRP', 9.16), ('CB', 'ASP', 'CG', 'TRP', 7.67), ('CB', 'ASP', 'CD1', 'TRP', 6.7), ('CB', 'ASP', 'CD2', 'TRP', 7.22), ('CB', 'ASP', 'NE1', 'TRP', 5.44), ('CB', 'ASP', 'CE2', 'TRP', 5.82), ('CB', 'ASP', 'CE3', 'TRP', 8.09), ('CB', 'ASP', 'CZ2', 'TRP', 5.38), ('CB', 'ASP', 'CZ3', 'TRP', 7.79), ('CB', 'ASP', 'CH2', 'TRP', 6.53)], [('CG', 'ASP', 'CB', 'TRP', 8.3), ('CG', 'ASP', 'CG', 'TRP', 6.82), ('CG', 'ASP', 'CD1', 'TRP', 5.9), ('CG', 'ASP', 'CD2', 'TRP', 6.35), ('CG', 'ASP', 'NE1', 'TRP', 4.62), ('CG', 'ASP', 'CE2', 'TRP', 4.96), ('CG', 'ASP', 'CE3', 'TRP', 7.24), ('CG', 'ASP', 'CZ2', 'TRP', 4.59), ('CG', 'ASP', 'CZ3', 'TRP', 6.99), ('CG', 'ASP', 'CH2', 'TRP', 5.79)], [('OD1', 'ASP', 'CB', 'TRP', 8.75), ('OD1', 'ASP', 'CG', 'TRP', 7.28), ('OD1', 'ASP', 'CD1', 'TRP', 6.54), ('OD1', 'ASP', 'CD2', 'TRP', 6.61), ('OD1', 'ASP', 'NE1', 'TRP', 5.24), ('OD1', 'ASP', 'CE2', 'TRP', 5.26), ('OD1', 'ASP', 'CE3', 'TRP', 7.29), ('OD1', 'ASP', 'CZ2', 'TRP', 4.6), ('OD1', 'ASP', 'CZ3', 'TRP', 6.84), ('OD1', 'ASP', 'CH2', 'TRP', 5.57)], [('OD2', 'ASP', 'CB', 'TRP', 7.4), ('OD2', 'ASP', 'CG', 'TRP', 5.98), ('OD2', 'ASP', 'CD1', 'TRP', 4.92), ('OD2', 'ASP', 'CD2', 'TRP', 5.77), ('OD2', 'ASP', 'NE1', 'TRP', 3.78), ('OD2', 'ASP', 'CE2', 'TRP', 4.46), ('OD2', 'ASP', 'CE3', 'TRP', 6.84), ('OD2', 'ASP', 'CZ2', 'TRP', 4.54), ('OD2', 'ASP', 'CZ3', 'TRP', 6.87), ('OD2', 'ASP', 'CH2', 'TRP', 5.86)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'P_1diz_3_2_2_21')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(TYR_TRP, d, 'P_1diz_3_2_2_21')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TRP, d, 'P_1diz_3_2_2_21')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'TYR_TRP' :  match2,
		'ASP_TRP' :  match3}