import os
import re

with open(r'C:\Projects\beamer\win_app\kvm_bridge_win.py', 'r', encoding='utf-8') as f:
    content = f.read()

reps = [
    ('Type this code into Beamer on the Mac.', 'Type this code into Beamer on the other PC.'),
    ('Waiting for your Mac', 'Waiting for the other PC'),
    ('Mac connected', 'Other PC connected'),
    ('Ctrl arrives on the Mac as Command and the Windows key as Control, so Ctrl+C copies there too.', 'Ctrl and Windows keys are swapped so shortcuts mapped to Ctrl on this PC will map to the Windows key on the other PC.'),
    ('Each key arrives as the Mac key in the same place: Ctrl as Control, the Windows key as Command.', 'Each key arrives exactly as it is: Ctrl as Ctrl, and Windows key as Windows key.'),
    ('Your Mac drives this PC', 'The other PC drives this PC'),
    ('This PC drives your Mac', 'This PC drives the other PC'),
    ('Not connected to the Mac', 'Not connected to the other PC'),
    ('Send input to your Mac', 'Send input to the other PC'),
    ('Where your Mac is', 'Where the other PC is'),
    ('On your Mac', 'On the other PC'),
    ('your Mac tells this PC', 'the other PC tells this PC'),
    ('Mac sets how its own edge', 'other PC sets how its own edge'),
    ('Your Mac', 'Other PC'),
    ('Pair a Mac', 'Pair a PC'),
    ('Pair a different Mac', 'Pair a different PC'),
    ('Press Pair a Mac, then on your Mac choose this PC', 'Press Pair a PC, then on the other PC choose this PC'),
    ('Not listed on the Mac?', 'Not listed on the other PC?'),
    ('The Mac runs a different version of Beamer. Update Beamer on both machines, then pair again.', 'The other PC runs a different version of Beamer. Update Beamer on both machines, then pair again.'),
    ('Your Mac\'s IP address:', 'Other PC\'s IP address:'),
    ('The Mac\'s address', 'The other PC\'s address'),
    ('Learned the Mac at %s', 'Learned the other PC at %s'),
    ('The Mac took input', 'The other PC took input'),
    ('the Mac only while the Mac has input', 'the other PC only while the other PC has input'),
    ('a Mac dropping and reconnecting', 'a PC dropping and reconnecting'),
    ('The Mac\'s name', 'The other PC\'s name'),
    ('One keyboard and mouse for your Mac and PC.', 'One keyboard and mouse for your two PCs.'),
    ('paired_with or "Your Mac"', 'paired_with or "Other PC"'),
    ('paired_with or "your Mac"', 'paired_with or "the other PC"'),
    ('who = mac_name or "your Mac"', 'who = pc_name or "the other PC"'),
    ('"the Mac"', '"the other PC"'),
    ('your Mac', 'the other PC'),
    ('the Mac', 'the other PC'),
    ('The Mac', 'The other PC'),
]

for old, new in reps:
    content = content.replace(old, new)

with open(r'C:\Projects\beamer\win_app\kvm_bridge_win.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Bridge strings replaced.")
