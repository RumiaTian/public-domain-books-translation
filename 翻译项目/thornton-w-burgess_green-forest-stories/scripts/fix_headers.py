import re

path = r'C:\Users\HanTi\OneDrive\translate\翻译项目\thornton-w-burgess_green-forest-stories\译文\whitefoot-the-wood-mouse.zh-CN.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Strategy: find each Original/Chinese pair and merge headers
# Pattern: ===Original===\n## ENG_HEADER\n...\n===Chinese===\n## CHN_HEADER\n...
# Replace with: ===Original===\n## ENG_HEADER / CHN_HEADER\n...\n===Chinese===\n## ENG_HEADER / CHN_HEADER\n...

# Split into blocks by ===Original=== markers
parts = re.split(r'(===Original===)', content)
# parts[0] = before first Original (the top title)
# parts[1] = ===Original===, parts[2] = content until next Original or end
# parts[3] = ===Original===, parts[4] = content, etc.

result = parts[0]  # Keep the top title as-is

for idx in range(1, len(parts), 2):
    marker = parts[idx]  # ===Original===
    block = parts[idx + 1] if idx + 1 < len(parts) else ''

    # Find the English header and Chinese header in this block
    # Block format: \n## ENG_HEADER\n...\n===Chinese===\n## CHN_HEADER\n...rest
    m = re.match(r'\n(## .+?)\n(.*?)===Chinese===\n(## .+?)\n(.*)', block, re.DOTALL)
    if m:
        eng_header = m.group(1)
        eng_content = m.group(2)
        chn_header = m.group(3)
        chn_content = m.group(4)

        # Merge headers: ## English / 中文
        eng_title = eng_header[3:]  # Remove "## "
        chn_title = chn_header[3:]  # Remove "## "
        merged_header = f'## {eng_title} / {chn_title}'

        result += marker + '\n' + merged_header + '\n' + eng_content
        result += '===Chinese===\n' + merged_header + '\n' + chn_content
    else:
        # Fallback: just append as-is
        result += marker + block

with open(path, 'w', encoding='utf-8') as f:
    f.write(result)

print('Headers fixed successfully')
