import matplotlib.pyplot

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

meses = matplotlib.pyplot.plot(meses, valores)

matplotlib.pyplot.show(meses)
