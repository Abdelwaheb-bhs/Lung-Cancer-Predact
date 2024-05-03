from flet import *
from methods import load_data
import pandas as pd
import matplotlib.pyplot as plt

def main(page:Page):

    l=load_data("cancer_des_poumons (1).csv"),
    Container(content=Row([Column([l[2]],scroll="always")],scroll="always"))




dataSet=pd.read_csv("/content/drive/MyDrive/Colab Notebooks/cancer_des_poumons.csv")
dataSet
dataSet.info()
missing_values = dataSet.isnull().any()
missing_values
for column in dataSet.columns:
    if missing_values[column]:
        mean_value = dataSet[column].mean()
        dataSet[column].fillna(mean_value, inplace=True)
missing_values
#methode 1

male = dataSet['GENDER'] == 'M'
female = dataSet['GENDER'] == 'F'
dataSet.loc[male, 'GENDER'] = 1
dataSet.loc[female, 'GENDER'] = 0
#methode 2
dataSet['GENDER'] = dataSet['GENDER'].map({'M':1,'F':0})
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
scaled_data = scaler.fit_transform(dataSet)
dataSet_normalized = pd.DataFrame(scaled_data, columns=dataSet.columns)
proportions_variance = lamdas / np.sum(lamdas)
for i, prop_variance in enumerate(proportions_variance):
    print(f"Composante Principale {i+1}: {prop_variance*100:.4f}")
dataSet_normalized
matrice_correlation = dataSet_normalized .corr()
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()
proportions_variance = lamdas / np.sum(lamdas)
for i, prop_variance in enumerate(proportions_variance):
    print(f"Composante Principale {i+1}: {prop_variance*100:.4f}")
app(target=main)
matrice_saturation = acp_norme.components_.T * np.sqrt(val_propres)
print("Matrice de corrélation des anciennes et des nouvelles variables :\n", matrice_saturation)

# 21. Analyser la saturation des variables en projetant les variables sur le cercle de corrélation
plt.figure(figsize=(10,10))
plt.Circle((0, 0), 1, color='blue', fill=False)
for i in range(len(matrice_saturation)):
    x, y = matrice_saturation[i, 0], matrice_saturation[i, 1]
    plt.plot([0, x], [0, y], linestyle='-', marker='o', label=dataSet.columns[i])
    plt.text(x, y, dataSet.columns[i])
plt.xlabel('Composante principale 1')
plt.ylabel('Composante principale 2')
plt.title('Cercle de corrélation')
plt.grid()
plt.axis('equal')
plt.legend(loc='upper center',bbox_to_anchor=(0.2, -0.02), ncol=3)
plt.show()