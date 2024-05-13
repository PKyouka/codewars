def check_exam(arr1,arr2):
    if len(arr1) != len(arr2):
        return 0
    score = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr2[i] == "":
            score += 0
        else:
            score -= 1
    return score if score > 0 else 0