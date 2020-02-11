# ----------------------------------------------------------
# --------              HW 6: Part 2               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Name: Alexa Canaan
# Time spent on part 2: 5 hours
# Collaborators and sources: mike belleville
#   (List any collaborators or sources here.)
# ----------------------------------------------------------

def print_logo():
    'prints logo'
    print('''
       +--------+
      /        /|    _____           _                                  
     /        / |   / ____|         | |                                 
    +--------+  |  | |     _ __ __ _| |_ ___ ______ __ _ _______  _ __  
    |        |  +  | |    | '__/ _` | __/ _ \______/ _` |_  / _ \| '_ \ 
    |        | /   | |____| | | (_| | ||  __/     | (_| |/ / (_) | | | |
    |        |/     \_____|_|  \__,_|\__\___|      \__,_/___\___/|_| |_|
    +--------+
''') 


def select_items():
    'asks the customer for price and percentage of crate space consumed by each item to be purchased'
    'continues to ask for an item price and crate space until crate is 100% full or customer enters price of 0.00'
    'returns a list of item prices and the total percentage of crate space filled'
    cratespace = 0
    itempricelist = []
    while cratespace < 100:         #while the crate is not full
        itemprice = str(input('Item price? '))
        if itemprice == '0.00':     #if 0.00 is entered, terminate the function
            print('')
            return (itempricelist, cratespace)
        resultprice = is_valid_price(itemprice)
        while resultprice == False: #while the price is invalid, continue to ask for a valid price
            itemprice = str(input('Item price? '))
            if itemprice == '0.00': #0.00 stops the item price prompt
                print('')
                return (itempricelist, cratespace)
            resultprice = is_valid_price(itemprice)
        if itemprice != 0.00 and resultprice == True:   #if the price inputed is valid, ask for crate space
            takencratespace = float(input('Crate space consumed? '))
            resultspace = is_valid_percentage(takencratespace)
            while resultspace == False:         #if crate space not valid, ask again
                takencratespace = float(input('Crate space consumed? '))
                resultspace = is_valid_percentage(takencratespace)
            if resultspace == True and (cratespace + takencratespace) > 100:    #if crate space overflows crate, say so
                print('Not enough space')
                print('')
            if resultspace == True and (cratespace + takencratespace) <= 100:       #valid crate space entered is accounted for
                print('Added to crate')
                print('')
                cratespace += takencratespace
                itempricelist.append(itemprice)
    print('')
    return (itempricelist, cratespace)

def is_valid_price(string):
    'takes a string aka price'
    'returns True if the string is a valid price'
    'returns False if the string is invalid price'
    
    if len(string) < 4:     #if string is less than 4 integers, not a valid price
        return False
    else:                   #if string is minimum valid length
        if string[-3] == '.':       #if there are two decimal points
            try:
                num = float(string)     #check if the number is a positive float
                if num > 0:
                    return True
            except ValueError:          #if the string contains any character that isn't a digit or a period
                return False
        else:
            return False
    
##    alphalist = []
##    for chindex in range(len(string)):
##        a = string[chindex].isalpha()
##        if a == True:
##            alphalist.append(string[chindex])
##    if int((len(alphalist) + 1)) == (len(string)) and string[-3] == '.':
    
##    list1 = []
##    for ch in string:
##        if ch.isdigit() == True:
##            list1 += 'True'
##        else:
##            list1 += 'False'
##    if 'False' in list1:
##        return  False
##    else:
##        return True

##    a = string[0].isdigit()
##    b = string[-1].isdigit()
##    c = string[-2].isdigit()
##    if a == True and b == True and c == True and string[-3] == '.':
##        roundedstring = string
##    else:
##        roundedstring = -1
##        return False
##    
##    if roundedstring[0].isdigit() == True and roundedstring[-3] == '.':
##        return True
##    return False
    
##    a = string.isdigit()
##    roundedstring = 0
##    if a == True:
##        roundedstring = round(float(string), 2)
##    for ch in string:
##        if ch == '.' and string[-3] == '.' and roundedstring > 0.00 and a == True:
##            return True
##        else:
##            return False
    
def is_valid_percentage(num):
    'takes a string aka crate space'
    'returns True if the string is a valid percentage'
    'returns False if the string is an invalid percentage'
    validintlist = []
    i = 0
    while i <= 100:     #create a list of valid crate space integers
        validintlist.append(i)
        i += 1
    if num in validintlist: #if cratespace is a valid integer
        return True
    else:
        return False

def get_coupons():
    'asks the customer to enter coupon codes until the customer does not enter another coupon code'
    'returns a list of the coupon codes entered by the user'
    validcode = ['freeship', 'tenorfewer', 'fullcrate', '15off']
    couponcodelist = []
    couponcode = input('Coupon code? ')
    while couponcode !='':  #iterating over each given coupon code
        if couponcode in validcode: #if the given coupon is valid
                if couponcode not in couponcodelist and couponcode in validcode:    #if couponcode is valid and not yet entered, add to list of coupons
                    couponcodelist.append(couponcode)
                elif couponcode in couponcodelist and couponcode in validcode:      #if couponcode has already been entered, say so
                    print('Already entered coupon code')
                couponcode = input('Coupon code? ')
        else:       #if the coupon code is invalid, say so and prompt again
            if couponcode not in validcode:
                print('Invalid coupon code')
                couponcode = input('Coupon code? ')   
            
    return couponcodelist

def display_summary(itempricelist, cratespace, couponcodelist):
    'takes the item price list, percent of crate space full, and coupons applied'
    'calculates and outputs number of items in crate, the price of each item in the crate'
    'calculates and outputs total cost of all items'
    'outputs percentage of crate space filled, shipping cost, the coupon code and discount applied for each coupon'
    'calculates and outputs the total discounts'
    'calculates and outputs the total cost of the order'
    print('Your crate contains', len(itempricelist), 'items: ')
    totalprice = 0.00
    shipping = 9.99
    for items in range(len(itempricelist)): #creates a list of items bought with the price
        print('Item', str(items + 1)+':', '$'+str(itempricelist[items]))
        totalprice += float(itempricelist[items])
    print('--------------------')
    print('Item Total:', '$'+str(round((totalprice), 2)))
    print('')
    print('Your crate is', str(round((cratespace)))+'%', 'full')
    print('Shipping: $9.99')
    print('')
    print('Discounts applied: ')
    totaldiscount = 0
    for code in couponcodelist: #iterating over each coupon given
        if code == 'freeship':  #freeship means free shipping
            print('freeship: -$9.99')
            shipping = 0.00
            totaldiscount += 9.99
        elif code == 'tenorfewer':  #tenorfewer gives the customer 10% off the total cost of items if the crate contains ten or fewer items
            if len(itempricelist) <= 10:
                totalpricediscount1 = (totalprice * .10)
                totalprice = (totalprice * .90)
                print('tenorfewer: -$'+str(round((totalpricediscount1), 2)))
                totaldiscount += totalpricediscount1
        elif code == 'fullcrate':   #gives the customer 5% off the total cost of items if the crate is 100% full; otherwise, no discount is applied
            if cratespace == 100:
                totalpricediscount2 = (totalprice * .05)
                totalprice = (totalprice * .95)
                print('tenorfewer :-$'+str(round((totalpricediscount2), 2)))
                totaldiscount += totalpricediscount2
        elif code == '15off':   #gives the customer 15% off the total cost of items If the customer enters an invalid coupon code, the program must display the error Invalid coupon code.
            totalpricediscount3 = (totalprice * .15)
            totalprice = (totalprice * .85)
            print('15off :-$'+str(round((totalpricediscount3), 2)))
            totaldiscount += totalpricediscount3
    totalprice += shipping
    totalprice = str(round((totalprice), 2))
    print('--------------------')
    print('Total Discounts: -$'+str(round((totaldiscount), 2)))
    print('')
    print(totalprice) 
    print('Order Total: $'+str(totalprice))


def main():
    'computes the total cost of purchasing a crate of items given the price and percentage of crate space consumed'
    'asks the customer for coupon codes and apply the associated discounts'
    'provide the customer a summary of their order'
    print_logo()
    a = select_items()
    b = get_coupons()
    if a[1] == 0:               #easter egg,  printed if the crate is completely empty
        print('Enjoy your Hamilton, NY air!')
    else:
        c = display_summary(a[0], a[1], b)



if __name__ == "__main__":
    main()
