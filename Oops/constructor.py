class Factory:
    def __init__(self, material, zips, pockets):
        # print(self)
        self.material = material
        self.zips = zips
        self.pocket = pockets

    def show(self):
        print(f"Your objects details are: {self.material}, {self.pocket}, {self.zips} ")


reebok= Factory("leather",3,2)
campus = Factory("nylon",3,3)

# print(reebok.pocket)
# print(campus.pocket)

reebok.show()

