# 定义一个列表来存储所有学生信息
student_info = []

while True:
    # 1-指定展示界面
    print('==============欢迎登录学生管理系统==============')
    print('================1、添加学生数据================')
    print('================2、删除学生数据================')
    print('================3、修改学生数据================')
    print('================4、查询学生数据================')
    print('================5、退出管理系统================')
    num = input('请选择使用功能的编号：')
    # 2-对用户输入的编号进行判断，执行不同的操作功能
    if num == '1':

        # 实现添加功能
        name = input('请输入姓名:')
        gender = input('请输入性别:')
        age = input('请输入年龄:')
        address = input('请输入地址:')
        # 定义一个字典存放新添加的学生信息
        new_info = {}
        new_info['name'] = name
        new_info['gender'] = gender
        new_info['age'] = age
        new_info['address'] = address
        student_info.append(new_info)
        print("添加成功!")
       # print(student_info)


    elif num == '2':
        # 实现删除功能
        if len(student_info) != 0:
            del_num = int(input("请输入要删除的序号:")) - 1
            if del_num < len(student_info):
                del student_info[del_num]
                print(student_info)
                print(f"删除序号{del_num + 1}成功")
            else:
                print('删除序号有误')
        else:
            print("学生信息表为空")

    elif num == '3':
        # 实现修改功能
        if len(student_info) != 0:
            change_num = int(input("请输入要修改的学生编号:")) - 1
            if change_num >= len(student_info):
                print("输入的序号有误")
            else:
                change_name = input("请输入修改的学生姓名:")
                change_gender = input("请输入修改的学生性别:")
                change_age = input("请输入修改的学生年龄:")
                change_address = input("请输入修改的学生地址:")
                student_info[change_num]['name'] = change_name
                student_info[change_num]['gender'] = change_gender
                student_info[change_num]['age'] = change_age
                student_info[change_num]['address'] = change_address
                #print(student_info)
        else:
            print("学生信息表为空")


    elif num == '4':
        # 实现查询功能
        if len(student_info) != 0:
            print("学生信息如下:")
            print("=" * 30)
            print('序号   姓名   性别   年龄    地址')
            i=1
            for tmp_info in student_info:
                print("%d    %s    %s    %s    %s"%(i,tmp_info['name'],tmp_info['gender'],tmp_info['age'],tmp_info['address']))
                i+=17777777777777
        else:
            print("学生信息表为空")

    elif num == '5':
        print('退出系统')
        break
    else:
        print('错误的输入')
