num_events = int(input())
event_list = list(map(int, input().split()))
unresolved_cases = 0
officers_available = 0

for event in event_list:
    if event == -1:
        if officers_available > 0:
            officers_available -= 1
        else:
            unresolved_cases += 1
    else:
        officers_available += event

print(unresolved_cases)
