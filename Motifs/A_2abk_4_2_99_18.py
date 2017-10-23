'''
FUNC:A_2abk_4_2_99_18
PDB:2abk
EC:4.2.99.18
RESI:lys,asp
LOCI:a-120,138;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[9.25, 7.91, 7.01, 6.27, 6.0], [10.6, 9.19, 8.41, 7.52, 7.26], [11.16, 9.75, 9.13, 8.37, 8.3], [11.26, 9.83, 8.97, 7.89, 7.46]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 9.25), ('CB', 'ASP', 'CG', 'LYS', 7.91), ('CB', 'ASP', 'CD', 'LYS', 7.01), ('CB', 'ASP', 'CE', 'LYS', 6.27), ('CB', 'ASP', 'NZ', 'LYS', 6.0)], [('CG', 'ASP', 'CB', 'LYS', 10.6), ('CG', 'ASP', 'CG', 'LYS', 9.19), ('CG', 'ASP', 'CD', 'LYS', 8.41), ('CG', 'ASP', 'CE', 'LYS', 7.52), ('CG', 'ASP', 'NZ', 'LYS', 7.26)], [('OD1', 'ASP', 'CB', 'LYS', 11.16), ('OD1', 'ASP', 'CG', 'LYS', 9.75), ('OD1', 'ASP', 'CD', 'LYS', 9.13), ('OD1', 'ASP', 'CE', 'LYS', 8.37), ('OD1', 'ASP', 'NZ', 'LYS', 8.3)], [('OD2', 'ASP', 'CB', 'LYS', 11.26), ('OD2', 'ASP', 'CG', 'LYS', 9.83), ('OD2', 'ASP', 'CD', 'LYS', 8.97), ('OD2', 'ASP', 'CE', 'LYS', 7.89), ('OD2', 'ASP', 'NZ', 'LYS', 7.46)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'A_2abk_4_2_99_18')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1}