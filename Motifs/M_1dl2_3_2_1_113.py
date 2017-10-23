'''
FUNC:M_1dl2_3_2_1_113
PDB:1dl2
EC:3.2.1.113
RESI:glu,arg,asp,glu,ca
LOCI:a-132,136,275,435,901;
'''
import motifFunctions as cmd
GLU_GLU = { 
	'distances':
		[[18.32, 17.5, 16.07, 15.72, 15.4], [16.87, 16.06, 14.65, 14.31, 13.99], [15.89, 15.07, 13.62, 13.25, 12.95], [14.76, 13.99, 12.54, 12.12, 11.94], [16.35, 15.48, 14.01, 13.68, 13.29], [18.32, 16.87, 15.89, 14.76, 16.35], [17.5, 16.06, 15.07, 13.99, 15.48], [16.07, 14.65, 13.62, 12.54, 14.01], [15.72, 14.31, 13.25, 12.12, 13.68], [15.4, 13.99, 12.95, 11.94, 13.29]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'GLU', 18.32), ('CB', 'GLU', 'CG', 'GLU', 17.5), ('CB', 'GLU', 'CD', 'GLU', 16.07), ('CB', 'GLU', 'OE1', 'GLU', 15.72), ('CB', 'GLU', 'OE2', 'GLU', 15.4)], [('CG', 'GLU', 'CB', 'GLU', 16.87), ('CG', 'GLU', 'CG', 'GLU', 16.06), ('CG', 'GLU', 'CD', 'GLU', 14.65), ('CG', 'GLU', 'OE1', 'GLU', 14.31), ('CG', 'GLU', 'OE2', 'GLU', 13.99)], [('CD', 'GLU', 'CB', 'GLU', 15.89), ('CD', 'GLU', 'CG', 'GLU', 15.07), ('CD', 'GLU', 'CD', 'GLU', 13.62), ('CD', 'GLU', 'OE1', 'GLU', 13.25), ('CD', 'GLU', 'OE2', 'GLU', 12.95)], [('OE1', 'GLU', 'CB', 'GLU', 14.76), ('OE1', 'GLU', 'CG', 'GLU', 13.99), ('OE1', 'GLU', 'CD', 'GLU', 12.54), ('OE1', 'GLU', 'OE1', 'GLU', 12.12), ('OE1', 'GLU', 'OE2', 'GLU', 11.94)], [('OE2', 'GLU', 'CB', 'GLU', 16.35), ('OE2', 'GLU', 'CG', 'GLU', 15.48), ('OE2', 'GLU', 'CD', 'GLU', 14.01), ('OE2', 'GLU', 'OE1', 'GLU', 13.68), ('OE2', 'GLU', 'OE2', 'GLU', 13.29)], [('CB', 'GLU', 'CB', 'GLU', 18.32), ('CB', 'GLU', 'CG', 'GLU', 16.87), ('CB', 'GLU', 'CD', 'GLU', 15.89), ('CB', 'GLU', 'OE1', 'GLU', 14.76), ('CB', 'GLU', 'OE2', 'GLU', 16.35)], [('CG', 'GLU', 'CB', 'GLU', 17.5), ('CG', 'GLU', 'CG', 'GLU', 16.06), ('CG', 'GLU', 'CD', 'GLU', 15.07), ('CG', 'GLU', 'OE1', 'GLU', 13.99), ('CG', 'GLU', 'OE2', 'GLU', 15.48)], [('CD', 'GLU', 'CB', 'GLU', 16.07), ('CD', 'GLU', 'CG', 'GLU', 14.65), ('CD', 'GLU', 'CD', 'GLU', 13.62), ('CD', 'GLU', 'OE1', 'GLU', 12.54), ('CD', 'GLU', 'OE2', 'GLU', 14.01)], [('OE1', 'GLU', 'CB', 'GLU', 15.72), ('OE1', 'GLU', 'CG', 'GLU', 14.31), ('OE1', 'GLU', 'CD', 'GLU', 13.25), ('OE1', 'GLU', 'OE1', 'GLU', 12.12), ('OE1', 'GLU', 'OE2', 'GLU', 13.68)], [('OE2', 'GLU', 'CB', 'GLU', 15.4), ('OE2', 'GLU', 'CG', 'GLU', 13.99), ('OE2', 'GLU', 'CD', 'GLU', 12.95), ('OE2', 'GLU', 'OE1', 'GLU', 11.94), ('OE2', 'GLU', 'OE2', 'GLU', 13.29)]]}
ARG_CA = { 
	'distances':
		[[12.64], [11.56], [12.09], [11.59], [11.96], [12.74], [11.79]],
	'comparisons':
		[[('CB', 'ARG', 'CA', 'CA', 12.64)], [('CG', 'ARG', 'CA', 'CA', 11.56)], [('CD', 'ARG', 'CA', 'CA', 12.09)], [('NE', 'ARG', 'CA', 'CA', 11.59)], [('CZ', 'ARG', 'CA', 'CA', 11.96)], [('NH1', 'ARG', 'CA', 'CA', 12.74)], [('NH2', 'ARG', 'CA', 'CA', 11.79)]]}
ASP_CA = { 
	'distances':
		[[9.05], [8.52], [8.07], [8.86]],
	'comparisons':
		[[('CB', 'ASP', 'CA', 'CA', 9.05)], [('CG', 'ASP', 'CA', 'CA', 8.52)], [('OD1', 'ASP', 'CA', 'CA', 8.07)], [('OD2', 'ASP', 'CA', 'CA', 8.86)]]}
ARG_GLU = { 
	'distances':
		[[17.57, 16.28, 15.28, 14.06, 15.82], [16.33, 15.02, 13.99, 12.77, 14.5], [16.27, 15.01, 13.85, 12.68, 14.22], [15.51, 14.24, 13.04, 11.89, 13.35], [15.26, 14.05, 12.75, 11.67, 12.93], [15.69, 14.57, 13.22, 12.18, 13.3], [14.79, 13.56, 12.25, 11.22, 12.37], [7.75, 8.72, 8.33, 7.18, 9.38], [7.06, 7.76, 7.11, 5.9, 8.06], [7.27, 7.77, 7.01, 5.83, 7.83], [6.77, 6.9, 5.9, 4.79, 6.55], [7.51, 7.39, 6.29, 5.42, 6.66], [8.58, 8.56, 7.55, 6.7, 7.91], [7.49, 7.0, 5.76, 5.21, 5.8]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 17.57), ('CB', 'ARG', 'CG', 'GLU', 16.28), ('CB', 'ARG', 'CD', 'GLU', 15.28), ('CB', 'ARG', 'OE1', 'GLU', 14.06), ('CB', 'ARG', 'OE2', 'GLU', 15.82)], [('CG', 'ARG', 'CB', 'GLU', 16.33), ('CG', 'ARG', 'CG', 'GLU', 15.02), ('CG', 'ARG', 'CD', 'GLU', 13.99), ('CG', 'ARG', 'OE1', 'GLU', 12.77), ('CG', 'ARG', 'OE2', 'GLU', 14.5)], [('CD', 'ARG', 'CB', 'GLU', 16.27), ('CD', 'ARG', 'CG', 'GLU', 15.01), ('CD', 'ARG', 'CD', 'GLU', 13.85), ('CD', 'ARG', 'OE1', 'GLU', 12.68), ('CD', 'ARG', 'OE2', 'GLU', 14.22)], [('NE', 'ARG', 'CB', 'GLU', 15.51), ('NE', 'ARG', 'CG', 'GLU', 14.24), ('NE', 'ARG', 'CD', 'GLU', 13.04), ('NE', 'ARG', 'OE1', 'GLU', 11.89), ('NE', 'ARG', 'OE2', 'GLU', 13.35)], [('CZ', 'ARG', 'CB', 'GLU', 15.26), ('CZ', 'ARG', 'CG', 'GLU', 14.05), ('CZ', 'ARG', 'CD', 'GLU', 12.75), ('CZ', 'ARG', 'OE1', 'GLU', 11.67), ('CZ', 'ARG', 'OE2', 'GLU', 12.93)], [('NH1', 'ARG', 'CB', 'GLU', 15.69), ('NH1', 'ARG', 'CG', 'GLU', 14.57), ('NH1', 'ARG', 'CD', 'GLU', 13.22), ('NH1', 'ARG', 'OE1', 'GLU', 12.18), ('NH1', 'ARG', 'OE2', 'GLU', 13.3)], [('NH2', 'ARG', 'CB', 'GLU', 14.79), ('NH2', 'ARG', 'CG', 'GLU', 13.56), ('NH2', 'ARG', 'CD', 'GLU', 12.25), ('NH2', 'ARG', 'OE1', 'GLU', 11.22), ('NH2', 'ARG', 'OE2', 'GLU', 12.37)], [('CB', 'ARG', 'CB', 'GLU', 7.75), ('CB', 'ARG', 'CG', 'GLU', 8.72), ('CB', 'ARG', 'CD', 'GLU', 8.33), ('CB', 'ARG', 'OE1', 'GLU', 7.18), ('CB', 'ARG', 'OE2', 'GLU', 9.38)], [('CG', 'ARG', 'CB', 'GLU', 7.06), ('CG', 'ARG', 'CG', 'GLU', 7.76), ('CG', 'ARG', 'CD', 'GLU', 7.11), ('CG', 'ARG', 'OE1', 'GLU', 5.9), ('CG', 'ARG', 'OE2', 'GLU', 8.06)], [('CD', 'ARG', 'CB', 'GLU', 7.27), ('CD', 'ARG', 'CG', 'GLU', 7.77), ('CD', 'ARG', 'CD', 'GLU', 7.01), ('CD', 'ARG', 'OE1', 'GLU', 5.83), ('CD', 'ARG', 'OE2', 'GLU', 7.83)], [('NE', 'ARG', 'CB', 'GLU', 6.77), ('NE', 'ARG', 'CG', 'GLU', 6.9), ('NE', 'ARG', 'CD', 'GLU', 5.9), ('NE', 'ARG', 'OE1', 'GLU', 4.79), ('NE', 'ARG', 'OE2', 'GLU', 6.55)], [('CZ', 'ARG', 'CB', 'GLU', 7.51), ('CZ', 'ARG', 'CG', 'GLU', 7.39), ('CZ', 'ARG', 'CD', 'GLU', 6.29), ('CZ', 'ARG', 'OE1', 'GLU', 5.42), ('CZ', 'ARG', 'OE2', 'GLU', 6.66)], [('NH1', 'ARG', 'CB', 'GLU', 8.58), ('NH1', 'ARG', 'CG', 'GLU', 8.56), ('NH1', 'ARG', 'CD', 'GLU', 7.55), ('NH1', 'ARG', 'OE1', 'GLU', 6.7), ('NH1', 'ARG', 'OE2', 'GLU', 7.91)], [('NH2', 'ARG', 'CB', 'GLU', 7.49), ('NH2', 'ARG', 'CG', 'GLU', 7.0), ('NH2', 'ARG', 'CD', 'GLU', 5.76), ('NH2', 'ARG', 'OE1', 'GLU', 5.21), ('NH2', 'ARG', 'OE2', 'GLU', 5.8)]]}
GLU_CA = { 
	'distances':
		[[8.48], [7.12], [7.17], [6.27], [8.36], [13.6], [13.15], [11.92], [11.39], [11.65]],
	'comparisons':
		[[('CB', 'GLU', 'CA', 'CA', 8.48)], [('CG', 'GLU', 'CA', 'CA', 7.12)], [('CD', 'GLU', 'CA', 'CA', 7.17)], [('OE1', 'GLU', 'CA', 'CA', 6.27)], [('OE2', 'GLU', 'CA', 'CA', 8.36)], [('CB', 'GLU', 'CA', 'CA', 13.6)], [('CG', 'GLU', 'CA', 'CA', 13.15)], [('CD', 'GLU', 'CA', 'CA', 11.92)], [('OE1', 'GLU', 'CA', 'CA', 11.39)], [('OE2', 'GLU', 'CA', 'CA', 11.65)]]}
ARG_ASP = { 
	'distances':
		[[17.78, 16.51, 16.05, 16.09], [16.51, 15.21, 14.69, 14.82], [16.93, 15.59, 14.96, 15.27], [15.96, 14.58, 13.91, 14.28], [16.14, 14.76, 13.98, 14.54], [17.21, 15.85, 15.02, 15.7], [15.39, 13.98, 13.16, 13.77]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'ASP', 17.78), ('CB', 'ARG', 'CG', 'ASP', 16.51), ('CB', 'ARG', 'OD1', 'ASP', 16.05), ('CB', 'ARG', 'OD2', 'ASP', 16.09)], [('CG', 'ARG', 'CB', 'ASP', 16.51), ('CG', 'ARG', 'CG', 'ASP', 15.21), ('CG', 'ARG', 'OD1', 'ASP', 14.69), ('CG', 'ARG', 'OD2', 'ASP', 14.82)], [('CD', 'ARG', 'CB', 'ASP', 16.93), ('CD', 'ARG', 'CG', 'ASP', 15.59), ('CD', 'ARG', 'OD1', 'ASP', 14.96), ('CD', 'ARG', 'OD2', 'ASP', 15.27)], [('NE', 'ARG', 'CB', 'ASP', 15.96), ('NE', 'ARG', 'CG', 'ASP', 14.58), ('NE', 'ARG', 'OD1', 'ASP', 13.91), ('NE', 'ARG', 'OD2', 'ASP', 14.28)], [('CZ', 'ARG', 'CB', 'ASP', 16.14), ('CZ', 'ARG', 'CG', 'ASP', 14.76), ('CZ', 'ARG', 'OD1', 'ASP', 13.98), ('CZ', 'ARG', 'OD2', 'ASP', 14.54)], [('NH1', 'ARG', 'CB', 'ASP', 17.21), ('NH1', 'ARG', 'CG', 'ASP', 15.85), ('NH1', 'ARG', 'OD1', 'ASP', 15.02), ('NH1', 'ARG', 'OD2', 'ASP', 15.7)], [('NH2', 'ARG', 'CB', 'ASP', 15.39), ('NH2', 'ARG', 'CG', 'ASP', 13.98), ('NH2', 'ARG', 'OD1', 'ASP', 13.16), ('NH2', 'ARG', 'OD2', 'ASP', 13.77)]]}
GLU_ASP = { 
	'distances':
		[[10.47, 10.54, 9.65, 11.62], [9.46, 9.34, 8.42, 10.35], [10.09, 9.7, 8.65, 10.61], [10.03, 9.46, 8.43, 10.23], [10.9, 10.49, 9.37, 11.42], [16.16, 14.68, 14.36, 13.96], [15.17, 13.67, 13.3, 12.97], [14.29, 12.79, 12.31, 12.22], [14.5, 13.04, 12.52, 12.53], [13.54, 12.02, 11.47, 11.49]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 10.47), ('CB', 'GLU', 'CG', 'ASP', 10.54), ('CB', 'GLU', 'OD1', 'ASP', 9.65), ('CB', 'GLU', 'OD2', 'ASP', 11.62)], [('CG', 'GLU', 'CB', 'ASP', 9.46), ('CG', 'GLU', 'CG', 'ASP', 9.34), ('CG', 'GLU', 'OD1', 'ASP', 8.42), ('CG', 'GLU', 'OD2', 'ASP', 10.35)], [('CD', 'GLU', 'CB', 'ASP', 10.09), ('CD', 'GLU', 'CG', 'ASP', 9.7), ('CD', 'GLU', 'OD1', 'ASP', 8.65), ('CD', 'GLU', 'OD2', 'ASP', 10.61)], [('OE1', 'GLU', 'CB', 'ASP', 10.03), ('OE1', 'GLU', 'CG', 'ASP', 9.46), ('OE1', 'GLU', 'OD1', 'ASP', 8.43), ('OE1', 'GLU', 'OD2', 'ASP', 10.23)], [('OE2', 'GLU', 'CB', 'ASP', 10.9), ('OE2', 'GLU', 'CG', 'ASP', 10.49), ('OE2', 'GLU', 'OD1', 'ASP', 9.37), ('OE2', 'GLU', 'OD2', 'ASP', 11.42)], [('CB', 'GLU', 'CB', 'ASP', 16.16), ('CB', 'GLU', 'CG', 'ASP', 14.68), ('CB', 'GLU', 'OD1', 'ASP', 14.36), ('CB', 'GLU', 'OD2', 'ASP', 13.96)], [('CG', 'GLU', 'CB', 'ASP', 15.17), ('CG', 'GLU', 'CG', 'ASP', 13.67), ('CG', 'GLU', 'OD1', 'ASP', 13.3), ('CG', 'GLU', 'OD2', 'ASP', 12.97)], [('CD', 'GLU', 'CB', 'ASP', 14.29), ('CD', 'GLU', 'CG', 'ASP', 12.79), ('CD', 'GLU', 'OD1', 'ASP', 12.31), ('CD', 'GLU', 'OD2', 'ASP', 12.22)], [('OE1', 'GLU', 'CB', 'ASP', 14.5), ('OE1', 'GLU', 'CG', 'ASP', 13.04), ('OE1', 'GLU', 'OD1', 'ASP', 12.52), ('OE1', 'GLU', 'OD2', 'ASP', 12.53)], [('OE2', 'GLU', 'CB', 'ASP', 13.54), ('OE2', 'GLU', 'CG', 'ASP', 12.02), ('OE2', 'GLU', 'OD1', 'ASP', 11.47), ('OE2', 'GLU', 'OD2', 'ASP', 11.49)]]}
CA_GLUI = { 
	'distances':
		[13.6, 13.15, 11.92, 11.39, 11.65],
	'comparisons':
		[('CA', 'CA', 'CB', 'GLUI', 13.6), ('CA', 'CA', 'CG', 'GLUI', 13.15), ('CA', 'CA', 'CD', 'GLUI', 11.92), ('CA', 'CA', 'OE1', 'GLUI', 11.39), ('CA', 'CA', 'OE2', 'GLUI', 11.65)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_GLU, d, 'M_1dl2_3_2_1_113')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_CA, d, 'M_1dl2_3_2_1_113')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_CA, d, 'M_1dl2_3_2_1_113')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_GLU, d, 'M_1dl2_3_2_1_113')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_CA, d, 'M_1dl2_3_2_1_113')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_ASP, d, 'M_1dl2_3_2_1_113')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLU_ASP, d, 'M_1dl2_3_2_1_113')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(CA_GLUI, d, 'M_1dl2_3_2_1_113')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_GLU' :  match1,
		'ARG_CA' :  match2,
		'ASP_CA' :  match3,
		'ARG_GLU' :  match4,
		'GLU_CA' :  match5,
		'ARG_ASP' :  match6,
		'GLU_ASP' :  match7,
		'CA_GLUI' :  match8}