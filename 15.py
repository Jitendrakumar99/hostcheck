import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
print(cancer)
print(df.head())
print(df.shape)
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
scalar.fit(df)
scaled_data=scalar.transform(df)
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)
print(x_pca.shape)
plt.figure(figsize=(6,4))
plt.scatter(x_pca[:, 0],x_pca[:, 1],c=cancer['target'],cmap='plasma')
plt.xlabel('First Principal component')
plt.ylabel('Second Principal component')
df_comp=pd.DataFrame(pca.components_,columns=cancer['feature_names'])
plt.figure(figsize=(14,6))
sns.heatmap(df_comp,cmap='coolwarm')
plt.title('Heatmap of PCA Components')
plt.xlabel('Original Features')
plt.ylabel('Principal components')
plt.show()
# output:
# {'data': array([[1.799e+01, 1.038e+01, 1.228e+02, ..., 2.654e-01, 4.601e-01,
#         1.189e-01],
#        [2.057e+01, 1.777e+01, 1.329e+02, ..., 1.860e-01, 2.750e-01,
#         8.902e-02],
#        [1.969e+01, 2.125e+01, 1.300e+02, ..., 2.430e-01, 3.613e-01,
#         8.758e-02],