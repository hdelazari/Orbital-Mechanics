

class Body:
    def __init__(self, x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, size, mass):
        self.position = [x_pos, y_pos, z_pos]
        self.velocity = [x_vel, y_vel, z_vel]
        self.size = [size, mass]


class System:
    def __init__(self):
        self.bodies = []
        
    def add_body(self, body):
        self.bodies.append(body)

#    def remove_body(self,body):
        
