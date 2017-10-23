'''
FUNC:A_1pnt_3_1_3_2
PDB:1pnt
EC:3.1.3.2
RESI:cys,cys,arg,asp
LOCI:a-12,17,18,129;
'''
import motifFunctions as cmd
ARG_ASP = { 
	'distances':
		[[8.97, 8.95, 8.57, 9.49], [7.81, 7.91, 7.47, 8.64], [6.76, 7.15, 7.02, 7.85], [6.32, 6.48, 6.56, 6.93], [5.96, 6.29, 6.75, 6.54], [5.95, 6.71, 7.34, 7.03], [6.23, 6.24, 6.84, 6.12]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 8.97), ('CB', 'ARG', 'CG', 'ASP', 8.95), ('CB', 'ARG', 'OD1', 'ASP', 8.57), ('CB', 'ARG', 'OD2', 'ASP', 9.49)], [('CG', 'ARG', 'CB', 'ASP', 7.81), ('CG', 'ARG', 'CG', 'ASP', 7.91), ('CG', 'ARG', 'OD1', 'ASP', 7.47), ('CG', 'ARG', 'OD2', 'ASP', 8.64)], [('CD', 'ARG', 'CB', 'ASP', 6.76), ('CD', 'ARG', 'CG', 'ASP', 7.15), ('CD', 'ARG', 'OD1', 'ASP', 7.02), ('CD', 'ARG', 'OD2', 'ASP', 7.85)], [('NE', 'ARG', 'CB', 'ASP', 6.32), ('NE', 'ARG', 'CG', 'ASP', 6.48), ('NE', 'ARG', 'OD1', 'ASP', 6.56), ('NE', 'ARG', 'OD2', 'ASP', 6.93)], [('CZ', 'ARG', 'CB', 'ASP', 5.96), ('CZ', 'ARG', 'CG', 'ASP', 6.29), ('CZ', 'ARG', 'OD1', 'ASP', 6.75), ('CZ', 'ARG', 'OD2', 'ASP', 6.54)], [('NH1', 'ARG', 'CB', 'ASP', 5.95), ('NH1', 'ARG', 'CG', 'ASP', 6.71), ('NH1', 'ARG', 'OD1', 'ASP', 7.34), ('NH1', 'ARG', 'OD2', 'ASP', 7.03)], [('NH2', 'ARG', 'CB', 'ASP', 6.23), ('NH2', 'ARG', 'CG', 'ASP', 6.24), ('NH2', 'ARG', 'OD1', 'ASP', 6.84), ('NH2', 'ARG', 'OD2', 'ASP', 6.12)]]}
CYS_ASP = { 
	'distances':
		[[9.81, 9.6, 9.76, 9.49], [10.27, 9.76, 9.68, 9.65], [8.99, 8.09, 7.02, 8.56], [9.35, 8.2, 7.07, 8.5]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 9.81), ('CB', 'CYS', 'CG', 'ASP', 9.6), ('CB', 'CYS', 'OD1', 'ASP', 9.76), ('CB', 'CYS', 'OD2', 'ASP', 9.49)], [('SG', 'CYS', 'CB', 'ASP', 10.27), ('SG', 'CYS', 'CG', 'ASP', 9.76), ('SG', 'CYS', 'OD1', 'ASP', 9.68), ('SG', 'CYS', 'OD2', 'ASP', 9.65)], [('CB', 'CYS', 'CB', 'ASP', 8.99), ('CB', 'CYS', 'CG', 'ASP', 8.09), ('CB', 'CYS', 'OD1', 'ASP', 7.02), ('CB', 'CYS', 'OD2', 'ASP', 8.56)], [('SG', 'CYS', 'CB', 'ASP', 9.35), ('SG', 'CYS', 'CG', 'ASP', 8.2), ('SG', 'CYS', 'OD1', 'ASP', 7.07), ('SG', 'CYS', 'OD2', 'ASP', 8.5)]]}
CYS_CYS = { 
	'distances':
		[[9.02, 10.18], [7.97, 9.02], [9.02, 7.97], [10.18, 9.02]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'CYS', 9.02), ('CB', 'CYS', 'SG', 'CYS', 10.18)], [('SG', 'CYS', 'CB', 'CYS', 7.97), ('SG', 'CYS', 'SG', 'CYS', 9.02)], [('CB', 'CYS', 'CB', 'CYS', 9.02), ('CB', 'CYS', 'SG', 'CYS', 7.97)], [('SG', 'CYS', 'CB', 'CYS', 10.18), ('SG', 'CYS', 'SG', 'CYS', 9.02)]]}
CYS_ARG = { 
	'distances':
		[[6.14, 7.11, 7.01, 6.06, 6.15, 7.1, 5.8], [6.22, 7.28, 7.59, 6.69, 7.1, 8.27, 6.68], [6.94, 6.64, 7.59, 7.46, 8.53, 9.65, 8.68], [8.64, 8.26, 9.01, 8.7, 9.57, 10.7, 9.51]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 6.14), ('CB', 'CYS', 'CG', 'ARG', 7.11), ('CB', 'CYS', 'CD', 'ARG', 7.01), ('CB', 'CYS', 'NE', 'ARG', 6.06), ('CB', 'CYS', 'CZ', 'ARG', 6.15), ('CB', 'CYS', 'NH1', 'ARG', 7.1), ('CB', 'CYS', 'NH2', 'ARG', 5.8)], [('SG', 'CYS', 'CB', 'ARG', 6.22), ('SG', 'CYS', 'CG', 'ARG', 7.28), ('SG', 'CYS', 'CD', 'ARG', 7.59), ('SG', 'CYS', 'NE', 'ARG', 6.69), ('SG', 'CYS', 'CZ', 'ARG', 7.1), ('SG', 'CYS', 'NH1', 'ARG', 8.27), ('SG', 'CYS', 'NH2', 'ARG', 6.68)], [('CB', 'CYS', 'CB', 'ARG', 6.94), ('CB', 'CYS', 'CG', 'ARG', 6.64), ('CB', 'CYS', 'CD', 'ARG', 7.59), ('CB', 'CYS', 'NE', 'ARG', 7.46), ('CB', 'CYS', 'CZ', 'ARG', 8.53), ('CB', 'CYS', 'NH1', 'ARG', 9.65), ('CB', 'CYS', 'NH2', 'ARG', 8.68)], [('SG', 'CYS', 'CB', 'ARG', 8.64), ('SG', 'CYS', 'CG', 'ARG', 8.26), ('SG', 'CYS', 'CD', 'ARG', 9.01), ('SG', 'CYS', 'NE', 'ARG', 8.7), ('SG', 'CYS', 'CZ', 'ARG', 9.57), ('SG', 'CYS', 'NH1', 'ARG', 10.7), ('SG', 'CYS', 'NH2', 'ARG', 9.51)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_ASP, d, 'A_1pnt_3_1_3_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_ASP, d, 'A_1pnt_3_1_3_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_CYS, d, 'A_1pnt_3_1_3_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_ARG, d, 'A_1pnt_3_1_3_2')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_ASP' :  match1,
		'CYS_ASP' :  match2,
		'CYS_CYS' :  match3,
		'CYS_ARG' :  match4}