from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel
from random import shuffle

app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста:')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# Список вопросов
questions = [
    ('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'),
    ('Год основания Витебска', '974', '1009', '1234', '666'),
    ('Столица Франции', 'Париж', 'Берлин', 'Рим', 'Мадрид'),
    ('Самая высокая гора в мире', 'Эверест', 'Килиманджаро', 'Эльбрус', 'Монблан')
]

current_question = -1  # Индекс текущего вопроса

def ask(question, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неверно!')

# Перемешанный список вопросов (создаётся один раз)
shuffled_questions = questions.copy()
shuffle(shuffled_questions)

def next_question():
    global current_question, shuffled_questions
    current_question += 1
    if current_question >= len(shuffled_questions):
        current_question = 0
        shuffle(shuffled_questions)  # Перемешать вопросы заново
    question, right_answer, wrong1, wrong2, wrong3 = shuffled_questions[current_question]
    ask(question, right_answer, wrong1, wrong2, wrong3)


# Установить начальный вопрос
next_question()

def on_btn_ok_clicked():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(on_btn_ok_clicked)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.resize(400, 300)
window.show()
app.exec_()
