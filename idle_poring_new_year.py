def best_skill_to_upgrade(click_dmg_level, crit_chance_level, crit_dmg_level):
    click_dmg = 9 + click_dmg_level
    crit_chance = 0.02 + 0.03 * crit_chance_level
    crit_dmg = 2.2 + 0.3 * crit_dmg_level

    click_dmg_dmg_increase = 1.0 / click_dmg if click_dmg_level < 30 else 0
    crit_chance_dmg_increase = (1.0 - crit_chance - 0.03 + (crit_chance + 0.03) * crit_dmg) / (1.0 - crit_chance + crit_chance * crit_dmg) - 1 if crit_chance_level < 30 else 0
    crit_dmg_dmg_increase = (0.3 * crit_chance) / (1 - crit_chance + crit_chance * crit_dmg) if crit_dmg_level < 30 else 0

    max_increase = max(click_dmg_dmg_increase, crit_chance_dmg_increase, crit_dmg_dmg_increase)

    if max_increase == 0:
        return
    if click_dmg_dmg_increase == max_increase:
        return "Click Damage"
    if crit_chance_dmg_increase == max_increase:
        return "Crit Chance"
    return "CRI dmg"


click_dmg_level = 17
crit_chance_level = 19
crit_dmg_level = 16

for i in range(5):
    next_skill = best_skill_to_upgrade(click_dmg_level, crit_chance_level, crit_dmg_level)

    if not next_skill:
        break

    print "Current skills: Click Damage {}, Crit Chance {}, CRI Dmg {}".format(click_dmg_level, crit_chance_level, crit_dmg_level)
    print "Skill to upgrade: {}\n".format(next_skill)

    if next_skill == "Click Damage":
        click_dmg_level += 1
    elif next_skill == "Crit Chance":
        crit_chance_level += 1
    else:
        crit_dmg_level += 1

