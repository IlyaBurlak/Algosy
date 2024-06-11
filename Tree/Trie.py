class TrieNode:
    def __init__(self):
      self.children = dict()
      self.is_termin = False

class Trie:
    def __init__(self):

        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_termin = True

    
    def search(self , word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.is_termin 



    def startswith(self , prefix: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return True


kol_el = int(input())
s_1 = input().split()
s_2 = input().split()
s_3 = input().split()

arr_1 = Trie()
arr_2 = Trie()
arr_3 = Trie()

for i in range(len(s_1)):
    arr_1.insert(s_1[i])
    arr_2.insert(s_2[i])
    arr_3.insert(s_3[i])

count_1 = 0
count_2 = 0
count_3 = 0

for i in range(len(s_1)):
    if arr_2.search(s_1[i]) and arr_3.search(s_1[i]):
        continue
    if arr_2.search(s_1[i]) or arr_3.search(s_1[i]):
        count_1 +=1
    else:
        count_1+=2

for i in range(len(s_1)):
    if arr_1.search(s_2[i]) and arr_3.search(s_2[i]):
        continue
    if arr_1.search(s_2[i]) or arr_3.search(s_2[i]):
        count_2 +=1
    else:
        count_2+=2
for i in range(len(s_1)):
    if arr_1.search(s_3[i]) and arr_2.search(s_3[i]):
        continue
    if arr_1.search(s_3[i]) or arr_2.search(s_3[i]):
        count_3 +=1
    else:
        count_3+=2

print(count_1 ,count_2 , count_3)
             


