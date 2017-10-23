'''
FUNC:A_1b5d_2_1_2_8
PDB:1b5d
EC:2.1.2.8
RESI:glu,cys,asp
LOCI:a-60,148,179;
'''
import motifFunctions as cmd
CYS_ASP = { 
	'distances':
		[[10.01, 8.82, 8.94, 8.0], [11.03, 9.7, 9.72, 8.82]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'ASP', 10.01), ('CB', 'CYS', 'CG', 'ASP', 8.82), ('CB', 'CYS', 'OD1', 'ASP', 8.94), ('CB', 'CYS', 'OD2', 'ASP', 8.0)], [('SG', 'CYS', 'CB', 'ASP', 11.03), ('SG', 'CYS', 'CG', 'ASP', 9.7), ('SG', 'CYS', 'OD1', 'ASP', 9.72), ('SG', 'CYS', 'OD2', 'ASP', 8.82)]]}
CYS_GLU = { 
	'distances':
		[[16.0, 14.63, 13.6, 13.31, 13.26], [16.15, 14.77, 13.69, 13.53, 13.16]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLU', 16.0), ('CB', 'CYS', 'CG', 'GLU', 14.63), ('CB', 'CYS', 'CD', 'GLU', 13.6), ('CB', 'CYS', 'OE1', 'GLU', 13.31), ('CB', 'CYS', 'OE2', 'GLU', 13.26)], [('SG', 'CYS', 'CB', 'GLU', 16.15), ('SG', 'CYS', 'CG', 'GLU', 14.77), ('SG', 'CYS', 'CD', 'GLU', 13.69), ('SG', 'CYS', 'OE1', 'GLU', 13.53), ('SG', 'CYS', 'OE2', 'GLU', 13.16)]]}
ASP_GLU = { 
	'distances':
		[[11.85, 11.1, 10.03, 8.97, 10.43], [11.47, 10.55, 9.4, 8.49, 9.61], [10.41, 9.41, 8.3, 7.46, 8.53], [12.37, 11.4, 10.17, 9.34, 10.22]],
	'comparisons':
		[[('CB', 'ASP', 'CB', 'GLU', 11.85), ('CB', 'ASP', 'CG', 'GLU', 11.1), ('CB', 'ASP', 'CD', 'GLU', 10.03), ('CB', 'ASP', 'OE1', 'GLU', 8.97), ('CB', 'ASP', 'OE2', 'GLU', 10.43)], [('CG', 'ASP', 'CB', 'GLU', 11.47), ('CG', 'ASP', 'CG', 'GLU', 10.55), ('CG', 'ASP', 'CD', 'GLU', 9.4), ('CG', 'ASP', 'OE1', 'GLU', 8.49), ('CG', 'ASP', 'OE2', 'GLU', 9.61)], [('OD1', 'ASP', 'CB', 'GLU', 10.41), ('OD1', 'ASP', 'CG', 'GLU', 9.41), ('OD1', 'ASP', 'CD', 'GLU', 8.3), ('OD1', 'ASP', 'OE1', 'GLU', 7.46), ('OD1', 'ASP', 'OE2', 'GLU', 8.53)], [('OD2', 'ASP', 'CB', 'GLU', 12.37), ('OD2', 'ASP', 'CG', 'GLU', 11.4), ('OD2', 'ASP', 'CD', 'GLU', 10.17), ('OD2', 'ASP', 'OE1', 'GLU', 9.34), ('OD2', 'ASP', 'OE2', 'GLU', 10.22)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_ASP, d, 'A_1b5d_2_1_2_8')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_GLU, d, 'A_1b5d_2_1_2_8')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ASP_GLU, d, 'A_1b5d_2_1_2_8')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_ASP' :  match1,
		'CYS_GLU' :  match2,
		'ASP_GLU' :  match3}