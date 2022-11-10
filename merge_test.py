from Sort import MergeStringList

sort_list = MergeStringList();
sample_list = ["Swedish","McFish","Puff Daddy","Floater","Wave","Chips","Bob","Flotsam","Miso","Cod","Finley","Finneus",
"Larry","Salmon","Sea Beast","Otto","Sardine","Pirate","Captain Jack Sparrow","Long John Silver"]

for string in sample_list:
    sort_list.add(string=string)

if __name__=="__main__":
    import timeit
    print('*******************Sorting Result********************');
    time_taken=timeit.repeat(stmt='sort_list.sort(sort_list.list)', setup="from __main__ import sort_list", repeat=5)
    print(time_taken)
    print(f'Average time {sum(time_taken)/5}')
