import PySimpleGUI as sg

sg.theme("DarkBrown1")

calculationEvalText = ""
calculationDisplayText = ""

numbersButtonsList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
signList = ["+", "-", "/", "*", "."]
displaySignList = ["+", "−", "÷", "×"]

layout = [
    [ sg.Text("", background_color="yellow", text_color="black", font="_ 20", size=(20, 1), key="-CALCULATION-") ],
    [ sg.Text("Made by Vitor Philip Vieira Bojco", font="_ 10 italic") ],
    [ sg.Button("1"), sg.Button("2"), sg.Button("3"), sg.Button("÷"), sg.Button("C") ],
    [ sg.Button("4"), sg.Button("5"), sg.Button("6"), sg.Button("×"), sg.Button("⌫", font="_ 12") ],
    [ sg.Button("7"), sg.Button("8"), sg.Button("9"), sg.Button("−") ],
    [ sg.Button("0"), sg.Button(". "), sg.Button("="), sg.Button("+")]
]

window = sg.Window("Calculator", layout, font="_ 15", icon="img/icon.ico")

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    # Convert calculation eval and display text into string
    calculationEvalText = str(calculationEvalText)
    calculationDisplayText = str(calculationDisplayText)

    # Check if delete button was clicked
    if event == "⌫":
        try:
            # Then delete last character
            calculationEvalText = calculationEvalText[:-1]

            # Delete last character from display calculation text
            if (calculationDisplayText[-1] in displaySignList and calculationDisplayText[-1] != "."):
                calculationDisplayText = calculationDisplayText[:-3]
            elif (calculationDisplayText[-1] == " " and calculationDisplayText[-2] in displaySignList):
                calculationDisplayText = calculationDisplayText[:-3]
            else:
                calculationDisplayText = calculationDisplayText[:-1]

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

        # Ignore errors
        except:
            pass

    # Check if clear button was clicked
    if event == "C":
        # Then clear calculation eval and display text
        calculationEvalText = ""
        calculationDisplayText = ""

        # And update calculation label
        window["-CALCULATION-"].update(calculationDisplayText)

    # Check if any number button was clicked
    for number in numbersButtonsList:
        if event == str(number):
            # Then add it to calculation eval and display text
            calculationEvalText += str(number)
            calculationDisplayText += str(number)

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

    # Check if plus button was clicked
    if event == "+":
        # Check if calculation is able to add a plus sign
        try:
            if (calculationEvalText[-1] not in signList):
                # Then update calculation eval and display text
                calculationEvalText += "+"
                calculationDisplayText += " + "

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

        # Ignore errors
        except:
            pass

    # Check if minus button was clicked
    if event == "−":
        # Check if calculation is able to add a minus sign
        try:
            if (calculationEvalText[-1] not in signList):
                # Then update calculation eval and display text
                calculationEvalText += "-"
                calculationDisplayText += " − "

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

        # Ignore errors
        except:
            pass

    # Check if division button was clicked
    if event == "÷":
        # Check if calculation is able to add a division sign
        try:
            if (calculationEvalText[-1] not in signList):
                # Then update calculation eval and display text
                calculationEvalText += "/"
                calculationDisplayText += " ÷ "

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

        # Ignore errors
        except:
            pass

    # Check if multiplication button was clicked
    if event == "×":
        # Check if calculation is able to add a multiplication sign
        try:
            if (calculationEvalText[-1] not in signList):
                # Then update calculation eval and display text
                calculationEvalText += "*"
                calculationDisplayText += " × "

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

        # Ignore errors
        except:
            pass

    # Check if float button was clicked
    if event == ". ":
        # Check if calculation is able to add float sign
        try:
            if (calculationEvalText[-1] not in signList):
                # Then update calculation eval and display text
                calculationEvalText += "."
                calculationDisplayText += "."

            # And update calculation label
            window["-CALCULATION-"].update(calculationDisplayText)

        # Ignore errors
        except:
            pass

    # Check if equals button was clicked
    if event == "=":
        # Check if calculation is able to get a result
        try:
            if (calculationEvalText[-1] not in signList):
                # Then try to get the result
                calculationDisplayText = eval(calculationEvalText)
                calculationEvalText = calculationDisplayText

                # And update calculation label
                window["-CALCULATION-"].update(calculationDisplayText)
        
        # Ignore errors
        except:
            pass

window.close()