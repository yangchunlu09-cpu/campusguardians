import re

# 读取index.html文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 定义宠物和对应的介绍页面
pets_mapping = [
    ('小橘', 'pet_xiaoxiang_intro.html'),
    ('小黑', 'pet_xiaohei_intro.html'),
    ('雪球', 'pet_xueqiu_intro.html'),
    ('花花', 'pet_huahua_intro.html'),
    ('虎子', 'pet_huzi_intro.html'),
    ('小黄', 'pet_xiaohuang_intro.html'),
    ('斑斑', 'pet_banban_intro.html'),
    ('咪咪', 'pet_mimi_intro.html')
]

# 找到所有宠物卡片并替换链接
count = 0
for pet_name, intro_page in pets_mapping:
    # 使用正则表达式匹配包含宠物名称的卡片中的"了解更多"链接
    pattern = f'({pet_name}.*?href=")share_detail.html(".*?</a>)'
    replacement = f'\\1{intro_page}\\2'
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        content = new_content
        count += 1
        print(f"已替换 {pet_name} 的链接为 {intro_page}")

# 如果正则表达式没有匹配到，使用更简单的方法
if count == 0:
    # 替换所有的share_detail.html链接为第一个宠物介绍页面（然后我们需要手动调整）
    content = content.replace('href="share_detail.html"', 'href="pet_xiaoxiang_intro.html"')
    print("已使用备用方法替换链接")

# 写入修改后的内容
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"修改完成，共替换了 {count} 个链接")