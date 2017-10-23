'''
FUNC:A_1pa9_3_1_3_48
PDB:1pa9
EC:3.1.3.48
RESI:asp,cys,arg,thr
LOCI:a-194,241,247,248;
'''
import motifFunctions as cmd
THR_ASP = { 
	'distances':
		[[13.56, 13.08, 11.9, 14.0], [12.98, 12.55, 11.43, 13.46], [15.07, 14.56, 13.38, 15.45]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 13.56), ('CB', 'THR', 'CG', 'ASP', 13.08), ('CB', 'THR', 'OD1', 'ASP', 11.9), ('CB', 'THR', 'OD2', 'ASP', 14.0)], [('OG1', 'THR', 'CB', 'ASP', 12.98), ('OG1', 'THR', 'CG', 'ASP', 12.55), ('OG1', 'THR', 'OD1', 'ASP', 11.43), ('OG1', 'THR', 'OD2', 'ASP', 13.46)], [('CG2', 'THR', 'CB', 'ASP', 15.07), ('CG2', 'THR', 'CG', 'ASP', 14.56), ('CG2', 'THR', 'OD1', 'ASP', 13.38), ('CG2', 'THR', 'OD2', 'ASP', 15.45)]]}
CYS_THR = { 
	'distances':
		[[6.76, 5.72, 8.09], [5.77, 5.1, 7.17]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'THR', 6.76), ('CB', 'CYS', 'OG1', 'THR', 5.72), ('CB', 'CYS', 'CG2', 'THR', 8.09)], [('SG', 'CYS', 'CB', 'THR', 5.77), ('SG', 'CYS', 'OG1', 'THR', 5.1), ('SG', 'CYS', 'CG2', 'THR', 7.17)]]}
ARG_ASP = { 
	'distances':
		[[9.52, 9.57, 8.6, 10.75], [8.35, 8.54, 7.69, 9.75], [7.3, 7.69, 7.0, 8.94], [6.54, 6.68, 5.89, 7.89], [5.78, 6.06, 5.51, 7.23], [5.76, 6.49, 6.27, 7.62], [5.67, 5.57, 4.98, 6.57]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 9.52), ('CB', 'ARG', 'CG', 'ASP', 9.57), ('CB', 'ARG', 'OD1', 'ASP', 8.6), ('CB', 'ARG', 'OD2', 'ASP', 10.75)], [('CG', 'ARG', 'CB', 'ASP', 8.35), ('CG', 'ARG', 'CG', 'ASP', 8.54), ('CG', 'ARG', 'OD1', 'ASP', 7.69), ('CG', 'ARG', 'OD2', 'ASP', 9.75)], [('CD', 'ARG', 'CB', 'ASP', 7.3), ('CD', 'ARG', 'CG', 'ASP', 7.69), ('CD', 'ARG', 'OD1', 'ASP', 7.0), ('CD', 'ARG', 'OD2', 'ASP', 8.94)], [('NE', 'ARG', 'CB', 'ASP', 6.54), ('NE', 'ARG', 'CG', 'ASP', 6.68), ('NE', 'ARG', 'OD1', 'ASP', 5.89), ('NE', 'ARG', 'OD2', 'ASP', 7.89)], [('CZ', 'ARG', 'CB', 'ASP', 5.78), ('CZ', 'ARG', 'CG', 'ASP', 6.06), ('CZ', 'ARG', 'OD1', 'ASP', 5.51), ('CZ', 'ARG', 'OD2', 'ASP', 7.23)], [('NH1', 'ARG', 'CB', 'ASP', 5.76), ('NH1', 'ARG', 'CG', 'ASP', 6.49), ('NH1', 'ARG', 'OD1', 'ASP', 6.27), ('NH1', 'ARG', 'OD2', 'ASP', 7.62)], [('NH2', 'ARG', 'CB', 'ASP', 5.67), ('NH2', 'ARG', 'CG', 'ASP', 5.57), ('NH2', 'ARG', 'OD1', 'ASP', 4.98), ('NH2', 'ARG', 'OD2', 'ASP', 6.57)]]}
CYS_ASP = { 
	'distances':
		[[9.55, 9.28, 8.32, 10.24], [10.07, 9.51, 8.38, 10.38]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 9.55), ('CB', 'CYS', 'CG', 'ASP', 9.28), ('CB', 'CYS', 'OD1', 'ASP', 8.32), ('CB', 'CYS', 'OD2', 'ASP', 10.24)], [('SG', 'CYS', 'CB', 'ASP', 10.07), ('SG', 'CYS', 'CG', 'ASP', 9.51), ('SG', 'CYS', 'OD1', 'ASP', 8.38), ('SG', 'CYS', 'OD2', 'ASP', 10.38)]]}
ARG_THR = { 
	'distances':
		[[7.43, 7.33, 8.85], [8.85, 8.71, 10.3], [9.58, 9.16, 11.05], [9.38, 8.83, 10.89], [10.27, 9.54, 11.74], [11.26, 10.48, 12.71], [10.38, 9.58, 11.83]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'THR', 7.43), ('CB', 'ARG', 'OG1', 'THR', 7.33), ('CB', 'ARG', 'CG2', 'THR', 8.85)], [('CG', 'ARG', 'CB', 'THR', 8.85), ('CG', 'ARG', 'OG1', 'THR', 8.71), ('CG', 'ARG', 'CG2', 'THR', 10.3)], [('CD', 'ARG', 'CB', 'THR', 9.58), ('CD', 'ARG', 'OG1', 'THR', 9.16), ('CD', 'ARG', 'CG2', 'THR', 11.05)], [('NE', 'ARG', 'CB', 'THR', 9.38), ('NE', 'ARG', 'OG1', 'THR', 8.83), ('NE', 'ARG', 'CG2', 'THR', 10.89)], [('CZ', 'ARG', 'CB', 'THR', 10.27), ('CZ', 'ARG', 'OG1', 'THR', 9.54), ('CZ', 'ARG', 'CG2', 'THR', 11.74)], [('NH1', 'ARG', 'CB', 'THR', 11.26), ('NH1', 'ARG', 'OG1', 'THR', 10.48), ('NH1', 'ARG', 'CG2', 'THR', 12.71)], [('NH2', 'ARG', 'CB', 'THR', 10.38), ('NH2', 'ARG', 'OG1', 'THR', 9.58), ('NH2', 'ARG', 'CG2', 'THR', 11.83)]]}
CYS_ARG = { 
	'distances':
		[[6.02, 6.79, 6.49, 5.72, 6.04, 6.97, 5.99], [6.14, 7.02, 7.18, 6.38, 6.97, 8.13, 6.78]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ARG', 6.02), ('CB', 'CYS', 'CG', 'ARG', 6.79), ('CB', 'CYS', 'CD', 'ARG', 6.49), ('CB', 'CYS', 'NE', 'ARG', 5.72), ('CB', 'CYS', 'CZ', 'ARG', 6.04), ('CB', 'CYS', 'NH1', 'ARG', 6.97), ('CB', 'CYS', 'NH2', 'ARG', 5.99)], [('SG', 'CYS', 'CB', 'ARG', 6.14), ('SG', 'CYS', 'CG', 'ARG', 7.02), ('SG', 'CYS', 'CD', 'ARG', 7.18), ('SG', 'CYS', 'NE', 'ARG', 6.38), ('SG', 'CYS', 'CZ', 'ARG', 6.97), ('SG', 'CYS', 'NH1', 'ARG', 8.13), ('SG', 'CYS', 'NH2', 'ARG', 6.78)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_ASP, d, 'A_1pa9_3_1_3_48')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_THR, d, 'A_1pa9_3_1_3_48')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ASP, d, 'A_1pa9_3_1_3_48')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(CYS_ASP, d, 'A_1pa9_3_1_3_48')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_THR, d, 'A_1pa9_3_1_3_48')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_ARG, d, 'A_1pa9_3_1_3_48')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_ASP' :  match1,
		'CYS_THR' :  match2,
		'ARG_ASP' :  match3,
		'CYS_ASP' :  match4,
		'ARG_THR' :  match5,
		'CYS_ARG' :  match6}