'''
FUNC:M_1ez1_2_1_2_-
PDB:1ez1
EC:2.1.2.-
RESI:ser,gly,asp,thr,arg,mg
LOCI:a-160,162,286,287,362,401;
'''
import motifFunctions as cmd
ASP_MG = { 
	'distances':
		[[11.82], [10.66], [10.25], [10.35]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 11.82)], [('CG', 'ASP', 'MG', 'MG', 10.66)], [('OD1', 'ASP', 'MG', 'MG', 10.25)], [('OD2', 'ASP', 'MG', 'MG', 10.35)]]}
ASP_GLY = { 
	'distances':
		[[15.72, 14.76, 13.67, 12.41], [14.58, 13.63, 12.46, 11.24], [14.8, 13.86, 12.59, 11.41], [13.41, 12.47, 11.35, 10.14]],
	'comparisons':
		[[('CB', 'ASP', 'O', 'GLY', 15.72), ('CB', 'ASP', 'C', 'GLY', 14.76), ('CB', 'ASP', 'CA', 'GLY', 13.67), ('CB', 'ASP', 'N', 'GLY', 12.41)], [('CG', 'ASP', 'O', 'GLY', 14.58), ('CG', 'ASP', 'C', 'GLY', 13.63), ('CG', 'ASP', 'CA', 'GLY', 12.46), ('CG', 'ASP', 'N', 'GLY', 11.24)], [('OD1', 'ASP', 'O', 'GLY', 14.8), ('OD1', 'ASP', 'C', 'GLY', 13.86), ('OD1', 'ASP', 'CA', 'GLY', 12.59), ('OD1', 'ASP', 'N', 'GLY', 11.41)], [('OD2', 'ASP', 'O', 'GLY', 13.41), ('OD2', 'ASP', 'C', 'GLY', 12.47), ('OD2', 'ASP', 'CA', 'GLY', 11.35), ('OD2', 'ASP', 'N', 'GLY', 10.14)]]}
THR_MG = { 
	'distances':
		[[13.25], [12.87], [12.4]],
	'comparisons':
		[[('CB', 'THR', 'MG', 'MG', 13.25)], [('OG1', 'THR', 'MG', 'MG', 12.87)], [('CG2', 'THR', 'MG', 'MG', 12.4)]]}
ASP_THR = { 
	'distances':
		[[7.49, 8.06, 7.31], [7.07, 7.61, 6.53], [6.22, 6.6, 5.64], [8.08, 8.7, 7.29]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 7.49), ('CB', 'ASP', 'OG1', 'THR', 8.06), ('CB', 'ASP', 'CG2', 'THR', 7.31)], [('CG', 'ASP', 'CB', 'THR', 7.07), ('CG', 'ASP', 'OG1', 'THR', 7.61), ('CG', 'ASP', 'CG2', 'THR', 6.53)], [('OD1', 'ASP', 'CB', 'THR', 6.22), ('OD1', 'ASP', 'OG1', 'THR', 6.6), ('OD1', 'ASP', 'CG2', 'THR', 5.64)], [('OD2', 'ASP', 'CB', 'THR', 8.08), ('OD2', 'ASP', 'OG1', 'THR', 8.7), ('OD2', 'ASP', 'CG2', 'THR', 7.29)]]}
ASP_ARG = { 
	'distances':
		[[14.79, 14.08, 15.17, 14.81, 15.72, 16.94, 15.49], [15.16, 14.54, 15.69, 15.37, 16.33, 17.58, 16.12], [16.32, 15.72, 16.89, 16.56, 17.53, 18.78, 17.3], [14.2, 13.62, 14.82, 14.53, 15.54, 16.79, 15.37]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 14.79), ('CB', 'ASP', 'CG', 'ARG', 14.08), ('CB', 'ASP', 'CD', 'ARG', 15.17), ('CB', 'ASP', 'NE', 'ARG', 14.81), ('CB', 'ASP', 'CZ', 'ARG', 15.72), ('CB', 'ASP', 'NH1', 'ARG', 16.94), ('CB', 'ASP', 'NH2', 'ARG', 15.49)], [('CG', 'ASP', 'CB', 'ARG', 15.16), ('CG', 'ASP', 'CG', 'ARG', 14.54), ('CG', 'ASP', 'CD', 'ARG', 15.69), ('CG', 'ASP', 'NE', 'ARG', 15.37), ('CG', 'ASP', 'CZ', 'ARG', 16.33), ('CG', 'ASP', 'NH1', 'ARG', 17.58), ('CG', 'ASP', 'NH2', 'ARG', 16.12)], [('OD1', 'ASP', 'CB', 'ARG', 16.32), ('OD1', 'ASP', 'CG', 'ARG', 15.72), ('OD1', 'ASP', 'CD', 'ARG', 16.89), ('OD1', 'ASP', 'NE', 'ARG', 16.56), ('OD1', 'ASP', 'CZ', 'ARG', 17.53), ('OD1', 'ASP', 'NH1', 'ARG', 18.78), ('OD1', 'ASP', 'NH2', 'ARG', 17.3)], [('OD2', 'ASP', 'CB', 'ARG', 14.2), ('OD2', 'ASP', 'CG', 'ARG', 13.62), ('OD2', 'ASP', 'CD', 'ARG', 14.82), ('OD2', 'ASP', 'NE', 'ARG', 14.53), ('OD2', 'ASP', 'CZ', 'ARG', 15.54), ('OD2', 'ASP', 'NH1', 'ARG', 16.79), ('OD2', 'ASP', 'NH2', 'ARG', 15.37)]]}
ARG_GLY = { 
	'distances':
		[[16.12, 15.73, 15.97, 15.39], [16.07, 15.57, 15.76, 15.06], [17.11, 16.6, 16.87, 16.16], [17.06, 16.46, 16.72, 15.92], [18.01, 17.38, 17.69, 16.87], [19.02, 18.44, 18.81, 18.04], [18.01, 17.31, 17.6, 16.71]],
	'comparisons':
		[[('CB', 'ARG', 'O', 'GLY', 16.12), ('CB', 'ARG', 'C', 'GLY', 15.73), ('CB', 'ARG', 'CA', 'GLY', 15.97), ('CB', 'ARG', 'N', 'GLY', 15.39)], [('CG', 'ARG', 'O', 'GLY', 16.07), ('CG', 'ARG', 'C', 'GLY', 15.57), ('CG', 'ARG', 'CA', 'GLY', 15.76), ('CG', 'ARG', 'N', 'GLY', 15.06)], [('CD', 'ARG', 'O', 'GLY', 17.11), ('CD', 'ARG', 'C', 'GLY', 16.6), ('CD', 'ARG', 'CA', 'GLY', 16.87), ('CD', 'ARG', 'N', 'GLY', 16.16)], [('NE', 'ARG', 'O', 'GLY', 17.06), ('NE', 'ARG', 'C', 'GLY', 16.46), ('NE', 'ARG', 'CA', 'GLY', 16.72), ('NE', 'ARG', 'N', 'GLY', 15.92)], [('CZ', 'ARG', 'O', 'GLY', 18.01), ('CZ', 'ARG', 'C', 'GLY', 17.38), ('CZ', 'ARG', 'CA', 'GLY', 17.69), ('CZ', 'ARG', 'N', 'GLY', 16.87)], [('NH1', 'ARG', 'O', 'GLY', 19.02), ('NH1', 'ARG', 'C', 'GLY', 18.44), ('NH1', 'ARG', 'CA', 'GLY', 18.81), ('NH1', 'ARG', 'N', 'GLY', 18.04)], [('NH2', 'ARG', 'O', 'GLY', 18.01), ('NH2', 'ARG', 'C', 'GLY', 17.31), ('NH2', 'ARG', 'CA', 'GLY', 17.6), ('NH2', 'ARG', 'N', 'GLY', 16.71)]]}
THR_SER = { 
	'distances':
		[[15.02, 14.23], [15.0, 14.09], [14.16, 13.41]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'SER', 15.02), ('CB', 'THR', 'OG', 'SER', 14.23)], [('OG1', 'THR', 'CB', 'SER', 15.0), ('OG1', 'THR', 'OG', 'SER', 14.09)], [('CG2', 'THR', 'CB', 'SER', 14.16), ('CG2', 'THR', 'OG', 'SER', 13.41)]]}
ARG_MG = { 
	'distances':
		[[19.68], [18.94], [19.89], [19.26], [19.99], [21.29], [19.44]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 19.68)], [('CG', 'ARG', 'MG', 'MG', 18.94)], [('CD', 'ARG', 'MG', 'MG', 19.89)], [('NE', 'ARG', 'MG', 'MG', 19.26)], [('CZ', 'ARG', 'MG', 'MG', 19.99)], [('NH1', 'ARG', 'MG', 'MG', 21.29)], [('NH2', 'ARG', 'MG', 'MG', 19.44)]]}
GLY_MG = { 
	'distances':
		[[11.54], [10.49], [9.41], [8.45]],
	'comparisons':
		[[('O', 'GLY', 'MG', 'MG', 11.54)], [('C', 'GLY', 'MG', 'MG', 10.49)], [('CA', 'GLY', 'MG', 'MG', 9.41)], [('N', 'GLY', 'MG', 'MG', 8.45)]]}
THR_GLY = { 
	'distances':
		[[17.95, 17.16, 15.78, 14.81], [18.39, 17.56, 16.15, 15.15], [16.54, 15.8, 14.41, 13.5]],
	'comparisons':
		[[('CB', 'THR', 'O', 'GLY', 17.95), ('CB', 'THR', 'C', 'GLY', 17.16), ('CB', 'THR', 'CA', 'GLY', 15.78), ('CB', 'THR', 'N', 'GLY', 14.81)], [('OG1', 'THR', 'O', 'GLY', 18.39), ('OG1', 'THR', 'C', 'GLY', 17.56), ('OG1', 'THR', 'CA', 'GLY', 16.15), ('OG1', 'THR', 'N', 'GLY', 15.15)], [('CG2', 'THR', 'O', 'GLY', 16.54), ('CG2', 'THR', 'C', 'GLY', 15.8), ('CG2', 'THR', 'CA', 'GLY', 14.41), ('CG2', 'THR', 'N', 'GLY', 13.5)]]}
ARG_SER = { 
	'distances':
		[[16.14, 17.12], [15.26, 16.24], [16.0, 17.03], [15.23, 16.27], [15.83, 16.89], [17.1, 18.18], [15.21, 16.26]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'SER', 16.14), ('CB', 'ARG', 'OG', 'SER', 17.12)], [('CG', 'ARG', 'CB', 'SER', 15.26), ('CG', 'ARG', 'OG', 'SER', 16.24)], [('CD', 'ARG', 'CB', 'SER', 16.0), ('CD', 'ARG', 'OG', 'SER', 17.03)], [('NE', 'ARG', 'CB', 'SER', 15.23), ('NE', 'ARG', 'OG', 'SER', 16.27)], [('CZ', 'ARG', 'CB', 'SER', 15.83), ('CZ', 'ARG', 'OG', 'SER', 16.89)], [('NH1', 'ARG', 'CB', 'SER', 17.1), ('NH1', 'ARG', 'OG', 'SER', 18.18)], [('NH2', 'ARG', 'CB', 'SER', 15.21), ('NH2', 'ARG', 'OG', 'SER', 16.26)]]}
SER_GLY = { 
	'distances':
		[[10.23, 9.02, 8.55, 7.32], [10.87, 9.66, 8.97, 7.72]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 10.23), ('CB', 'SER', 'C', 'GLY', 9.02), ('CB', 'SER', 'CA', 'GLY', 8.55), ('CB', 'SER', 'N', 'GLY', 7.32)], [('OG', 'SER', 'O', 'GLY', 10.87), ('OG', 'SER', 'C', 'GLY', 9.66), ('OG', 'SER', 'CA', 'GLY', 8.97), ('OG', 'SER', 'N', 'GLY', 7.72)]]}
ARG_THR = { 
	'distances':
		[[19.31, 20.33, 18.6], [18.89, 19.83, 18.24], [20.12, 21.03, 19.52], [19.96, 20.78, 19.41], [20.97, 21.74, 20.47], [22.16, 22.95, 21.67], [20.86, 21.54, 20.4]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'THR', 19.31), ('CB', 'ARG', 'OG1', 'THR', 20.33), ('CB', 'ARG', 'CG2', 'THR', 18.6)], [('CG', 'ARG', 'CB', 'THR', 18.89), ('CG', 'ARG', 'OG1', 'THR', 19.83), ('CG', 'ARG', 'CG2', 'THR', 18.24)], [('CD', 'ARG', 'CB', 'THR', 20.12), ('CD', 'ARG', 'OG1', 'THR', 21.03), ('CD', 'ARG', 'CG2', 'THR', 19.52)], [('NE', 'ARG', 'CB', 'THR', 19.96), ('NE', 'ARG', 'OG1', 'THR', 20.78), ('NE', 'ARG', 'CG2', 'THR', 19.41)], [('CZ', 'ARG', 'CB', 'THR', 20.97), ('CZ', 'ARG', 'OG1', 'THR', 21.74), ('CZ', 'ARG', 'CG2', 'THR', 20.47)], [('NH1', 'ARG', 'CB', 'THR', 22.16), ('NH1', 'ARG', 'OG1', 'THR', 22.95), ('NH1', 'ARG', 'CG2', 'THR', 21.67)], [('NH2', 'ARG', 'CB', 'THR', 20.86), ('NH2', 'ARG', 'OG1', 'THR', 21.54), ('NH2', 'ARG', 'CG2', 'THR', 20.4)]]}
SER_MG = { 
	'distances':
		[[6.71], [5.45]],
	'comparisons':
		[[('CB', 'SER', 'MG', 'MG', 6.71)], [('OG', 'SER', 'MG', 'MG', 5.45)]]}
ASP_SER = { 
	'distances':
		[[11.54, 11.17], [10.78, 10.33], [11.04, 10.41], [10.05, 9.75]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'SER', 11.54), ('CB', 'ASP', 'OG', 'SER', 11.17)], [('CG', 'ASP', 'CB', 'SER', 10.78), ('CG', 'ASP', 'OG', 'SER', 10.33)], [('OD1', 'ASP', 'CB', 'SER', 11.04), ('OD1', 'ASP', 'OG', 'SER', 10.41)], [('OD2', 'ASP', 'CB', 'SER', 10.05), ('OD2', 'ASP', 'OG', 'SER', 9.75)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MG, d, 'M_1ez1_2_1_2_-')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_GLY, d, 'M_1ez1_2_1_2_-')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(THR_MG, d, 'M_1ez1_2_1_2_-')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_THR, d, 'M_1ez1_2_1_2_-')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_ARG, d, 'M_1ez1_2_1_2_-')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ARG_GLY, d, 'M_1ez1_2_1_2_-')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(THR_SER, d, 'M_1ez1_2_1_2_-')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ARG_MG, d, 'M_1ez1_2_1_2_-')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(GLY_MG, d, 'M_1ez1_2_1_2_-')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(THR_GLY, d, 'M_1ez1_2_1_2_-')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ARG_SER, d, 'M_1ez1_2_1_2_-')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(SER_GLY, d, 'M_1ez1_2_1_2_-')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(ARG_THR, d, 'M_1ez1_2_1_2_-')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(SER_MG, d, 'M_1ez1_2_1_2_-')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(ASP_SER, d, 'M_1ez1_2_1_2_-')
	if match15 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MG' :  match1,
		'ASP_GLY' :  match2,
		'THR_MG' :  match3,
		'ASP_THR' :  match4,
		'ASP_ARG' :  match5,
		'ARG_GLY' :  match6,
		'THR_SER' :  match7,
		'ARG_MG' :  match8,
		'GLY_MG' :  match9,
		'THR_GLY' :  match10,
		'ARG_SER' :  match11,
		'SER_GLY' :  match12,
		'ARG_THR' :  match13,
		'SER_MG' :  match14,
		'ASP_SER' :  match15}