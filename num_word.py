
a_bit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
ten_twenty = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
ten_bit = ['twenty', 'thirt', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

inputnum = raw_input('Eneter one num: ')
numlength = len(inputnum)
print numlength
fact_num = int(inputnum)

if numlength < 2:
    print a_bit[fact_num]
elif 2 <= numlength and numlength < 3:
    if fact_num == 10:
        print a_bit[10]
    elif fact_num <= 20:
        print ten_twenty[fact_num % 2 - 1]
    else:
        tenbit_abit = a_bit[fact_num % 10]
        fact_num = fact_num/10;
        print ten_twenty[fact_num - 1] + "-" + tenbit_abit