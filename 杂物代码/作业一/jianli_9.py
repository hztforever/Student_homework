user_name=input('请输入你的名字')
user_sex=input('请输入你的性别')
user_age=input('请输入你的年龄')
user_school=input('请输入你的学校')
print('正在生成您的简历.............')
print('*'*20)
print('\t\t\t\t简历\n')
print('姓名:'+'\t'+user_name)
print('姓名:'+'\t'+user_sex)
print('姓名:'+'\t'+user_age)
print('姓名:'+'\t'+user_school)

# 整体来说，思路清晰从输入到输出整体给出的代码清晰。
#但，对于之后的多人协作完成某个项目，就需要更加清晰快速定位，所以我们需要做出如下几点优化：
# 1.划分区域与input后的括号应使用英文输入法下的括号，不要使用中文输入法下括号！！！；
# 2.变量名再更加直观一些；（做的不错，不做示例）
# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 4.星号的优化；（你已经做到了）
# 6.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；（你无此问题）此条为提醒！
# 7.简历内容可以更加完善；（不做示例）
# 8.是否可以加个输入判断？
# 扩展可以添加一个动态效果，在这里我就不讲述，自己有兴趣去查找一下；（初步达到动态效果import time）
# 注意：文件命名不要用“-”要用这个："_":就是这样命名：my_report.py
#修改demo：
# 1.划分区域与input后的括号应使用英文输入法下的括号，不要使用中文输入法下括号！！！(此条为提醒）
#<----------------user_input_area--------------->
user_name=input('请输入你的名字')
user_sex=input('请输入你的性别')
user_age=input('请输入你的年龄')
user_school=input('请输入你的学校')
    #<----------------print_area--------------->
print('正在生成您的简历.............')
print('*'*20)
print('\t\t\t\t简历\n')
print('姓名:'+'\t'+user_name)
print('姓名:'+'\t'+user_sex)
print('姓名:'+'\t'+user_age)
print('姓名:'+'\t'+user_school)
# 2.变量名再更加直观一些:(此条为其他同学问题，作为提醒你，加深印象！)
# 因为有时候输入的内容很多，你得区分哪些是系统输入变量，哪些是人工输入变量。
# 英文版：(Because sometimes there is a lot of input, you have to distinguish between system input variables and manual input variables.)
# 在变量前面加个user即可(并尽量用英文）；
# 3.为了使代码更具有观赏性，建议：在赋值号两边加上空格；
# 修改示例：
user_name = input('请输入你的名字')
user_sex = input('请输入你的性别')
user_age = input('请输入你的年龄')
user_school = input('请输入你的学校')
# 4.星号的优化:
#多个星号这样输出：(你已经做到）
print('*'*30)  # 数字30就是你要几个星号；
# 5.在print当中，能不掉用函数尽量不调用，为了提升代码运行效率；（此条为其他同学调用format()函数,作为补充）
# 7.简历内容可以更加完善；（不做示例）

# 8.是否可以加个输入判断？
# 示例：
#输入性别并判断
while True:
    gender = input('请输入您的性别（男/女）：>')
    if gender == '男' or gender == '女':
        break
    else:
        print('性别输入错误')

#输入年龄并判断
while True:
    age = input('请输入您的年龄：>')
    if age.isdigit():
        break
    else:
        print('年龄输入错误')
    
        
# 好整体就是这样，希望下次看见你的代码有所提升哦，一起加油吧！