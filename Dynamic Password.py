'''
%b - month name short version
%B - month name full
%m - month as a number
%y - year short version (without century)
%Y - year full version
%H - hour (24 hours)
%I - hour (12 hours)
%p - AM/PM
%M - Minute '''



p=input('Enter a Password : ')
import datetime
x=datetime.datetime.now()
h=x.strftime('%I')
m=x.strftime('%M')

'''print('Current Hour : ',h)
print('Current Minute : ',m)'''
'''for a in range(0,len(p)):
    al=p[a]
    if al.isalpha():
        print('INVALID PASSWORD')
        break'''
        
for d in range(0,len(p)):
    dl=p[d]
    if dl.isdigit():
        '''print('VALID PASSWORD')'''
        break

if len(p)==4 and dl.isdigit():
    hc=p[:2]
    '''print('Hour Entered by you : ',hc)'''
    mc=p[2:]
    '''print('Minute Entered by you : ',mc)'''
else:
    print('INVALID PASSWORD')

    
if len(p)==4 and dl.isdigit():
    print('-'*99)




if len(p)==4 and dl.isdigit():
    if hc==h and mc==m:
        print('ACCESS GRANTED')
    else:
        print('INCORRECT PASSWORD')
    

    

