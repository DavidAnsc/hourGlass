
class InitModel:
    theme = 0 # The colour theme, default is 0, options: 0 for dark, 1 for light.

    @staticmethod
    def init():
        print("**HourGlassModel initialized**")
        
        print()
        user_input = input("pls enter your preferred theme: 0 for dark, empty for light: ")

        if user_input.replace(" ", "") == "0":
            InitModel.theme = 0
        elif user_input.replace(" ", "") == "":
            InitModel.theme = 1
        else:
            print("Invalid input, defaulting to dark theme (0).")
            InitModel.theme = 0

        print("Theme set to: ", InitModel.theme == 0 and "DARK" or "LIGHT")
        