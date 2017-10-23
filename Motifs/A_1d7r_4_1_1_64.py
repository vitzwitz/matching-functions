'''
FUNC:A_1d7r_4_1_1_64
PDB:1d7r
EC:4.1.1.64
RESI:trp,asp,lys
LOCI:a-138,243,272;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[12.48, 11.79, 11.89, 11.9, 13.02], [11.19, 10.4, 10.51, 10.46, 11.61], [10.1, 9.42, 9.64, 9.75, 10.99], [11.45, 10.49, 10.5, 10.22, 11.29]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 12.48), ('CB', 'ASP', 'CG', 'LYS', 11.79), ('CB', 'ASP', 'CD', 'LYS', 11.89), ('CB', 'ASP', 'CE', 'LYS', 11.9), ('CB', 'ASP', 'NZ', 'LYS', 13.02)], [('CG', 'ASP', 'CB', 'LYS', 11.19), ('CG', 'ASP', 'CG', 'LYS', 10.4), ('CG', 'ASP', 'CD', 'LYS', 10.51), ('CG', 'ASP', 'CE', 'LYS', 10.46), ('CG', 'ASP', 'NZ', 'LYS', 11.61)], [('OD1', 'ASP', 'CB', 'LYS', 10.1), ('OD1', 'ASP', 'CG', 'LYS', 9.42), ('OD1', 'ASP', 'CD', 'LYS', 9.64), ('OD1', 'ASP', 'CE', 'LYS', 9.75), ('OD1', 'ASP', 'NZ', 'LYS', 10.99)], [('OD2', 'ASP', 'CB', 'LYS', 11.45), ('OD2', 'ASP', 'CG', 'LYS', 10.49), ('OD2', 'ASP', 'CD', 'LYS', 10.5), ('OD2', 'ASP', 'CE', 'LYS', 10.22), ('OD2', 'ASP', 'NZ', 'LYS', 11.29)]]}
ASP_TRP = { 
	'distances':
		[[10.66, 11.13, 10.55, 12.46, 11.55, 12.66, 13.61, 13.96, 14.79, 14.94], [9.85, 10.13, 9.4, 11.43, 10.31, 11.51, 12.67, 12.78, 13.79, 13.83], [10.41, 10.56, 9.71, 11.85, 10.54, 11.81, 13.14, 13.04, 14.22, 14.17], [8.8, 9.03, 8.31, 10.3, 9.22, 10.38, 11.51, 11.64, 12.62, 12.66]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TRP', 10.66), ('CB', 'ASP', 'CG', 'TRP', 11.13), ('CB', 'ASP', 'CD1', 'TRP', 10.55), ('CB', 'ASP', 'CD2', 'TRP', 12.46), ('CB', 'ASP', 'NE1', 'TRP', 11.55), ('CB', 'ASP', 'CE2', 'TRP', 12.66), ('CB', 'ASP', 'CE3', 'TRP', 13.61), ('CB', 'ASP', 'CZ2', 'TRP', 13.96), ('CB', 'ASP', 'CZ3', 'TRP', 14.79), ('CB', 'ASP', 'CH2', 'TRP', 14.94)], [('CG', 'ASP', 'CB', 'TRP', 9.85), ('CG', 'ASP', 'CG', 'TRP', 10.13), ('CG', 'ASP', 'CD1', 'TRP', 9.4), ('CG', 'ASP', 'CD2', 'TRP', 11.43), ('CG', 'ASP', 'NE1', 'TRP', 10.31), ('CG', 'ASP', 'CE2', 'TRP', 11.51), ('CG', 'ASP', 'CE3', 'TRP', 12.67), ('CG', 'ASP', 'CZ2', 'TRP', 12.78), ('CG', 'ASP', 'CZ3', 'TRP', 13.79), ('CG', 'ASP', 'CH2', 'TRP', 13.83)], [('OD1', 'ASP', 'CB', 'TRP', 10.41), ('OD1', 'ASP', 'CG', 'TRP', 10.56), ('OD1', 'ASP', 'CD1', 'TRP', 9.71), ('OD1', 'ASP', 'CD2', 'TRP', 11.85), ('OD1', 'ASP', 'NE1', 'TRP', 10.54), ('OD1', 'ASP', 'CE2', 'TRP', 11.81), ('OD1', 'ASP', 'CE3', 'TRP', 13.14), ('OD1', 'ASP', 'CZ2', 'TRP', 13.04), ('OD1', 'ASP', 'CZ3', 'TRP', 14.22), ('OD1', 'ASP', 'CH2', 'TRP', 14.17)], [('OD2', 'ASP', 'CB', 'TRP', 8.8), ('OD2', 'ASP', 'CG', 'TRP', 9.03), ('OD2', 'ASP', 'CD1', 'TRP', 8.31), ('OD2', 'ASP', 'CD2', 'TRP', 10.3), ('OD2', 'ASP', 'NE1', 'TRP', 9.22), ('OD2', 'ASP', 'CE2', 'TRP', 10.38), ('OD2', 'ASP', 'CE3', 'TRP', 11.51), ('OD2', 'ASP', 'CZ2', 'TRP', 11.64), ('OD2', 'ASP', 'CZ3', 'TRP', 12.62), ('OD2', 'ASP', 'CH2', 'TRP', 12.66)]]}
TRP_LYS = { 
	'distances':
		[[13.59, 12.27, 11.38, 10.29, 10.31], [13.02, 11.61, 10.78, 9.54, 9.54], [11.89, 10.46, 9.74, 8.49, 8.66], [13.79, 12.35, 11.51, 10.16, 10.0], [11.98, 10.49, 9.85, 8.47, 8.56], [13.15, 11.68, 10.95, 9.52, 9.4], [15.08, 13.65, 12.75, 11.38, 11.09], [13.88, 12.39, 11.7, 10.21, 9.99], [15.68, 14.23, 13.37, 11.92, 11.55], [15.12, 13.65, 12.88, 11.39, 11.04]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'LYS', 13.59), ('CB', 'TRP', 'CG', 'LYS', 12.27), ('CB', 'TRP', 'CD', 'LYS', 11.38), ('CB', 'TRP', 'CE', 'LYS', 10.29), ('CB', 'TRP', 'NZ', 'LYS', 10.31)], [('CG', 'TRP', 'CB', 'LYS', 13.02), ('CG', 'TRP', 'CG', 'LYS', 11.61), ('CG', 'TRP', 'CD', 'LYS', 10.78), ('CG', 'TRP', 'CE', 'LYS', 9.54), ('CG', 'TRP', 'NZ', 'LYS', 9.54)], [('CD1', 'TRP', 'CB', 'LYS', 11.89), ('CD1', 'TRP', 'CG', 'LYS', 10.46), ('CD1', 'TRP', 'CD', 'LYS', 9.74), ('CD1', 'TRP', 'CE', 'LYS', 8.49), ('CD1', 'TRP', 'NZ', 'LYS', 8.66)], [('CD2', 'TRP', 'CB', 'LYS', 13.79), ('CD2', 'TRP', 'CG', 'LYS', 12.35), ('CD2', 'TRP', 'CD', 'LYS', 11.51), ('CD2', 'TRP', 'CE', 'LYS', 10.16), ('CD2', 'TRP', 'NZ', 'LYS', 10.0)], [('NE1', 'TRP', 'CB', 'LYS', 11.98), ('NE1', 'TRP', 'CG', 'LYS', 10.49), ('NE1', 'TRP', 'CD', 'LYS', 9.85), ('NE1', 'TRP', 'CE', 'LYS', 8.47), ('NE1', 'TRP', 'NZ', 'LYS', 8.56)], [('CE2', 'TRP', 'CB', 'LYS', 13.15), ('CE2', 'TRP', 'CG', 'LYS', 11.68), ('CE2', 'TRP', 'CD', 'LYS', 10.95), ('CE2', 'TRP', 'CE', 'LYS', 9.52), ('CE2', 'TRP', 'NZ', 'LYS', 9.4)], [('CE3', 'TRP', 'CB', 'LYS', 15.08), ('CE3', 'TRP', 'CG', 'LYS', 13.65), ('CE3', 'TRP', 'CD', 'LYS', 12.75), ('CE3', 'TRP', 'CE', 'LYS', 11.38), ('CE3', 'TRP', 'NZ', 'LYS', 11.09)], [('CZ2', 'TRP', 'CB', 'LYS', 13.88), ('CZ2', 'TRP', 'CG', 'LYS', 12.39), ('CZ2', 'TRP', 'CD', 'LYS', 11.7), ('CZ2', 'TRP', 'CE', 'LYS', 10.21), ('CZ2', 'TRP', 'NZ', 'LYS', 9.99)], [('CZ3', 'TRP', 'CB', 'LYS', 15.68), ('CZ3', 'TRP', 'CG', 'LYS', 14.23), ('CZ3', 'TRP', 'CD', 'LYS', 13.37), ('CZ3', 'TRP', 'CE', 'LYS', 11.92), ('CZ3', 'TRP', 'NZ', 'LYS', 11.55)], [('CH2', 'TRP', 'CB', 'LYS', 15.12), ('CH2', 'TRP', 'CG', 'LYS', 13.65), ('CH2', 'TRP', 'CD', 'LYS', 12.88), ('CH2', 'TRP', 'CE', 'LYS', 11.39), ('CH2', 'TRP', 'NZ', 'LYS', 11.04)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'A_1d7r_4_1_1_64')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_TRP, d, 'A_1d7r_4_1_1_64')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TRP_LYS, d, 'A_1d7r_4_1_1_64')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1,
		'ASP_TRP' :  match2,
		'TRP_LYS' :  match3}