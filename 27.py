import itertools
for i in itertools.permutations('xyz'):
    if i[0]!='x' and i[2]!='x' and i[2]!='z':
        print('a-%s,b-%s,c-%s'%(i[0],i[1],i[2]))
