import csv
PRODUCTS=[]

def load_data_from_database():
    print('loading...⏳')
    f=open('data.csv','r')
    for row in f:
        info=row[:-1].split(',')
        new_dic={'code':info[0],'name':info[1],'price':info[2],'number':info[3]}
        PRODUCTS.append(new_dic)
    print('load complete.📑')

def show_list():
    for product in PRODUCTS:
        print(product)

def add():
    print('enter the information of new product : ')
    code=input('code : ')
    name=input('name : ')
    price=input('price : ')
    num=input('number : ')
    PRODUCTS.append({"code": code, "name": name, "price": price, "number": num})

def edit():
    Edit_code=input('enter the code of product : ')
    for p in PRODUCTS:
        if Edit_code==p['code'] :
           while True:
               ch = int(input("which part do you want to edit ? \n 1.name\n 2.price\n 3.number \n"))
               if ch == 1:
                   edit_name = input('enter the new name :')
                   p['name'] = edit_name
                   break
               elif ch == 2:
                   edit_price = input('enter the new price :')
                   p['price'] = edit_price
                   break
               elif ch == 3:
                   edit_number = input('enter the new number :')
                   p['number'] = edit_number
                   break
               else:
                   break

def delete():
    Del_code = input('enter the code of product : ')
    for p in PRODUCTS:
        if p["code"] == Del_code:
            PRODUCTS.remove(p)
            print("Removed successfully📤")
            return

def search():
    s_pr=input('enter the name of your product : ')
    for p in PRODUCTS:
        if s_pr== p['name'] :
            print(p)
            return True
        else:
            print('Couldn\'t find !🚫')
            return False

def buy():
    p_b=input('enter the name of product that you want : ')
    nu=int(input('how many do you want ? '))
    for p in PRODUCTS:
        if p_b==p['name'] :
            n=int(p['number'])
            if n==0 :
                delete(p_b)
                print('This product is not available')
                break
            elif nu>n :
                print('This product is not available enough')
                break
            else:
                pay =int(p['price'])
                paym=pay*n
                print('payment : '+str(paym))
                n-=nu
                p['number']=n
                print('Thanks for your purchase')

def save():
    lst = ['', '', '', '']
    f = open("data.csv", 'w')
    writer = csv.writer(f)
    for pr in PRODUCTS :
        lst[0] = pr["code"]
        lst[1] = pr["name"]
        lst[2] = pr["price"]
        lst[3] = pr["number"]
        writer.writerow(lst)
    f.close()
    exit()

def show_menu():
    print('welcome to our store')
    print('1-add')
    print('2-edit')
    print('3-delete')
    print('4-show list')
    print('5-search')
    print('6-buy')
    print('7-exit')

load_data_from_database()
while True:
    show_menu()
    choice=int(input('please choose from menu : '))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        delete()
    elif choice==4:
        show_list()
    elif choice==5:
        search()
    elif choice==6:
        buy()
    elif choice==7:
        save()