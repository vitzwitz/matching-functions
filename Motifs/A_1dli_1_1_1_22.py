'''
FUNC:A_1dli_1_1_1_22
PDB:1dli
EC:1.1.1.22
RESI:thr,glu,lys,asn,cys,asp
LOCI:a-118,145,204,208,260,264;
'''
import motifFunctions as cmd
ASN_LYS = { 
	'distances':
		[[8.57, 7.73, 7.63, 6.61, 6.95], [8.23, 7.25, 6.79, 5.69, 5.69], [8.44, 7.61, 6.92, 5.58, 5.32], [8.14, 6.92, 6.41, 5.63, 5.52]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'LYS', 8.57), ('CB', 'ASN', 'CG', 'LYS', 7.73), ('CB', 'ASN', 'CD', 'LYS', 7.63), ('CB', 'ASN', 'CE', 'LYS', 6.61), ('CB', 'ASN', 'NZ', 'LYS', 6.95)], [('CG', 'ASN', 'CB', 'LYS', 8.23), ('CG', 'ASN', 'CG', 'LYS', 7.25), ('CG', 'ASN', 'CD', 'LYS', 6.79), ('CG', 'ASN', 'CE', 'LYS', 5.69), ('CG', 'ASN', 'NZ', 'LYS', 5.69)], [('OD1', 'ASN', 'CB', 'LYS', 8.44), ('OD1', 'ASN', 'CG', 'LYS', 7.61), ('OD1', 'ASN', 'CD', 'LYS', 6.92), ('OD1', 'ASN', 'CE', 'LYS', 5.58), ('OD1', 'ASN', 'NZ', 'LYS', 5.32)], [('ND2', 'ASN', 'CB', 'LYS', 8.14), ('ND2', 'ASN', 'CG', 'LYS', 6.92), ('ND2', 'ASN', 'CD', 'LYS', 6.41), ('ND2', 'ASN', 'CE', 'LYS', 5.63), ('ND2', 'ASN', 'NZ', 'LYS', 5.52)]]}
ASN_GLU = { 
	'distances':
		[[15.08, 14.02, 14.19, 15.12, 13.54], [13.88, 12.82, 13.09, 14.08, 12.47], [13.59, 12.64, 13.06, 14.05, 12.57], [13.29, 12.13, 12.32, 13.35, 11.61]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 15.08), ('CB', 'ASN', 'CG', 'GLU', 14.02), ('CB', 'ASN', 'CD', 'GLU', 14.19), ('CB', 'ASN', 'OE1', 'GLU', 15.12), ('CB', 'ASN', 'OE2', 'GLU', 13.54)], [('CG', 'ASN', 'CB', 'GLU', 13.88), ('CG', 'ASN', 'CG', 'GLU', 12.82), ('CG', 'ASN', 'CD', 'GLU', 13.09), ('CG', 'ASN', 'OE1', 'GLU', 14.08), ('CG', 'ASN', 'OE2', 'GLU', 12.47)], [('OD1', 'ASN', 'CB', 'GLU', 13.59), ('OD1', 'ASN', 'CG', 'GLU', 12.64), ('OD1', 'ASN', 'CD', 'GLU', 13.06), ('OD1', 'ASN', 'OE1', 'GLU', 14.05), ('OD1', 'ASN', 'OE2', 'GLU', 12.57)], [('ND2', 'ASN', 'CB', 'GLU', 13.29), ('ND2', 'ASN', 'CG', 'GLU', 12.13), ('ND2', 'ASN', 'CD', 'GLU', 12.32), ('ND2', 'ASN', 'OE1', 'GLU', 13.35), ('ND2', 'ASN', 'OE2', 'GLU', 11.61)]]}
ASP_THR = { 
	'distances':
		[[8.06, 8.24, 6.99], [6.75, 6.91, 5.91], [6.31, 6.78, 5.53], [6.52, 6.3, 5.93]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'THR', 8.06), ('CB', 'ASP', 'OG1', 'THR', 8.24), ('CB', 'ASP', 'CG2', 'THR', 6.99)], [('CG', 'ASP', 'CB', 'THR', 6.75), ('CG', 'ASP', 'OG1', 'THR', 6.91), ('CG', 'ASP', 'CG2', 'THR', 5.91)], [('OD1', 'ASP', 'CB', 'THR', 6.31), ('OD1', 'ASP', 'OG1', 'THR', 6.78), ('OD1', 'ASP', 'CG2', 'THR', 5.53)], [('OD2', 'ASP', 'CB', 'THR', 6.52), ('OD2', 'ASP', 'OG1', 'THR', 6.3), ('OD2', 'ASP', 'CG2', 'THR', 5.93)]]}
ASP_CYS = { 
	'distances':
		[[7.34, 8.57], [6.42, 7.35], [6.84, 7.5], [5.68, 6.55]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'CYS', 7.34), ('CB', 'ASP', 'SG', 'CYS', 8.57)], [('CG', 'ASP', 'CB', 'CYS', 6.42), ('CG', 'ASP', 'SG', 'CYS', 7.35)], [('OD1', 'ASP', 'CB', 'CYS', 6.84), ('OD1', 'ASP', 'SG', 'CYS', 7.5)], [('OD2', 'ASP', 'CB', 'CYS', 5.68), ('OD2', 'ASP', 'SG', 'CYS', 6.55)]]}
ASP_GLU = { 
	'distances':
		[[16.04, 14.72, 14.49, 15.39, 13.52], [15.07, 13.7, 13.49, 14.46, 12.49], [15.34, 13.91, 13.61, 14.57, 12.52], [14.17, 12.83, 12.75, 13.77, 11.81]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 16.04), ('CB', 'ASP', 'CG', 'GLU', 14.72), ('CB', 'ASP', 'CD', 'GLU', 14.49), ('CB', 'ASP', 'OE1', 'GLU', 15.39), ('CB', 'ASP', 'OE2', 'GLU', 13.52)], [('CG', 'ASP', 'CB', 'GLU', 15.07), ('CG', 'ASP', 'CG', 'GLU', 13.7), ('CG', 'ASP', 'CD', 'GLU', 13.49), ('CG', 'ASP', 'OE1', 'GLU', 14.46), ('CG', 'ASP', 'OE2', 'GLU', 12.49)], [('OD1', 'ASP', 'CB', 'GLU', 15.34), ('OD1', 'ASP', 'CG', 'GLU', 13.91), ('OD1', 'ASP', 'CD', 'GLU', 13.61), ('OD1', 'ASP', 'OE1', 'GLU', 14.57), ('OD1', 'ASP', 'OE2', 'GLU', 12.52)], [('OD2', 'ASP', 'CB', 'GLU', 14.17), ('OD2', 'ASP', 'CG', 'GLU', 12.83), ('OD2', 'ASP', 'CD', 'GLU', 12.75), ('OD2', 'ASP', 'OE1', 'GLU', 13.77), ('OD2', 'ASP', 'OE2', 'GLU', 11.81)]]}
CYS_THR = { 
	'distances':
		[[8.67, 8.08, 8.81], [8.19, 7.5, 8.74]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'THR', 8.67), ('CB', 'CYS', 'OG1', 'THR', 8.08), ('CB', 'CYS', 'CG2', 'THR', 8.81)], [('SG', 'CYS', 'CB', 'THR', 8.19), ('SG', 'CYS', 'OG1', 'THR', 7.5), ('SG', 'CYS', 'CG2', 'THR', 8.74)]]}
ASN_CYS = { 
	'distances':
		[[7.61, 8.95], [6.77, 7.9], [7.36, 8.33], [5.72, 6.74]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'CYS', 7.61), ('CB', 'ASN', 'SG', 'CYS', 8.95)], [('CG', 'ASN', 'CB', 'CYS', 6.77), ('CG', 'ASN', 'SG', 'CYS', 7.9)], [('OD1', 'ASN', 'CB', 'CYS', 7.36), ('OD1', 'ASN', 'SG', 'CYS', 8.33)], [('ND2', 'ASN', 'CB', 'CYS', 5.72), ('ND2', 'ASN', 'SG', 'CYS', 6.74)]]}
THR_LYS = { 
	'distances':
		[[7.48, 6.23, 6.47, 7.65, 8.08], [6.99, 5.65, 5.43, 6.56, 6.8], [6.97, 5.77, 6.43, 7.49, 8.2]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'LYS', 7.48), ('CB', 'THR', 'CG', 'LYS', 6.23), ('CB', 'THR', 'CD', 'LYS', 6.47), ('CB', 'THR', 'CE', 'LYS', 7.65), ('CB', 'THR', 'NZ', 'LYS', 8.08)], [('OG1', 'THR', 'CB', 'LYS', 6.99), ('OG1', 'THR', 'CG', 'LYS', 5.65), ('OG1', 'THR', 'CD', 'LYS', 5.43), ('OG1', 'THR', 'CE', 'LYS', 6.56), ('OG1', 'THR', 'NZ', 'LYS', 6.8)], [('CG2', 'THR', 'CB', 'LYS', 6.97), ('CG2', 'THR', 'CG', 'LYS', 5.77), ('CG2', 'THR', 'CD', 'LYS', 6.43), ('CG2', 'THR', 'CE', 'LYS', 7.49), ('CG2', 'THR', 'NZ', 'LYS', 8.2)]]}
CYS_LYS = { 
	'distances':
		[[11.12, 9.65, 8.99, 8.65, 8.0], [11.25, 9.76, 8.94, 8.85, 8.04]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'LYS', 11.12), ('CB', 'CYS', 'CG', 'LYS', 9.65), ('CB', 'CYS', 'CD', 'LYS', 8.99), ('CB', 'CYS', 'CE', 'LYS', 8.65), ('CB', 'CYS', 'NZ', 'LYS', 8.0)], [('SG', 'CYS', 'CB', 'LYS', 11.25), ('SG', 'CYS', 'CG', 'LYS', 9.76), ('SG', 'CYS', 'CD', 'LYS', 8.94), ('SG', 'CYS', 'CE', 'LYS', 8.85), ('SG', 'CYS', 'NZ', 'LYS', 8.04)]]}
ASN_THR = { 
	'distances':
		[[9.76, 9.18, 9.0], [9.15, 8.35, 8.66], [9.85, 8.89, 9.49], [8.08, 7.31, 7.71]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'THR', 9.76), ('CB', 'ASN', 'OG1', 'THR', 9.18), ('CB', 'ASN', 'CG2', 'THR', 9.0)], [('CG', 'ASN', 'CB', 'THR', 9.15), ('CG', 'ASN', 'OG1', 'THR', 8.35), ('CG', 'ASN', 'CG2', 'THR', 8.66)], [('OD1', 'ASN', 'CB', 'THR', 9.85), ('OD1', 'ASN', 'OG1', 'THR', 8.89), ('OD1', 'ASN', 'CG2', 'THR', 9.49)], [('ND2', 'ASN', 'CB', 'THR', 8.08), ('ND2', 'ASN', 'OG1', 'THR', 7.31), ('ND2', 'ASN', 'CG2', 'THR', 7.71)]]}
ASN_ASP = { 
	'distances':
		[[6.06, 6.49, 7.74, 5.91], [6.6, 6.54, 7.72, 5.6], [7.82, 7.7, 8.85, 6.68], [6.05, 5.61, 6.7, 4.51]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'ASP', 6.06), ('CB', 'ASN', 'CG', 'ASP', 6.49), ('CB', 'ASN', 'OD1', 'ASP', 7.74), ('CB', 'ASN', 'OD2', 'ASP', 5.91)], [('CG', 'ASN', 'CB', 'ASP', 6.6), ('CG', 'ASN', 'CG', 'ASP', 6.54), ('CG', 'ASN', 'OD1', 'ASP', 7.72), ('CG', 'ASN', 'OD2', 'ASP', 5.6)], [('OD1', 'ASN', 'CB', 'ASP', 7.82), ('OD1', 'ASN', 'CG', 'ASP', 7.7), ('OD1', 'ASN', 'OD1', 'ASP', 8.85), ('OD1', 'ASN', 'OD2', 'ASP', 6.68)], [('ND2', 'ASN', 'CB', 'ASP', 6.05), ('ND2', 'ASN', 'CG', 'ASP', 5.61), ('ND2', 'ASN', 'OD1', 'ASP', 6.7), ('ND2', 'ASN', 'OD2', 'ASP', 4.51)]]}
ASP_LYS = { 
	'distances':
		[[9.25, 8.1, 8.57, 8.45, 9.01], [8.82, 7.48, 7.77, 7.86, 8.27], [9.32, 7.97, 8.33, 8.66, 9.07], [8.29, 6.87, 6.88, 6.84, 7.1]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'LYS', 9.25), ('CB', 'ASP', 'CG', 'LYS', 8.1), ('CB', 'ASP', 'CD', 'LYS', 8.57), ('CB', 'ASP', 'CE', 'LYS', 8.45), ('CB', 'ASP', 'NZ', 'LYS', 9.01)], [('CG', 'ASP', 'CB', 'LYS', 8.82), ('CG', 'ASP', 'CG', 'LYS', 7.48), ('CG', 'ASP', 'CD', 'LYS', 7.77), ('CG', 'ASP', 'CE', 'LYS', 7.86), ('CG', 'ASP', 'NZ', 'LYS', 8.27)], [('OD1', 'ASP', 'CB', 'LYS', 9.32), ('OD1', 'ASP', 'CG', 'LYS', 7.97), ('OD1', 'ASP', 'CD', 'LYS', 8.33), ('OD1', 'ASP', 'CE', 'LYS', 8.66), ('OD1', 'ASP', 'NZ', 'LYS', 9.07)], [('OD2', 'ASP', 'CB', 'LYS', 8.29), ('OD2', 'ASP', 'CG', 'LYS', 6.87), ('OD2', 'ASP', 'CD', 'LYS', 6.88), ('OD2', 'ASP', 'CE', 'LYS', 6.84), ('OD2', 'ASP', 'NZ', 'LYS', 7.1)]]}
LYS_GLU = { 
	'distances':
		[[17.81, 16.64, 17.1, 18.29, 16.35], [16.56, 15.34, 15.72, 16.91, 14.93], [15.27, 14.11, 14.59, 15.8, 13.88], [14.81, 13.73, 14.27, 15.44, 13.65], [13.42, 12.39, 13.02, 14.19, 12.48]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 17.81), ('CB', 'LYS', 'CG', 'GLU', 16.64), ('CB', 'LYS', 'CD', 'GLU', 17.1), ('CB', 'LYS', 'OE1', 'GLU', 18.29), ('CB', 'LYS', 'OE2', 'GLU', 16.35)], [('CG', 'LYS', 'CB', 'GLU', 16.56), ('CG', 'LYS', 'CG', 'GLU', 15.34), ('CG', 'LYS', 'CD', 'GLU', 15.72), ('CG', 'LYS', 'OE1', 'GLU', 16.91), ('CG', 'LYS', 'OE2', 'GLU', 14.93)], [('CD', 'LYS', 'CB', 'GLU', 15.27), ('CD', 'LYS', 'CG', 'GLU', 14.11), ('CD', 'LYS', 'CD', 'GLU', 14.59), ('CD', 'LYS', 'OE1', 'GLU', 15.8), ('CD', 'LYS', 'OE2', 'GLU', 13.88)], [('CE', 'LYS', 'CB', 'GLU', 14.81), ('CE', 'LYS', 'CG', 'GLU', 13.73), ('CE', 'LYS', 'CD', 'GLU', 14.27), ('CE', 'LYS', 'OE1', 'GLU', 15.44), ('CE', 'LYS', 'OE2', 'GLU', 13.65)], [('NZ', 'LYS', 'CB', 'GLU', 13.42), ('NZ', 'LYS', 'CG', 'GLU', 12.39), ('NZ', 'LYS', 'CD', 'GLU', 13.02), ('NZ', 'LYS', 'OE1', 'GLU', 14.19), ('NZ', 'LYS', 'OE2', 'GLU', 12.48)]]}
CYS_GLU = { 
	'distances':
		[[10.72, 9.38, 9.18, 10.15, 8.29], [9.89, 8.46, 8.35, 9.45, 7.38]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 10.72), ('CB', 'CYS', 'CG', 'GLU', 9.38), ('CB', 'CYS', 'CD', 'GLU', 9.18), ('CB', 'CYS', 'OE1', 'GLU', 10.15), ('CB', 'CYS', 'OE2', 'GLU', 8.29)], [('SG', 'CYS', 'CB', 'GLU', 9.89), ('SG', 'CYS', 'CG', 'GLU', 8.46), ('SG', 'CYS', 'CD', 'GLU', 8.35), ('SG', 'CYS', 'OE1', 'GLU', 9.45), ('SG', 'CYS', 'OE2', 'GLU', 7.38)]]}
THR_GLU = { 
	'distances':
		[[15.53, 14.11, 14.17, 15.33, 13.15], [14.56, 13.19, 13.39, 14.59, 12.46], [16.37, 14.95, 14.96, 16.09, 13.93]],
	'comparisons':
		[[('CB', 'THR', 'CB', 'GLU', 15.53), ('CB', 'THR', 'CG', 'GLU', 14.11), ('CB', 'THR', 'CD', 'GLU', 14.17), ('CB', 'THR', 'OE1', 'GLU', 15.33), ('CB', 'THR', 'OE2', 'GLU', 13.15)], [('OG1', 'THR', 'CB', 'GLU', 14.56), ('OG1', 'THR', 'CG', 'GLU', 13.19), ('OG1', 'THR', 'CD', 'GLU', 13.39), ('OG1', 'THR', 'OE1', 'GLU', 14.59), ('OG1', 'THR', 'OE2', 'GLU', 12.46)], [('CG2', 'THR', 'CB', 'GLU', 16.37), ('CG2', 'THR', 'CG', 'GLU', 14.95), ('CG2', 'THR', 'CD', 'GLU', 14.96), ('CG2', 'THR', 'OE1', 'GLU', 16.09), ('CG2', 'THR', 'OE2', 'GLU', 13.93)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASN_LYS, d, 'A_1dli_1_1_1_22')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ASN_GLU, d, 'A_1dli_1_1_1_22')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_THR, d, 'A_1dli_1_1_1_22')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ASP_CYS, d, 'A_1dli_1_1_1_22')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASP_GLU, d, 'A_1dli_1_1_1_22')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(CYS_THR, d, 'A_1dli_1_1_1_22')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASN_CYS, d, 'A_1dli_1_1_1_22')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(THR_LYS, d, 'A_1dli_1_1_1_22')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(CYS_LYS, d, 'A_1dli_1_1_1_22')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(ASN_THR, d, 'A_1dli_1_1_1_22')
	if match10 == []:
		 flag = True
		 break
	match11 , totTime11 = cmd.detect(ASN_ASP, d, 'A_1dli_1_1_1_22')
	if match11 == []:
		 flag = True
		 break
	match12 , totTime12 = cmd.detect(ASP_LYS, d, 'A_1dli_1_1_1_22')
	if match12 == []:
		 flag = True
		 break
	match13 , totTime13 = cmd.detect(LYS_GLU, d, 'A_1dli_1_1_1_22')
	if match13 == []:
		 flag = True
		 break
	match14 , totTime14 = cmd.detect(CYS_GLU, d, 'A_1dli_1_1_1_22')
	if match14 == []:
		 flag = True
		 break
	match15 , totTime15 = cmd.detect(THR_GLU, d, 'A_1dli_1_1_1_22')
	if match15 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASN_LYS' :  match1,
		'ASN_GLU' :  match2,
		'ASP_THR' :  match3,
		'ASP_CYS' :  match4,
		'ASP_GLU' :  match5,
		'CYS_THR' :  match6,
		'ASN_CYS' :  match7,
		'THR_LYS' :  match8,
		'CYS_LYS' :  match9,
		'ASN_THR' :  match10,
		'ASN_ASP' :  match11,
		'ASP_LYS' :  match12,
		'LYS_GLU' :  match13,
		'CYS_GLU' :  match14,
		'THR_GLU' :  match15}