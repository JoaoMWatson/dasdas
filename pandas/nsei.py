import pandas

#  => Abre o arquivo com o pandas
file = pandas.read_csv('./dataset1.csv')

#  => Mostra o arquivo com o pandas usando o metodo head("Coloca quantas linhas quer q apareça toptop")
print(file.head())

print('=' * 50)
#  => Ordena por valor inserido no mtodo sort_values()
print(file.sort_values('idade'))

print('=' * 50)
#  => metodo .mean() determina a media "varial[coluna].mean()"
print('Media de idade: ', file['idade'].mean())