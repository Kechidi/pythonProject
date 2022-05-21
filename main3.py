import cv2
import numpy as np
import time

start = time.time()
file_path = 'picture.png'
#Lecture d'image graphique
img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Contenu de img:[coordonnée y,coordonnée x, [R, G, B]]
#Obtenez le nombre d'éléments sur l'axe des x et l'axe des y
i_range = img.shape[0]
j_range = img.shape[1]
#Tableau de stockage de coordonnées
graph_coordinate = [[0 for i in range(3)] for j in range(i_range * j_range)]
x_list = []
#boucle de l'axe y
for i in range(i_range):
    #boucle de l'axe des x
    for j in range(j_range):
        #Stocker chaque valeur RVB
        R, G, B = img[i, j]
        #Obtenez uniquement les coordonnées qui s'appliquent à la couleur du graphique
        if (230 <= R <= 255) and (0 <= G <= 30) and (130 <= B <= 160):
                graph_coordinate.append([i, j, img[i, j]])
                x_list.append(j)
coordinate = np.asarray(graph_coordinate)
#Trouvez la coordonnée y à partir de la valeur maximale sur l'axe x (coordonnée x à la fin du graphique)
target = np.where(coordinate[:, 1] == 0)
target2= np.where(coordinate[:, 1] == 0)
x_axis_target = coordinate[target2]
x_axis = x_axis_target[0][0]

y_axis_target = coordinate[target]
y_axis = y_axis_target[0][0]
print(f'y_axis:{y_axis}')
print('elapsed_time:{time} sec'.format(time=time.time() - start))
print(f'x_axis:{x_axis}')
print('elapsed_time2:{time} sec'.format(time=time.time() - start))


