'''
FUNC:A_1vr7_4_1_1_50
PDB:1vr7
EC:4.1.1.50
RESI:ser,ser,his,cys
LOCI:a-55,63,68,83;
'''
import motifFunctions as cmd
HIS_CYS = { 
	'distances':
		[[23.69, 22.51], [22.63, 21.42], [22.88, 21.67], [21.42, 20.17], [21.85, 20.62], [20.91, 19.65]],
	'comparisons':
		[[('CB', 'HIS', 'CB', 'CYS', 23.69), ('CB', 'HIS', 'SG', 'CYS', 22.51)], [('CG', 'HIS', 'CB', 'CYS', 22.63), ('CG', 'HIS', 'SG', 'CYS', 21.42)], [('ND1', 'HIS', 'CB', 'CYS', 22.88), ('ND1', 'HIS', 'SG', 'CYS', 21.67)], [('CD2', 'HIS', 'CB', 'CYS', 21.42), ('CD2', 'HIS', 'SG', 'CYS', 20.17)], [('CE1', 'HIS', 'CB', 'CYS', 21.85), ('CE1', 'HIS', 'SG', 'CYS', 20.62)], [('NE2', 'HIS', 'CB', 'CYS', 20.91), ('NE2', 'HIS', 'SG', 'CYS', 19.65)]]}
CYS_SERI = { 
	'distances':
		[[7.19, 6.55], [6.0, 5.81]],
	'comparisons':
		[[('CB', 'CYS', 'CB', 'SERI', 7.19), ('CB', 'CYS', 'OG', 'SERI', 6.55)], [('SG', 'CYS', 'CB', 'SERI', 6.0), ('SG', 'CYS', 'OG', 'SERI', 5.81)]]}
SER_SER = { 
	'distances':
		[[19.46, 19.93], [20.07, 20.59], [19.46, 20.07], [19.93, 20.59]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'SER', 19.46), ('CB', 'SER', 'OG', 'SER', 19.93)], [('OG', 'SER', 'CB', 'SER', 20.07), ('OG', 'SER', 'OG', 'SER', 20.59)], [('CB', 'SER', 'CB', 'SER', 19.46), ('CB', 'SER', 'OG', 'SER', 20.07)], [('OG', 'SER', 'CB', 'SER', 19.93), ('OG', 'SER', 'OG', 'SER', 20.59)]]}
SER_CYS = { 
	'distances':
		[[24.45, 23.37], [25.08, 23.93], [7.19, 6.0], [6.55, 5.81]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'CYS', 24.45), ('CB', 'SER', 'SG', 'CYS', 23.37)], [('OG', 'SER', 'CB', 'CYS', 25.08), ('OG', 'SER', 'SG', 'CYS', 23.93)], [('CB', 'SER', 'CB', 'CYS', 7.19), ('CB', 'SER', 'SG', 'CYS', 6.0)], [('OG', 'SER', 'CB', 'CYS', 6.55), ('OG', 'SER', 'SG', 'CYS', 5.81)]]}
SER_HIS = { 
	'distances':
		[[6.93, 6.42, 5.24, 7.32, 5.73, 6.96], [6.11, 5.82, 4.75, 6.91, 5.59, 6.79], [18.94, 17.77, 17.91, 16.57, 16.83, 15.94], [19.42, 18.31, 18.47, 17.14, 17.44, 16.56]],
	'comparisons':
		[[('CB', 'SER', 'CB', 'HIS', 6.93), ('CB', 'SER', 'CG', 'HIS', 6.42), ('CB', 'SER', 'ND1', 'HIS', 5.24), ('CB', 'SER', 'CD2', 'HIS', 7.32), ('CB', 'SER', 'CE1', 'HIS', 5.73), ('CB', 'SER', 'NE2', 'HIS', 6.96)], [('OG', 'SER', 'CB', 'HIS', 6.11), ('OG', 'SER', 'CG', 'HIS', 5.82), ('OG', 'SER', 'ND1', 'HIS', 4.75), ('OG', 'SER', 'CD2', 'HIS', 6.91), ('OG', 'SER', 'CE1', 'HIS', 5.59), ('OG', 'SER', 'NE2', 'HIS', 6.79)], [('CB', 'SER', 'CB', 'HIS', 18.94), ('CB', 'SER', 'CG', 'HIS', 17.77), ('CB', 'SER', 'ND1', 'HIS', 17.91), ('CB', 'SER', 'CD2', 'HIS', 16.57), ('CB', 'SER', 'CE1', 'HIS', 16.83), ('CB', 'SER', 'NE2', 'HIS', 15.94)], [('OG', 'SER', 'CB', 'HIS', 19.42), ('OG', 'SER', 'CG', 'HIS', 18.31), ('OG', 'SER', 'ND1', 'HIS', 18.47), ('OG', 'SER', 'CD2', 'HIS', 17.14), ('OG', 'SER', 'CE1', 'HIS', 17.44), ('OG', 'SER', 'NE2', 'HIS', 16.56)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(HIS_CYS, d, 'A_1vr7_4_1_1_50')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(CYS_SERI, d, 'A_1vr7_4_1_1_50')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(SER_SER, d, 'A_1vr7_4_1_1_50')
	if match3 == []:
		 flag = True
		 break
	match4 , totTime4 = cmd.detect(SER_CYS, d, 'A_1vr7_4_1_1_50')
	if match4 == []:
		 flag = True
		 break
	match5 , totTime5 = cmd.detect(SER_HIS, d, 'A_1vr7_4_1_1_50')
	if match5 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'HIS_CYS' :  match1,
		'CYS_SERI' :  match2,
		'SER_SER' :  match3,
		'SER_CYS' :  match4,
		'SER_HIS' :  match5}