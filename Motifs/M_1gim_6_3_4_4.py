'''
FUNC:M_1gim_6_3_4_4
PDB:1gim
EC:6.3.4.4
RESI:asp,lys,his,gln,mg
LOCI:a-13,16,41,224,435;
'''
import motifFunctions as cmd
ASP_MG = { 
	'distances':
		[[6.14], [5.64], [5.16], [6.29]],
	'comparisons':
		[[('CB', 'ASP', 'MG', 'MG', 6.14)], [('CG', 'ASP', 'MG', 'MG', 5.64)], [('OD1', 'ASP', 'MG', 'MG', 5.16)], [('OD2', 'ASP', 'MG', 'MG', 6.29)]]}
GLN_LYS = { 
	'distances':
		[[11.25, 10.91, 9.46, 8.74, 7.43], [12.06, 11.91, 10.5, 9.71, 8.35], [12.02, 11.98, 10.6, 9.95, 8.52], [12.4, 12.26, 10.86, 10.4, 8.96], [11.91, 12.06, 10.77, 10.04, 8.64]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'LYS', 11.25), ('CB', 'GLN', 'CG', 'LYS', 10.91), ('CB', 'GLN', 'CD', 'LYS', 9.46), ('CB', 'GLN', 'CE', 'LYS', 8.74), ('CB', 'GLN', 'NZ', 'LYS', 7.43)], [('CG', 'GLN', 'CB', 'LYS', 12.06), ('CG', 'GLN', 'CG', 'LYS', 11.91), ('CG', 'GLN', 'CD', 'LYS', 10.5), ('CG', 'GLN', 'CE', 'LYS', 9.71), ('CG', 'GLN', 'NZ', 'LYS', 8.35)], [('CD', 'GLN', 'CB', 'LYS', 12.02), ('CD', 'GLN', 'CG', 'LYS', 11.98), ('CD', 'GLN', 'CD', 'LYS', 10.6), ('CD', 'GLN', 'CE', 'LYS', 9.95), ('CD', 'GLN', 'NZ', 'LYS', 8.52)], [('OE1', 'GLN', 'CB', 'LYS', 12.4), ('OE1', 'GLN', 'CG', 'LYS', 12.26), ('OE1', 'GLN', 'CD', 'LYS', 10.86), ('OE1', 'GLN', 'CE', 'LYS', 10.4), ('OE1', 'GLN', 'NZ', 'LYS', 8.96)], [('NE2', 'GLN', 'CB', 'LYS', 11.91), ('NE2', 'GLN', 'CG', 'LYS', 12.06), ('NE2', 'GLN', 'CD', 'LYS', 10.77), ('NE2', 'GLN', 'CE', 'LYS', 10.04), ('NE2', 'GLN', 'NZ', 'LYS', 8.64)]]}
ASP_HIS = { 
	'distances':
		[[10.61, 10.64, 9.62, 11.76, 10.28, 11.54], [10.69, 10.56, 9.49, 11.58, 9.99, 11.25], [10.21, 9.89, 8.72, 10.8, 9.07, 10.33], [11.47, 11.41, 10.39, 12.42, 10.9, 12.11]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 10.61), ('CB', 'ASP', 'CG', 'HIS', 10.64), ('CB', 'ASP', 'ND1', 'HIS', 9.62), ('CB', 'ASP', 'CD2', 'HIS', 11.76), ('CB', 'ASP', 'CE1', 'HIS', 10.28), ('CB', 'ASP', 'NE2', 'HIS', 11.54)], [('CG', 'ASP', 'CB', 'HIS', 10.69), ('CG', 'ASP', 'CG', 'HIS', 10.56), ('CG', 'ASP', 'ND1', 'HIS', 9.49), ('CG', 'ASP', 'CD2', 'HIS', 11.58), ('CG', 'ASP', 'CE1', 'HIS', 9.99), ('CG', 'ASP', 'NE2', 'HIS', 11.25)], [('OD1', 'ASP', 'CB', 'HIS', 10.21), ('OD1', 'ASP', 'CG', 'HIS', 9.89), ('OD1', 'ASP', 'ND1', 'HIS', 8.72), ('OD1', 'ASP', 'CD2', 'HIS', 10.8), ('OD1', 'ASP', 'CE1', 'HIS', 9.07), ('OD1', 'ASP', 'NE2', 'HIS', 10.33)], [('OD2', 'ASP', 'CB', 'HIS', 11.47), ('OD2', 'ASP', 'CG', 'HIS', 11.41), ('OD2', 'ASP', 'ND1', 'HIS', 10.39), ('OD2', 'ASP', 'CD2', 'HIS', 12.42), ('OD2', 'ASP', 'CE1', 'HIS', 10.9), ('OD2', 'ASP', 'NE2', 'HIS', 12.11)]]}
ASP_GLN = { 
	'distances':
		[[10.49, 10.7, 11.51, 12.62, 11.17], [9.69, 9.67, 10.47, 11.64, 10.06], [8.57, 8.53, 9.26, 10.42, 8.85], [10.35, 10.16, 10.98, 12.18, 10.51]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLN', 10.49), ('CB', 'ASP', 'CG', 'GLN', 10.7), ('CB', 'ASP', 'CD', 'GLN', 11.51), ('CB', 'ASP', 'OE1', 'GLN', 12.62), ('CB', 'ASP', 'NE2', 'GLN', 11.17)], [('CG', 'ASP', 'CB', 'GLN', 9.69), ('CG', 'ASP', 'CG', 'GLN', 9.67), ('CG', 'ASP', 'CD', 'GLN', 10.47), ('CG', 'ASP', 'OE1', 'GLN', 11.64), ('CG', 'ASP', 'NE2', 'GLN', 10.06)], [('OD1', 'ASP', 'CB', 'GLN', 8.57), ('OD1', 'ASP', 'CG', 'GLN', 8.53), ('OD1', 'ASP', 'CD', 'GLN', 9.26), ('OD1', 'ASP', 'OE1', 'GLN', 10.42), ('OD1', 'ASP', 'NE2', 'GLN', 8.85)], [('OD2', 'ASP', 'CB', 'GLN', 10.35), ('OD2', 'ASP', 'CG', 'GLN', 10.16), ('OD2', 'ASP', 'CD', 'GLN', 10.98), ('OD2', 'ASP', 'OE1', 'GLN', 12.18), ('OD2', 'ASP', 'NE2', 'GLN', 10.51)]]}
HIS_MG = { 
	'distances':
		[[7.31], [7.17], [6.27], [8.18], [6.95], [8.04]],
	'comparisons':
		[[('CB', 'HIS', 'MG', 'MG', 7.31)], [('CG', 'HIS', 'MG', 'MG', 7.17)], [('ND1', 'HIS', 'MG', 'MG', 6.27)], [('CD2', 'HIS', 'MG', 'MG', 8.18)], [('CE1', 'HIS', 'MG', 'MG', 6.95)], [('NE2', 'HIS', 'MG', 'MG', 8.04)]]}
GLN_MG = { 
	'distances':
		[[10.06], [9.85], [9.99], [11.05], [9.18]],
	'comparisons':
		[[('CB', 'GLN', 'MG', 'MG', 10.06)], [('CG', 'GLN', 'MG', 'MG', 9.85)], [('CD', 'GLN', 'MG', 'MG', 9.99)], [('OE1', 'GLN', 'MG', 'MG', 11.05)], [('NE2', 'GLN', 'MG', 'MG', 9.18)]]}
HIS_GLN = { 
	'distances':
		[[13.19, 13.17, 12.74, 13.4, 11.88], [12.05, 12.02, 11.49, 12.07, 10.66], [10.73, 10.75, 10.32, 10.95, 9.55], [12.17, 12.09, 11.38, 11.82, 10.54], [10.01, 10.01, 9.42, 9.93, 8.69], [10.96, 10.89, 10.12, 10.5, 9.34]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'GLN', 13.19), ('CB', 'HIS', 'CG', 'GLN', 13.17), ('CB', 'HIS', 'CD', 'GLN', 12.74), ('CB', 'HIS', 'OE1', 'GLN', 13.4), ('CB', 'HIS', 'NE2', 'GLN', 11.88)], [('CG', 'HIS', 'CB', 'GLN', 12.05), ('CG', 'HIS', 'CG', 'GLN', 12.02), ('CG', 'HIS', 'CD', 'GLN', 11.49), ('CG', 'HIS', 'OE1', 'GLN', 12.07), ('CG', 'HIS', 'NE2', 'GLN', 10.66)], [('ND1', 'HIS', 'CB', 'GLN', 10.73), ('ND1', 'HIS', 'CG', 'GLN', 10.75), ('ND1', 'HIS', 'CD', 'GLN', 10.32), ('ND1', 'HIS', 'OE1', 'GLN', 10.95), ('ND1', 'HIS', 'NE2', 'GLN', 9.55)], [('CD2', 'HIS', 'CB', 'GLN', 12.17), ('CD2', 'HIS', 'CG', 'GLN', 12.09), ('CD2', 'HIS', 'CD', 'GLN', 11.38), ('CD2', 'HIS', 'OE1', 'GLN', 11.82), ('CD2', 'HIS', 'NE2', 'GLN', 10.54)], [('CE1', 'HIS', 'CB', 'GLN', 10.01), ('CE1', 'HIS', 'CG', 'GLN', 10.01), ('CE1', 'HIS', 'CD', 'GLN', 9.42), ('CE1', 'HIS', 'OE1', 'GLN', 9.93), ('CE1', 'HIS', 'NE2', 'GLN', 8.69)], [('NE2', 'HIS', 'CB', 'GLN', 10.96), ('NE2', 'HIS', 'CG', 'GLN', 10.89), ('NE2', 'HIS', 'CD', 'GLN', 10.12), ('NE2', 'HIS', 'OE1', 'GLN', 10.5), ('NE2', 'HIS', 'NE2', 'GLN', 9.34)]]}
HIS_LYS = { 
	'distances':
		[[8.13, 9.56, 9.82, 9.33, 9.44], [7.61, 8.94, 9.0, 8.57, 8.48], [7.02, 8.23, 8.06, 7.46, 7.24], [8.08, 9.32, 9.3, 9.07, 8.84], [7.2, 8.22, 7.83, 7.38, 6.89], [7.84, 8.9, 8.62, 8.41, 7.95]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'LYS', 8.13), ('CB', 'HIS', 'CG', 'LYS', 9.56), ('CB', 'HIS', 'CD', 'LYS', 9.82), ('CB', 'HIS', 'CE', 'LYS', 9.33), ('CB', 'HIS', 'NZ', 'LYS', 9.44)], [('CG', 'HIS', 'CB', 'LYS', 7.61), ('CG', 'HIS', 'CG', 'LYS', 8.94), ('CG', 'HIS', 'CD', 'LYS', 9.0), ('CG', 'HIS', 'CE', 'LYS', 8.57), ('CG', 'HIS', 'NZ', 'LYS', 8.48)], [('ND1', 'HIS', 'CB', 'LYS', 7.02), ('ND1', 'HIS', 'CG', 'LYS', 8.23), ('ND1', 'HIS', 'CD', 'LYS', 8.06), ('ND1', 'HIS', 'CE', 'LYS', 7.46), ('ND1', 'HIS', 'NZ', 'LYS', 7.24)], [('CD2', 'HIS', 'CB', 'LYS', 8.08), ('CD2', 'HIS', 'CG', 'LYS', 9.32), ('CD2', 'HIS', 'CD', 'LYS', 9.3), ('CD2', 'HIS', 'CE', 'LYS', 9.07), ('CD2', 'HIS', 'NZ', 'LYS', 8.84)], [('CE1', 'HIS', 'CB', 'LYS', 7.2), ('CE1', 'HIS', 'CG', 'LYS', 8.22), ('CE1', 'HIS', 'CD', 'LYS', 7.83), ('CE1', 'HIS', 'CE', 'LYS', 7.38), ('CE1', 'HIS', 'NZ', 'LYS', 6.89)], [('NE2', 'HIS', 'CB', 'LYS', 7.84), ('NE2', 'HIS', 'CG', 'LYS', 8.9), ('NE2', 'HIS', 'CD', 'LYS', 8.62), ('NE2', 'HIS', 'CE', 'LYS', 8.41), ('NE2', 'HIS', 'NZ', 'LYS', 7.95)]]}
ASP_LYS = { 
	'distances':
		[[10.52, 10.93, 10.5, 9.03, 9.05], [11.05, 11.47, 10.86, 9.37, 9.09], [10.42, 10.82, 10.07, 8.61, 8.14], [12.26, 12.72, 12.09, 10.6, 10.26]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 10.52), ('CB', 'ASP', 'CG', 'LYS', 10.93), ('CB', 'ASP', 'CD', 'LYS', 10.5), ('CB', 'ASP', 'CE', 'LYS', 9.03), ('CB', 'ASP', 'NZ', 'LYS', 9.05)], [('CG', 'ASP', 'CB', 'LYS', 11.05), ('CG', 'ASP', 'CG', 'LYS', 11.47), ('CG', 'ASP', 'CD', 'LYS', 10.86), ('CG', 'ASP', 'CE', 'LYS', 9.37), ('CG', 'ASP', 'NZ', 'LYS', 9.09)], [('OD1', 'ASP', 'CB', 'LYS', 10.42), ('OD1', 'ASP', 'CG', 'LYS', 10.82), ('OD1', 'ASP', 'CD', 'LYS', 10.07), ('OD1', 'ASP', 'CE', 'LYS', 8.61), ('OD1', 'ASP', 'NZ', 'LYS', 8.14)], [('OD2', 'ASP', 'CB', 'LYS', 12.26), ('OD2', 'ASP', 'CG', 'LYS', 12.72), ('OD2', 'ASP', 'CD', 'LYS', 12.09), ('OD2', 'ASP', 'CE', 'LYS', 10.6), ('OD2', 'ASP', 'NZ', 'LYS', 10.26)]]}
LYS_MG = { 
	'distances':
		[[9.46], [10.35], [9.9], [8.62], [8.26]],
	'comparisons':
		[[('CB', 'LYS', 'MG', 'MG', 9.46)], [('CG', 'LYS', 'MG', 'MG', 10.35)], [('CD', 'LYS', 'MG', 'MG', 9.9)], [('CE', 'LYS', 'MG', 'MG', 8.62)], [('NZ', 'LYS', 'MG', 'MG', 8.26)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_MG, d, 'M_1gim_6_3_4_4')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_LYS, d, 'M_1gim_6_3_4_4')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_HIS, d, 'M_1gim_6_3_4_4')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_GLN, d, 'M_1gim_6_3_4_4')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(HIS_MG, d, 'M_1gim_6_3_4_4')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLN_MG, d, 'M_1gim_6_3_4_4')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(HIS_GLN, d, 'M_1gim_6_3_4_4')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(HIS_LYS, d, 'M_1gim_6_3_4_4')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASP_LYS, d, 'M_1gim_6_3_4_4')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(LYS_MG, d, 'M_1gim_6_3_4_4')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_MG' :  match1,
		'GLN_LYS' :  match2,
		'ASP_HIS' :  match3,
		'ASP_GLN' :  match4,
		'HIS_MG' :  match5,
		'GLN_MG' :  match6,
		'HIS_GLN' :  match7,
		'HIS_LYS' :  match8,
		'ASP_LYS' :  match9,
		'LYS_MG' :  match10}