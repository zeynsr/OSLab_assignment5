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
    code = input('code : ')
    while True:
        name = input('name : ')
        check = False
        for p in PRODUCTS:
            if name == p['name']:
                check = True
                print('This product is already stored in the list')

        if check == False:
            break

    price = input('price : ')
    num = input('number : ')
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
            print('name'+"   "+'price'+"   "+'number')
            print(p['name']+' '+p['price']+' '+p['number'])
            return True
        else:
            print('This product is not in stock !🚫')
            return False

def Delete(name):
    for p in PRODUCTS:
        if p["name"] == name:
            PRODUCTS.remove(p)
            return

def buy():
  show_list()
  f=1
  sum=0
  shopping=[]
  while f==1:
      pr_b = input('enter the name of product that you want : ')
      for p in PRODUCTS:
          if pr_b == p['name']:
              nu = int(input('how many do you want ? '))
              sum = sum + (int(nu) * int(p['price']))
              n = int(p['number'])
              if n == 0:
                  Delete(pr_b)
                  print('This product is not available')
                  break
              elif nu > n:
                  print('This product is not available enough')
                  break
              else:
                  pay = int(p['price'])
                  paym = pay * n
                  print('payment : ' + str(paym))
                  n -= nu
                  p['number'] = n
                  shoppingg = {'code': p['code'], 'name': p['name'], 'price': p['price'],'count': nu}
                  shopping.append(shoppingg)
                  break
      else:
         print('This product is not in stock.')

      fl=int(input('Do you want to continue ? \n1.yes\n2.no\n'))
      if fl==1:
          f=1
      else:
          f=-1
          for i in shopping:
              print(f"{i['code']}\t{i['name']}\t\t{i['price']}\t{i['count']}")
          print("Total amount =", sum)
          print('\nThanks for your purchase\n')
          break

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
