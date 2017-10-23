'''
FUNC:A_1ald_4_1_2_13
PDB:1ald
EC:4.1.2.13
RESI:asp,glu,lys
LOCI:a-33,187,229;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[13.8, 12.46, 12.27, 11.64], [13.13, 11.72, 11.38, 11.03], [11.63, 10.23, 9.9, 9.57], [11.15, 9.7, 9.16, 9.23], [9.78, 8.37, 7.78, 8.0]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 13.8), ('CB', 'LYS', 'CG', 'ASP', 12.46), ('CB', 'LYS', 'OD1', 'ASP', 12.27), ('CB', 'LYS', 'OD2', 'ASP', 11.64)], [('CG', 'LYS', 'CB', 'ASP', 13.13), ('CG', 'LYS', 'CG', 'ASP', 11.72), ('CG', 'LYS', 'OD1', 'ASP', 11.38), ('CG', 'LYS', 'OD2', 'ASP', 11.03)], [('CD', 'LYS', 'CB', 'ASP', 11.63), ('CD', 'LYS', 'CG', 'ASP', 10.23), ('CD', 'LYS', 'OD1', 'ASP', 9.9), ('CD', 'LYS', 'OD2', 'ASP', 9.57)], [('CE', 'LYS', 'CB', 'ASP', 11.15), ('CE', 'LYS', 'CG', 'ASP', 9.7), ('CE', 'LYS', 'OD1', 'ASP', 9.16), ('CE', 'LYS', 'OD2', 'ASP', 9.23)], [('NZ', 'LYS', 'CB', 'ASP', 9.78), ('NZ', 'LYS', 'CG', 'ASP', 8.37), ('NZ', 'LYS', 'OD1', 'ASP', 7.78), ('NZ', 'LYS', 'OD2', 'ASP', 8.0)]]}
GLU_LYS = { 
	'distances':
		[[6.07, 6.48, 6.65, 7.61, 8.35], [6.1, 6.04, 6.3, 6.93, 7.81], [6.53, 6.02, 5.8, 6.06, 6.7], [7.18, 6.35, 6.15, 5.95, 6.62], [6.75, 6.32, 5.68, 6.0, 6.29]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 6.07), ('CB', 'GLU', 'CG', 'LYS', 6.48), ('CB', 'GLU', 'CD', 'LYS', 6.65), ('CB', 'GLU', 'CE', 'LYS', 7.61), ('CB', 'GLU', 'NZ', 'LYS', 8.35)], [('CG', 'GLU', 'CB', 'LYS', 6.1), ('CG', 'GLU', 'CG', 'LYS', 6.04), ('CG', 'GLU', 'CD', 'LYS', 6.3), ('CG', 'GLU', 'CE', 'LYS', 6.93), ('CG', 'GLU', 'NZ', 'LYS', 7.81)], [('CD', 'GLU', 'CB', 'LYS', 6.53), ('CD', 'GLU', 'CG', 'LYS', 6.02), ('CD', 'GLU', 'CD', 'LYS', 5.8), ('CD', 'GLU', 'CE', 'LYS', 6.06), ('CD', 'GLU', 'NZ', 'LYS', 6.7)], [('OE1', 'GLU', 'CB', 'LYS', 7.18), ('OE1', 'GLU', 'CG', 'LYS', 6.35), ('OE1', 'GLU', 'CD', 'LYS', 6.15), ('OE1', 'GLU', 'CE', 'LYS', 5.95), ('OE1', 'GLU', 'NZ', 'LYS', 6.62)], [('OE2', 'GLU', 'CB', 'LYS', 6.75), ('OE2', 'GLU', 'CG', 'LYS', 6.32), ('OE2', 'GLU', 'CD', 'LYS', 5.68), ('OE2', 'GLU', 'CE', 'LYS', 6.0), ('OE2', 'GLU', 'NZ', 'LYS', 6.29)]]}
GLU_ASP = { 
	'distances':
		[[13.15, 11.82, 11.91, 10.72], [13.17, 11.75, 11.66, 10.76], [11.85, 10.4, 10.23, 9.48], [11.99, 10.49, 10.15, 9.71], [10.73, 9.31, 9.27, 8.33]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 13.15), ('CB', 'GLU', 'CG', 'ASP', 11.82), ('CB', 'GLU', 'OD1', 'ASP', 11.91), ('CB', 'GLU', 'OD2', 'ASP', 10.72)], [('CG', 'GLU', 'CB', 'ASP', 13.17), ('CG', 'GLU', 'CG', 'ASP', 11.75), ('CG', 'GLU', 'OD1', 'ASP', 11.66), ('CG', 'GLU', 'OD2', 'ASP', 10.76)], [('CD', 'GLU', 'CB', 'ASP', 11.85), ('CD', 'GLU', 'CG', 'ASP', 10.4), ('CD', 'GLU', 'OD1', 'ASP', 10.23), ('CD', 'GLU', 'OD2', 'ASP', 9.48)], [('OE1', 'GLU', 'CB', 'ASP', 11.99), ('OE1', 'GLU', 'CG', 'ASP', 10.49), ('OE1', 'GLU', 'OD1', 'ASP', 10.15), ('OE1', 'GLU', 'OD2', 'ASP', 9.71)], [('OE2', 'GLU', 'CB', 'ASP', 10.73), ('OE2', 'GLU', 'CG', 'ASP', 9.31), ('OE2', 'GLU', 'OD1', 'ASP', 9.27), ('OE2', 'GLU', 'OD2', 'ASP', 8.33)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'A_1ald_4_1_2_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LYS, d, 'A_1ald_4_1_2_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ASP, d, 'A_1ald_4_1_2_13')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'GLU_LYS' :  match2,
		'GLU_ASP' :  match3}