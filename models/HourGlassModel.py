class HourGlassModel:
    theme: int
    def __init__(self, theme: int):
        self.theme = theme

    size: int = 2 # Size of the hourglass model, default is 1, options: 0, 1, 2
    contrast: float = 0.8 # The contrast (colour) of the hourglass, default is 0.8, range: 0.2 to 1.0


    #///
    totalColumns: int
    totalRows: int
    validColumns: int
    validRows: int
    avgIndentation: int
    #///



    def _getDimensions(self):
        if self.size == 1:
            totalColumns = 50
            totalRows = 26
        elif self.size == 0:
            totalColumns = 24
            totalRows = 20
        else:
            totalColumns = 88
            totalRows = 70
        # store dimensions on the instance so other methods can use them
        self.totalColumns = int(totalColumns)
        self.totalRows = int(totalRows)

        # compute usable area and convert to integers
        validColumns = (self.totalColumns - 6) // 2
        validRows = (self.totalRows - 2) // 2

        # average indentation per row (ensure at least 1)
        avgIndentation = max(1, round(validColumns / max(1, validRows)))

        # assign computed values back to the instance
        self.validColumns = int(validColumns)
        self.validRows = int(validRows)
        self.avgIndentation = int(avgIndentation)

        print("got avg indentation: ", self.avgIndentation)


    def _drawUpper(self):
        for row in range(0, int(self.totalRows/2)):
            lastColumns: int = 0

            if row == 0:
                for x in range(0, self.totalColumns):
                    print("_", end="")
                print()
                for x in range(0, self.totalColumns):
                    print("-", end="")
            else:
                for x in range(0, self.totalColumns):
                    
                    if row == 1:
                        if x == 0:
                            print("\\|", end="")
                            lastColumns += 2
                            lastColumns = self.totalColumns - lastColumns*2
                        elif x == self.totalColumns-1-row:
                            print("|/", end="")
                        else:
                            if lastColumns > 0:
                                print(" ", end="")
                                lastColumns -= 1
                    else:
                        if x == 0:
                            for y in range(0, (row-1) * self.avgIndentation):
                                print(" ", end="")
                                lastColumns += 1
                            print("\\|", end="")
                            lastColumns += 2

                            lastColumns = self.totalColumns - lastColumns*2

                        elif x == self.totalColumns-1-row:
                            print("|/", end="")
                            for y in range(0, (row-1) * self.avgIndentation):
                                print(" ", end="")
                            
                        else:
                            if lastColumns > 0:
                                print(" ", end="")
                                lastColumns -= 1



                    

            print()


    def _drawLower(self):
        for row in range(int(self.totalRows/2), 0, -1):
            lastColumns: int = 0

            if row == int(self.totalRows/2):
                # o = (self.totalRows-1) * self.avgIndentation
                for x in range(0, int((row - 2) * self.avgIndentation)):
                    print(" ", end="")
                    lastColumns += 1

                lastColumns = self.totalColumns - lastColumns*2 - 4
                print("/|", end="")

                # lastColumns = int(self.totalColumns - (self.totalRows/2 - 1) * self.avgIndentation)

                if lastColumns > 0:
                    for x in range(0, lastColumns):
                        print(" ", end="")
                print("|\\")

            else:
                if row == 1:
                    for x in range(0, self.totalColumns):
                        print("_", end="")
                    print()
                    for x in range(0, self.totalColumns):
                        print("-", end="")

                else:
                    for x in range(1, int((row - 1) * self.avgIndentation)):
                        print(" ", end="")
                        lastColumns += 1
                    lastColumns = self.totalColumns - lastColumns*2 - 4
                    print("/|", end="")

                    if lastColumns > 0:
                        for x in range(0, lastColumns):
                            print(" ", end="")
                    print("|\\")
                                
            

        print()





    def __set_size(self):
        print()
        print("**Setting HourGlassModel size**")
        user_input = input("Please enter your preferred size (0 for smaller font, 1 for default, or 2 for bigger): ")
        if user_input.replace(" ", "") in ["0", "1", "2"]:
            self.size = int(user_input.replace(" ", ""))
            print("Size set to: ", self.size)
        else:
            print("Invalid size, defaulting to 1.")
            self.size = 1
        print()

    def __set_contrast(self):
        print()
        print("**Setting HourGlassModel contrast**")
        user_input = input("Please enter your preferred contrast (0.2 to 1.0, default is 0.8): ")
        if 0.2 <= round(float(user_input.replace(" ", "")), 1) <= 1.0:
            self.contrast = float(user_input.replace(" ", ""))
            print("Contrast set to: ", self.contrast)
        else:
            print("Invalid contrast, defaulting to 0.8.")
            self.contrast = 0.8
        print()

    def configure(self):
        self.__set_size()
        self.__set_contrast()
        print()
        print("Finished configuring HourGlassModel")
        print("HourGlassModel configured with size:", self.size, "and contrast:", self.contrast)
        print()
        

model = HourGlassModel(1)
model._getDimensions()
model._drawUpper()
model._drawLower()