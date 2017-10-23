'''
FUNC:R_1g8k_1_20_98_1
PDB:1g8k
EC:1.20.98.1
RESI:4mo,f3s,fes
LOCI:a-5004,5005;b-5006;
'''
import motifFunctions as cmd
4MO_F3S = { 
	'distances':
		[15.95, 17.01, 14.34, 18.01, 14.4, 15.4, 16.02],
	'comparisons':
		[('MO', '4MO', 'FE1', 'F3S', 15.95), ('MO', '4MO', 'FE3', 'F3S', 17.01), ('MO', '4MO', 'FE4', 'F3S', 14.34), ('MO', '4MO', 'S1', 'F3S', 18.01), ('MO', '4MO', 'S2', 'F3S', 14.4), ('MO', '4MO', 'S3', 'F3S', 15.4), ('MO', '4MO', 'S4', 'F3S', 16.02)]}
4MO_FES = { 
	'distances':
		[28.99, 27.17, 26.89, 29.4],
	'comparisons':
		[('MO', '4MO', 'FE1', 'FES', 28.99), ('MO', '4MO', 'FE2', 'FES', 27.17), ('MO', '4MO', 'S1', 'FES', 26.89), ('MO', '4MO', 'S2', 'FES', 29.4)]}
F3S_FES = { 
	'distances':
		[[18.59, 16.29, 17.0, 18.19], [17.45, 14.95, 15.83, 16.88], [18.75, 16.43, 16.94, 18.5], [16.68, 14.3, 15.22, 16.12], [18.54, 16.4, 16.78, 18.43], [19.68, 17.23, 18.03, 19.17], [16.9, 14.49, 15.07, 16.58]],
	'comparisons':
		[[('FE1', 'F3S', 'FE1', 'FES', 18.59), ('FE1', 'F3S', 'FE2', 'FES', 16.29), ('FE1', 'F3S', 'S1', 'FES', 17.0), ('FE1', 'F3S', 'S2', 'FES', 18.19)], [('FE3', 'F3S', 'FE1', 'FES', 17.45), ('FE3', 'F3S', 'FE2', 'FES', 14.95), ('FE3', 'F3S', 'S1', 'FES', 15.83), ('FE3', 'F3S', 'S2', 'FES', 16.88)], [('FE4', 'F3S', 'FE1', 'FES', 18.75), ('FE4', 'F3S', 'FE2', 'FES', 16.43), ('FE4', 'F3S', 'S1', 'FES', 16.94), ('FE4', 'F3S', 'S2', 'FES', 18.5)], [('S1', 'F3S', 'FE1', 'FES', 16.68), ('S1', 'F3S', 'FE2', 'FES', 14.3), ('S1', 'F3S', 'S1', 'FES', 15.22), ('S1', 'F3S', 'S2', 'FES', 16.12)], [('S2', 'F3S', 'FE1', 'FES', 18.54), ('S2', 'F3S', 'FE2', 'FES', 16.4), ('S2', 'F3S', 'S1', 'FES', 16.78), ('S2', 'F3S', 'S2', 'FES', 18.43)], [('S3', 'F3S', 'FE1', 'FES', 19.68), ('S3', 'F3S', 'FE2', 'FES', 17.23), ('S3', 'F3S', 'S1', 'FES', 18.03), ('S3', 'F3S', 'S2', 'FES', 19.17)], [('S4', 'F3S', 'FE1', 'FES', 16.9), ('S4', 'F3S', 'FE2', 'FES', 14.49), ('S4', 'F3S', 'S1', 'FES', 15.07), ('S4', 'F3S', 'S2', 'FES', 16.58)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(4MO_F3S, d, 'R_1g8k_1_20_98_1')
	if match1 == []:
		 flag = True
		 break
	match2 , totTime2 = cmd.detect(4MO_FES, d, 'R_1g8k_1_20_98_1')
	if match2 == []:
		 flag = True
		 break
	match3 , totTime3 = cmd.detect(F3S_FES, d, 'R_1g8k_1_20_98_1')
	if match3 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'4MO_F3S' :  match1,
		'4MO_FES' :  match2,
		'F3S_FES' :  match3}