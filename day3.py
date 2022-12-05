from core.data_loader import load_data

lower_letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
upper_letters = [i.upper() for i in lower_letters]

priority_map = zip(lower_letters + upper_letters, list(range(1, 52)))

data = load_data("backpack_items.txt")

parsed_data = data.split("\n")[:-1]

for i in parsed_data:
    split_point = len(i)/2 + 1
    comp1 = i[:split_point]
    comp2 = i[split_point:]
    
