def solution(skill, skill_trees):
    answer = 0
    new_skill_trees = []
    for tree in skill_trees:
        new_skill = ''
        for char in tree:
            if char in skill:
                new_skill += char
        
        if skill.startswith(new_skill):
            answer += 1
    return answer