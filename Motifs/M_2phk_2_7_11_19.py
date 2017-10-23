'''
FUNC:M_2phk_2_7_11_19
PDB:2phk
EC:2.7.11.19
RESI:asp,lys,mn,mn
LOCI:a-149,151,382,383;
'''
import motifFunctions as cmd
MN_MN = { 
	'distances':
		[5.91, 5.91],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 5.91), ('MN', 'MN', 'MN', 'MN', 5.91)]}
LYS_ASP = { 
	'distances':
		[[8.5, 7.92, 7.18, 8.48], [7.79, 7.02, 6.45, 7.35], [8.02, 6.93, 6.19, 7.11], [7.88, 6.62, 6.17, 6.43], [8.05, 6.61, 6.09, 6.28]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 8.5), ('CB', 'LYS', 'CG', 'ASP', 7.92), ('CB', 'LYS', 'OD1', 'ASP', 7.18), ('CB', 'LYS', 'OD2', 'ASP', 8.48)], [('CG', 'LYS', 'CB', 'ASP', 7.79), ('CG', 'LYS', 'CG', 'ASP', 7.02), ('CG', 'LYS', 'OD1', 'ASP', 6.45), ('CG', 'LYS', 'OD2', 'ASP', 7.35)], [('CD', 'LYS', 'CB', 'ASP', 8.02), ('CD', 'LYS', 'CG', 'ASP', 6.93), ('CD', 'LYS', 'OD1', 'ASP', 6.19), ('CD', 'LYS', 'OD2', 'ASP', 7.11)], [('CE', 'LYS', 'CB', 'ASP', 7.88), ('CE', 'LYS', 'CG', 'ASP', 6.62), ('CE', 'LYS', 'OD1', 'ASP', 6.17), ('CE', 'LYS', 'OD2', 'ASP', 6.43)], [('NZ', 'LYS', 'CB', 'ASP', 8.05), ('NZ', 'LYS', 'CG', 'ASP', 6.61), ('NZ', 'LYS', 'OD1', 'ASP', 6.09), ('NZ', 'LYS', 'OD2', 'ASP', 6.28)]]}
ASP_MN = { 
	'distances':
		[[7.69], [7.1], [8.07], [5.91], [8.64], [7.71], [8.22], [6.73]],
	'comparisons':
		[[('CB', 'ASP', 'MN', 'MN', 7.69)], [('CG', 'ASP', 'MN', 'MN', 7.1)], [('OD1', 'ASP', 'MN', 'MN', 8.07)], [('OD2', 'ASP', 'MN', 'MN', 5.91)], [('CB', 'ASP', 'MN', 'MN', 8.64)], [('CG', 'ASP', 'MN', 'MN', 7.71)], [('OD1', 'ASP', 'MN', 'MN', 8.22)], [('OD2', 'ASP', 'MN', 'MN', 6.73)]]}
LYS_MN = { 
	'distances':
		[[11.63], [10.24], [9.91], [8.66], [8.36], [9.46], [7.96], [7.71], [6.31], [6.58]],
	'comparisons':
		[[('CB', 'LYS', 'MN', 'MN', 11.63)], [('CG', 'LYS', 'MN', 'MN', 10.24)], [('CD', 'LYS', 'MN', 'MN', 9.91)], [('CE', 'LYS', 'MN', 'MN', 8.66)], [('NZ', 'LYS', 'MN', 'MN', 8.36)], [('CB', 'LYS', 'MN', 'MN', 9.46)], [('CG', 'LYS', 'MN', 'MN', 7.96)], [('CD', 'LYS', 'MN', 'MN', 7.71)], [('CE', 'LYS', 'MN', 'MN', 6.31)], [('NZ', 'LYS', 'MN', 'MN', 6.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MN_MN, d, 'M_2phk_2_7_11_19')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ASP, d, 'M_2phk_2_7_11_19')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_MN, d, 'M_2phk_2_7_11_19')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(LYS_MN, d, 'M_2phk_2_7_11_19')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MN_MN' :  match1,
		'LYS_ASP' :  match2,
		'ASP_MN' :  match3,
		'LYS_MN' :  match4}