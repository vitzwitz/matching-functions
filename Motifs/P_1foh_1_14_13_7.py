'''
FUNC:P_1foh_1_14_13_7
PDB:1foh
EC:1.14.13.7
RESI:asp,arg,tyr
LOCI:a-54,281,289;
'''
import motifFunctions as cmd
ASP_ARG = { 
	'distances':
		[[7.56, 6.34, 5.02, 5.14, 5.1, 4.71, 5.91], [7.4, 6.0, 4.98, 5.52, 5.49, 4.74, 6.53], [8.34, 6.9, 5.96, 6.67, 6.72, 5.95, 7.78], [6.57, 5.11, 4.38, 5.02, 4.88, 3.91, 6.01]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 7.56), ('CB', 'ASP', 'CG', 'ARG', 6.34), ('CB', 'ASP', 'CD', 'ARG', 5.02), ('CB', 'ASP', 'NE', 'ARG', 5.14), ('CB', 'ASP', 'CZ', 'ARG', 5.1), ('CB', 'ASP', 'NH1', 'ARG', 4.71), ('CB', 'ASP', 'NH2', 'ARG', 5.91)], [('CG', 'ASP', 'CB', 'ARG', 7.4), ('CG', 'ASP', 'CG', 'ARG', 6.0), ('CG', 'ASP', 'CD', 'ARG', 4.98), ('CG', 'ASP', 'NE', 'ARG', 5.52), ('CG', 'ASP', 'CZ', 'ARG', 5.49), ('CG', 'ASP', 'NH1', 'ARG', 4.74), ('CG', 'ASP', 'NH2', 'ARG', 6.53)], [('OD1', 'ASP', 'CB', 'ARG', 8.34), ('OD1', 'ASP', 'CG', 'ARG', 6.9), ('OD1', 'ASP', 'CD', 'ARG', 5.96), ('OD1', 'ASP', 'NE', 'ARG', 6.67), ('OD1', 'ASP', 'CZ', 'ARG', 6.72), ('OD1', 'ASP', 'NH1', 'ARG', 5.95), ('OD1', 'ASP', 'NH2', 'ARG', 7.78)], [('OD2', 'ASP', 'CB', 'ARG', 6.57), ('OD2', 'ASP', 'CG', 'ARG', 5.11), ('OD2', 'ASP', 'CD', 'ARG', 4.38), ('OD2', 'ASP', 'NE', 'ARG', 5.02), ('OD2', 'ASP', 'CZ', 'ARG', 4.88), ('OD2', 'ASP', 'NH1', 'ARG', 3.91), ('OD2', 'ASP', 'NH2', 'ARG', 6.01)]]}
ARG_TYR = { 
	'distances':
		[[13.16, 12.31, 11.12, 12.86, 10.49, 12.32, 11.15, 10.81], [11.92, 10.99, 9.78, 11.48, 9.07, 10.89, 9.69, 9.32], [12.35, 11.25, 10.06, 11.57, 9.15, 10.79, 9.57, 8.96], [13.21, 12.09, 10.99, 12.3, 10.06, 11.47, 10.33, 9.65], [12.79, 11.68, 10.68, 11.79, 9.77, 10.97, 9.93, 9.28], [11.49, 10.36, 9.4, 10.46, 8.51, 9.66, 8.66, 8.06], [13.72, 12.62, 11.7, 12.66, 10.81, 11.83, 10.88, 10.21]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 13.16), ('CB', 'ARG', 'CG', 'TYR', 12.31), ('CB', 'ARG', 'CD1', 'TYR', 11.12), ('CB', 'ARG', 'CD2', 'TYR', 12.86), ('CB', 'ARG', 'CE1', 'TYR', 10.49), ('CB', 'ARG', 'CE2', 'TYR', 12.32), ('CB', 'ARG', 'CZ', 'TYR', 11.15), ('CB', 'ARG', 'OH', 'TYR', 10.81)], [('CG', 'ARG', 'CB', 'TYR', 11.92), ('CG', 'ARG', 'CG', 'TYR', 10.99), ('CG', 'ARG', 'CD1', 'TYR', 9.78), ('CG', 'ARG', 'CD2', 'TYR', 11.48), ('CG', 'ARG', 'CE1', 'TYR', 9.07), ('CG', 'ARG', 'CE2', 'TYR', 10.89), ('CG', 'ARG', 'CZ', 'TYR', 9.69), ('CG', 'ARG', 'OH', 'TYR', 9.32)], [('CD', 'ARG', 'CB', 'TYR', 12.35), ('CD', 'ARG', 'CG', 'TYR', 11.25), ('CD', 'ARG', 'CD1', 'TYR', 10.06), ('CD', 'ARG', 'CD2', 'TYR', 11.57), ('CD', 'ARG', 'CE1', 'TYR', 9.15), ('CD', 'ARG', 'CE2', 'TYR', 10.79), ('CD', 'ARG', 'CZ', 'TYR', 9.57), ('CD', 'ARG', 'OH', 'TYR', 8.96)], [('NE', 'ARG', 'CB', 'TYR', 13.21), ('NE', 'ARG', 'CG', 'TYR', 12.09), ('NE', 'ARG', 'CD1', 'TYR', 10.99), ('NE', 'ARG', 'CD2', 'TYR', 12.3), ('NE', 'ARG', 'CE1', 'TYR', 10.06), ('NE', 'ARG', 'CE2', 'TYR', 11.47), ('NE', 'ARG', 'CZ', 'TYR', 10.33), ('NE', 'ARG', 'OH', 'TYR', 9.65)], [('CZ', 'ARG', 'CB', 'TYR', 12.79), ('CZ', 'ARG', 'CG', 'TYR', 11.68), ('CZ', 'ARG', 'CD1', 'TYR', 10.68), ('CZ', 'ARG', 'CD2', 'TYR', 11.79), ('CZ', 'ARG', 'CE1', 'TYR', 9.77), ('CZ', 'ARG', 'CE2', 'TYR', 10.97), ('CZ', 'ARG', 'CZ', 'TYR', 9.93), ('CZ', 'ARG', 'OH', 'TYR', 9.28)], [('NH1', 'ARG', 'CB', 'TYR', 11.49), ('NH1', 'ARG', 'CG', 'TYR', 10.36), ('NH1', 'ARG', 'CD1', 'TYR', 9.4), ('NH1', 'ARG', 'CD2', 'TYR', 10.46), ('NH1', 'ARG', 'CE1', 'TYR', 8.51), ('NH1', 'ARG', 'CE2', 'TYR', 9.66), ('NH1', 'ARG', 'CZ', 'TYR', 8.66), ('NH1', 'ARG', 'OH', 'TYR', 8.06)], [('NH2', 'ARG', 'CB', 'TYR', 13.72), ('NH2', 'ARG', 'CG', 'TYR', 12.62), ('NH2', 'ARG', 'CD1', 'TYR', 11.7), ('NH2', 'ARG', 'CD2', 'TYR', 12.66), ('NH2', 'ARG', 'CE1', 'TYR', 10.81), ('NH2', 'ARG', 'CE2', 'TYR', 11.83), ('NH2', 'ARG', 'CZ', 'TYR', 10.88), ('NH2', 'ARG', 'OH', 'TYR', 10.21)]]}
ASP_TYR = { 
	'distances':
		[[11.87, 10.47, 9.5, 10.28, 8.23, 9.12, 8.01, 6.89], [10.47, 9.09, 8.06, 8.98, 6.8, 7.89, 6.69, 5.66], [10.08, 8.66, 7.64, 8.52, 6.31, 7.38, 6.15, 5.04], [9.88, 8.57, 7.51, 8.62, 6.36, 7.66, 6.46, 5.67]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 11.87), ('CB', 'ASP', 'CG', 'TYR', 10.47), ('CB', 'ASP', 'CD1', 'TYR', 9.5), ('CB', 'ASP', 'CD2', 'TYR', 10.28), ('CB', 'ASP', 'CE1', 'TYR', 8.23), ('CB', 'ASP', 'CE2', 'TYR', 9.12), ('CB', 'ASP', 'CZ', 'TYR', 8.01), ('CB', 'ASP', 'OH', 'TYR', 6.89)], [('CG', 'ASP', 'CB', 'TYR', 10.47), ('CG', 'ASP', 'CG', 'TYR', 9.09), ('CG', 'ASP', 'CD1', 'TYR', 8.06), ('CG', 'ASP', 'CD2', 'TYR', 8.98), ('CG', 'ASP', 'CE1', 'TYR', 6.8), ('CG', 'ASP', 'CE2', 'TYR', 7.89), ('CG', 'ASP', 'CZ', 'TYR', 6.69), ('CG', 'ASP', 'OH', 'TYR', 5.66)], [('OD1', 'ASP', 'CB', 'TYR', 10.08), ('OD1', 'ASP', 'CG', 'TYR', 8.66), ('OD1', 'ASP', 'CD1', 'TYR', 7.64), ('OD1', 'ASP', 'CD2', 'TYR', 8.52), ('OD1', 'ASP', 'CE1', 'TYR', 6.31), ('OD1', 'ASP', 'CE2', 'TYR', 7.38), ('OD1', 'ASP', 'CZ', 'TYR', 6.15), ('OD1', 'ASP', 'OH', 'TYR', 5.04)], [('OD2', 'ASP', 'CB', 'TYR', 9.88), ('OD2', 'ASP', 'CG', 'TYR', 8.57), ('OD2', 'ASP', 'CD1', 'TYR', 7.51), ('OD2', 'ASP', 'CD2', 'TYR', 8.62), ('OD2', 'ASP', 'CE1', 'TYR', 6.36), ('OD2', 'ASP', 'CE2', 'TYR', 7.66), ('OD2', 'ASP', 'CZ', 'TYR', 6.46), ('OD2', 'ASP', 'OH', 'TYR', 5.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ARG, d, 'P_1foh_1_14_13_7')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_TYR, d, 'P_1foh_1_14_13_7')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_TYR, d, 'P_1foh_1_14_13_7')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ARG' :  match1,
		'ARG_TYR' :  match2,
		'ASP_TYR' :  match3}