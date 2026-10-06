import os
import re

def rep(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        if isinstance(old, re.Pattern):
            content = old.sub(new, content)
        else:
            content = content.replace(old, new)
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

pages_rep = [
    ('Pair with your Mac here', 'Pair with the other PC here'),
    ('moves input to your Mac', 'moves input to the other PC'),
    ('arrive on your Mac', 'arrive on the other PC'),
    ('how fast your Mac\'s pointer', 'how fast the other PC\'s pointer'),
    ('push toward your Mac', 'push toward the other PC'),
    ('lets your Mac in', 'lets the other PC in'),
    ('your Mac\'s IP address', 'the other PC\'s IP address'),
    ('your Mac keeps its own', 'the other PC keeps its own'),
    ('your Mac is on', 'the other PC is on'),
    ('your Mac\'s edge', 'the other PC\'s edge'),
    ('at your Mac\'s notch', 'at the other PC\'s notch'),
    ('Mac\'s is', 'other PC\'s is'),
    ('Mac is on', 'other PC is on'),
    ('Mac is', 'other PC is'),
    ('Mac sits', 'other PC sits'),
    ('Mac\'s own ways', 'other PC\'s own ways'),
    ('to your Mac', 'to the other PC'),
    ('from your Mac', 'from the other PC'),
    ('into your Mac', 'into the other PC'),
    ('drives your Mac', 'drives the other PC'),
    ('connected to your Mac', 'connected to the other PC'),
    ('drives this Mac', 'drives this PC'),
    ('Mac tells this PC', 'other PC tells this PC'),
    ('your Mac', 'the other PC'),
    ('the Mac', 'the other PC'),
    ('"semantic", "semantic") == "positional"', '"modifier_style", "positional") == "positional"'),
    ('MODIFIER_NOTES', 'MODIFIER_NOTES_REPLACED')
]

rep(r'C:\Projects\beamer\win_app\pages_win.py', pages_rep)

diagram_rep = [
    ('your Mac\'s', 'the other PC\'s'),
    ('your Mac', 'the other PC'),
    ('"Your Mac"', '"Other PC"'),
    ('the Mac\'s', 'the other PC\'s'),
    ('the Mac', 'the other PC'),
    ('Mac on', 'other PC on'),
]

rep(r'C:\Projects\beamer\win_app\diagram.py', diagram_rep)

sender_rep = [
    ('to the Mac', 'to the other PC'),
    ('from the Mac', 'from the other PC'),
    ('Mac\'s', 'other PC\'s'),
    ('Mac is', 'other PC is'),
    ('the Mac', 'the other PC'),
    ('Waking your Mac…', 'Waking the other PC…'),
    ('Your Mac did not wake', 'The other PC did not wake'),
    ('OLD_RECEIVER_STATUS ="The Mac', 'OLD_RECEIVER_STATUS ="The other PC'),
    ('older Beamer; update it', 'older Beamer; update both apps'),
    ('AUTH_FAILED_STATUS = "The Mac', 'AUTH_FAILED_STATUS = "The other PC'),
    ('Not connected to the Mac', 'Not connected to the other PC'),
    ('"modifier_style", "semantic"', '"modifier_style", "positional"'),
]

rep(r'C:\Projects\beamer\win_app\sender.py', sender_rep)

config_rep = [
    ('to the Mac', 'to the other PC'),
    ('the Mac', 'the other PC'),
    ('Mac\'s', 'other PC\'s'),
    ('modifier_style: str = "semantic"', 'modifier_style: str = "positional"'),
]

rep(r'C:\Projects\beamer\win_app\app_config.py', config_rep)

print("Done string replacements.")
