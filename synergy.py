def synergy(nl):
    dic_freq = {}
    for i in nl:
        for j in i:
            if j in dic_freq.keys():
                dic_freq[j] += 1
            else:
                dic_freq[j] = 1
    max_freq = max(dic_freq.values())
    max_syn = []
    for i,j in dic_freq.items():
        if j == max_freq:
            max_syn.append(i)
    return max_syn