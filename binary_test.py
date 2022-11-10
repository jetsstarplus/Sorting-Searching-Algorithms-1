from Search import BinaryStringList

search_list = BinaryStringList();
sample_list = ["Swedish","McFish","Puff Daddy","Floater","Wave","Chips","Bob","Flotsam","Miso","Cod","Finley","Finneus",
"Larry","Salmon","Sea Beast","Otto","Sardine","Pirate","Captain Jack Sparrow","Long John Silver"]

for string in sample_list:
    search_list.add(string=string)

if __name__=="__main__":
    import timeit
    print('*******************Within The list********************');
    time_taken=timeit.repeat(stmt='search_list.find(string="Flotsam")', setup="from __main__ import search_list", repeat=5)
    print(time_taken)
    print(f'Average time {sum(time_taken)/5}')

    print('*******************Not in the list********************');
    time_taken=timeit.repeat(stmt='search_list.find(string="test")', setup="from __main__ import search_list", repeat=5)
    print(time_taken)
    print(f'Average time {sum(time_taken)/5}')

