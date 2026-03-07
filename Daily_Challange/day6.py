def calculate_sleep_debt(planned, actual):
  total_debt = 0
  current_streak = 0
  longest_streak = 0
  for h in range(len(planned)):
    daily_debt = max(0, planned[h] - actual[h])
    total_debt += daily_debt
    if daily_debt > 0:
      current_streak += 1
      longest_streak = max(longest_streak, current_streak)
    else:
      current_streak = 0

  total_debt += 1 
  return total_debt, longest_streak