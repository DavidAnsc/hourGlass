import enum




class HourGlassModel:
    theme: int = 1  # 0 for dark, 1 for light

    class hourglassStyles(enum.Enum):
        THICK = 1
        MODERN = 2
        MINIMAL = 3

    def __set_size(self):
        print()
        print("**Setting HourGlassModel size**")
        user_input = input("Please enter your preferred size (0 for small, 1 for default, or 2 for big): ")
        if user_input.replace(" ", "") in ["0", "1", "2"]:
            self.size = int(user_input.replace(" ", ""))
            print("Size set to: ", self.size)
        else:
            print("Invalid size, defaulting to 1.")
            self.size = 1
        print()

    def __set_style(self):
        print()
        print("**Setting HourGlassModel style**")
        user_input = input("Please enter your preferred style (1 for THICK, 2 for MODERN, 3 for MINIMAL): ")
        if user_input.replace(" ", "") == "":
            self.style = self.hourglassStyles.MODERN
            print("Style set to default: ", self.style.name)

        elif user_input.replace(" ", "") in ["1", "2", "3"]:
            self.style = self.hourglassStyles(int(user_input.replace(" ", "")))
            print("Style set to: ", self.style.name)
        else:
            print("Invalid style, defaulting to THICK.")
            self.style = self.hourglassStyles.THICK
        print()

    def __set_contrast(self):
        print()
        print("**Setting HourGlassModel contrast**")
        user_input = input("Please enter your preferred contrast (0.2 to 1.0, default is 0.8): ")
        if user_input.replace(" ", "") == "":
            self.contrast = 0.8
            print("Contrast set to default: ", self.contrast)
        elif 0.2 <= round(float(user_input.replace(" ", "")), 1) <= 1.0:
            self.contrast = float(user_input.replace(" ", ""))
            print("Contrast set to: ", self.contrast)
        else:
            print("Invalid contrast, defaulting to 0.8.")
            self.contrast = 0.8
        print()
    def __getDimensions(self):
        if self.size == 1:
            totalColumns = 50
            totalRows = 26
        elif self.size == 0:
            totalColumns = 24
            totalRows = 20
        else:
            totalColumns = 88
            totalRows = 45


        # store dimensions on the instance so other methods can use them
        self.totalColumns = int(totalColumns)
        self.totalRows = int(totalRows)


        validColumns = (self.totalColumns - 6) // 2
        validRows = (self.totalRows - 2) // 2

        # average indentation per row (ensure at least 1)
        avgIndentation = round(validColumns / validRows)

        # assign computed values back to the instance
        self.validColumns = int(validColumns)
        self.validRows = int(validRows)
        self.avgIndentation = int(avgIndentation)

        print("got avg indentation: ", self.avgIndentation)

        if self.style == self.hourglassStyles.THICK:
            self.style_string = "$&%"
            self.style_blocker_string = "*#"
        elif self.style == self.hourglassStyles.MINIMAL:
            self.style_string = "|"
            self.style_blocker_string = "_-"
        else:
            self.style_string = "|%"
            self.style_blocker_string = " #"
    
    # def __init__(self):


    size: int = 2 # Size of the hourglass model, default is 1, options: 0, 1, 2
    contrast: float = 0.8 # The contrast (colour) of the hourglass, default is 0.8, range: 0.2 to 1.0
    style: hourglassStyles = hourglassStyles.MINIMAL
    style_string: str
    style_blocker_string: str

    #///
    totalColumns: int
    totalRows: int
    validColumns: int
    validRows: int
    avgIndentation: int
    #///


    def getoppo(self) -> str:
        string: str = ""

        for x in range(len(self.style_string)-1, -1, -1):
            string += self.style_string[x]

        return string

    def getblock(self) -> str:
        string: str = ""

        for x in range(len(self.style_blocker_string)-1, -1, -1):
            string += self.style_blocker_string[x]

        return string




    def _drawUpper(self):
        for row in range(0, int(self.totalRows/2)):
            lastColumns: int = 0

            if row == 0:
                for x in range(0, self.totalColumns):
                    print(self.style_blocker_string[0], end="")
                for y in range(0, len(self.style_string)*2-2):
                    print((self.style_blocker_string[0]), end="")
                print()
                for x in range(0, self.totalColumns):
                    print(self.style_blocker_string[1], end="")
                for y in range(0, len(self.style_string)*2-2):
                    print((self.style_blocker_string[1]), end="")
                
            else:
                for x in range(0, self.totalColumns):
                    
                    if row == 1:
                        if x == 0:
                            print("\\" + self.style_string, end="")
                            lastColumns += 2
                            lastColumns = self.totalColumns - lastColumns*2
                        elif x == self.totalColumns-1-row:
                            print(self.getoppo() + "/", end="")
                        else:
                            if lastColumns > 0:
                                print(" ", end="")
                                lastColumns -= 1
                    else:
                        if x == 0:
                            for y in range(0, (row-1) * self.avgIndentation):
                                print(" ", end="")
                                lastColumns += 1
                            print("\\" + self.style_string, end="")
                            lastColumns += 2

                            lastColumns = self.totalColumns - lastColumns*2

                        elif x == self.totalColumns-1-row:
                            print(self.getoppo() + "/", end="")
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
                print("/" + self.style_string, end="")

                # lastColumns = int(self.totalColumns - (self.totalRows/2 - 1) * self.avgIndentation)

                if lastColumns > 0:
                    for x in range(0, lastColumns):
                        print(" ", end="")
                print(self.getoppo() + "\\")

            else:
                if row == 1:
                    for x in range(0, self.totalColumns):
                        print(self.getblock()[0], end="")
                    for y in range(0, len(self.style_string)*2-2):
                        print((self.getblock()[0]), end="")
                    print()
                    for x in range(0, self.totalColumns):
                        print(self.getblock()[1], end="")
                    for y in range(0, len(self.style_string)*2-2):
                        print((self.getblock()[1]), end="")

                else:
                    for x in range(0, int((row - 2) * self.avgIndentation)):
                        print(" ", end="")
                        lastColumns += 1
                    lastColumns = self.totalColumns - lastColumns*2 - 4
                    print("/" + self.style_string, end="")

                    if lastColumns > 0:
                        for x in range(0, lastColumns):
                            print(" ", end="")
                    print(self.getoppo() + "\\")
                                
            

        print()





    

    def initialize(self):
        self.init()

        self.__set_size()
        self.__set_contrast()
        self.__set_style()
        self.__getDimensions()
        print("\n\n")
        print("******* Finished configuring HourGlassModel *******")
        print("\n\n")
        self._drawUpper()
        self._drawLower()

    def init(self):
        print("**HourGlassModel initialized**")
        
        print()
        user_input = input("pls enter your preferred theme: 0 for dark, empty for light: ")

        if user_input.replace(" ", "") == "0":
            self.theme = 0
        elif user_input.replace(" ", "") == "":
            self.theme = 1
        else:
            print("Invalid input, defaulting to dark theme (0).")
            self.theme = 0

        print("Theme set to: ", self.theme == 0 and "DARK" or "LIGHT")
        
        

# model = HourGlassModel(1)
# model._drawUpper()
# model._drawLower()
# model.initialize()
