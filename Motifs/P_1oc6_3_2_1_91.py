'''
FUNC:P_1oc6_3_2_1_91
PDB:1oc6
EC:3.2.1.91
RESI:tyr,arg,asp,asp
LOCI:a-174,179,180,226;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[11.62, 10.18, 9.63, 9.78], [10.21, 8.75, 8.18, 8.37], [9.28, 7.89, 7.23, 7.69], [10.06, 8.55, 8.04, 8.07], [8.01, 6.6, 5.88, 6.52], [8.95, 7.44, 6.93, 7.0], [7.81, 6.32, 5.67, 6.09], [6.78, 5.32, 4.66, 5.24], [10.37, 11.54, 12.64, 11.55], [9.14, 10.23, 11.38, 10.15], [8.01, 9.1, 10.22, 9.09], [9.35, 10.32, 11.52, 10.11], [6.95, 7.91, 9.08, 7.79], [8.51, 9.33, 10.54, 8.99], [7.24, 8.04, 9.26, 7.72], [6.69, 7.2, 8.44, 6.7]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 11.62), ('CB', 'TYR', 'CG', 'ASP', 10.18), ('CB', 'TYR', 'OD1', 'ASP', 9.63), ('CB', 'TYR', 'OD2', 'ASP', 9.78)], [('CG', 'TYR', 'CB', 'ASP', 10.21), ('CG', 'TYR', 'CG', 'ASP', 8.75), ('CG', 'TYR', 'OD1', 'ASP', 8.18), ('CG', 'TYR', 'OD2', 'ASP', 8.37)], [('CD1', 'TYR', 'CB', 'ASP', 9.28), ('CD1', 'TYR', 'CG', 'ASP', 7.89), ('CD1', 'TYR', 'OD1', 'ASP', 7.23), ('CD1', 'TYR', 'OD2', 'ASP', 7.69)], [('CD2', 'TYR', 'CB', 'ASP', 10.06), ('CD2', 'TYR', 'CG', 'ASP', 8.55), ('CD2', 'TYR', 'OD1', 'ASP', 8.04), ('CD2', 'TYR', 'OD2', 'ASP', 8.07)], [('CE1', 'TYR', 'CB', 'ASP', 8.01), ('CE1', 'TYR', 'CG', 'ASP', 6.6), ('CE1', 'TYR', 'OD1', 'ASP', 5.88), ('CE1', 'TYR', 'OD2', 'ASP', 6.52)], [('CE2', 'TYR', 'CB', 'ASP', 8.95), ('CE2', 'TYR', 'CG', 'ASP', 7.44), ('CE2', 'TYR', 'OD1', 'ASP', 6.93), ('CE2', 'TYR', 'OD2', 'ASP', 7.0)], [('CZ', 'TYR', 'CB', 'ASP', 7.81), ('CZ', 'TYR', 'CG', 'ASP', 6.32), ('CZ', 'TYR', 'OD1', 'ASP', 5.67), ('CZ', 'TYR', 'OD2', 'ASP', 6.09)], [('OH', 'TYR', 'CB', 'ASP', 6.78), ('OH', 'TYR', 'CG', 'ASP', 5.32), ('OH', 'TYR', 'OD1', 'ASP', 4.66), ('OH', 'TYR', 'OD2', 'ASP', 5.24)], [('CB', 'TYR', 'CB', 'ASP', 10.37), ('CB', 'TYR', 'CG', 'ASP', 11.54), ('CB', 'TYR', 'OD1', 'ASP', 12.64), ('CB', 'TYR', 'OD2', 'ASP', 11.55)], [('CG', 'TYR', 'CB', 'ASP', 9.14), ('CG', 'TYR', 'CG', 'ASP', 10.23), ('CG', 'TYR', 'OD1', 'ASP', 11.38), ('CG', 'TYR', 'OD2', 'ASP', 10.15)], [('CD1', 'TYR', 'CB', 'ASP', 8.01), ('CD1', 'TYR', 'CG', 'ASP', 9.1), ('CD1', 'TYR', 'OD1', 'ASP', 10.22), ('CD1', 'TYR', 'OD2', 'ASP', 9.09)], [('CD2', 'TYR', 'CB', 'ASP', 9.35), ('CD2', 'TYR', 'CG', 'ASP', 10.32), ('CD2', 'TYR', 'OD1', 'ASP', 11.52), ('CD2', 'TYR', 'OD2', 'ASP', 10.11)], [('CE1', 'TYR', 'CB', 'ASP', 6.95), ('CE1', 'TYR', 'CG', 'ASP', 7.91), ('CE1', 'TYR', 'OD1', 'ASP', 9.08), ('CE1', 'TYR', 'OD2', 'ASP', 7.79)], [('CE2', 'TYR', 'CB', 'ASP', 8.51), ('CE2', 'TYR', 'CG', 'ASP', 9.33), ('CE2', 'TYR', 'OD1', 'ASP', 10.54), ('CE2', 'TYR', 'OD2', 'ASP', 8.99)], [('CZ', 'TYR', 'CB', 'ASP', 7.24), ('CZ', 'TYR', 'CG', 'ASP', 8.04), ('CZ', 'TYR', 'OD1', 'ASP', 9.26), ('CZ', 'TYR', 'OD2', 'ASP', 7.72)], [('OH', 'TYR', 'CB', 'ASP', 6.69), ('OH', 'TYR', 'CG', 'ASP', 7.2), ('OH', 'TYR', 'OD1', 'ASP', 8.44), ('OH', 'TYR', 'OD2', 'ASP', 6.7)]]}
ARG_ASP = { 
	'distances':
		[[6.61, 6.12, 6.83, 5.54], [6.82, 5.97, 6.29, 5.5], [7.69, 6.56, 6.79, 5.82], [7.22, 5.97, 6.3, 4.98], [8.21, 6.91, 7.2, 5.84], [9.45, 8.14, 8.35, 7.11], [8.18, 6.91, 7.26, 5.81], [9.57, 9.54, 10.52, 8.85], [8.69, 8.94, 9.98, 8.42], [9.28, 9.7, 10.84, 9.17], [9.21, 9.52, 10.72, 8.83], [10.06, 10.44, 11.67, 9.74], [10.97, 11.49, 12.71, 10.88], [10.27, 10.54, 11.76, 9.73]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 6.61), ('CB', 'ARG', 'CG', 'ASP', 6.12), ('CB', 'ARG', 'OD1', 'ASP', 6.83), ('CB', 'ARG', 'OD2', 'ASP', 5.54)], [('CG', 'ARG', 'CB', 'ASP', 6.82), ('CG', 'ARG', 'CG', 'ASP', 5.97), ('CG', 'ARG', 'OD1', 'ASP', 6.29), ('CG', 'ARG', 'OD2', 'ASP', 5.5)], [('CD', 'ARG', 'CB', 'ASP', 7.69), ('CD', 'ARG', 'CG', 'ASP', 6.56), ('CD', 'ARG', 'OD1', 'ASP', 6.79), ('CD', 'ARG', 'OD2', 'ASP', 5.82)], [('NE', 'ARG', 'CB', 'ASP', 7.22), ('NE', 'ARG', 'CG', 'ASP', 5.97), ('NE', 'ARG', 'OD1', 'ASP', 6.3), ('NE', 'ARG', 'OD2', 'ASP', 4.98)], [('CZ', 'ARG', 'CB', 'ASP', 8.21), ('CZ', 'ARG', 'CG', 'ASP', 6.91), ('CZ', 'ARG', 'OD1', 'ASP', 7.2), ('CZ', 'ARG', 'OD2', 'ASP', 5.84)], [('NH1', 'ARG', 'CB', 'ASP', 9.45), ('NH1', 'ARG', 'CG', 'ASP', 8.14), ('NH1', 'ARG', 'OD1', 'ASP', 8.35), ('NH1', 'ARG', 'OD2', 'ASP', 7.11)], [('NH2', 'ARG', 'CB', 'ASP', 8.18), ('NH2', 'ARG', 'CG', 'ASP', 6.91), ('NH2', 'ARG', 'OD1', 'ASP', 7.26), ('NH2', 'ARG', 'OD2', 'ASP', 5.81)], [('CB', 'ARG', 'CB', 'ASP', 9.57), ('CB', 'ARG', 'CG', 'ASP', 9.54), ('CB', 'ARG', 'OD1', 'ASP', 10.52), ('CB', 'ARG', 'OD2', 'ASP', 8.85)], [('CG', 'ARG', 'CB', 'ASP', 8.69), ('CG', 'ARG', 'CG', 'ASP', 8.94), ('CG', 'ARG', 'OD1', 'ASP', 9.98), ('CG', 'ARG', 'OD2', 'ASP', 8.42)], [('CD', 'ARG', 'CB', 'ASP', 9.28), ('CD', 'ARG', 'CG', 'ASP', 9.7), ('CD', 'ARG', 'OD1', 'ASP', 10.84), ('CD', 'ARG', 'OD2', 'ASP', 9.17)], [('NE', 'ARG', 'CB', 'ASP', 9.21), ('NE', 'ARG', 'CG', 'ASP', 9.52), ('NE', 'ARG', 'OD1', 'ASP', 10.72), ('NE', 'ARG', 'OD2', 'ASP', 8.83)], [('CZ', 'ARG', 'CB', 'ASP', 10.06), ('CZ', 'ARG', 'CG', 'ASP', 10.44), ('CZ', 'ARG', 'OD1', 'ASP', 11.67), ('CZ', 'ARG', 'OD2', 'ASP', 9.74)], [('NH1', 'ARG', 'CB', 'ASP', 10.97), ('NH1', 'ARG', 'CG', 'ASP', 11.49), ('NH1', 'ARG', 'OD1', 'ASP', 12.71), ('NH1', 'ARG', 'OD2', 'ASP', 10.88)], [('NH2', 'ARG', 'CB', 'ASP', 10.27), ('NH2', 'ARG', 'CG', 'ASP', 10.54), ('NH2', 'ARG', 'OD1', 'ASP', 11.76), ('NH2', 'ARG', 'OD2', 'ASP', 9.73)]]}
TYR_ARG = { 
	'distances':
		[[9.66, 8.3, 7.22, 7.55, 7.33, 6.76, 8.14], [8.7, 7.34, 6.3, 6.4, 6.28, 6.03, 6.99], [7.94, 6.5, 5.79, 6.1, 6.39, 6.44, 7.2], [8.96, 7.74, 6.58, 6.22, 5.78, 5.65, 6.18], [7.37, 6.0, 5.53, 5.55, 6.03, 6.48, 6.65], [8.52, 7.4, 6.41, 5.73, 5.39, 5.74, 5.49], [7.71, 6.55, 5.89, 5.35, 5.53, 6.17, 5.78], [7.68, 6.75, 6.38, 5.58, 5.88, 6.83, 5.79]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ARG', 9.66), ('CB', 'TYR', 'CG', 'ARG', 8.3), ('CB', 'TYR', 'CD', 'ARG', 7.22), ('CB', 'TYR', 'NE', 'ARG', 7.55), ('CB', 'TYR', 'CZ', 'ARG', 7.33), ('CB', 'TYR', 'NH1', 'ARG', 6.76), ('CB', 'TYR', 'NH2', 'ARG', 8.14)], [('CG', 'TYR', 'CB', 'ARG', 8.7), ('CG', 'TYR', 'CG', 'ARG', 7.34), ('CG', 'TYR', 'CD', 'ARG', 6.3), ('CG', 'TYR', 'NE', 'ARG', 6.4), ('CG', 'TYR', 'CZ', 'ARG', 6.28), ('CG', 'TYR', 'NH1', 'ARG', 6.03), ('CG', 'TYR', 'NH2', 'ARG', 6.99)], [('CD1', 'TYR', 'CB', 'ARG', 7.94), ('CD1', 'TYR', 'CG', 'ARG', 6.5), ('CD1', 'TYR', 'CD', 'ARG', 5.79), ('CD1', 'TYR', 'NE', 'ARG', 6.1), ('CD1', 'TYR', 'CZ', 'ARG', 6.39), ('CD1', 'TYR', 'NH1', 'ARG', 6.44), ('CD1', 'TYR', 'NH2', 'ARG', 7.2)], [('CD2', 'TYR', 'CB', 'ARG', 8.96), ('CD2', 'TYR', 'CG', 'ARG', 7.74), ('CD2', 'TYR', 'CD', 'ARG', 6.58), ('CD2', 'TYR', 'NE', 'ARG', 6.22), ('CD2', 'TYR', 'CZ', 'ARG', 5.78), ('CD2', 'TYR', 'NH1', 'ARG', 5.65), ('CD2', 'TYR', 'NH2', 'ARG', 6.18)], [('CE1', 'TYR', 'CB', 'ARG', 7.37), ('CE1', 'TYR', 'CG', 'ARG', 6.0), ('CE1', 'TYR', 'CD', 'ARG', 5.53), ('CE1', 'TYR', 'NE', 'ARG', 5.55), ('CE1', 'TYR', 'CZ', 'ARG', 6.03), ('CE1', 'TYR', 'NH1', 'ARG', 6.48), ('CE1', 'TYR', 'NH2', 'ARG', 6.65)], [('CE2', 'TYR', 'CB', 'ARG', 8.52), ('CE2', 'TYR', 'CG', 'ARG', 7.4), ('CE2', 'TYR', 'CD', 'ARG', 6.41), ('CE2', 'TYR', 'NE', 'ARG', 5.73), ('CE2', 'TYR', 'CZ', 'ARG', 5.39), ('CE2', 'TYR', 'NH1', 'ARG', 5.74), ('CE2', 'TYR', 'NH2', 'ARG', 5.49)], [('CZ', 'TYR', 'CB', 'ARG', 7.71), ('CZ', 'TYR', 'CG', 'ARG', 6.55), ('CZ', 'TYR', 'CD', 'ARG', 5.89), ('CZ', 'TYR', 'NE', 'ARG', 5.35), ('CZ', 'TYR', 'CZ', 'ARG', 5.53), ('CZ', 'TYR', 'NH1', 'ARG', 6.17), ('CZ', 'TYR', 'NH2', 'ARG', 5.78)], [('OH', 'TYR', 'CB', 'ARG', 7.68), ('OH', 'TYR', 'CG', 'ARG', 6.75), ('OH', 'TYR', 'CD', 'ARG', 6.38), ('OH', 'TYR', 'NE', 'ARG', 5.58), ('OH', 'TYR', 'CZ', 'ARG', 5.88), ('OH', 'TYR', 'NH1', 'ARG', 6.83), ('OH', 'TYR', 'NH2', 'ARG', 5.79)]]}
ASP_ASP = { 
	'distances':
		[[7.17, 6.35, 7.17, 5.19], [6.71, 6.31, 7.38, 5.27], [5.55, 5.39, 6.56, 4.54], [7.76, 7.52, 8.62, 6.5], [7.17, 6.71, 5.55, 7.76], [6.35, 6.31, 5.39, 7.52], [7.17, 7.38, 6.56, 8.62], [5.19, 5.27, 4.54, 6.5]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 7.17), ('CB', 'ASP', 'CG', 'ASP', 6.35), ('CB', 'ASP', 'OD1', 'ASP', 7.17), ('CB', 'ASP', 'OD2', 'ASP', 5.19)], [('CG', 'ASP', 'CB', 'ASP', 6.71), ('CG', 'ASP', 'CG', 'ASP', 6.31), ('CG', 'ASP', 'OD1', 'ASP', 7.38), ('CG', 'ASP', 'OD2', 'ASP', 5.27)], [('OD1', 'ASP', 'CB', 'ASP', 5.55), ('OD1', 'ASP', 'CG', 'ASP', 5.39), ('OD1', 'ASP', 'OD1', 'ASP', 6.56), ('OD1', 'ASP', 'OD2', 'ASP', 4.54)], [('OD2', 'ASP', 'CB', 'ASP', 7.76), ('OD2', 'ASP', 'CG', 'ASP', 7.52), ('OD2', 'ASP', 'OD1', 'ASP', 8.62), ('OD2', 'ASP', 'OD2', 'ASP', 6.5)], [('CB', 'ASP', 'CB', 'ASP', 7.17), ('CB', 'ASP', 'CG', 'ASP', 6.71), ('CB', 'ASP', 'OD1', 'ASP', 5.55), ('CB', 'ASP', 'OD2', 'ASP', 7.76)], [('CG', 'ASP', 'CB', 'ASP', 6.35), ('CG', 'ASP', 'CG', 'ASP', 6.31), ('CG', 'ASP', 'OD1', 'ASP', 5.39), ('CG', 'ASP', 'OD2', 'ASP', 7.52)], [('OD1', 'ASP', 'CB', 'ASP', 7.17), ('OD1', 'ASP', 'CG', 'ASP', 7.38), ('OD1', 'ASP', 'OD1', 'ASP', 6.56), ('OD1', 'ASP', 'OD2', 'ASP', 8.62)], [('OD2', 'ASP', 'CB', 'ASP', 5.19), ('OD2', 'ASP', 'CG', 'ASP', 5.27), ('OD2', 'ASP', 'OD1', 'ASP', 4.54), ('OD2', 'ASP', 'OD2', 'ASP', 6.5)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'P_1oc6_3_2_1_91')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_ASP, d, 'P_1oc6_3_2_1_91')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_ARG, d, 'P_1oc6_3_2_1_91')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_ASP, d, 'P_1oc6_3_2_1_91')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'ARG_ASP' :  match2,
		'TYR_ARG' :  match3,
		'ASP_ASP' :  match4}