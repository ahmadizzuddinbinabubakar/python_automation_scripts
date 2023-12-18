import language_tool_python
tool = language_tool_python.LanguageTool('en-US')

# text = "Your the best but their are allso  good !"
text = "I dont like sand. It’s   coarse and rough and irrritating… and it gets every,where"
matches = tool.check(text)

for x in matches:
	print(x)