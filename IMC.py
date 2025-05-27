def featInchToMeters(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

def lbToKg(lb):
    return lb * 0.4535923

def cmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2

print(cmi(weight = lbToKg(176), height = featInchToMeters(5, 7)))
