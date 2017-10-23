'''
FUNC:A_1d2t_3_1_3_2
PDB:1d2t
EC:3.1.3.2
RESI:his,arg,his,asp
LOCI:a-150,183,189,193;
'''
import motifFunctions as cmd
ARG_HIS = { 
	'distances':
		[[6.17, 6.58, 7.91, 6.13, 8.34, 7.38], [7.34, 7.39, 8.63, 6.56, 8.76, 7.6], [8.14, 8.06, 9.24, 7.12, 9.23, 8.01], [9.53, 9.35, 10.48, 8.29, 10.32, 9.03], [10.26, 9.86, 10.86, 8.67, 10.5, 9.17], [9.85, 9.25, 10.12, 7.99, 9.63, 8.31], [11.55, 11.15, 12.14, 9.94, 11.74, 10.39], [7.94, 7.92, 9.05, 7.16, 9.12, 8.04], [6.74, 6.5, 7.56, 5.72, 7.6, 6.57], [6.97, 6.63, 7.45, 6.06, 7.47, 6.68], [6.67, 5.95, 6.46, 5.37, 6.29, 5.63], [6.26, 5.57, 5.81, 5.44, 5.83, 5.61], [5.91, 5.69, 6.05, 5.95, 6.48, 6.42], [6.79, 5.81, 5.57, 5.71, 5.31, 5.4]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 6.17), ('CB', 'ARG', 'CG', 'HIS', 6.58), ('CB', 'ARG', 'ND1', 'HIS', 7.91), ('CB', 'ARG', 'CD2', 'HIS', 6.13), ('CB', 'ARG', 'CE1', 'HIS', 8.34), ('CB', 'ARG', 'NE2', 'HIS', 7.38)], [('CG', 'ARG', 'CB', 'HIS', 7.34), ('CG', 'ARG', 'CG', 'HIS', 7.39), ('CG', 'ARG', 'ND1', 'HIS', 8.63), ('CG', 'ARG', 'CD2', 'HIS', 6.56), ('CG', 'ARG', 'CE1', 'HIS', 8.76), ('CG', 'ARG', 'NE2', 'HIS', 7.6)], [('CD', 'ARG', 'CB', 'HIS', 8.14), ('CD', 'ARG', 'CG', 'HIS', 8.06), ('CD', 'ARG', 'ND1', 'HIS', 9.24), ('CD', 'ARG', 'CD2', 'HIS', 7.12), ('CD', 'ARG', 'CE1', 'HIS', 9.23), ('CD', 'ARG', 'NE2', 'HIS', 8.01)], [('NE', 'ARG', 'CB', 'HIS', 9.53), ('NE', 'ARG', 'CG', 'HIS', 9.35), ('NE', 'ARG', 'ND1', 'HIS', 10.48), ('NE', 'ARG', 'CD2', 'HIS', 8.29), ('NE', 'ARG', 'CE1', 'HIS', 10.32), ('NE', 'ARG', 'NE2', 'HIS', 9.03)], [('CZ', 'ARG', 'CB', 'HIS', 10.26), ('CZ', 'ARG', 'CG', 'HIS', 9.86), ('CZ', 'ARG', 'ND1', 'HIS', 10.86), ('CZ', 'ARG', 'CD2', 'HIS', 8.67), ('CZ', 'ARG', 'CE1', 'HIS', 10.5), ('CZ', 'ARG', 'NE2', 'HIS', 9.17)], [('NH1', 'ARG', 'CB', 'HIS', 9.85), ('NH1', 'ARG', 'CG', 'HIS', 9.25), ('NH1', 'ARG', 'ND1', 'HIS', 10.12), ('NH1', 'ARG', 'CD2', 'HIS', 7.99), ('NH1', 'ARG', 'CE1', 'HIS', 9.63), ('NH1', 'ARG', 'NE2', 'HIS', 8.31)], [('NH2', 'ARG', 'CB', 'HIS', 11.55), ('NH2', 'ARG', 'CG', 'HIS', 11.15), ('NH2', 'ARG', 'ND1', 'HIS', 12.14), ('NH2', 'ARG', 'CD2', 'HIS', 9.94), ('NH2', 'ARG', 'CE1', 'HIS', 11.74), ('NH2', 'ARG', 'NE2', 'HIS', 10.39)], [('CB', 'ARG', 'CB', 'HIS', 7.94), ('CB', 'ARG', 'CG', 'HIS', 7.92), ('CB', 'ARG', 'ND1', 'HIS', 9.05), ('CB', 'ARG', 'CD2', 'HIS', 7.16), ('CB', 'ARG', 'CE1', 'HIS', 9.12), ('CB', 'ARG', 'NE2', 'HIS', 8.04)], [('CG', 'ARG', 'CB', 'HIS', 6.74), ('CG', 'ARG', 'CG', 'HIS', 6.5), ('CG', 'ARG', 'ND1', 'HIS', 7.56), ('CG', 'ARG', 'CD2', 'HIS', 5.72), ('CG', 'ARG', 'CE1', 'HIS', 7.6), ('CG', 'ARG', 'NE2', 'HIS', 6.57)], [('CD', 'ARG', 'CB', 'HIS', 6.97), ('CD', 'ARG', 'CG', 'HIS', 6.63), ('CD', 'ARG', 'ND1', 'HIS', 7.45), ('CD', 'ARG', 'CD2', 'HIS', 6.06), ('CD', 'ARG', 'CE1', 'HIS', 7.47), ('CD', 'ARG', 'NE2', 'HIS', 6.68)], [('NE', 'ARG', 'CB', 'HIS', 6.67), ('NE', 'ARG', 'CG', 'HIS', 5.95), ('NE', 'ARG', 'ND1', 'HIS', 6.46), ('NE', 'ARG', 'CD2', 'HIS', 5.37), ('NE', 'ARG', 'CE1', 'HIS', 6.29), ('NE', 'ARG', 'NE2', 'HIS', 5.63)], [('CZ', 'ARG', 'CB', 'HIS', 6.26), ('CZ', 'ARG', 'CG', 'HIS', 5.57), ('CZ', 'ARG', 'ND1', 'HIS', 5.81), ('CZ', 'ARG', 'CD2', 'HIS', 5.44), ('CZ', 'ARG', 'CE1', 'HIS', 5.83), ('CZ', 'ARG', 'NE2', 'HIS', 5.61)], [('NH1', 'ARG', 'CB', 'HIS', 5.91), ('NH1', 'ARG', 'CG', 'HIS', 5.69), ('NH1', 'ARG', 'ND1', 'HIS', 6.05), ('NH1', 'ARG', 'CD2', 'HIS', 5.95), ('NH1', 'ARG', 'CE1', 'HIS', 6.48), ('NH1', 'ARG', 'NE2', 'HIS', 6.42)], [('NH2', 'ARG', 'CB', 'HIS', 6.79), ('NH2', 'ARG', 'CG', 'HIS', 5.81), ('NH2', 'ARG', 'ND1', 'HIS', 5.57), ('NH2', 'ARG', 'CD2', 'HIS', 5.71), ('NH2', 'ARG', 'CE1', 'HIS', 5.31), ('NH2', 'ARG', 'NE2', 'HIS', 5.4)]]}
HIS_ASP = { 
	'distances':
		[[6.18, 6.52, 7.75, 5.81], [6.09, 6.44, 7.62, 5.82], [5.56, 5.64, 6.7, 5.06], [7.12, 7.62, 8.76, 7.11], [6.41, 6.55, 7.46, 6.14], [7.25, 7.64, 8.64, 7.22], [11.62, 12.59, 13.62, 12.44], [12.66, 13.67, 14.75, 13.48], [14.0, 15.0, 16.07, 14.8], [12.59, 13.65, 14.78, 13.44], [14.72, 15.75, 16.86, 15.52], [13.91, 14.98, 16.12, 14.74]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 6.18), ('CB', 'HIS', 'CG', 'ASP', 6.52), ('CB', 'HIS', 'OD1', 'ASP', 7.75), ('CB', 'HIS', 'OD2', 'ASP', 5.81)], [('CG', 'HIS', 'CB', 'ASP', 6.09), ('CG', 'HIS', 'CG', 'ASP', 6.44), ('CG', 'HIS', 'OD1', 'ASP', 7.62), ('CG', 'HIS', 'OD2', 'ASP', 5.82)], [('ND1', 'HIS', 'CB', 'ASP', 5.56), ('ND1', 'HIS', 'CG', 'ASP', 5.64), ('ND1', 'HIS', 'OD1', 'ASP', 6.7), ('ND1', 'HIS', 'OD2', 'ASP', 5.06)], [('CD2', 'HIS', 'CB', 'ASP', 7.12), ('CD2', 'HIS', 'CG', 'ASP', 7.62), ('CD2', 'HIS', 'OD1', 'ASP', 8.76), ('CD2', 'HIS', 'OD2', 'ASP', 7.11)], [('CE1', 'HIS', 'CB', 'ASP', 6.41), ('CE1', 'HIS', 'CG', 'ASP', 6.55), ('CE1', 'HIS', 'OD1', 'ASP', 7.46), ('CE1', 'HIS', 'OD2', 'ASP', 6.14)], [('NE2', 'HIS', 'CB', 'ASP', 7.25), ('NE2', 'HIS', 'CG', 'ASP', 7.64), ('NE2', 'HIS', 'OD1', 'ASP', 8.64), ('NE2', 'HIS', 'OD2', 'ASP', 7.22)], [('CB', 'HIS', 'CB', 'ASP', 11.62), ('CB', 'HIS', 'CG', 'ASP', 12.59), ('CB', 'HIS', 'OD1', 'ASP', 13.62), ('CB', 'HIS', 'OD2', 'ASP', 12.44)], [('CG', 'HIS', 'CB', 'ASP', 12.66), ('CG', 'HIS', 'CG', 'ASP', 13.67), ('CG', 'HIS', 'OD1', 'ASP', 14.75), ('CG', 'HIS', 'OD2', 'ASP', 13.48)], [('ND1', 'HIS', 'CB', 'ASP', 14.0), ('ND1', 'HIS', 'CG', 'ASP', 15.0), ('ND1', 'HIS', 'OD1', 'ASP', 16.07), ('ND1', 'HIS', 'OD2', 'ASP', 14.8)], [('CD2', 'HIS', 'CB', 'ASP', 12.59), ('CD2', 'HIS', 'CG', 'ASP', 13.65), ('CD2', 'HIS', 'OD1', 'ASP', 14.78), ('CD2', 'HIS', 'OD2', 'ASP', 13.44)], [('CE1', 'HIS', 'CB', 'ASP', 14.72), ('CE1', 'HIS', 'CG', 'ASP', 15.75), ('CE1', 'HIS', 'OD1', 'ASP', 16.86), ('CE1', 'HIS', 'OD2', 'ASP', 15.52)], [('NE2', 'HIS', 'CB', 'ASP', 13.91), ('NE2', 'HIS', 'CG', 'ASP', 14.98), ('NE2', 'HIS', 'OD1', 'ASP', 16.12), ('NE2', 'HIS', 'OD2', 'ASP', 14.74)]]}
HIS_HIS = { 
	'distances':
		[[9.84, 10.55, 11.85, 10.26, 12.36, 11.46], [8.98, 9.9, 11.19, 9.85, 11.87, 11.13], [9.62, 10.71, 11.98, 10.82, 12.78, 12.13], [7.67, 8.63, 9.89, 8.7, 10.64, 9.98], [8.93, 10.16, 11.37, 10.48, 12.3, 11.8], [7.67, 8.86, 10.06, 9.19, 10.98, 10.5], [9.84, 8.98, 9.62, 7.67, 8.93, 7.67], [10.55, 9.9, 10.71, 8.63, 10.16, 8.86], [11.85, 11.19, 11.98, 9.89, 11.37, 10.06], [10.26, 9.85, 10.82, 8.7, 10.48, 9.19], [12.36, 11.87, 12.78, 10.64, 12.3, 10.98], [11.46, 11.13, 12.13, 9.98, 11.8, 10.5]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'HIS', 9.84), ('CB', 'HIS', 'CG', 'HIS', 10.55), ('CB', 'HIS', 'ND1', 'HIS', 11.85), ('CB', 'HIS', 'CD2', 'HIS', 10.26), ('CB', 'HIS', 'CE1', 'HIS', 12.36), ('CB', 'HIS', 'NE2', 'HIS', 11.46)], [('CG', 'HIS', 'CB', 'HIS', 8.98), ('CG', 'HIS', 'CG', 'HIS', 9.9), ('CG', 'HIS', 'ND1', 'HIS', 11.19), ('CG', 'HIS', 'CD2', 'HIS', 9.85), ('CG', 'HIS', 'CE1', 'HIS', 11.87), ('CG', 'HIS', 'NE2', 'HIS', 11.13)], [('ND1', 'HIS', 'CB', 'HIS', 9.62), ('ND1', 'HIS', 'CG', 'HIS', 10.71), ('ND1', 'HIS', 'ND1', 'HIS', 11.98), ('ND1', 'HIS', 'CD2', 'HIS', 10.82), ('ND1', 'HIS', 'CE1', 'HIS', 12.78), ('ND1', 'HIS', 'NE2', 'HIS', 12.13)], [('CD2', 'HIS', 'CB', 'HIS', 7.67), ('CD2', 'HIS', 'CG', 'HIS', 8.63), ('CD2', 'HIS', 'ND1', 'HIS', 9.89), ('CD2', 'HIS', 'CD2', 'HIS', 8.7), ('CD2', 'HIS', 'CE1', 'HIS', 10.64), ('CD2', 'HIS', 'NE2', 'HIS', 9.98)], [('CE1', 'HIS', 'CB', 'HIS', 8.93), ('CE1', 'HIS', 'CG', 'HIS', 10.16), ('CE1', 'HIS', 'ND1', 'HIS', 11.37), ('CE1', 'HIS', 'CD2', 'HIS', 10.48), ('CE1', 'HIS', 'CE1', 'HIS', 12.3), ('CE1', 'HIS', 'NE2', 'HIS', 11.8)], [('NE2', 'HIS', 'CB', 'HIS', 7.67), ('NE2', 'HIS', 'CG', 'HIS', 8.86), ('NE2', 'HIS', 'ND1', 'HIS', 10.06), ('NE2', 'HIS', 'CD2', 'HIS', 9.19), ('NE2', 'HIS', 'CE1', 'HIS', 10.98), ('NE2', 'HIS', 'NE2', 'HIS', 10.5)], [('CB', 'HIS', 'CB', 'HIS', 9.84), ('CB', 'HIS', 'CG', 'HIS', 8.98), ('CB', 'HIS', 'ND1', 'HIS', 9.62), ('CB', 'HIS', 'CD2', 'HIS', 7.67), ('CB', 'HIS', 'CE1', 'HIS', 8.93), ('CB', 'HIS', 'NE2', 'HIS', 7.67)], [('CG', 'HIS', 'CB', 'HIS', 10.55), ('CG', 'HIS', 'CG', 'HIS', 9.9), ('CG', 'HIS', 'ND1', 'HIS', 10.71), ('CG', 'HIS', 'CD2', 'HIS', 8.63), ('CG', 'HIS', 'CE1', 'HIS', 10.16), ('CG', 'HIS', 'NE2', 'HIS', 8.86)], [('ND1', 'HIS', 'CB', 'HIS', 11.85), ('ND1', 'HIS', 'CG', 'HIS', 11.19), ('ND1', 'HIS', 'ND1', 'HIS', 11.98), ('ND1', 'HIS', 'CD2', 'HIS', 9.89), ('ND1', 'HIS', 'CE1', 'HIS', 11.37), ('ND1', 'HIS', 'NE2', 'HIS', 10.06)], [('CD2', 'HIS', 'CB', 'HIS', 10.26), ('CD2', 'HIS', 'CG', 'HIS', 9.85), ('CD2', 'HIS', 'ND1', 'HIS', 10.82), ('CD2', 'HIS', 'CD2', 'HIS', 8.7), ('CD2', 'HIS', 'CE1', 'HIS', 10.48), ('CD2', 'HIS', 'NE2', 'HIS', 9.19)], [('CE1', 'HIS', 'CB', 'HIS', 12.36), ('CE1', 'HIS', 'CG', 'HIS', 11.87), ('CE1', 'HIS', 'ND1', 'HIS', 12.78), ('CE1', 'HIS', 'CD2', 'HIS', 10.64), ('CE1', 'HIS', 'CE1', 'HIS', 12.3), ('CE1', 'HIS', 'NE2', 'HIS', 10.98)], [('NE2', 'HIS', 'CB', 'HIS', 11.46), ('NE2', 'HIS', 'CG', 'HIS', 11.13), ('NE2', 'HIS', 'ND1', 'HIS', 12.13), ('NE2', 'HIS', 'CD2', 'HIS', 9.98), ('NE2', 'HIS', 'CE1', 'HIS', 11.8), ('NE2', 'HIS', 'NE2', 'HIS', 10.5)]]}
ARG_ASP = { 
	'distances':
		[[9.77, 10.51, 11.75, 9.95], [10.68, 11.5, 12.72, 11.01], [11.73, 12.4, 13.62, 11.79], [12.94, 13.68, 14.89, 13.13], [13.51, 14.22, 15.39, 13.68], [12.98, 13.61, 14.74, 13.05], [14.73, 15.49, 16.65, 14.97]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 9.77), ('CB', 'ARG', 'CG', 'ASP', 10.51), ('CB', 'ARG', 'OD1', 'ASP', 11.75), ('CB', 'ARG', 'OD2', 'ASP', 9.95)], [('CG', 'ARG', 'CB', 'ASP', 10.68), ('CG', 'ARG', 'CG', 'ASP', 11.5), ('CG', 'ARG', 'OD1', 'ASP', 12.72), ('CG', 'ARG', 'OD2', 'ASP', 11.01)], [('CD', 'ARG', 'CB', 'ASP', 11.73), ('CD', 'ARG', 'CG', 'ASP', 12.4), ('CD', 'ARG', 'OD1', 'ASP', 13.62), ('CD', 'ARG', 'OD2', 'ASP', 11.79)], [('NE', 'ARG', 'CB', 'ASP', 12.94), ('NE', 'ARG', 'CG', 'ASP', 13.68), ('NE', 'ARG', 'OD1', 'ASP', 14.89), ('NE', 'ARG', 'OD2', 'ASP', 13.13)], [('CZ', 'ARG', 'CB', 'ASP', 13.51), ('CZ', 'ARG', 'CG', 'ASP', 14.22), ('CZ', 'ARG', 'OD1', 'ASP', 15.39), ('CZ', 'ARG', 'OD2', 'ASP', 13.68)], [('NH1', 'ARG', 'CB', 'ASP', 12.98), ('NH1', 'ARG', 'CG', 'ASP', 13.61), ('NH1', 'ARG', 'OD1', 'ASP', 14.74), ('NH1', 'ARG', 'OD2', 'ASP', 13.05)], [('NH2', 'ARG', 'CB', 'ASP', 14.73), ('NH2', 'ARG', 'CG', 'ASP', 15.49), ('NH2', 'ARG', 'OD1', 'ASP', 16.65), ('NH2', 'ARG', 'OD2', 'ASP', 14.97)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_HIS, d, 'A_1d2t_3_1_3_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1d2t_3_1_3_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_HIS, d, 'A_1d2t_3_1_3_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_ASP, d, 'A_1d2t_3_1_3_2')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_HIS' :  match1,
		'HIS_ASP' :  match2,
		'HIS_HIS' :  match3,
		'ARG_ASP' :  match4}