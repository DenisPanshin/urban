from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
from tkhtmlview import HTMLLabel


def get_entry():
    value = entry_in.get()
    if value:
        return value
    else:
        return f'https://razgovor.edsoo.ru/topic/102/'


def get_name_of_day(): # Функция вернет название темы РоВ
    page = requests.get(get_entry())
    soup = BeautifulSoup(page.text, "html.parser")
    my_list = []
    for link in soup.find_all('a', href=True):
        if 'https://disk.yandex.ru' in link.get('href'):
            my_list.append(link)
    name_of_day = soup.find('span', 'topic-header-title').text.strip()
    choose_your_class = soup.find('span', 'topic-header-grade-title').text.strip()
    all_class = soup.find('a', 'topic-header-button blue-border active').text.replace('класс', '').strip()
    one_two = soup.find('a', 'topic-header-button pink-border').text.replace('класс', '').strip()
    three_four = soup.find('a', 'topic-header-button yellow-border').text.replace('класс', '').strip()
    fife_seven = soup.find('a', 'topic-header-button darkpink-border').text.replace('класс', '').strip()
    eight_nine = soup.find('a', 'topic-header-button red-border').text.replace('класс', '').strip()
    ten_eleven = soup.find('a', 'topic-header-button green-border').text.replace('класс', '').strip()
    spo = soup.find('a', 'topic-header-button blue2-border').text.replace('класс', '').strip()
    return name_of_day, choose_your_class, all_class, one_two, three_four, fife_seven, eight_nine, ten_eleven, spo, my_list


def refresh():
    label_name_of_day.configure(text=get_name_of_day()[0])



def btn_topic_next():
    url = get_entry()
    num_page = url[url.find('c/') + 2:url.rfind('/')]
    new_url = url[:url.rfind('/') - int(len(num_page))] + str(int(num_page) + 1) + '/'
    entry_in.delete(0, 'end')
    entry_in.insert(0, new_url)
    refresh()


def btn_topic_prev():
    url = get_entry()
    num_page = url[url.find('c/') + 2:url.rfind('/')]
    new_url = url[:url.rfind('/') - int(len(num_page))] + str(int(num_page) - 1) + '/'
    entry_in.delete(0, 'end')
    entry_in.insert(0, new_url)
    refresh()


window = tk.Tk()
window.title('Разговоры о важном')
window.geometry('400x300+300+300')
# window.resizable(False, False)
label_1 = tk.Label(window, text='Вставьте ссылку:')
label_1.place(x=1, y=5)
entry_in = tk.Entry(window, width=50)
entry_in.place(x=2, y=25)
btn1 = Button(text = 'Обновить данные', command=refresh)
btn1.place(x=1, y=60)
btn_topic_prev = Button(text='Предыдущая тема', command=btn_topic_prev)
btn_topic_prev.place(x=120, y=60)
btn_topic_next = Button(text='Следующая тема', command=btn_topic_next)
btn_topic_next.place(x=240, y=60)
label_name_of_day = tk.Label(window, text=get_name_of_day()[0])
label_name_of_day.place(x=1, y=100)
label_choose_your_class = tk.Label(window, text=get_name_of_day()[1])
label_choose_your_class.place(x=1, y=120)
label_link = tk.Label(window, text='Ссылка на скачивание')
label_link.place(x=160, y=120)
label_one_two = tk.Label(window, text=get_name_of_day()[3],)
label_one_two.place(x=1, y=140)
label_three_four = tk.Label(window, text=get_name_of_day()[4])
label_three_four.place(x=1, y=160)
label_fife_seven = tk.Label(window, text=get_name_of_day()[5])
label_fife_seven.place(x=1, y=180)
label_eight_nine = tk.Label(window, text=get_name_of_day()[6])
label_eight_nine.place(x=1, y=200)
label_ten_eleven = tk.Label(window, text=get_name_of_day()[7])
label_ten_eleven.place(x=1, y=220)
label_spo = tk.Label(window, text=get_name_of_day()[8])
label_spo.place(x=1, y=240)
html_label_one_two = HTMLLabel(window, html=str(get_name_of_day()[9][0]))
html_label_one_two.place(x=160, y=140)
html_label_three_four = HTMLLabel(window, html=str(get_name_of_day()[9][1]))
html_label_three_four.place(x=160, y=160)
html_label_fife_seven = HTMLLabel(window, html=str(get_name_of_day()[9][2]))
html_label_fife_seven.place(x=160, y=180)
html_label_eight_nine = HTMLLabel(window, html=str(get_name_of_day()[9][3]))
html_label_eight_nine.place(x=160, y=200)
html_label_ten_eleven = HTMLLabel(window, html=str(get_name_of_day()[9][4]))
html_label_ten_eleven.place(x=160, y=220)
html_label_spo = HTMLLabel(window, html=str(get_name_of_day()[9][5]))
html_label_spo.place(x=160, y=240)

window.mainloop()












