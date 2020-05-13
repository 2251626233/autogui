import pyautogui as pg

# pg.move(50, 50, 0.5)
# pg.moveTo(200, 300, 0.5)
# pg.drag(50, 50, 0.5, button='left')
# print(pg.position())

# pg.click(287, 31, duration=0.5)
# pg.rightClick(287, 31)
# pg.leftClick(287, 31)
# pg.doubleClick(287, 31)

# pg.typewrite("Hello World", 0.5)

# pg.click(x=233, y=64)
# pg.typewrite("google.com")
# pg.typewrite(["enter"])

# pg.typewrite("www.youtube.comn", 0.2)
# pg.hotkey("winleft", "up")
# pg.hotkey("ctrl", "t")

# pg.alert("Some info message", "Title message", button="Button text")
# age = pg.prompt("Enter your age", "Your age")
# print(age)
# pg.confirm("Are you older than 18?", "Are you sure?", ("Yes, I am", "No, I am not"))
# pg.password("Enter password", "Password Title")

# pg.screenshot("yourPic.png")

pg.click(x=168, y=63)
pg.typewrite("https://pyautogui.readthedocs.io/en/latest/")
pg.typewrite(["enter"])