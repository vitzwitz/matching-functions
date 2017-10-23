'''
FUNC:A_1nba_3_5_1_59
PDB:1nba
EC:3.5.1.59
RESI:asp,lys,ala,thr,cys
LOCI:a-51,144,172,173,177;
'''
import motifFunctions as cmd
ALA_THR = { 
	'distances':
		[[6.58, 7.61, 6.05, 7.64, 7.01, 5.77, 5.37], [6.54, 6.8, 6.72, 6.07, 6.2, 5.48, 4.13], [5.61, 6.15, 5.81, 5.55, 5.35, 4.44, 3.32], [6.27, 7.18, 6.27, 6.43, 5.96, 5.04, 4.55], [7.66, 8.49, 7.72, 7.2, 6.94, 6.32, 5.72]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'THR', 6.58), ('CB', 'ALA', 'OG1', 'THR', 7.61), ('CB', 'ALA', 'CG2', 'THR', 6.05), ('CB', 'ALA', 'O', 'THR', 7.64), ('CB', 'ALA', 'C', 'THR', 7.01), ('CB', 'ALA', 'CA', 'THR', 5.77), ('CB', 'ALA', 'N', 'THR', 5.37)], [('O', 'ALA', 'CB', 'THR', 6.54), ('O', 'ALA', 'OG1', 'THR', 6.8), ('O', 'ALA', 'CG2', 'THR', 6.72), ('O', 'ALA', 'O', 'THR', 6.07), ('O', 'ALA', 'C', 'THR', 6.2), ('O', 'ALA', 'CA', 'THR', 5.48), ('O', 'ALA', 'N', 'THR', 4.13)], [('C', 'ALA', 'CB', 'THR', 5.61), ('C', 'ALA', 'OG1', 'THR', 6.15), ('C', 'ALA', 'CG2', 'THR', 5.81), ('C', 'ALA', 'O', 'THR', 5.55), ('C', 'ALA', 'C', 'THR', 5.35), ('C', 'ALA', 'CA', 'THR', 4.44), ('C', 'ALA', 'N', 'THR', 3.32)], [('CA', 'ALA', 'CB', 'THR', 6.27), ('CA', 'ALA', 'OG1', 'THR', 7.18), ('CA', 'ALA', 'CG2', 'THR', 6.27), ('CA', 'ALA', 'O', 'THR', 6.43), ('CA', 'ALA', 'C', 'THR', 5.96), ('CA', 'ALA', 'CA', 'THR', 5.04), ('CA', 'ALA', 'N', 'THR', 4.55)], [('N', 'ALA', 'CB', 'THR', 7.66), ('N', 'ALA', 'OG1', 'THR', 8.49), ('N', 'ALA', 'CG2', 'THR', 7.72), ('N', 'ALA', 'O', 'THR', 7.2), ('N', 'ALA', 'C', 'THR', 6.94), ('N', 'ALA', 'CA', 'THR', 6.32), ('N', 'ALA', 'N', 'THR', 5.72)]]}
THR_ASP = { 
	'distances':
		[[9.97, 10.46, 11.66, 9.79], [10.18, 10.41, 11.58, 9.58], [9.53, 10.15, 11.39, 9.56], [10.09, 10.34, 11.34, 9.72], [10.22, 10.66, 11.73, 10.09], [9.26, 9.83, 10.98, 9.3], [7.94, 8.41, 9.55, 7.87]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ASP', 9.97), ('CB', 'THR', 'CG', 'ASP', 10.46), ('CB', 'THR', 'OD1', 'ASP', 11.66), ('CB', 'THR', 'OD2', 'ASP', 9.79)], [('OG1', 'THR', 'CB', 'ASP', 10.18), ('OG1', 'THR', 'CG', 'ASP', 10.41), ('OG1', 'THR', 'OD1', 'ASP', 11.58), ('OG1', 'THR', 'OD2', 'ASP', 9.58)], [('CG2', 'THR', 'CB', 'ASP', 9.53), ('CG2', 'THR', 'CG', 'ASP', 10.15), ('CG2', 'THR', 'OD1', 'ASP', 11.39), ('CG2', 'THR', 'OD2', 'ASP', 9.56)], [('O', 'THR', 'CB', 'ASP', 10.09), ('O', 'THR', 'CG', 'ASP', 10.34), ('O', 'THR', 'OD1', 'ASP', 11.34), ('O', 'THR', 'OD2', 'ASP', 9.72)], [('C', 'THR', 'CB', 'ASP', 10.22), ('C', 'THR', 'CG', 'ASP', 10.66), ('C', 'THR', 'OD1', 'ASP', 11.73), ('C', 'THR', 'OD2', 'ASP', 10.09)], [('CA', 'THR', 'CB', 'ASP', 9.26), ('CA', 'THR', 'CG', 'ASP', 9.83), ('CA', 'THR', 'OD1', 'ASP', 10.98), ('CA', 'THR', 'OD2', 'ASP', 9.3)], [('N', 'THR', 'CB', 'ASP', 7.94), ('N', 'THR', 'CG', 'ASP', 8.41), ('N', 'THR', 'OD1', 'ASP', 9.55), ('N', 'THR', 'OD2', 'ASP', 7.87)]]}
ALA_ASP = { 
	'distances':
		[[7.1, 8.29, 9.38, 8.31], [6.06, 6.56, 7.63, 6.26], [6.96, 7.63, 8.74, 7.32], [7.32, 8.31, 9.36, 8.26], [7.11, 8.17, 9.06, 8.36]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'ASP', 7.1), ('CB', 'ALA', 'CG', 'ASP', 8.29), ('CB', 'ALA', 'OD1', 'ASP', 9.38), ('CB', 'ALA', 'OD2', 'ASP', 8.31)], [('O', 'ALA', 'CB', 'ASP', 6.06), ('O', 'ALA', 'CG', 'ASP', 6.56), ('O', 'ALA', 'OD1', 'ASP', 7.63), ('O', 'ALA', 'OD2', 'ASP', 6.26)], [('C', 'ALA', 'CB', 'ASP', 6.96), ('C', 'ALA', 'CG', 'ASP', 7.63), ('C', 'ALA', 'OD1', 'ASP', 8.74), ('C', 'ALA', 'OD2', 'ASP', 7.32)], [('CA', 'ALA', 'CB', 'ASP', 7.32), ('CA', 'ALA', 'CG', 'ASP', 8.31), ('CA', 'ALA', 'OD1', 'ASP', 9.36), ('CA', 'ALA', 'OD2', 'ASP', 8.26)], [('N', 'ALA', 'CB', 'ASP', 7.11), ('N', 'ALA', 'CG', 'ASP', 8.17), ('N', 'ALA', 'OD1', 'ASP', 9.06), ('N', 'ALA', 'OD2', 'ASP', 8.36)]]}
ALA_CYS = { 
	'distances':
		[[8.78, 9.41], [5.65, 6.58], [6.49, 7.39], [7.9, 8.86], [8.23, 9.36]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'CYS', 8.78), ('CB', 'ALA', 'SG', 'CYS', 9.41)], [('O', 'ALA', 'CB', 'CYS', 5.65), ('O', 'ALA', 'SG', 'CYS', 6.58)], [('C', 'ALA', 'CB', 'CYS', 6.49), ('C', 'ALA', 'SG', 'CYS', 7.39)], [('CA', 'ALA', 'CB', 'CYS', 7.9), ('CA', 'ALA', 'SG', 'CYS', 8.86)], [('N', 'ALA', 'CB', 'CYS', 8.23), ('N', 'ALA', 'SG', 'CYS', 9.36)]]}
CYS_LYS = { 
	'distances':
		[[10.28, 8.98, 7.89, 6.58, 6.0], [9.71, 8.36, 7.59, 6.3, 5.23]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'LYS', 10.28), ('CB', 'CYS', 'CG', 'LYS', 8.98), ('CB', 'CYS', 'CD', 'LYS', 7.89), ('CB', 'CYS', 'CE', 'LYS', 6.58), ('CB', 'CYS', 'NZ', 'LYS', 6.0)], [('SG', 'CYS', 'CB', 'LYS', 9.71), ('SG', 'CYS', 'CG', 'LYS', 8.36), ('SG', 'CYS', 'CD', 'LYS', 7.59), ('SG', 'CYS', 'CE', 'LYS', 6.3), ('SG', 'CYS', 'NZ', 'LYS', 5.23)]]}
THR_LYS = { 
	'distances':
		[[15.93, 14.46, 13.65, 12.17, 11.47], [15.34, 13.91, 13.1, 11.66, 10.83], [15.99, 14.49, 13.82, 12.31, 11.61], [14.9, 13.59, 12.45, 11.1, 10.64], [15.71, 14.34, 13.28, 11.86, 11.39], [15.38, 13.93, 13.01, 11.53, 11.02], [13.96, 12.51, 11.6, 10.11, 9.65]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 15.93), ('CB', 'THR', 'CG', 'LYS', 14.46), ('CB', 'THR', 'CD', 'LYS', 13.65), ('CB', 'THR', 'CE', 'LYS', 12.17), ('CB', 'THR', 'NZ', 'LYS', 11.47)], [('OG1', 'THR', 'CB', 'LYS', 15.34), ('OG1', 'THR', 'CG', 'LYS', 13.91), ('OG1', 'THR', 'CD', 'LYS', 13.1), ('OG1', 'THR', 'CE', 'LYS', 11.66), ('OG1', 'THR', 'NZ', 'LYS', 10.83)], [('CG2', 'THR', 'CB', 'LYS', 15.99), ('CG2', 'THR', 'CG', 'LYS', 14.49), ('CG2', 'THR', 'CD', 'LYS', 13.82), ('CG2', 'THR', 'CE', 'LYS', 12.31), ('CG2', 'THR', 'NZ', 'LYS', 11.61)], [('O', 'THR', 'CB', 'LYS', 14.9), ('O', 'THR', 'CG', 'LYS', 13.59), ('O', 'THR', 'CD', 'LYS', 12.45), ('O', 'THR', 'CE', 'LYS', 11.1), ('O', 'THR', 'NZ', 'LYS', 10.64)], [('C', 'THR', 'CB', 'LYS', 15.71), ('C', 'THR', 'CG', 'LYS', 14.34), ('C', 'THR', 'CD', 'LYS', 13.28), ('C', 'THR', 'CE', 'LYS', 11.86), ('C', 'THR', 'NZ', 'LYS', 11.39)], [('CA', 'THR', 'CB', 'LYS', 15.38), ('CA', 'THR', 'CG', 'LYS', 13.93), ('CA', 'THR', 'CD', 'LYS', 13.01), ('CA', 'THR', 'CE', 'LYS', 11.53), ('CA', 'THR', 'NZ', 'LYS', 11.02)], [('N', 'THR', 'CB', 'LYS', 13.96), ('N', 'THR', 'CG', 'LYS', 12.51), ('N', 'THR', 'CD', 'LYS', 11.6), ('N', 'THR', 'CE', 'LYS', 10.11), ('N', 'THR', 'NZ', 'LYS', 9.65)]]}
ALA_LYS = { 
	'distances':
		[[14.87, 13.39, 12.69, 11.21, 11.07], [12.33, 10.89, 9.98, 8.5, 8.31], [13.53, 12.08, 11.18, 9.69, 9.43], [14.52, 13.08, 12.2, 10.73, 10.64], [14.24, 12.87, 11.93, 10.55, 10.7]],
	'comparisons':
		[[('CB', 'ALA', 'CB', 'LYS', 14.87), ('CB', 'ALA', 'CG', 'LYS', 13.39), ('CB', 'ALA', 'CD', 'LYS', 12.69), ('CB', 'ALA', 'CE', 'LYS', 11.21), ('CB', 'ALA', 'NZ', 'LYS', 11.07)], [('O', 'ALA', 'CB', 'LYS', 12.33), ('O', 'ALA', 'CG', 'LYS', 10.89), ('O', 'ALA', 'CD', 'LYS', 9.98), ('O', 'ALA', 'CE', 'LYS', 8.5), ('O', 'ALA', 'NZ', 'LYS', 8.31)], [('C', 'ALA', 'CB', 'LYS', 13.53), ('C', 'ALA', 'CG', 'LYS', 12.08), ('C', 'ALA', 'CD', 'LYS', 11.18), ('C', 'ALA', 'CE', 'LYS', 9.69), ('C', 'ALA', 'NZ', 'LYS', 9.43)], [('CA', 'ALA', 'CB', 'LYS', 14.52), ('CA', 'ALA', 'CG', 'LYS', 13.08), ('CA', 'ALA', 'CD', 'LYS', 12.2), ('CA', 'ALA', 'CE', 'LYS', 10.73), ('CA', 'ALA', 'NZ', 'LYS', 10.64)], [('N', 'ALA', 'CB', 'LYS', 14.24), ('N', 'ALA', 'CG', 'LYS', 12.87), ('N', 'ALA', 'CD', 'LYS', 11.93), ('N', 'ALA', 'CE', 'LYS', 10.55), ('N', 'ALA', 'NZ', 'LYS', 10.7)]]}
ASP_LYS = { 
	'distances':
		[[10.27, 8.84, 8.46, 7.18, 7.42], [8.82, 7.36, 7.03, 5.76, 5.99], [7.93, 6.55, 6.36, 5.35, 5.94], [8.77, 7.24, 6.86, 5.45, 5.24]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 10.27), ('CB', 'ASP', 'CG', 'LYS', 8.84), ('CB', 'ASP', 'CD', 'LYS', 8.46), ('CB', 'ASP', 'CE', 'LYS', 7.18), ('CB', 'ASP', 'NZ', 'LYS', 7.42)], [('CG', 'ASP', 'CB', 'LYS', 8.82), ('CG', 'ASP', 'CG', 'LYS', 7.36), ('CG', 'ASP', 'CD', 'LYS', 7.03), ('CG', 'ASP', 'CE', 'LYS', 5.76), ('CG', 'ASP', 'NZ', 'LYS', 5.99)], [('OD1', 'ASP', 'CB', 'LYS', 7.93), ('OD1', 'ASP', 'CG', 'LYS', 6.55), ('OD1', 'ASP', 'CD', 'LYS', 6.36), ('OD1', 'ASP', 'CE', 'LYS', 5.35), ('OD1', 'ASP', 'NZ', 'LYS', 5.94)], [('OD2', 'ASP', 'CB', 'LYS', 8.77), ('OD2', 'ASP', 'CG', 'LYS', 7.24), ('OD2', 'ASP', 'CD', 'LYS', 6.86), ('OD2', 'ASP', 'CE', 'LYS', 5.45), ('OD2', 'ASP', 'NZ', 'LYS', 5.24)]]}
CYS_ASP = { 
	'distances':
		[[7.67, 7.07, 7.78, 6.19], [7.74, 6.88, 7.6, 5.74]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 7.67), ('CB', 'CYS', 'CG', 'ASP', 7.07), ('CB', 'CYS', 'OD1', 'ASP', 7.78), ('CB', 'CYS', 'OD2', 'ASP', 6.19)], [('SG', 'CYS', 'CB', 'ASP', 7.74), ('SG', 'CYS', 'CG', 'ASP', 6.88), ('SG', 'CYS', 'OD1', 'ASP', 7.6), ('SG', 'CYS', 'OD2', 'ASP', 5.74)]]}
THR_CYS = { 
	'distances':
		[[8.16, 8.58], [7.5, 7.74], [8.76, 8.92], [6.69, 7.91], [7.57, 8.62], [7.54, 8.33], [6.33, 7.13]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'CYS', 8.16), ('CB', 'THR', 'SG', 'CYS', 8.58)], [('OG1', 'THR', 'CB', 'CYS', 7.5), ('OG1', 'THR', 'SG', 'CYS', 7.74)], [('CG2', 'THR', 'CB', 'CYS', 8.76), ('CG2', 'THR', 'SG', 'CYS', 8.92)], [('O', 'THR', 'CB', 'CYS', 6.69), ('O', 'THR', 'SG', 'CYS', 7.91)], [('C', 'THR', 'CB', 'CYS', 7.57), ('C', 'THR', 'SG', 'CYS', 8.62)], [('CA', 'THR', 'CB', 'CYS', 7.54), ('CA', 'THR', 'SG', 'CYS', 8.33)], [('N', 'THR', 'CB', 'CYS', 6.33), ('N', 'THR', 'SG', 'CYS', 7.13)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ALA_THR, d, 'A_1nba_3_5_1_59')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(THR_ASP, d, 'A_1nba_3_5_1_59')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ALA_ASP, d, 'A_1nba_3_5_1_59')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ALA_CYS, d, 'A_1nba_3_5_1_59')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(CYS_LYS, d, 'A_1nba_3_5_1_59')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_LYS, d, 'A_1nba_3_5_1_59')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ALA_LYS, d, 'A_1nba_3_5_1_59')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_LYS, d, 'A_1nba_3_5_1_59')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(CYS_ASP, d, 'A_1nba_3_5_1_59')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(THR_CYS, d, 'A_1nba_3_5_1_59')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ALA_THR' :  match1,
		'THR_ASP' :  match2,
		'ALA_ASP' :  match3,
		'ALA_CYS' :  match4,
		'CYS_LYS' :  match5,
		'THR_LYS' :  match6,
		'ALA_LYS' :  match7,
		'ASP_LYS' :  match8,
		'CYS_ASP' :  match9,
		'THR_CYS' :  match10}