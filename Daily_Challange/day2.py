def blood_moon(time): 
 hours = []
 t = time.split(':')
 totalh = (int(t[0])*60)+int(t[1]) # Convert time to total minutes
 for i in range(3):
  totalh = totalh + 168  # 2h 48min in minutes
  current_time_in_minutes = totalh % 1440 # 1440 minutes in a day
  h = current_time_in_minutes // 60 # Get hours
  m = current_time_in_minutes % 60 # Get minutes
  h1 = f"{h:02}:{m:02}" # Format time as HH:MM
  hours.append(h1)
 return hours