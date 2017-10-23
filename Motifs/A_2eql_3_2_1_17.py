'''
FUNC:A_2eql_3_2_1_17
PDB:2eql
EC:3.2.1.17
RESI:glu,asp
LOCI:a-35,53;
'''
import motifFunctions as cmd
GLU_ASP = { 
	'distances':
		[[9.51, 9.75, 10.63, 9.26, 10.72, 10.57, 10.67, 11.91], [9.4, 9.42, 10.14, 8.94, 10.98, 10.65, 10.56, 11.8], [9.11, 8.86, 9.56, 8.21, 11.05, 10.71, 10.39, 11.5], [8.29, 8.0, 8.78, 7.23, 10.3, 10.04, 9.66, 10.67], [9.97, 9.55, 10.13, 8.88, 12.07, 11.65, 11.23, 12.3], [8.82, 9.26, 10.39, 8.63, 9.59, 9.84, 10.07, 11.08], [9.71, 10.14, 11.21, 9.54, 10.48, 10.65, 10.92, 12.01], [10.08, 10.29, 11.27, 9.63, 11.24, 11.25, 11.35, 12.47], [11.54, 11.73, 12.7, 11.05, 12.65, 12.68, 12.8, 13.93]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 9.51), ('CB', 'GLU', 'CG', 'ASP', 9.75), ('CB', 'GLU', 'OD1', 'ASP', 10.63), ('CB', 'GLU', 'OD2', 'ASP', 9.26), ('CB', 'GLU', 'O', 'ASP', 10.72), ('CB', 'GLU', 'C', 'ASP', 10.57), ('CB', 'GLU', 'CA', 'ASP', 10.67), ('CB', 'GLU', 'N', 'ASP', 11.91)], [('CG', 'GLU', 'CB', 'ASP', 9.4), ('CG', 'GLU', 'CG', 'ASP', 9.42), ('CG', 'GLU', 'OD1', 'ASP', 10.14), ('CG', 'GLU', 'OD2', 'ASP', 8.94), ('CG', 'GLU', 'O', 'ASP', 10.98), ('CG', 'GLU', 'C', 'ASP', 10.65), ('CG', 'GLU', 'CA', 'ASP', 10.56), ('CG', 'GLU', 'N', 'ASP', 11.8)], [('CD', 'GLU', 'CB', 'ASP', 9.11), ('CD', 'GLU', 'CG', 'ASP', 8.86), ('CD', 'GLU', 'OD1', 'ASP', 9.56), ('CD', 'GLU', 'OD2', 'ASP', 8.21), ('CD', 'GLU', 'O', 'ASP', 11.05), ('CD', 'GLU', 'C', 'ASP', 10.71), ('CD', 'GLU', 'CA', 'ASP', 10.39), ('CD', 'GLU', 'N', 'ASP', 11.5)], [('OE1', 'GLU', 'CB', 'ASP', 8.29), ('OE1', 'GLU', 'CG', 'ASP', 8.0), ('OE1', 'GLU', 'OD1', 'ASP', 8.78), ('OE1', 'GLU', 'OD2', 'ASP', 7.23), ('OE1', 'GLU', 'O', 'ASP', 10.3), ('OE1', 'GLU', 'C', 'ASP', 10.04), ('OE1', 'GLU', 'CA', 'ASP', 9.66), ('OE1', 'GLU', 'N', 'ASP', 10.67)], [('OE2', 'GLU', 'CB', 'ASP', 9.97), ('OE2', 'GLU', 'CG', 'ASP', 9.55), ('OE2', 'GLU', 'OD1', 'ASP', 10.13), ('OE2', 'GLU', 'OD2', 'ASP', 8.88), ('OE2', 'GLU', 'O', 'ASP', 12.07), ('OE2', 'GLU', 'C', 'ASP', 11.65), ('OE2', 'GLU', 'CA', 'ASP', 11.23), ('OE2', 'GLU', 'N', 'ASP', 12.3)], [('O', 'GLU', 'CB', 'ASP', 8.82), ('O', 'GLU', 'CG', 'ASP', 9.26), ('O', 'GLU', 'OD1', 'ASP', 10.39), ('O', 'GLU', 'OD2', 'ASP', 8.63), ('O', 'GLU', 'O', 'ASP', 9.59), ('O', 'GLU', 'C', 'ASP', 9.84), ('O', 'GLU', 'CA', 'ASP', 10.07), ('O', 'GLU', 'N', 'ASP', 11.08)], [('C', 'GLU', 'CB', 'ASP', 9.71), ('C', 'GLU', 'CG', 'ASP', 10.14), ('C', 'GLU', 'OD1', 'ASP', 11.21), ('C', 'GLU', 'OD2', 'ASP', 9.54), ('C', 'GLU', 'O', 'ASP', 10.48), ('C', 'GLU', 'C', 'ASP', 10.65), ('C', 'GLU', 'CA', 'ASP', 10.92), ('C', 'GLU', 'N', 'ASP', 12.01)], [('CA', 'GLU', 'CB', 'ASP', 10.08), ('CA', 'GLU', 'CG', 'ASP', 10.29), ('CA', 'GLU', 'OD1', 'ASP', 11.27), ('CA', 'GLU', 'OD2', 'ASP', 9.63), ('CA', 'GLU', 'O', 'ASP', 11.24), ('CA', 'GLU', 'C', 'ASP', 11.25), ('CA', 'GLU', 'CA', 'ASP', 11.35), ('CA', 'GLU', 'N', 'ASP', 12.47)], [('N', 'GLU', 'CB', 'ASP', 11.54), ('N', 'GLU', 'CG', 'ASP', 11.73), ('N', 'GLU', 'OD1', 'ASP', 12.7), ('N', 'GLU', 'OD2', 'ASP', 11.05), ('N', 'GLU', 'O', 'ASP', 12.65), ('N', 'GLU', 'C', 'ASP', 12.68), ('N', 'GLU', 'CA', 'ASP', 12.8), ('N', 'GLU', 'N', 'ASP', 13.93)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ASP, d, 'A_2eql_3_2_1_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ASP' :  match1}