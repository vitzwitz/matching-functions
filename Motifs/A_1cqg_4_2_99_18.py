'''
FUNC:A_1cqg_4_2_99_18
PDB:1cqg
EC:4.2.99.18
RESI:cys,ala
LOCI:a-32,35;
'''
import motifFunctions as cmd
ALA_CYS = { 
	'distances':
		[[5.86, 6.48, 5.7, 6.42, 6.72, 7.25], [8.73, 9.36, 6.96, 8.07, 9.02, 9.39], [7.55, 8.2, 5.8, 6.89, 7.82, 8.25], [6.76, 7.11, 5.79, 6.63, 7.36, 8.04], [6.34, 6.32, 5.3, 5.88, 6.77, 7.74]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'CYS', 5.86), ('CB', 'ALA', 'SG', 'CYS', 6.48), ('CB', 'ALA', 'O', 'CYS', 5.7), ('CB', 'ALA', 'C', 'CYS', 6.42), ('CB', 'ALA', 'CA', 'CYS', 6.72), ('CB', 'ALA', 'N', 'CYS', 7.25)], [('O', 'ALA', 'CB', 'CYS', 8.73), ('O', 'ALA', 'SG', 'CYS', 9.36), ('O', 'ALA', 'O', 'CYS', 6.96), ('O', 'ALA', 'C', 'CYS', 8.07), ('O', 'ALA', 'CA', 'CYS', 9.02), ('O', 'ALA', 'N', 'CYS', 9.39)], [('C', 'ALA', 'CB', 'CYS', 7.55), ('C', 'ALA', 'SG', 'CYS', 8.2), ('C', 'ALA', 'O', 'CYS', 5.8), ('C', 'ALA', 'C', 'CYS', 6.89), ('C', 'ALA', 'CA', 'CYS', 7.82), ('C', 'ALA', 'N', 'CYS', 8.25)], [('CA', 'ALA', 'CB', 'CYS', 6.76), ('CA', 'ALA', 'SG', 'CYS', 7.11), ('CA', 'ALA', 'O', 'CYS', 5.79), ('CA', 'ALA', 'C', 'CYS', 6.63), ('CA', 'ALA', 'CA', 'CYS', 7.36), ('CA', 'ALA', 'N', 'CYS', 8.04)], [('N', 'ALA', 'CB', 'CYS', 6.34), ('N', 'ALA', 'SG', 'CYS', 6.32), ('N', 'ALA', 'O', 'CYS', 5.3), ('N', 'ALA', 'C', 'CYS', 5.88), ('N', 'ALA', 'CA', 'CYS', 6.77), ('N', 'ALA', 'N', 'CYS', 7.74)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ALA_CYS, d, 'A_1cqg_4_2_99_18')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ALA_CYS' :  match1}