#Dependencias
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from faker import Faker
import logging

#Formato para el logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

#Dataframe de prueba para los problemas
df = pd.DataFrame({"id":[0,1,2,3],"name":['Kevin', 'Alex', 'Jose', 'Kevin'], "age":[2,5,7,10]})

#Generamos conjunto de datos falsos binarios para regresion logistica
faker = Faker()
X_fake_binary = pd.DataFrame([faker.random_elements(elements=(0,1), length=2, unique=False) for _ in range(100)])
y_fake = pd.Series([faker.random_int(min=0, max=1) for _ in range(100)])

#Funciones
def filter_dataframe(df:pd.DataFrame, col:str, threshold:float) -> pd.DataFrame:
    """ Permite filtrar un dataframe en base a una columna y un valor de umbral
    
    Parameters
    ----------
    df : DataFrame
        Dataframe inicial a filtrar.
    col : str
        Columna que se va a filtrar.
    threshold: float
        Umbral o valor a partir del cual se va a filtrar.

    Returns
    -------
    DataFrame
        Dataframe filtrado en base a columna y umbral.
    """
    try:
        df_filter = df[df[col] > threshold]
    except (TypeError, KeyError):
        logging.error('Revisa nombre de la columna a filtrar o el tipo de dato')
    else:
        logging.info('filter_dataframe ejecutada CORRECTAMENTE')
        return df_filter

def generate_regression_data(n_samples:int, features:int=2) -> (pd.DataFrame, pd.Series):
    """ Permite generar datos falsos para simular una regresión. 
    Como dato de entrada tenemos número de registros
    Y por defecto un argumento features que representa el número de dimensiones o columnas del dataset final
    
    Parameters
    ----------
    n_samples : int
        Número de registros o muestras aleatorias a generar.
    features : int, optional
        Número de columnas o dimensiones a generar, es decir n_samples x features(por defecto 2 features).

    Returns
    -------
    DataFrame
        Dataframe con variables independientes de dimensiones n_samples X features.
    Series
        Serie que representa el dato objetivo o variable y dependiente
    """
    try:
        #Inicializamos objetos y variables
        count = 0
        dic_df = {}

        for i in range(features+1):
            #Dividimos entre 100 para normalizar 
            sample = [faker.randomize_nb_elements(number=100)/100 for _ in range(n_samples)]
            col = 'feature_'+str(i+1)
            dic_df[col] = sample

        df = pd.DataFrame(dic_df)
        #Separamos variables independientes y objetivo
        y = df[col]
        df = df.drop(col,axis=1) 
    except:
        logging.error('Revisa que el número de muestras sea mayor a 0 o el tipo de dato ingresado')

    else:
        logging.info('generate_regression_data ejecutada CORRECTAMENTE')
        return df, y


def train_multiple_linear_regression(X: pd.DataFrame, y:pd.Series) -> LinearRegression:
    """ Permite entrenar un modelo de regresión lineal multiple
    
    Parameters
    ----------
    X : DataFrame
        Dataframe que contienen las variables indepenidientes .
    y : Serie
        Serie que contiene la variable dependiente.

    Returns
    -------
    LinearRegression
        Objeto Modelo de regresión entrenado.
    """
    try:
        #Hacemos split para dividir en train y test y entrenar el modelo sobre train solamente
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        reg_model = LinearRegression()
        reg_model.fit(X_train, y_train)
    except (TypeError, KeyError):
        logging.error('Revisa el tipo de dato ingresado sea el adecuado')
    else:
        logging.info('train_multiple_linear_regression ejecutada CORRECTAMENTE')
        return reg_model

def flatten_list(lst:list)->list:
    """ Permite hacer un aplanado de listas de listas
    
    Parameters
    ----------
    lst : list
        Lista de listas a unificar.

    Returns
    -------
    list
        Una lista global unificada.
    """
    try:
        new_list = [item2 for item in lst for item2 in item]
    except(TypeError):
        logging.error('Revisa el tipo de dato ingresado sea el adecuado')
    else:
        logging.info('flatten_list ejecutada CORRECTAMENTE')
        return new_list

def group_and_aggregate(df:pd.DataFrame, gr_col:str, agg_col:str)->pd.DataFrame:
    """ Permite hacer un aplanado de listas de listas
    
    Parameters
    ----------
    df : DataFrame
        Dataframe que será transformado mediante agreación y agrupación.
    gr_col: str
        Nombre de la columna a agrupar.
    agg_col: str
        Nombre de la columna que será agregada.

    Returns
    -------
    DataFrame
        Un dataframe agrupado y agregado mediante las columnas proporcionadas.
    """
    try:
        new_df = df.groupby(gr_col)[[agg_col]].mean()
    except:
        logging.error('Revisa el tipo de dato ingresado sea el adecuado o el nombre de las columnas')
    else:
        logging.info('group_and_aggregate ejecutada CORRECTAMENTE')
        return new_df

def train_logistic_regression(X:pd.DataFrame, y:pd.Series)-> LogisticRegression:
    """ Permite entrenar un modelo de regresión logistica
    
    Parameters
    ----------
    X : DataFrame
        Dataframe que contienen las variables indepenidientes .
    y : Serie
        Serie que contiene la variable dependiente.

    Returns
    -------
    LogisticRegression
        Objeto de Modelo de regresión logistica entrenado.
    """
    try:
        #Hacemos split para dividir en train y test y entrenar el modelo sobre train solamente
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        lg_model = LogisticRegression()
        lg_model.fit(X_train, y_train)
    except (TypeError, KeyError):
        logging.error('Revisa el tipo de dato ingresado sea el adecuado')
    else:
        logging.info('train_logistic_regression ejecutada CORRECTAMENTE')
        return lg_model
    
def apply_function_to_column(df:pd.DataFrame, col:str, func):
    """ Permite aplicar una función personalizada a una columna de un dataframe
    
    Parameters
    ----------
    df : DataFrame
        Dataframe inicial.
    col: str
        Nombre de la columna a transformar.
    func: function
        Nombre de la función personalizada a aplicar a determinada columna.

    Returns
    -------
    DataFrame
        Un dataframe con una columna transformada.
    """
    try:
        df[col] = df[col].apply(func)
    except:
        logging.error('Revisa que la función pueda manejar el tiempo de dato correctamente o el nombre de columna')
    else:
        logging.info('apply_function_to_column ejecutada CORRECTAMENTE')
        return df

def filter_and_square(lst:list)->list:
    """ Permite elevar un elemento de la lista mayor que 5 al cuadrado 
    
    Parameters
    ----------
    lst : list
        Lista de números de entrada.

    Returns
    -------
    list
        Lista de números mayores que 5 al cuadrado.
    """
    try:
        new_list = [item**2 for item in lst if item >5]
    except:
        logging.error('Revisa el tipo de dato ingresado sea el adecuado')
    else:
        logging.info('filter_and_square ejecutada CORRECTAMENTE')
        return new_list

    
#Main Execution
if __name__=="__main__":
    logging.info('Inicia Ejecución del programa')
    #Inician pruebas de funciones
    filter_dataframe(df, 'age', 2.0)
    X, y = generate_regression_data(100)
    reg = train_multiple_linear_regression(X, y)
    lst = flatten_list([[0],[1,2,3],[4,5],[6,7,8,9,10]])
    group_and_aggregate(df, 'name', 'age')
    train_logistic_regression(X_fake_binary, y_fake)
    apply_function_to_column(df, 'age', lambda x: x + 1)
    filter_and_square(lst)
    logging.info('Fin de programa')

