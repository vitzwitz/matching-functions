'''
FUNC:A_1alk_3_1_3_1
PDB:1alk
EC:3.1.3.1
RESI:ser,arg
LOCI:a-102,166;
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. arg'%(d*9.47))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. arg'%(d*9.57))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CD&r. arg'%(d*8.36))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. NE&r. arg'%(d*7.63))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. CZ&r. arg'%(d*6.48))
cmd.select('ser6', 'n. CB&r. ser w. %s of n. NH1&r. arg'%(d*6.03))
cmd.select('ser7', 'n. CB&r. ser w. %s of n. NH2&r. arg'%(d*6.13))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CB&r. arg'%(d*10.72))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. CG&r. arg'%(d*10.68))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. CD&r. arg'%(d*9.40))
cmd.select('ser11', 'n. OG&r. ser w. %s of n. NE&r. arg'%(d*8.55))
cmd.select('ser12', 'n. OG&r. ser w. %s of n. CZ&r. arg'%(d*7.28))
cmd.select('ser13', 'n. OG&r. ser w. %s of n. NH1&r. arg'%(d*6.81))
cmd.select('ser14', 'n. OG&r. ser w. %s of n. NH2&r. arg'%(d*6.77))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.select('arg1', 'n. CB&r. arg w. %s of n. CB&ser'%(d*9.47))
cmd.select('arg2', 'n. CB&r. arg w. %s of n. OG&ser'%(d*10.72))
cmd.select('arg3', 'n. CG&r. arg w. %s of n. CB&ser'%(d*9.57))
cmd.select('arg4', 'n. CG&r. arg w. %s of n. OG&ser'%(d*10.68))
cmd.select('arg5', 'n. CD&r. arg w. %s of n. CB&ser'%(d*8.36))
cmd.select('arg6', 'n. CD&r. arg w. %s of n. OG&ser'%(d*9.40))
cmd.select('arg7', 'n. NE&r. arg w. %s of n. CB&ser'%(d*7.63))
cmd.select('arg8', 'n. NE&r. arg w. %s of n. OG&ser'%(d*8.55))
cmd.select('arg9', 'n. CZ&r. arg w. %s of n. CB&ser'%(d*6.48))
cmd.select('arg10', 'n. CZ&r. arg w. %s of n. OG&ser'%(d*7.28))
cmd.select('arg11', 'n. NH1&r. arg w. %s of n. CB&ser'%(d*6.03))
cmd.select('arg12', 'n. NH1&r. arg w. %s of n. OG&ser'%(d*6.81))
cmd.select('arg13', 'n. NH2&r. arg w. %s of n. CB&ser'%(d*6.13))
cmd.select('arg14', 'n. NH2&r. arg w. %s of n. OG&ser'%(d*6.77))
cmd.select('arg',' br. arg1&br. arg2&br. arg3&br. arg4&br. arg5&br. arg6&br. arg7&br. arg8&br. arg9&br. arg10&br. arg11&br. arg12&br. arg13&br. arg14')
cmd.delete('arg1')
cmd.delete('arg2')
cmd.delete('arg3')
cmd.delete('arg4')
cmd.delete('arg5')
cmd.delete('arg6')
cmd.delete('arg7')
cmd.delete('arg8')
cmd.delete('arg9')
cmd.delete('arg10')
cmd.delete('arg11')
cmd.delete('arg12')
cmd.delete('arg13')
cmd.delete('arg14')
cmd.select('A_1alk_3_1_3_1', 'ser|arg')
cmd.delete('ser')
cmd.delete('arg')
