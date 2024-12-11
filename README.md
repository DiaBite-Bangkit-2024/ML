# DiaBite : Machine Learning

## 📑 Description

This project aims to predict the likelihood of diabetes based on user input and provide personalized dietary recommendations. By combining the power of Deep Neural Networks (DNN) for accurate prediction and Machine Learning (ML) for clustering dietary data, we aim to create an interactive and informative health tool. The application will leverage Gemini to provide user assistance and answer inquiries.

## 📚 Related Project Repositories

|    Learning Paths     |                            Link                             |
| :-------------------: | :---------------------------------------------------------: |
|  ☁️ Cloud Computing   | [CC Repository](https://github.com/DiaBite-Bangkit-2024/CC) |
| 📱 Mobile Development | [MD Repository](https://github.com/DiaBite-Bangkit-2024/MD) |

## 🤖 Machine Learning

### Model #1

The diabetes model use relevant features from the dataset to predict the likelihood of diabetes in user using neural network.

> Dataset: [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

### Model #2

The clustering model to make new data of food dataset. This data will used to make the 'Food Suggestion' feature in our app. We use [scikit-learn](https://scikit-learn.org/stable/) for this task using K-Means algorithm.

> Dataset: [Food Nutrition Dataset](https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset)

![Screenshot of Model 2 (1)](https://github.com/DiaBite-Bangkit-2024/.github/blob/main/assets/ss_model_2_1.png?raw=true)
![Screenshot of Model 2 (2)](https://github.com/DiaBite-Bangkit-2024/.github/blob/main/assets/ss_model_2_2.png?raw=true)

## 📚 Libraries Used

This project utilizes several Python libraries for data handling, machine learning, and visualization:

| Library             | Purpose                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `pandas`            | Facilitates data manipulation and analysis with data frames.                                  |
| `numpy`             | Enables efficient numerical computations and array operations.                                |
| `scikit-learn`      | A machine learning library for training models.                                               |
| `tensorflow`        | An open-source machine learning framework for building and training models.                   |
| `keras`             | High-level neural networks API, integrated with TensorFlow for easy model construction.       |
| `matplotlib.pyplot` | Used for creating visualizations, plots, and charts in Python.                                |
| `seaborn`           | Used for creating visualizations, plots, and charts in Python.                                |
| `gdown`             | Open-source Python library that allows users to download files and folders from Google Drive. |

## 🏃‍➡️ How To Run

### Model #1

1. Clone this GitHub Repository

    ```
    git clone https://github.com/DiaBite-Bangkit-2024/ML.git
    ```

2. Change directory to Model 1 (`diabetesModel`) folder

    ```
    cd diabetesModel
    ```

3. Install dependencies

    ```
    # if using pip
    pip install -r requirements.txt

    # if using pip3
    pip3 install -r requirements.txt

    # if using conda
    conda install --yes --file requirements.txt
    ```

4. Now you can execute and explore every script and notebook in `diabetesModel`

### Model #2

1. Clone this GitHub Repository

    ```
    git clone https://github.com/DiaBite-Bangkit-2024/ML.git
    ```

2. Change directory to Model 2 (`clusterModel`) folder

    ```
    cd clusterModel
    ```

3. Now you can execute and explore the notebook in `clusterModel`

    > Google Colab: [Data_Preprocessing_and_Clustering.ipynb](https://colab.research.google.com/github/DiaBite-Bangkit-2024/ML/blob/main/clusterModel/Data_Preprocessing_and_Clustering.ipynb)
