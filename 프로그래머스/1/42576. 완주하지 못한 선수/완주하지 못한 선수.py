def solution(participant, completion):
    from collections import defaultdict
    
    participant_dict = defaultdict(int)
    
    for part in participant:
        participant_dict[part] += 1
    
    for comp in completion:
        participant_dict[comp] -= 1
    
    for key in participant_dict:
        if participant_dict[key] > 0:
            return key

