class Object :
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y
    
    def move(self):
        self.actions = input('Please choose an action :')
        if self.actions == 'f':
            x_f = self.coord_x +1
            y_f = self.coord_y +1
            print(f"{x_f} and {y_f}")
            
        elif self.actions == 'b':
            x_b = self.coord_x -1
            y_b = self.coord_y -1
            print(f"{x_b} and {y_b}")
        else:
            print('Invalid action')
point = Object(12,15)
print(point.coord_x, point.coord_y)
point.move()