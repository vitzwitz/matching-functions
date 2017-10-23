'''
FUNC:M_1do6_1_15_1_2
PDB:1do6
EC:1.15.1.2
RESI:glu,lys,fe
LOCI:a-14,15,200;
'''
import motifFunctions as cmd
LYS_GLU = { 
	'distances':
		[[7.88, 7.71, 9.13, 10.06, 9.49], [8.14, 8.29, 9.78, 10.54, 10.34], [9.47, 9.7, 11.2, 11.96, 11.75], [9.6, 10.11, 11.63, 12.26, 12.3], [10.0, 10.52, 12.01, 12.69, 12.62]],
	'comparisons':
		[[('CB', 'LYS', 'CB', 'GLU', 7.88), ('CB', 'LYS', 'CG', 'GLU', 7.71), ('CB', 'LYS', 'CD', 'GLU', 9.13), ('CB', 'LYS', 'OE1', 'GLU', 10.06), ('CB', 'LYS', 'OE2', 'GLU', 9.49)], [('CG', 'LYS', 'CB', 'GLU', 8.14), ('CG', 'LYS', 'CG', 'GLU', 8.29), ('CG', 'LYS', 'CD', 'GLU', 9.78), ('CG', 'LYS', 'OE1', 'GLU', 10.54), ('CG', 'LYS', 'OE2', 'GLU', 10.34)], [('CD', 'LYS', 'CB', 'GLU', 9.47), ('CD', 'LYS', 'CG', 'GLU', 9.7), ('CD', 'LYS', 'CD', 'GLU', 11.2), ('CD', 'LYS', 'OE1', 'GLU', 11.96), ('CD', 'LYS', 'OE2', 'GLU', 11.75)], [('CE', 'LYS', 'CB', 'GLU', 9.6), ('CE', 'LYS', 'CG', 'GLU', 10.11), ('CE', 'LYS', 'CD', 'GLU', 11.63), ('CE', 'LYS', 'OE1', 'GLU', 12.26), ('CE', 'LYS', 'OE2', 'GLU', 12.3)], [('NZ', 'LYS', 'CB', 'GLU', 10.0), ('NZ', 'LYS', 'CG', 'GLU', 10.52), ('NZ', 'LYS', 'CD', 'GLU', 12.01), ('NZ', 'LYS', 'OE1', 'GLU', 12.69), ('NZ', 'LYS', 'OE2', 'GLU', 12.62)]]}
LYS_FE = { 
	'distances':
		[[10.52], [11.59], [12.92], [13.57], [13.75]],
	'comparisons':
		[[('CB', 'LYS', 'FE', 'FE', 10.52)], [('CG', 'LYS', 'FE', 'FE', 11.59)], [('CD', 'LYS', 'FE', 'FE', 12.92)], [('CE', 'LYS', 'FE', 'FE', 13.57)], [('NZ', 'LYS', 'FE', 'FE', 13.75)]]}
GLU_FE = { 
	'distances':
		[[7.5], [6.18], [5.22], [6.02], [4.01]],
	'comparisons':
		[[('CB', 'GLU', 'FE', 'FE', 7.5)], [('CG', 'GLU', 'FE', 'FE', 6.18)], [('CD', 'GLU', 'FE', 'FE', 5.22)], [('OE1', 'GLU', 'FE', 'FE', 6.02)], [('OE2', 'GLU', 'FE', 'FE', 4.01)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_GLU, d, 'M_1do6_1_15_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(LYS_FE, d, 'M_1do6_1_15_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_FE, d, 'M_1do6_1_15_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_GLU' :  match1,
		'LYS_FE' :  match2,
		'GLU_FE' :  match3}