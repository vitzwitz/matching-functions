'''
FUNC:P_1aw5_4_2_1_24
PDB:1aw5
EC:4.2.1.24
RESI:asp,ser,lys,lys
LOCI:a-131,179,210,263;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[13.32, 12.58, 11.33, 11.53, 10.55], [12.11, 11.33, 10.02, 10.13, 9.13], [10.99, 10.23, 8.98, 9.24, 8.34], [12.4, 11.57, 10.18, 10.07, 9.0], [12.97, 12.75, 11.26, 11.19, 9.84], [12.13, 11.85, 10.38, 10.24, 8.81], [10.94, 10.74, 9.29, 9.29, 7.9], [12.77, 12.39, 10.93, 10.63, 9.14]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 13.32), ('CB', 'ASP', 'CG', 'LYS', 12.58), ('CB', 'ASP', 'CD', 'LYS', 11.33), ('CB', 'ASP', 'CE', 'LYS', 11.53), ('CB', 'ASP', 'NZ', 'LYS', 10.55)], [('CG', 'ASP', 'CB', 'LYS', 12.11), ('CG', 'ASP', 'CG', 'LYS', 11.33), ('CG', 'ASP', 'CD', 'LYS', 10.02), ('CG', 'ASP', 'CE', 'LYS', 10.13), ('CG', 'ASP', 'NZ', 'LYS', 9.13)], [('OD1', 'ASP', 'CB', 'LYS', 10.99), ('OD1', 'ASP', 'CG', 'LYS', 10.23), ('OD1', 'ASP', 'CD', 'LYS', 8.98), ('OD1', 'ASP', 'CE', 'LYS', 9.24), ('OD1', 'ASP', 'NZ', 'LYS', 8.34)], [('OD2', 'ASP', 'CB', 'LYS', 12.4), ('OD2', 'ASP', 'CG', 'LYS', 11.57), ('OD2', 'ASP', 'CD', 'LYS', 10.18), ('OD2', 'ASP', 'CE', 'LYS', 10.07), ('OD2', 'ASP', 'NZ', 'LYS', 9.0)], [('CB', 'ASP', 'CB', 'LYS', 12.97), ('CB', 'ASP', 'CG', 'LYS', 12.75), ('CB', 'ASP', 'CD', 'LYS', 11.26), ('CB', 'ASP', 'CE', 'LYS', 11.19), ('CB', 'ASP', 'NZ', 'LYS', 9.84)], [('CG', 'ASP', 'CB', 'LYS', 12.13), ('CG', 'ASP', 'CG', 'LYS', 11.85), ('CG', 'ASP', 'CD', 'LYS', 10.38), ('CG', 'ASP', 'CE', 'LYS', 10.24), ('CG', 'ASP', 'NZ', 'LYS', 8.81)], [('OD1', 'ASP', 'CB', 'LYS', 10.94), ('OD1', 'ASP', 'CG', 'LYS', 10.74), ('OD1', 'ASP', 'CD', 'LYS', 9.29), ('OD1', 'ASP', 'CE', 'LYS', 9.29), ('OD1', 'ASP', 'NZ', 'LYS', 7.9)], [('OD2', 'ASP', 'CB', 'LYS', 12.77), ('OD2', 'ASP', 'CG', 'LYS', 12.39), ('OD2', 'ASP', 'CD', 'LYS', 10.93), ('OD2', 'ASP', 'CE', 'LYS', 10.63), ('OD2', 'ASP', 'NZ', 'LYS', 9.14)]]}
SER_LYS = { 
	'distances':
		[[8.05, 7.57, 6.24, 6.69, 6.4], [9.26, 8.63, 7.21, 7.32, 6.7], [9.59, 9.64, 8.52, 8.77, 7.57], [10.6, 10.47, 9.23, 9.23, 7.86]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 8.05), ('CB', 'SER', 'CG', 'LYS', 7.57), ('CB', 'SER', 'CD', 'LYS', 6.24), ('CB', 'SER', 'CE', 'LYS', 6.69), ('CB', 'SER', 'NZ', 'LYS', 6.4)], [('OG', 'SER', 'CB', 'LYS', 9.26), ('OG', 'SER', 'CG', 'LYS', 8.63), ('OG', 'SER', 'CD', 'LYS', 7.21), ('OG', 'SER', 'CE', 'LYS', 7.32), ('OG', 'SER', 'NZ', 'LYS', 6.7)], [('CB', 'SER', 'CB', 'LYS', 9.59), ('CB', 'SER', 'CG', 'LYS', 9.64), ('CB', 'SER', 'CD', 'LYS', 8.52), ('CB', 'SER', 'CE', 'LYS', 8.77), ('CB', 'SER', 'NZ', 'LYS', 7.57)], [('OG', 'SER', 'CB', 'LYS', 10.6), ('OG', 'SER', 'CG', 'LYS', 10.47), ('OG', 'SER', 'CD', 'LYS', 9.23), ('OG', 'SER', 'CE', 'LYS', 9.23), ('OG', 'SER', 'NZ', 'LYS', 7.86)]]}
LYS_LYS = { 
	'distances':
		[[6.8, 7.31, 7.55, 8.26, 8.32], [6.28, 6.39, 6.46, 6.94, 6.97], [7.09, 7.03, 6.63, 6.9, 6.47], [8.11, 7.72, 7.27, 7.08, 6.52], [8.44, 7.81, 7.04, 6.53, 5.66], [6.8, 6.28, 7.09, 8.11, 8.44], [7.31, 6.39, 7.03, 7.72, 7.81], [7.55, 6.46, 6.63, 7.27, 7.04], [8.26, 6.94, 6.9, 7.08, 6.53], [8.32, 6.97, 6.47, 6.52, 5.66]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'LYS', 6.8), ('CB', 'LYS', 'CG', 'LYS', 7.31), ('CB', 'LYS', 'CD', 'LYS', 7.55), ('CB', 'LYS', 'CE', 'LYS', 8.26), ('CB', 'LYS', 'NZ', 'LYS', 8.32)], [('CG', 'LYS', 'CB', 'LYS', 6.28), ('CG', 'LYS', 'CG', 'LYS', 6.39), ('CG', 'LYS', 'CD', 'LYS', 6.46), ('CG', 'LYS', 'CE', 'LYS', 6.94), ('CG', 'LYS', 'NZ', 'LYS', 6.97)], [('CD', 'LYS', 'CB', 'LYS', 7.09), ('CD', 'LYS', 'CG', 'LYS', 7.03), ('CD', 'LYS', 'CD', 'LYS', 6.63), ('CD', 'LYS', 'CE', 'LYS', 6.9), ('CD', 'LYS', 'NZ', 'LYS', 6.47)], [('CE', 'LYS', 'CB', 'LYS', 8.11), ('CE', 'LYS', 'CG', 'LYS', 7.72), ('CE', 'LYS', 'CD', 'LYS', 7.27), ('CE', 'LYS', 'CE', 'LYS', 7.08), ('CE', 'LYS', 'NZ', 'LYS', 6.52)], [('NZ', 'LYS', 'CB', 'LYS', 8.44), ('NZ', 'LYS', 'CG', 'LYS', 7.81), ('NZ', 'LYS', 'CD', 'LYS', 7.04), ('NZ', 'LYS', 'CE', 'LYS', 6.53), ('NZ', 'LYS', 'NZ', 'LYS', 5.66)], [('CB', 'LYS', 'CB', 'LYS', 6.8), ('CB', 'LYS', 'CG', 'LYS', 6.28), ('CB', 'LYS', 'CD', 'LYS', 7.09), ('CB', 'LYS', 'CE', 'LYS', 8.11), ('CB', 'LYS', 'NZ', 'LYS', 8.44)], [('CG', 'LYS', 'CB', 'LYS', 7.31), ('CG', 'LYS', 'CG', 'LYS', 6.39), ('CG', 'LYS', 'CD', 'LYS', 7.03), ('CG', 'LYS', 'CE', 'LYS', 7.72), ('CG', 'LYS', 'NZ', 'LYS', 7.81)], [('CD', 'LYS', 'CB', 'LYS', 7.55), ('CD', 'LYS', 'CG', 'LYS', 6.46), ('CD', 'LYS', 'CD', 'LYS', 6.63), ('CD', 'LYS', 'CE', 'LYS', 7.27), ('CD', 'LYS', 'NZ', 'LYS', 7.04)], [('CE', 'LYS', 'CB', 'LYS', 8.26), ('CE', 'LYS', 'CG', 'LYS', 6.94), ('CE', 'LYS', 'CD', 'LYS', 6.9), ('CE', 'LYS', 'CE', 'LYS', 7.08), ('CE', 'LYS', 'NZ', 'LYS', 6.53)], [('NZ', 'LYS', 'CB', 'LYS', 8.32), ('NZ', 'LYS', 'CG', 'LYS', 6.97), ('NZ', 'LYS', 'CD', 'LYS', 6.47), ('NZ', 'LYS', 'CE', 'LYS', 6.52), ('NZ', 'LYS', 'NZ', 'LYS', 5.66)]]}
ASP_SER = { 
	'distances':
		[[7.66, 6.77], [6.4, 5.38], [5.46, 4.73], [6.64, 5.38]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 7.66), ('CB', 'ASP', 'OG', 'SER', 6.77)], [('CG', 'ASP', 'CB', 'SER', 6.4), ('CG', 'ASP', 'OG', 'SER', 5.38)], [('OD1', 'ASP', 'CB', 'SER', 5.46), ('OD1', 'ASP', 'OG', 'SER', 4.73)], [('OD2', 'ASP', 'CB', 'SER', 6.64), ('OD2', 'ASP', 'OG', 'SER', 5.38)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'P_1aw5_4_2_1_24')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_LYS, d, 'P_1aw5_4_2_1_24')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(LYS_LYS, d, 'P_1aw5_4_2_1_24')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_SER, d, 'P_1aw5_4_2_1_24')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1,
		'SER_LYS' :  match2,
		'LYS_LYS' :  match3,
		'ASP_SER' :  match4}