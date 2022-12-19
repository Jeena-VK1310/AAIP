from fuzzywuzzy import fuzz
from fuzzywuzzy import process

print("Jeena Vinod Kumar, 32")
S1 = "i like softcomputing"
S2 = "i like hardcomputing"
print("Fuzzywuzzy ratio:", fuzz.ratio(S1, S2))
print("Fuzzywuzzy partialratio:", fuzz.partial_ratio(S1, S2))
print("Fuzzywuzzy tokensortratio:", fuzz.token_sort_ratio(S1, S2))
print("Fuzzywuzzy tokensortratio:", fuzz.token_set_ratio(S1, S2))
print("Fuzzywuzzy Wratio:", fuzz.WRatio(S1, S2), '\n\n')
print("Done")
