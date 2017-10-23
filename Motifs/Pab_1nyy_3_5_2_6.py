'''
FUNC:Pab_1nyy_3_5_2_6
PDB:1nyy
EC:3.5.2.6
RESI:ser,lys,ser,glu
LOCI:a-70,73,130,166;
'''
import motifFunctions as cmd
LYS_GLU = { 
	'distances':
		[[11.36, 9.86, 9.59, 10.64, 8.5], [9.88, 8.39, 8.07, 9.12, 6.99], [9.63, 8.21, 7.79, 8.71, 6.78], [8.21, 6.83, 6.34, 7.23, 5.42], [8.33, 7.17, 6.51, 7.11, 5.8]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 11.36), ('CB', 'LYS', 'CG', 'GLU', 9.86), ('CB', 'LYS', 'CD', 'GLU', 9.59), ('CB', 'LYS', 'OE1', 'GLU', 10.64), ('CB', 'LYS', 'OE2', 'GLU', 8.5)], [('CG', 'LYS', 'CB', 'GLU', 9.88), ('CG', 'LYS', 'CG', 'GLU', 8.39), ('CG', 'LYS', 'CD', 'GLU', 8.07), ('CG', 'LYS', 'OE1', 'GLU', 9.12), ('CG', 'LYS', 'OE2', 'GLU', 6.99)], [('CD', 'LYS', 'CB', 'GLU', 9.63), ('CD', 'LYS', 'CG', 'GLU', 8.21), ('CD', 'LYS', 'CD', 'GLU', 7.79), ('CD', 'LYS', 'OE1', 'GLU', 8.71), ('CD', 'LYS', 'OE2', 'GLU', 6.78)], [('CE', 'LYS', 'CB', 'GLU', 8.21), ('CE', 'LYS', 'CG', 'GLU', 6.83), ('CE', 'LYS', 'CD', 'GLU', 6.34), ('CE', 'LYS', 'OE1', 'GLU', 7.23), ('CE', 'LYS', 'OE2', 'GLU', 5.42)], [('NZ', 'LYS', 'CB', 'GLU', 8.33), ('NZ', 'LYS', 'CG', 'GLU', 7.17), ('NZ', 'LYS', 'CD', 'GLU', 6.51), ('NZ', 'LYS', 'OE1', 'GLU', 7.11), ('NZ', 'LYS', 'OE2', 'GLU', 5.8)]]}
SER_LYS = { 
	'distances':
		[[7.4, 6.6, 5.93, 5.83, 5.63], [8.01, 6.92, 6.05, 5.42, 4.86], [8.68, 8.18, 6.73, 6.89, 5.85], [8.08, 7.43, 6.04, 6.06, 5.05]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'LYS', 7.4), ('CB', 'SER', 'CG', 'LYS', 6.6), ('CB', 'SER', 'CD', 'LYS', 5.93), ('CB', 'SER', 'CE', 'LYS', 5.83), ('CB', 'SER', 'NZ', 'LYS', 5.63)], [('OG', 'SER', 'CB', 'LYS', 8.01), ('OG', 'SER', 'CG', 'LYS', 6.92), ('OG', 'SER', 'CD', 'LYS', 6.05), ('OG', 'SER', 'CE', 'LYS', 5.42), ('OG', 'SER', 'NZ', 'LYS', 4.86)], [('CB', 'SER', 'CB', 'LYS', 8.68), ('CB', 'SER', 'CG', 'LYS', 8.18), ('CB', 'SER', 'CD', 'LYS', 6.73), ('CB', 'SER', 'CE', 'LYS', 6.89), ('CB', 'SER', 'NZ', 'LYS', 5.85)], [('OG', 'SER', 'CB', 'LYS', 8.08), ('OG', 'SER', 'CG', 'LYS', 7.43), ('OG', 'SER', 'CD', 'LYS', 6.04), ('OG', 'SER', 'CE', 'LYS', 6.06), ('OG', 'SER', 'NZ', 'LYS', 5.05)]]}
GLU_SERI = { 
	'distances':
		[[11.94, 11.2], [10.94, 10.12], [10.22, 9.25], [10.56, 9.57], [9.54, 8.47]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SERI', 11.94), ('CB', 'GLU', 'OG', 'SERI', 11.2)], [('CG', 'GLU', 'CB', 'SERI', 10.94), ('CG', 'GLU', 'OG', 'SERI', 10.12)], [('CD', 'GLU', 'CB', 'SERI', 10.22), ('CD', 'GLU', 'OG', 'SERI', 9.25)], [('OE1', 'GLU', 'CB', 'SERI', 10.56), ('OE1', 'GLU', 'OG', 'SERI', 9.57)], [('OE2', 'GLU', 'CB', 'SERI', 9.54), ('OE2', 'GLU', 'OG', 'SERI', 8.47)]]}
SER_SER = { 
	'distances':
		[[6.65, 5.25], [6.53, 5.14], [6.65, 6.53], [5.25, 5.14]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'SER', 6.65), ('CB', 'SER', 'OG', 'SER', 5.25)], [('OG', 'SER', 'CB', 'SER', 6.53), ('OG', 'SER', 'OG', 'SER', 5.14)], [('CB', 'SER', 'CB', 'SER', 6.65), ('CB', 'SER', 'OG', 'SER', 6.53)], [('OG', 'SER', 'CB', 'SER', 5.25), ('OG', 'SER', 'OG', 'SER', 5.14)]]}
SER_GLU = { 
	'distances':
		[[10.63, 9.38, 8.2, 8.54, 7.14], [9.5, 8.38, 7.14, 7.35, 6.23], [11.94, 10.94, 10.22, 10.56, 9.54], [11.2, 10.12, 9.25, 9.57, 8.47]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'GLU', 10.63), ('CB', 'SER', 'CG', 'GLU', 9.38), ('CB', 'SER', 'CD', 'GLU', 8.2), ('CB', 'SER', 'OE1', 'GLU', 8.54), ('CB', 'SER', 'OE2', 'GLU', 7.14)], [('OG', 'SER', 'CB', 'GLU', 9.5), ('OG', 'SER', 'CG', 'GLU', 8.38), ('OG', 'SER', 'CD', 'GLU', 7.14), ('OG', 'SER', 'OE1', 'GLU', 7.35), ('OG', 'SER', 'OE2', 'GLU', 6.23)], [('CB', 'SER', 'CB', 'GLU', 11.94), ('CB', 'SER', 'CG', 'GLU', 10.94), ('CB', 'SER', 'CD', 'GLU', 10.22), ('CB', 'SER', 'OE1', 'GLU', 10.56), ('CB', 'SER', 'OE2', 'GLU', 9.54)], [('OG', 'SER', 'CB', 'GLU', 11.2), ('OG', 'SER', 'CG', 'GLU', 10.12), ('OG', 'SER', 'CD', 'GLU', 9.25), ('OG', 'SER', 'OE1', 'GLU', 9.57), ('OG', 'SER', 'OE2', 'GLU', 8.47)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_GLU, d, 'Pab_1nyy_3_5_2_6')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(SER_LYS, d, 'Pab_1nyy_3_5_2_6')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_SERI, d, 'Pab_1nyy_3_5_2_6')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_SER, d, 'Pab_1nyy_3_5_2_6')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_GLU, d, 'Pab_1nyy_3_5_2_6')
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