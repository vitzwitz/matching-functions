'''
FUNC:P_1i2r_2_2_1_2
PDB:1i2r
EC:2.2.1.2
RESI:asp,glu,lys
LOCI:a-17,96,132;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[12.25, 11.3, 9.9, 9.06, 7.68], [11.15, 10.14, 8.73, 7.81, 6.4], [10.05, 9.12, 7.67, 6.88, 5.43], [11.5, 10.4, 9.04, 7.96, 6.59]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 12.25), ('CB', 'ASP', 'CG', 'LYS', 11.3), ('CB', 'ASP', 'CD', 'LYS', 9.9), ('CB', 'ASP', 'CE', 'LYS', 9.06), ('CB', 'ASP', 'NZ', 'LYS', 7.68)], [('CG', 'ASP', 'CB', 'LYS', 11.15), ('CG', 'ASP', 'CG', 'LYS', 10.14), ('CG', 'ASP', 'CD', 'LYS', 8.73), ('CG', 'ASP', 'CE', 'LYS', 7.81), ('CG', 'ASP', 'NZ', 'LYS', 6.4)], [('OD1', 'ASP', 'CB', 'LYS', 10.05), ('OD1', 'ASP', 'CG', 'LYS', 9.12), ('OD1', 'ASP', 'CD', 'LYS', 7.67), ('OD1', 'ASP', 'CE', 'LYS', 6.88), ('OD1', 'ASP', 'NZ', 'LYS', 5.43)], [('OD2', 'ASP', 'CB', 'LYS', 11.5), ('OD2', 'ASP', 'CG', 'LYS', 10.4), ('OD2', 'ASP', 'CD', 'LYS', 9.04), ('OD2', 'ASP', 'CE', 'LYS', 7.96), ('OD2', 'ASP', 'NZ', 'LYS', 6.59)]]}
GLU_LYS = { 
	'distances':
		[[4.17, 4.75, 4.71, 5.7, 6.27], [4.43, 4.81, 5.11, 5.87, 6.66], [4.91, 4.75, 4.86, 5.19, 5.91], [4.86, 4.45, 4.14, 4.29, 4.79], [5.79, 5.51, 5.78, 5.9, 6.68]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 4.17), ('CB', 'GLU', 'CG', 'LYS', 4.75), ('CB', 'GLU', 'CD', 'LYS', 4.71), ('CB', 'GLU', 'CE', 'LYS', 5.7), ('CB', 'GLU', 'NZ', 'LYS', 6.27)], [('CG', 'GLU', 'CB', 'LYS', 4.43), ('CG', 'GLU', 'CG', 'LYS', 4.81), ('CG', 'GLU', 'CD', 'LYS', 5.11), ('CG', 'GLU', 'CE', 'LYS', 5.87), ('CG', 'GLU', 'NZ', 'LYS', 6.66)], [('CD', 'GLU', 'CB', 'LYS', 4.91), ('CD', 'GLU', 'CG', 'LYS', 4.75), ('CD', 'GLU', 'CD', 'LYS', 4.86), ('CD', 'GLU', 'CE', 'LYS', 5.19), ('CD', 'GLU', 'NZ', 'LYS', 5.91)], [('OE1', 'GLU', 'CB', 'LYS', 4.86), ('OE1', 'GLU', 'CG', 'LYS', 4.45), ('OE1', 'GLU', 'CD', 'LYS', 4.14), ('OE1', 'GLU', 'CE', 'LYS', 4.29), ('OE1', 'GLU', 'NZ', 'LYS', 4.79)], [('OE2', 'GLU', 'CB', 'LYS', 5.79), ('OE2', 'GLU', 'CG', 'LYS', 5.51), ('OE2', 'GLU', 'CD', 'LYS', 5.78), ('OE2', 'GLU', 'CE', 'LYS', 5.9), ('OE2', 'GLU', 'NZ', 'LYS', 6.68)]]}
ASP_GLU = { 
	'distances':
		[[12.68, 13.39, 12.61, 11.37, 13.34], [11.43, 12.06, 11.21, 9.96, 11.89], [10.3, 11.0, 10.24, 8.99, 11.0], [11.7, 12.19, 11.2, 9.97, 11.76]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 12.68), ('CB', 'ASP', 'CG', 'GLU', 13.39), ('CB', 'ASP', 'CD', 'GLU', 12.61), ('CB', 'ASP', 'OE1', 'GLU', 11.37), ('CB', 'ASP', 'OE2', 'GLU', 13.34)], [('CG', 'ASP', 'CB', 'GLU', 11.43), ('CG', 'ASP', 'CG', 'GLU', 12.06), ('CG', 'ASP', 'CD', 'GLU', 11.21), ('CG', 'ASP', 'OE1', 'GLU', 9.96), ('CG', 'ASP', 'OE2', 'GLU', 11.89)], [('OD1', 'ASP', 'CB', 'GLU', 10.3), ('OD1', 'ASP', 'CG', 'GLU', 11.0), ('OD1', 'ASP', 'CD', 'GLU', 10.24), ('OD1', 'ASP', 'OE1', 'GLU', 8.99), ('OD1', 'ASP', 'OE2', 'GLU', 11.0)], [('OD2', 'ASP', 'CB', 'GLU', 11.7), ('OD2', 'ASP', 'CG', 'GLU', 12.19), ('OD2', 'ASP', 'CD', 'GLU', 11.2), ('OD2', 'ASP', 'OE1', 'GLU', 9.97), ('OD2', 'ASP', 'OE2', 'GLU', 11.76)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'P_1i2r_2_2_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LYS, d, 'P_1i2r_2_2_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'P_1i2r_2_2_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1,
		'GLU_LYS' :  match2,
		'ASP_GLU' :  match3}