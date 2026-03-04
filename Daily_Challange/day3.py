"""
You're given a 7x7 grid representing an area covered in Holi powders.
Each cell contains an emoji representing one of these colors:

["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]

Some colors may be missing from the grid. Can you find which ones are missing? 🤫

Complete the function that finds and returns all the colors missing from the area
(in that order).
"""

def find_missing_colors(grid):
  colours = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  present_colors = set() # Use a set to store present colors for O(1) lookups

# Iterate through the grid and add each color to the set of present colors
  for row in grid:
    for cell in row:
      present_colors.add(cell)

  missing = [] # List to store missing colors
  for color in colours:
    if color not in present_colors: # If the color is not in the set of present colors, it's missing
      missing.append(color)

  return missing