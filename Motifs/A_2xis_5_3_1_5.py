'''
FUNC:A_2xis_5_3_1_5
PDB:2xis
EC:5.3.1.5
RESI:his,asp,glu,lys
LOCI:a-54,57,181,183;
'''
import motifFunctions as cmd
ASP_HIS = { 
	'distances':
		[[6.61, 7.3, 6.99, 8.66, 8.22, 9.11], [5.87, 6.2, 5.68, 7.51, 6.84, 7.79], [6.16, 6.35, 5.85, 7.53, 6.87, 7.77], [5.47, 5.57, 4.88, 6.86, 6.03, 7.04]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 6.61), ('CB', 'ASP', 'CG', 'HIS', 7.3), ('CB', 'ASP', 'ND1', 'HIS', 6.99), ('CB', 'ASP', 'CD2', 'HIS', 8.66), ('CB', 'ASP', 'CE1', 'HIS', 8.22), ('CB', 'ASP', 'NE2', 'HIS', 9.11)], [('CG', 'ASP', 'CB', 'HIS', 5.87), ('CG', 'ASP', 'CG', 'HIS', 6.2), ('CG', 'ASP', 'ND1', 'HIS', 5.68), ('CG', 'ASP', 'CD2', 'HIS', 7.51), ('CG', 'ASP', 'CE1', 'HIS', 6.84), ('CG', 'ASP', 'NE2', 'HIS', 7.79)], [('OD1', 'ASP', 'CB', 'HIS', 6.16), ('OD1', 'ASP', 'CG', 'HIS', 6.35), ('OD1', 'ASP', 'ND1', 'HIS', 5.85), ('OD1', 'ASP', 'CD2', 'HIS', 7.53), ('OD1', 'ASP', 'CE1', 'HIS', 6.87), ('OD1', 'ASP', 'NE2', 'HIS', 7.77)], [('OD2', 'ASP', 'CB', 'HIS', 5.47), ('OD2', 'ASP', 'CG', 'HIS', 5.57), ('OD2', 'ASP', 'ND1', 'HIS', 4.88), ('OD2', 'ASP', 'CD2', 'HIS', 6.86), ('OD2', 'ASP', 'CE1', 'HIS', 6.03), ('OD2', 'ASP', 'NE2', 'HIS', 7.04)]]}
ASP_GLU = { 
	'distances':
		[[18.02, 17.93, 16.64, 15.68, 16.51], [16.8, 16.64, 15.34, 14.43, 15.17], [16.96, 16.74, 15.47, 14.63, 15.25], [15.78, 15.63, 14.32, 13.38, 14.18]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 18.02), ('CB', 'ASP', 'CG', 'GLU', 17.93), ('CB', 'ASP', 'CD', 'GLU', 16.64), ('CB', 'ASP', 'OE1', 'GLU', 15.68), ('CB', 'ASP', 'OE2', 'GLU', 16.51)], [('CG', 'ASP', 'CB', 'GLU', 16.8), ('CG', 'ASP', 'CG', 'GLU', 16.64), ('CG', 'ASP', 'CD', 'GLU', 15.34), ('CG', 'ASP', 'OE1', 'GLU', 14.43), ('CG', 'ASP', 'OE2', 'GLU', 15.17)], [('OD1', 'ASP', 'CB', 'GLU', 16.96), ('OD1', 'ASP', 'CG', 'GLU', 16.74), ('OD1', 'ASP', 'CD', 'GLU', 15.47), ('OD1', 'ASP', 'OE1', 'GLU', 14.63), ('OD1', 'ASP', 'OE2', 'GLU', 15.25)], [('OD2', 'ASP', 'CB', 'GLU', 15.78), ('OD2', 'ASP', 'CG', 'GLU', 15.63), ('OD2', 'ASP', 'CD', 'GLU', 14.32), ('OD2', 'ASP', 'OE1', 'GLU', 13.38), ('OD2', 'ASP', 'OE2', 'GLU', 14.18)]]}
HIS_LYS = { 
	'distances':
		[[17.5, 17.88, 16.76, 17.15, 16.13], [16.1, 16.44, 15.33, 15.71, 14.7], [15.91, 16.14, 15.0, 15.26, 14.24], [14.91, 15.33, 14.24, 14.72, 13.77], [14.61, 14.82, 13.7, 13.96, 12.98], [13.93, 14.26, 13.17, 13.58, 12.65]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 17.5), ('CB', 'HIS', 'CG', 'LYS', 17.88), ('CB', 'HIS', 'CD', 'LYS', 16.76), ('CB', 'HIS', 'CE', 'LYS', 17.15), ('CB', 'HIS', 'NZ', 'LYS', 16.13)], [('CG', 'HIS', 'CB', 'LYS', 16.1), ('CG', 'HIS', 'CG', 'LYS', 16.44), ('CG', 'HIS', 'CD', 'LYS', 15.33), ('CG', 'HIS', 'CE', 'LYS', 15.71), ('CG', 'HIS', 'NZ', 'LYS', 14.7)], [('ND1', 'HIS', 'CB', 'LYS', 15.91), ('ND1', 'HIS', 'CG', 'LYS', 16.14), ('ND1', 'HIS', 'CD', 'LYS', 15.0), ('ND1', 'HIS', 'CE', 'LYS', 15.26), ('ND1', 'HIS', 'NZ', 'LYS', 14.24)], [('CD2', 'HIS', 'CB', 'LYS', 14.91), ('CD2', 'HIS', 'CG', 'LYS', 15.33), ('CD2', 'HIS', 'CD', 'LYS', 14.24), ('CD2', 'HIS', 'CE', 'LYS', 14.72), ('CD2', 'HIS', 'NZ', 'LYS', 13.77)], [('CE1', 'HIS', 'CB', 'LYS', 14.61), ('CE1', 'HIS', 'CG', 'LYS', 14.82), ('CE1', 'HIS', 'CD', 'LYS', 13.7), ('CE1', 'HIS', 'CE', 'LYS', 13.96), ('CE1', 'HIS', 'NZ', 'LYS', 12.98)], [('NE2', 'HIS', 'CB', 'LYS', 13.93), ('NE2', 'HIS', 'CG', 'LYS', 14.26), ('NE2', 'HIS', 'CD', 'LYS', 13.17), ('NE2', 'HIS', 'CE', 'LYS', 13.58), ('NE2', 'HIS', 'NZ', 'LYS', 12.65)]]}
HIS_GLU = { 
	'distances':
		[[14.41, 14.59, 13.52, 12.49, 13.68], [13.2, 13.28, 12.17, 11.19, 12.26], [13.19, 13.09, 11.86, 10.94, 11.81], [12.09, 12.22, 11.19, 10.25, 11.35], [12.09, 11.91, 10.67, 9.82, 10.57], [11.34, 11.29, 10.17, 9.3, 10.21]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLU', 14.41), ('CB', 'HIS', 'CG', 'GLU', 14.59), ('CB', 'HIS', 'CD', 'GLU', 13.52), ('CB', 'HIS', 'OE1', 'GLU', 12.49), ('CB', 'HIS', 'OE2', 'GLU', 13.68)], [('CG', 'HIS', 'CB', 'GLU', 13.2), ('CG', 'HIS', 'CG', 'GLU', 13.28), ('CG', 'HIS', 'CD', 'GLU', 12.17), ('CG', 'HIS', 'OE1', 'GLU', 11.19), ('CG', 'HIS', 'OE2', 'GLU', 12.26)], [('ND1', 'HIS', 'CB', 'GLU', 13.19), ('ND1', 'HIS', 'CG', 'GLU', 13.09), ('ND1', 'HIS', 'CD', 'GLU', 11.86), ('ND1', 'HIS', 'OE1', 'GLU', 10.94), ('ND1', 'HIS', 'OE2', 'GLU', 11.81)], [('CD2', 'HIS', 'CB', 'GLU', 12.09), ('CD2', 'HIS', 'CG', 'GLU', 12.22), ('CD2', 'HIS', 'CD', 'GLU', 11.19), ('CD2', 'HIS', 'OE1', 'GLU', 10.25), ('CD2', 'HIS', 'OE2', 'GLU', 11.35)], [('CE1', 'HIS', 'CB', 'GLU', 12.09), ('CE1', 'HIS', 'CG', 'GLU', 11.91), ('CE1', 'HIS', 'CD', 'GLU', 10.67), ('CE1', 'HIS', 'OE1', 'GLU', 9.82), ('CE1', 'HIS', 'OE2', 'GLU', 10.57)], [('NE2', 'HIS', 'CB', 'GLU', 11.34), ('NE2', 'HIS', 'CG', 'GLU', 11.29), ('NE2', 'HIS', 'CD', 'GLU', 10.17), ('NE2', 'HIS', 'OE1', 'GLU', 9.3), ('NE2', 'HIS', 'OE2', 'GLU', 10.21)]]}
ASP_LYS = { 
	'distances':
		[[20.76, 20.86, 19.64, 19.69, 18.53], [19.29, 19.36, 18.13, 18.17, 17.01], [18.98, 18.98, 17.69, 17.68, 16.45], [18.57, 18.69, 17.53, 17.62, 16.53]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 20.76), ('CB', 'ASP', 'CG', 'LYS', 20.86), ('CB', 'ASP', 'CD', 'LYS', 19.64), ('CB', 'ASP', 'CE', 'LYS', 19.69), ('CB', 'ASP', 'NZ', 'LYS', 18.53)], [('CG', 'ASP', 'CB', 'LYS', 19.29), ('CG', 'ASP', 'CG', 'LYS', 19.36), ('CG', 'ASP', 'CD', 'LYS', 18.13), ('CG', 'ASP', 'CE', 'LYS', 18.17), ('CG', 'ASP', 'NZ', 'LYS', 17.01)], [('OD1', 'ASP', 'CB', 'LYS', 18.98), ('OD1', 'ASP', 'CG', 'LYS', 18.98), ('OD1', 'ASP', 'CD', 'LYS', 17.69), ('OD1', 'ASP', 'CE', 'LYS', 17.68), ('OD1', 'ASP', 'NZ', 'LYS', 16.45)], [('OD2', 'ASP', 'CB', 'LYS', 18.57), ('OD2', 'ASP', 'CG', 'LYS', 18.69), ('OD2', 'ASP', 'CD', 'LYS', 17.53), ('OD2', 'ASP', 'CE', 'LYS', 17.62), ('OD2', 'ASP', 'NZ', 'LYS', 16.53)]]}
LYS_GLU = { 
	'distances':
		[[8.82, 7.97, 8.58, 9.64, 8.39], [10.01, 8.97, 9.34, 10.42, 8.89], [10.21, 9.17, 9.29, 10.22, 8.75], [11.37, 10.19, 10.12, 11.04, 9.39], [11.78, 10.65, 10.37, 11.13, 9.61]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 8.82), ('CB', 'LYS', 'CG', 'GLU', 7.97), ('CB', 'LYS', 'CD', 'GLU', 8.58), ('CB', 'LYS', 'OE1', 'GLU', 9.64), ('CB', 'LYS', 'OE2', 'GLU', 8.39)], [('CG', 'LYS', 'CB', 'GLU', 10.01), ('CG', 'LYS', 'CG', 'GLU', 8.97), ('CG', 'LYS', 'CD', 'GLU', 9.34), ('CG', 'LYS', 'OE1', 'GLU', 10.42), ('CG', 'LYS', 'OE2', 'GLU', 8.89)], [('CD', 'LYS', 'CB', 'GLU', 10.21), ('CD', 'LYS', 'CG', 'GLU', 9.17), ('CD', 'LYS', 'CD', 'GLU', 9.29), ('CD', 'LYS', 'OE1', 'GLU', 10.22), ('CD', 'LYS', 'OE2', 'GLU', 8.75)], [('CE', 'LYS', 'CB', 'GLU', 11.37), ('CE', 'LYS', 'CG', 'GLU', 10.19), ('CE', 'LYS', 'CD', 'GLU', 10.12), ('CE', 'LYS', 'OE1', 'GLU', 11.04), ('CE', 'LYS', 'OE2', 'GLU', 9.39)], [('NZ', 'LYS', 'CB', 'GLU', 11.78), ('NZ', 'LYS', 'CG', 'GLU', 10.65), ('NZ', 'LYS', 'CD', 'GLU', 10.37), ('NZ', 'LYS', 'OE1', 'GLU', 11.13), ('NZ', 'LYS', 'OE2', 'GLU', 9.61)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_HIS, d, 'A_2xis_5_3_1_5')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLU, d, 'A_2xis_5_3_1_5')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(HIS_LYS, d, 'A_2xis_5_3_1_5')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(HIS_GLU, d, 'A_2xis_5_3_1_5')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_LYS, d, 'A_2xis_5_3_1_5')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(LYS_GLU, d, 'A_2xis_5_3_1_5')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_HIS' :  match1,
		'ASP_GLU' :  match2,
		'HIS_LYS' :  match3,
		'HIS_GLU' :  match4,
		'ASP_LYS' :  match5,
		'LYS_GLU' :  match6}