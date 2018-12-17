import sys
start = "hit"
end = "cog"
ad = ["hit", "hot", "dot", "dog", "lot", "cog"]
ne = len(ad)
dict = {}
def find_path(path):
        word = path[len(path)-1]
        if word == end:
            if len(path) == ne:
                print(path)
            return
        visit = []
        for w in dict[word]:
            if w not in path:
                visit.append(w)
        if len(visit) == 0:
            return
        for ww in visit:
            path1 = path.copy()
            path1.append(ww)
            # print(path1)
            find_path(path1)

def print_path():
        path = []
        path.append("hit")
        for i in ad:
            dict[i] = []
        for i in range(len(ad)):
            for j in range(len(ad)):
                num = 0
                for k in range(3):
                    if (ad[i][k] == ad[j][k]):
                        num += 1
                if num == 2:
                    dict[ad[i]].append(ad[j])
        find_path(path)

print_path()
