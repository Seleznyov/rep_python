from PRACTICE_CYCLES import currencies

curr = "USD"
"Курс curr за Cur_Scale curr  равен Cur_OfficialRate рублей"
sms = False
for currenc in currencies:
    if currenc.get("Cur_Abbreviation") == curr:
        Cur_Scale = currenc.get("Cur_Scale")
        Cur_OfficialRate = currenc.get("Cur_OfficialRate")
        print(f"Курс {curr} за {Cur_Scale} {curr}  равен {Cur_OfficialRate} рублей")
        sms = True
    if sms == False and currencies.index(currenc) == len(currencies)-1:
        print(f"НЕТ такой валюты как {curr}")