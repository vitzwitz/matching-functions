'''
FUNC:A_1fnb_1_18_1_2
PDB:1fnb
EC:1.18.1.2
RESI:ser,cys,glu
LOCI:a-96,272,312;
'''
import motifFunctions as cmd
CYS_SER = { 
	'distances':
		[[8.76, 8.09], [7.23, 6.4]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'SER', 8.76), ('CB', 'CYS', 'OG', 'SER', 8.09)], [('SG', 'CYS', 'CB', 'SER', 7.23), ('SG', 'CYS', 'OG', 'SER', 6.4)]]}
GLU_SER = { 
	'distances':
		[[9.15, 8.01], [8.33, 7.09], [6.98, 5.83], [7.35, 6.43], [5.88, 4.65]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'SER', 9.15), ('CB', 'GLU', 'OG', 'SER', 8.01)], [('CG', 'GLU', 'CB', 'SER', 8.33), ('CG', 'GLU', 'OG', 'SER', 7.09)], [('CD', 'GLU', 'CB', 'SER', 6.98), ('CD', 'GLU', 'OG', 'SER', 5.83)], [('OE1', 'GLU', 'CB', 'SER', 7.35), ('OE1', 'GLU', 'OG', 'SER', 6.43)], [('OE2', 'GLU', 'CB', 'SER', 5.88), ('OE2', 'GLU', 'OG', 'SER', 4.65)]]}
GLU_CYS = { 
	'distances':
		[[6.9, 6.34], [7.52, 6.46], [7.54, 6.24], [8.28, 7.17], [7.21, 5.66]],
	'comparisons':
		[[('CB', 'GLU', 'CB', 'CYS', 6.9), ('CB', 'GLU', 'SG', 'CYS', 6.34)], [('CG', 'GLU', 'CB', 'CYS', 7.52), ('CG', 'GLU', 'SG', 'CYS', 6.46)], [('CD', 'GLU', 'CB', 'CYS', 7.54), ('CD', 'GLU', 'SG', 'CYS', 6.24)], [('OE1', 'GLU', 'CB', 'CYS', 8.28), ('OE1', 'GLU', 'SG', 'CYS', 7.17)], [('OE2', 'GLU', 'CB', 'CYS', 7.21), ('OE2', 'GLU', 'SG', 'CYS', 5.66)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_SER, d, 'A_1fnb_1_18_1_2')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(GLU_SER, d, 'A_1fnb_1_18_1_2')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(GLU_CYS, d, 'A_1fnb_1_18_1_2')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_SER' :  match1,
		'GLU_SER' :  match2,
		'GLU_CYS' :  match3}