import json
import re
import os
import subprocess

PATTERN = re.compile(r"<td>([a-zA-Z\d\s\-]+)</td>\s*<td>([^(<]+)\s*</td>\s*(?:<td>(?:[^<]+)\s*</td>)?</tr>")
EXTRA_TRANSLATIONS ={
    "shelf": "展示架",
    "data value": "数据值",
    "block state": "方块状态",
    "argument": "参数",
    "parameter": "参数",
    "sprite": "精灵图",
    "variant": "变种",
    "job site": "工作站点",
    "workplace": "工作站点"
}
URL = 'https://zh.minecraft.wiki/w/Minecraft_Wiki:译名标准化?variant=zh-cn'
print('Getting translations from Minecraft Wiki...')
result = subprocess.run(['curl', '-H', 'Accept-Charset: utf-8', URL],
                         text=True, capture_output=True, check=True ).stdout
print('Parsing translations...')
translations = {}
for en,zh in re.findall(PATTERN, result):
    en = en.lower()
    zh = zh.replace("\n","")
    if zh == '-':
        translations[en] = en
    else:
        translations[en] = zh
translations.update(EXTRA_TRANSLATIONS)
print('Writing translations to file...')
with open(f'data{os.sep}translations.json','w', encoding='utf-8') as file:
    json.dump(translations, file, ensure_ascii=False, indent=2)
print('Done.')