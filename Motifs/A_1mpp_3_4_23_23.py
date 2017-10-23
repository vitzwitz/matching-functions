'''
FUNC:A_1mpp_3_4_23_23
PDB:1mpp
EC:3.4.23.23
RESI:asp,ser,tyr,asp
LOCI:a-32,35,75,215;
'''
import motifFunctions as cmd
SER_TYR = { 
	'distances':
		[[9.11, 8.1, 6.71, 8.77, 6.01, 8.24, 7.01, 6.98], [9.22, 8.08, 6.75, 8.6, 5.87, 7.93, 6.67, 6.47]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'TYR', 9.11), ('CB', 'SER', 'CG', 'TYR', 8.1), ('CB', 'SER', 'CD1', 'TYR', 6.71), ('CB', 'SER', 'CD2', 'TYR', 8.77), ('CB', 'SER', 'CE1', 'TYR', 6.01), ('CB', 'SER', 'CE2', 'TYR', 8.24), ('CB', 'SER', 'CZ', 'TYR', 7.01), ('CB', 'SER', 'OH', 'TYR', 6.98)], [('OG', 'SER', 'CB', 'TYR', 9.22), ('OG', 'SER', 'CG', 'TYR', 8.08), ('OG', 'SER', 'CD1', 'TYR', 6.75), ('OG', 'SER', 'CD2', 'TYR', 8.6), ('OG', 'SER', 'CE1', 'TYR', 5.87), ('OG', 'SER', 'CE2', 'TYR', 7.93), ('OG', 'SER', 'CZ', 'TYR', 6.67), ('OG', 'SER', 'OH', 'TYR', 6.47)]]}
ASP_ASP = { 
	'distances':
		[[9.69, 8.51, 7.35, 9.04], [8.8, 7.47, 6.42, 7.83], [7.54, 6.25, 5.18, 6.71], [9.48, 8.05, 7.14, 8.18], [9.69, 8.8, 7.54, 9.48], [8.51, 7.47, 6.25, 8.05], [7.35, 6.42, 5.18, 7.14], [9.04, 7.83, 6.71, 8.18]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 9.69), ('CB', 'ASP', 'CG', 'ASP', 8.51), ('CB', 'ASP', 'OD1', 'ASP', 7.35), ('CB', 'ASP', 'OD2', 'ASP', 9.04)], [('CG', 'ASP', 'CB', 'ASP', 8.8), ('CG', 'ASP', 'CG', 'ASP', 7.47), ('CG', 'ASP', 'OD1', 'ASP', 6.42), ('CG', 'ASP', 'OD2', 'ASP', 7.83)], [('OD1', 'ASP', 'CB', 'ASP', 7.54), ('OD1', 'ASP', 'CG', 'ASP', 6.25), ('OD1', 'ASP', 'OD1', 'ASP', 5.18), ('OD1', 'ASP', 'OD2', 'ASP', 6.71)], [('OD2', 'ASP', 'CB', 'ASP', 9.48), ('OD2', 'ASP', 'CG', 'ASP', 8.05), ('OD2', 'ASP', 'OD1', 'ASP', 7.14), ('OD2', 'ASP', 'OD2', 'ASP', 8.18)], [('CB', 'ASP', 'CB', 'ASP', 9.69), ('CB', 'ASP', 'CG', 'ASP', 8.8), ('CB', 'ASP', 'OD1', 'ASP', 7.54), ('CB', 'ASP', 'OD2', 'ASP', 9.48)], [('CG', 'ASP', 'CB', 'ASP', 8.51), ('CG', 'ASP', 'CG', 'ASP', 7.47), ('CG', 'ASP', 'OD1', 'ASP', 6.25), ('CG', 'ASP', 'OD2', 'ASP', 8.05)], [('OD1', 'ASP', 'CB', 'ASP', 7.35), ('OD1', 'ASP', 'CG', 'ASP', 6.42), ('OD1', 'ASP', 'OD1', 'ASP', 5.18), ('OD1', 'ASP', 'OD2', 'ASP', 7.14)], [('OD2', 'ASP', 'CB', 'ASP', 9.04), ('OD2', 'ASP', 'CG', 'ASP', 7.83), ('OD2', 'ASP', 'OD1', 'ASP', 6.71), ('OD2', 'ASP', 'OD2', 'ASP', 8.18)]]}
ASP_TYR = { 
	'distances':
		[[11.11, 10.21, 9.14, 10.72, 8.56, 10.19, 9.18, 9.03], [9.96, 9.19, 8.09, 9.9, 7.74, 9.55, 8.6, 8.71], [10.36, 9.79, 8.69, 10.65, 8.55, 10.44, 9.54, 9.79], [8.84, 8.0, 6.9, 8.69, 6.55, 8.35, 7.41, 7.64], [13.32, 13.42, 12.55, 14.63, 12.98, 14.89, 14.22, 14.81], [11.87, 11.92, 11.06, 13.11, 11.49, 13.37, 12.72, 13.33], [11.71, 11.6, 10.66, 12.7, 10.94, 12.82, 12.1, 12.6], [11.07, 11.28, 10.52, 12.53, 11.13, 12.92, 12.39, 13.13]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 11.11), ('CB', 'ASP', 'CG', 'TYR', 10.21), ('CB', 'ASP', 'CD1', 'TYR', 9.14), ('CB', 'ASP', 'CD2', 'TYR', 10.72), ('CB', 'ASP', 'CE1', 'TYR', 8.56), ('CB', 'ASP', 'CE2', 'TYR', 10.19), ('CB', 'ASP', 'CZ', 'TYR', 9.18), ('CB', 'ASP', 'OH', 'TYR', 9.03)], [('CG', 'ASP', 'CB', 'TYR', 9.96), ('CG', 'ASP', 'CG', 'TYR', 9.19), ('CG', 'ASP', 'CD1', 'TYR', 8.09), ('CG', 'ASP', 'CD2', 'TYR', 9.9), ('CG', 'ASP', 'CE1', 'TYR', 7.74), ('CG', 'ASP', 'CE2', 'TYR', 9.55), ('CG', 'ASP', 'CZ', 'TYR', 8.6), ('CG', 'ASP', 'OH', 'TYR', 8.71)], [('OD1', 'ASP', 'CB', 'TYR', 10.36), ('OD1', 'ASP', 'CG', 'TYR', 9.79), ('OD1', 'ASP', 'CD1', 'TYR', 8.69), ('OD1', 'ASP', 'CD2', 'TYR', 10.65), ('OD1', 'ASP', 'CE1', 'TYR', 8.55), ('OD1', 'ASP', 'CE2', 'TYR', 10.44), ('OD1', 'ASP', 'CZ', 'TYR', 9.54), ('OD1', 'ASP', 'OH', 'TYR', 9.79)], [('OD2', 'ASP', 'CB', 'TYR', 8.84), ('OD2', 'ASP', 'CG', 'TYR', 8.0), ('OD2', 'ASP', 'CD1', 'TYR', 6.9), ('OD2', 'ASP', 'CD2', 'TYR', 8.69), ('OD2', 'ASP', 'CE1', 'TYR', 6.55), ('OD2', 'ASP', 'CE2', 'TYR', 8.35), ('OD2', 'ASP', 'CZ', 'TYR', 7.41), ('OD2', 'ASP', 'OH', 'TYR', 7.64)], [('CB', 'ASP', 'CB', 'TYR', 13.32), ('CB', 'ASP', 'CG', 'TYR', 13.42), ('CB', 'ASP', 'CD1', 'TYR', 12.55), ('CB', 'ASP', 'CD2', 'TYR', 14.63), ('CB', 'ASP', 'CE1', 'TYR', 12.98), ('CB', 'ASP', 'CE2', 'TYR', 14.89), ('CB', 'ASP', 'CZ', 'TYR', 14.22), ('CB', 'ASP', 'OH', 'TYR', 14.81)], [('CG', 'ASP', 'CB', 'TYR', 11.87), ('CG', 'ASP', 'CG', 'TYR', 11.92), ('CG', 'ASP', 'CD1', 'TYR', 11.06), ('CG', 'ASP', 'CD2', 'TYR', 13.11), ('CG', 'ASP', 'CE1', 'TYR', 11.49), ('CG', 'ASP', 'CE2', 'TYR', 13.37), ('CG', 'ASP', 'CZ', 'TYR', 12.72), ('CG', 'ASP', 'OH', 'TYR', 13.33)], [('OD1', 'ASP', 'CB', 'TYR', 11.71), ('OD1', 'ASP', 'CG', 'TYR', 11.6), ('OD1', 'ASP', 'CD1', 'TYR', 10.66), ('OD1', 'ASP', 'CD2', 'TYR', 12.7), ('OD1', 'ASP', 'CE1', 'TYR', 10.94), ('OD1', 'ASP', 'CE2', 'TYR', 12.82), ('OD1', 'ASP', 'CZ', 'TYR', 12.1), ('OD1', 'ASP', 'OH', 'TYR', 12.6)], [('OD2', 'ASP', 'CB', 'TYR', 11.07), ('OD2', 'ASP', 'CG', 'TYR', 11.28), ('OD2', 'ASP', 'CD1', 'TYR', 10.52), ('OD2', 'ASP', 'CD2', 'TYR', 12.53), ('OD2', 'ASP', 'CE1', 'TYR', 11.13), ('OD2', 'ASP', 'CE2', 'TYR', 12.92), ('OD2', 'ASP', 'CZ', 'TYR', 12.39), ('OD2', 'ASP', 'OH', 'TYR', 13.13)]]}
ASP_SER = { 
	'distances':
		[[6.98, 5.79], [6.24, 5.29], [6.78, 6.14], [5.65, 4.67], [11.12, 11.14], [9.87, 9.83], [9.2, 8.99], [9.89, 9.95]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 6.98), ('CB', 'ASP', 'OG', 'SER', 5.79)], [('CG', 'ASP', 'CB', 'SER', 6.24), ('CG', 'ASP', 'OG', 'SER', 5.29)], [('OD1', 'ASP', 'CB', 'SER', 6.78), ('OD1', 'ASP', 'OG', 'SER', 6.14)], [('OD2', 'ASP', 'CB', 'SER', 5.65), ('OD2', 'ASP', 'OG', 'SER', 4.67)], [('CB', 'ASP', 'CB', 'SER', 11.12), ('CB', 'ASP', 'OG', 'SER', 11.14)], [('CG', 'ASP', 'CB', 'SER', 9.87), ('CG', 'ASP', 'OG', 'SER', 9.83)], [('OD1', 'ASP', 'CB', 'SER', 9.2), ('OD1', 'ASP', 'OG', 'SER', 8.99)], [('OD2', 'ASP', 'CB', 'SER', 9.89), ('OD2', 'ASP', 'OG', 'SER', 9.95)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(SER_TYR, d, 'A_1mpp_3_4_23_23')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_ASP, d, 'A_1mpp_3_4_23_23')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TYR, d, 'A_1mpp_3_4_23_23')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_SER, d, 'A_1mpp_3_4_23_23')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'SER_TYR' :  match1,
		'ASP_ASP' :  match2,
		'ASP_TYR' :  match3,
		'ASP_SER' :  match4}