'''
FUNC:A_1ok4_4_1_2_13
PDB:1ok4
EC:4.1.2.13
RESI:asp,tyr,lys
LOCI:a-24,146,177;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[14.57, 13.26, 13.46, 12.12], [13.53, 12.15, 12.24, 11.07], [13.95, 12.52, 12.47, 11.51], [12.27, 10.9, 11.01, 9.82], [13.23, 11.74, 11.57, 10.84], [11.41, 9.96, 9.93, 8.97], [11.95, 10.46, 10.27, 9.57], [11.41, 9.88, 9.51, 9.15]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 14.57), ('CB', 'TYR', 'CG', 'ASP', 13.26), ('CB', 'TYR', 'OD1', 'ASP', 13.46), ('CB', 'TYR', 'OD2', 'ASP', 12.12)], [('CG', 'TYR', 'CB', 'ASP', 13.53), ('CG', 'TYR', 'CG', 'ASP', 12.15), ('CG', 'TYR', 'OD1', 'ASP', 12.24), ('CG', 'TYR', 'OD2', 'ASP', 11.07)], [('CD1', 'TYR', 'CB', 'ASP', 13.95), ('CD1', 'TYR', 'CG', 'ASP', 12.52), ('CD1', 'TYR', 'OD1', 'ASP', 12.47), ('CD1', 'TYR', 'OD2', 'ASP', 11.51)], [('CD2', 'TYR', 'CB', 'ASP', 12.27), ('CD2', 'TYR', 'CG', 'ASP', 10.9), ('CD2', 'TYR', 'OD1', 'ASP', 11.01), ('CD2', 'TYR', 'OD2', 'ASP', 9.82)], [('CE1', 'TYR', 'CB', 'ASP', 13.23), ('CE1', 'TYR', 'CG', 'ASP', 11.74), ('CE1', 'TYR', 'OD1', 'ASP', 11.57), ('CE1', 'TYR', 'OD2', 'ASP', 10.84)], [('CE2', 'TYR', 'CB', 'ASP', 11.41), ('CE2', 'TYR', 'CG', 'ASP', 9.96), ('CE2', 'TYR', 'OD1', 'ASP', 9.93), ('CE2', 'TYR', 'OD2', 'ASP', 8.97)], [('CZ', 'TYR', 'CB', 'ASP', 11.95), ('CZ', 'TYR', 'CG', 'ASP', 10.46), ('CZ', 'TYR', 'OD1', 'ASP', 10.27), ('CZ', 'TYR', 'OD2', 'ASP', 9.57)], [('OH', 'TYR', 'CB', 'ASP', 11.41), ('OH', 'TYR', 'CG', 'ASP', 9.88), ('OH', 'TYR', 'OD1', 'ASP', 9.51), ('OH', 'TYR', 'OD2', 'ASP', 9.15)]]}
LYS_ASP = { 
	'distances':
		[[12.96, 11.67, 11.35, 11.11], [12.43, 11.06, 10.59, 10.58], [10.93, 9.57, 9.08, 9.15], [10.63, 9.2, 8.53, 8.9], [9.23, 7.79, 7.07, 7.58]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 12.96), ('CB', 'LYS', 'CG', 'ASP', 11.67), ('CB', 'LYS', 'OD1', 'ASP', 11.35), ('CB', 'LYS', 'OD2', 'ASP', 11.11)], [('CG', 'LYS', 'CB', 'ASP', 12.43), ('CG', 'LYS', 'CG', 'ASP', 11.06), ('CG', 'LYS', 'OD1', 'ASP', 10.59), ('CG', 'LYS', 'OD2', 'ASP', 10.58)], [('CD', 'LYS', 'CB', 'ASP', 10.93), ('CD', 'LYS', 'CG', 'ASP', 9.57), ('CD', 'LYS', 'OD1', 'ASP', 9.08), ('CD', 'LYS', 'OD2', 'ASP', 9.15)], [('CE', 'LYS', 'CB', 'ASP', 10.63), ('CE', 'LYS', 'CG', 'ASP', 9.2), ('CE', 'LYS', 'OD1', 'ASP', 8.53), ('CE', 'LYS', 'OD2', 'ASP', 8.9)], [('NZ', 'LYS', 'CB', 'ASP', 9.23), ('NZ', 'LYS', 'CG', 'ASP', 7.79), ('NZ', 'LYS', 'OD1', 'ASP', 7.07), ('NZ', 'LYS', 'OD2', 'ASP', 7.58)]]}
LYS_TYR = { 
	'distances':
		[[10.52, 9.3, 8.37, 9.38, 7.42, 8.58, 7.56, 7.05], [10.44, 9.07, 8.11, 8.99, 6.94, 7.99, 6.87, 6.06], [10.6, 9.17, 8.46, 8.8, 7.24, 7.66, 6.77, 5.8], [10.81, 9.3, 8.63, 8.78, 7.3, 7.49, 6.61, 5.36], [11.09, 9.59, 9.17, 8.82, 7.91, 7.47, 6.93, 5.71]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'TYR', 10.52), ('CB', 'LYS', 'CG', 'TYR', 9.3), ('CB', 'LYS', 'CD1', 'TYR', 8.37), ('CB', 'LYS', 'CD2', 'TYR', 9.38), ('CB', 'LYS', 'CE1', 'TYR', 7.42), ('CB', 'LYS', 'CE2', 'TYR', 8.58), ('CB', 'LYS', 'CZ', 'TYR', 7.56), ('CB', 'LYS', 'OH', 'TYR', 7.05)], [('CG', 'LYS', 'CB', 'TYR', 10.44), ('CG', 'LYS', 'CG', 'TYR', 9.07), ('CG', 'LYS', 'CD1', 'TYR', 8.11), ('CG', 'LYS', 'CD2', 'TYR', 8.99), ('CG', 'LYS', 'CE1', 'TYR', 6.94), ('CG', 'LYS', 'CE2', 'TYR', 7.99), ('CG', 'LYS', 'CZ', 'TYR', 6.87), ('CG', 'LYS', 'OH', 'TYR', 6.06)], [('CD', 'LYS', 'CB', 'TYR', 10.6), ('CD', 'LYS', 'CG', 'TYR', 9.17), ('CD', 'LYS', 'CD1', 'TYR', 8.46), ('CD', 'LYS', 'CD2', 'TYR', 8.8), ('CD', 'LYS', 'CE1', 'TYR', 7.24), ('CD', 'LYS', 'CE2', 'TYR', 7.66), ('CD', 'LYS', 'CZ', 'TYR', 6.77), ('CD', 'LYS', 'OH', 'TYR', 5.8)], [('CE', 'LYS', 'CB', 'TYR', 10.81), ('CE', 'LYS', 'CG', 'TYR', 9.3), ('CE', 'LYS', 'CD1', 'TYR', 8.63), ('CE', 'LYS', 'CD2', 'TYR', 8.78), ('CE', 'LYS', 'CE1', 'TYR', 7.3), ('CE', 'LYS', 'CE2', 'TYR', 7.49), ('CE', 'LYS', 'CZ', 'TYR', 6.61), ('CE', 'LYS', 'OH', 'TYR', 5.36)], [('NZ', 'LYS', 'CB', 'TYR', 11.09), ('NZ', 'LYS', 'CG', 'TYR', 9.59), ('NZ', 'LYS', 'CD1', 'TYR', 9.17), ('NZ', 'LYS', 'CD2', 'TYR', 8.82), ('NZ', 'LYS', 'CE1', 'TYR', 7.91), ('NZ', 'LYS', 'CE2', 'TYR', 7.47), ('NZ', 'LYS', 'CZ', 'TYR', 6.93), ('NZ', 'LYS', 'OH', 'TYR', 5.71)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'A_1ok4_4_1_2_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ASP, d, 'A_1ok4_4_1_2_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_TYR, d, 'A_1ok4_4_1_2_13')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'LYS_ASP' :  match2,
		'LYS_TYR' :  match3}