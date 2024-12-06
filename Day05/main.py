def parse_transitions(transitions):
    transition_dict = {}
    for transition in transitions:
        parts = transition.split('|')
        for i in range(len(parts) - 1):
            if parts[i] not in transition_dict:
                transition_dict[parts[i]] = []
            transition_dict[parts[i]].append(parts[i + 1])
    return transition_dict

def is_valid_order(transition_dict, update):
    numbers = update.split(',')
    for i in range(len(numbers) - 1):
        if numbers[i] in transition_dict and numbers[i + 1] not in transition_dict[numbers[i]]:
            return False
    return True

def solve1(page_ordering_rules, updates):
    transition_dict = parse_transitions(page_ordering_rules)
    res = 0
    for update in updates:
        if is_valid_order(transition_dict, update):
            numbers = update.split(',')
            middle_index = len(numbers) // 2
            middle_number = int(numbers[middle_index])
            res += middle_number
    
    print(res)

                
def main():
    page_ordering_rules = []
    updates = []

    with open("input.txt", "r") as file:
            input_lines = file.read().splitlines()
            for line in input_lines:
                if '|' in line:
                    page_ordering_rules.append(line)
                elif ',' in line:
                    updates.append(line)

    solve1(page_ordering_rules, updates)

main()