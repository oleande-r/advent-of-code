with open("2024\day05\\test_input.txt", 'r') as file:
    split_index = 0
    safety_manual = []
    
    for i, line in enumerate(file):
        if line == '\n':
            split_index = i
        
        safety_manual.append(line.strip("\n"))

page_ord_rules = safety_manual[:split_index]
pages_to_prod = safety_manual[split_index+1:]

def check_if_valid(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            index_1 = update.index(rule[0])
            index_2 = update.index(rule[1])
                
            if index_1 > index_2:
                return (rule, (index_1, index_2), update)
    
    return

def identify_valid_and_invalid_updates (rules, updates):
    rules = [rule.split('|') for rule in rules]
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        page_order = update.split(",")
        valid = True
        
        if check_if_valid(rules, page_order) != None:
            valid = False
        
        if valid:
            valid_updates.append(page_order)
        else:
            invalid_updates.append(page_order)
            
    return (valid_updates, invalid_updates)

def fix_invalid_updates(rules, invalid_updates):
    rules = [rule.split('|') for rule in rules]
    fixed_updates = []
    
    for update in invalid_updates:        
        valid = False
        
        while not valid:
            results = check_if_valid(rules, update)
            
            if results == None:
                valid = True
            else:
                rule,indicies, _ = results
                update[indicies[0]] = rule[1]
                update[indicies[1]] = rule[0]
        
        fixed_updates.append(update)
        
    return(fixed_updates)

def get_sumOfMiddles(rules, updates):
    valid_updates, invalid_updates = identify_valid_and_invalid_updates(rules, updates)
    fixed_updates = fix_invalid_updates(rules, invalid_updates)
    
    valid_middle_nums = [int(update[len(update) // 2]) for update in valid_updates]
    fixed_middle_nums = [int(update[len(update) // 2]) for update in fixed_updates]
    
    return (sum(valid_middle_nums), sum(fixed_middle_nums))

results = get_sumOfMiddles(page_ord_rules, pages_to_prod)
print('The sum of middle pages for part one is:', results[0])
print('The sum of middle pages for part two is:', results[1])