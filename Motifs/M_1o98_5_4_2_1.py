'''
FUNC:M_1o98_5_4_2_1
PDB:1o98
EC:5.4.2.1
RESI:ser,asp,arg,mn,mn
LOCI:a-62,154,261,601,701;
'''
import motifFunctions as cmd
MN_MN = { 
	'distances':
		[6.89, 6.89],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 6.89), ('MN', 'MN', 'MN', 'MN', 6.89)]}
SER_MN = { 
	'distances':
		[[7.81], [6.77], [5.1], [4.0]],
	'comparisons':
		[[('CB', 'SER', 'MN', 'MN', 7.81)], [('OG', 'SER', 'MN', 'MN', 6.77)], [('CB', 'SER', 'MN', 'MN', 5.1)], [('OG', 'SER', 'MN', 'MN', 4.0)]]}
ASP_ARG = { 
	'distances':
		[[12.27, 12.5, 11.4, 11.73, 11.33, 10.52, 11.94], [11.08, 11.19, 10.06, 10.3, 9.89, 9.14, 10.47], [11.16, 11.09, 9.83, 9.91, 9.33, 8.5, 9.81], [10.22, 10.43, 9.43, 9.74, 9.5, 8.9, 10.13]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ARG', 12.27), ('CB', 'ASP', 'CG', 'ARG', 12.5), ('CB', 'ASP', 'CD', 'ARG', 11.4), ('CB', 'ASP', 'NE', 'ARG', 11.73), ('CB', 'ASP', 'CZ', 'ARG', 11.33), ('CB', 'ASP', 'NH1', 'ARG', 10.52), ('CB', 'ASP', 'NH2', 'ARG', 11.94)], [('CG', 'ASP', 'CB', 'ARG', 11.08), ('CG', 'ASP', 'CG', 'ARG', 11.19), ('CG', 'ASP', 'CD', 'ARG', 10.06), ('CG', 'ASP', 'NE', 'ARG', 10.3), ('CG', 'ASP', 'CZ', 'ARG', 9.89), ('CG', 'ASP', 'NH1', 'ARG', 9.14), ('CG', 'ASP', 'NH2', 'ARG', 10.47)], [('OD1', 'ASP', 'CB', 'ARG', 11.16), ('OD1', 'ASP', 'CG', 'ARG', 11.09), ('OD1', 'ASP', 'CD', 'ARG', 9.83), ('OD1', 'ASP', 'NE', 'ARG', 9.91), ('OD1', 'ASP', 'CZ', 'ARG', 9.33), ('OD1', 'ASP', 'NH1', 'ARG', 8.5), ('OD1', 'ASP', 'NH2', 'ARG', 9.81)], [('OD2', 'ASP', 'CB', 'ARG', 10.22), ('OD2', 'ASP', 'CG', 'ARG', 10.43), ('OD2', 'ASP', 'CD', 'ARG', 9.43), ('OD2', 'ASP', 'NE', 'ARG', 9.74), ('OD2', 'ASP', 'CZ', 'ARG', 9.5), ('OD2', 'ASP', 'NH1', 'ARG', 8.9), ('OD2', 'ASP', 'NH2', 'ARG', 10.13)]]}
ASP_MN = { 
	'distances':
		[[10.46], [9.5], [8.29], [10.1], [14.26], [13.2], [12.02], [13.63]],
	'comparisons':
		[[('CB', 'ASP', 'MN', 'MN', 10.46)], [('CG', 'ASP', 'MN', 'MN', 9.5)], [('OD1', 'ASP', 'MN', 'MN', 8.29)], [('OD2', 'ASP', 'MN', 'MN', 10.1)], [('CB', 'ASP', 'MN', 'MN', 14.26)], [('CG', 'ASP', 'MN', 'MN', 13.2)], [('OD1', 'ASP', 'MN', 'MN', 12.02)], [('OD2', 'ASP', 'MN', 'MN', 13.63)]]}
ARG_MN = { 
	'distances':
		[[13.55], [12.64], [11.21], [10.39], [9.13], [8.53], [8.67], [14.04], [12.83], [11.56], [10.64], [9.38], [8.91], [8.82]],
	'comparisons':
		[[('CB', 'ARG', 'MN', 'MN', 13.55)], [('CG', 'ARG', 'MN', 'MN', 12.64)], [('CD', 'ARG', 'MN', 'MN', 11.21)], [('NE', 'ARG', 'MN', 'MN', 10.39)], [('CZ', 'ARG', 'MN', 'MN', 9.13)], [('NH1', 'ARG', 'MN', 'MN', 8.53)], [('NH2', 'ARG', 'MN', 'MN', 8.67)], [('CB', 'ARG', 'MN', 'MN', 14.04)], [('CG', 'ARG', 'MN', 'MN', 12.83)], [('CD', 'ARG', 'MN', 'MN', 11.56)], [('NE', 'ARG', 'MN', 'MN', 10.64)], [('CZ', 'ARG', 'MN', 'MN', 9.38)], [('NH1', 'ARG', 'MN', 'MN', 8.91)], [('NH2', 'ARG', 'MN', 'MN', 8.82)]]}
SER_ARG = { 
	'distances':
		[[11.35, 10.03, 8.91, 7.89, 6.75, 6.61, 6.16], [12.38, 11.1, 9.89, 8.84, 7.6, 7.35, 6.91]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ARG', 11.35), ('CB', 'SER', 'CG', 'ARG', 10.03), ('CB', 'SER', 'CD', 'ARG', 8.91), ('CB', 'SER', 'NE', 'ARG', 7.89), ('CB', 'SER', 'CZ', 'ARG', 6.75), ('CB', 'SER', 'NH1', 'ARG', 6.61), ('CB', 'SER', 'NH2', 'ARG', 6.16)], [('OG', 'SER', 'CB', 'ARG', 12.38), ('OG', 'SER', 'CG', 'ARG', 11.1), ('OG', 'SER', 'CD', 'ARG', 9.89), ('OG', 'SER', 'NE', 'ARG', 8.84), ('OG', 'SER', 'CZ', 'ARG', 7.6), ('OG', 'SER', 'NH1', 'ARG', 7.35), ('OG', 'SER', 'NH2', 'ARG', 6.91)]]}
SER_ASP = { 
	'distances':
		[[13.8, 12.52, 11.52, 12.64], [13.63, 12.4, 11.31, 12.65]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'ASP', 13.8), ('CB', 'SER', 'CG', 'ASP', 12.52), ('CB', 'SER', 'OD1', 'ASP', 11.52), ('CB', 'SER', 'OD2', 'ASP', 12.64)], [('OG', 'SER', 'CB', 'ASP', 13.63), ('OG', 'SER', 'CG', 'ASP', 12.4), ('OG', 'SER', 'OD1', 'ASP', 11.31), ('OG', 'SER', 'OD2', 'ASP', 12.65)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MN_MN, d, 'M_1o98_5_4_2_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_MN, d, 'M_1o98_5_4_2_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_ARG, d, 'M_1o98_5_4_2_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_MN, d, 'M_1o98_5_4_2_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ARG_MN, d, 'M_1o98_5_4_2_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(SER_ARG, d, 'M_1o98_5_4_2_1')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(SER_ASP, d, 'M_1o98_5_4_2_1')
	if match7 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MN_MN' :  match1,
		'SER_MN' :  match2,
		'ASP_ARG' :  match3,
		'ASP_MN' :  match4,
		'ARG_MN' :  match5,
		'SER_ARG' :  match6,
		'SER_ASP' :  match7}