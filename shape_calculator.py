class rectangle:
    def __init__(self, height, width):  
      self.height = height
      self.width = width
      
    def area(self):
      get_area = self.height * self.width
      return get_area
      
    def perimeter(self):
      get_perimeter = 2 * (self.height + self.width)
      return get_perimeter
  
    def get_diagonal(self):
      get_diagonal = (self.height ** 2 + self.width ** 2) ** 0.5
      return get_diagonal

    def get_picture(self):
      if self.height > 50 or self.width > 50:
        return "Too big for picture."
      else:
        return "\n".join(["*" * self.width for _ in range(self.height)])

    def get_amount_inside(self , shape):
      if self.height > shape.height and self.width > shape.width:
        return (self.height // shape.height) * (self.width // shape.width)

    def __str__(self):
      return f'rectangle(height={self.height}, width={self.width})'

class square(rectangle):
    def __init__(self, length):
      self.height = length
      self.width = length

    def set_aside(self):
      self.height = self.width
      return self.height

print(rectangle(2,3).area())
