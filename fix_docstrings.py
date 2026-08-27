#!/usr/bin/env python3
"""
修复 captcha_model.py 中的文档字符串问题
将 \"\"\" ... \"\"\" 替换为三重引号文档字符串
"""

import sys
import os

file_path = r"D:\allin\not\OK\captcha_demo\model\captcha_model.py"

# 读取文件
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 修复每一行
fixed_count = 0
for i, line in enumerate(lines):
    if '\\"\\"\\"' in line:
        lines[i] = line.replace('\\"\\"\\"', '"""')
        fixed_count += 1

# 写回文件
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"已修复: {file_path}")
print(f"修复了 {fixed_count} 行")
