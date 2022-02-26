# 친구 리스트에서 자신의 모든 친구를 찾는 알고리즘
# 주석 달기

def print_all_friends(g, start): #함수 생성 g는 친구 관계 리스트, start는 친구 찾는 자신
    qu = [] # 큐 자료형 생성
    done = set() # 집합자료형 set 이용하여 집합 done 생성 

    qu.append(start) # 큐에 자료 추가
    done.add(start) # 집합에도 자료 추가  

    while qu: # 큐에 자료가 안 남을 때까지          
        p = qu.pop(0) # 큐에서 자료 꺼내서 p에 저장 
        print(p) # p 출력       
        for x in g[p]: # 자료들 중에 ex) Summer의 친구 John Justin Mike 중에
            if x not in done: # 집합 done에 추가된 적 없는 자료를
                qu.append(x) # 큐에 저장   
                done.add(x)  # 집합 done에도 저장  

# 친구 관계 리스트 생성

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'], # Summer의 친구 John Justin Mike
    'John': ['Summer', 'Justin'], # John의 친구 Summer, Justin
    'Justin': ['John', 'Summer', 'Mike', 'May'], # Justin의 친구 John Summer Mike May
    'Mike': ['Summer', 'Justin'], # Mike의 친구 Summer Justin
    'May': ['Justin', 'Kim'], # May의 친구 Justin Kim
    'Kim': ['May'], # Kim의 친구 May
    'Tom': ['Jerry'], # Tom의 친구 Jerry
    'Jerry': ['Tom'] # Jerry의 친구 Tom
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')

#출력
# Summer John Justin Mike May Kim
# 자기 자신(Summer) 출력하고 Summer의 친구 John Justin Mike 출력하고 Justin의 친구 May, May의 친구 Kim까지 출력
# Jerry Tom
# 자기 자신(Jerry) 출력하고 Jerry의 친구 Tom 출력(Tom의 친구도 Jerry)



