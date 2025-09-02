def solution(info, query):
    # db[4][3][3][3]
    db = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]
    answer = []
    
    # mappings
    lang_map = { "-": 0, "cpp": 1, "java": 2, "python": 3 }
    job_map = { "-": 0, "backend": 1, "frontend": 2 }
    role_map = { "-": 0, "junior": 1, "senior": 2 }
    food_map = { "-": 0, "chicken": 1, "pizza": 2 }
    
    # indexing
    for column_info in info:
        lang, job, role, food, score = column_info.split(" ")
        
        for a in [0, lang_map[lang]]:
            for b in [0, job_map[job]]:
                for c in [0, role_map[role]]:
                    for d in [0, food_map[food]]:
                        db[a][b][c][d].append(int(score))
    
    # sorting
    for a in range(4):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    db[a][b][c][d].sort()
                    
    # querying
    for column_query in query:
        tokens = column_query.split(" ")
        lang, job, role, food, score = tokens[0], tokens[2], tokens[4], tokens[6], int(tokens[7])
        scores = db[lang_map[lang]][job_map[job]][role_map[role]][food_map[food]]
        
        size = len(scores)
        first, last = 0, size
        
        while first < last:
            mid = (first + last) // 2
            
            if score <= scores[mid]:
                last = mid
            
            else:
                first = mid + 1
        
        answer.append(size - first)
    
    return answer