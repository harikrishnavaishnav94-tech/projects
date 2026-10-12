print('-'*90)
print('\t\tINSTRUCTIONS')
print('-'*90)
print('"M" or "m - MENU" ')
print('"0" - Place Order')
print('"00" - Display Bill')
print('"000" - Finish the Bill')
print('-'*100)
modl={}
tn=0
while True:
    ch=input('Enter your Choice : ')
    print('-'*100)
    if ch =='m' or ch =='M':
        print('\t\tHK Restaurant')
        print('-'*100)
        print('\t\tMenu')
        print('='*100)
        print(' 1. Plan Dhosa                             \tRs.50')
        print(' 2. Masala Dhosa                           \tRs.90')
        print(' 3. Cheese Dhosa                           \tRs.110')
        print(' 4. Paneer Dhosa                           \tRs.130')
        print(' 5. Pizza Dhosa                            \tRs.170')
        print(' 6. Palak Dhosa                            \tRs.200')
        print(' 7. Jini Roll                              \tRs.210')
        print(' 8. Schezwan Dosa                          \tRs.120')
        print(' 9. Sweet Dhosa                            \tRs.110')
        print('10. RajaRani Dhosa                         \tRs.250')
        print('11. Manchuriyan                            \tRs.100')
        print('12. Noodles                                \tRs.110')
        print('13. Aloo Samosa(2 Pieces)                  \tRs.40')
        print('14. VadaPav(1 Piece)                       \tRs.30')
        print('15. Italian Pizza                          \tRs.100')
        print('='*100)
        print('\n')
    elif ch=='0':
        od=input('Enter your Item Number : ')
        if od=='1':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Plan Dhosa'
            odl['Quantity']=n
            odl['Price']=50*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='2':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Masala Dhosa'
            odl['Quantity']=n
            odl['Price']=90*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='3':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Cheese Dhosa'
            odl['Quantity']=n
            odl['Price']=110*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='4':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Paneer Dhosa'
            odl['Quantity']=n
            odl['Price']=130*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='5':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Pizza Dhosa'
            odl['Quantity']=n
            odl['Price']=170*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='6':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Palak Dhosa'
            odl['Quantity']=n
            odl['Price']=200*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='7':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Jini Roll'
            odl['Quantity']=n
            odl['Price']=210*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='8':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Schezwan Dhosa'
            odl['Quantity']=n
            odl['Price']=120*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='9':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Sweet Dhosa'
            odl['Quantity']=n
            odl['Price']=110*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='10':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='RajaRani Dhosa'
            odl['Quantity']=n
            odl['Price']=250*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='11':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Manchuriyan'
            odl['Quantity']=n
            odl['Price']=100*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='12':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Cheese Noodles'
            odl['Quantity']=n
            odl['Price']=110*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='13':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Aloo Samosa'
            odl['Quantity']=n
            odl['Price']=40*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='14':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Vada Pav'
            odl['Quantity']=n
            odl['Price']=30*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        elif od=='15':
            n=int(input('Enter Number of Item : '))
            odl={}
            odl['Item No']=tn+1
            odl['Item']='Cheese Pizza'
            odl['Quantity']=n
            odl['Price']=100*n
            tn+=1
            modl[tn]=odl
            print('-'*100)
            print()
        else:
            print('-'*100)
            print('...INCORRECT CODE ENTERED...')
    elif ch=='00':
        print('\n')
        print('\t\tHK Restaurant')
        print('-'*100)
        print('\n\t\tBill')
        print('-'*100)
        print('Sr.No  \t Item \t    Quantity   Price')
        print('-'*90)
        for a in modl:
            for b in modl[a]:
                print(modl[a][b],end=' \t')
            print()
        tot=0
        for c in modl:
            tot+=modl[c]['Price']        
        print('='*90)
        print('\tTotal Amount : ',tot)
        print('\n')
    elif ch=='000':
        print('\n')
        print('...Thanks for Visiting HK Restaurant...')
        break
    else:
        print('...ENTERED THE CHOICE GIVEN ABOVE...')








                
        
    
            
        
        
    
