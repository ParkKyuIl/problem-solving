class Node: # 노드 클래스 생성
    def __init__(self, data, prev = None, next = None): # 생성자, 셀프와, 데이터값, 그리고 이전값 포인터, 다음값 포인터
        self.data = data # 받은 값을 셀프에 할당
        self.prev = prev # 생성자이기 때문에 할당되도 None으로 할당
        self.next = next # 생성자이기 때문에 할당되도 None으로 할당

class DLinkedList: #더블링크드리스트 클래스 선언
    def __init__(self): # 더블링크드리스트 생성자 선언
        self.head = None  # 전체 링크드리스트이 첫번째 노드인 head 생성, 그러나 첫 생성시에 내부에는 노드가 없으므로  None 
    
    def insert(self, data):  # (끝에 넣는것)삽입 메서드, 객체 자체인 self와 data값을 매개변수로 요구 한다. 
        if self.head == None:   # 값을 넣는데, 만약에 head가 없다면, 즉 빈 리스트이면?
            self.head = Node(data)  # 해당 값을 이용하여 노드 객체를 만들고, 이를 헤드로 지정 해준다. 
        else:   # 만약 리스트 안에 노드가 존재한다면
            node = self.head # head 객체를 노드에 할당
            
            while node.next: # 그리고 head로 부터 시작해서 노드의 next가 존재할때 까지, 즉 끝에 달할때 까지
                node = node.next # 다음값 포인터를 이용하여 계속 뒤로 움직인다. 
                                 # 그리고 아까 위의 조건대로 끝에 달하면 while 문 탈출
                
            temp = Node(data)  # 아까 받은 data를 토대로 노드를 하나 만들고
            node.next = temp   # 위의 temp 객체를 아까 끝에 도달한 노드가 다음값으로 가르키게 하고
            temp.prev = node   # 끝에 도달한 노드가 temp(insert 할 값)의 이전값이 되게 한다.

            # 요약: 헤드 받아서 끝까지 쭉 탐색해서 끝의 노드를 끝 노드로 기억했다가
            # 끝에 insert할 데이터 가진 temp 하나 만들어서 temp의 prev이 끝 노드가 되게 하고 
            # 끝 노드의 다음값을 temp를 가르키게 하면 맨 끝에 노드가 하나 추가 되는 원리
    
    def descend(self):  # 걍 출력임
        node = self.head
        
        while node:   # 노드 없을때 까지 반복해서 출력
            print(node.data)
            node = node.next
    
    def delete(self, data): # 삭제 
        if self.head == None: # head가 없다면, 즉 리스트가 비었다면
            return False  # false 리턴
        
        if self.head.data == data:  # 만약에 삭제하려는 데이터가 head의 데이터면?
            temp = self.head          # 헤드를 temp에 저장하고 
            self.head = self.head.next # 지울꺼니까 헤드의 다음값을 본인으로 두게 하고
            self.head.prev = None # prev은 None으로, 근데 왜 prev은 굳이 None이지??
            del temp # 지우기
        
        else:
            node = self.head #객체의 head를 노드로 설정 

            while node.next:              # next가 존재할때까지 탐색 (끝까지)
                if node.next.data == data: # 지우고자 하는 데이터가 그 다음에 있다면?  
                    temp = node.next    # # 그전의 노드의 다음값을 temp에 저장을 하고
                    node.next = node.next.next # 지우고자 하는 노드의 다음값을 그전의 노드의 다음값으로 할당
                    
                    if node.next == None: # 그다음 노드가 없다면
                        pass              # 암것도 안하고 패스
                    else:
                        node.next.prev = node # 아니라면 노드 그다음(지우려고 하는 노드, 그 다음거)의 prev을 노드에 저장 
                                              # 앞에 꺼와 뒤에꺼를 연걸하는 작업
                     
                    del temp   # 메모리 삭제
                
                else:
                    node = node.next  # 위에 node.next.data == data가 (현재 노드의 다음 노드가 우리가 삭제하려는 노드가 아니면)
                                      # 그 다음노드로 전진


#Test Code
dLinked_list = DLinkedList()

for a in range(1, 10):
    dLinked_list.insert(a)

dLinked_list.descend()

dLinked_list.delete(1)
dLinked_list.delete(9)
dLinked_list.delete(8)
dLinked_list.delete(101)


dLinked_list.descend()

print(dLinked_list.head.next.prev.data)