#INPUT ID
iid=input('Enter your ID (INPUT ID WITH ALPHABET , DIGIT AND NO SPACE ) : ')
ial=False
idig=False
ispace=True
iidl=len(iid)


 #checking alphabet in id
for a in range(0,iidl):
    x=iid[a]
    if x.isalpha():
        ial=True



 #check number in id
for a in range(0,iidl):
    x=iid[a]
    if x.isdigit():
        idig=True
        

 #check space in id
for a in range(0,iidl):
    x=iid[a]
    if x==' ':
        ispacel=False


 #final check of id
if ial!=True or idig!=True or ispace!=True:
    print(' INVALID ID ')




#INPUT PASSWORD
if ial==True and idig==True and ispace==True:
    #input password
    ps=input('Enter Password for your ID (INPUT A PASSWORD WITH ALPHABET , DIGIT AND SPECIAL CHARACTER AND NO SPACE) : ')
    pal=False
    pdig=False
    pspace=True
    pspecial=False
    pl=len(ps)


    # check alphabet in password
    for a in range(0,pl):
        x=ps[a]
        if x.isalpha():
            pal=True


    # check number in password
    for a in range(0,pl):
        x=ps[a]
        if x.isdigit():
            pdig=True


    # check space in password
    for a in range(0,pl):
        x=ps[a]
        if x==' ':
            psapce=False


    # check special character in password
    for a in range(0,pl):
        x=ps[a]
        if x=='!' or x=='@' or x=='#' or x=='$' or x=='%' or x=='^' or x=='&' or x=='*' or x=='(' or x==')' or x=='_' or x=='[' or x==']' or x=='{' or x==',' or x=='.' or x=='/' or x=='?' or x=='<' or x=='>' or x==':' or x=="'" or x=='"' or x=='+' or x=='=' or x=='-' or x=='=' or x=='`' or x=='~' or x=='|' or x=='}' or x==';':
            pspecial=True


    # final check of password
    if pal!=True or pdig!=True or pspace!=True or pspecial!=True:
        print(' INVALID PASSWORD ')
    



# STORING ENTERED ID  AND PASSWORD INTO LIST
if ial==True and idig==True and ispace==True and pal==True and pdig==True and pspace==True and pspecial==True:
    idlist=[]
    for a in range(0,len(iid)):
        h=iid[a]
        idid=id(h)
        idlist.append(idid)
    for a in range(0,len(ps)):
        hp=ps[a]
        idps=id(hp)
        idlist.append(idps)
    '''print(idlist)'''




if ial==True and idig==True and ispace==True and pal==True and pdig==True and pspace==True and pspecial==True:
    print('\nTHANK YOU FOR MAKING ID')
    print('\n')
    print('-'*99)
    print('\n')






#RECHECK OF ID AND PASSWORD
if ial==True and idig==True and ispace==True and pal==True and pdig==True and pspace==True and pspecial==True:
    idlist1=[]
    iid1=input('Enter ID : ')
    for a in range(0,len(iid1)):
        h1=iid1[a]
        idid1=id(h1)
        idlist1.append(idid1)
    ps1=input('Enter Password : ')
    for a in range(0,len(ps1)):
        h2=ps1[a]
        idps1=id(h2)
        idlist1.append(idps1)
    '''print(idlist1)'''

    if idlist==idlist1:
        print(' ACCESS GRANTED ')
    else:
        print('INCORRECT ID OR PASSWORD')
        
 
        
