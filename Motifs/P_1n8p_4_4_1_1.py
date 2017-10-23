'''
FUNC:P_1n8p_4_4_1_1
PDB:1n8p
EC:4.4.1.1
RESI:tyr,asp,lys
LOCI:a-103,178,203;
'''
import motifFunctions as cmd
TYR_ASP = { 
	'distances':
		[[10.2, 9.35, 9.77, 8.47], [10.69, 9.67, 9.86, 8.9], [10.54, 9.55, 9.58, 8.98], [11.57, 10.43, 10.54, 9.59], [11.29, 10.19, 10.02, 9.72], [12.25, 11.01, 10.93, 10.28], [12.11, 10.9, 10.69, 10.33], [12.99, 11.73, 11.36, 11.26]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'ASP', 10.2), ('CB', 'TYR', 'CG', 'ASP', 9.35), ('CB', 'TYR', 'OD1', 'ASP', 9.77), ('CB', 'TYR', 'OD2', 'ASP', 8.47)], [('CG', 'TYR', 'CB', 'ASP', 10.69), ('CG', 'TYR', 'CG', 'ASP', 9.67), ('CG', 'TYR', 'OD1', 'ASP', 9.86), ('CG', 'TYR', 'OD2', 'ASP', 8.9)], [('CD1', 'TYR', 'CB', 'ASP', 10.54), ('CD1', 'TYR', 'CG', 'ASP', 9.55), ('CD1', 'TYR', 'OD1', 'ASP', 9.58), ('CD1', 'TYR', 'OD2', 'ASP', 8.98)], [('CD2', 'TYR', 'CB', 'ASP', 11.57), ('CD2', 'TYR', 'CG', 'ASP', 10.43), ('CD2', 'TYR', 'OD1', 'ASP', 10.54), ('CD2', 'TYR', 'OD2', 'ASP', 9.59)], [('CE1', 'TYR', 'CB', 'ASP', 11.29), ('CE1', 'TYR', 'CG', 'ASP', 10.19), ('CE1', 'TYR', 'OD1', 'ASP', 10.02), ('CE1', 'TYR', 'OD2', 'ASP', 9.72)], [('CE2', 'TYR', 'CB', 'ASP', 12.25), ('CE2', 'TYR', 'CG', 'ASP', 11.01), ('CE2', 'TYR', 'OD1', 'ASP', 10.93), ('CE2', 'TYR', 'OD2', 'ASP', 10.28)], [('CZ', 'TYR', 'CB', 'ASP', 12.11), ('CZ', 'TYR', 'CG', 'ASP', 10.9), ('CZ', 'TYR', 'OD1', 'ASP', 10.69), ('CZ', 'TYR', 'OD2', 'ASP', 10.33)], [('OH', 'TYR', 'CB', 'ASP', 12.99), ('OH', 'TYR', 'CG', 'ASP', 11.73), ('OH', 'TYR', 'OD1', 'ASP', 11.36), ('OH', 'TYR', 'OD2', 'ASP', 11.26)]]}
ASP_LYS = { 
	'distances':
		[[12.85, 12.72, 12.5, 13.02, 12.43], [11.6, 11.4, 11.09, 11.58, 10.95], [10.48, 10.38, 10.17, 10.79, 10.31], [11.86, 11.51, 11.02, 11.37, 10.57]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 12.85), ('CB', 'ASP', 'CG', 'LYS', 12.72), ('CB', 'ASP', 'CD', 'LYS', 12.5), ('CB', 'ASP', 'CE', 'LYS', 13.02), ('CB', 'ASP', 'NZ', 'LYS', 12.43)], [('CG', 'ASP', 'CB', 'LYS', 11.6), ('CG', 'ASP', 'CG', 'LYS', 11.4), ('CG', 'ASP', 'CD', 'LYS', 11.09), ('CG', 'ASP', 'CE', 'LYS', 11.58), ('CG', 'ASP', 'NZ', 'LYS', 10.95)], [('OD1', 'ASP', 'CB', 'LYS', 10.48), ('OD1', 'ASP', 'CG', 'LYS', 10.38), ('OD1', 'ASP', 'CD', 'LYS', 10.17), ('OD1', 'ASP', 'CE', 'LYS', 10.79), ('OD1', 'ASP', 'NZ', 'LYS', 10.31)], [('OD2', 'ASP', 'CB', 'LYS', 11.86), ('OD2', 'ASP', 'CG', 'LYS', 11.51), ('OD2', 'ASP', 'CD', 'LYS', 11.02), ('OD2', 'ASP', 'CE', 'LYS', 11.37), ('OD2', 'ASP', 'NZ', 'LYS', 10.57)]]}
TYR_LYS = { 
	'distances':
		[[13.43, 12.26, 11.57, 10.86, 9.8], [12.31, 11.06, 10.39, 9.55, 8.56], [11.64, 10.39, 9.92, 9.13, 8.37], [12.12, 10.81, 9.97, 8.99, 7.88], [10.73, 9.38, 8.99, 8.07, 7.48], [11.26, 9.86, 9.04, 7.91, 6.9], [10.52, 9.09, 8.5, 7.38, 6.66], [9.84, 8.34, 7.83, 6.56, 6.11]],
	'comparisons':
		[[('CB', 'TYR', 'CB', 'LYS', 13.43), ('CB', 'TYR', 'CG', 'LYS', 12.26), ('CB', 'TYR', 'CD', 'LYS', 11.57), ('CB', 'TYR', 'CE', 'LYS', 10.86), ('CB', 'TYR', 'NZ', 'LYS', 9.8)], [('CG', 'TYR', 'CB', 'LYS', 12.31), ('CG', 'TYR', 'CG', 'LYS', 11.06), ('CG', 'TYR', 'CD', 'LYS', 10.39), ('CG', 'TYR', 'CE', 'LYS', 9.55), ('CG', 'TYR', 'NZ', 'LYS', 8.56)], [('CD1', 'TYR', 'CB', 'LYS', 11.64), ('CD1', 'TYR', 'CG', 'LYS', 10.39), ('CD1', 'TYR', 'CD', 'LYS', 9.92), ('CD1', 'TYR', 'CE', 'LYS', 9.13), ('CD1', 'TYR', 'NZ', 'LYS', 8.37)], [('CD2', 'TYR', 'CB', 'LYS', 12.12), ('CD2', 'TYR', 'CG', 'LYS', 10.81), ('CD2', 'TYR', 'CD', 'LYS', 9.97), ('CD2', 'TYR', 'CE', 'LYS', 8.99), ('CD2', 'TYR', 'NZ', 'LYS', 7.88)], [('CE1', 'TYR', 'CB', 'LYS', 10.73), ('CE1', 'TYR', 'CG', 'LYS', 9.38), ('CE1', 'TYR', 'CD', 'LYS', 8.99), ('CE1', 'TYR', 'CE', 'LYS', 8.07), ('CE1', 'TYR', 'NZ', 'LYS', 7.48)], [('CE2', 'TYR', 'CB', 'LYS', 11.26), ('CE2', 'TYR', 'CG', 'LYS', 9.86), ('CE2', 'TYR', 'CD', 'LYS', 9.04), ('CE2', 'TYR', 'CE', 'LYS', 7.91), ('CE2', 'TYR', 'NZ', 'LYS', 6.9)], [('CZ', 'TYR', 'CB', 'LYS', 10.52), ('CZ', 'TYR', 'CG', 'LYS', 9.09), ('CZ', 'TYR', 'CD', 'LYS', 8.5), ('CZ', 'TYR', 'CE', 'LYS', 7.38), ('CZ', 'TYR', 'NZ', 'LYS', 6.66)], [('OH', 'TYR', 'CB', 'LYS', 9.84), ('OH', 'TYR', 'CG', 'LYS', 8.34), ('OH', 'TYR', 'CD', 'LYS', 7.83), ('OH', 'TYR', 'CE', 'LYS', 6.56), ('OH', 'TYR', 'NZ', 'LYS', 6.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(TYR_ASP, d, 'P_1n8p_4_4_1_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_LYS, d, 'P_1n8p_4_4_1_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(TYR_LYS, d, 'P_1n8p_4_4_1_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'TYR_ASP' :  match1,
		'ASP_LYS' :  match2,
		'TYR_LYS' :  match3}