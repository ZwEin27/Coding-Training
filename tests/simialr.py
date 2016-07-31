from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def suggest_most_overlap(extracted_phone_list):
    # def sim_compare(x, y):
    #     if similar(x, y) > .7:
    #         if abs(len(x)-10) <= abs(len(y)-10):
    #             return -1
    #         else:
    #             return 1
    #     return -1
    # distinct_phone_list = list(set(extracted_phone_list))
    # sorted_list = sorted(distinct_phone_list, cmp=sim_compare)
    # return sorted_list


    potential_invalid, potential_valid = [], []
    for pn in extracted_phone_list:
        if len(pn) == 10:
            potential_valid.append(pn)
        else:
            potential_invalid.append(pn)
    ans = list(potential_valid)
    for pi in potential_invalid:
        if not any(similar(pi, pv) > .7 for pv in potential_valid):
            ans.append(pi)
    return ans


# extracted_phone_list = ["6022284192","60222084192","284192", "2133790691", "2133790394"]
# print suggest_most_overlap(extracted_phone_list)

# print similar("2133790691", "2133790314")
text_data = [None]

print ' '.join(text_data)
