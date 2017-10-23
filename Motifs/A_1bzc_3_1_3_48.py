'''
FUNC:A_1bzc_3_1_3_48
PDB:1bzc
EC:3.1.3.48
RESI:asp,cys,arg,ser
LOCI:a-181,215,221,222;
'''
import motifFunctions as cmd
ARG_SER = { 
	'distances':
		[[7.42, 7.33], [8.86, 8.75], [9.55, 9.17], [9.35, 8.86], [10.24, 9.58], [11.21, 10.49], [10.41, 9.7]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 7.42), ('CB', 'ARG', 'OG', 'SER', 7.33)], [('CG', 'ARG', 'CB', 'SER', 8.86), ('CG', 'ARG', 'OG', 'SER', 8.75)], [('CD', 'ARG', 'CB', 'SER', 9.55), ('CD', 'ARG', 'OG', 'SER', 9.17)], [('NE', 'ARG', 'CB', 'SER', 9.35), ('NE', 'ARG', 'OG', 'SER', 8.86)], [('CZ', 'ARG', 'CB', 'SER', 10.24), ('CZ', 'ARG', 'OG', 'SER', 9.58)], [('NH1', 'ARG', 'CB', 'SER', 11.21), ('NH1', 'ARG', 'OG', 'SER', 10.49)], [('NH2', 'ARG', 'CB', 'SER', 10.41), ('NH2', 'ARG', 'OG', 'SER', 9.7)]]}
ARG_ASP = { 
	'distances':
		[[9.13, 10.59, 11.02, 11.45], [8.09, 9.5, 9.85, 10.44], [7.16, 8.5, 8.75, 9.51], [6.28, 7.7, 8.16, 8.58], [5.56, 6.85, 7.26, 7.73], [5.76, 6.78, 6.88, 7.81], [5.21, 6.45, 7.1, 7.1]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 9.13), ('CB', 'ARG', 'CG', 'ASP', 10.59), ('CB', 'ARG', 'OD1', 'ASP', 11.02), ('CB', 'ARG', 'OD2', 'ASP', 11.45)], [('CG', 'ARG', 'CB', 'ASP', 8.09), ('CG', 'ARG', 'CG', 'ASP', 9.5), ('CG', 'ARG', 'OD1', 'ASP', 9.85), ('CG', 'ARG', 'OD2', 'ASP', 10.44)], [('CD', 'ARG', 'CB', 'ASP', 7.16), ('CD', 'ARG', 'CG', 'ASP', 8.5), ('CD', 'ARG', 'OD1', 'ASP', 8.75), ('CD', 'ARG', 'OD2', 'ASP', 9.51)], [('NE', 'ARG', 'CB', 'ASP', 6.28), ('NE', 'ARG', 'CG', 'ASP', 7.7), ('NE', 'ARG', 'OD1', 'ASP', 8.16), ('NE', 'ARG', 'OD2', 'ASP', 8.58)], [('CZ', 'ARG', 'CB', 'ASP', 5.56), ('CZ', 'ARG', 'CG', 'ASP', 6.85), ('CZ', 'ARG', 'OD1', 'ASP', 7.26), ('CZ', 'ARG', 'OD2', 'ASP', 7.73)], [('NH1', 'ARG', 'CB', 'ASP', 5.76), ('NH1', 'ARG', 'CG', 'ASP', 6.78), ('NH1', 'ARG', 'OD1', 'ASP', 6.88), ('NH1', 'ARG', 'OD2', 'ASP', 7.81)], [('NH2', 'ARG', 'CB', 'ASP', 5.21), ('NH2', 'ARG', 'CG', 'ASP', 6.45), ('NH2', 'ARG', 'OD1', 'ASP', 7.1), ('NH2', 'ARG', 'OD2', 'ASP', 7.1)]]}
CYS_SER = { 
	'distances':
		[[6.87, 5.89], [5.7, 5.02]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'SER', 6.87), ('CB', 'CYS', 'OG', 'SER', 5.89)], [('SG', 'CYS', 'CB', 'SER', 5.7), ('SG', 'CYS', 'OG', 'SER', 5.02)]]}
CYS_ASP = { 
	'distances':
		[[9.13, 10.47, 11.05, 11.08], [9.66, 11.07, 11.83, 11.55]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 9.13), ('CB', 'CYS', 'CG', 'ASP', 10.47), ('CB', 'CYS', 'OD1', 'ASP', 11.05), ('CB', 'CYS', 'OD2', 'ASP', 11.08)], [('SG', 'CYS', 'CB', 'ASP', 9.66), ('SG', 'CYS', 'CG', 'ASP', 11.07), ('SG', 'CYS', 'OD1', 'ASP', 11.83), ('SG', 'CYS', 'OD2', 'ASP', 11.55)]]}
CYS_ARG = { 
	'distances':
		[[5.85, 6.66, 6.31, 5.6, 5.92, 6.78, 6.03], [5.98, 6.96, 7.08, 6.32, 6.91, 8.01, 6.83]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 5.85), ('CB', 'CYS', 'CG', 'ARG', 6.66), ('CB', 'CYS', 'CD', 'ARG', 6.31), ('CB', 'CYS', 'NE', 'ARG', 5.6), ('CB', 'CYS', 'CZ', 'ARG', 5.92), ('CB', 'CYS', 'NH1', 'ARG', 6.78), ('CB', 'CYS', 'NH2', 'ARG', 6.03)], [('SG', 'CYS', 'CB', 'ARG', 5.98), ('SG', 'CYS', 'CG', 'ARG', 6.96), ('SG', 'CYS', 'CD', 'ARG', 7.08), ('SG', 'CYS', 'NE', 'ARG', 6.32), ('SG', 'CYS', 'CZ', 'ARG', 6.91), ('SG', 'CYS', 'NH1', 'ARG', 8.01), ('SG', 'CYS', 'NH2', 'ARG', 6.83)]]}
SER_ASP = { 
	'distances':
		[[13.09, 14.57, 15.29, 15.09], [12.59, 14.02, 14.71, 14.55]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 13.09), ('CB', 'SER', 'CG', 'ASP', 14.57), ('CB', 'SER', 'OD1', 'ASP', 15.29), ('CB', 'SER', 'OD2', 'ASP', 15.09)], [('OG', 'SER', 'CB', 'ASP', 12.59), ('OG', 'SER', 'CG', 'ASP', 14.02), ('OG', 'SER', 'OD1', 'ASP', 14.71), ('OG', 'SER', 'OD2', 'ASP', 14.55)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_SER, d, 'A_1bzc_3_1_3_48')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_ASP, d, 'A_1bzc_3_1_3_48')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_SER, d, 'A_1bzc_3_1_3_48')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_ASP, d, 'A_1bzc_3_1_3_48')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_ARG, d, 'A_1bzc_3_1_3_48')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ASP, d, 'A_1bzc_3_1_3_48')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_SER' :  match1,
		'ARG_ASP' :  match2,
		'CYS_SER' :  match3,
		'CYS_ASP' :  match4,
		'CYS_ARG' :  match5,
		'SER_ASP' :  match6}