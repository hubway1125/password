#密碼重試程式

#先在程式碼中設定密碼 password = 'a123456'
#讓使用者[最多輸入3次密碼]
#不對的話，就印出"密碼錯誤! 還有__次機會"
#對的話，印出"登入成功!"

password = "a123456"
i = 0

while i < 3 :
	chance = 2 - i
	answer = input("請輸入密碼: ")
	if answer != password:
		print("密碼錯誤! 還有%s次機會" % chance)
		i += 1
	else:
		print("登入成功!")
		break



