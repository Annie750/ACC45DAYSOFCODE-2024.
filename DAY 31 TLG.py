n = int(input().strip())
cumulative_score_p1 = 0
cumulative_score_p2 = 0
max_lead = 0
winner = 0
for _ in range(n):
    s1, s2 = map(int, input().strip().split())
    cumulative_score_p1 += s1
    cumulative_score_p2 += s2
    if cumulative_score_p1 > cumulative_score_p2:
        current_lead = cumulative_score_p1 - cumulative_score_p2
        current_leader = 1
    else:
        current_lead = cumulative_score_p2 - cumulative_score_p1
        current_leader = 2
    if current_lead > max_lead:
        max_lead = current_lead
        winner = current_leader
print(winner, max_lead)
