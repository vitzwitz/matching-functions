'''
FUNC:M_1uw8_4_1_1_2
PDB:1uw8
EC:4.1.1.2
RESI:arg,glu,mn,mn
LOCI:a-92,162,1383,1384;
'''
import motifFunctions as cmd
ARG_MN = { 
	'distances':
		[[9.42], [8.21], [8.76], [7.89], [7.98], [8.88], [7.53], [32.24], [31.6], [31.87], [31.35], [32.13], [33.42], [31.64]],
	'comparisons':
		[[('CB', 'ARG', 'MN', 'MN', 9.42)], [('CG', 'ARG', 'MN', 'MN', 8.21)], [('CD', 'ARG', 'MN', 'MN', 8.76)], [('NE', 'ARG', 'MN', 'MN', 7.89)], [('CZ', 'ARG', 'MN', 'MN', 7.98)], [('NH1', 'ARG', 'MN', 'MN', 8.88)], [('NH2', 'ARG', 'MN', 'MN', 7.53)], [('CB', 'ARG', 'MN', 'MN', 32.24)], [('CG', 'ARG', 'MN', 'MN', 31.6)], [('CD', 'ARG', 'MN', 'MN', 31.87)], [('NE', 'ARG', 'MN', 'MN', 31.35)], [('CZ', 'ARG', 'MN', 'MN', 32.13)], [('NH1', 'ARG', 'MN', 'MN', 33.42)], [('NH2', 'ARG', 'MN', 'MN', 31.64)]]}
ARG_GLU = { 
	'distances':
		[[11.34, 9.81, 9.28, 10.17, 8.15], [10.04, 8.51, 7.9, 8.8, 6.73], [9.05, 7.53, 7.24, 8.31, 6.17], [7.91, 6.42, 6.05, 7.15, 4.96], [8.07, 6.72, 6.41, 7.5, 5.39], [9.23, 7.93, 7.73, 8.81, 6.72], [7.36, 6.19, 5.81, 6.79, 4.97]],
	'comparisons':
		[[('CB', 'ARG', 'CB', 'GLU', 11.34), ('CB', 'ARG', 'CG', 'GLU', 9.81), ('CB', 'ARG', 'CD', 'GLU', 9.28), ('CB', 'ARG', 'OE1', 'GLU', 10.17), ('CB', 'ARG', 'OE2', 'GLU', 8.15)], [('CG', 'ARG', 'CB', 'GLU', 10.04), ('CG', 'ARG', 'CG', 'GLU', 8.51), ('CG', 'ARG', 'CD', 'GLU', 7.9), ('CG', 'ARG', 'OE1', 'GLU', 8.8), ('CG', 'ARG', 'OE2', 'GLU', 6.73)], [('CD', 'ARG', 'CB', 'GLU', 9.05), ('CD', 'ARG', 'CG', 'GLU', 7.53), ('CD', 'ARG', 'CD', 'GLU', 7.24), ('CD', 'ARG', 'OE1', 'GLU', 8.31), ('CD', 'ARG', 'OE2', 'GLU', 6.17)], [('NE', 'ARG', 'CB', 'GLU', 7.91), ('NE', 'ARG', 'CG', 'GLU', 6.42), ('NE', 'ARG', 'CD', 'GLU', 6.05), ('NE', 'ARG', 'OE1', 'GLU', 7.15), ('NE', 'ARG', 'OE2', 'GLU', 4.96)], [('CZ', 'ARG', 'CB', 'GLU', 8.07), ('CZ', 'ARG', 'CG', 'GLU', 6.72), ('CZ', 'ARG', 'CD', 'GLU', 6.41), ('CZ', 'ARG', 'OE1', 'GLU', 7.5), ('CZ', 'ARG', 'OE2', 'GLU', 5.39)], [('NH1', 'ARG', 'CB', 'GLU', 9.23), ('NH1', 'ARG', 'CG', 'GLU', 7.93), ('NH1', 'ARG', 'CD', 'GLU', 7.73), ('NH1', 'ARG', 'OE1', 'GLU', 8.81), ('NH1', 'ARG', 'OE2', 'GLU', 6.72)], [('NH2', 'ARG', 'CB', 'GLU', 7.36), ('NH2', 'ARG', 'CG', 'GLU', 6.19), ('NH2', 'ARG', 'CD', 'GLU', 5.81), ('NH2', 'ARG', 'OE1', 'GLU', 6.79), ('NH2', 'ARG', 'OE2', 'GLU', 4.97)]]}
MN_MN = { 
	'distances':
		[28.03, 28.03],
	'comparisons':
		[('MN', 'MN', 'MN', 'MN', 28.03), ('MN', 'MN', 'MN', 'MN', 28.03)]}
GLU_MN = { 
	'distances':
		[[9.68], [8.82], [7.32], [7.06], [6.64], [28.2], [28.72], [28.13], [27.02], [28.82]],
	'comparisons':
		[[('CB', 'GLU', 'MN', 'MN', 9.68)], [('CG', 'GLU', 'MN', 'MN', 8.82)], [('CD', 'GLU', 'MN', 'MN', 7.32)], [('OE1', 'GLU', 'MN', 'MN', 7.06)], [('OE2', 'GLU', 'MN', 'MN', 6.64)], [('CB', 'GLU', 'MN', 'MN', 28.2)], [('CG', 'GLU', 'MN', 'MN', 28.72)], [('CD', 'GLU', 'MN', 'MN', 28.13)], [('OE1', 'GLU', 'MN', 'MN', 27.02)], [('OE2', 'GLU', 'MN', 'MN', 28.82)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_MN, d, 'M_1uw8_4_1_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(ARG_GLU, d, 'M_1uw8_4_1_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(MN_MN, d, 'M_1uw8_4_1_1_2')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(GLU_MN, d, 'M_1uw8_4_1_1_2')
	if match4 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_MN' :  match1,
		'ARG_GLU' :  match2,
		'MN_MN' :  match3,
		'GLU_MN' :  match4}