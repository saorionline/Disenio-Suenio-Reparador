import json

# 1. This is the part that calls and loads the JSON file
with open(r"C:\Users\virtu\Documents\DeepDev\LevelOne\Disenio-Suenio-Reparador\dental_cdt_codes.json", 'r') as f:
    dental_codes = json.load(f)

def find_code(term):
    # Now dental_codes exists because we loaded it above
    for category, sub_dict in dental_codes.items():
        if term in sub_dict:
            return sub_dict[term], category
    return None, None

term_input = input("Enter terminology: ").title()
code, cat = find_code(term_input)

if code:
    print(f"Code: {code} | Category: {cat}")
else:
    print("Not found.")