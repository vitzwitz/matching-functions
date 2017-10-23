'''
FUNC:M_1gp5_1_14_11_19
PDB:1gp5
EC:1.14.11.19
RESI:lys,fe
LOCI:a-213,390;
'''
import motifFunctions as cmd
LYS_FE = { 
	'distances':
		[[11.05], [11.1], [10.03], [10.47], [9.68]],
	'comparisons':
		[[('CB', 'LYS', 'FE', 'FE', 11.05)], [('CG', 'LYS', 'FE', 'FE', 11.1)], [('CD', 'LYS', 'FE', 'FE', 10.03)], [('CE', 'LYS', 'FE', 'FE', 10.47)], [('NZ', 'LYS', 'FE', 'FE', 9.68)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(LYS_FE, d, 'M_1gp5_1_14_11_19')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'LYS_FE' :  match1}