#####!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Token Similarity Distances
==================================

Based on term/token similarity calculations.

"""

__author__ = 'Abel Meneses-Abad, Pablo Ulacia'

from ..decorators import string2tokenset, string2vec

try:
    from nltk.metrics import jaccard_distance as jaccard_distance_nltk
    from nltk.metrics import masi_distance as masi_distance_nltk
    from nltk.metrics import interval_distance as interval_distance_nltk
except:
    pass

try:
    from sklearn.metrics.pairwise import manhattan_distances as manhattan_sklearn
    from sklearn.metrics.pairwise import cosine_distances as cosine_distance_sklearn
    from sklearn.metrics.pairwise import euclidean_distances as euclidean_distances_sklearn
except:
    pass

try:
    from scipy.spatial.distance import jaccard as jaccard_scipy
    from scipy.spatial.distance import braycurtis as braycurtis_scipy
    from scipy.spatial.distance import canberra as canberra_scipy
    from scipy.spatial.distance import chebyshev as chebyshev_scipy
    from scipy.spatial.distance import correlation as correlation_scipy
    from scipy.spatial.distance import dice as dice_scipy
    from scipy.spatial.distance import hamming as hamming_scipy
    from scipy.spatial.distance import kulsinski as kulsinski_scipy
    from scipy.spatial.distance import mahalanobis as mahalanobis_scipy
    from scipy.spatial.distance import matching as matching_scipy
    from scipy.spatial.distance import minkowski as minkowski_scipy
    from scipy.spatial.distance import rogerstanimoto as rogerstanimoto_scipy
    from scipy.spatial.distance import russellrao as russellrao_scipy
    from scipy.spatial.distance import seuclidean as seuclidean_scipy
    from scipy.spatial.distance import sokalmichener as sokalmichener_scipy
    from scipy.spatial.distance import sokalsneath as sokalsneath_scipy
    from scipy.spatial.distance import sqeuclidean as sqeuclidean_scipy
    from scipy.spatial.distance import yule as yule_scipy
except:
    pass

import numpy as np
from scipy.spatial.distance import (_copy_arrays_if_base_present,
                                    _convert_to_double)
from ..decorators import score_original, Appender

from .distances_doc import *

@string2tokenset
@Appender(jaccard_distance_textsim.__doc__)
def jaccard_distance(s1,s2):
    """NLTK Jaccard distance implementation.
    """
    return jaccard_distance_nltk(s1,s2)

@string2tokenset
@Appender(masi_distance_nltk.__doc__)
def masi_distance(s1,s2):
    """Masi distance
    """
    return masi_distance_nltk(s1,s2)

@string2tokenset
@Appender(interval_distance_nltk.__doc__)
def interval_distance(s1,s2):
    """Interval distance.
    """
    return float(interval_distance_nltk(s1.__len__(),s2.__len__()))

@string2vec
@Appender(manhattan_sklearn.__doc__)
def manhattan_distance(s1,s2):
    """Manhattan distance also known as City Block, L1.
    """
    return manhattan_sklearn(s1,s2)

@string2vec
@Appender(euclidean_distances_sklearn.__doc__)
def euclidean_distance(s1,s2):
    """Euclidean distance also known as L1.
    """
    return euclidean_distances_sklearn(s1,s2)

@string2vec
@Appender(cosine_distance_sklearn.__doc__)
def cosine_distance(s1,s2):
    """Cosine distance also known as Orchini, Angular, Niche.
    """
    return cosine_distance_sklearn(s1,s2)

@string2vec
@Appender(jaccard_scipy.__doc__)
def jaccard_distance_scipy(s1,s2):
    "Jaccard distance also known as Tanimoto distance."
    return jaccard_scipy(s1,s2)

@string2vec
@Appender(braycurtis_scipy.__doc__)
def braycurtis_distance_scipy(s1,s2):
    ""
    return braycurtis_scipy(s1,s2)

@string2vec
@Appender(canberra_scipy.__doc__)
def canberra_distance_scipy(s1,s2):
    ""
    return canberra_scipy(s1,s2)

@string2vec
@Appender(chebyshev_scipy.__doc__)
def chebyshev_distance_scipy(s1,s2):
    ""
    return chebyshev_scipy(s1,s2)

@string2vec
@Appender(correlation_scipy.__doc__)
def correlation_distance_scipy(s1,s2):
    ""
    return correlation_scipy(s1,s2)

@string2vec
@Appender(dice_scipy.__doc__)
def dice_distance_scipy(s1,s2):
    ""
    return dice_scipy(s1,s2)

@string2vec
@Appender(hamming_scipy.__doc__)
def hamming_distance_scipy(s1,s2):
    ""
    return hamming_scipy(s1,s2)

@string2vec
@Appender(kulsinski_scipy.__doc__)
def kulsinski_distance_scipy(s1,s2):
    ""
    return kulsinski_scipy(s1,s2)

@string2vec
@Appender(mahalanobis_scipy.__doc__)
def mahalanobis_distance_scipy(s1,s2):
    ""
    [XA] = _copy_arrays_if_base_present([_convert_to_double(s1)])
    [XB] = _copy_arrays_if_base_present([_convert_to_double(s2)])
    X = np.vstack([XA, XB])
    VI = np.cov(X.T)
    return mahalanobis_scipy(s1,s2,VI)

@string2vec
@Appender(matching_scipy.__doc__)
def matching_distance_scipy(s1,s2):
    ""
    return matching_scipy(s1,s2)

@string2vec
@Appender(minkowski_scipy.__doc__)
def minkowski_distance_scipy(s1,s2):
    ""
    return minkowski_scipy(s1,s2, p=1)

@string2vec
@Appender(rogerstanimoto_scipy.__doc__)
def rogerstanimoto_distance_scipy(s1,s2):
    ""
    return rogerstanimoto_scipy(s1,s2)

@string2vec
@Appender(russellrao_scipy.__doc__)
def russellrao_distance_scipy(s1,s2):
    ""
    return russellrao_scipy(s1,s2)

@string2vec
@Appender(seuclidean_scipy.__doc__)
def seuclidean_distance_scipy(s1,s2):
    ""
    [XA] = _copy_arrays_if_base_present([_convert_to_double(s1)])
    [XB] = _copy_arrays_if_base_present([_convert_to_double(s2)])
    X = np.vstack([XA, XB])
    V = np.var(X, axis=0, ddof=1)
    return np.nansum(np.sqrt((XA - XB) ** 2 / V))

@string2vec
@Appender(sokalmichener_scipy.__doc__)
def sokalmichener_distance_scipy(s1,s2):
    ""
    return sokalmichener_scipy(s1,s2)

@string2vec
@Appender(sokalsneath_scipy.__doc__)
def sokalsneath_distance_scipy(s1,s2):
    ""
    return sokalsneath_scipy(s1,s2)

@string2vec
@Appender(sqeuclidean_scipy.__doc__)
def sqeuclidean_distance_scipy(s1,s2):
    ""
    return sqeuclidean_scipy(s1,s2)

@string2vec
@Appender(yule_scipy.__doc__)
def yule_distance_scipy(s1,s2):
    ""
    return yule_scipy(s1,s2)

@string2tokenset
def matching_coefficient_textsim(s1,s2):
    """
    Medida de similitud basada en vectores. Similar a la distancia de Hamming pero
    esta debe ser entre vectores de igual longitud. Esta distancia va a devolver un
    valor entre [0-x] donde cuanto menor sea la distancia entre los vectores mas
    semejanza existira por lo que su valor tendera a 0.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor
    similitud.
    Esta operacion se realizo dividiendo entre la longitud de la cadena mas larga y restando el resultado
    con 1 para invertir el orden a que esta tendiendo

                   (|x|-|x∩y|)
    M(x,y) = 1 -  -----------------
                   max_longitud(x,y)

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> matching_coefficient(x, y, "", "",idioma) ==  0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    maxlen = float(max(len(s1),len(s2)))
    return 1-(maxlen -len(s1.intersection(s2)))/maxlen

@string2tokenset
def jaccard_distance_textsim(s1,s2):
    """
    Jaccard or Tanimoto distance [Jaccard1901]_.

    The Jaccard distance tends to 1 while compared vectors are more similar.
    The range of values is between [0-1].

    .. math::


        jaccard(X,Y) = \\frac{|X ∩ Y|}{|X ∪ Y|}


    where :math:`X` and :math:`Y` are the token set of each sentence :math:`s1,s2`
    respectively.

    :Citation:

    .. [Jaccard1901] Jaccard, P. (1901). Étude comparative de la distribution
        florale dans une portion des Alpes et des Jura. Bulletin de la Société
        Vaudoise des Sciences Naturelles 37, 547-579.

    :param s1,s2: Sentences to compare.
    :type s1,s2: str
    :returns: float

    :Doctest:

        >>> x = "0.1 0.2 0.3 0.4"
        >>> y = "0.1 0.2 0.3 0.5"
        >>> jaccard(x, y) == 0.6
        True
    """
    c1 = s1 & s2
    c2 = s1 | s2
    if len(c2) == 0:
        result = 'inf'
    else:
        result = float(abs(len(c1)-len(c2)))/len(c2)
    return result

@string2tokenset
def dice_coefficient_textsim(s1,s2):
    """
    La medida de Dice_coefficient (similar a Jaccard) es una medida de similitud que va
    a tender a 2 mientras mas semejanza exista entre dos vectores y el rango de su
    resultado va estar entre [0-2]

                    2|X ∩ Y|
    dice(X,Y) = -----------
                     |X|+|Y|

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> dice_coefficient(x, y, "", "",idioma) == 1.2
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """
    c1 = s1 & s2
    c2 = s1 | s2
    return 2*(float(len(c1)))/(float(len(c2))+float(len(c2)))

@string2tokenset
def overlap_distance_textsim(s1,s2):
    """
    Overlap es una medida que tiende a 1 mientras mayor sea la semejanza entre los
    dos vectores y su resultado esta entre [0-1]. Este machea completamente si el vector1
    es un subconjunto del vector2 o viceversa

                |X ∩ Y|
    OC(x,y)= ---------------
              min(|x|,|y|)

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> overlap(x, y, "", "", idioma) == 0.75
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """

    if float(min(len(s1),len(s2))) == 0:
        result = 'inf'
    else:
        result = float(len(s1.intersection(s2)))/float(min(len(s1),len(s2)))

    return result

@string2tokenset
def euclidean_distance_textsim(s1,s2):
    """
    Euclidean es una medida de distancia geometrica entre dos vectores que tiende a 0 mientras mas
    semejantes son los vectores. Esta medida utiliza el metodo tf para asignarle un peso a las palabras
    de acuerdo a la frecuencia.
    En esta implementacion se realizo una modificacion para obtener un valor entre [0-1]
    donde cuando tiende a 1 es que existe mayor similitud y cuando tiende a 0 tiene menor
    similitud.
    Esta operacion se realizo  restando el resultado con 1 para invertir el orden a que esta tendiendo

                               ₂
    euclidean(x,y)= ⎷∑ |x - y |
                      i  i   i

    @param s1, s2: Cadenas a analizar
    @type s1: str
    @type s2: str
    @rtype: float

    >>> x = "0.1 0.2 0.3 0.4"
    >>> y = "0.1 0.2 0.3 0.5"
    >>> idioma = 'english'
    >>> euclidean(x, y, "", "", idioma) == 1.0
    True

    Understanding Plagiarism Linguistic Patterns,Textual Features, and Detection Methods
    Salha M. Alzahrani, Naomie Salim, and Ajith Abraham, Senior Member, IEEE
    """

    s1 = list(s1)
    s2 = list(s2)

    suma=0
    if len(s1)<len(s2):
        for i in range(len(s1)):
            suma+=pow(tf(s1[i],s1) - tf(s2[i],s2),2)
        return float(1-float(pow(suma,0.5)))
    else:
        for i in range(len(s2)):
            suma+=pow(tf(s1[i],s1) - tf(s2[i],s2),2)
        return float(1-float(pow(suma,0.5)))

def tf(t,d):
    return float(d.count(t)) / float(sum(d.count(w) for w in set(d)))

if __name__ == '__main__':
        v1="PCCW's chief operating officer, Mike Butcher, and Alex Arena, the chief financial officer, will report directly to Mr So."
        v2="Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So."
        print("MASI distance:", masi_distance_nltk("0.1 0.2 0.3 0.4", "0.1 0.2 0.3 0.5"))
        print("Dice's coefficient:",dice_coefficient_textsim(v1,v2))
        print("Matching coefficient:",matching_coefficient_textsim("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Jaccard:",jaccard_distance(v1,v2))
        print("Overlap coefficient:",overlap("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Cosine distance:",cosine_distance("0.1 0.2 0.3 0.4","0.1 0.2 0.3 0.5"))
        print("Euclidean distance:",euclidean_distance(v1,v2))
        print("Manhattan distance:",manhattan_distance(v1,v2))

