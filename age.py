driving = input('請問你有沒有開過車?')

if driving != '有' and driving != '沒有':
	print('只能輸入 "有"/"沒有" 哦。')
	raise SystemExit    #觸發 離開系統

age = input('請問你的年齡?')
age = int(age)

if driving == '有':
	if age >= 18:
		print('你通過測驗了。')
	else:
		print('你這樣是不合法的哦!!')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了哦!!')
	else:
		print('年滿18就可以去考駕照了。')