a = input()
under = False
camel =[]
for i in range(len(a)):
    if a[i] == '_':
        under =True
        if a[i-1] == '_':
            camel.append(i)       
    
    elif a[i].isupper():
        camel.append(i)

if a[0] == '_' or a[0].isupper() or a[-1] == '_':
    under = True
    camel.append(-1)


if under and not camel:
    c = a.split('_')
    for index,value in enumerate(c):
        if index == 0:
            d = value
        else:
            d = d + value.capitalize()
    print(d)
elif not under and camel:    
    c = a.lower()
    d = []
    for index,value in enumerate(camel):
        if index == 0:
            d.append(c[:value])
            if len(camel) == 1:
                d.append('_'+c[value:])
            j=value
        elif index == len(camel)-1:
            d.append('_'+c[j:value])
            d.append('_'+c[value:])
        else:
            d.append('_'+c[j:value])
            j = value
    l = ''
    for k in d:
       l = l+k 
    print(l)

else:
    print("Error!")