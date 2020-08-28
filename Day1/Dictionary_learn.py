brand = { 'ray' : 'mac',
          'bob' : 'pc',
          'num': 'chromebook'}

print(type(brand))    #brand.__clas__

print(len(brand))    # brand.__len__()

print('bob' in brand) # brand.__contains__('bob')
print('sync' in brand)
print(brand['ray'])   ##brand.__getitem__('rachel')

print(brand.__getitem__('ray'))

print(brand.keys())
print(brand.values())
print(brand.items())

me = 'cindy'
#EAPF : Easier to ask forgiveness than permission
try :   #database lookup
    #me = 'cindy'
    print(me, 'likes', brand[me])
except KeyError:
    print(me, 'likes', 'unknown')


#LBYL : look before you leap
if me in brand:
    print(me , 'likes', brand[me])
else:
    print(me , 'like', 'unknown')

print("Hello world trying jenkins for first time")



