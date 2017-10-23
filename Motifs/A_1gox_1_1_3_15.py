'''
FUNC:A_1gox_1_1_3_15
PDB:1gox
EC:1.1.3.15
RESI:tyr,asp,his,arg
LOCI:a-129,157,254,257;
'''
import motifFunctions as cmd
ARG_TYR = { 
	'distances':
		[[16.42, 14.95, 14.11, 14.54, 12.73, 13.18, 12.23, 10.9], [16.61, 15.13, 14.36, 14.64, 12.98, 13.26, 12.38, 11.05], [16.92, 15.43, 14.8, 14.8, 13.42, 13.39, 12.67, 11.31], [15.95, 14.45, 13.91, 13.74, 12.54, 12.33, 11.69, 10.34], [16.65, 15.17, 14.73, 14.36, 13.39, 12.95, 12.44, 11.11], [18.0, 16.51, 16.06, 15.7, 14.72, 14.29, 13.78, 12.44], [16.17, 14.71, 14.37, 13.82, 13.08, 12.42, 12.04, 10.75]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'TYR', 16.42), ('CB', 'ARG', 'CG', 'TYR', 14.95), ('CB', 'ARG', 'CD1', 'TYR', 14.11), ('CB', 'ARG', 'CD2', 'TYR', 14.54), ('CB', 'ARG', 'CE1', 'TYR', 12.73), ('CB', 'ARG', 'CE2', 'TYR', 13.18), ('CB', 'ARG', 'CZ', 'TYR', 12.23), ('CB', 'ARG', 'OH', 'TYR', 10.9)], [('CG', 'ARG', 'CB', 'TYR', 16.61), ('CG', 'ARG', 'CG', 'TYR', 15.13), ('CG', 'ARG', 'CD1', 'TYR', 14.36), ('CG', 'ARG', 'CD2', 'TYR', 14.64), ('CG', 'ARG', 'CE1', 'TYR', 12.98), ('CG', 'ARG', 'CE2', 'TYR', 13.26), ('CG', 'ARG', 'CZ', 'TYR', 12.38), ('CG', 'ARG', 'OH', 'TYR', 11.05)], [('CD', 'ARG', 'CB', 'TYR', 16.92), ('CD', 'ARG', 'CG', 'TYR', 15.43), ('CD', 'ARG', 'CD1', 'TYR', 14.8), ('CD', 'ARG', 'CD2', 'TYR', 14.8), ('CD', 'ARG', 'CE1', 'TYR', 13.42), ('CD', 'ARG', 'CE2', 'TYR', 13.39), ('CD', 'ARG', 'CZ', 'TYR', 12.67), ('CD', 'ARG', 'OH', 'TYR', 11.31)], [('NE', 'ARG', 'CB', 'TYR', 15.95), ('NE', 'ARG', 'CG', 'TYR', 14.45), ('NE', 'ARG', 'CD1', 'TYR', 13.91), ('NE', 'ARG', 'CD2', 'TYR', 13.74), ('NE', 'ARG', 'CE1', 'TYR', 12.54), ('NE', 'ARG', 'CE2', 'TYR', 12.33), ('NE', 'ARG', 'CZ', 'TYR', 11.69), ('NE', 'ARG', 'OH', 'TYR', 10.34)], [('CZ', 'ARG', 'CB', 'TYR', 16.65), ('CZ', 'ARG', 'CG', 'TYR', 15.17), ('CZ', 'ARG', 'CD1', 'TYR', 14.73), ('CZ', 'ARG', 'CD2', 'TYR', 14.36), ('CZ', 'ARG', 'CE1', 'TYR', 13.39), ('CZ', 'ARG', 'CE2', 'TYR', 12.95), ('CZ', 'ARG', 'CZ', 'TYR', 12.44), ('CZ', 'ARG', 'OH', 'TYR', 11.11)], [('NH1', 'ARG', 'CB', 'TYR', 18.0), ('NH1', 'ARG', 'CG', 'TYR', 16.51), ('NH1', 'ARG', 'CD1', 'TYR', 16.06), ('NH1', 'ARG', 'CD2', 'TYR', 15.7), ('NH1', 'ARG', 'CE1', 'TYR', 14.72), ('NH1', 'ARG', 'CE2', 'TYR', 14.29), ('NH1', 'ARG', 'CZ', 'TYR', 13.78), ('NH1', 'ARG', 'OH', 'TYR', 12.44)], [('NH2', 'ARG', 'CB', 'TYR', 16.17), ('NH2', 'ARG', 'CG', 'TYR', 14.71), ('NH2', 'ARG', 'CD1', 'TYR', 14.37), ('NH2', 'ARG', 'CD2', 'TYR', 13.82), ('NH2', 'ARG', 'CE1', 'TYR', 13.08), ('NH2', 'ARG', 'CE2', 'TYR', 12.42), ('NH2', 'ARG', 'CZ', 'TYR', 12.04), ('NH2', 'ARG', 'OH', 'TYR', 10.75)]]}
HIS_ASP = { 
	'distances':
		[[7.46, 6.09, 5.44, 5.93], [7.8, 6.39, 6.12, 5.78], [7.09, 5.74, 5.86, 4.84], [9.09, 7.69, 7.47, 6.97], [8.14, 6.88, 7.13, 5.81], [9.25, 7.92, 7.96, 6.97]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'ASP', 7.46), ('CB', 'HIS', 'CG', 'ASP', 6.09), ('CB', 'HIS', 'OD1', 'ASP', 5.44), ('CB', 'HIS', 'OD2', 'ASP', 5.93)], [('CG', 'HIS', 'CB', 'ASP', 7.8), ('CG', 'HIS', 'CG', 'ASP', 6.39), ('CG', 'HIS', 'OD1', 'ASP', 6.12), ('CG', 'HIS', 'OD2', 'ASP', 5.78)], [('ND1', 'HIS', 'CB', 'ASP', 7.09), ('ND1', 'HIS', 'CG', 'ASP', 5.74), ('ND1', 'HIS', 'OD1', 'ASP', 5.86), ('ND1', 'HIS', 'OD2', 'ASP', 4.84)], [('CD2', 'HIS', 'CB', 'ASP', 9.09), ('CD2', 'HIS', 'CG', 'ASP', 7.69), ('CD2', 'HIS', 'OD1', 'ASP', 7.47), ('CD2', 'HIS', 'OD2', 'ASP', 6.97)], [('CE1', 'HIS', 'CB', 'ASP', 8.14), ('CE1', 'HIS', 'CG', 'ASP', 6.88), ('CE1', 'HIS', 'OD1', 'ASP', 7.13), ('CE1', 'HIS', 'OD2', 'ASP', 5.81)], [('NE2', 'HIS', 'CB', 'ASP', 9.25), ('NE2', 'HIS', 'CG', 'ASP', 7.92), ('NE2', 'HIS', 'OD1', 'ASP', 7.96), ('NE2', 'HIS', 'OD2', 'ASP', 6.97)]]}
ARG_ASP = { 
	'distances':
		[[11.81, 10.68, 10.31, 10.29], [12.15, 10.89, 10.38, 10.51], [13.38, 12.07, 11.59, 11.59], [13.48, 12.16, 11.85, 11.52], [14.8, 13.5, 13.2, 12.81], [15.74, 14.44, 14.06, 13.84], [15.29, 14.01, 13.83, 13.21]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 11.81), ('CB', 'ARG', 'CG', 'ASP', 10.68), ('CB', 'ARG', 'OD1', 'ASP', 10.31), ('CB', 'ARG', 'OD2', 'ASP', 10.29)], [('CG', 'ARG', 'CB', 'ASP', 12.15), ('CG', 'ARG', 'CG', 'ASP', 10.89), ('CG', 'ARG', 'OD1', 'ASP', 10.38), ('CG', 'ARG', 'OD2', 'ASP', 10.51)], [('CD', 'ARG', 'CB', 'ASP', 13.38), ('CD', 'ARG', 'CG', 'ASP', 12.07), ('CD', 'ARG', 'OD1', 'ASP', 11.59), ('CD', 'ARG', 'OD2', 'ASP', 11.59)], [('NE', 'ARG', 'CB', 'ASP', 13.48), ('NE', 'ARG', 'CG', 'ASP', 12.16), ('NE', 'ARG', 'OD1', 'ASP', 11.85), ('NE', 'ARG', 'OD2', 'ASP', 11.52)], [('CZ', 'ARG', 'CB', 'ASP', 14.8), ('CZ', 'ARG', 'CG', 'ASP', 13.5), ('CZ', 'ARG', 'OD1', 'ASP', 13.2), ('CZ', 'ARG', 'OD2', 'ASP', 12.81)], [('NH1', 'ARG', 'CB', 'ASP', 15.74), ('NH1', 'ARG', 'CG', 'ASP', 14.44), ('NH1', 'ARG', 'OD1', 'ASP', 14.06), ('NH1', 'ARG', 'OD2', 'ASP', 13.84)], [('NH2', 'ARG', 'CB', 'ASP', 15.29), ('NH2', 'ARG', 'CG', 'ASP', 14.01), ('NH2', 'ARG', 'OD1', 'ASP', 13.83), ('NH2', 'ARG', 'OD2', 'ASP', 13.21)]]}
ASP_TYR = { 
	'distances':
		[[12.7, 11.84, 10.5, 12.51, 9.83, 11.97, 10.65, 10.36], [12.39, 11.38, 10.1, 11.88, 9.26, 11.19, 9.89, 9.44], [13.33, 12.28, 11.05, 12.67, 10.14, 11.9, 10.63, 10.06], [11.33, 10.26, 8.99, 10.7, 8.08, 9.97, 8.66, 8.19]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 12.7), ('CB', 'ASP', 'CG', 'TYR', 11.84), ('CB', 'ASP', 'CD1', 'TYR', 10.5), ('CB', 'ASP', 'CD2', 'TYR', 12.51), ('CB', 'ASP', 'CE1', 'TYR', 9.83), ('CB', 'ASP', 'CE2', 'TYR', 11.97), ('CB', 'ASP', 'CZ', 'TYR', 10.65), ('CB', 'ASP', 'OH', 'TYR', 10.36)], [('CG', 'ASP', 'CB', 'TYR', 12.39), ('CG', 'ASP', 'CG', 'TYR', 11.38), ('CG', 'ASP', 'CD1', 'TYR', 10.1), ('CG', 'ASP', 'CD2', 'TYR', 11.88), ('CG', 'ASP', 'CE1', 'TYR', 9.26), ('CG', 'ASP', 'CE2', 'TYR', 11.19), ('CG', 'ASP', 'CZ', 'TYR', 9.89), ('CG', 'ASP', 'OH', 'TYR', 9.44)], [('OD1', 'ASP', 'CB', 'TYR', 13.33), ('OD1', 'ASP', 'CG', 'TYR', 12.28), ('OD1', 'ASP', 'CD1', 'TYR', 11.05), ('OD1', 'ASP', 'CD2', 'TYR', 12.67), ('OD1', 'ASP', 'CE1', 'TYR', 10.14), ('OD1', 'ASP', 'CE2', 'TYR', 11.9), ('OD1', 'ASP', 'CZ', 'TYR', 10.63), ('OD1', 'ASP', 'OH', 'TYR', 10.06)], [('OD2', 'ASP', 'CB', 'TYR', 11.33), ('OD2', 'ASP', 'CG', 'TYR', 10.26), ('OD2', 'ASP', 'CD1', 'TYR', 8.99), ('OD2', 'ASP', 'CD2', 'TYR', 10.7), ('OD2', 'ASP', 'CE1', 'TYR', 8.08), ('OD2', 'ASP', 'CE2', 'TYR', 9.97), ('OD2', 'ASP', 'CZ', 'TYR', 8.66), ('OD2', 'ASP', 'OH', 'TYR', 8.19)]]}
ARG_HIS = { 
	'distances':
		[[7.12, 6.97, 7.99, 6.32, 8.07, 7.13], [6.99, 6.89, 8.08, 6.12, 8.16, 7.08], [8.16, 7.86, 8.98, 6.85, 8.84, 7.61], [8.5, 7.86, 8.76, 6.65, 8.34, 7.05], [9.87, 9.19, 10.03, 7.95, 9.5, 8.2], [10.65, 10.15, 11.11, 8.98, 10.69, 9.39], [10.62, 9.75, 10.41, 8.45, 9.69, 8.42]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 7.12), ('CB', 'ARG', 'CG', 'HIS', 6.97), ('CB', 'ARG', 'ND1', 'HIS', 7.99), ('CB', 'ARG', 'CD2', 'HIS', 6.32), ('CB', 'ARG', 'CE1', 'HIS', 8.07), ('CB', 'ARG', 'NE2', 'HIS', 7.13)], [('CG', 'ARG', 'CB', 'HIS', 6.99), ('CG', 'ARG', 'CG', 'HIS', 6.89), ('CG', 'ARG', 'ND1', 'HIS', 8.08), ('CG', 'ARG', 'CD2', 'HIS', 6.12), ('CG', 'ARG', 'CE1', 'HIS', 8.16), ('CG', 'ARG', 'NE2', 'HIS', 7.08)], [('CD', 'ARG', 'CB', 'HIS', 8.16), ('CD', 'ARG', 'CG', 'HIS', 7.86), ('CD', 'ARG', 'ND1', 'HIS', 8.98), ('CD', 'ARG', 'CD2', 'HIS', 6.85), ('CD', 'ARG', 'CE1', 'HIS', 8.84), ('CD', 'ARG', 'NE2', 'HIS', 7.61)], [('NE', 'ARG', 'CB', 'HIS', 8.5), ('NE', 'ARG', 'CG', 'HIS', 7.86), ('NE', 'ARG', 'ND1', 'HIS', 8.76), ('NE', 'ARG', 'CD2', 'HIS', 6.65), ('NE', 'ARG', 'CE1', 'HIS', 8.34), ('NE', 'ARG', 'NE2', 'HIS', 7.05)], [('CZ', 'ARG', 'CB', 'HIS', 9.87), ('CZ', 'ARG', 'CG', 'HIS', 9.19), ('CZ', 'ARG', 'ND1', 'HIS', 10.03), ('CZ', 'ARG', 'CD2', 'HIS', 7.95), ('CZ', 'ARG', 'CE1', 'HIS', 9.5), ('CZ', 'ARG', 'NE2', 'HIS', 8.2)], [('NH1', 'ARG', 'CB', 'HIS', 10.65), ('NH1', 'ARG', 'CG', 'HIS', 10.15), ('NH1', 'ARG', 'ND1', 'HIS', 11.11), ('NH1', 'ARG', 'CD2', 'HIS', 8.98), ('NH1', 'ARG', 'CE1', 'HIS', 10.69), ('NH1', 'ARG', 'NE2', 'HIS', 9.39)], [('NH2', 'ARG', 'CB', 'HIS', 10.62), ('NH2', 'ARG', 'CG', 'HIS', 9.75), ('NH2', 'ARG', 'ND1', 'HIS', 10.41), ('NH2', 'ARG', 'CD2', 'HIS', 8.45), ('NH2', 'ARG', 'CE1', 'HIS', 9.69), ('NH2', 'ARG', 'NE2', 'HIS', 8.42)]]}
HIS_TYR = { 
	'distances':
		[[13.96, 12.63, 11.59, 12.6, 10.35, 11.47, 10.3, 9.28], [12.76, 11.38, 10.4, 11.25, 9.1, 10.07, 8.93, 7.84], [11.5, 10.15, 9.11, 10.13, 7.84, 9.04, 7.81, 6.84], [12.81, 11.36, 10.53, 11.04, 9.18, 9.76, 8.74, 7.51], [10.72, 9.3, 8.38, 9.13, 7.03, 7.93, 6.77, 5.66], [11.59, 10.12, 9.34, 9.75, 7.97, 8.44, 7.44, 6.18]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'TYR', 13.96), ('CB', 'HIS', 'CG', 'TYR', 12.63), ('CB', 'HIS', 'CD1', 'TYR', 11.59), ('CB', 'HIS', 'CD2', 'TYR', 12.6), ('CB', 'HIS', 'CE1', 'TYR', 10.35), ('CB', 'HIS', 'CE2', 'TYR', 11.47), ('CB', 'HIS', 'CZ', 'TYR', 10.3), ('CB', 'HIS', 'OH', 'TYR', 9.28)], [('CG', 'HIS', 'CB', 'TYR', 12.76), ('CG', 'HIS', 'CG', 'TYR', 11.38), ('CG', 'HIS', 'CD1', 'TYR', 10.4), ('CG', 'HIS', 'CD2', 'TYR', 11.25), ('CG', 'HIS', 'CE1', 'TYR', 9.1), ('CG', 'HIS', 'CE2', 'TYR', 10.07), ('CG', 'HIS', 'CZ', 'TYR', 8.93), ('CG', 'HIS', 'OH', 'TYR', 7.84)], [('ND1', 'HIS', 'CB', 'TYR', 11.5), ('ND1', 'HIS', 'CG', 'TYR', 10.15), ('ND1', 'HIS', 'CD1', 'TYR', 9.11), ('ND1', 'HIS', 'CD2', 'TYR', 10.13), ('ND1', 'HIS', 'CE1', 'TYR', 7.84), ('ND1', 'HIS', 'CE2', 'TYR', 9.04), ('ND1', 'HIS', 'CZ', 'TYR', 7.81), ('ND1', 'HIS', 'OH', 'TYR', 6.84)], [('CD2', 'HIS', 'CB', 'TYR', 12.81), ('CD2', 'HIS', 'CG', 'TYR', 11.36), ('CD2', 'HIS', 'CD1', 'TYR', 10.53), ('CD2', 'HIS', 'CD2', 'TYR', 11.04), ('CD2', 'HIS', 'CE1', 'TYR', 9.18), ('CD2', 'HIS', 'CE2', 'TYR', 9.76), ('CD2', 'HIS', 'CZ', 'TYR', 8.74), ('CD2', 'HIS', 'OH', 'TYR', 7.51)], [('CE1', 'HIS', 'CB', 'TYR', 10.72), ('CE1', 'HIS', 'CG', 'TYR', 9.3), ('CE1', 'HIS', 'CD1', 'TYR', 8.38), ('CE1', 'HIS', 'CD2', 'TYR', 9.13), ('CE1', 'HIS', 'CE1', 'TYR', 7.03), ('CE1', 'HIS', 'CE2', 'TYR', 7.93), ('CE1', 'HIS', 'CZ', 'TYR', 6.77), ('CE1', 'HIS', 'OH', 'TYR', 5.66)], [('NE2', 'HIS', 'CB', 'TYR', 11.59), ('NE2', 'HIS', 'CG', 'TYR', 10.12), ('NE2', 'HIS', 'CD1', 'TYR', 9.34), ('NE2', 'HIS', 'CD2', 'TYR', 9.75), ('NE2', 'HIS', 'CE1', 'TYR', 7.97), ('NE2', 'HIS', 'CE2', 'TYR', 8.44), ('NE2', 'HIS', 'CZ', 'TYR', 7.44), ('NE2', 'HIS', 'OH', 'TYR', 6.18)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_TYR, d, 'A_1gox_1_1_3_15')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(HIS_ASP, d, 'A_1gox_1_1_3_15')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASP, d, 'A_1gox_1_1_3_15')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_TYR, d, 'A_1gox_1_1_3_15')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_HIS, d, 'A_1gox_1_1_3_15')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(HIS_TYR, d, 'A_1gox_1_1_3_15')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_TYR' :  match1,
		'HIS_ASP' :  match2,
		'ARG_ASP' :  match3,
		'ASP_TYR' :  match4,
		'ARG_HIS' :  match5,
		'HIS_TYR' :  match6}