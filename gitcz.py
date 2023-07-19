import os

# type:     commit 的类型

# feat:     新特性
# fix:      修改问题
# refactor: 代码重构
# docs:     文档修改
# style:    代码格式修改, 注意不是 css 修改
# test:     测试用例修改
# chore:    其他修改, 比如构建流程, 依赖管理.

# scope:    commit 影响的范围, 比如: route, component, utils, build...
# subject:  commit 的概述, 建议符合 50/72 formatting
# body:     commit 具体修改内容, 可以分为多行, 建议符合 50/72 formatting
# footer:   一些备注, 通常是 BREAKING CHANGE 或修复的 bug 的链接.

list=["feat","fix","refactor","docs","style","test","chore"]

print("git cz generator via python")
os.system("pause")

print("""
一、commit类型（type）
0 feat:     新特性
1 fix:      debug
2 refactor: 代码重构（不是新增功能，也不是修改bug的代码变动）
3 docs:     文档修改
4 style:    代码格式修改，不影响原有功能运行
5 test:     测试用例修改
6 chore:    其他修改, 比如构建流程、依赖管理"""
)
i=input("键入数字：")
i=int(i)
if 0<=i<=6:
    print("选择了：",list[i])
else:
    raise ValueError("必填项")

print("""
二、commit影响范围（scope）
不能换行，输入方法、文件名等，回车以跳过""")
scope=input("键入文本：")
if scope:
    print("键入了：",scope)

print("""
三、commit提要（subject）
不能换行，长度不要超过72列"""
)
subject=input("键入文本：")
if subject:
    print("键入了：",subject)
else:
    raise ValueError("必填项")

print("""
四、commit描述（body）
多行输入，超过72列要换行哦~
输入空行以退出
键入文本："""
)
body_list=[]
body=""
while True:
    body=input()
    body_list.append(body)
    if not body:
        body_list.pop()
        break
print("键入了：")
for item in body_list:
    print(item)

print("""
五、commit脚注（footer）
一些备注, 通常是 BREAKING CHANGE 或修复的 bug 的链接（issue）.
是否有BREAKING CHANGE？输入提要"""
)
temp=input("键入y/n：")
brkchg=""
if temp=="y":
    brkchg=input("键入文本：")
    if brkchg:
        print("键入了：",brkchg)
    else:
        raise ValueError("必填项")
elif temp!="n":
    raise ValueError("必填项")

print("是否有issue解决了？输入e.g.#114, #514")
temp=input("键入y/n：")
issues=""
if temp=="y":
    issues=input("键入文本：")
    if issues:
        print("键入了：",issues)
    else:
        raise ValueError("必填项")
elif temp!="n":
    raise ValueError("必填项")

print("\n已生成commit如下：")
print(f"{list[i]}({scope}): {subject}\n")
for item in body_list:
    print(item)
if len(body_list)!=0:
    print()
if brkchg:
    print(f"BREAKING CHANGE:\n{brkchg}")
    if issues:
        print()
if issues:
    print(f"Closes {issues}")

input()