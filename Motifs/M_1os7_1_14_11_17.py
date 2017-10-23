'''
FUNC:M_1os7_1_14_11_17
PDB:1os7
EC:1.14.11.17
RESI:arg,fe2
LOCI:a-270;a-302;
'''
import motifFunctions as cmd
ARG_FE2 = { 
	'distances':
		[[9.53], [8.85], [7.48], [7.52], [6.87], [5.93], [7.53]],
	'comparisons':
		[[('CB', 'ARG', 'FE', 'FE2', 9.53)], [('CG', 'ARG', 'FE', 'FE2', 8.85)], [('CD', 'ARG', 'FE', 'FE2', 7.48)], [('NE', 'ARG', 'FE', 'FE2', 7.52)], [('CZ', 'ARG', 'FE', 'FE2', 6.87)], [('NH1', 'ARG', 'FE', 'FE2', 5.93)], [('NH2', 'ARG', 'FE', 'FE2', 7.53)]]}


flag = False
while True:
	match1 , totTime1 = cmd.detect(ARG_FE2, d, 'M_1os7_1_14_11_17')
	if match1 == []:
		 flag = True
		 break
	break

if flag == False:
	matches = {
		'ARG_FE2' :  match1}