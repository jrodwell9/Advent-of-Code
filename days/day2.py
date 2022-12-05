from core.data_loader import load_data

data = load_data("strategy_guide.txt")

parsed_data = [i.split(" ") for i in data.split("\n") if i != ""]

####################  PART 1  #########################
score = 0

own_score_map = {"X": 1, "Y": 2, "Z": 3}

equiv_map = {"A": "X", "B": "Y", "C": "Z"}

mapped_data = list(map(lambda x: [equiv_map[x[0]], x[1]], parsed_data))

for r in mapped_data:
    score += own_score_map[r[1]]
    if r[0] == r[1]:
        score += 3
    elif r[0] == "X" and r[1] == "Z":
        score += 0 
    elif (r[0] == "Z" and r[1] == "X") or r[0] < r[1]:
        score += 6

print(score)

####################  PART 2  ########################

score = 0

own_score_map = {"X": 0, "Y": 3, "Z": 6}

result_map = {"A": {"X": 3, "Y": 1, "Z": 2}, 
              "B": {"X": 1, "Y": 2, "Z": 3},
              "C": {"X": 2, "Y": 3, "Z": 1}}

for r in parsed_data:
    score += own_score_map[r[1]]
    score += result_map[r[0]][r[1]]

print(score)
