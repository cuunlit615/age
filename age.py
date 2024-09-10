driving = input('開過車嗎?')
if driving != '有'  and driving != '沒有':
    print('只能輸入有/沒有')
    raise SystemExit

age = int(input('請問你幾歲?'))

if driving == '有':
    if age >= 18:
        print('原來如此')
    else:
        print('How???')
else:
    if age >= 18:
        print('原來如此，可以考慮一下')
    else:
        print('過幾年後就可以考駕照啦')