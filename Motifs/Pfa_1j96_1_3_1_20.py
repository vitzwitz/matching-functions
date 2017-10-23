'''
FUNC:Pfa_1j96_1_3_1_20
PDB:1j96
EC:1.3.1.20
RESI:asp,tyr,lys,his
LOCI:a-50,55,84,117;
'''
import motifFunctions as cmd
LYS_HIS = { 
	'distances':
		[[5.79, 5.77, 5.6, 6.57, 6.34, 6.87], [6.69, 6.34, 6.22, 6.74, 6.56, 6.86], [6.4, 5.73, 5.81, 5.72, 5.84, 5.79], [7.81, 7.01, 7.05, 6.68, 6.76, 6.52], [8.63, 7.63, 7.31, 7.3, 6.77, 6.75]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'HIS', 5.79), ('CB', 'LYS', 'CG', 'HIS', 5.77), ('CB', 'LYS', 'ND1', 'HIS', 5.6), ('CB', 'LYS', 'CD2', 'HIS', 6.57), ('CB', 'LYS', 'CE1', 'HIS', 6.34), ('CB', 'LYS', 'NE2', 'HIS', 6.87)], [('CG', 'LYS', 'CB', 'HIS', 6.69), ('CG', 'LYS', 'CG', 'HIS', 6.34), ('CG', 'LYS', 'ND1', 'HIS', 6.22), ('CG', 'LYS', 'CD2', 'HIS', 6.74), ('CG', 'LYS', 'CE1', 'HIS', 6.56), ('CG', 'LYS', 'NE2', 'HIS', 6.86)], [('CD', 'LYS', 'CB', 'HIS', 6.4), ('CD', 'LYS', 'CG', 'HIS', 5.73), ('CD', 'LYS', 'ND1', 'HIS', 5.81), ('CD', 'LYS', 'CD2', 'HIS', 5.72), ('CD', 'LYS', 'CE1', 'HIS', 5.84), ('CD', 'LYS', 'NE2', 'HIS', 5.79)], [('CE', 'LYS', 'CB', 'HIS', 7.81), ('CE', 'LYS', 'CG', 'HIS', 7.01), ('CE', 'LYS', 'ND1', 'HIS', 7.05), ('CE', 'LYS', 'CD2', 'HIS', 6.68), ('CE', 'LYS', 'CE1', 'HIS', 6.76), ('CE', 'LYS', 'NE2', 'HIS', 6.52)], [('NZ', 'LYS', 'CB', 'HIS', 8.63), ('NZ', 'LYS', 'CG', 'HIS', 7.63), ('NZ', 'LYS', 'ND1', 'HIS', 7.31), ('NZ', 'LYS', 'CD2', 'HIS', 7.3), ('NZ', 'LYS', 'CE1', 'HIS', 6.77), ('NZ', 'LYS', 'NE2', 'HIS', 6.75)]]}
ASP_HIS = { 
	'distances':
		[[13.33, 12.42, 12.08, 12.02, 11.47, 11.41], [11.88, 10.98, 10.73, 10.56, 10.15, 10.02], [11.44, 10.69, 10.58, 10.34, 10.16, 10.0], [11.32, 10.29, 9.97, 9.78, 9.26, 9.11]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 13.33), ('CB', 'ASP', 'CG', 'HIS', 12.42), ('CB', 'ASP', 'ND1', 'HIS', 12.08), ('CB', 'ASP', 'CD2', 'HIS', 12.02), ('CB', 'ASP', 'CE1', 'HIS', 11.47), ('CB', 'ASP', 'NE2', 'HIS', 11.41)], [('CG', 'ASP', 'CB', 'HIS', 11.88), ('CG', 'ASP', 'CG', 'HIS', 10.98), ('CG', 'ASP', 'ND1', 'HIS', 10.73), ('CG', 'ASP', 'CD2', 'HIS', 10.56), ('CG', 'ASP', 'CE1', 'HIS', 10.15), ('CG', 'ASP', 'NE2', 'HIS', 10.02)], [('OD1', 'ASP', 'CB', 'HIS', 11.44), ('OD1', 'ASP', 'CG', 'HIS', 10.69), ('OD1', 'ASP', 'ND1', 'HIS', 10.58), ('OD1', 'ASP', 'CD2', 'HIS', 10.34), ('OD1', 'ASP', 'CE1', 'HIS', 10.16), ('OD1', 'ASP', 'NE2', 'HIS', 10.0)], [('OD2', 'ASP', 'CB', 'HIS', 11.32), ('OD2', 'ASP', 'CG', 'HIS', 10.29), ('OD2', 'ASP', 'ND1', 'HIS', 9.97), ('OD2', 'ASP', 'CD2', 'HIS', 9.78), ('OD2', 'ASP', 'CE1', 'HIS', 9.26), ('OD2', 'ASP', 'NE2', 'HIS', 9.11)]]}
TYR_HIS = { 
	'distances':
		[[12.12, 10.9, 9.63, 10.93, 8.83, 9.69], [11.07, 9.78, 8.59, 9.67, 7.67, 8.4], [10.26, 8.9, 7.76, 8.7, 6.72, 7.38], [11.17, 9.89, 8.81, 9.71, 7.89, 8.49], [9.49, 8.06, 7.08, 7.66, 5.89, 6.3], [10.49, 9.17, 8.26, 8.83, 7.27, 7.64], [9.62, 8.21, 7.38, 7.75, 6.23, 6.48], [9.23, 7.83, 7.28, 7.15, 6.13, 6.0]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'HIS', 12.12), ('CB', 'TYR', 'CG', 'HIS', 10.9), ('CB', 'TYR', 'ND1', 'HIS', 9.63), ('CB', 'TYR', 'CD2', 'HIS', 10.93), ('CB', 'TYR', 'CE1', 'HIS', 8.83), ('CB', 'TYR', 'NE2', 'HIS', 9.69)], [('CG', 'TYR', 'CB', 'HIS', 11.07), ('CG', 'TYR', 'CG', 'HIS', 9.78), ('CG', 'TYR', 'ND1', 'HIS', 8.59), ('CG', 'TYR', 'CD2', 'HIS', 9.67), ('CG', 'TYR', 'CE1', 'HIS', 7.67), ('CG', 'TYR', 'NE2', 'HIS', 8.4)], [('CD1', 'TYR', 'CB', 'HIS', 10.26), ('CD1', 'TYR', 'CG', 'HIS', 8.9), ('CD1', 'TYR', 'ND1', 'HIS', 7.76), ('CD1', 'TYR', 'CD2', 'HIS', 8.7), ('CD1', 'TYR', 'CE1', 'HIS', 6.72), ('CD1', 'TYR', 'NE2', 'HIS', 7.38)], [('CD2', 'TYR', 'CB', 'HIS', 11.17), ('CD2', 'TYR', 'CG', 'HIS', 9.89), ('CD2', 'TYR', 'ND1', 'HIS', 8.81), ('CD2', 'TYR', 'CD2', 'HIS', 9.71), ('CD2', 'TYR', 'CE1', 'HIS', 7.89), ('CD2', 'TYR', 'NE2', 'HIS', 8.49)], [('CE1', 'TYR', 'CB', 'HIS', 9.49), ('CE1', 'TYR', 'CG', 'HIS', 8.06), ('CE1', 'TYR', 'ND1', 'HIS', 7.08), ('CE1', 'TYR', 'CD2', 'HIS', 7.66), ('CE1', 'TYR', 'CE1', 'HIS', 5.89), ('CE1', 'TYR', 'NE2', 'HIS', 6.3)], [('CE2', 'TYR', 'CB', 'HIS', 10.49), ('CE2', 'TYR', 'CG', 'HIS', 9.17), ('CE2', 'TYR', 'ND1', 'HIS', 8.26), ('CE2', 'TYR', 'CD2', 'HIS', 8.83), ('CE2', 'TYR', 'CE1', 'HIS', 7.27), ('CE2', 'TYR', 'NE2', 'HIS', 7.64)], [('CZ', 'TYR', 'CB', 'HIS', 9.62), ('CZ', 'TYR', 'CG', 'HIS', 8.21), ('CZ', 'TYR', 'ND1', 'HIS', 7.38), ('CZ', 'TYR', 'CD2', 'HIS', 7.75), ('CZ', 'TYR', 'CE1', 'HIS', 6.23), ('CZ', 'TYR', 'NE2', 'HIS', 6.48)], [('OH', 'TYR', 'CB', 'HIS', 9.23), ('OH', 'TYR', 'CG', 'HIS', 7.83), ('OH', 'TYR', 'ND1', 'HIS', 7.28), ('OH', 'TYR', 'CD2', 'HIS', 7.15), ('OH', 'TYR', 'CE1', 'HIS', 6.13), ('OH', 'TYR', 'NE2', 'HIS', 6.0)]]}
ASP_TYR = { 
	'distances':
		[[11.16, 10.17, 10.74, 8.79, 10.15, 7.99, 8.79, 8.33], [10.75, 9.61, 9.99, 8.3, 9.24, 7.31, 7.88, 7.24], [11.54, 10.37, 10.66, 9.12, 9.85, 8.09, 8.53, 7.79], [9.84, 8.61, 8.89, 7.35, 8.09, 6.24, 6.72, 6.05]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'TYR', 11.16), ('CB', 'ASP', 'CG', 'TYR', 10.17), ('CB', 'ASP', 'CD1', 'TYR', 10.74), ('CB', 'ASP', 'CD2', 'TYR', 8.79), ('CB', 'ASP', 'CE1', 'TYR', 10.15), ('CB', 'ASP', 'CE2', 'TYR', 7.99), ('CB', 'ASP', 'CZ', 'TYR', 8.79), ('CB', 'ASP', 'OH', 'TYR', 8.33)], [('CG', 'ASP', 'CB', 'TYR', 10.75), ('CG', 'ASP', 'CG', 'TYR', 9.61), ('CG', 'ASP', 'CD1', 'TYR', 9.99), ('CG', 'ASP', 'CD2', 'TYR', 8.3), ('CG', 'ASP', 'CE1', 'TYR', 9.24), ('CG', 'ASP', 'CE2', 'TYR', 7.31), ('CG', 'ASP', 'CZ', 'TYR', 7.88), ('CG', 'ASP', 'OH', 'TYR', 7.24)], [('OD1', 'ASP', 'CB', 'TYR', 11.54), ('OD1', 'ASP', 'CG', 'TYR', 10.37), ('OD1', 'ASP', 'CD1', 'TYR', 10.66), ('OD1', 'ASP', 'CD2', 'TYR', 9.12), ('OD1', 'ASP', 'CE1', 'TYR', 9.85), ('OD1', 'ASP', 'CE2', 'TYR', 8.09), ('OD1', 'ASP', 'CZ', 'TYR', 8.53), ('OD1', 'ASP', 'OH', 'TYR', 7.79)], [('OD2', 'ASP', 'CB', 'TYR', 9.84), ('OD2', 'ASP', 'CG', 'TYR', 8.61), ('OD2', 'ASP', 'CD1', 'TYR', 8.89), ('OD2', 'ASP', 'CD2', 'TYR', 7.35), ('OD2', 'ASP', 'CE1', 'TYR', 8.09), ('OD2', 'ASP', 'CE2', 'TYR', 6.24), ('OD2', 'ASP', 'CZ', 'TYR', 6.72), ('OD2', 'ASP', 'OH', 'TYR', 6.05)]]}
ASP_LYS = { 
	'distances':
		[[10.62, 9.17, 8.96, 7.62, 6.8], [9.34, 7.86, 7.52, 6.13, 5.41], [8.82, 7.3, 7.06, 5.7, 5.43], [9.07, 7.65, 7.1, 5.72, 4.74]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 10.62), ('CB', 'ASP', 'CG', 'LYS', 9.17), ('CB', 'ASP', 'CD', 'LYS', 8.96), ('CB', 'ASP', 'CE', 'LYS', 7.62), ('CB', 'ASP', 'NZ', 'LYS', 6.8)], [('CG', 'ASP', 'CB', 'LYS', 9.34), ('CG', 'ASP', 'CG', 'LYS', 7.86), ('CG', 'ASP', 'CD', 'LYS', 7.52), ('CG', 'ASP', 'CE', 'LYS', 6.13), ('CG', 'ASP', 'NZ', 'LYS', 5.41)], [('OD1', 'ASP', 'CB', 'LYS', 8.82), ('OD1', 'ASP', 'CG', 'LYS', 7.3), ('OD1', 'ASP', 'CD', 'LYS', 7.06), ('OD1', 'ASP', 'CE', 'LYS', 5.7), ('OD1', 'ASP', 'NZ', 'LYS', 5.43)], [('OD2', 'ASP', 'CB', 'LYS', 9.07), ('OD2', 'ASP', 'CG', 'LYS', 7.65), ('OD2', 'ASP', 'CD', 'LYS', 7.1), ('OD2', 'ASP', 'CE', 'LYS', 5.72), ('OD2', 'ASP', 'NZ', 'LYS', 4.74)]]}
TYR_LYS = { 
	'distances':
		[[10.71, 10.51, 10.41, 10.43, 9.15], [9.76, 9.42, 9.15, 9.09, 7.82], [9.51, 9.27, 8.8, 8.87, 7.77], [9.44, 8.86, 8.59, 8.29, 6.9], [8.93, 8.55, 7.86, 7.84, 6.84], [8.86, 8.09, 7.61, 7.14, 5.75], [8.58, 7.92, 7.18, 6.87, 5.71], [8.34, 7.5, 6.5, 5.98, 5.0]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 10.71), ('CB', 'TYR', 'CG', 'LYS', 10.51), ('CB', 'TYR', 'CD', 'LYS', 10.41), ('CB', 'TYR', 'CE', 'LYS', 10.43), ('CB', 'TYR', 'NZ', 'LYS', 9.15)], [('CG', 'TYR', 'CB', 'LYS', 9.76), ('CG', 'TYR', 'CG', 'LYS', 9.42), ('CG', 'TYR', 'CD', 'LYS', 9.15), ('CG', 'TYR', 'CE', 'LYS', 9.09), ('CG', 'TYR', 'NZ', 'LYS', 7.82)], [('CD1', 'TYR', 'CB', 'LYS', 9.51), ('CD1', 'TYR', 'CG', 'LYS', 9.27), ('CD1', 'TYR', 'CD', 'LYS', 8.8), ('CD1', 'TYR', 'CE', 'LYS', 8.87), ('CD1', 'TYR', 'NZ', 'LYS', 7.77)], [('CD2', 'TYR', 'CB', 'LYS', 9.44), ('CD2', 'TYR', 'CG', 'LYS', 8.86), ('CD2', 'TYR', 'CD', 'LYS', 8.59), ('CD2', 'TYR', 'CE', 'LYS', 8.29), ('CD2', 'TYR', 'NZ', 'LYS', 6.9)], [('CE1', 'TYR', 'CB', 'LYS', 8.93), ('CE1', 'TYR', 'CG', 'LYS', 8.55), ('CE1', 'TYR', 'CD', 'LYS', 7.86), ('CE1', 'TYR', 'CE', 'LYS', 7.84), ('CE1', 'TYR', 'NZ', 'LYS', 6.84)], [('CE2', 'TYR', 'CB', 'LYS', 8.86), ('CE2', 'TYR', 'CG', 'LYS', 8.09), ('CE2', 'TYR', 'CD', 'LYS', 7.61), ('CE2', 'TYR', 'CE', 'LYS', 7.14), ('CE2', 'TYR', 'NZ', 'LYS', 5.75)], [('CZ', 'TYR', 'CB', 'LYS', 8.58), ('CZ', 'TYR', 'CG', 'LYS', 7.92), ('CZ', 'TYR', 'CD', 'LYS', 7.18), ('CZ', 'TYR', 'CE', 'LYS', 6.87), ('CZ', 'TYR', 'NZ', 'LYS', 5.71)], [('OH', 'TYR', 'CB', 'LYS', 8.34), ('OH', 'TYR', 'CG', 'LYS', 7.5), ('OH', 'TYR', 'CD', 'LYS', 6.5), ('OH', 'TYR', 'CE', 'LYS', 5.98), ('OH', 'TYR', 'NZ', 'LYS', 5.0)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_HIS, d, 'Pfa_1j96_1_3_1_20')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'Pfa_1j96_1_3_1_20')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_HIS, d, 'Pfa_1j96_1_3_1_20')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_TYR, d, 'Pfa_1j96_1_3_1_20')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_LYS, d, 'Pfa_1j96_1_3_1_20')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(TYR_LYS, d, 'Pfa_1j96_1_3_1_20')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_HIS' :  match1,
		'ASP_HIS' :  match2,
		'TYR_HIS' :  match3,
		'ASP_TYR' :  match4,
		'ASP_LYS' :  match5,
		'TYR_LYS' :  match6}