def solution(sizes):
    garo_max = 0
    sero_max = 0
    
    for card in sizes:

        if(card[0] < card[1]):
            temp = card[0]
            card[0] = card[1]
            card[1] = temp
    
    for card in sizes:
        
        if(garo_max<card[0]):
            garo_max = card[0]
        if(sero_max<card[1]):
            sero_max = card[1]
    
                     
    answer = sero_max * garo_max
    return answer







# def solution(sizes):
#     # 명함을 회전시켜 큰 값을 가로, 작은 값을 세로로 정렬한 뒤 최대값 계산
#     garo_max = 0
#     sero_max = 0
    
#     for w, h in sizes:
#         w, h = max(w, h), min(w, h)  # 큰 값은 가로, 작은 값은 세로로
#         garo_max = max(garo_max, w)  # 가로 최대값 갱신
#         sero_max = max(sero_max, h)  # 세로 최대값 갱신
    
#     return garo_max * sero_max