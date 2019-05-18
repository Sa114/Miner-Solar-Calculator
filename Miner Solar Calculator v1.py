import time
loop1 = "true"
loop2 = "true"
loop3 = "true"
loop4 = "true"
clear_loop = "true"
count = 1
countROI = 1
list1 = 1
end = 1
def clear(list1,clear_loop):
    while (clear_loop == "true"):
        print(" ")
        list1 = list1 + 1
        if (list1 > 125):
            break
    return
                
print("===========================")
print("| Miner  Solar Calculator |")
print("===========================")
print("Created by MeibionCymru / Sa114")
print(" ")
print(" ")
print(" ")
mine_wattage = input("1. Enter miner wattage " )
s_d_mine_profit = input("2. Enter miner daily earnings ($) ")
s_mine_price = input ("3. Enter miner price ($) ")
total_mines = input("4. Enter ammout of mines ")
print(" ")
print(" ")
while (loop1 == "true"):
    print("Please confirm values")
    print("1. Miner Wattage = " + mine_wattage + "w")
    print("2. Daily Earnings = $" + s_d_mine_profit)
    print("3. Miner Price = $" + s_mine_price)
    print("4. Total Mines = " + total_mines)
    print(" ")
    print("Enter Y to continue with current values.")
    print("To edit a value, enter the number you would like to edit.")
    miner_check_1 = input("Make Selection: ")
    miner_check_1 = str.upper(miner_check_1)
    print(" ")
    print(" ")

    if (miner_check_1 == "1"):
        mine_wattage = input("1. Enter miner wattage " )
    elif (miner_check_1 == "2"):
        s_d_mine_profit = input("2. Enter miner daily earnings ($)")
    elif (miner_check_1 == "3"):
        s_mine_price = input ("3. Enter miner price ($) ")
    elif (miner_check_1 == "4"):
        total_mines = input("4. Enter ammout of mines ")
    elif (miner_check_1 == "Y"):
        break
        loop1 == "false"
    else:
        print("Something went wrong! Please check your selection.")

clear(list1,clear_loop)
clear_loop = "true"
print("Miner Information Saved...")
print("===========================")
print("| Miner  Solar Calculator |")
print("===========================")
print(" ")
print(" ")
print(" ")

s_pannel_wattage = input("1. Enter pannel wattage ")
s_pannel_price = input("2. Enter price per pannel ($) ")
t_pannel_ammount = input("3. Enter ammount of pannels (Leave blank for suggested ammount) ")
print(" ")
print(" ")
while (loop2 == "true"):
    print("Please confirm values")
    print("1. Pannel Wattage = " + s_pannel_wattage + "w")
    print("2. Price Per Pannel = $" + s_pannel_price)
    print("3. Ammount of pannels = " + t_pannel_ammount)
    print(" ")
    print("Enter Y to continue with current values.")
    print("To edit a value, enter the number you would like to edit.")
    solar_check_1 = input("Make Selection: ")
    solar_check_1 = str.upper(solar_check_1)
    print(" ")
    print(" ")

    if (solar_check_1 == "1"):
        s_pannel_wattage = input("Enter pannel wattage ")
    elif (solar_check_1 == "2"):
        s_pannel_price = input("Enter price per pannel ($) ")
    elif (solar_check_1 == "3"):
        t_pannel_ammount = input("3. Enter ammount of pannels (Leave blank for suggested ammount) ")
    elif (solar_check_1 == "Y"):
        break
        loop2 == "false"
    else:
        print("Something went wrong! Please check your selection.")

clear(list1,clear_loop)
clear_loop = "true"
print("Solar Information Saved...")
print("===========================")
print("| Miner  Solar Calculator |")
print("===========================")
print(" ")
print(" ")
print(" ")
print("Important - Any upcoming RED errors will be caused by BAD INPUTS")
print("Processing.. ")

mine_wattage = float(mine_wattage)
total_mines = float(total_mines)
t_mine_wattage = mine_wattage * total_mines
t_247_mine_wattage = t_mine_wattage * 2

s_d_mine_profit = float(s_d_mine_profit)
t_d_mine_profit = s_d_mine_profit * total_mines
t_w_mine_profit = t_d_mine_profit * 7
t_m_mine_profit = t_d_mine_profit * 30
t_y_mine_profit = t_d_mine_profit * 365

s_mine_price = float(s_mine_price)
t_mine_price = s_mine_price * total_mines


s_pannel_wattage = float(s_pannel_wattage)
s_pannel_price = float(s_pannel_price)

t_solar_wattage = mine_wattage * total_mines
t_solar_percent = t_mine_wattage / 5
sug_solar_wattage = t_solar_wattage + t_solar_percent

if (t_pannel_ammount == ""):
    counted_wattage = s_pannel_wattage
    while(counted_wattage < t_247_mine_wattage):
        if (counted_wattage > t_247_mine_wattage):
            break
        counted_wattage = counted_wattage + s_pannel_wattage
        count = count + 1
        t_pannel_ammount = count
        
    while(counted_wattage > t_247_mine_wattage):
        old_counted_wattage = counted_wattage
        counted_wattage = counted_wattage + t_solar_percent
        t_pannel_wattage = counted_wattage
        t_pannel_ammount = count
        break

    while(old_counted_wattage < counted_wattage):
        if (old_counted_wattage > counted_wattage):
            break
        old_counted_wattage = old_counted_wattage + s_pannel_wattage
        count = count + 1
        t_pannel_ammount = count
        sug_pannel_print = "Reccomended pannels have been calculated."
 
    
else:
    t_pannel_ammount = float(t_pannel_ammount)
    t_pannel_wattage = s_pannel_wattage * t_pannel_ammount
    if (sug_solar_wattage > t_pannel_wattage):
        sug_pannel_print = "More pannels suggested, insufficient wattage for 24/7 use."
    else:
        sug_pannel_print = "Pannel ammount is sufficient for 24/7 use."


t_pannel_price = s_pannel_price * t_pannel_ammount
o_price = t_pannel_price + t_mine_price

o_ROI = t_m_mine_profit
while (o_ROI < o_price):
    if (o_ROI >= o_price):
        break
    o_ROI = o_ROI + t_m_mine_profit
    countROI = countROI + 1

print(" ")
print(" ")
print(" ")
print("- Miner Stats - ")
print(" ")
print(" ")
print("Mine Daily Earnings: $" + str(t_d_mine_profit))
print("Mine Weekly Earnings: $" + str(t_w_mine_profit))
print("Mine Monthly Earnings: $" + str(t_m_mine_profit))
print("Mine Annual Earnings: $" + str(t_y_mine_profit))
print(" ")
print("Total Miner Wattage:" + str(t_mine_wattage) + "w")
print("Total Miner Price: $" + str(t_mine_price))
print(" ")
print(" ")
print("- Solar Stats - ")
print(" ")
print("Amount Of Solar Pannels: " + str(t_pannel_ammount) + " (approx)")
print("Total Solar Pannel Wattage: " + str(t_pannel_wattage) + "w")
print("Total Solar Pannel Cost: $" + str(t_pannel_price))
print(sug_pannel_print)
print(" ")
print(" ")
print("- Overall Stats - ")
print(" ")
print("Overall Cost: $" + str(o_price))
print("ROI Time : " + str(countROI) + " Months (approx)")

while(loop4 == "true"):
    end = end + 1
