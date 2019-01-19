# gender = input("性别：")
# print("请输入你的性别： {}".format(gender))
# if gender =="男":
# 	print ("答对了")
# else:
# 	print("你不是！")
# score = input("你的学习成绩：")
# score = int (score)
# if  score >= 90:
# 	print("A")
# elif score >= 80:
# 	print("B")
# elif score >= 60:
# 	print("C")
# else:
# 	print("回家吧~")
# for name in ['wanglintian','wangqying','jinjing']:
# 	print(name.title())
# magicians = ['wang','lin','tian']
# for magician in magicians:
# 	print(magician.title()+ ",it is beauty")
# 	print("I can't wait to see you tommrow,"+ magician.title())
benqian = 1000
year = 0
while benqian< 2000:
	benqian = benqian * (1+0.067)
	year+= 1
	print("第{}年是{}钱".format(year,benqian))

def hello(p):
	print("{0}, 你肿么咧".format(p))
	print("Sir, 你不理额额就走咧")
	return "我已经跟{0}打招呼了，{1}不理我".format(p, p)
name = "明月"
rst = hello(name)
print(rst)