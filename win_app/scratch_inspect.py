import re

with open(r'C:\Projects\beamer\win_app\kvm_bridge_win.py', 'r', encoding='utf-8') as f:
    content = f.read()

init_match = re.search(r'self\.announcer = Announcer\([\s\S]+?\n', content)
if init_match:
    print("Found announcer init:", init_match.group(0))

pairing_block_match = re.search(r'def _pairing_block\([\s\S]+?def ', content)
if pairing_block_match:
    print("Found _pairing_block")
