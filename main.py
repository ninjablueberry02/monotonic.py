sr = pd.Series(['football', 'basketball', 'chess'])
sr.index = ['1', ' 2', ' 3']
print(sr)
# check if monotonically increasing
sr.is_monotonic
