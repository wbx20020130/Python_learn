# -*- coding: utf-8 -*-
# @Time    : 2025/3/28
# @Author  : Your Name
# @File    : contacts_manager.py

def menu():
    print("-" * 40)
    print("通讯录管理系统")
    print("1. 添加联系人信息\t2. 删除联系人信息\t3. 修改联系人信息")
    print("4. 查询联系人信息\t5. 显示所有联系人信息\t6. 退出系统")
    print("-" * 40)

contacts = []

# 添加联系人信息
def add_contact():
    contact = {}
    contact["name"] = input("请输入联系人姓名: ")
    contact["age"] = int(input("请输入联系人年龄: "))
    contact["phone"] = input("请输入联系人电话: ")
    contacts.append(contact)
    print("联系人信息添加成功!")
    print(contacts)

# 删除联系人信息
def delete_contact():
    name = input("请输入要删除的联系人姓名: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("联系人信息删除成功!")
            print(contacts)
            break
    else:
        print("没有找到要删除的联系人信息!")

# 修改联系人信息
def modify_contact():
    name = input("请输入要修改的联系人姓名: ")
    for contact in contacts:
        if contact["name"] == name:
            contact["name"] = input("请输入修改后的姓名: ")
            contact["age"] = int(input("请输入修改后的年龄: "))
            contact["phone"] = input("请输入修改后的电话: ")
            print("联系人信息修改成功!")
            print(contacts)
            break
    else:
        print("未找到联系人信息!")

# 查询联系人信息
def search_contact():
    name = input("请输入要查询的联系人姓名: ")
    for contact in contacts:
        if contact["name"] == name:
            print(f'联系人姓名：{contact["name"]}, 年龄：{contact["age"]}, 电话：{contact["phone"]}')
            break
    else:
        print("未查询到联系人信息！")

# 显示所有联系人信息
def show_all_contacts():
    for contact in contacts:
        print(f'联系人姓名：{contact["name"]}, 年龄：{contact["age"]}, 电话：{contact["phone"]}')

while True:
    menu()
    user_choice = int(input("请输入您要操作的功能编号: "))
    if user_choice == 1:
        add_contact()
    elif user_choice == 2:
        delete_contact()
    elif user_choice == 3:
        modify_contact()
    elif user_choice == 4:
        search_contact()
    elif user_choice == 5:
        show_all_contacts()
    elif user_choice == 6:
        print("感谢使用通讯录管理系统")
        break
    else:
        print("输入信息错误，请重新输入!")
