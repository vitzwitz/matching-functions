'''
FUNC:M_1ra0_3_5_4_1
PDB:1ra0
EC:3.5.4.1
RESI:gln,glu,fe
LOCI:a-156,217,500;
'''
import motifFunctions as cmd
GLN_FE = { 
	'distances':
		[[10.96], [10.79], [9.47], [8.66], [9.45]],
	'comparisons':
		[[('CB', 'GLN', 'FE', 'FE', 10.96)], [('CG', 'GLN', 'FE', 'FE', 10.79)], [('CD', 'GLN', 'FE', 'FE', 9.47)], [('OE1', 'GLN', 'FE', 'FE', 8.66)], [('NE2', 'GLN', 'FE', 'FE', 9.45)]]}
GLN_GLU = { 
	'distances':
		[[13.59, 13.91, 12.83, 13.26, 11.65], [13.05, 13.25, 12.13, 12.49, 11.02], [11.7, 11.81, 10.65, 10.98, 9.56], [11.73, 11.68, 10.4, 10.58, 9.36], [10.64, 10.88, 9.83, 10.3, 8.71]],
	'comparisons':
		[[('CB', 'GLN', 'CB', 'GLU', 13.59), ('CB', 'GLN', 'CG', 'GLU', 13.91), ('CB', 'GLN', 'CD', 'GLU', 12.83), ('CB', 'GLN', 'OE1', 'GLU', 13.26), ('CB', 'GLN', 'OE2', 'GLU', 11.65)], [('CG', 'GLN', 'CB', 'GLU', 13.05), ('CG', 'GLN', 'CG', 'GLU', 13.25), ('CG', 'GLN', 'CD', 'GLU', 12.13), ('CG', 'GLN', 'OE1', 'GLU', 12.49), ('CG', 'GLN', 'OE2', 'GLU', 11.02)], [('CD', 'GLN', 'CB', 'GLU', 11.7), ('CD', 'GLN', 'CG', 'GLU', 11.81), ('CD', 'GLN', 'CD', 'GLU', 10.65), ('CD', 'GLN', 'OE1', 'GLU', 10.98), ('CD', 'GLN', 'OE2', 'GLU', 9.56)], [('OE1', 'GLN', 'CB', 'GLU', 11.73), ('OE1', 'GLN', 'CG', 'GLU', 11.68), ('OE1', 'GLN', 'CD', 'GLU', 10.4), ('OE1', 'GLN', 'OE1', 'GLU', 10.58), ('OE1', 'GLN', 'OE2', 'GLU', 9.36)], [('NE2', 'GLN', 'CB', 'GLU', 10.64), ('NE2', 'GLN', 'CG', 'GLU', 10.88), ('NE2', 'GLN', 'CD', 'GLU', 9.83), ('NE2', 'GLN', 'OE1', 'GLU', 10.3), ('NE2', 'GLN', 'OE2', 'GLU', 8.71)]]}
GLU_FE = { 
	'distances':
		[[9.65], [9.23], [7.96], [7.84], [7.36]],
	'comparisons':
		[[('CB', 'GLU', 'FE', 'FE', 9.65)], [('CG', 'GLU', 'FE', 'FE', 9.23)], [('CD', 'GLU', 'FE', 'FE', 7.96)], [('OE1', 'GLU', 'FE', 'FE', 7.84)], [('OE2', 'GLU', 'FE', 'FE', 7.36)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLN_FE, d, 'M_1ra0_3_5_4_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLN_GLU, d, 'M_1ra0_3_5_4_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_FE, d, 'M_1ra0_3_5_4_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLN_FE' :  match1,
		'GLN_GLU' :  match2,
		'GLU_FE' :  match3}