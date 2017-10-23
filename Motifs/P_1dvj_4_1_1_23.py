'''
FUNC:P_1dvj_4_1_1_23
PDB:1dvj
EC:4.1.1.23
RESI:asp,lys
LOCI:a-70,72;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[7.6, 6.66, 6.91, 6.84, 5.58], [6.73, 5.6, 5.63, 5.41, 4.15], [5.66, 4.66, 4.64, 4.75, 3.83], [7.35, 6.03, 5.87, 5.24, 3.81]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 7.6), ('CB', 'ASP', 'CG', 'LYS', 6.66), ('CB', 'ASP', 'CD', 'LYS', 6.91), ('CB', 'ASP', 'CE', 'LYS', 6.84), ('CB', 'ASP', 'NZ', 'LYS', 5.58)], [('CG', 'ASP', 'CB', 'LYS', 6.73), ('CG', 'ASP', 'CG', 'LYS', 5.6), ('CG', 'ASP', 'CD', 'LYS', 5.63), ('CG', 'ASP', 'CE', 'LYS', 5.41), ('CG', 'ASP', 'NZ', 'LYS', 4.15)], [('OD1', 'ASP', 'CB', 'LYS', 5.66), ('OD1', 'ASP', 'CG', 'LYS', 4.66), ('OD1', 'ASP', 'CD', 'LYS', 4.64), ('OD1', 'ASP', 'CE', 'LYS', 4.75), ('OD1', 'ASP', 'NZ', 'LYS', 3.83)], [('OD2', 'ASP', 'CB', 'LYS', 7.35), ('OD2', 'ASP', 'CG', 'LYS', 6.03), ('OD2', 'ASP', 'CD', 'LYS', 5.87), ('OD2', 'ASP', 'CE', 'LYS', 5.24), ('OD2', 'ASP', 'NZ', 'LYS', 3.81)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'P_1dvj_4_1_1_23')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1}