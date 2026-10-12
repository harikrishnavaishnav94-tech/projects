ps=input('Enter Password '
         '(Including Alphabets, Digits, special character and no space) : ')
al=False
dt=False
special=False
space=True
l=len(ps)

#chekcking alphabet
for t in range(0,l):
    x=ps[t]
    if x.isalpha():
        al=True
        


#checking number
for t in range(0,l):
    x=ps[t]
    if x.isdigit():
        dt=True
        
    


#checking special character
for t in range(0,l):
    x=ps[t]
    if x=='!' or x=='@' or x=='#' or x=='$' or x=='%' or x=='^' or x=='&' or x=='*' or x=='(' or x==')' or x=='_' or x=='[' or x==']' or x=='{' or x=='}' or x==',' or x=='.' or x=='/' or x=='?' or x=='<' or x=='>' or x==':' or x==';' or x=="'" or x=='"' or x=='+' or x=='=' or x=='-':
        special=True
    



#checking space
for t in range(0,l):
    x=ps[t]
    if x==' ':
        space=False





#final process
if al==True and dt==True and special==True and space==True:
    print('Valid Password')
else:
    print('Input a Valid Password Under Given Criteria')




#store id into list
if al==True and dt==True and special==True and space==True:


    il=[]
    for a in range(0,l):
        i=ps[a]
        index=id(i)
        il.append(index)
    '''print(il)'''




    
    

#checking password again 
if al==True and dt==True and special==True and space==True:


    ifl=[]
    ps1=input('Enter Your Password : ')
    for f in range(0,len(ps1)):
        g=ps1[f]
        h=id(g)
        ifl.append(h)
        '''print(ifl)'''
    if il==ifl:
        print('Access to Account')
    else:
        print('Access Denied')



    
      

    



        
    
