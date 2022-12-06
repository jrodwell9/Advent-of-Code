from core.data_loader import load_data

lower_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
upper_letters = [i.upper() for i in lower_letters]

priority_map = dict(zip(lower_letters + upper_letters, list(range(1, 53))))

data = load_data("backpack_items.txt")

parsed_data = data.split("\n")[:-1]

total = 0

for bag in parsed_data:
    split_point = len(bag)//2
    comp1 = {i for i in bag[:split_point]}
    comp2 = {i for i in bag[split_point:]}
    common = comp1.intersection(comp2)
    total += sum(map(lambda x: priority_map[x], common))
    
print(total)   

###################### PART 2 ###########################

total = 0

start_index = 0
end_index = 3
for _ in range(0, len(parsed_data)//3):
    group = [{i for i in bag} for bag in parsed_data[start_index:end_index]]
    badge = list(group[0].intersection(group[1]).intersection(group[2]))[0]
    total += priority_map[badge]
    start_index += 3
    end_index += 3

print(total)
