#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读取index.html文件
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 宠物和对应的介绍页面映射
pet_mappings = [
    ('小橘', 'pet_xiaoxiang_intro.html'),
    ('小黑', 'pet_xiaohei_intro.html'),
    ('雪球', 'pet_xueqiu_intro.html'),
    ('花花', 'pet_huahua_intro.html'),
    ('虎子', 'pet_huzi_intro.html'),
    ('小黄', 'pet_xiaohuang_intro.html'),
    ('斑斑', 'pet_banban_intro.html'),
    ('咪咪', 'pet_mimi_intro.html')
]

# 逐行处理
modified = False
for i, line in enumerate(lines):
    # 检查是否包含宠物名称的卡片中的"了解更多"链接
    for j, (pet_name, intro_page) in enumerate(pet_mappings):
        if pet_name in line and '了解更多' in line:
            # 如果找到包含宠物名称和"了解更多"的行，替换链接
            if 'share_detail.html' in line:
                lines[i] = line.replace('share_detail.html', intro_page)
                print(f"已替换第{j+1}个宠物({pet_name})的链接为 {intro_page}")
                modified = True
                break

# 写入修改后的内容
if modified:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print("所有链接替换完成！")
else:
    print("未找到需要替换的链接")