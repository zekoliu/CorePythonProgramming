
dollar = 0.74
total_cents = (int)(dollar * 100)
twentyfive_cent = 0
ten_cent = 0
five_cent = 0
one_cent = 0
while (total_cents > 0):
        if (total_cents >= 25):
            twentyfive_cent = total_cents / 25
            total_cents = total_cents % 25
        elif (total_cents >= 10):
            ten_cent = total_cents % 10
            total_cents = total_cents / 10
        elif (total_cents >= 5):
            five_cent = total_cents / 5
            total_cents = total_cents % 5
        else:
            one_cent = total_cents
            total_cents = 0

print  twentyfive_cent," ",  ten_cent, " ", five_cent, " ", one_cent