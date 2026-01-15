CAMERA_RADIUS = 0.25

COLLIDERS = [
    (-3.5, -0.9, 0.0, 1.2, -3.0, -1.2),
    (-3.7, -2.7, 0.0, 0.9, -1.6, -0.6),
    (-3.45, -2.95, 0.7, 1.3, -1.35, -0.85),
    (3.35, 3.65, 0.0, 3.0, -4.2, -1.8),
    (-3.9, -3.3, 0.0, 0.7, 3.3, 3.9),
    (-4.0, -2.4, 0.0, 1.4, 0.6, 2.0),
    (3.45, 4.05, 0.0, 0.6, 1.25, 1.85),
    (3.35, 3.95, 1.0, 3.0, -0.3, 1.4),
]


def sphere_aabb(px, py, pz, r, box):
    minX, maxX, minY, maxY, minZ, maxZ = box

    cx = max(minX, min(px, maxX))
    cy = max(minY, min(py, maxY))
    cz = max(minZ, min(pz, maxZ))

    dx = px - cx
    dy = py - cy
    dz = pz - cz

    return (dx * dx + dy * dy + dz * dz) < (r * r)
