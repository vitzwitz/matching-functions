'''
FUNC:R_1nfs_5_3_3_2
PDB:1nfs
EC:5.3.3.2
RESI:mn,mg
LOCI:a-201,401;
'''
import motifFunctions as cmd
MN_MG = { 
	'distances':
		[11.06],
	'comparisons':
		[('MN', 'MN', 'MG', 'MG', 11.06)]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(MN_MG, d, 'R_1nfs_5_3_3_2')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'MN_MG' :  match1}