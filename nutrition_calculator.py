# https://www.youtube.com/watch?v=hZjxWqwoWTg&t=479s

body_weight_kg = 
body_fat_percent = 
calories_target = 

def kg_to_lbs(weight_kg):
    return 2.2046226218 * weight_kg

# weight in lbs
body_weight = kg_to_lbs(body_weight_kg)
fat_weight = body_weight * body_fat_percent
lean_weight = body_weight - fat_weight

protein_needed_m = 1.5 * lean_weight
fat_needed_m = 0.5 * lean_weight

protein_in_cal = protein_needed_m * 4
fat_in_cal = fat_needed_m * 9
carb_in_cal = calories_target - protein_in_cal - fat_in_cal

carb_needed_m = carb_in_cal / 4

print protein_needed_m
print fat_needed_m
print carb_needed_m

