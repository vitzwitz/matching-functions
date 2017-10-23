'''
FUNC:M_1uaq_3_5_4_1
PDB:1uaq
EC:3.5.4.1
RESI:glu,ser,cys,zn
LOCI:a-64,89,91,200;
'''
import motifFunctions as cmd
GLU_CYS = { 
	'distances':
		[[10.25, 9.38], [9.84, 9.3], [8.63, 8.24], [8.85, 8.42], [7.67, 7.49]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYS', 10.25), ('CB', 'GLU', 'SG', 'CYS', 9.38)], [('CG', 'GLU', 'CB', 'CYS', 9.84), ('CG', 'GLU', 'SG', 'CYS', 9.3)], [('CD', 'GLU', 'CB', 'CYS', 8.63), ('CD', 'GLU', 'SG', 'CYS', 8.24)], [('OE1', 'GLU', 'CB', 'CYS', 8.85), ('OE1', 'GLU', 'SG', 'CYS', 8.42)], [('OE2', 'GLU', 'CB', 'CYS', 7.67), ('OE2', 'GLU', 'SG', 'CYS', 7.49)]]}
CYS_ZN = { 
	'distances':
		[[5.34], [4.35]],
	'comparisons':
		[[('CB', 'CYS', 'ZN', 'ZN', 5.34)], [('SG', 'CYS', 'ZN', 'ZN', 4.35)]]}
CYS_SER = { 
	'distances':
		[[10.11, 10.29], [11.43, 11.58]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'SER', 10.11), ('CB', 'CYS', 'OG', 'SER', 10.29)], [('SG', 'CYS', 'CB', 'SER', 11.43), ('SG', 'CYS', 'OG', 'SER', 11.58)]]}
GLU_ZN = { 
	'distances':
		[[7.5], [7.44], [6.28], [6.23], [5.85]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 7.5)], [('CG', 'GLU', 'ZN', 'ZN', 7.44)], [('CD', 'GLU', 'ZN', 'ZN', 6.28)], [('OE1', 'GLU', 'ZN', 'ZN', 6.23)], [('OE2', 'GLU', 'ZN', 'ZN', 5.85)]]}
SER_ZN = { 
	'distances':
		[[11.24], [11.62]],
	'comparisons':
		[[('CB', 'SER', 'ZN', 'ZN', 11.24)], [('OG', 'SER', 'ZN', 'ZN', 11.62)]]}
GLU_SER = { 
	'distances':
		[[12.36, 12.64], [10.92, 11.27], [10.13, 10.6], [10.7, 11.32], [9.15, 9.56]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 12.36), ('CB', 'GLU', 'OG', 'SER', 12.64)], [('CG', 'GLU', 'CB', 'SER', 10.92), ('CG', 'GLU', 'OG', 'SER', 11.27)], [('CD', 'GLU', 'CB', 'SER', 10.13), ('CD', 'GLU', 'OG', 'SER', 10.6)], [('OE1', 'GLU', 'CB', 'SER', 10.7), ('OE1', 'GLU', 'OG', 'SER', 11.32)], [('OE2', 'GLU', 'CB', 'SER', 9.15), ('OE2', 'GLU', 'OG', 'SER', 9.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_CYS, d, 'M_1uaq_3_5_4_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_ZN, d, 'M_1uaq_3_5_4_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(CYS_SER, d, 'M_1uaq_3_5_4_1')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_ZN, d, 'M_1uaq_3_5_4_1')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_ZN, d, 'M_1uaq_3_5_4_1')
	if match5 == []:
		 flag = True
		 break
	match6 , totTime6 = cmd.detect(GLU_SER, d, 'M_1uaq_3_5_4_1')
	if match6 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_CYS' :  match1,
		'CYS_ZN' :  match2,
		'CYS_SER' :  match3,
		'GLU_ZN' :  match4,
		'SER_ZN' :  match5,
		'GLU_SER' :  match6}