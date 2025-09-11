N = int(input())

options = [input() for _ in range(N)]

used_shortcuts = set()
sequence = []

for option in options:
    shortcut_assigned = False
    
    words = option.split(' ')
    
    for i, word in enumerate(words):
        if not word:
            continue
        
        first_char = word[0]
        if first_char.upper() not in used_shortcuts:
            used_shortcuts.add(first_char.upper())
            
            words[i] = '[' + word[0] + ']' + word[1:]
            print(' '.join(words))
            
            shortcut_assigned = True
            break
    if shortcut_assigned:
        continue
    
    for i, char in enumerate(option):
        if char == ' ':
            continue
        
        if char.upper() not in used_shortcuts:
            used_shortcuts.add(char.upper())
            
            result = option[:i] + '[' + char + ']' + option[i + 1:]
            print(result)
            
            shortcut_assigned = True
            break
    
    if not shortcut_assigned:
        print(option)