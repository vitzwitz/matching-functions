'''
FUNC:M_1r44_3_4_13_22
PDB:1r44
EC:3.4.13.22
RESI:arg,glu,zn
LOCI:a-71,181,203;
'''
import motifFunctions as cmd
GLU_ARG = { 
	'distances':
		[[15.67, 15.76, 14.46, 13.4, 12.11, 11.78, 11.3], [15.56, 15.47, 14.1, 13.13, 11.81, 11.34, 11.13], [14.23, 14.09, 12.69, 11.79, 10.46, 9.91, 9.88], [14.28, 13.99, 12.54, 11.75, 10.44, 9.74, 10.01], [13.26, 13.22, 11.87, 10.92, 9.61, 9.14, 8.98]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'ARG', 15.67), ('CB', 'GLU', 'CG', 'ARG', 15.76), ('CB', 'GLU', 'CD', 'ARG', 14.46), ('CB', 'GLU', 'NE', 'ARG', 13.4), ('CB', 'GLU', 'CZ', 'ARG', 12.11), ('CB', 'GLU', 'NH1', 'ARG', 11.78), ('CB', 'GLU', 'NH2', 'ARG', 11.3)], [('CG', 'GLU', 'CB', 'ARG', 15.56), ('CG', 'GLU', 'CG', 'ARG', 15.47), ('CG', 'GLU', 'CD', 'ARG', 14.1), ('CG', 'GLU', 'NE', 'ARG', 13.13), ('CG', 'GLU', 'CZ', 'ARG', 11.81), ('CG', 'GLU', 'NH1', 'ARG', 11.34), ('CG', 'GLU', 'NH2', 'ARG', 11.13)], [('CD', 'GLU', 'CB', 'ARG', 14.23), ('CD', 'GLU', 'CG', 'ARG', 14.09), ('CD', 'GLU', 'CD', 'ARG', 12.69), ('CD', 'GLU', 'NE', 'ARG', 11.79), ('CD', 'GLU', 'CZ', 'ARG', 10.46), ('CD', 'GLU', 'NH1', 'ARG', 9.91), ('CD', 'GLU', 'NH2', 'ARG', 9.88)], [('OE1', 'GLU', 'CB', 'ARG', 14.28), ('OE1', 'GLU', 'CG', 'ARG', 13.99), ('OE1', 'GLU', 'CD', 'ARG', 12.54), ('OE1', 'GLU', 'NE', 'ARG', 11.75), ('OE1', 'GLU', 'CZ', 'ARG', 10.44), ('OE1', 'GLU', 'NH1', 'ARG', 9.74), ('OE1', 'GLU', 'NH2', 'ARG', 10.01)], [('OE2', 'GLU', 'CB', 'ARG', 13.26), ('OE2', 'GLU', 'CG', 'ARG', 13.22), ('OE2', 'GLU', 'CD', 'ARG', 11.87), ('OE2', 'GLU', 'NE', 'ARG', 10.92), ('OE2', 'GLU', 'CZ', 'ARG', 9.61), ('OE2', 'GLU', 'NH1', 'ARG', 9.14), ('OE2', 'GLU', 'NH2', 'ARG', 8.98)]]}
GLU_ZN = { 
	'distances':
		[[8.15], [8.58], [7.69], [8.42], [6.49]],
	'comparisons':
		[[('CB', 'GLU', 'ZN', 'ZN', 8.15)], [('CG', 'GLU', 'ZN', 'ZN', 8.58)], [('CD', 'GLU', 'ZN', 'ZN', 7.69)], [('OE1', 'GLU', 'ZN', 'ZN', 8.42)], [('OE2', 'GLU', 'ZN', 'ZN', 6.49)]]}
ARG_ZN = { 
	'distances':
		[[9.99], [10.47], [9.49], [8.29], [7.27], [7.49], [6.3]],
	'comparisons':
		[[('CB', 'ARG', 'ZN', 'ZN', 9.99)], [('CG', 'ARG', 'ZN', 'ZN', 10.47)], [('CD', 'ARG', 'ZN', 'ZN', 9.49)], [('NE', 'ARG', 'ZN', 'ZN', 8.29)], [('CZ', 'ARG', 'ZN', 'ZN', 7.27)], [('NH1', 'ARG', 'ZN', 'ZN', 7.49)], [('NH2', 'ARG', 'ZN', 'ZN', 6.3)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(GLU_ARG, d, 'M_1r44_3_4_13_22')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_ZN, d, 'M_1r44_3_4_13_22')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(ARG_ZN, d, 'M_1r44_3_4_13_22')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'GLU_ARG' :  match1,
		'GLU_ZN' :  match2,
		'ARG_ZN' :  match3}