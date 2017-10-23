'''
FUNC:Pfa_1pzp_3_5_2_6
PDB:1pzp
EC:3.5.2.6
RESI:ser,lys,ser,glu
LOCI:a-70,73,130,166;
'''
import motifFunctions as cmd
LYS_GLU = { 
	'distances':
		[[11.25, 9.76, 9.5, 10.56, 8.42], [9.71, 8.24, 7.99, 9.07, 6.95], [9.43, 8.04, 7.66, 8.63, 6.66], [7.94, 6.57, 6.15, 7.12, 5.23], [7.92, 6.76, 6.11, 6.8, 5.35]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 11.25), ('CB', 'LYS', 'CG', 'GLU', 9.76), ('CB', 'LYS', 'CD', 'GLU', 9.5), ('CB', 'LYS', 'OE1', 'GLU', 10.56), ('CB', 'LYS', 'OE2', 'GLU', 8.42)], [('CG', 'LYS', 'CB', 'GLU', 9.71), ('CG', 'LYS', 'CG', 'GLU', 8.24), ('CG', 'LYS', 'CD', 'GLU', 7.99), ('CG', 'LYS', 'OE1', 'GLU', 9.07), ('CG', 'LYS', 'OE2', 'GLU', 6.95)], [('CD', 'LYS', 'CB', 'GLU', 9.43), ('CD', 'LYS', 'CG', 'GLU', 8.04), ('CD', 'LYS', 'CD', 'GLU', 7.66), ('CD', 'LYS', 'OE1', 'GLU', 8.63), ('CD', 'LYS', 'OE2', 'GLU', 6.66)], [('CE', 'LYS', 'CB', 'GLU', 7.94), ('CE', 'LYS', 'CG', 'GLU', 6.57), ('CE', 'LYS', 'CD', 'GLU', 6.15), ('CE', 'LYS', 'OE1', 'GLU', 7.12), ('CE', 'LYS', 'OE2', 'GLU', 5.23)], [('NZ', 'LYS', 'CB', 'GLU', 7.92), ('NZ', 'LYS', 'CG', 'GLU', 6.76), ('NZ', 'LYS', 'CD', 'GLU', 6.11), ('NZ', 'LYS', 'OE1', 'GLU', 6.8), ('NZ', 'LYS', 'OE2', 'GLU', 5.35)]]}
SER_LYS = { 
	'distances':
		[[7.3, 6.71, 5.95, 5.95, 5.58], [7.82, 6.89, 5.93, 5.41, 4.66], [8.94, 8.47, 7.0, 7.2, 6.17], [8.12, 7.59, 6.19, 6.35, 5.38]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 7.3), ('CB', 'SER', 'CG', 'LYS', 6.71), ('CB', 'SER', 'CD', 'LYS', 5.95), ('CB', 'SER', 'CE', 'LYS', 5.95), ('CB', 'SER', 'NZ', 'LYS', 5.58)], [('OG', 'SER', 'CB', 'LYS', 7.82), ('OG', 'SER', 'CG', 'LYS', 6.89), ('OG', 'SER', 'CD', 'LYS', 5.93), ('OG', 'SER', 'CE', 'LYS', 5.41), ('OG', 'SER', 'NZ', 'LYS', 4.66)], [('CB', 'SER', 'CB', 'LYS', 8.94), ('CB', 'SER', 'CG', 'LYS', 8.47), ('CB', 'SER', 'CD', 'LYS', 7.0), ('CB', 'SER', 'CE', 'LYS', 7.2), ('CB', 'SER', 'NZ', 'LYS', 6.17)], [('OG', 'SER', 'CB', 'LYS', 8.12), ('OG', 'SER', 'CG', 'LYS', 7.59), ('OG', 'SER', 'CD', 'LYS', 6.19), ('OG', 'SER', 'CE', 'LYS', 6.35), ('OG', 'SER', 'NZ', 'LYS', 5.38)]]}
GLU_SERI = { 
	'distances':
		[[11.68, 11.07], [10.76, 10.04], [10.01, 9.15], [10.37, 9.52], [9.32, 8.33]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SERI', 11.68), ('CB', 'GLU', 'OG', 'SERI', 11.07)], [('CG', 'GLU', 'CB', 'SERI', 10.76), ('CG', 'GLU', 'OG', 'SERI', 10.04)], [('CD', 'GLU', 'CB', 'SERI', 10.01), ('CD', 'GLU', 'OG', 'SERI', 9.15)], [('OE1', 'GLU', 'CB', 'SERI', 10.37), ('OE1', 'GLU', 'OG', 'SERI', 9.52)], [('OE2', 'GLU', 'CB', 'SERI', 9.32), ('OE2', 'GLU', 'OG', 'SERI', 8.33)]]}
SER_SER = { 
	'distances':
		[[6.58, 5.17], [6.35, 5.03], [6.58, 6.35], [5.17, 5.03]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'SER', 6.58), ('CB', 'SER', 'OG', 'SER', 5.17)], [('OG', 'SER', 'CB', 'SER', 6.35), ('OG', 'SER', 'OG', 'SER', 5.03)], [('CB', 'SER', 'CB', 'SER', 6.58), ('CB', 'SER', 'OG', 'SER', 6.35)], [('OG', 'SER', 'CB', 'SER', 5.17), ('OG', 'SER', 'OG', 'SER', 5.03)]]}
SER_GLU = { 
	'distances':
		[[10.46, 9.23, 8.06, 8.43, 6.97], [9.28, 8.16, 6.94, 7.22, 5.98], [11.68, 10.76, 10.01, 10.37, 9.32], [11.07, 10.04, 9.15, 9.52, 8.33]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 10.46), ('CB', 'SER', 'CG', 'GLU', 9.23), ('CB', 'SER', 'CD', 'GLU', 8.06), ('CB', 'SER', 'OE1', 'GLU', 8.43), ('CB', 'SER', 'OE2', 'GLU', 6.97)], [('OG', 'SER', 'CB', 'GLU', 9.28), ('OG', 'SER', 'CG', 'GLU', 8.16), ('OG', 'SER', 'CD', 'GLU', 6.94), ('OG', 'SER', 'OE1', 'GLU', 7.22), ('OG', 'SER', 'OE2', 'GLU', 5.98)], [('CB', 'SER', 'CB', 'GLU', 11.68), ('CB', 'SER', 'CG', 'GLU', 10.76), ('CB', 'SER', 'CD', 'GLU', 10.01), ('CB', 'SER', 'OE1', 'GLU', 10.37), ('CB', 'SER', 'OE2', 'GLU', 9.32)], [('OG', 'SER', 'CB', 'GLU', 11.07), ('OG', 'SER', 'CG', 'GLU', 10.04), ('OG', 'SER', 'CD', 'GLU', 9.15), ('OG', 'SER', 'OE1', 'GLU', 9.52), ('OG', 'SER', 'OE2', 'GLU', 8.33)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_GLU, d, 'Pfa_1pzp_3_5_2_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_LYS, d, 'Pfa_1pzp_3_5_2_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_SERI, d, 'Pfa_1pzp_3_5_2_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_SER, d, 'Pfa_1pzp_3_5_2_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_GLU, d, 'Pfa_1pzp_3_5_2_6')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_GLU' :  match1,
		'SER_LYS' :  match2,
		'GLU_SERI' :  match3,
		'SER_SER' :  match4,
		'SER_GLU' :  match5}