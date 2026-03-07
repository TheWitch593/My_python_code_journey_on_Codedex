def calculate_score(elements):
    total_tes = 0
    
    for name, base_value, scores in elements:  
        scores.sort()
        trimmed = scores[1:-1]
        
        avg_goe = sum(trimmed) / len(trimmed)
        element_score = base_value + (avg_goe * 0.1 * base_value)
        
        total_tes += element_score
        
    return round(total_tes, 1)