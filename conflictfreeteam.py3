from itertools import combinations

def max_team_expertise(num_employees, conflicts, expertise_levels, conflict_pairs):
    max_expertise = 0

    conflict_set = set()
    for pair in conflict_pairs:
        emp1, emp2 = map(int, pair.split())
        conflict_set.add((emp1, emp2))
        conflict_set.add((emp2, emp1))

    for r in range(1, num_employees + 1):
        possible_teams = combinations(range(1, num_employees + 1), r)
        for team in possible_teams:
            team_skills = [expertise_levels[i - 1] for i in team]
            conflict_free = True
            for pair in combinations(team, 2):
                if pair in conflict_set:
                    conflict_free = False
                    break
            if conflict_free:
                max_expertise = max(max_expertise, sum(team_skills))

    return max_expertise

num_employees, conflicts = map(int, input().split())
conflict_pairs = []
for _ in range(conflicts):
    conflict_pairs.append(input())
expertise_levels = list(map(int, input().split()))
result = max_team_expertise(num_employees, conflicts, expertise_levels, conflict_pairs)
print(result)