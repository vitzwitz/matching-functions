'''
FUNC:A_1dbt_4_1_1_23
PDB:1dbt
EC:4.1.1.23
RESI:asp,lys
LOCI:a-60,62;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[8.5, 7.45, 8.14, 7.61, 6.53, 10.74, 9.94, 8.52, 7.49], [7.66, 6.4, 6.89, 6.18, 5.14, 10.13, 9.46, 7.96, 7.22], [6.6, 5.33, 5.99, 5.46, 4.79, 9.1, 8.41, 6.89, 6.31], [8.32, 6.97, 7.09, 6.11, 4.89, 10.9, 10.34, 8.86, 8.23], [7.13, 6.53, 7.32, 7.38, 6.37, 8.95, 8.32, 7.14, 5.93], [7.15, 6.61, 7.66, 7.76, 6.92, 8.87, 8.05, 6.85, 5.53], [8.05, 7.27, 8.28, 8.08, 7.21, 9.96, 9.05, 7.73, 6.53], [9.37, 8.69, 9.73, 9.53, 8.61, 11.07, 10.1, 8.88, 7.59]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 8.5), ('CB', 'ASP', 'CG', 'LYS', 7.45), ('CB', 'ASP', 'CD', 'LYS', 8.14), ('CB', 'ASP', 'CE', 'LYS', 7.61), ('CB', 'ASP', 'NZ', 'LYS', 6.53), ('CB', 'ASP', 'O', 'LYS', 10.74), ('CB', 'ASP', 'C', 'LYS', 9.94), ('CB', 'ASP', 'CA', 'LYS', 8.52), ('CB', 'ASP', 'N', 'LYS', 7.49)], [('CG', 'ASP', 'CB', 'LYS', 7.66), ('CG', 'ASP', 'CG', 'LYS', 6.4), ('CG', 'ASP', 'CD', 'LYS', 6.89), ('CG', 'ASP', 'CE', 'LYS', 6.18), ('CG', 'ASP', 'NZ', 'LYS', 5.14), ('CG', 'ASP', 'O', 'LYS', 10.13), ('CG', 'ASP', 'C', 'LYS', 9.46), ('CG', 'ASP', 'CA', 'LYS', 7.96), ('CG', 'ASP', 'N', 'LYS', 7.22)], [('OD1', 'ASP', 'CB', 'LYS', 6.6), ('OD1', 'ASP', 'CG', 'LYS', 5.33), ('OD1', 'ASP', 'CD', 'LYS', 5.99), ('OD1', 'ASP', 'CE', 'LYS', 5.46), ('OD1', 'ASP', 'NZ', 'LYS', 4.79), ('OD1', 'ASP', 'O', 'LYS', 9.1), ('OD1', 'ASP', 'C', 'LYS', 8.41), ('OD1', 'ASP', 'CA', 'LYS', 6.89), ('OD1', 'ASP', 'N', 'LYS', 6.31)], [('OD2', 'ASP', 'CB', 'LYS', 8.32), ('OD2', 'ASP', 'CG', 'LYS', 6.97), ('OD2', 'ASP', 'CD', 'LYS', 7.09), ('OD2', 'ASP', 'CE', 'LYS', 6.11), ('OD2', 'ASP', 'NZ', 'LYS', 4.89), ('OD2', 'ASP', 'O', 'LYS', 10.9), ('OD2', 'ASP', 'C', 'LYS', 10.34), ('OD2', 'ASP', 'CA', 'LYS', 8.86), ('OD2', 'ASP', 'N', 'LYS', 8.23)], [('O', 'ASP', 'CB', 'LYS', 7.13), ('O', 'ASP', 'CG', 'LYS', 6.53), ('O', 'ASP', 'CD', 'LYS', 7.32), ('O', 'ASP', 'CE', 'LYS', 7.38), ('O', 'ASP', 'NZ', 'LYS', 6.37), ('O', 'ASP', 'O', 'LYS', 8.95), ('O', 'ASP', 'C', 'LYS', 8.32), ('O', 'ASP', 'CA', 'LYS', 7.14), ('O', 'ASP', 'N', 'LYS', 5.93)], [('C', 'ASP', 'CB', 'LYS', 7.15), ('C', 'ASP', 'CG', 'LYS', 6.61), ('C', 'ASP', 'CD', 'LYS', 7.66), ('C', 'ASP', 'CE', 'LYS', 7.76), ('C', 'ASP', 'NZ', 'LYS', 6.92), ('C', 'ASP', 'O', 'LYS', 8.87), ('C', 'ASP', 'C', 'LYS', 8.05), ('C', 'ASP', 'CA', 'LYS', 6.85), ('C', 'ASP', 'N', 'LYS', 5.53)], [('CA', 'ASP', 'CB', 'LYS', 8.05), ('CA', 'ASP', 'CG', 'LYS', 7.27), ('CA', 'ASP', 'CD', 'LYS', 8.28), ('CA', 'ASP', 'CE', 'LYS', 8.08), ('CA', 'ASP', 'NZ', 'LYS', 7.21), ('CA', 'ASP', 'O', 'LYS', 9.96), ('CA', 'ASP', 'C', 'LYS', 9.05), ('CA', 'ASP', 'CA', 'LYS', 7.73), ('CA', 'ASP', 'N', 'LYS', 6.53)], [('N', 'ASP', 'CB', 'LYS', 9.37), ('N', 'ASP', 'CG', 'LYS', 8.69), ('N', 'ASP', 'CD', 'LYS', 9.73), ('N', 'ASP', 'CE', 'LYS', 9.53), ('N', 'ASP', 'NZ', 'LYS', 8.61), ('N', 'ASP', 'O', 'LYS', 11.07), ('N', 'ASP', 'C', 'LYS', 10.1), ('N', 'ASP', 'CA', 'LYS', 8.88), ('N', 'ASP', 'N', 'LYS', 7.59)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'A_1dbt_4_1_1_23')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1}