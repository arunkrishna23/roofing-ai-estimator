def estimate_price(area, material, stories, pitch):
    material_base = {'asphalt': 6, 'tile': 8, 'metal': 10}  # price per sqft
    pitch_factor = {'low': 1.0, 'med': 1.2, 'high': 1.4}
    base_price = area * material_base.get(material, 6)
    total = base_price * pitch_factor.get(pitch, 1.0) * (1 + 0.1 * (stories-1))
    return round(total, 2)
