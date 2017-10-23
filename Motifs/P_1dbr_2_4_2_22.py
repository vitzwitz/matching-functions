'''
FUNC:P_1dbr_2_4_2_22
PDB:1dbr
EC:2.4.2.22
RESI:glu,asp,asp,lys
LOCI:a-146,147,150,178;
'''
import motifFunctions as cmd
LYS_ASP = { 
	'distances':
		[[13.3, 13.09, 13.28, 12.94], [12.3, 12.14, 12.47, 11.91], [12.61, 12.32, 12.7, 11.91], [11.47, 11.14, 11.61, 10.63], [11.88, 11.36, 11.8, 10.7], [9.54, 8.6, 7.61, 9.03], [9.45, 8.49, 7.33, 9.02], [9.29, 8.12, 6.96, 8.49], [8.82, 7.68, 6.44, 8.16], [8.42, 7.14, 6.0, 7.43]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ASP', 13.3), ('CB', 'LYS', 'CG', 'ASP', 13.09), ('CB', 'LYS', 'OD1', 'ASP', 13.28), ('CB', 'LYS', 'OD2', 'ASP', 12.94)], [('CG', 'LYS', 'CB', 'ASP', 12.3), ('CG', 'LYS', 'CG', 'ASP', 12.14), ('CG', 'LYS', 'OD1', 'ASP', 12.47), ('CG', 'LYS', 'OD2', 'ASP', 11.91)], [('CD', 'LYS', 'CB', 'ASP', 12.61), ('CD', 'LYS', 'CG', 'ASP', 12.32), ('CD', 'LYS', 'OD1', 'ASP', 12.7), ('CD', 'LYS', 'OD2', 'ASP', 11.91)], [('CE', 'LYS', 'CB', 'ASP', 11.47), ('CE', 'LYS', 'CG', 'ASP', 11.14), ('CE', 'LYS', 'OD1', 'ASP', 11.61), ('CE', 'LYS', 'OD2', 'ASP', 10.63)], [('NZ', 'LYS', 'CB', 'ASP', 11.88), ('NZ', 'LYS', 'CG', 'ASP', 11.36), ('NZ', 'LYS', 'OD1', 'ASP', 11.8), ('NZ', 'LYS', 'OD2', 'ASP', 10.7)], [('CB', 'LYS', 'CB', 'ASP', 9.54), ('CB', 'LYS', 'CG', 'ASP', 8.6), ('CB', 'LYS', 'OD1', 'ASP', 7.61), ('CB', 'LYS', 'OD2', 'ASP', 9.03)], [('CG', 'LYS', 'CB', 'ASP', 9.45), ('CG', 'LYS', 'CG', 'ASP', 8.49), ('CG', 'LYS', 'OD1', 'ASP', 7.33), ('CG', 'LYS', 'OD2', 'ASP', 9.02)], [('CD', 'LYS', 'CB', 'ASP', 9.29), ('CD', 'LYS', 'CG', 'ASP', 8.12), ('CD', 'LYS', 'OD1', 'ASP', 6.96), ('CD', 'LYS', 'OD2', 'ASP', 8.49)], [('CE', 'LYS', 'CB', 'ASP', 8.82), ('CE', 'LYS', 'CG', 'ASP', 7.68), ('CE', 'LYS', 'OD1', 'ASP', 6.44), ('CE', 'LYS', 'OD2', 'ASP', 8.16)], [('NZ', 'LYS', 'CB', 'ASP', 8.42), ('NZ', 'LYS', 'CG', 'ASP', 7.14), ('NZ', 'LYS', 'OD1', 'ASP', 6.0), ('NZ', 'LYS', 'OD2', 'ASP', 7.43)]]}
GLU_LYS = { 
	'distances':
		[[13.92, 13.54, 14.22, 13.55, 14.04], [14.62, 14.3, 14.89, 14.21, 14.56], [14.09, 13.73, 14.17, 13.42, 13.62], [13.57, 13.07, 13.44, 12.58, 12.76], [14.34, 14.06, 14.44, 13.73, 13.82]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'LYS', 13.92), ('CB', 'GLU', 'CG', 'LYS', 13.54), ('CB', 'GLU', 'CD', 'LYS', 14.22), ('CB', 'GLU', 'CE', 'LYS', 13.55), ('CB', 'GLU', 'NZ', 'LYS', 14.04)], [('CG', 'GLU', 'CB', 'LYS', 14.62), ('CG', 'GLU', 'CG', 'LYS', 14.3), ('CG', 'GLU', 'CD', 'LYS', 14.89), ('CG', 'GLU', 'CE', 'LYS', 14.21), ('CG', 'GLU', 'NZ', 'LYS', 14.56)], [('CD', 'GLU', 'CB', 'LYS', 14.09), ('CD', 'GLU', 'CG', 'LYS', 13.73), ('CD', 'GLU', 'CD', 'LYS', 14.17), ('CD', 'GLU', 'CE', 'LYS', 13.42), ('CD', 'GLU', 'NZ', 'LYS', 13.62)], [('OE1', 'GLU', 'CB', 'LYS', 13.57), ('OE1', 'GLU', 'CG', 'LYS', 13.07), ('OE1', 'GLU', 'CD', 'LYS', 13.44), ('OE1', 'GLU', 'CE', 'LYS', 12.58), ('OE1', 'GLU', 'NZ', 'LYS', 12.76)], [('OE2', 'GLU', 'CB', 'LYS', 14.34), ('OE2', 'GLU', 'CG', 'LYS', 14.06), ('OE2', 'GLU', 'CD', 'LYS', 14.44), ('OE2', 'GLU', 'CE', 'LYS', 13.73), ('OE2', 'GLU', 'NZ', 'LYS', 13.82)]]}
ASP_ASP = { 
	'distances':
		[[10.93, 11.44, 10.84, 12.65], [9.78, 10.37, 9.89, 11.54], [9.3, 10.09, 9.77, 11.26], [9.53, 9.98, 9.48, 11.07], [10.93, 9.78, 9.3, 9.53], [11.44, 10.37, 10.09, 9.98], [10.84, 9.89, 9.77, 9.48], [12.65, 11.54, 11.26, 11.07]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASP', 10.93), ('CB', 'ASP', 'CG', 'ASP', 11.44), ('CB', 'ASP', 'OD1', 'ASP', 10.84), ('CB', 'ASP', 'OD2', 'ASP', 12.65)], [('CG', 'ASP', 'CB', 'ASP', 9.78), ('CG', 'ASP', 'CG', 'ASP', 10.37), ('CG', 'ASP', 'OD1', 'ASP', 9.89), ('CG', 'ASP', 'OD2', 'ASP', 11.54)], [('OD1', 'ASP', 'CB', 'ASP', 9.3), ('OD1', 'ASP', 'CG', 'ASP', 10.09), ('OD1', 'ASP', 'OD1', 'ASP', 9.77), ('OD1', 'ASP', 'OD2', 'ASP', 11.26)], [('OD2', 'ASP', 'CB', 'ASP', 9.53), ('OD2', 'ASP', 'CG', 'ASP', 9.98), ('OD2', 'ASP', 'OD1', 'ASP', 9.48), ('OD2', 'ASP', 'OD2', 'ASP', 11.07)], [('CB', 'ASP', 'CB', 'ASP', 10.93), ('CB', 'ASP', 'CG', 'ASP', 9.78), ('CB', 'ASP', 'OD1', 'ASP', 9.3), ('CB', 'ASP', 'OD2', 'ASP', 9.53)], [('CG', 'ASP', 'CB', 'ASP', 11.44), ('CG', 'ASP', 'CG', 'ASP', 10.37), ('CG', 'ASP', 'OD1', 'ASP', 10.09), ('CG', 'ASP', 'OD2', 'ASP', 9.98)], [('OD1', 'ASP', 'CB', 'ASP', 10.84), ('OD1', 'ASP', 'CG', 'ASP', 9.89), ('OD1', 'ASP', 'OD1', 'ASP', 9.77), ('OD1', 'ASP', 'OD2', 'ASP', 9.48)], [('OD2', 'ASP', 'CB', 'ASP', 12.65), ('OD2', 'ASP', 'CG', 'ASP', 11.54), ('OD2', 'ASP', 'OD1', 'ASP', 11.26), ('OD2', 'ASP', 'OD2', 'ASP', 11.07)]]}
GLU_ASP = { 
	'distances':
		[[6.97, 6.82, 5.82, 7.97], [7.86, 7.4, 6.22, 8.43], [7.55, 6.76, 5.49, 7.59], [6.39, 5.5, 4.23, 6.3], [8.62, 7.68, 6.41, 8.35], [10.3, 11.42, 11.29, 12.64], [10.07, 11.34, 11.4, 12.48], [8.88, 10.18, 10.31, 11.29], [8.57, 9.74, 9.74, 10.89], [8.45, 9.85, 10.17, 10.87]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ASP', 6.97), ('CB', 'GLU', 'CG', 'ASP', 6.82), ('CB', 'GLU', 'OD1', 'ASP', 5.82), ('CB', 'GLU', 'OD2', 'ASP', 7.97)], [('CG', 'GLU', 'CB', 'ASP', 7.86), ('CG', 'GLU', 'CG', 'ASP', 7.4), ('CG', 'GLU', 'OD1', 'ASP', 6.22), ('CG', 'GLU', 'OD2', 'ASP', 8.43)], [('CD', 'GLU', 'CB', 'ASP', 7.55), ('CD', 'GLU', 'CG', 'ASP', 6.76), ('CD', 'GLU', 'OD1', 'ASP', 5.49), ('CD', 'GLU', 'OD2', 'ASP', 7.59)], [('OE1', 'GLU', 'CB', 'ASP', 6.39), ('OE1', 'GLU', 'CG', 'ASP', 5.5), ('OE1', 'GLU', 'OD1', 'ASP', 4.23), ('OE1', 'GLU', 'OD2', 'ASP', 6.3)], [('OE2', 'GLU', 'CB', 'ASP', 8.62), ('OE2', 'GLU', 'CG', 'ASP', 7.68), ('OE2', 'GLU', 'OD1', 'ASP', 6.41), ('OE2', 'GLU', 'OD2', 'ASP', 8.35)], [('CB', 'GLU', 'CB', 'ASP', 10.3), ('CB', 'GLU', 'CG', 'ASP', 11.42), ('CB', 'GLU', 'OD1', 'ASP', 11.29), ('CB', 'GLU', 'OD2', 'ASP', 12.64)], [('CG', 'GLU', 'CB', 'ASP', 10.07), ('CG', 'GLU', 'CG', 'ASP', 11.34), ('CG', 'GLU', 'OD1', 'ASP', 11.4), ('CG', 'GLU', 'OD2', 'ASP', 12.48)], [('CD', 'GLU', 'CB', 'ASP', 8.88), ('CD', 'GLU', 'CG', 'ASP', 10.18), ('CD', 'GLU', 'OD1', 'ASP', 10.31), ('CD', 'GLU', 'OD2', 'ASP', 11.29)], [('OE1', 'GLU', 'CB', 'ASP', 8.57), ('OE1', 'GLU', 'CG', 'ASP', 9.74), ('OE1', 'GLU', 'OD1', 'ASP', 9.74), ('OE1', 'GLU', 'OD2', 'ASP', 10.89)], [('OE2', 'GLU', 'CB', 'ASP', 8.45), ('OE2', 'GLU', 'CG', 'ASP', 9.85), ('OE2', 'GLU', 'OD1', 'ASP', 10.17), ('OE2', 'GLU', 'OD2', 'ASP', 10.87)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_ASP, d, 'P_1dbr_2_4_2_22')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_LYS, d, 'P_1dbr_2_4_2_22')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ASP, d, 'P_1dbr_2_4_2_22')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ASP, d, 'P_1dbr_2_4_2_22')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_ASP' :  match1,
		'GLU_LYS' :  match2,
		'ASP_ASP' :  match3,
		'GLU_ASP' :  match4}