import matplotlib.pyplot as plt

def survey_ex():
    labels = ['Sports', 'Video Games', 'Partying', 'Programming', 'No idea']
    pie_sections = [30, 10, 45, 5, 10]
    
    plt.pie (pie_sections, labels = labels)
    plt.title ("Hobby Survey")
    plt.show()

    
survey_ex()
