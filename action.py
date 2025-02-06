import json
import re
import os
import subprocess

PATTERN = re.compile(r"<td>([a-zA-Z\d\s\-]+)</td>\s*<td>([^(<]+)\s*</td>\s*(?:<td>(?:[^<]+)\s*</td>)?</tr>")
EXTRA_TRANSLATIONS ={
    "data value": "数据值",
    "block state": "方块状态",
    "argument": "参数",
    "parameter": "参数",
    "sprite": "精灵图",
    "variant": "变种",
    "job site": "工作站点",
    "workplace": "工作站点"
}
URL = 'https://zh.minecraft.wiki/w/Minecraft_Wiki:%E8%AF%91%E5%90%8D%E6%A0%87%E5%87%86%E5%8C%96'
content = result = subprocess.run(['curl', URL], text=True, capture_output=True ).stdout
print(content)

translations = {}
for en,zh in re.findall(PATTERN,content):
    en = en.lower()
    zh = zh.replace("\n","")
    if zh == '-':
        translations[en] = en
    else:
        translations[en] = zh

translations.update(EXTRA_TRANSLATIONS)

with open(f'data{os.sep}translations.json','w', encoding='utf-8') as file:
    json.dump(translations, file, ensure_ascii = False)
