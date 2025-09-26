def solution(word):
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(current_word):
        words.append(current_word)
        
        if len(current_word) == 5:
            return
            
        for vowel in vowels:
            dfs(current_word + vowel)

    for vowel in vowels:
        dfs(vowel)
        
    return words.index(word) + 1