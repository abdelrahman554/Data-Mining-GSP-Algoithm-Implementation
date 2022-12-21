from mlxtend.preprocessing import transactionencoder
import itertools

dataset = [['A', 'B', 'FG', 'C', 'D'],
           ['B', 'G', 'D'],
           ['B', 'F', 'G', 'AB'],
           ['F', 'AB', 'C', 'D'],
           ['A', 'BC', 'G', 'F', 'DE']]

# min_sup step 1
min_sup = 2
flatten_list = list(itertools.chain.from_iterable(dataset))
flatten_list = "".join(flatten_list)
print(flatten_list)

set1 = set(flatten_list)
l1 = list(set1)
l1.sort()
print(l1)

dic_counter = {}
for k in l1 :
    dic_counter[k] =0

for item in l1 :
    for set in dataset :
        for i in set :
            if i.find(item) != -1:
                dic_counter[item] +=1
                break

one_item_set = {}
for val,counter in dic_counter.items() :
    if counter >= min_sup :
        one_item_set[val] = counter
print(one_item_set)
one_item_list = [*one_item_set.keys()]
print(one_item_list)


# step2 : join2
matrix1 = [p for p in itertools.product(one_item_list, repeat=2)]
matrix1 = [tuple(i) for i in matrix1]
print(matrix1)
print(f"size of matrix1 = {len(matrix1)}")
print("*********")
comb = itertools.combinations(one_item_list, 2)
matrix2 = list(comb)
matrix2 = [f"{i[0]}{i[1]}" for i in matrix2]
print(matrix2)
print(f"size of matrix2 = {len(matrix2)}")

# step3 : count 2_item support
l2 = matrix1 + matrix2
print(l2)

dic_counter2 = {}
for k in l2 :
    dic_counter2[k] =0

print(dic_counter2)

for item in l2 :
    for set in dataset :
        position = 0
        flag_length = 0
        if type(item) is tuple :
            for i in range(len(item)) :
                while position < len(set) :
                    if set[position].find(item[i]) != -1 :
                        position += 1
                        flag_length +=1
                        break
                    position +=1
                if flag_length == len(item):
                    dic_counter2[item] +=1
                    break
                elif flag_length == 0:
                    break
        else:
            while position < len(set):
                if set[position].find(item) != -1:
                     dic_counter2[item] +=1
                     break
                else :
                    position +=1


print(dic_counter2)
two_item_set = {}
for val,counter in dic_counter2.items() :
    if counter >= min_sup :
        two_item_set[val] = counter
print(two_item_set)
two_item_list = [*two_item_set.keys()]
print(two_item_list)

#join3
three_item_list = []
for item in two_item_list :
    for item2 in two_item_list:
        if type(item2) is tuple and type(item) is tuple :
            #first case
            if len(item[0])==1 and len(item2[-1])==1 :
                if item[1:] == item2[:len(item2)-1]:
                    three_item_list.append(tuple([*item , item2[-1]]))
            #second case
            elif len(item[0]) != 1 and len(item2[-1]) == 1:
                temp = item
                temp[0]= temp[0][1:]
                if temp[0:] == item2[:len(item2)-1]:
                    three_item_list.append(tuple([*item , item2[-1]]))
            # third case
            elif len(item[0]) == 1 and len(item2[-1]) != 1:
                temp = item2
                temp[-1] = temp[-1][:len(temp)-1]
                if item[1:] == temp[0:]:
                    three_item_list.append(tuple([*item, item2[-1]]))
            # forth case
            # else :
            #     temp_item = item
            #     temp_item[0] = temp_item[0][1:]
            #
            #     temp_item2 = item2
            #     temp_item2[-1] = temp_item2[-1][:len(temp_item2) - 1]
            #     if temp_item[0:] == temp_item2[0:]:
            #         three_item_list.append(tuple([*item, item2[-1]]))

        elif type(item2) is not tuple and type(item) is tuple: # (A , B) + (AB)
            # first case
            if len(item[0]) == 1 :
                if item[1:][0] == item2[:len(item2)-1] or item[1:][0] == item2[1:len(item2)]:
                    three_item_list.append(tuple([item[0], item2]))
            # second case
            elif len(item[0]) != 1 :
                temp = item
                temp[0] = temp[0][1:]
                if temp[0:][0] == item2[:len(item2)-1] or item[1:][0] == item2[1:len(item2)] :
                    three_item_list.append(tuple([item[0], item2]))

        elif type(item2) is  tuple and type(item) is not tuple:
            #first case
            if  len(item2[-1])==1 :
                if item[1:] == item2[:len(item2)-1][0] or item[1:] == item2[1:len(item2)][0] :
                    three_item_list.append(tuple([item , item2[-1]]))
            # third case
            elif  len(item2[-1]) != 1:
                temp = item2
                temp[-1] = temp[-1][:len(temp)-1]
                if item[1:] == temp[0:][0] or item[1:] == temp[0:][0]:
                    three_item_list.append(tuple([item, item2[-1]]))
        #else :



print(three_item_list)
three_item_set = set(three_item_list)
three_item_list = list(three_item_set)
print(three_item_list)