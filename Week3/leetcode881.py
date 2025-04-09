def numRescueBoats(people, limit):
    # 按體重排序
    people.sort()
    
    # 初始化雙指針
    left, right = 0, len(people) - 1
    boats = 0
    
    # 使用雙指針配對
    while left <= right:
        # 嘗試配對最輕和最重的人
        if people[left] + people[right] <= limit:
            left += 1  # 最輕的人可以與最重的人同船
        # 無論是否配對成功，最重的人都會乘一艘船
        right -= 1
        boats += 1
    
    return boats