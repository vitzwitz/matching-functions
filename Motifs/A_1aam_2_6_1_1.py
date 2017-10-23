'''
FUNC:A_1aam_2_6_1_1
PDB:1aam
EC:2.6.1.1
RESI:trp,asp,lys
LOCI:a-142,223,258;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[13.52, 12.13, 12.02, 11.36, 10.99], [12.23, 10.79, 10.62, 9.89, 9.51], [11.73, 10.29, 10.24, 9.44, 9.27], [11.87, 10.43, 10.07, 9.35, 8.78]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.52), ('CB', 'ASP', 'CG', 'LYS', 12.13), ('CB', 'ASP', 'CD', 'LYS', 12.02), ('CB', 'ASP', 'CE', 'LYS', 11.36), ('CB', 'ASP', 'NZ', 'LYS', 10.99)], [('CG', 'ASP', 'CB', 'LYS', 12.23), ('CG', 'ASP', 'CG', 'LYS', 10.79), ('CG', 'ASP', 'CD', 'LYS', 10.62), ('CG', 'ASP', 'CE', 'LYS', 9.89), ('CG', 'ASP', 'NZ', 'LYS', 9.51)], [('OD1', 'ASP', 'CB', 'LYS', 11.73), ('OD1', 'ASP', 'CG', 'LYS', 10.29), ('OD1', 'ASP', 'CD', 'LYS', 10.24), ('OD1', 'ASP', 'CE', 'LYS', 9.44), ('OD1', 'ASP', 'NZ', 'LYS', 9.27)], [('OD2', 'ASP', 'CB', 'LYS', 11.87), ('OD2', 'ASP', 'CG', 'LYS', 10.43), ('OD2', 'ASP', 'CD', 'LYS', 10.07), ('OD2', 'ASP', 'CE', 'LYS', 9.35), ('OD2', 'ASP', 'NZ', 'LYS', 8.78)]]}
ASP_TRP = { 
	'distances':
		[[9.36, 9.51, 10.66, 8.85, 10.81, 9.79, 7.8, 9.86, 7.85, 8.92], [8.91, 8.81, 9.81, 8.07, 9.83, 8.83, 7.15, 8.82, 7.1, 7.98], [9.91, 9.65, 10.53, 8.81, 10.39, 9.37, 7.92, 9.17, 7.64, 8.3], [7.76, 7.63, 8.62, 6.98, 8.69, 7.77, 6.2, 7.92, 6.35, 7.24]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TRP', 9.36), ('CB', 'ASP', 'CG', 'TRP', 9.51), ('CB', 'ASP', 'CD1', 'TRP', 10.66), ('CB', 'ASP', 'CD2', 'TRP', 8.85), ('CB', 'ASP', 'NE1', 'TRP', 10.81), ('CB', 'ASP', 'CE2', 'TRP', 9.79), ('CB', 'ASP', 'CE3', 'TRP', 7.8), ('CB', 'ASP', 'CZ2', 'TRP', 9.86), ('CB', 'ASP', 'CZ3', 'TRP', 7.85), ('CB', 'ASP', 'CH2', 'TRP', 8.92)], [('CG', 'ASP', 'CB', 'TRP', 8.91), ('CG', 'ASP', 'CG', 'TRP', 8.81), ('CG', 'ASP', 'CD1', 'TRP', 9.81), ('CG', 'ASP', 'CD2', 'TRP', 8.07), ('CG', 'ASP', 'NE1', 'TRP', 9.83), ('CG', 'ASP', 'CE2', 'TRP', 8.83), ('CG', 'ASP', 'CE3', 'TRP', 7.15), ('CG', 'ASP', 'CZ2', 'TRP', 8.82), ('CG', 'ASP', 'CZ3', 'TRP', 7.1), ('CG', 'ASP', 'CH2', 'TRP', 7.98)], [('OD1', 'ASP', 'CB', 'TRP', 9.91), ('OD1', 'ASP', 'CG', 'TRP', 9.65), ('OD1', 'ASP', 'CD1', 'TRP', 10.53), ('OD1', 'ASP', 'CD2', 'TRP', 8.81), ('OD1', 'ASP', 'NE1', 'TRP', 10.39), ('OD1', 'ASP', 'CE2', 'TRP', 9.37), ('OD1', 'ASP', 'CE3', 'TRP', 7.92), ('OD1', 'ASP', 'CZ2', 'TRP', 9.17), ('OD1', 'ASP', 'CZ3', 'TRP', 7.64), ('OD1', 'ASP', 'CH2', 'TRP', 8.3)], [('OD2', 'ASP', 'CB', 'TRP', 7.76), ('OD2', 'ASP', 'CG', 'TRP', 7.63), ('OD2', 'ASP', 'CD1', 'TRP', 8.62), ('OD2', 'ASP', 'CD2', 'TRP', 6.98), ('OD2', 'ASP', 'NE1', 'TRP', 8.69), ('OD2', 'ASP', 'CE2', 'TRP', 7.77), ('OD2', 'ASP', 'CE3', 'TRP', 6.2), ('OD2', 'ASP', 'CZ2', 'TRP', 7.92), ('OD2', 'ASP', 'CZ3', 'TRP', 6.35), ('OD2', 'ASP', 'CH2', 'TRP', 7.24)]]}
TRP_LYS = { 
	'distances':
		[[14.26, 13.06, 12.04, 11.52, 10.22], [13.7, 12.46, 11.34, 10.67, 9.31], [13.48, 12.31, 11.06, 10.41, 8.96], [13.61, 12.27, 11.2, 10.33, 9.04], [13.24, 12.03, 10.74, 9.91, 8.46], [13.32, 12.0, 10.83, 9.85, 8.51], [13.97, 12.56, 11.64, 10.69, 9.54], [13.39, 12.02, 10.9, 9.74, 8.51], [14.02, 12.56, 11.68, 10.58, 9.52], [13.74, 12.3, 11.33, 10.11, 9.03]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'LYS', 14.26), ('CB', 'TRP', 'CG', 'LYS', 13.06), ('CB', 'TRP', 'CD', 'LYS', 12.04), ('CB', 'TRP', 'CE', 'LYS', 11.52), ('CB', 'TRP', 'NZ', 'LYS', 10.22)], [('CG', 'TRP', 'CB', 'LYS', 13.7), ('CG', 'TRP', 'CG', 'LYS', 12.46), ('CG', 'TRP', 'CD', 'LYS', 11.34), ('CG', 'TRP', 'CE', 'LYS', 10.67), ('CG', 'TRP', 'NZ', 'LYS', 9.31)], [('CD1', 'TRP', 'CB', 'LYS', 13.48), ('CD1', 'TRP', 'CG', 'LYS', 12.31), ('CD1', 'TRP', 'CD', 'LYS', 11.06), ('CD1', 'TRP', 'CE', 'LYS', 10.41), ('CD1', 'TRP', 'NZ', 'LYS', 8.96)], [('CD2', 'TRP', 'CB', 'LYS', 13.61), ('CD2', 'TRP', 'CG', 'LYS', 12.27), ('CD2', 'TRP', 'CD', 'LYS', 11.2), ('CD2', 'TRP', 'CE', 'LYS', 10.33), ('CD2', 'TRP', 'NZ', 'LYS', 9.04)], [('NE1', 'TRP', 'CB', 'LYS', 13.24), ('NE1', 'TRP', 'CG', 'LYS', 12.03), ('NE1', 'TRP', 'CD', 'LYS', 10.74), ('NE1', 'TRP', 'CE', 'LYS', 9.91), ('NE1', 'TRP', 'NZ', 'LYS', 8.46)], [('CE2', 'TRP', 'CB', 'LYS', 13.32), ('CE2', 'TRP', 'CG', 'LYS', 12.0), ('CE2', 'TRP', 'CD', 'LYS', 10.83), ('CE2', 'TRP', 'CE', 'LYS', 9.85), ('CE2', 'TRP', 'NZ', 'LYS', 8.51)], [('CE3', 'TRP', 'CB', 'LYS', 13.97), ('CE3', 'TRP', 'CG', 'LYS', 12.56), ('CE3', 'TRP', 'CD', 'LYS', 11.64), ('CE3', 'TRP', 'CE', 'LYS', 10.69), ('CE3', 'TRP', 'NZ', 'LYS', 9.54)], [('CZ2', 'TRP', 'CB', 'LYS', 13.39), ('CZ2', 'TRP', 'CG', 'LYS', 12.02), ('CZ2', 'TRP', 'CD', 'LYS', 10.9), ('CZ2', 'TRP', 'CE', 'LYS', 9.74), ('CZ2', 'TRP', 'NZ', 'LYS', 8.51)], [('CZ3', 'TRP', 'CB', 'LYS', 14.02), ('CZ3', 'TRP', 'CG', 'LYS', 12.56), ('CZ3', 'TRP', 'CD', 'LYS', 11.68), ('CZ3', 'TRP', 'CE', 'LYS', 10.58), ('CZ3', 'TRP', 'NZ', 'LYS', 9.52)], [('CH2', 'TRP', 'CB', 'LYS', 13.74), ('CH2', 'TRP', 'CG', 'LYS', 12.3), ('CH2', 'TRP', 'CD', 'LYS', 11.33), ('CH2', 'TRP', 'CE', 'LYS', 10.11), ('CH2', 'TRP', 'NZ', 'LYS', 9.03)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'A_1aam_2_6_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_TRP, d, 'A_1aam_2_6_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TRP_LYS, d, 'A_1aam_2_6_1_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1,
		'ASP_TRP' :  match2,
		'TRP_LYS' :  match3}