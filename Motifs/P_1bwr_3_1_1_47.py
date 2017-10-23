'''
FUNC:P_1bwr_3_1_1_47
PDB:1bwr
EC:3.1.1.47
RESI:ser,gly,asn,asp,his
LOCI:a-47,74,104,192,195;
'''
import motifFunctions as cmd
GLY_HIS = { 
	'distances':
		[[15.01, 13.63, 13.49, 12.44, 12.23, 11.52], [14.17, 12.82, 12.77, 11.59, 11.54, 10.73], [13.09, 11.69, 11.55, 10.5, 10.29, 9.55], [12.14, 10.81, 10.83, 9.56, 9.64, 8.75]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'HIS', 15.01), ('O', 'GLY', 'CG', 'HIS', 13.63), ('O', 'GLY', 'ND1', 'HIS', 13.49), ('O', 'GLY', 'CD2', 'HIS', 12.44), ('O', 'GLY', 'CE1', 'HIS', 12.23), ('O', 'GLY', 'NE2', 'HIS', 11.52)], [('C', 'GLY', 'CB', 'HIS', 14.17), ('C', 'GLY', 'CG', 'HIS', 12.82), ('C', 'GLY', 'ND1', 'HIS', 12.77), ('C', 'GLY', 'CD2', 'HIS', 11.59), ('C', 'GLY', 'CE1', 'HIS', 11.54), ('C', 'GLY', 'NE2', 'HIS', 10.73)], [('CA', 'GLY', 'CB', 'HIS', 13.09), ('CA', 'GLY', 'CG', 'HIS', 11.69), ('CA', 'GLY', 'ND1', 'HIS', 11.55), ('CA', 'GLY', 'CD2', 'HIS', 10.5), ('CA', 'GLY', 'CE1', 'HIS', 10.29), ('CA', 'GLY', 'NE2', 'HIS', 9.55)], [('N', 'GLY', 'CB', 'HIS', 12.14), ('N', 'GLY', 'CG', 'HIS', 10.81), ('N', 'GLY', 'ND1', 'HIS', 10.83), ('N', 'GLY', 'CD2', 'HIS', 9.56), ('N', 'GLY', 'CE1', 'HIS', 9.64), ('N', 'GLY', 'NE2', 'HIS', 8.75)]]}
ASP_HIS = { 
	'distances':
		[[7.61, 7.71, 6.81, 8.93, 7.73, 8.9], [6.19, 6.22, 5.37, 7.44, 6.38, 7.48], [5.58, 5.89, 5.38, 7.15, 6.53, 7.43], [6.01, 5.66, 4.56, 6.75, 5.41, 6.6]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'HIS', 7.61), ('CB', 'ASP', 'CG', 'HIS', 7.71), ('CB', 'ASP', 'ND1', 'HIS', 6.81), ('CB', 'ASP', 'CD2', 'HIS', 8.93), ('CB', 'ASP', 'CE1', 'HIS', 7.73), ('CB', 'ASP', 'NE2', 'HIS', 8.9)], [('CG', 'ASP', 'CB', 'HIS', 6.19), ('CG', 'ASP', 'CG', 'HIS', 6.22), ('CG', 'ASP', 'ND1', 'HIS', 5.37), ('CG', 'ASP', 'CD2', 'HIS', 7.44), ('CG', 'ASP', 'CE1', 'HIS', 6.38), ('CG', 'ASP', 'NE2', 'HIS', 7.48)], [('OD1', 'ASP', 'CB', 'HIS', 5.58), ('OD1', 'ASP', 'CG', 'HIS', 5.89), ('OD1', 'ASP', 'ND1', 'HIS', 5.38), ('OD1', 'ASP', 'CD2', 'HIS', 7.15), ('OD1', 'ASP', 'CE1', 'HIS', 6.53), ('OD1', 'ASP', 'NE2', 'HIS', 7.43)], [('OD2', 'ASP', 'CB', 'HIS', 6.01), ('OD2', 'ASP', 'CG', 'HIS', 5.66), ('OD2', 'ASP', 'ND1', 'HIS', 4.56), ('OD2', 'ASP', 'CD2', 'HIS', 6.75), ('OD2', 'ASP', 'CE1', 'HIS', 5.41), ('OD2', 'ASP', 'NE2', 'HIS', 6.6)]]}
GLY_ASN = { 
	'distances':
		[[6.03, 6.2, 7.23, 5.73], [6.37, 6.17, 7.17, 5.35], [6.87, 6.23, 6.95, 5.36], [7.58, 6.68, 7.3, 5.55]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASN', 6.03), ('O', 'GLY', 'CG', 'ASN', 6.2), ('O', 'GLY', 'OD1', 'ASN', 7.23), ('O', 'GLY', 'ND2', 'ASN', 5.73)], [('C', 'GLY', 'CB', 'ASN', 6.37), ('C', 'GLY', 'CG', 'ASN', 6.17), ('C', 'GLY', 'OD1', 'ASN', 7.17), ('C', 'GLY', 'ND2', 'ASN', 5.35)], [('CA', 'GLY', 'CB', 'ASN', 6.87), ('CA', 'GLY', 'CG', 'ASN', 6.23), ('CA', 'GLY', 'OD1', 'ASN', 6.95), ('CA', 'GLY', 'ND2', 'ASN', 5.36)], [('N', 'GLY', 'CB', 'ASN', 7.58), ('N', 'GLY', 'CG', 'ASN', 6.68), ('N', 'GLY', 'OD1', 'ASN', 7.3), ('N', 'GLY', 'ND2', 'ASN', 5.55)]]}
ASN_ASP = { 
	'distances':
		[[16.02, 14.88, 14.74, 14.19], [14.7, 13.52, 13.38, 12.8], [13.63, 12.49, 12.35, 11.82], [14.83, 13.56, 13.43, 12.77]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 16.02), ('CB', 'ASN', 'CG', 'ASP', 14.88), ('CB', 'ASN', 'OD1', 'ASP', 14.74), ('CB', 'ASN', 'OD2', 'ASP', 14.19)], [('CG', 'ASN', 'CB', 'ASP', 14.7), ('CG', 'ASN', 'CG', 'ASP', 13.52), ('CG', 'ASN', 'OD1', 'ASP', 13.38), ('CG', 'ASN', 'OD2', 'ASP', 12.8)], [('OD1', 'ASN', 'CB', 'ASP', 13.63), ('OD1', 'ASN', 'CG', 'ASP', 12.49), ('OD1', 'ASN', 'OD1', 'ASP', 12.35), ('OD1', 'ASN', 'OD2', 'ASP', 11.82)], [('ND2', 'ASN', 'CB', 'ASP', 14.83), ('ND2', 'ASN', 'CG', 'ASP', 13.56), ('ND2', 'ASN', 'OD1', 'ASP', 13.43), ('ND2', 'ASN', 'OD2', 'ASP', 12.77)]]}
GLY_ASP = { 
	'distances':
		[[17.56, 16.39, 16.48, 15.43], [17.03, 15.8, 15.87, 14.82], [15.77, 14.57, 14.71, 13.53], [15.28, 14.0, 14.09, 12.96]],
	'comparisons':
		[[('O', 'GLY', 'CB', 'ASP', 17.56), ('O', 'GLY', 'CG', 'ASP', 16.39), ('O', 'GLY', 'OD1', 'ASP', 16.48), ('O', 'GLY', 'OD2', 'ASP', 15.43)], [('C', 'GLY', 'CB', 'ASP', 17.03), ('C', 'GLY', 'CG', 'ASP', 15.8), ('C', 'GLY', 'OD1', 'ASP', 15.87), ('C', 'GLY', 'OD2', 'ASP', 14.82)], [('CA', 'GLY', 'CB', 'ASP', 15.77), ('CA', 'GLY', 'CG', 'ASP', 14.57), ('CA', 'GLY', 'OD1', 'ASP', 14.71), ('CA', 'GLY', 'OD2', 'ASP', 13.53)], [('N', 'GLY', 'CB', 'ASP', 15.28), ('N', 'GLY', 'CG', 'ASP', 14.0), ('N', 'GLY', 'OD1', 'ASP', 14.09), ('N', 'GLY', 'OD2', 'ASP', 12.96)]]}
SER_GLY = { 
	'distances':
		[[10.09, 8.96, 8.06, 6.69], [10.66, 9.63, 8.7, 7.48]],
	'comparisons':
		[[('CB', 'SER', 'O', 'GLY', 10.09), ('CB', 'SER', 'C', 'GLY', 8.96), ('CB', 'SER', 'CA', 'GLY', 8.06), ('CB', 'SER', 'N', 'GLY', 6.69)], [('OG', 'SER', 'O', 'GLY', 10.66), ('OG', 'SER', 'C', 'GLY', 9.63), ('OG', 'SER', 'CA', 'GLY', 8.7), ('OG', 'SER', 'N', 'GLY', 7.48)]]}
ASN_HIS = { 
	'distances':
		[[13.69, 12.44, 12.32, 11.4, 11.22, 10.6], [12.23, 10.96, 10.85, 9.91, 9.75, 9.1], [11.47, 10.2, 10.0, 9.27, 8.93, 8.42], [11.91, 10.64, 10.66, 9.47, 9.54, 8.72]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'HIS', 13.69), ('CB', 'ASN', 'CG', 'HIS', 12.44), ('CB', 'ASN', 'ND1', 'HIS', 12.32), ('CB', 'ASN', 'CD2', 'HIS', 11.4), ('CB', 'ASN', 'CE1', 'HIS', 11.22), ('CB', 'ASN', 'NE2', 'HIS', 10.6)], [('CG', 'ASN', 'CB', 'HIS', 12.23), ('CG', 'ASN', 'CG', 'HIS', 10.96), ('CG', 'ASN', 'ND1', 'HIS', 10.85), ('CG', 'ASN', 'CD2', 'HIS', 9.91), ('CG', 'ASN', 'CE1', 'HIS', 9.75), ('CG', 'ASN', 'NE2', 'HIS', 9.1)], [('OD1', 'ASN', 'CB', 'HIS', 11.47), ('OD1', 'ASN', 'CG', 'HIS', 10.2), ('OD1', 'ASN', 'ND1', 'HIS', 10.0), ('OD1', 'ASN', 'CD2', 'HIS', 9.27), ('OD1', 'ASN', 'CE1', 'HIS', 8.93), ('OD1', 'ASN', 'NE2', 'HIS', 8.42)], [('ND2', 'ASN', 'CB', 'HIS', 11.91), ('ND2', 'ASN', 'CG', 'HIS', 10.64), ('ND2', 'ASN', 'ND1', 'HIS', 10.66), ('ND2', 'ASN', 'CD2', 'HIS', 9.47), ('ND2', 'ASN', 'CE1', 'HIS', 9.54), ('ND2', 'ASN', 'NE2', 'HIS', 8.72)]]}
SER_ASP = { 
	'distances':
		[[12.94, 11.49, 11.33, 10.6], [11.77, 10.3, 10.05, 9.49]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 12.94), ('CB', 'SER', 'CG', 'ASP', 11.49), ('CB', 'SER', 'OD1', 'ASP', 11.33), ('CB', 'SER', 'OD2', 'ASP', 10.6)], [('OG', 'SER', 'CB', 'ASP', 11.77), ('OG', 'SER', 'CG', 'ASP', 10.3), ('OG', 'SER', 'OD1', 'ASP', 10.05), ('OG', 'SER', 'OD2', 'ASP', 9.49)]]}
SER_ASN = { 
	'distances':
		[[10.34, 8.98, 9.02, 7.94], [10.29, 8.85, 8.66, 8.0]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASN', 10.34), ('CB', 'SER', 'CG', 'ASN', 8.98), ('CB', 'SER', 'OD1', 'ASN', 9.02), ('CB', 'SER', 'ND2', 'ASN', 7.94)], [('OG', 'SER', 'CB', 'ASN', 10.29), ('OG', 'SER', 'CG', 'ASN', 8.85), ('OG', 'SER', 'OD1', 'ASN', 8.66), ('OG', 'SER', 'ND2', 'ASN', 8.0)]]}
SER_HIS = { 
	'distances':
		[[8.44, 7.48, 8.14, 6.2, 7.48, 6.22], [7.17, 6.21, 6.97, 4.9, 6.42, 5.11]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 8.44), ('CB', 'SER', 'CG', 'HIS', 7.48), ('CB', 'SER', 'ND1', 'HIS', 8.14), ('CB', 'SER', 'CD2', 'HIS', 6.2), ('CB', 'SER', 'CE1', 'HIS', 7.48), ('CB', 'SER', 'NE2', 'HIS', 6.22)], [('OG', 'SER', 'CB', 'HIS', 7.17), ('OG', 'SER', 'CG', 'HIS', 6.21), ('OG', 'SER', 'ND1', 'HIS', 6.97), ('OG', 'SER', 'CD2', 'HIS', 4.9), ('OG', 'SER', 'CE1', 'HIS', 6.42), ('OG', 'SER', 'NE2', 'HIS', 5.11)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLY_HIS, d, 'P_1bwr_3_1_1_47')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASP_HIS, d, 'P_1bwr_3_1_1_47')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLY_ASN, d, 'P_1bwr_3_1_1_47')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASN_ASP, d, 'P_1bwr_3_1_1_47')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(GLY_ASP, d, 'P_1bwr_3_1_1_47')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_GLY, d, 'P_1bwr_3_1_1_47')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASN_HIS, d, 'P_1bwr_3_1_1_47')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(SER_ASP, d, 'P_1bwr_3_1_1_47')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(SER_ASN, d, 'P_1bwr_3_1_1_47')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(SER_HIS, d, 'P_1bwr_3_1_1_47')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLY_HIS' :  match1,
		'ASP_HIS' :  match2,
		'GLY_ASN' :  match3,
		'ASN_ASP' :  match4,
		'GLY_ASP' :  match5,
		'SER_GLY' :  match6,
		'ASN_HIS' :  match7,
		'SER_ASP' :  match8,
		'SER_ASN' :  match9,
		'SER_HIS' :  match10}