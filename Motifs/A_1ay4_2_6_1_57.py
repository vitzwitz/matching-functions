'''
FUNC:A_1ay4_2_6_1_57
PDB:1ay4
EC:2.6.1.57
RESI:trp,asp,lys
LOCI:a-140,222,258;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[14.4, 14.06, 12.69, 12.6, 11.27], [13.25, 12.8, 11.39, 11.22, 9.86], [12.24, 11.87, 10.46, 10.4, 9.13], [13.48, 12.87, 11.45, 11.08, 9.66]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 14.4), ('CB', 'ASP', 'CG', 'LYS', 14.06), ('CB', 'ASP', 'CD', 'LYS', 12.69), ('CB', 'ASP', 'CE', 'LYS', 12.6), ('CB', 'ASP', 'NZ', 'LYS', 11.27)], [('CG', 'ASP', 'CB', 'LYS', 13.25), ('CG', 'ASP', 'CG', 'LYS', 12.8), ('CG', 'ASP', 'CD', 'LYS', 11.39), ('CG', 'ASP', 'CE', 'LYS', 11.22), ('CG', 'ASP', 'NZ', 'LYS', 9.86)], [('OD1', 'ASP', 'CB', 'LYS', 12.24), ('OD1', 'ASP', 'CG', 'LYS', 11.87), ('OD1', 'ASP', 'CD', 'LYS', 10.46), ('OD1', 'ASP', 'CE', 'LYS', 10.4), ('OD1', 'ASP', 'NZ', 'LYS', 9.13)], [('OD2', 'ASP', 'CB', 'LYS', 13.48), ('OD2', 'ASP', 'CG', 'LYS', 12.87), ('OD2', 'ASP', 'CD', 'LYS', 11.45), ('OD2', 'ASP', 'CE', 'LYS', 11.08), ('OD2', 'ASP', 'NZ', 'LYS', 9.66)]]}
ASP_TRP = { 
	'distances':
		[[9.4, 9.85, 10.9, 9.52, 11.23, 10.47, 8.78, 10.76, 9.12, 10.12], [8.52, 8.74, 9.71, 8.29, 9.92, 9.12, 7.59, 9.34, 7.84, 8.73], [9.18, 9.18, 10.0, 8.62, 10.03, 9.23, 7.99, 9.29, 8.04, 8.71], [7.35, 7.6, 8.65, 7.17, 8.92, 8.11, 6.45, 8.43, 6.86, 7.86]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TRP', 9.4), ('CB', 'ASP', 'CG', 'TRP', 9.85), ('CB', 'ASP', 'CD1', 'TRP', 10.9), ('CB', 'ASP', 'CD2', 'TRP', 9.52), ('CB', 'ASP', 'NE1', 'TRP', 11.23), ('CB', 'ASP', 'CE2', 'TRP', 10.47), ('CB', 'ASP', 'CE3', 'TRP', 8.78), ('CB', 'ASP', 'CZ2', 'TRP', 10.76), ('CB', 'ASP', 'CZ3', 'TRP', 9.12), ('CB', 'ASP', 'CH2', 'TRP', 10.12)], [('CG', 'ASP', 'CB', 'TRP', 8.52), ('CG', 'ASP', 'CG', 'TRP', 8.74), ('CG', 'ASP', 'CD1', 'TRP', 9.71), ('CG', 'ASP', 'CD2', 'TRP', 8.29), ('CG', 'ASP', 'NE1', 'TRP', 9.92), ('CG', 'ASP', 'CE2', 'TRP', 9.12), ('CG', 'ASP', 'CE3', 'TRP', 7.59), ('CG', 'ASP', 'CZ2', 'TRP', 9.34), ('CG', 'ASP', 'CZ3', 'TRP', 7.84), ('CG', 'ASP', 'CH2', 'TRP', 8.73)], [('OD1', 'ASP', 'CB', 'TRP', 9.18), ('OD1', 'ASP', 'CG', 'TRP', 9.18), ('OD1', 'ASP', 'CD1', 'TRP', 10.0), ('OD1', 'ASP', 'CD2', 'TRP', 8.62), ('OD1', 'ASP', 'NE1', 'TRP', 10.03), ('OD1', 'ASP', 'CE2', 'TRP', 9.23), ('OD1', 'ASP', 'CE3', 'TRP', 7.99), ('OD1', 'ASP', 'CZ2', 'TRP', 9.29), ('OD1', 'ASP', 'CZ3', 'TRP', 8.04), ('OD1', 'ASP', 'CH2', 'TRP', 8.71)], [('OD2', 'ASP', 'CB', 'TRP', 7.35), ('OD2', 'ASP', 'CG', 'TRP', 7.6), ('OD2', 'ASP', 'CD1', 'TRP', 8.65), ('OD2', 'ASP', 'CD2', 'TRP', 7.17), ('OD2', 'ASP', 'NE1', 'TRP', 8.92), ('OD2', 'ASP', 'CE2', 'TRP', 8.11), ('OD2', 'ASP', 'CE3', 'TRP', 6.45), ('OD2', 'ASP', 'CZ2', 'TRP', 8.43), ('OD2', 'ASP', 'CZ3', 'TRP', 6.86), ('OD2', 'ASP', 'CH2', 'TRP', 7.86)]]}
TRP_LYS = { 
	'distances':
		[[14.64, 13.55, 12.38, 11.37, 10.01], [13.75, 12.57, 11.4, 10.28, 8.97], [13.2, 11.93, 10.89, 9.66, 8.47], [13.45, 12.27, 11.01, 9.88, 8.56], [12.53, 11.2, 10.14, 8.82, 7.71], [12.68, 11.41, 10.2, 8.95, 7.76], [13.95, 12.86, 11.5, 10.48, 9.13], [12.42, 11.15, 9.9, 8.65, 7.56], [13.71, 12.63, 11.22, 10.22, 8.96], [12.96, 11.8, 10.44, 9.34, 8.21]],
	'comparisons':
		[[('CB', 'TRP', 'CB', 'LYS', 14.64), ('CB', 'TRP', 'CG', 'LYS', 13.55), ('CB', 'TRP', 'CD', 'LYS', 12.38), ('CB', 'TRP', 'CE', 'LYS', 11.37), ('CB', 'TRP', 'NZ', 'LYS', 10.01)], [('CG', 'TRP', 'CB', 'LYS', 13.75), ('CG', 'TRP', 'CG', 'LYS', 12.57), ('CG', 'TRP', 'CD', 'LYS', 11.4), ('CG', 'TRP', 'CE', 'LYS', 10.28), ('CG', 'TRP', 'NZ', 'LYS', 8.97)], [('CD1', 'TRP', 'CB', 'LYS', 13.2), ('CD1', 'TRP', 'CG', 'LYS', 11.93), ('CD1', 'TRP', 'CD', 'LYS', 10.89), ('CD1', 'TRP', 'CE', 'LYS', 9.66), ('CD1', 'TRP', 'NZ', 'LYS', 8.47)], [('CD2', 'TRP', 'CB', 'LYS', 13.45), ('CD2', 'TRP', 'CG', 'LYS', 12.27), ('CD2', 'TRP', 'CD', 'LYS', 11.01), ('CD2', 'TRP', 'CE', 'LYS', 9.88), ('CD2', 'TRP', 'NZ', 'LYS', 8.56)], [('NE1', 'TRP', 'CB', 'LYS', 12.53), ('NE1', 'TRP', 'CG', 'LYS', 11.2), ('NE1', 'TRP', 'CD', 'LYS', 10.14), ('NE1', 'TRP', 'CE', 'LYS', 8.82), ('NE1', 'TRP', 'NZ', 'LYS', 7.71)], [('CE2', 'TRP', 'CB', 'LYS', 12.68), ('CE2', 'TRP', 'CG', 'LYS', 11.41), ('CE2', 'TRP', 'CD', 'LYS', 10.2), ('CE2', 'TRP', 'CE', 'LYS', 8.95), ('CE2', 'TRP', 'NZ', 'LYS', 7.76)], [('CE3', 'TRP', 'CB', 'LYS', 13.95), ('CE3', 'TRP', 'CG', 'LYS', 12.86), ('CE3', 'TRP', 'CD', 'LYS', 11.5), ('CE3', 'TRP', 'CE', 'LYS', 10.48), ('CE3', 'TRP', 'NZ', 'LYS', 9.13)], [('CZ2', 'TRP', 'CB', 'LYS', 12.42), ('CZ2', 'TRP', 'CG', 'LYS', 11.15), ('CZ2', 'TRP', 'CD', 'LYS', 9.9), ('CZ2', 'TRP', 'CE', 'LYS', 8.65), ('CZ2', 'TRP', 'NZ', 'LYS', 7.56)], [('CZ3', 'TRP', 'CB', 'LYS', 13.71), ('CZ3', 'TRP', 'CG', 'LYS', 12.63), ('CZ3', 'TRP', 'CD', 'LYS', 11.22), ('CZ3', 'TRP', 'CE', 'LYS', 10.22), ('CZ3', 'TRP', 'NZ', 'LYS', 8.96)], [('CH2', 'TRP', 'CB', 'LYS', 12.96), ('CH2', 'TRP', 'CG', 'LYS', 11.8), ('CH2', 'TRP', 'CD', 'LYS', 10.44), ('CH2', 'TRP', 'CE', 'LYS', 9.34), ('CH2', 'TRP', 'NZ', 'LYS', 8.21)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'A_1ay4_2_6_1_57')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_TRP, d, 'A_1ay4_2_6_1_57')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TRP_LYS, d, 'A_1ay4_2_6_1_57')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1,
		'ASP_TRP' :  match2,
		'TRP_LYS' :  match3}