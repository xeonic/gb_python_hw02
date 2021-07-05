# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

l_season = ['winter', 'spring', 'summer', 'autumn']
d_season = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer',
            7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
while True:
    try:
        month = int(input('Input number in range from 1 to 12 - '))
        if 0 < month <= 12:
            break
        else:
            print('Input number in range from 1 to 12')
    except ValueError:
        print('Input number!')

print('List solution:', l_season[0 if (month > 11 or month < 3) else month // 3])
print('Dict solution:', d_season.get(month))
