'''
FUNC:M_1v25_6_2_1_3
PDB:1v25
EC:6.2.1.3
RESI:lys,trp,mg
LOCI:a-439,444,1001;
'''
import motifFunctions as cmd
TRP_MG = { 
	'distances':
		[[10.25], [9.0], [8.22], [8.66], [7.3], [7.59], [9.43], [7.39], [9.26], [8.31]],
	'comparisons':
		[[('CB', 'TRP', 'MG', 'MG', 10.25)], [('CG', 'TRP', 'MG', 'MG', 9.0)], [('CD1', 'TRP', 'MG', 'MG', 8.22)], [('CD2', 'TRP', 'MG', 'MG', 8.66)], [('NE1', 'TRP', 'MG', 'MG', 7.3)], [('CE2', 'TRP', 'MG', 'MG', 7.59)], [('CE3', 'TRP', 'MG', 'MG', 9.43)], [('CZ2', 'TRP', 'MG', 'MG', 7.39)], [('CZ3', 'TRP', 'MG', 'MG', 9.26)], [('CH2', 'TRP', 'MG', 'MG', 8.31)]]}
LYS_MG = { 
	'distances':
		[[12.1], [11.56], [10.59], [9.83], [9.05]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 12.1)], [('CG', 'LYS', 'MG', 'MG', 11.56)], [('CD', 'LYS', 'MG', 'MG', 10.59)], [('CE', 'LYS', 'MG', 'MG', 9.83)], [('NZ', 'LYS', 'MG', 'MG', 9.05)]]}
LYS_TRP = { 
	'distances':
		[[7.76, 7.22, 7.87, 6.44, 7.64, 6.79, 5.99, 6.76, 5.93, 6.33], [7.57, 6.87, 7.19, 6.31, 6.92, 6.36, 6.35, 6.48, 6.44, 6.5], [8.16, 7.13, 7.18, 6.38, 6.52, 5.96, 6.55, 5.72, 6.31, 5.91], [7.96, 6.81, 6.46, 6.34, 5.74, 5.64, 6.95, 5.65, 6.94, 6.34], [8.93, 7.61, 7.05, 7.03, 6.01, 5.97, 7.67, 5.63, 7.42, 6.47]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TRP', 7.76), ('CB', 'LYS', 'CG', 'TRP', 7.22), ('CB', 'LYS', 'CD1', 'TRP', 7.87), ('CB', 'LYS', 'CD2', 'TRP', 6.44), ('CB', 'LYS', 'NE1', 'TRP', 7.64), ('CB', 'LYS', 'CE2', 'TRP', 6.79), ('CB', 'LYS', 'CE3', 'TRP', 5.99), ('CB', 'LYS', 'CZ2', 'TRP', 6.76), ('CB', 'LYS', 'CZ3', 'TRP', 5.93), ('CB', 'LYS', 'CH2', 'TRP', 6.33)], [('CG', 'LYS', 'CB', 'TRP', 7.57), ('CG', 'LYS', 'CG', 'TRP', 6.87), ('CG', 'LYS', 'CD1', 'TRP', 7.19), ('CG', 'LYS', 'CD2', 'TRP', 6.31), ('CG', 'LYS', 'NE1', 'TRP', 6.92), ('CG', 'LYS', 'CE2', 'TRP', 6.36), ('CG', 'LYS', 'CE3', 'TRP', 6.35), ('CG', 'LYS', 'CZ2', 'TRP', 6.48), ('CG', 'LYS', 'CZ3', 'TRP', 6.44), ('CG', 'LYS', 'CH2', 'TRP', 6.5)], [('CD', 'LYS', 'CB', 'TRP', 8.16), ('CD', 'LYS', 'CG', 'TRP', 7.13), ('CD', 'LYS', 'CD1', 'TRP', 7.18), ('CD', 'LYS', 'CD2', 'TRP', 6.38), ('CD', 'LYS', 'NE1', 'TRP', 6.52), ('CD', 'LYS', 'CE2', 'TRP', 5.96), ('CD', 'LYS', 'CE3', 'TRP', 6.55), ('CD', 'LYS', 'CZ2', 'TRP', 5.72), ('CD', 'LYS', 'CZ3', 'TRP', 6.31), ('CD', 'LYS', 'CH2', 'TRP', 5.91)], [('CE', 'LYS', 'CB', 'TRP', 7.96), ('CE', 'LYS', 'CG', 'TRP', 6.81), ('CE', 'LYS', 'CD1', 'TRP', 6.46), ('CE', 'LYS', 'CD2', 'TRP', 6.34), ('CE', 'LYS', 'NE1', 'TRP', 5.74), ('CE', 'LYS', 'CE2', 'TRP', 5.64), ('CE', 'LYS', 'CE3', 'TRP', 6.95), ('CE', 'LYS', 'CZ2', 'TRP', 5.65), ('CE', 'LYS', 'CZ3', 'TRP', 6.94), ('CE', 'LYS', 'CH2', 'TRP', 6.34)], [('NZ', 'LYS', 'CB', 'TRP', 8.93), ('NZ', 'LYS', 'CG', 'TRP', 7.61), ('NZ', 'LYS', 'CD1', 'TRP', 7.05), ('NZ', 'LYS', 'CD2', 'TRP', 7.03), ('NZ', 'LYS', 'NE1', 'TRP', 6.01), ('NZ', 'LYS', 'CE2', 'TRP', 5.97), ('NZ', 'LYS', 'CE3', 'TRP', 7.67), ('NZ', 'LYS', 'CZ2', 'TRP', 5.63), ('NZ', 'LYS', 'CZ3', 'TRP', 7.42), ('NZ', 'LYS', 'CH2', 'TRP', 6.47)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TRP_MG, d, 'M_1v25_6_2_1_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_MG, d, 'M_1v25_6_2_1_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_TRP, d, 'M_1v25_6_2_1_3')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TRP_MG' :  match1,
		'LYS_MG' :  match2,
		'LYS_TRP' :  match3}