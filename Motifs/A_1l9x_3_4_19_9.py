'''
FUNC:A_1l9x_3_4_19_9
PDB:1l9x
EC:3.4.19.9
RESI:cys,his
LOCI:a-110,220;
'''
cmd.select('his1', 'n. CB&r. his w. %s of n. CB&r. cys'%(d*8.07))
cmd.select('his2', 'n. CB&r. his w. %s of n. SG&r. cys'%(d*8.85))
cmd.select('his3', 'n. CG&r. his w. %s of n. CB&r. cys'%(d*6.81))
cmd.select('his4', 'n. CG&r. his w. %s of n. SG&r. cys'%(d*7.49))
cmd.select('his5', 'n. ND1&r. his w. %s of n. CB&r. cys'%(d*6.48))
cmd.select('his6', 'n. ND1&r. his w. %s of n. SG&r. cys'%(d*7.35))
cmd.select('his7', 'n. CD2&r. his w. %s of n. CB&r. cys'%(d*6.18))
cmd.select('his8', 'n. CD2&r. his w. %s of n. SG&r. cys'%(d*6.48))
cmd.select('his9', 'n. CE1&r. his w. %s of n. CB&r. cys'%(d*5.60))
cmd.select('his10', 'n. CE1&r. his w. %s of n. SG&r. cys'%(d*6.27))
cmd.select('his11', 'n. NE2&r. his w. %s of n. CB&r. cys'%(d*5.34))
cmd.select('his12', 'n. NE2&r. his w. %s of n. SG&r. cys'%(d*5.58))
cmd.select('his',' br. his1&br. his2&br. his3&br. his4&br. his5&br. his6&br. his7&br. his8&br. his9&br. his10&br. his11&br. his12')
cmd.delete('his1')
cmd.delete('his2')
cmd.delete('his3')
cmd.delete('his4')
cmd.delete('his5')
cmd.delete('his6')
cmd.delete('his7')
cmd.delete('his8')
cmd.delete('his9')
cmd.delete('his10')
cmd.delete('his11')
cmd.delete('his12')
cmd.select('cys1', 'n. CB&r. cys w. %s of n. CB&his'%(d*8.07))
cmd.select('cys2', 'n. CB&r. cys w. %s of n. CG&his'%(d*6.81))
cmd.select('cys3', 'n. CB&r. cys w. %s of n. ND1&his'%(d*6.48))
cmd.select('cys4', 'n. CB&r. cys w. %s of n. CD2&his'%(d*6.18))
cmd.select('cys5', 'n. CB&r. cys w. %s of n. CE1&his'%(d*5.60))
cmd.select('cys6', 'n. CB&r. cys w. %s of n. NE2&his'%(d*5.34))
cmd.select('cys7', 'n. SG&r. cys w. %s of n. CB&his'%(d*8.85))
cmd.select('cys8', 'n. SG&r. cys w. %s of n. CG&his'%(d*7.49))
cmd.select('cys9', 'n. SG&r. cys w. %s of n. ND1&his'%(d*7.35))
cmd.select('cys10', 'n. SG&r. cys w. %s of n. CD2&his'%(d*6.48))
cmd.select('cys11', 'n. SG&r. cys w. %s of n. CE1&his'%(d*6.27))
cmd.select('cys12', 'n. SG&r. cys w. %s of n. NE2&his'%(d*5.58))
cmd.select('cys',' br. cys1&br. cys2&br. cys3&br. cys4&br. cys5&br. cys6&br. cys7&br. cys8&br. cys9&br. cys10&br. cys11&br. cys12')
cmd.delete('cys1')
cmd.delete('cys2')
cmd.delete('cys3')
cmd.delete('cys4')
cmd.delete('cys5')
cmd.delete('cys6')
cmd.delete('cys7')
cmd.delete('cys8')
cmd.delete('cys9')
cmd.delete('cys10')
cmd.delete('cys11')
cmd.delete('cys12')
cmd.select('A_1l9x_3_4_19_9', 'his|cys')
cmd.delete('his')
cmd.delete('cys')
