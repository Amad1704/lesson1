answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
def get_answer(question, answer = answers):
		question=question.lower()
		print(answer[question])
		

question = input()
print(get_answer(question))

