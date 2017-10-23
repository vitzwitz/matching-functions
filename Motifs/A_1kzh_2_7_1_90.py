'''
FUNC:A_1kzh_2_7_1_90
PDB:1kzh
EC:2.7.1.90
RESI:gly,arg,lys,thr,asp
LOCI:a-82,146,203,204,206;
'''
import motifFunctions as cmd
THR_ARG = { 
	'distances':
		[[14.49, 13.46, 13.55, 12.68, 11.38, 10.81, 10.82], [14.26, 13.17, 13.07, 12.12, 10.8, 10.3, 10.14], [15.63, 14.69, 14.78, 13.98, 12.67, 12.0, 12.17]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'ARG', 14.49), ('CB', 'THR', 'CG', 'ARG', 13.46), ('CB', 'THR', 'CD', 'ARG', 13.55), ('CB', 'THR', 'NE', 'ARG', 12.68), ('CB', 'THR', 'CZ', 'ARG', 11.38), ('CB', 'THR', 'NH1', 'ARG', 10.81), ('CB', 'THR', 'NH2', 'ARG', 10.82)], [('OG1', 'THR', 'CB', 'ARG', 14.26), ('OG1', 'THR', 'CG', 'ARG', 13.17), ('OG1', 'THR', 'CD', 'ARG', 13.07), ('OG1', 'THR', 'NE', 'ARG', 12.12), ('OG1', 'THR', 'CZ', 'ARG', 10.8), ('OG1', 'THR', 'NH1', 'ARG', 10.3), ('OG1', 'THR', 'NH2', 'ARG', 10.14)], [('CG2', 'THR', 'CB', 'ARG', 15.63), ('CG2', 'THR', 'CG', 'ARG', 14.69), ('CG2', 'THR', 'CD', 'ARG', 14.78), ('CG2', 'THR', 'NE', 'ARG', 13.98), ('CG2', 'THR', 'CZ', 'ARG', 12.67), ('CG2', 'THR', 'NH1', 'ARG', 12.0), ('CG2', 'THR', 'NH2', 'ARG', 12.17)]]}
ASP_THR = { 
	'distances':
		[[6.64, 5.43, 6.68], [6.76, 5.35, 7.25], [7.54, 6.13, 8.16], [6.52, 5.15, 7.14]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 6.64), ('CB', 'ASP', 'OG1', 'THR', 5.43), ('CB', 'ASP', 'CG2', 'THR', 6.68)], [('CG', 'ASP', 'CB', 'THR', 6.76), ('CG', 'ASP', 'OG1', 'THR', 5.35), ('CG', 'ASP', 'CG2', 'THR', 7.25)], [('OD1', 'ASP', 'CB', 'THR', 7.54), ('OD1', 'ASP', 'OG1', 'THR', 6.13), ('OD1', 'ASP', 'CG2', 'THR', 8.16)], [('OD2', 'ASP', 'CB', 'THR', 6.52), ('OD2', 'ASP', 'OG1', 'THR', 5.15), ('OD2', 'ASP', 'CG2', 'THR', 7.14)]]}
ASP_ARG = { 
	'distances':
		[[16.07, 14.98, 14.52, 13.52, 12.23, 11.83, 11.49], [14.9, 13.76, 13.22, 12.17, 10.9, 10.6, 10.1], [15.19, 13.97, 13.36, 12.2, 10.98, 10.87, 10.05], [13.76, 12.68, 12.17, 11.18, 9.9, 9.5, 9.21]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 16.07), ('CB', 'ASP', 'CG', 'ARG', 14.98), ('CB', 'ASP', 'CD', 'ARG', 14.52), ('CB', 'ASP', 'NE', 'ARG', 13.52), ('CB', 'ASP', 'CZ', 'ARG', 12.23), ('CB', 'ASP', 'NH1', 'ARG', 11.83), ('CB', 'ASP', 'NH2', 'ARG', 11.49)], [('CG', 'ASP', 'CB', 'ARG', 14.9), ('CG', 'ASP', 'CG', 'ARG', 13.76), ('CG', 'ASP', 'CD', 'ARG', 13.22), ('CG', 'ASP', 'NE', 'ARG', 12.17), ('CG', 'ASP', 'CZ', 'ARG', 10.9), ('CG', 'ASP', 'NH1', 'ARG', 10.6), ('CG', 'ASP', 'NH2', 'ARG', 10.1)], [('OD1', 'ASP', 'CB', 'ARG', 15.19), ('OD1', 'ASP', 'CG', 'ARG', 13.97), ('OD1', 'ASP', 'CD', 'ARG', 13.36), ('OD1', 'ASP', 'NE', 'ARG', 12.2), ('OD1', 'ASP', 'CZ', 'ARG', 10.98), ('OD1', 'ASP', 'NH1', 'ARG', 10.87), ('OD1', 'ASP', 'NH2', 'ARG', 10.05)], [('OD2', 'ASP', 'CB', 'ARG', 13.76), ('OD2', 'ASP', 'CG', 'ARG', 12.68), ('OD2', 'ASP', 'CD', 'ARG', 12.17), ('OD2', 'ASP', 'NE', 'ARG', 11.18), ('OD2', 'ASP', 'CZ', 'ARG', 9.9), ('OD2', 'ASP', 'NH1', 'ARG', 9.5), ('OD2', 'ASP', 'NH2', 'ARG', 9.21)]]}
GLY_LYS = { 
	'distances':
		[[8.0, 6.79, 5.59, 5.47, 4.81], [9.21, 7.96, 6.81, 6.66, 5.89], [10.26, 9.14, 7.85, 7.46, 6.36], [10.0, 9.09, 7.76, 7.02, 5.77]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'LYS', 8.0), ('O', 'GLY', 'CG', 'LYS', 6.79), ('O', 'GLY', 'CD', 'LYS', 5.59), ('O', 'GLY', 'CE', 'LYS', 5.47), ('O', 'GLY', 'NZ', 'LYS', 4.81)], [('C', 'GLY', 'CB', 'LYS', 9.21), ('C', 'GLY', 'CG', 'LYS', 7.96), ('C', 'GLY', 'CD', 'LYS', 6.81), ('C', 'GLY', 'CE', 'LYS', 6.66), ('C', 'GLY', 'NZ', 'LYS', 5.89)], [('CA', 'GLY', 'CB', 'LYS', 10.26), ('CA', 'GLY', 'CG', 'LYS', 9.14), ('CA', 'GLY', 'CD', 'LYS', 7.85), ('CA', 'GLY', 'CE', 'LYS', 7.46), ('CA', 'GLY', 'NZ', 'LYS', 6.36)], [('N', 'GLY', 'CB', 'LYS', 10.0), ('N', 'GLY', 'CG', 'LYS', 9.09), ('N', 'GLY', 'CD', 'LYS', 7.76), ('N', 'GLY', 'CE', 'LYS', 7.02), ('N', 'GLY', 'NZ', 'LYS', 5.77)]]}
THR_GLY = { 
	'distances':
		[[8.5, 9.51, 9.97, 9.79], [8.57, 9.41, 9.69, 9.61], [9.98, 11.01, 11.48, 11.24]],
	'comparisons':
		[[('CB', 'THR', 'O', 'GLY', 8.5), ('CB', 'THR', 'C', 'GLY', 9.51), ('CB', 'THR', 'CA', 'GLY', 9.97), ('CB', 'THR', 'N', 'GLY', 9.79)], [('OG1', 'THR', 'O', 'GLY', 8.57), ('OG1', 'THR', 'C', 'GLY', 9.41), ('OG1', 'THR', 'CA', 'GLY', 9.69), ('OG1', 'THR', 'N', 'GLY', 9.61)], [('CG2', 'THR', 'O', 'GLY', 9.98), ('CG2', 'THR', 'C', 'GLY', 11.01), ('CG2', 'THR', 'CA', 'GLY', 11.48), ('CG2', 'THR', 'N', 'GLY', 11.24)]]}
THR_LYS = { 
	'distances':
		[[7.3, 7.27, 6.46, 7.0, 6.91], [8.54, 8.3, 7.28, 7.77, 7.34], [7.86, 8.15, 7.61, 8.14, 8.21]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 7.3), ('CB', 'THR', 'CG', 'LYS', 7.27), ('CB', 'THR', 'CD', 'LYS', 6.46), ('CB', 'THR', 'CE', 'LYS', 7.0), ('CB', 'THR', 'NZ', 'LYS', 6.91)], [('OG1', 'THR', 'CB', 'LYS', 8.54), ('OG1', 'THR', 'CG', 'LYS', 8.3), ('OG1', 'THR', 'CD', 'LYS', 7.28), ('OG1', 'THR', 'CE', 'LYS', 7.77), ('OG1', 'THR', 'NZ', 'LYS', 7.34)], [('CG2', 'THR', 'CB', 'LYS', 7.86), ('CG2', 'THR', 'CG', 'LYS', 8.15), ('CG2', 'THR', 'CD', 'LYS', 7.61), ('CG2', 'THR', 'CE', 'LYS', 8.14), ('CG2', 'THR', 'NZ', 'LYS', 8.21)]]}
GLY_ARG = { 
	'distances':
		[[11.03, 9.72, 10.09, 9.09, 8.24, 8.39, 7.58], [10.71, 9.33, 9.6, 8.52, 7.82, 8.22, 7.08], [9.48, 8.03, 8.17, 7.03, 6.38, 6.93, 5.64], [8.34, 6.96, 7.29, 6.35, 5.64, 5.9, 5.29]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ARG', 11.03), ('O', 'GLY', 'CG', 'ARG', 9.72), ('O', 'GLY', 'CD', 'ARG', 10.09), ('O', 'GLY', 'NE', 'ARG', 9.09), ('O', 'GLY', 'CZ', 'ARG', 8.24), ('O', 'GLY', 'NH1', 'ARG', 8.39), ('O', 'GLY', 'NH2', 'ARG', 7.58)], [('C', 'GLY', 'CB', 'ARG', 10.71), ('C', 'GLY', 'CG', 'ARG', 9.33), ('C', 'GLY', 'CD', 'ARG', 9.6), ('C', 'GLY', 'NE', 'ARG', 8.52), ('C', 'GLY', 'CZ', 'ARG', 7.82), ('C', 'GLY', 'NH1', 'ARG', 8.22), ('C', 'GLY', 'NH2', 'ARG', 7.08)], [('CA', 'GLY', 'CB', 'ARG', 9.48), ('CA', 'GLY', 'CG', 'ARG', 8.03), ('CA', 'GLY', 'CD', 'ARG', 8.17), ('CA', 'GLY', 'NE', 'ARG', 7.03), ('CA', 'GLY', 'CZ', 'ARG', 6.38), ('CA', 'GLY', 'NH1', 'ARG', 6.93), ('CA', 'GLY', 'NH2', 'ARG', 5.64)], [('N', 'GLY', 'CB', 'ARG', 8.34), ('N', 'GLY', 'CG', 'ARG', 6.96), ('N', 'GLY', 'CD', 'ARG', 7.29), ('N', 'GLY', 'NE', 'ARG', 6.35), ('N', 'GLY', 'CZ', 'ARG', 5.64), ('N', 'GLY', 'NH1', 'ARG', 5.9), ('N', 'GLY', 'NH2', 'ARG', 5.29)]]}
ASP_LYS = { 
	'distances':
		[[11.89, 11.64, 10.65, 11.14, 10.53], [11.82, 11.4, 10.24, 10.64, 9.83], [12.37, 11.79, 10.61, 11.11, 10.27], [11.45, 11.08, 9.83, 10.02, 9.1]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 11.89), ('CB', 'ASP', 'CG', 'LYS', 11.64), ('CB', 'ASP', 'CD', 'LYS', 10.65), ('CB', 'ASP', 'CE', 'LYS', 11.14), ('CB', 'ASP', 'NZ', 'LYS', 10.53)], [('CG', 'ASP', 'CB', 'LYS', 11.82), ('CG', 'ASP', 'CG', 'LYS', 11.4), ('CG', 'ASP', 'CD', 'LYS', 10.24), ('CG', 'ASP', 'CE', 'LYS', 10.64), ('CG', 'ASP', 'NZ', 'LYS', 9.83)], [('OD1', 'ASP', 'CB', 'LYS', 12.37), ('OD1', 'ASP', 'CG', 'LYS', 11.79), ('OD1', 'ASP', 'CD', 'LYS', 10.61), ('OD1', 'ASP', 'CE', 'LYS', 11.11), ('OD1', 'ASP', 'NZ', 'LYS', 10.27)], [('OD2', 'ASP', 'CB', 'LYS', 11.45), ('OD2', 'ASP', 'CG', 'LYS', 11.08), ('OD2', 'ASP', 'CD', 'LYS', 9.83), ('OD2', 'ASP', 'CE', 'LYS', 10.02), ('OD2', 'ASP', 'NZ', 'LYS', 9.1)]]}
ASP_GLY = { 
	'distances':
		[[11.37, 11.95, 11.96, 12.0], [10.42, 10.87, 10.74, 10.82], [10.44, 10.76, 10.62, 10.9], [9.88, 10.35, 10.09, 10.01]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 11.37), ('CB', 'ASP', 'C', 'GLY', 11.95), ('CB', 'ASP', 'CA', 'GLY', 11.96), ('CB', 'ASP', 'N', 'GLY', 12.0)], [('CG', 'ASP', 'O', 'GLY', 10.42), ('CG', 'ASP', 'C', 'GLY', 10.87), ('CG', 'ASP', 'CA', 'GLY', 10.74), ('CG', 'ASP', 'N', 'GLY', 10.82)], [('OD1', 'ASP', 'O', 'GLY', 10.44), ('OD1', 'ASP', 'C', 'GLY', 10.76), ('OD1', 'ASP', 'CA', 'GLY', 10.62), ('OD1', 'ASP', 'N', 'GLY', 10.9)], [('OD2', 'ASP', 'O', 'GLY', 9.88), ('OD2', 'ASP', 'C', 'GLY', 10.35), ('OD2', 'ASP', 'CA', 'GLY', 10.09), ('OD2', 'ASP', 'N', 'GLY', 10.01)]]}
LYS_ARG = { 
	'distances':
		[[14.79, 13.92, 14.61, 13.96, 12.94, 12.43, 12.6], [14.4, 13.39, 14.01, 13.25, 12.25, 11.91, 11.78], [13.2, 12.13, 12.65, 11.84, 10.8, 10.47, 10.31], [11.93, 10.96, 11.61, 10.95, 9.96, 9.52, 9.68], [10.77, 9.73, 10.26, 9.54, 8.51, 8.07, 8.22]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'ARG', 14.79), ('CB', 'LYS', 'CG', 'ARG', 13.92), ('CB', 'LYS', 'CD', 'ARG', 14.61), ('CB', 'LYS', 'NE', 'ARG', 13.96), ('CB', 'LYS', 'CZ', 'ARG', 12.94), ('CB', 'LYS', 'NH1', 'ARG', 12.43), ('CB', 'LYS', 'NH2', 'ARG', 12.6)], [('CG', 'LYS', 'CB', 'ARG', 14.4), ('CG', 'LYS', 'CG', 'ARG', 13.39), ('CG', 'LYS', 'CD', 'ARG', 14.01), ('CG', 'LYS', 'NE', 'ARG', 13.25), ('CG', 'LYS', 'CZ', 'ARG', 12.25), ('CG', 'LYS', 'NH1', 'ARG', 11.91), ('CG', 'LYS', 'NH2', 'ARG', 11.78)], [('CD', 'LYS', 'CB', 'ARG', 13.2), ('CD', 'LYS', 'CG', 'ARG', 12.13), ('CD', 'LYS', 'CD', 'ARG', 12.65), ('CD', 'LYS', 'NE', 'ARG', 11.84), ('CD', 'LYS', 'CZ', 'ARG', 10.8), ('CD', 'LYS', 'NH1', 'ARG', 10.47), ('CD', 'LYS', 'NH2', 'ARG', 10.31)], [('CE', 'LYS', 'CB', 'ARG', 11.93), ('CE', 'LYS', 'CG', 'ARG', 10.96), ('CE', 'LYS', 'CD', 'ARG', 11.61), ('CE', 'LYS', 'NE', 'ARG', 10.95), ('CE', 'LYS', 'CZ', 'ARG', 9.96), ('CE', 'LYS', 'NH1', 'ARG', 9.52), ('CE', 'LYS', 'NH2', 'ARG', 9.68)], [('NZ', 'LYS', 'CB', 'ARG', 10.77), ('NZ', 'LYS', 'CG', 'ARG', 9.73), ('NZ', 'LYS', 'CD', 'ARG', 10.26), ('NZ', 'LYS', 'NE', 'ARG', 9.54), ('NZ', 'LYS', 'CZ', 'ARG', 8.51), ('NZ', 'LYS', 'NH1', 'ARG', 8.07), ('NZ', 'LYS', 'NH2', 'ARG', 8.22)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(THR_ARG, d, 'A_1kzh_2_7_1_90')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_THR, d, 'A_1kzh_2_7_1_90')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ARG, d, 'A_1kzh_2_7_1_90')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLY_LYS, d, 'A_1kzh_2_7_1_90')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(THR_GLY, d, 'A_1kzh_2_7_1_90')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(THR_LYS, d, 'A_1kzh_2_7_1_90')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(GLY_ARG, d, 'A_1kzh_2_7_1_90')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASP_LYS, d, 'A_1kzh_2_7_1_90')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASP_GLY, d, 'A_1kzh_2_7_1_90')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(LYS_ARG, d, 'A_1kzh_2_7_1_90')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'THR_ARG' :  match1,
		'ASP_THR' :  match2,
		'ASP_ARG' :  match3,
		'GLY_LYS' :  match4,
		'THR_GLY' :  match5,
		'THR_LYS' :  match6,
		'GLY_ARG' :  match7,
		'ASP_LYS' :  match8,
		'ASP_GLY' :  match9,
		'LYS_ARG' :  match10}