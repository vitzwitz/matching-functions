'''
FUNC:P_1aug_3_4_19_3
PDB:1aug
EC:3.4.19.3
RESI:glu,arg,cys,his
LOCI:a-81,91,144,168;
'''
import motifFunctions as cmd
GLU_CYS = { 
	'distances':
		[[10.54, 11.89, 9.79, 10.23, 11.07, 12.36], [9.46, 10.68, 9.26, 9.54, 10.19, 11.46], [9.72, 10.87, 9.96, 10.03, 10.61, 11.76], [10.61, 11.84, 10.69, 10.74, 11.43, 12.52], [9.28, 10.25, 10.03, 9.96, 10.34, 11.44]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYS', 10.54), ('CB', 'GLU', 'SG', 'CYS', 11.89), ('CB', 'GLU', 'O', 'CYS', 9.79), ('CB', 'GLU', 'C', 'CYS', 10.23), ('CB', 'GLU', 'CA', 'CYS', 11.07), ('CB', 'GLU', 'N', 'CYS', 12.36)], [('CG', 'GLU', 'CB', 'CYS', 9.46), ('CG', 'GLU', 'SG', 'CYS', 10.68), ('CG', 'GLU', 'O', 'CYS', 9.26), ('CG', 'GLU', 'C', 'CYS', 9.54), ('CG', 'GLU', 'CA', 'CYS', 10.19), ('CG', 'GLU', 'N', 'CYS', 11.46)], [('CD', 'GLU', 'CB', 'CYS', 9.72), ('CD', 'GLU', 'SG', 'CYS', 10.87), ('CD', 'GLU', 'O', 'CYS', 9.96), ('CD', 'GLU', 'C', 'CYS', 10.03), ('CD', 'GLU', 'CA', 'CYS', 10.61), ('CD', 'GLU', 'N', 'CYS', 11.76)], [('OE1', 'GLU', 'CB', 'CYS', 10.61), ('OE1', 'GLU', 'SG', 'CYS', 11.84), ('OE1', 'GLU', 'O', 'CYS', 10.69), ('OE1', 'GLU', 'C', 'CYS', 10.74), ('OE1', 'GLU', 'CA', 'CYS', 11.43), ('OE1', 'GLU', 'N', 'CYS', 12.52)], [('OE2', 'GLU', 'CB', 'CYS', 9.28), ('OE2', 'GLU', 'SG', 'CYS', 10.25), ('OE2', 'GLU', 'O', 'CYS', 10.03), ('OE2', 'GLU', 'C', 'CYS', 9.96), ('OE2', 'GLU', 'CA', 'CYS', 10.34), ('OE2', 'GLU', 'N', 'CYS', 11.44)]]}
ARG_HIS = { 
	'distances':
		[[18.46, 17.15, 16.44, 16.5, 15.33, 15.39], [16.93, 15.63, 14.9, 15.01, 13.81, 13.9], [16.02, 14.72, 14.09, 13.99, 12.96, 12.91], [14.57, 13.27, 12.63, 12.57, 11.52, 11.49], [13.62, 12.34, 11.82, 11.56, 10.7, 10.53], [14.04, 12.8, 12.42, 11.89, 11.29, 10.95], [12.32, 11.04, 10.49, 10.3, 9.39, 9.27]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'HIS', 18.46), ('CB', 'ARG', 'CG', 'HIS', 17.15), ('CB', 'ARG', 'ND1', 'HIS', 16.44), ('CB', 'ARG', 'CD2', 'HIS', 16.5), ('CB', 'ARG', 'CE1', 'HIS', 15.33), ('CB', 'ARG', 'NE2', 'HIS', 15.39)], [('CG', 'ARG', 'CB', 'HIS', 16.93), ('CG', 'ARG', 'CG', 'HIS', 15.63), ('CG', 'ARG', 'ND1', 'HIS', 14.9), ('CG', 'ARG', 'CD2', 'HIS', 15.01), ('CG', 'ARG', 'CE1', 'HIS', 13.81), ('CG', 'ARG', 'NE2', 'HIS', 13.9)], [('CD', 'ARG', 'CB', 'HIS', 16.02), ('CD', 'ARG', 'CG', 'HIS', 14.72), ('CD', 'ARG', 'ND1', 'HIS', 14.09), ('CD', 'ARG', 'CD2', 'HIS', 13.99), ('CD', 'ARG', 'CE1', 'HIS', 12.96), ('CD', 'ARG', 'NE2', 'HIS', 12.91)], [('NE', 'ARG', 'CB', 'HIS', 14.57), ('NE', 'ARG', 'CG', 'HIS', 13.27), ('NE', 'ARG', 'ND1', 'HIS', 12.63), ('NE', 'ARG', 'CD2', 'HIS', 12.57), ('NE', 'ARG', 'CE1', 'HIS', 11.52), ('NE', 'ARG', 'NE2', 'HIS', 11.49)], [('CZ', 'ARG', 'CB', 'HIS', 13.62), ('CZ', 'ARG', 'CG', 'HIS', 12.34), ('CZ', 'ARG', 'ND1', 'HIS', 11.82), ('CZ', 'ARG', 'CD2', 'HIS', 11.56), ('CZ', 'ARG', 'CE1', 'HIS', 10.7), ('CZ', 'ARG', 'NE2', 'HIS', 10.53)], [('NH1', 'ARG', 'CB', 'HIS', 14.04), ('NH1', 'ARG', 'CG', 'HIS', 12.8), ('NH1', 'ARG', 'ND1', 'HIS', 12.42), ('NH1', 'ARG', 'CD2', 'HIS', 11.89), ('NH1', 'ARG', 'CE1', 'HIS', 11.29), ('NH1', 'ARG', 'NE2', 'HIS', 10.95)], [('NH2', 'ARG', 'CB', 'HIS', 12.32), ('NH2', 'ARG', 'CG', 'HIS', 11.04), ('NH2', 'ARG', 'ND1', 'HIS', 10.49), ('NH2', 'ARG', 'CD2', 'HIS', 10.3), ('NH2', 'ARG', 'CE1', 'HIS', 9.39), ('NH2', 'ARG', 'NE2', 'HIS', 9.27)]]}
GLU_ARG = { 
	'distances':
		[[20.5, 18.99, 18.48, 17.06, 16.53, 17.35, 15.25], [19.45, 17.93, 17.34, 15.89, 15.3, 16.06, 13.99], [18.71, 17.18, 16.66, 15.2, 14.65, 15.47, 13.33], [18.89, 17.37, 16.96, 15.53, 15.08, 15.98, 13.78], [18.07, 16.53, 15.94, 14.48, 13.85, 14.63, 12.52]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 20.5), ('CB', 'GLU', 'CG', 'ARG', 18.99), ('CB', 'GLU', 'CD', 'ARG', 18.48), ('CB', 'GLU', 'NE', 'ARG', 17.06), ('CB', 'GLU', 'CZ', 'ARG', 16.53), ('CB', 'GLU', 'NH1', 'ARG', 17.35), ('CB', 'GLU', 'NH2', 'ARG', 15.25)], [('CG', 'GLU', 'CB', 'ARG', 19.45), ('CG', 'GLU', 'CG', 'ARG', 17.93), ('CG', 'GLU', 'CD', 'ARG', 17.34), ('CG', 'GLU', 'NE', 'ARG', 15.89), ('CG', 'GLU', 'CZ', 'ARG', 15.3), ('CG', 'GLU', 'NH1', 'ARG', 16.06), ('CG', 'GLU', 'NH2', 'ARG', 13.99)], [('CD', 'GLU', 'CB', 'ARG', 18.71), ('CD', 'GLU', 'CG', 'ARG', 17.18), ('CD', 'GLU', 'CD', 'ARG', 16.66), ('CD', 'GLU', 'NE', 'ARG', 15.2), ('CD', 'GLU', 'CZ', 'ARG', 14.65), ('CD', 'GLU', 'NH1', 'ARG', 15.47), ('CD', 'GLU', 'NH2', 'ARG', 13.33)], [('OE1', 'GLU', 'CB', 'ARG', 18.89), ('OE1', 'GLU', 'CG', 'ARG', 17.37), ('OE1', 'GLU', 'CD', 'ARG', 16.96), ('OE1', 'GLU', 'NE', 'ARG', 15.53), ('OE1', 'GLU', 'CZ', 'ARG', 15.08), ('OE1', 'GLU', 'NH1', 'ARG', 15.98), ('OE1', 'GLU', 'NH2', 'ARG', 13.78)], [('OE2', 'GLU', 'CB', 'ARG', 18.07), ('OE2', 'GLU', 'CG', 'ARG', 16.53), ('OE2', 'GLU', 'CD', 'ARG', 15.94), ('OE2', 'GLU', 'NE', 'ARG', 14.48), ('OE2', 'GLU', 'CZ', 'ARG', 13.85), ('OE2', 'GLU', 'NH1', 'ARG', 14.63), ('OE2', 'GLU', 'NH2', 'ARG', 12.52)]]}
ARG_CYS = { 
	'distances':
		[[14.52, 14.38, 16.46, 15.26, 14.8, 13.73], [13.17, 13.07, 15.18, 13.98, 13.53, 12.54], [12.15, 11.87, 14.4, 13.18, 12.57, 11.56], [10.92, 10.69, 13.26, 12.04, 11.45, 10.56], [10.11, 9.69, 12.73, 11.51, 10.76, 9.93], [10.49, 9.78, 13.25, 12.05, 11.13, 10.24], [9.11, 8.78, 11.82, 10.62, 9.91, 9.25]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'CYS', 14.52), ('CB', 'ARG', 'SG', 'CYS', 14.38), ('CB', 'ARG', 'O', 'CYS', 16.46), ('CB', 'ARG', 'C', 'CYS', 15.26), ('CB', 'ARG', 'CA', 'CYS', 14.8), ('CB', 'ARG', 'N', 'CYS', 13.73)], [('CG', 'ARG', 'CB', 'CYS', 13.17), ('CG', 'ARG', 'SG', 'CYS', 13.07), ('CG', 'ARG', 'O', 'CYS', 15.18), ('CG', 'ARG', 'C', 'CYS', 13.98), ('CG', 'ARG', 'CA', 'CYS', 13.53), ('CG', 'ARG', 'N', 'CYS', 12.54)], [('CD', 'ARG', 'CB', 'CYS', 12.15), ('CD', 'ARG', 'SG', 'CYS', 11.87), ('CD', 'ARG', 'O', 'CYS', 14.4), ('CD', 'ARG', 'C', 'CYS', 13.18), ('CD', 'ARG', 'CA', 'CYS', 12.57), ('CD', 'ARG', 'N', 'CYS', 11.56)], [('NE', 'ARG', 'CB', 'CYS', 10.92), ('NE', 'ARG', 'SG', 'CYS', 10.69), ('NE', 'ARG', 'O', 'CYS', 13.26), ('NE', 'ARG', 'C', 'CYS', 12.04), ('NE', 'ARG', 'CA', 'CYS', 11.45), ('NE', 'ARG', 'N', 'CYS', 10.56)], [('CZ', 'ARG', 'CB', 'CYS', 10.11), ('CZ', 'ARG', 'SG', 'CYS', 9.69), ('CZ', 'ARG', 'O', 'CYS', 12.73), ('CZ', 'ARG', 'C', 'CYS', 11.51), ('CZ', 'ARG', 'CA', 'CYS', 10.76), ('CZ', 'ARG', 'N', 'CYS', 9.93)], [('NH1', 'ARG', 'CB', 'CYS', 10.49), ('NH1', 'ARG', 'SG', 'CYS', 9.78), ('NH1', 'ARG', 'O', 'CYS', 13.25), ('NH1', 'ARG', 'C', 'CYS', 12.05), ('NH1', 'ARG', 'CA', 'CYS', 11.13), ('NH1', 'ARG', 'N', 'CYS', 10.24)], [('NH2', 'ARG', 'CB', 'CYS', 9.11), ('NH2', 'ARG', 'SG', 'CYS', 8.78), ('NH2', 'ARG', 'O', 'CYS', 11.82), ('NH2', 'ARG', 'C', 'CYS', 10.62), ('NH2', 'ARG', 'CA', 'CYS', 9.91), ('NH2', 'ARG', 'N', 'CYS', 9.25)]]}
GLU_HIS = { 
	'distances':
		[[8.25, 8.17, 7.6, 9.23, 8.4, 9.32], [6.8, 6.65, 6.09, 7.74, 6.97, 7.87], [6.61, 6.46, 5.72, 7.65, 6.67, 7.72], [7.69, 7.55, 6.72, 8.74, 7.59, 8.72], [5.66, 5.49, 4.79, 6.72, 5.86, 6.86]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'HIS', 8.25), ('CB', 'GLU', 'CG', 'HIS', 8.17), ('CB', 'GLU', 'ND1', 'HIS', 7.6), ('CB', 'GLU', 'CD2', 'HIS', 9.23), ('CB', 'GLU', 'CE1', 'HIS', 8.4), ('CB', 'GLU', 'NE2', 'HIS', 9.32)], [('CG', 'GLU', 'CB', 'HIS', 6.8), ('CG', 'GLU', 'CG', 'HIS', 6.65), ('CG', 'GLU', 'ND1', 'HIS', 6.09), ('CG', 'GLU', 'CD2', 'HIS', 7.74), ('CG', 'GLU', 'CE1', 'HIS', 6.97), ('CG', 'GLU', 'NE2', 'HIS', 7.87)], [('CD', 'GLU', 'CB', 'HIS', 6.61), ('CD', 'GLU', 'CG', 'HIS', 6.46), ('CD', 'GLU', 'ND1', 'HIS', 5.72), ('CD', 'GLU', 'CD2', 'HIS', 7.65), ('CD', 'GLU', 'CE1', 'HIS', 6.67), ('CD', 'GLU', 'NE2', 'HIS', 7.72)], [('OE1', 'GLU', 'CB', 'HIS', 7.69), ('OE1', 'GLU', 'CG', 'HIS', 7.55), ('OE1', 'GLU', 'ND1', 'HIS', 6.72), ('OE1', 'GLU', 'CD2', 'HIS', 8.74), ('OE1', 'GLU', 'CE1', 'HIS', 7.59), ('OE1', 'GLU', 'NE2', 'HIS', 8.72)], [('OE2', 'GLU', 'CB', 'HIS', 5.66), ('OE2', 'GLU', 'CG', 'HIS', 5.49), ('OE2', 'GLU', 'ND1', 'HIS', 4.79), ('OE2', 'GLU', 'CD2', 'HIS', 6.72), ('OE2', 'GLU', 'CE1', 'HIS', 5.86), ('OE2', 'GLU', 'NE2', 'HIS', 6.86)]]}
CYS_HIS = { 
	'distances':
		[[8.86, 7.41, 7.0, 6.59, 5.88, 5.56], [9.03, 7.69, 7.64, 6.54, 6.55, 5.73], [10.57, 9.29, 8.69, 8.93, 7.94, 8.11], [10.43, 9.04, 8.37, 8.56, 7.43, 7.57], [10.19, 8.78, 8.31, 8.03, 7.25, 7.05], [11.27, 9.81, 9.32, 8.97, 8.15, 7.9]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'HIS', 8.86), ('CB', 'CYS', 'CG', 'HIS', 7.41), ('CB', 'CYS', 'ND1', 'HIS', 7.0), ('CB', 'CYS', 'CD2', 'HIS', 6.59), ('CB', 'CYS', 'CE1', 'HIS', 5.88), ('CB', 'CYS', 'NE2', 'HIS', 5.56)], [('SG', 'CYS', 'CB', 'HIS', 9.03), ('SG', 'CYS', 'CG', 'HIS', 7.69), ('SG', 'CYS', 'ND1', 'HIS', 7.64), ('SG', 'CYS', 'CD2', 'HIS', 6.54), ('SG', 'CYS', 'CE1', 'HIS', 6.55), ('SG', 'CYS', 'NE2', 'HIS', 5.73)], [('O', 'CYS', 'CB', 'HIS', 10.57), ('O', 'CYS', 'CG', 'HIS', 9.29), ('O', 'CYS', 'ND1', 'HIS', 8.69), ('O', 'CYS', 'CD2', 'HIS', 8.93), ('O', 'CYS', 'CE1', 'HIS', 7.94), ('O', 'CYS', 'NE2', 'HIS', 8.11)], [('C', 'CYS', 'CB', 'HIS', 10.43), ('C', 'CYS', 'CG', 'HIS', 9.04), ('C', 'CYS', 'ND1', 'HIS', 8.37), ('C', 'CYS', 'CD2', 'HIS', 8.56), ('C', 'CYS', 'CE1', 'HIS', 7.43), ('C', 'CYS', 'NE2', 'HIS', 7.57)], [('CA', 'CYS', 'CB', 'HIS', 10.19), ('CA', 'CYS', 'CG', 'HIS', 8.78), ('CA', 'CYS', 'ND1', 'HIS', 8.31), ('CA', 'CYS', 'CD2', 'HIS', 8.03), ('CA', 'CYS', 'CE1', 'HIS', 7.25), ('CA', 'CYS', 'NE2', 'HIS', 7.05)], [('N', 'CYS', 'CB', 'HIS', 11.27), ('N', 'CYS', 'CG', 'HIS', 9.81), ('N', 'CYS', 'ND1', 'HIS', 9.32), ('N', 'CYS', 'CD2', 'HIS', 8.97), ('N', 'CYS', 'CE1', 'HIS', 8.15), ('N', 'CYS', 'NE2', 'HIS', 7.9)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_CYS, d, 'P_1aug_3_4_19_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_HIS, d, 'P_1aug_3_4_19_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_ARG, d, 'P_1aug_3_4_19_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ARG_CYS, d, 'P_1aug_3_4_19_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLU_HIS, d, 'P_1aug_3_4_19_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_HIS, d, 'P_1aug_3_4_19_3')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_CYS' :  match1,
		'ARG_HIS' :  match2,
		'GLU_ARG' :  match3,
		'ARG_CYS' :  match4,
		'GLU_HIS' :  match5,
		'CYS_HIS' :  match6}