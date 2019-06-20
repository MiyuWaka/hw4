# -*- coding: utf-8 -*-
#問題１　一番相互フォローが多い人を探したい！

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

def NumberOfMutualFollow(graph,number):
    if number not in graph.keys():
        MutualFollowNum[number] = 0
    else:
        followlist = graph[number]
        for follow in followlist:
            if (number in graph[follow]) == True:
                MutualFollowNum[number] += 1
    return MutualFollowNum

def MaxMutualFollow(MutualFollowlist,CorrespondenceTable):
    num_sorted = sorted(MutualFollowlist.values(),reverse=True)
    humannumbers =[k for k,v in MutualFollowlist.items() if v == num_sorted[0]]
    humanname = []
    for humannum in humannumbers:
        humanname.append(CorrespondenceTable[humannum])
    return humanname,num_sorted[0]



if __name__ == '__main__':
    LinksLinesData = read_link(".gitignore/links.txt")    #links.txtを1行ずつリストに出力
    NicknameLinesData = read_name(".gitignore/nicknames.txt")   #nickname.txtから番号と名前の対応を辞書にして出力
    graph = createGraph(LinksLinesData)                   #linkリストからグラフを出力
    MutualFollowNum = {}
    for num in NicknameLinesData.keys():
        MutualFollowNum[num] = 0
        MutualFollowNum = NumberOfMutualFollow(graph,num)   #それぞれ相互フォローが何人いるか出力
    max_human,max_num = MaxMutualFollow(MutualFollowNum,NicknameLinesData)  #一番多い人を出力
    print("一番相互フォローが多い人は %s で,相互フォロー人数は %d 人です" %(max_human,max_num))
