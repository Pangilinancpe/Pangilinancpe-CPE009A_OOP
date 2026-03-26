def generate_truthtable(number_of_variables=0):
    if number_of_variables == 0:
        return "You need to enter an integer"
    else:
        total_combinations = 2**number_of_variables
        combinations_list = []
        for i in range(total_combinations):
            bin_equivalent = bin(i)[2:]
            while len(bin_equivalent) < number_of_variables:
                bin_equivalent = "0" + bin_equivalent
            combinations_list.append(tuple(int(val) for val in bin_equivalent))
        return combinations_list


import itertools

def generate_truthtable(n):
    combinations = list(itertools.product([True, False], repeat=n))
    for combo in combinations:
        print(combo)
    return combinations

def evaluate_propositional_logic(c_list):
    print("\nP       | Q       | P AND Q | P OR Q  | NOT P")
    print("-" * 50)
    for combo in c_list:
        P = combo[0]
        Q = combo[1]

        and_result = P and Q
        or_result  = P or Q
        not_p      = not P

        print(f"{str(P):<8}| {str(Q):<8}| {str(and_result):<8}| {str(or_result):<8}| {str(not_p)}")

evaluate_propositional_logic(generate_truthtable(3))