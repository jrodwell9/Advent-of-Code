from core.data_loader import load_data
import re

data = load_data("calories.txt")

elf_dict = {idx: i.split("\n") for idx, i in enumerate(data.split("\n\n"))}

elf_dict = {k: {"items": [int(c) for c in v if c != ""]} for k, v in elf_dict.items()}

elf_dict = {k: {"items": v, "sum": sum(v["items"])} for k, v in elf_dict.items()}

sorted_elf_dict = {k: v for k, v in sorted(elf_dict.items(), key=lambda x: x[1]["sum"], reverse=True)}

top_3_elf_dict = {k: v for k, v in sorted(elf_dict.items(), key=lambda x: x[1]["sum"], reverse=True)[:3]}

top_elf = sorted(elf_dict.items(), key=lambda x: x[1]["sum"], reverse=True)[0]

print(sum([info["sum"] for elf, info in top_3_elf_dict.items()]))
