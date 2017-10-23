'''
FUNC:P_1lcp_3_4_11_1
PDB:1lcp
EC:3.4.11.1
RESI:asp,lys,arg
LOCI:a-255,262,336;
'''
import motifFunctions as cmd
ASP_LYS = { 
	'distances':
		[[8.08, 6.95, 5.96, 4.96, 5.94], [7.62, 6.33, 5.61, 4.43, 5.13], [7.45, 6.22, 5.82, 4.84, 5.56], [7.78, 6.36, 5.63, 4.21, 4.52]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 8.08), ('CB', 'ASP', 'CG', 'LYS', 6.95), ('CB', 'ASP', 'CD', 'LYS', 5.96), ('CB', 'ASP', 'CE', 'LYS', 4.96), ('CB', 'ASP', 'NZ', 'LYS', 5.94)], [('CG', 'ASP', 'CB', 'LYS', 7.62), ('CG', 'ASP', 'CG', 'LYS', 6.33), ('CG', 'ASP', 'CD', 'LYS', 5.61), ('CG', 'ASP', 'CE', 'LYS', 4.43), ('CG', 'ASP', 'NZ', 'LYS', 5.13)], [('OD1', 'ASP', 'CB', 'LYS', 7.45), ('OD1', 'ASP', 'CG', 'LYS', 6.22), ('OD1', 'ASP', 'CD', 'LYS', 5.82), ('OD1', 'ASP', 'CE', 'LYS', 4.84), ('OD1', 'ASP', 'NZ', 'LYS', 5.56)], [('OD2', 'ASP', 'CB', 'LYS', 7.78), ('OD2', 'ASP', 'CG', 'LYS', 6.36), ('OD2', 'ASP', 'CD', 'LYS', 5.63), ('OD2', 'ASP', 'CE', 'LYS', 4.21), ('OD2', 'ASP', 'NZ', 'LYS', 4.52)]]}
LYS_ARG = { 
	'distances':
		[[17.21, 16.61, 16.66, 15.61, 15.62, 16.64, 14.73], [15.72, 15.16, 15.24, 14.19, 14.23, 15.28, 13.35], [15.58, 15.16, 15.31, 14.23, 14.32, 15.44, 13.4], [14.15, 13.8, 13.99, 12.91, 13.05, 14.22, 12.15], [13.39, 13.0, 13.05, 11.9, 11.92, 13.05, 10.95]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 17.21), ('CB', 'LYS', 'CG', 'ARG', 16.61), ('CB', 'LYS', 'CD', 'ARG', 16.66), ('CB', 'LYS', 'NE', 'ARG', 15.61), ('CB', 'LYS', 'CZ', 'ARG', 15.62), ('CB', 'LYS', 'NH1', 'ARG', 16.64), ('CB', 'LYS', 'NH2', 'ARG', 14.73)], [('CG', 'LYS', 'CB', 'ARG', 15.72), ('CG', 'LYS', 'CG', 'ARG', 15.16), ('CG', 'LYS', 'CD', 'ARG', 15.24), ('CG', 'LYS', 'NE', 'ARG', 14.19), ('CG', 'LYS', 'CZ', 'ARG', 14.23), ('CG', 'LYS', 'NH1', 'ARG', 15.28), ('CG', 'LYS', 'NH2', 'ARG', 13.35)], [('CD', 'LYS', 'CB', 'ARG', 15.58), ('CD', 'LYS', 'CG', 'ARG', 15.16), ('CD', 'LYS', 'CD', 'ARG', 15.31), ('CD', 'LYS', 'NE', 'ARG', 14.23), ('CD', 'LYS', 'CZ', 'ARG', 14.32), ('CD', 'LYS', 'NH1', 'ARG', 15.44), ('CD', 'LYS', 'NH2', 'ARG', 13.4)], [('CE', 'LYS', 'CB', 'ARG', 14.15), ('CE', 'LYS', 'CG', 'ARG', 13.8), ('CE', 'LYS', 'CD', 'ARG', 13.99), ('CE', 'LYS', 'NE', 'ARG', 12.91), ('CE', 'LYS', 'CZ', 'ARG', 13.05), ('CE', 'LYS', 'NH1', 'ARG', 14.22), ('CE', 'LYS', 'NH2', 'ARG', 12.15)], [('NZ', 'LYS', 'CB', 'ARG', 13.39), ('NZ', 'LYS', 'CG', 'ARG', 13.0), ('NZ', 'LYS', 'CD', 'ARG', 13.05), ('NZ', 'LYS', 'NE', 'ARG', 11.9), ('NZ', 'LYS', 'CZ', 'ARG', 11.92), ('NZ', 'LYS', 'NH1', 'ARG', 13.05), ('NZ', 'LYS', 'NH2', 'ARG', 10.95)]]}
ASP_ARG = { 
	'distances':
		[[13.29, 13.2, 13.86, 13.04, 13.59, 14.89, 12.96], [12.28, 12.05, 12.64, 11.83, 12.35, 13.62, 11.74], [12.41, 12.05, 12.66, 11.93, 12.49, 13.73, 11.96], [11.5, 11.31, 11.8, 10.9, 11.35, 12.63, 10.67]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 13.29), ('CB', 'ASP', 'CG', 'ARG', 13.2), ('CB', 'ASP', 'CD', 'ARG', 13.86), ('CB', 'ASP', 'NE', 'ARG', 13.04), ('CB', 'ASP', 'CZ', 'ARG', 13.59), ('CB', 'ASP', 'NH1', 'ARG', 14.89), ('CB', 'ASP', 'NH2', 'ARG', 12.96)], [('CG', 'ASP', 'CB', 'ARG', 12.28), ('CG', 'ASP', 'CG', 'ARG', 12.05), ('CG', 'ASP', 'CD', 'ARG', 12.64), ('CG', 'ASP', 'NE', 'ARG', 11.83), ('CG', 'ASP', 'CZ', 'ARG', 12.35), ('CG', 'ASP', 'NH1', 'ARG', 13.62), ('CG', 'ASP', 'NH2', 'ARG', 11.74)], [('OD1', 'ASP', 'CB', 'ARG', 12.41), ('OD1', 'ASP', 'CG', 'ARG', 12.05), ('OD1', 'ASP', 'CD', 'ARG', 12.66), ('OD1', 'ASP', 'NE', 'ARG', 11.93), ('OD1', 'ASP', 'CZ', 'ARG', 12.49), ('OD1', 'ASP', 'NH1', 'ARG', 13.73), ('OD1', 'ASP', 'NH2', 'ARG', 11.96)], [('OD2', 'ASP', 'CB', 'ARG', 11.5), ('OD2', 'ASP', 'CG', 'ARG', 11.31), ('OD2', 'ASP', 'CD', 'ARG', 11.8), ('OD2', 'ASP', 'NE', 'ARG', 10.9), ('OD2', 'ASP', 'CZ', 'ARG', 11.35), ('OD2', 'ASP', 'NH1', 'ARG', 12.63), ('OD2', 'ASP', 'NH2', 'ARG', 10.67)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_LYS, d, 'P_1lcp_3_4_11_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_ARG, d, 'P_1lcp_3_4_11_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ARG, d, 'P_1lcp_3_4_11_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_LYS' :  match1,
		'LYS_ARG' :  match2,
		'ASP_ARG' :  match3}