a = input()

err = False
if a[0].isupper() or a[0] == '_' or a[-1] == '_' or '__' in a:
    print("Error!1")
    err = True

result = " "
j_flag = False
c_flag = False
upper = False
for b in a:
    if j_flag and b == '_':
        print("Error!2")
        err = True
        break
    if c_flag and b.isupper():
        print("Error!3")
        err = True
        break

    if b.isupper():
        result +='_'
        b.lower()
        flag = True
    
    if b == '_':
        upper = True

    if upper:
       result += b.upper()
       upper =False

    elif not upper:
        result += b

if not err:
   print(result)