'''
FUNC:A_1hzf_3_4_21_43
PDB:1hzf
EC:3.4.21.43
RESI:cys,gln
LOCI:a-991,994;
'''
import motifFunctions as cmd
CYS_GLN = { 
	'distances':
		[[7.3, 7.12, 8.42, 9.5, 8.53], [6.35, 5.85, 6.93, 8.1, 6.85]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'GLN', 7.3), ('CB', 'CYS', 'CG', 'GLN', 7.12), ('CB', 'CYS', 'CD', 'GLN', 8.42), ('CB', 'CYS', 'OE1', 'GLN', 9.5), ('CB', 'CYS', 'NE2', 'GLN', 8.53)], [('SG', 'CYS', 'CB', 'GLN', 6.35), ('SG', 'CYS', 'CG', 'GLN', 5.85), ('SG', 'CYS', 'CD', 'GLN', 6.93), ('SG', 'CYS', 'OE1', 'GLN', 8.1), ('SG', 'CYS', 'NE2', 'GLN', 6.85)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(CYS_GLN, d, 'A_1hzf_3_4_21_43')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'CYS_GLN' :  match1}