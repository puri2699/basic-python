# def function(a,b,c,d):
#     sum=a+b+c+d
#     return sum
# print(function(1,1,1,1))

def users1(user, *users):
    print('1 user only', user)

    for _ in users:
        print('many users', users)


users1(print("ceo", "man", "cto"))
users1(print('admin'))
