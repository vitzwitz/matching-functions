'''
FUNC:M_1b57_4_1_2_13
PDB:1b57
EC:4.1.2.13
RESI:asp,glu,asn,zn,na
LOCI:a-109,182,286,360,364;
'''
import motifFunctions as cmd
ASP_ZN = { 
	'distances':
		[[8.03], [6.58], [6.16], [6.21]],
	'comparisons':
		[[('CB', 'ASP', 'ZN', 'ZN', 8.03)], [('CG', 'ASP', 'ZN', 'ZN', 6.58)], [('OD1', 'ASP', 'ZN', 'ZN', 6.16)], [('OD2', 'ASP', 'ZN', 'ZN', 6.21)]]}
GLU_NA = { 
	'distances':
		[[14.86], [13.81], [14.35], [15.59], [13.62]],
	'comparisons':
		[[('CB', 'GLU', 'NA', 'NA', 14.86)], [('CG', 'GLU', 'NA', 'NA', 13.81)], [('CD', 'GLU', 'NA', 'NA', 14.35)], [('OE1', 'GLU', 'NA', 'NA', 15.59)], [('OE2', 'GLU', 'NA', 'NA', 13.62)]]}
ASN_GLU = { 
	'distances':
		[[14.29, 13.51, 13.42, 14.23, 12.65], [14.53, 13.9, 13.79, 14.5, 13.11], [15.67, 15.07, 14.91, 15.58, 14.24], [13.53, 13.02, 12.93, 13.59, 12.36]],
	'comparisons':
		[[('CB', 'ASN', 'CB', 'GLU', 14.29), ('CB', 'ASN', 'CG', 'GLU', 13.51), ('CB', 'ASN', 'CD', 'GLU', 13.42), ('CB', 'ASN', 'OE1', 'GLU', 14.23), ('CB', 'ASN', 'OE2', 'GLU', 12.65)], [('CG', 'ASN', 'CB', 'GLU', 14.53), ('CG', 'ASN', 'CG', 'GLU', 13.9), ('CG', 'ASN', 'CD', 'GLU', 13.79), ('CG', 'ASN', 'OE1', 'GLU', 14.5), ('CG', 'ASN', 'OE2', 'GLU', 13.11)], [('OD1', 'ASN', 'CB', 'GLU', 15.67), ('OD1', 'ASN', 'CG', 'GLU', 15.07), ('OD1', 'ASN', 'CD', 'GLU', 14.91), ('OD1', 'ASN', 'OE1', 'GLU', 15.58), ('OD1', 'ASN', 'OE2', 'GLU', 14.24)], [('ND2', 'ASN', 'CB', 'GLU', 13.53), ('ND2', 'ASN', 'CG', 'GLU', 13.02), ('ND2', 'ASN', 'CD', 'GLU', 12.93), ('ND2', 'ASN', 'OE1', 'GLU', 13.59), ('ND2', 'ASN', 'OE2', 'GLU', 12.36)]]}
ZN_NA = { 
	'distances':
		[10.62],
	'comparisons':
		[('ZN', 'ZN', 'NA', 'NA', 10.62)]}
ASN_NA = { 
	'distances':
		[[10.72], [12.06], [12.94], [12.39]],
	'comparisons':
		[[('CB', 'ASN', 'NA', 'NA', 10.72)], [('CG', 'ASN', 'NA', 'NA', 12.06)], [('OD1', 'ASN', 'NA', 'NA', 12.94)], [('ND2', 'ASN', 'NA', 'NA', 12.39)]]}
ASP_ASN = { 
	'distances':
		[[9.15, 8.4, 9.03, 7.24], [7.85, 7.17, 7.95, 5.95], [7.53, 6.65, 7.35, 5.34], [7.52, 7.16, 8.09, 6.05]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'ASN', 9.15), ('CB', 'ASP', 'CG', 'ASN', 8.4), ('CB', 'ASP', 'OD1', 'ASN', 9.03), ('CB', 'ASP', 'ND2', 'ASN', 7.24)], [('CG', 'ASP', 'CB', 'ASN', 7.85), ('CG', 'ASP', 'CG', 'ASN', 7.17), ('CG', 'ASP', 'OD1', 'ASN', 7.95), ('CG', 'ASP', 'ND2', 'ASN', 5.95)], [('OD1', 'ASP', 'CB', 'ASN', 7.53), ('OD1', 'ASP', 'CG', 'ASN', 6.65), ('OD1', 'ASP', 'OD1', 'ASN', 7.35), ('OD1', 'ASP', 'ND2', 'ASN', 5.34)], [('OD2', 'ASP', 'CB', 'ASN', 7.52), ('OD2', 'ASP', 'CG', 'ASN', 7.16), ('OD2', 'ASP', 'OD1', 'ASN', 8.09), ('OD2', 'ASP', 'ND2', 'ASN', 6.05)]]}
ASP_NA = { 
	'distances':
		[[15.65], [14.28], [14.24], [13.37]],
	'comparisons':
		[[('CB', 'ASP', 'NA', 'NA', 15.65)], [('CG', 'ASP', 'NA', 'NA', 14.28)], [('OD1', 'ASP', 'NA', 'NA', 14.24)], [('OD2', 'ASP', 'NA', 'NA', 13.37)]]}
ASN_ZN = { 
	'distances':
		[[6.9], [6.96], [8.06], [6.08]],
	'comparisons':
		[[('CB', 'ASN', 'ZN', 'ZN', 6.9)], [('CG', 'ASN', 'ZN', 'ZN', 6.96)], [('OD1', 'ASN', 'ZN', 'ZN', 8.06)], [('ND2', 'ASN', 'ZN', 'ZN', 6.08)]]}
ASP_GLU = { 
	'distances':
		[[10.85, 10.74, 10.31, 10.44, 10.1], [10.75, 10.52, 10.27, 10.62, 9.97], [11.52, 11.36, 11.25, 11.66, 10.99], [10.03, 9.64, 9.36, 9.81, 8.95]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 10.85), ('CB', 'ASP', 'CG', 'GLU', 10.74), ('CB', 'ASP', 'CD', 'GLU', 10.31), ('CB', 'ASP', 'OE1', 'GLU', 10.44), ('CB', 'ASP', 'OE2', 'GLU', 10.1)], [('CG', 'ASP', 'CB', 'GLU', 10.75), ('CG', 'ASP', 'CG', 'GLU', 10.52), ('CG', 'ASP', 'CD', 'GLU', 10.27), ('CG', 'ASP', 'OE1', 'GLU', 10.62), ('CG', 'ASP', 'OE2', 'GLU', 9.97)], [('OD1', 'ASP', 'CB', 'GLU', 11.52), ('OD1', 'ASP', 'CG', 'GLU', 11.36), ('OD1', 'ASP', 'CD', 'GLU', 11.25), ('OD1', 'ASP', 'OE1', 'GLU', 11.66), ('OD1', 'ASP', 'OE2', 'GLU', 10.99)], [('OD2', 'ASP', 'CB', 'GLU', 10.03), ('OD2', 'ASP', 'CG', 'GLU', 9.64), ('OD2', 'ASP', 'CD', 'GLU', 9.36), ('OD2', 'ASP', 'OE1', 'GLU', 9.81), ('OD2', 'ASP', 'OE2', 'GLU', 8.95)]]}
GLU_ZN = { 
	'distances':
		[[10.74], [10.38], [10.81], [11.66], [10.5]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 10.74)], [('CG', 'GLU', 'ZN', 'ZN', 10.38)], [('CD', 'GLU', 'ZN', 'ZN', 10.81)], [('OE1', 'GLU', 'ZN', 'ZN', 11.66)], [('OE2', 'GLU', 'ZN', 'ZN', 10.5)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ASP_ZN, d, 'M_1b57_4_1_2_13')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_NA, d, 'M_1b57_4_1_2_13')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASN_GLU, d, 'M_1b57_4_1_2_13')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(ZN_NA, d, 'M_1b57_4_1_2_13')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(ASN_NA, d, 'M_1b57_4_1_2_13')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(ASP_ASN, d, 'M_1b57_4_1_2_13')
	if match6 == []:
		 flag = True
		 break
	match7 , totTime7 = cmd.detect(ASP_NA, d, 'M_1b57_4_1_2_13')
	if match7 == []:
		 flag = True
		 break
	match8 , totTime8 = cmd.detect(ASN_ZN, d, 'M_1b57_4_1_2_13')
	if match8 == []:
		 flag = True
		 break
	match9 , totTime9 = cmd.detect(ASP_GLU, d, 'M_1b57_4_1_2_13')
	if match9 == []:
		 flag = True
		 break
	match10 , totTime10 = cmd.detect(GLU_ZN, d, 'M_1b57_4_1_2_13')
	if match10 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ASP_ZN' :  match1,
		'GLU_NA' :  match2,
		'ASN_GLU' :  match3,
		'ZN_NA' :  match4,
		'ASN_NA' :  match5,
		'ASP_ASN' :  match6,
		'ASP_NA' :  match7,
		'ASN_ZN' :  match8,
		'ASP_GLU' :  match9,
		'GLU_ZN' :  match10}