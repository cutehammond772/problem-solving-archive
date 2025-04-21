def convertSpellToOrder(spell):
    size = len(spell)
    result = 0
    
    for i in range(size):
        order = ord(spell[i]) - 97
        result += (26 ** (size - (i + 1))) * (order + 1)
    
    return result

def convertOrderToSpell(order):
    characters = []
    
    while order > 0:
        # 'z'가 포함된 경우
        if order % 26 == 0:
            characters.append('z')
            order = (order - 26) // 26
            continue
        
        # 'z'가 아닌 경우
        num = order % 26
        
        characters.append(chr(96 + num))
        order = order // 26
    
    return "".join(reversed(characters))

def solution(n, bans):
    orders = [*map(convertSpellToOrder, bans)]
    orders.sort()
    
    count = 0
    
    for order in orders:
        if n < order:
            break
            
        n += 1
    
    answer = convertOrderToSpell(n)
    return answer