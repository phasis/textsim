from .stringdists import (lcs_distance, lcs_similarity,
                            damerau_levenshtein_distance_textsim,
                            smith_waterman_distance,
                            needleman_wunch,
                            needleman_wunch_distance)
#from .stringdists import damerau_levenshtein_distance_textsim as damerau_levenshtein_distance

#This dict strategy is based on sklearn.metrics.pairwaise code example
PAIRED_DISTANCES = {
    'lcs_distance': lcs_distance,
    'lcs_similarity': lcs_similarity,
    'damerau_levenshtein_distance_textsim': damerau_levenshtein_distance_textsim,
    'smith_waterman_distance': smith_waterman_distance,
    'needleman_wunch': needleman_wunch,
    'needleman_wunch_distance': needleman_wunch_distance,
    }

#Import nltk distances from ~/nltk/metric/distance.py and modify after with decorators
global NLTKImportError
NLTKImportError = False
try:
    import nltk
except ImportError:
    NLTKImportError = True
    print("Some stringdists will not be available due to NLTK package isn't installed.")
    pass
finally:
    if not NLTKImportError:
        from .stringdists import (binary_distance, edit_distance_nltk,
                                edit_similarity_nltk)

        PAIRED_DISTANCES['binary_distance'] = binary_distance
        PAIRED_DISTANCES['edit_distance_nltk'] = edit_distance_nltk
        PAIRED_DISTANCES['edit_similarity_nltk'] = edit_similarity_nltk

JellyfishImportError = False
try:
    from .jellyfish import _normalize
except:
    JellyfishImportError = True
    print("Some stringdists will not be available due to Jellyfish package isn't installed.")
    pass
finally:
    if not JellyfishImportError:
        from .stringdists import (levenshtein_similarity_jellyfish,
                                levenshtein_distance_jellyfish)
        from .jellyfish import jaro_distance, hamming_distance
        from .jellyfish import jaro_winkler as jaro_winkler_distance
        from .jellyfish import damerau_levenshtein_distance as damerau_levenshtein_distance_jellyfish

        PAIRED_DISTANCES['levenshtein_distance_jellyfish'] = levenshtein_distance_jellyfish
        PAIRED_DISTANCES['levenshtein_similarity_jellyfish'] = levenshtein_similarity_jellyfish
        PAIRED_DISTANCES['jaro_distance'] = jaro_distance
        PAIRED_DISTANCES['jaro_winkler_distance'] = jaro_winkler_distance
        PAIRED_DISTANCES['hamming_distance'] = hamming_distance
        PAIRED_DISTANCES['damerau_levenshtein_distance_jellyfish'] = damerau_levenshtein_distance_jellyfish

from .stringdists import levenshtein_distance_pattern, levenshtein_similarity_pattern
from .pattern import dice_coefficient as dice_coefficient_pattern

PAIRED_DISTANCES['levenshtein_distance_pattern'] = levenshtein_distance_pattern
PAIRED_DISTANCES['levenshtein_similarity_pattern'] = levenshtein_similarity_pattern
PAIRED_DISTANCES['dice_coefficient_pattern'] = dice_coefficient_pattern

#After performance we compute result and stablished default edit, levenshtein
#damerau-levenshtein

from .stringdists import levenshtein_similarity_jellyfish as levenshtein_similarity
from .stringdists import levenshtein_similarity_jellyfish as edit_similarity
from .stringdists import levenshtein_similarity_pattern as damerau_levenshtein_similarity
from .stringdists import levenshtein_distance_pattern as levenshtein_distance
from .stringdists import levenshtein_distance_pattern as edit_distance

PAIRED_DISTANCES['levenshtein_similarity'] = levenshtein_similarity
PAIRED_DISTANCES['edit_similarity'] = edit_similarity
PAIRED_DISTANCES['damerau_levenshtein_similarity'] = damerau_levenshtein_similarity
PAIRED_DISTANCES['levenshtein_distance'] = levenshtein_distance
PAIRED_DISTANCES['edit_distance'] = edit_distance

# append all verified distances in module importing argument ALL
__all__ = []
for distance in PAIRED_DISTANCES:
	__all__.append(distance)

__not_implemented__ = [
    'Gotoh distance',
    'Monge Elkan distance',
]
