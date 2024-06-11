import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left" , "right"])):

    def walk(self , code , acc):
        self.left.walk(code , acc + "1")
        self.right.walk(code , acc + "0")

class Leaf(namedtuple("Leaf", ["char"])): # Если один символ 

    def walk(self , code , acc):
        code[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for ch , freq in Counter(s).items():    # Строим очередь по приоритету
        h.append((freq , len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:                            # Строим дерево 
        freq1, _count1 , left = heapq.heappop(h)
        freq2, _count2 , right = heapq.heappop(h)

        heapq.heappush(h , (freq1 + freq2 , count , Node(left, right))) # добовляем элкмент по сумме частот  24 и 25 стороока 

        count +=1
    code = {}
    if h:
        [(_freq , _count , root)] = h
        root.walk(code , "")
    return code 

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code) , len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch , code[ch]))
    print(encoded)

if __name__ == "__main__":
    main() 



