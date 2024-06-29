from config.config import EYE_AR_THRESH, EYE_AR_CONSEC_FRAMES

class EyeStatus:
    def __init__(self):
        self.frame_count = 0

    def calculate_polygon_area(self, vertices):
        # Ensure the vertices form a closed loop by repeating the first vertex at the end
        vertices = vertices + [vertices[0]]  # Closing the loop
        n = len(vertices)
        area = 0
        # Apply the Shoelace theorem
        for i in range(n - 1):
            x_i, y_i = vertices[i]
            x_ip1, y_ip1 = vertices[i + 1]
            area += x_i * y_ip1 - y_i * x_ip1
        area = abs(area) / 2.0
        return area

    def is_drowsy(self, ear):
        if ear < EYE_AR_THRESH:
            self.frame_count += 1
            if self.frame_count >= EYE_AR_CONSEC_FRAMES:
                return True
        else:
            self.frame_count = 0
        return False
