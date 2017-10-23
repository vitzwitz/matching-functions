'''
FUNC:M_1l0o_2_7_11_1
PDB:1l0o
EC:2.7.11.1
RESI:glu,arg,mg
LOCI:a-46,105;a-602;
'''
import motifFunctions as cmd
GLU_ARG = { 
	'distances':
		[[13.81, 14.2, 13.1, 12.99, 11.93, 10.73, 12.21], [13.61, 14.14, 13.12, 12.9, 11.77, 10.6, 11.95], [12.27, 12.81, 11.82, 11.53, 10.37, 9.24, 10.52], [11.23, 11.8, 10.86, 10.7, 9.62, 8.4, 9.93], [12.36, 12.89, 11.9, 11.43, 10.2, 9.18, 10.15]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 13.81), ('CB', 'GLU', 'CG', 'ARG', 14.2), ('CB', 'GLU', 'CD', 'ARG', 13.1), ('CB', 'GLU', 'NE', 'ARG', 12.99), ('CB', 'GLU', 'CZ', 'ARG', 11.93), ('CB', 'GLU', 'NH1', 'ARG', 10.73), ('CB', 'GLU', 'NH2', 'ARG', 12.21)], [('CG', 'GLU', 'CB', 'ARG', 13.61), ('CG', 'GLU', 'CG', 'ARG', 14.14), ('CG', 'GLU', 'CD', 'ARG', 13.12), ('CG', 'GLU', 'NE', 'ARG', 12.9), ('CG', 'GLU', 'CZ', 'ARG', 11.77), ('CG', 'GLU', 'NH1', 'ARG', 10.6), ('CG', 'GLU', 'NH2', 'ARG', 11.95)], [('CD', 'GLU', 'CB', 'ARG', 12.27), ('CD', 'GLU', 'CG', 'ARG', 12.81), ('CD', 'GLU', 'CD', 'ARG', 11.82), ('CD', 'GLU', 'NE', 'ARG', 11.53), ('CD', 'GLU', 'CZ', 'ARG', 10.37), ('CD', 'GLU', 'NH1', 'ARG', 9.24), ('CD', 'GLU', 'NH2', 'ARG', 10.52)], [('OE1', 'GLU', 'CB', 'ARG', 11.23), ('OE1', 'GLU', 'CG', 'ARG', 11.8), ('OE1', 'GLU', 'CD', 'ARG', 10.86), ('OE1', 'GLU', 'NE', 'ARG', 10.7), ('OE1', 'GLU', 'CZ', 'ARG', 9.62), ('OE1', 'GLU', 'NH1', 'ARG', 8.4), ('OE1', 'GLU', 'NH2', 'ARG', 9.93)], [('OE2', 'GLU', 'CB', 'ARG', 12.36), ('OE2', 'GLU', 'CG', 'ARG', 12.89), ('OE2', 'GLU', 'CD', 'ARG', 11.9), ('OE2', 'GLU', 'NE', 'ARG', 11.43), ('OE2', 'GLU', 'CZ', 'ARG', 10.2), ('OE2', 'GLU', 'NH1', 'ARG', 9.18), ('OE2', 'GLU', 'NH2', 'ARG', 10.15)]]}
GLU_MG = { 
	'distances':
		[[7.22], [7.65], [6.85], [5.76], [7.61]],
	'comparisons':
		[[('CB', 'GLU', 'MG', 'MG', 7.22)], [('CG', 'GLU', 'MG', 'MG', 7.65)], [('CD', 'GLU', 'MG', 'MG', 6.85)], [('OE1', 'GLU', 'MG', 'MG', 5.76)], [('OE2', 'GLU', 'MG', 'MG', 7.61)]]}
ARG_MG = { 
	'distances':
		[[9.12], [9.36], [8.33], [8.65], [7.96], [6.67], [8.79]],
	'comparisons':
		[[('CB', 'ARG', 'MG', 'MG', 9.12)], [('CG', 'ARG', 'MG', 'MG', 9.36)], [('CD', 'ARG', 'MG', 'MG', 8.33)], [('NE', 'ARG', 'MG', 'MG', 8.65)], [('CZ', 'ARG', 'MG', 'MG', 7.96)], [('NH1', 'ARG', 'MG', 'MG', 6.67)], [('NH2', 'ARG', 'MG', 'MG', 8.79)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ARG, d, 'M_1l0o_2_7_11_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_MG, d, 'M_1l0o_2_7_11_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_MG, d, 'M_1l0o_2_7_11_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ARG' :  match1,
		'GLU_MG' :  match2,
		'ARG_MG' :  match3}