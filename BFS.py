# -*- coding: utf-8 -*-
#問題１　Jacobから自分までのステップ数をだす
#始める人と終わる人を手入力で任意に決められるようなプログラムも考えてみました(一番下のコメント)
def __logging(visited, rest=[]):
    print("visited:%s\n   rest:%s\n" % (visited, rest))


def bfs(graph, start, end):
    queue = [start]
    visited = []
    while queue:
        label = queue.pop(0)
        if label == end:
            visited.append(label)
            #__logging(visited, queue)   #導出過程を出せる
            return visited
        if label not in visited:
            visited.append(label)
            queue += graph.get(label, [])
            #queue += [x for x in graph.get(label, []) if x not in visited]　#こっちでもいい
        #__logging(visited, queue)    #導出過程を出せる
    return visited

def read_link(filename):
    links = open(filename, "r")
    LinksLines = links.readlines()
    links.close()
    return LinksLines

def read_name(filename):
    nicknames = open(filename, "r")
    NicknameLines = nicknames.readlines()
    nicknames.close()
    CorrespondenceTable = {}
    for name in NicknameLines:
        key,onename = name.split("\t")
        key = int(key)
        onename = onename.rstrip('\n')
        CorrespondenceTable[key] = onename
    return CorrespondenceTable

def createGraph(link_data):
    graph = {}
    for link in link_data:
        key,onelink = map(int,link.split("\t"))
        if key not in graph:    
            graph[key] = []     
        graph[key].append(onelink)
    return graph

def DecisionStartEnd(CorrespondenceTable,Startname,Endname):
    StartNumber = [k for k,v in CorrespondenceTable.items() if v == Startname][0]
    EndNumber = [k for k,v in CorrespondenceTable.items() if v == Endname][0]
    return StartNumber,EndNumber

if __name__ == '__main__':
    LinksLinesData = read_link(".gitignore/links.txt")   #links.txtを1行ずつリストに出力
    NicknameLinesData = read_name(".gitignore/nicknames.txt")  #nickname.txtから番号と名前の対応を辞書にして出力
    graph = createGraph(LinksLinesData)                  #linkリストからグラフを出力
    StartNumber,EndNumber = DecisionStartEnd(NicknameLinesData,"jacob","kent") #jacobとkentがそれぞれ何番かみる
    Route = bfs(graph,StartNumber,EndNumber)   #経路をBFSで見つける
    #print(Route)  #どういう経路を辿ってきたのかがわかる
    print("jacobから自分まで %d ステップです" %len(Route))

'''
#任意の人から任意の人へのステップ数を表示させたい時は
if __name__ == '__main__':
    print("誰からはじめる？->")
    Startname = input()
    print("誰で終わる？->")
    Endname = input()
    LinksLinesData = read_link(".gitignore/links.txt")
    NicknameLinesData = read_name(".gitignore/nicknames.txt")
    graph = createGraph(LinksLinesData)
    StartNumber,EndNumber = DecisionStartEnd(NicknameLinesData,Startname,Endname)
    Route = bfs(graph,StartNumber,EndNumber)
    #print(Route)  #どういう経路を辿ってきたのかがわかる
    print("%s から %s まで %d ステップです" %Startname,Endname,len(Route))

#DecisionStartEndの時に入力された名前がなかった場合の条件分岐が必要
def DecisionStartEnd(Startname,Endname):
    StartNumbers = [k for k,v in CorrespondenceTable.items() if v == Startname]
    EndNumbers = [k for k,v in CorrespondenceTable.items() if v == Endname]
    if len(StartNumbers) == 0 or len(EndNumbers) == 0:
        print('Invalid syntax')
        exit(1)
    elif:
        StartNumber = StartNumbers[0]
        EndNumber = EndNumbers[0]
    return StartNumber,EndNumber
'''