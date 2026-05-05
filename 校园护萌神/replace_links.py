import re

# 读取index.html文件
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 替换所有的share_detail.html链接为对应的宠物介绍页面
# 按顺序替换，前8个链接分别对应8个宠物
pets_links = [
    'pet_xiaoxiang_intro.html',   # 小橘
    'pet_xiaohei_intro.html',     # 小黑  
    'pet_xueqiu_intro.html',      # 雪球
    'pet_huahua_intro.html',      # 花花
    'pet_huzi_intro.html',        # 虎子
    'pet_xiaohuang_intro.html',   # 小黄
    'pet_banban_intro.html',      # 斑斑
    'pet_mimi_intro.html'         # 咪咪
]

# 使用正则表达式找到所有的share_detail.html链接并按顺序替换
share_links = re.findall(r'href="share_detail\.html"', content)
print(f"找到 {len(share_links)} 个share_detail.html链接")

# 按顺序替换前8个链接
for i, pet_link in enumerate(pets_links):
    if i < len(share_links):
        # 找到第i个匹配项并替换
        match = re.search(r'(href=")share_detail\.html(")', content)
        if match:
            content = content.replace(match.group(0), f'href="{pet_link}"', 1)
            print(f"已替换第{i+1}个链接为 {pet_link}")

# 写入修改后的内容
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("链接替换完成！")