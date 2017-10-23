'''
FUNC:M_13pk_2_7_2_3
PDB:13pk
EC:2.7.2.3
RESI:arg,lys,gly,gly,mg
LOCI:a-39,219,376,399,422;
'''
import motifFunctions as cmd
GLY_LYS = { 
	'distances':
		[[14.96, 13.97, 12.88, 11.95, 12.73], [13.76, 12.76, 11.65, 10.71, 11.5], [13.44, 12.4, 11.18, 10.16, 10.78], [12.56, 11.64, 10.32, 9.43, 10.1], [11.78, 12.11, 10.97, 11.45, 11.47], [11.22, 11.4, 10.16, 10.51, 10.54], [9.83, 10.02, 8.77, 9.22, 9.41], [9.94, 9.92, 8.53, 8.76, 9.08]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'LYS', 14.96), ('O', 'GLY', 'CG', 'LYS', 13.97), ('O', 'GLY', 'CD', 'LYS', 12.88), ('O', 'GLY', 'CE', 'LYS', 11.95), ('O', 'GLY', 'NZ', 'LYS', 12.73)], [('C', 'GLY', 'CB', 'LYS', 13.76), ('C', 'GLY', 'CG', 'LYS', 12.76), ('C', 'GLY', 'CD', 'LYS', 11.65), ('C', 'GLY', 'CE', 'LYS', 10.71), ('C', 'GLY', 'NZ', 'LYS', 11.5)], [('CA', 'GLY', 'CB', 'LYS', 13.44), ('CA', 'GLY', 'CG', 'LYS', 12.4), ('CA', 'GLY', 'CD', 'LYS', 11.18), ('CA', 'GLY', 'CE', 'LYS', 10.16), ('CA', 'GLY', 'NZ', 'LYS', 10.78)], [('N', 'GLY', 'CB', 'LYS', 12.56), ('N', 'GLY', 'CG', 'LYS', 11.64), ('N', 'GLY', 'CD', 'LYS', 10.32), ('N', 'GLY', 'CE', 'LYS', 9.43), ('N', 'GLY', 'NZ', 'LYS', 10.1)], [('O', 'GLY', 'CB', 'LYS', 11.78), ('O', 'GLY', 'CG', 'LYS', 12.11), ('O', 'GLY', 'CD', 'LYS', 10.97), ('O', 'GLY', 'CE', 'LYS', 11.45), ('O', 'GLY', 'NZ', 'LYS', 11.47)], [('C', 'GLY', 'CB', 'LYS', 11.22), ('C', 'GLY', 'CG', 'LYS', 11.4), ('C', 'GLY', 'CD', 'LYS', 10.16), ('C', 'GLY', 'CE', 'LYS', 10.51), ('C', 'GLY', 'NZ', 'LYS', 10.54)], [('CA', 'GLY', 'CB', 'LYS', 9.83), ('CA', 'GLY', 'CG', 'LYS', 10.02), ('CA', 'GLY', 'CD', 'LYS', 8.77), ('CA', 'GLY', 'CE', 'LYS', 9.22), ('CA', 'GLY', 'NZ', 'LYS', 9.41)], [('N', 'GLY', 'CB', 'LYS', 9.94), ('N', 'GLY', 'CG', 'LYS', 9.92), ('N', 'GLY', 'CD', 'LYS', 8.53), ('N', 'GLY', 'CE', 'LYS', 8.76), ('N', 'GLY', 'NZ', 'LYS', 9.08)]]}
ARG_MG = { 
	'distances':
		[[12.33], [11.39], [10.21], [9.65], [8.45], [7.57], [8.35]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 12.33)], [('CG', 'ARG', 'MG', 'MG', 11.39)], [('CD', 'ARG', 'MG', 'MG', 10.21)], [('NE', 'ARG', 'MG', 'MG', 9.65)], [('CZ', 'ARG', 'MG', 'MG', 8.45)], [('NH1', 'ARG', 'MG', 'MG', 7.57)], [('NH2', 'ARG', 'MG', 'MG', 8.35)]]}
ARG_LYS = { 
	'distances':
		[[17.94, 16.75, 15.47, 14.19, 14.07], [16.77, 15.66, 14.32, 13.11, 13.07], [15.48, 14.33, 13.02, 11.77, 11.65], [14.49, 13.43, 12.05, 10.9, 10.87], [13.18, 12.11, 10.74, 9.59, 9.6], [12.73, 11.54, 10.27, 8.98, 8.94], [12.46, 11.52, 10.07, 9.08, 9.2]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'LYS', 17.94), ('CB', 'ARG', 'CG', 'LYS', 16.75), ('CB', 'ARG', 'CD', 'LYS', 15.47), ('CB', 'ARG', 'CE', 'LYS', 14.19), ('CB', 'ARG', 'NZ', 'LYS', 14.07)], [('CG', 'ARG', 'CB', 'LYS', 16.77), ('CG', 'ARG', 'CG', 'LYS', 15.66), ('CG', 'ARG', 'CD', 'LYS', 14.32), ('CG', 'ARG', 'CE', 'LYS', 13.11), ('CG', 'ARG', 'NZ', 'LYS', 13.07)], [('CD', 'ARG', 'CB', 'LYS', 15.48), ('CD', 'ARG', 'CG', 'LYS', 14.33), ('CD', 'ARG', 'CD', 'LYS', 13.02), ('CD', 'ARG', 'CE', 'LYS', 11.77), ('CD', 'ARG', 'NZ', 'LYS', 11.65)], [('NE', 'ARG', 'CB', 'LYS', 14.49), ('NE', 'ARG', 'CG', 'LYS', 13.43), ('NE', 'ARG', 'CD', 'LYS', 12.05), ('NE', 'ARG', 'CE', 'LYS', 10.9), ('NE', 'ARG', 'NZ', 'LYS', 10.87)], [('CZ', 'ARG', 'CB', 'LYS', 13.18), ('CZ', 'ARG', 'CG', 'LYS', 12.11), ('CZ', 'ARG', 'CD', 'LYS', 10.74), ('CZ', 'ARG', 'CE', 'LYS', 9.59), ('CZ', 'ARG', 'NZ', 'LYS', 9.6)], [('NH1', 'ARG', 'CB', 'LYS', 12.73), ('NH1', 'ARG', 'CG', 'LYS', 11.54), ('NH1', 'ARG', 'CD', 'LYS', 10.27), ('NH1', 'ARG', 'CE', 'LYS', 8.98), ('NH1', 'ARG', 'NZ', 'LYS', 8.94)], [('NH2', 'ARG', 'CB', 'LYS', 12.46), ('NH2', 'ARG', 'CG', 'LYS', 11.52), ('NH2', 'ARG', 'CD', 'LYS', 10.07), ('NH2', 'ARG', 'CE', 'LYS', 9.08), ('NH2', 'ARG', 'NZ', 'LYS', 9.2)]]}
GLY_MG = { 
	'distances':
		[[8.83], [7.69], [7.54], [7.39], [13.92], [12.82], [11.58], [10.62]],
	'comparisons':
		[[('O', 'GLY', 'MG', 'MG', 8.83)], [('C', 'GLY', 'MG', 'MG', 7.69)], [('CA', 'GLY', 'MG', 'MG', 7.54)], [('N', 'GLY', 'MG', 'MG', 7.39)], [('O', 'GLY', 'MG', 'MG', 13.92)], [('C', 'GLY', 'MG', 'MG', 12.82)], [('CA', 'GLY', 'MG', 'MG', 11.58)], [('N', 'GLY', 'MG', 'MG', 10.62)]]}
GLY_ARG = { 
	'distances':
		[[9.41, 8.57, 8.51, 8.29, 8.09, 8.05, 8.29], [9.42, 8.44, 8.12, 7.73, 7.3, 7.18, 7.41], [8.32, 7.21, 6.75, 6.25, 5.8, 5.79, 5.96], [8.94, 7.64, 7.07, 6.16, 5.49, 5.75, 5.16], [16.53, 15.16, 14.39, 13.01, 12.33, 13.0, 11.13], [15.38, 14.01, 13.21, 11.82, 11.12, 11.78, 9.91], [15.22, 13.82, 12.93, 11.53, 10.67, 11.2, 9.44], [14.0, 12.57, 11.72, 10.3, 9.44, 10.02, 8.17]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ARG', 9.41), ('O', 'GLY', 'CG', 'ARG', 8.57), ('O', 'GLY', 'CD', 'ARG', 8.51), ('O', 'GLY', 'NE', 'ARG', 8.29), ('O', 'GLY', 'CZ', 'ARG', 8.09), ('O', 'GLY', 'NH1', 'ARG', 8.05), ('O', 'GLY', 'NH2', 'ARG', 8.29)], [('C', 'GLY', 'CB', 'ARG', 9.42), ('C', 'GLY', 'CG', 'ARG', 8.44), ('C', 'GLY', 'CD', 'ARG', 8.12), ('C', 'GLY', 'NE', 'ARG', 7.73), ('C', 'GLY', 'CZ', 'ARG', 7.3), ('C', 'GLY', 'NH1', 'ARG', 7.18), ('C', 'GLY', 'NH2', 'ARG', 7.41)], [('CA', 'GLY', 'CB', 'ARG', 8.32), ('CA', 'GLY', 'CG', 'ARG', 7.21), ('CA', 'GLY', 'CD', 'ARG', 6.75), ('CA', 'GLY', 'NE', 'ARG', 6.25), ('CA', 'GLY', 'CZ', 'ARG', 5.8), ('CA', 'GLY', 'NH1', 'ARG', 5.79), ('CA', 'GLY', 'NH2', 'ARG', 5.96)], [('N', 'GLY', 'CB', 'ARG', 8.94), ('N', 'GLY', 'CG', 'ARG', 7.64), ('N', 'GLY', 'CD', 'ARG', 7.07), ('N', 'GLY', 'NE', 'ARG', 6.16), ('N', 'GLY', 'CZ', 'ARG', 5.49), ('N', 'GLY', 'NH1', 'ARG', 5.75), ('N', 'GLY', 'NH2', 'ARG', 5.16)], [('O', 'GLY', 'CB', 'ARG', 16.53), ('O', 'GLY', 'CG', 'ARG', 15.16), ('O', 'GLY', 'CD', 'ARG', 14.39), ('O', 'GLY', 'NE', 'ARG', 13.01), ('O', 'GLY', 'CZ', 'ARG', 12.33), ('O', 'GLY', 'NH1', 'ARG', 13.0), ('O', 'GLY', 'NH2', 'ARG', 11.13)], [('C', 'GLY', 'CB', 'ARG', 15.38), ('C', 'GLY', 'CG', 'ARG', 14.01), ('C', 'GLY', 'CD', 'ARG', 13.21), ('C', 'GLY', 'NE', 'ARG', 11.82), ('C', 'GLY', 'CZ', 'ARG', 11.12), ('C', 'GLY', 'NH1', 'ARG', 11.78), ('C', 'GLY', 'NH2', 'ARG', 9.91)], [('CA', 'GLY', 'CB', 'ARG', 15.22), ('CA', 'GLY', 'CG', 'ARG', 13.82), ('CA', 'GLY', 'CD', 'ARG', 12.93), ('CA', 'GLY', 'NE', 'ARG', 11.53), ('CA', 'GLY', 'CZ', 'ARG', 10.67), ('CA', 'GLY', 'NH1', 'ARG', 11.2), ('CA', 'GLY', 'NH2', 'ARG', 9.44)], [('N', 'GLY', 'CB', 'ARG', 14.0), ('N', 'GLY', 'CG', 'ARG', 12.57), ('N', 'GLY', 'CD', 'ARG', 11.72), ('N', 'GLY', 'NE', 'ARG', 10.3), ('N', 'GLY', 'CZ', 'ARG', 9.44), ('N', 'GLY', 'NH1', 'ARG', 10.02), ('N', 'GLY', 'NH2', 'ARG', 8.17)]]}
MG_GLYI = { 
	'distances':
		[13.92, 12.82, 11.58, 10.62],
	'comparisons':
		[('MG', 'MG', 'O', 'GLYI', 13.92), ('MG', 'MG', 'C', 'GLYI', 12.82), ('MG', 'MG', 'CA', 'GLYI', 11.58), ('MG', 'MG', 'N', 'GLYI', 10.62)]}
GLY_GLY = { 
	'distances':
		[[16.11, 14.96, 14.13, 12.71], [15.14, 13.97, 13.09, 11.69], [14.17, 12.97, 12.19, 10.79], [12.76, 11.58, 10.79, 9.38], [16.11, 15.14, 14.17, 12.76], [14.96, 13.97, 12.97, 11.58], [14.13, 13.09, 12.19, 10.79], [12.71, 11.69, 10.79, 9.38]],
	'comparisons':
		[[('O', 'GLY', 'O', 'GLY', 16.11), ('O', 'GLY', 'C', 'GLY', 14.96), ('O', 'GLY', 'CA', 'GLY', 14.13), ('O', 'GLY', 'N', 'GLY', 12.71)], [('C', 'GLY', 'O', 'GLY', 15.14), ('C', 'GLY', 'C', 'GLY', 13.97), ('C', 'GLY', 'CA', 'GLY', 13.09), ('C', 'GLY', 'N', 'GLY', 11.69)], [('CA', 'GLY', 'O', 'GLY', 14.17), ('CA', 'GLY', 'C', 'GLY', 12.97), ('CA', 'GLY', 'CA', 'GLY', 12.19), ('CA', 'GLY', 'N', 'GLY', 10.79)], [('N', 'GLY', 'O', 'GLY', 12.76), ('N', 'GLY', 'C', 'GLY', 11.58), ('N', 'GLY', 'CA', 'GLY', 10.79), ('N', 'GLY', 'N', 'GLY', 9.38)], [('O', 'GLY', 'O', 'GLY', 16.11), ('O', 'GLY', 'C', 'GLY', 15.14), ('O', 'GLY', 'CA', 'GLY', 14.17), ('O', 'GLY', 'N', 'GLY', 12.76)], [('C', 'GLY', 'O', 'GLY', 14.96), ('C', 'GLY', 'C', 'GLY', 13.97), ('C', 'GLY', 'CA', 'GLY', 12.97), ('C', 'GLY', 'N', 'GLY', 11.58)], [('CA', 'GLY', 'O', 'GLY', 14.13), ('CA', 'GLY', 'C', 'GLY', 13.09), ('CA', 'GLY', 'CA', 'GLY', 12.19), ('CA', 'GLY', 'N', 'GLY', 10.79)], [('N', 'GLY', 'O', 'GLY', 12.71), ('N', 'GLY', 'C', 'GLY', 11.69), ('N', 'GLY', 'CA', 'GLY', 10.79), ('N', 'GLY', 'N', 'GLY', 9.38)]]}
LYS_MG = { 
	'distances':
		[[8.96], [7.66], [6.95], [5.83], [6.69]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 8.96)], [('CG', 'LYS', 'MG', 'MG', 7.66)], [('CD', 'LYS', 'MG', 'MG', 6.95)], [('CE', 'LYS', 'MG', 'MG', 5.83)], [('NZ', 'LYS', 'MG', 'MG', 6.69)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_LYS, d, 'M_13pk_2_7_2_3')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_MG, d, 'M_13pk_2_7_2_3')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_LYS, d, 'M_13pk_2_7_2_3')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_MG, d, 'M_13pk_2_7_2_3')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_ARG, d, 'M_13pk_2_7_2_3')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(MG_GLYI, d, 'M_13pk_2_7_2_3')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_GLY, d, 'M_13pk_2_7_2_3')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(LYS_MG, d, 'M_13pk_2_7_2_3')
	if match8 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_LYS' :  match1,
		'ARG_MG' :  match2,
		'ARG_LYS' :  match3,
		'GLY_MG' :  match4,
		'GLY_ARG' :  match5,
		'MG_GLYI' :  match6,
		'GLY_GLY' :  match7,
		'LYS_MG' :  match8}