import nltk
import backend.sourceModule
import backend.Noun
import backend.Verb
import backend.Cases
import backend.Others
import backend.Possessiveness
import backend.Faces
import backend.Numeral
import backend.Adjectives_2
import backend.Pronoun
import backend.Adverb
import backend.file_reader
import backend.check_symbols
import backend.block_of_noun
import backend.block_of_verb
import backend.common
from backend.common import listToString
from backend.ending_split import ending_split
is_first_letter_upper = False
class Word:
    __original_word = ''
    __change_word = ''
    __root = ''
    __number = 0
    __root_from_the_end = ''
    __all_info = ''
    __info = ''
    __part_of_speech = ''
    __symbols = {}
    __symbols_list = []
    __negiz = ''
    __result_text = ''
    __first_punctuation_mark = ''
    __last_punctuation_mark = ''
    __word_without_punctuation = ''
    def __init__(self, word):
        self.__original_word = word
        self.__word_without_punctuation = word
        self.__change_word = word.lower()
        self.__symbols = {}
        self.__symbols_list = []

    def find_root(self, new_word):
        if (res := backend.file_reader.read_file(new_word)) != 'none':
            self.__part_of_speech = res[0]
            self.__root = new_word
            return True
        elif new_word in backend.Pronoun.all_pronoun:
            self.set_part_of_speech('prn')
            self.set_root(new_word)
            return True
        elif new_word in backend.Adverb.adv_words or new_word in backend.Adverb.adv_kosh_words:
            self.set_part_of_speech('adv')
            self.set_root(new_word)
            return True
        else:
            return False
    def find_root_from_the_end(self, new_word):
        if (res := backend.file_reader.read_file(new_word)) != 'none':
            self.__part_of_speech = res[0]
            self.__symbols_list.reverse()
            list = self.__symbols_list.copy()
            self.__symbols_list.clear()
            self.__symbols_list = res + list
            self.__symbols_list.reverse()
            self.__root = new_word

            return True
        elif new_word in backend.Pronoun.all_pronoun:
            self.set_part_of_speech('prn')
            self.set_root(new_word)
            if (symbol := backend.Pronoun.is_sg_or_pl(new_word)) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := backend.Pronoun.get_info_pronoun_root(new_word)) != 'none':
                self.set_symbols_list(symbol)
            return True
        elif new_word in backend.Adverb.adv_words or new_word in backend.Adverb.adv_kosh_words:
            self.set_part_of_speech('adv')
            self.set_root(new_word)
            return True
        else:
            return False
    def word_analyze(self, word):
        #word = backend.sourceModule.replace_letter(word)
        words = nltk.word_tokenize(word)
        try:
            syllables_of_words = ending_split(words)
        except:
            return 'Wrong'
        new_word = self.change_word[:1]
        self.set_change_word(self.__change_word[1:])
        for ch in self.change_word:
            if self.find_root(new_word):
                pass
            new_word += ch
        ending_list = syllables_of_words
        ending_list.reverse()
        new_list = list(ending_list)
        for ending in ending_list:
            str_ending = listToString(ending)
            index = new_list.index(ending)
            if self.part_of_speech == 'n':
                if (symbol := backend.Noun.get_info_noun_ending_from_noun(str_ending)) != 'none':
                    new_list, new_word = backend.block_of_noun.noun_ending_from_noun(self, index, new_list, symbol, str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := backend.Cases.get_info_cases(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Faces.get_info_faces(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        backend.common.faces( index, new_list, symbol, str_ending, self.__symbols_list, self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Others.get_info_other(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Possessiveness.get_info_possessive(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        backend.common.possessiveness(index, new_list, symbol, str_ending, self.__symbols_list,
                                                    self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Adjectives_2.get_info_adj_noun_to_adj(ending)) != 'none':
                    new_list, new_word = backend.block_of_noun.noun_to_adj(self, index, new_list, symbol, str_ending, new_word)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                else:
                    new_list, index, last_letter, str  = \
                        backend.common.common_exception_1(new_list, str_ending)
                    # for posessiveness_general (ныкы) итд
                    if ending in backend.sourceModule.half_of_ending_for_general_possessiveness and new_list[index - 1] in backend.sourceModule.posessiveness_general:
                        new_list, index, ending, ending_list = backend.common.common_exception_2(index, new_list, str_ending, ending_list, str)
                        continue
                    elif len(ending) == 2 and last_letter in backend.sourceModule.special_vowel:
                        if not self.__symbols:  # px3sp only
                            new_list, index, ending, ending_list, index2 = backend.common.common_exception_3\
                                (index, new_list, str_ending, ending_list, str)
                            if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                new_list, index, new_word = backend.common.common_exception_4\
                                    (self, new_list, symbol, last_letter, str)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        continue
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                                if key in backend.Possessiveness.posessiveness_2st_sg_politely or key in backend.Possessiveness.posessiveness_1st_pl or key \
                                        in backend.Possessiveness.posessiveness_2st_pl:
                                    is_px3sp = False
                                    index, new_list, last_letter, ending, self.__symbols, ending_list =\
                                        backend.common.common_exception_5(index, new_list, last_letter, ending, self.__symbols, ending_list, str)
                                else:
                                    continue
                            # px3sp with other endings
                            if is_px3sp:
                                new_list, ending_list = backend.common.common_exception_6(index, new_list, ending, ending_list, str)
                                if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    new_list, new_word = backend.common.common_exception_7(self, symbol, new_list, last_letter, str)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        new_word = listToString(new_list)
                                        if self.find_root_from_the_end(new_word):
                                            break
                                        else:
                                            continue
                            else:  # ыңар, ыбыз, ыңыз
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        continue
                    # for px1sg(ым) and px2sg(ың)
                    else:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        try:
                            new_list, ending_list = backend.common.common_exception_8(index, new_list, ending, ending_list, str)
                        except:
                            new_list, ending_list = backend.common.common_exception_9(index, new_list, ending,
                                                                                         ending_list, str)
                        str = listToString(new_list[index])
                        if (symbol := backend.Possessiveness.get_info_possessive(str)) != 'none':
                            new_list, new_word = backend.common.common_exception_10(self, new_list, symbol, str)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == 'v':
                if (symbol := backend.Verb.get_info_verb_verb_to_verb(str_ending)) != 'none':
                    new_list, new_word = backend.block_of_verb.verb_ending_from_verb(self, index, new_list, symbol,
                                                                                     str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue

                elif str_ending[1:] in backend.sourceModule.ending_of_gerund:
                    if (symbol := backend.Verb.get_gerund(ending[1:])) != 'none':
                        new_list, new_word = backend.block_of_verb.special_gerund(self, ending, symbol, index, new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue
                elif str_ending[1:] in backend.sourceModule.ending_of_gerund_pres:
                    if (symbol := backend.Verb.get_gerund(ending[1:])) != 'none':
                        new_list, new_word = backend.block_of_verb.special_gerund(self, ending, symbol, index, new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue
                elif (symbol := backend.Verb.get_gerund(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif str_ending[-1] == 'п' and self.find_root_from_the_end(self.__word_without_punctuation.lower()[:-1]):
                    new_list, new_word = backend.block_of_verb.special_chakchyl_1(self, ending, index, new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue


                elif str_ending[1:] in backend.sourceModule.ending_of_chakchyl:
                    if (symbol := backend.Verb.get_chakchyl(ending[1:])) != 'none':
                        new_list, new_word = backend.block_of_verb.special_chakchyl_2(self, ending, symbol, index, new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue
                elif (symbol := backend.Verb.get_chakchyl(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Verb.get_atoochtuk(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Verb.get_mood(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Verb.get_voice(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif str_ending[1:] in backend.sourceModule.v_voice_all_ending:
                    if (symbol := backend.Verb.get_voice(ending[1:])) != 'none':
                        new_list, new_word = backend.block_of_verb.special_voice(self, ending, symbol, index, new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue
                elif (symbol := backend.Cases.get_info_cases(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := backend.Faces.get_info_faces(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        backend.common.faces(index, new_list, symbol, str_ending, self.__symbols_list, self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Others.get_info_other(ending)) != 'none':
                    new_list, new_word = backend.common.common(self, index, new_list, symbol, str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Possessiveness.get_info_possessive(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        backend.common.possessiveness(index, new_list, symbol, str_ending, self.__symbols_list,
                                                      self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Noun.get_info_noun_ending_from_verb(ending)) != 'none':
                    new_list, new_word = backend.block_of_verb.noun_ending_from_verb(self, index, new_list, symbol,
                                                                                     str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                else:
                    new_list, index, last_letter, str = \
                        backend.common.common_exception_1(new_list, str_ending)
                    # for posessiveness_general (ныкы) итд
                    if ending in backend.sourceModule.half_of_ending_for_general_possessiveness and new_list[
                        index - 1] in backend.sourceModule.posessiveness_general:
                        new_list, index, ending, ending_list = backend.common.common_exception_2(index, new_list,
                                                                                                 str_ending,
                                                                                                 ending_list, str)
                        continue
                    elif len(ending) == 2 and last_letter in backend.sourceModule.special_vowel:
                        if not self.__symbols:  # px3sp only
                            new_list, index, ending, ending_list, index2 = backend.common.common_exception_3 \
                                (index, new_list, str_ending, ending_list, str)
                            if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                new_list, index, new_word = backend.common.common_exception_4 \
                                    (self, new_list, symbol, last_letter, str)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        continue
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                                if key in backend.Possessiveness.posessiveness_2st_sg_politely or key in backend.Possessiveness.posessiveness_1st_pl or key \
                                        in backend.Possessiveness.posessiveness_2st_pl:
                                    is_px3sp = False
                                    index, new_list, last_letter, ending, self.__symbols, ending_list = \
                                        backend.common.common_exception_5(index, new_list, last_letter, ending,
                                                                          self.__symbols, ending_list, str)
                                else:
                                    continue
                            # px3sp with other endings
                            if is_px3sp:
                                new_list, ending_list = backend.common.common_exception_6(index, new_list, ending,
                                                                                          ending_list, str)
                                if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    new_list, new_word = backend.common.common_exception_7(self, symbol, new_list,
                                                                                           last_letter, str)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        new_word = listToString(new_list)
                                        if self.find_root_from_the_end(new_word):
                                            break
                                        else:
                                            continue
                            else:  # ыңар, ыбыз, ыңыз
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        continue
                    # for px1sg(ым) and px2sg(ың)
                    else:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        try:
                            new_list, ending_list = backend.common.common_exception_8(index, new_list, ending,
                                                                                      ending_list, str)
                        except:
                            new_list, ending_list = backend.common.common_exception_9(index, new_list, ending,
                                                                                      ending_list, str)
                        str = listToString(new_list[index])
                        if (symbol := backend.Possessiveness.get_info_possessive(str)) != 'none':
                            new_list, new_word = backend.common.common_exception_10(self, new_list, symbol, str)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == 'num':
                if (symbol := backend.Numeral.get_info_numeral_ending(str_ending)) != 'none':

                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list_2 = list(new_list)
                    new_list_2.reverse()
                    new_word = listToString(new_list_2)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := backend.Cases.get_info_cases(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    self.set_symbols_list('subst')#subst - затташып кеткен символ
                    new_list.pop(index)
                    new_list_2 = list(new_list)
                    new_list_2.reverse()
                    new_word = listToString(new_list_2)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := backend.Faces.get_info_faces(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    for key in list(self.__symbols.keys()):
                        if ending in backend.Faces.face_2st_sg_politely and key in backend.Others.plural:#сыздар
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'p2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('p2pl')
                        elif ending in backend.Others.negative and key in self.__symbols:#сыз
                            self.__symbols[ending] = 'neg'
                            self.set_symbols_list('neg')

                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Others.get_info_plural_for_num(ending)) != 'none':
                    self.set_symbols_list('pl')
                    self.set_symbols_list(symbol)
                    self.set_symbol('pl', ending)
                    new_list.pop(index)
                    new_list_2 = list(new_list)
                    new_list_2.reverse()
                    new_word = listToString(new_list_2)
                    if self.find_root_from_the_end(new_word):

                        break
                    else:
                        continue
                elif (symbol := backend.Others.get_info_other(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list_2 = list(new_list)
                    new_list_2.reverse()
                    new_word = listToString(new_list_2)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := backend.Possessiveness.get_info_possessive(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    #------------
                    for key in list(self.__symbols.keys()):
                        if ending in backend.Possessiveness.posessiveness_for_poses_2st_pl_politely and key in backend.Others.plural:# ыңыздар итд
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'px2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('px2pl')
                        elif ending in backend.Possessiveness.posessiveness_for_face_p2pl and key in backend.Possessiveness.posessiveness_2st_pl: #сыңар
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'p2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('p2pl')
                    #------------

                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif ending in ['чы', 'чи' , 'чу' , 'чү']:
                    new_list.reverse()
                    index = new_list.index(ending)
                    str = listToString(new_list[index - 1])
                    new_list[index] = str[1:] + new_list[index]
                    str = str.replace(str[1:], '')
                    new_list[index - 1] = str
                    ending_list[index - 1] = str
                    str = listToString(new_list[index])
                    first_letter = str[0]

                    '''except:

                        index = new_list.index(ending)
                        str = listToString(new_list[index - 1])
                        new_list[index] = str[1:] + new_list[index]
                        str = str.replace(str[1:], '')
                        new_list[index - 1] = str
                        str = listToString(new_list[index])
                        first_letter = str[0]'''

                    if (symbol := backend.Numeral.get_info_numeral_ending(str)) != 'none':
                        self.set_symbol(symbol, str)
                        self.set_symbols_list(symbol)
                        new_list.pop(index)
                        new_word = listToString(new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_word = new_word + first_letter
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                continue
                elif ending in ['гон' , 'гөн' , 'ген' , 'ган']:
                    new_list.reverse()
                    index = new_list.index(ending)
                    str = listToString(new_list[index - 1])
                    new_list[index] = str + new_list[index]
                    new_list[index - 1] = str
                    ending_list[index - 1] = str
                    str = listToString(new_list[index])
                    if (symbol := backend.Numeral.get_info_numeral_ending(str)) != 'none':
                        self.set_symbol(symbol, str)
                        self.set_symbols_list(symbol)
                        new_list.pop(index)
                        new_list.pop(index-1)
                        new_word = listToString(new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            continue
                else:
                    new_list.reverse()
                    index = new_list.index(ending)
                    str = listToString(ending)
                    last_letter = str[-1]
                    # for posessiveness_general (ныкы) итд
                    if ending in ['кы', 'ки', 'ку', 'кү'] and new_list[
                        index - 1] in backend.sourceModule.posessiveness_general:
                        new_list[index - 1] = new_list[index - 1] + str
                        index2 = ending_list.index(ending)
                        ending_list[index2 + 1] = new_list[index - 1]
                        new_list.pop(index)
                        new_list.reverse()
                        continue
                    elif len(ending) == 2 and last_letter in backend.sourceModule.special_vowel:
                        if not self.__symbols:  # px3sp only
                            new_list[index - 1] = new_list[index - 1] + str[0]
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index - 1]
                            if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                self.set_symbol(symbol, last_letter)
                                self.set_symbols_list(symbol)
                                index = new_list.index(str)
                                new_list.pop(index)
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        # new_list.reverse()
                                        continue
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                                if key in backend.Possessiveness.posessiveness_2st_sg_politely or key in backend.Possessiveness.posessiveness_1st_pl or key \
                                        in backend.Possessiveness.posessiveness_2st_pl:
                                    is_px3sp = False
                                    new_list[index - 1] = new_list[index - 1] + str[0]
                                    new_ending = list(self.__symbols)[-1]
                                    self.__symbols[last_letter + new_ending] = self.__symbols.pop(new_ending)
                                    index2 = ending_list.index(ending)
                                    ending_list[index2 + 1] = new_list[index - 1]
                                    new_list.pop(index)
                                    new_list.reverse()
                                    break
                                else:
                                    continue
                            # px3sp with other endings
                            if is_px3sp:
                                new_list[index - 1] = new_list[index - 1] + str[0]
                                index2 = ending_list.index(ending)
                                ending_list[index2 + 1] = new_list[index - 1]
                                if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    self.set_symbol(symbol, last_letter)
                                    self.set_symbols_list(symbol)
                                    index = new_list.index(str)
                                    new_list.pop(index)
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        new_word = listToString(new_list)
                                        if self.find_root_from_the_end(new_word):
                                            break
                                        else:
                                            continue
                            else:#ыңар, ыбыз, ыңыз
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        # new_list.reverse()
                                        continue
                    # for px1sg(ым) and px2sg(ың)
                    else:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        try:
                            new_list[index + 1] = new_list[index + 1] + str
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index + 1]
                            ending_list.pop(index2)
                        except:
                            new_list[index - 1] = new_list[index - 1] + str
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index - 1]
                        str = listToString(new_list[index])
                        if (symbol := backend.Possessiveness.get_info_possessive(str)) != 'none':
                            self.set_symbol(symbol, str)
                            self.set_symbols_list(symbol)
                            index = new_list.index(str)
                            new_list.pop(index)
                            new_word = listToString(new_list)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "adj":
                if (symbol := backend.Adjectives_2.get_info_adj_ending(ending)) != 'none':
                    self.set_symbol('from_adj_to_adj', ending)
                    new_list.pop(index)
                    new_list_2 = list(new_list)
                    new_list_2.reverse()
                    new_word = listToString(new_list_2)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := backend.Cases.get_info_cases(ending)) != 'none':
                    self.set_symbols_list('subst')
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := backend.Faces.get_info_faces(ending)) != 'none':
                    self.set_symbols_list('subst')
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    for key in list(self.__symbols.keys()):
                        if ending in backend.Faces.face_2st_sg_politely and key in backend.Others.plural:#сыздар
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'p2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('p2pl')
                        elif ending in backend.Others.negative and key in self.__symbols:#сыз
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols[ending] = 'neg'
                            self.set_symbols_list('neg')

                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := backend.Others.get_info_other(ending)) != 'none':
                    self.set_symbols_list('subst')
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Possessiveness.get_info_possessive(ending)) != 'none':
                    self.set_symbols_list('subst')
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    #------------
                    for key in list(self.__symbols.keys()):
                        if ending in backend.Possessiveness.posessiveness_for_poses_2st_pl_politely and key in backend.Others.plural:# ыңыздар итд
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'px2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('px2pl')
                        elif ending in backend.Possessiveness.posessiveness_for_face_p2pl and key in backend.Possessiveness.posessiveness_2st_pl: #сыңар
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'p2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('p2pl')
                    #------------

                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                else:
                    new_list.reverse()
                    index = new_list.index(ending)
                    str = listToString(ending)
                    last_letter = str[-1]
                    #for posessiveness_general (ныкы) итд
                    if ending in ['кы', 'ки' , 'ку' , 'кү'] and new_list[index - 1] in backend.sourceModule.posessiveness_general:
                        new_list[index - 1] = new_list[index - 1] + str
                        index2 = ending_list.index(ending)
                        ending_list[index2 + 1] = new_list[index - 1]
                        new_list.pop(index)
                        new_list.reverse()
                        continue
                    elif len(ending) == 2 and last_letter in backend.sourceModule.special_vowel:
                        if not self.__symbols:  #px3sp only
                            new_list[index - 1] = new_list[index - 1] + str[0]
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index - 1]
                            if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                self.set_symbol(symbol, last_letter)
                                self.set_symbols_list(symbol)
                                index = new_list.index(str)
                                new_list.pop(index)
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        #new_list.reverse()
                                        continue
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()): #ыңар, ыбыз, ыңыз
                                if key in backend.Possessiveness.posessiveness_2st_sg_politely or key in backend.Possessiveness.posessiveness_1st_pl or key \
                                        in backend.Possessiveness.posessiveness_2st_pl:
                                    is_px3sp = False
                                    new_list[index - 1] = new_list[index - 1] + str[0]
                                    new_ending = list(self.__symbols)[-1]
                                    self.__symbols[last_letter + new_ending] = self.__symbols.pop(new_ending)
                                    index2 = ending_list.index(ending)
                                    ending_list[index2 + 1] = new_list[index - 1]
                                    new_list.pop(index)
                                    new_list.reverse()
                                    break
                                else:
                                    continue
                            #px3sp with other endings
                            if is_px3sp:
                                new_list[index - 1] = new_list[index - 1] + str[0]
                                index2 = ending_list.index(ending)
                                ending_list[index2 + 1] = new_list[index - 1]
                                if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    self.set_symbol(symbol, last_letter)
                                    self.set_symbols_list(symbol)
                                    index = new_list.index(str)
                                    new_list.pop(index)
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        new_word = listToString(new_list)
                                        if self.find_root_from_the_end(new_word):
                                            break
                                        else:
                                            continue
                            else:#ыңар, ыбыз, ыңыз
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        # new_list.reverse()
                                        continue
                    #for px1sg(ым) and px2sg(ың)
                    else:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        try:
                            new_list[index + 1] = new_list[index + 1] + str
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index + 1]
                            ending_list.pop(index2)
                        except:
                            new_list[index - 1] = new_list[index - 1] + str
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index - 1]
                        str = listToString(new_list[index])
                        if (symbol := backend.Possessiveness.get_info_possessive(str)) != 'none':
                            self.set_symbol(symbol, str)
                            self.set_symbols_list(symbol)
                            index = new_list.index(str)
                            new_list.pop(index)
                            new_word = listToString(new_list)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "prn":
                if (symbol := backend.Cases.get_info_cases(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := backend.Faces.get_info_faces(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    for key in list(self.__symbols.keys()):
                        if ending in backend.Faces.face_2st_sg_politely and key in backend.Others.plural:#сыздар
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'p2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('p2pl')
                        elif ending in backend.Others.negative and key in self.__symbols:#сыз
                            self.__symbols[ending] = 'neg'
                            self.set_symbols_list('neg')

                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := backend.Others.get_info_other(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Possessiveness.get_info_possessive(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    #------------
                    for key in list(self.__symbols.keys()):
                        if ending in backend.Possessiveness.posessiveness_for_poses_2st_pl_politely and key in backend.Others.plural:# ыңыздар итд
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'px2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('px2pl')
                        elif ending in backend.Possessiveness.posessiveness_for_face_p2pl and key in backend.Possessiveness.posessiveness_2st_pl: #сыңар
                            self.__symbols_list.remove(self.__symbols[ending])
                            self.__symbols[ending + key] = self.__symbols.pop(ending)
                            self.__symbols[ending + key] = 'p2pl'
                            self.__symbols_list.remove(self.__symbols[key])
                            self.__symbols.pop(key)
                            self.set_symbols_list('p2pl')
                    #------------

                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                else:
                    new_list.reverse()
                    index = new_list.index(ending)
                    str = listToString(ending)
                    last_letter = str[-1]
                    #for posessiveness_general (ныкы) итд
                    if ending in ['кы', 'ки' , 'ку' , 'кү'] and new_list[index - 1] in backend.sourceModule.posessiveness_general:
                        new_list[index - 1] = new_list[index - 1] + str
                        index2 = ending_list.index(ending)
                        ending_list[index2 + 1] = new_list[index - 1]
                        new_list.pop(index)
                        new_list.reverse()
                        continue
                    elif len(ending) == 2 and last_letter in backend.sourceModule.special_vowel:
                        if not self.__symbols:  #px3sp only
                            new_list[index - 1] = new_list[index - 1] + str[0]
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index - 1]
                            if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                self.set_symbol(symbol, last_letter)
                                self.set_symbols_list(symbol)
                                index = new_list.index(str)
                                new_list.pop(index)
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        #new_list.reverse()
                                        continue
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()): #ыңар, ыбыз, ыңыз
                                if key in backend.Possessiveness.posessiveness_2st_sg_politely or key in backend.Possessiveness.posessiveness_1st_pl or key \
                                        in backend.Possessiveness.posessiveness_2st_pl:
                                    is_px3sp = False
                                    new_list[index - 1] = new_list[index - 1] + str[0]
                                    new_ending = list(self.__symbols)[-1]
                                    self.__symbols[last_letter + new_ending] = self.__symbols.pop(new_ending)
                                    index2 = ending_list.index(ending)
                                    ending_list[index2 + 1] = new_list[index - 1]
                                    new_list.pop(index)
                                    new_list.reverse()
                                    break
                                else:
                                    continue
                            #px3sp with other endings
                            if is_px3sp:
                                new_list[index - 1] = new_list[index - 1] + str[0]
                                index2 = ending_list.index(ending)
                                ending_list[index2 + 1] = new_list[index - 1]
                                if (symbol := backend.Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    self.set_symbol(symbol, last_letter)
                                    self.set_symbols_list(symbol)
                                    index = new_list.index(str)
                                    new_list.pop(index)
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        new_word = listToString(new_list)
                                        if self.find_root_from_the_end(new_word):
                                            break
                                        else:
                                            continue
                            else:#ыңар, ыбыз, ыңыз
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        # new_list.reverse()
                                        continue
                    #for px1sg(ым) and px2sg(ың)
                    else:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        try:
                            new_list[index + 1] = new_list[index + 1] + str
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index + 1]
                            ending_list.pop(index2)
                        except:
                            new_list[index - 1] = new_list[index - 1] + str
                            index2 = ending_list.index(ending)
                            ending_list[index2 + 1] = new_list[index - 1]
                        str = listToString(new_list[index])
                        if (symbol := backend.Possessiveness.get_info_possessive(str)) != 'none':
                            self.set_symbol(symbol, str)
                            self.set_symbols_list(symbol)
                            index = new_list.index(str)
                            new_list.pop(index)
                            new_word = listToString(new_list)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "adv":
                if (symbol := backend.Cases.get_info_cases(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
        return 'end'

    def search_word_db(self,word):
        #self.__original_word

        if word[-1] in backend.sourceModule.all_punctuation_marks and word[0] not in backend.sourceModule.all_punctuation_marks:
            self.__last_punctuation_mark = word[-1] + ' '
            self.__word_without_punctuation = word[:-1]
        elif word[-1] not in backend.sourceModule.all_punctuation_marks and word[0] in backend.sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark = word[0]
            self.__word_without_punctuation = word[1:]

        elif word[0] in backend.sourceModule.all_punctuation_marks and word[-1] in backend.sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark = word[0]
            self.__last_punctuation_mark = word[-1] + ' '
            self.__word_without_punctuation = word[1:-1]
        if self.__word_without_punctuation.isnumeric():
            self.__root = self.__word_without_punctuation
            self.set_symbols_list('num')
            self.set_symbols_list('card')
            self.__part_of_speech = 'num'
            self.set_all_info()
            return self.__all_info
        elif len(self.__word_without_punctuation) > 2 and (number := backend.Numeral.get_info_numeral_root(nltk.word_tokenize(self.__word_without_punctuation))) != 'none':
            self.set_number(number)
            return self.__number
        elif self.__word_without_punctuation.lower() in backend.Pronoun.all_pronoun:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'prn'
            self.set_symbols_list('prn')
            if (symbol := backend.Pronoun.get_info_pronoun_root(self.__word_without_punctuation.lower())) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := backend.Pronoun.is_sg_or_pl(self.__word_without_punctuation.lower())) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := backend.Pronoun.cases_pronoun_root(self.__word_without_punctuation.lower())) != 'none':
                if symbol == 'gen':
                    if self.__word_without_punctuation.lower() == 'анын':
                        self.set_symbol(symbol, 'нын')
                        self.__root = 'ал'
                    elif self.__word_without_punctuation.lower() == 'менин':
                        self.set_symbol(symbol, 'нин')
                        self.__root = 'мен'
                    elif self.__word_without_punctuation.lower() == 'сенин':
                        self.set_symbol(symbol, 'нин')
                        self.__root = 'сен'
                elif symbol == 'dat':
                    if self.__word_without_punctuation.lower() == 'ага':
                        self.set_symbol(symbol, 'га')
                        self.__root = 'ал'
                    elif self.__word_without_punctuation.lower() == 'мага':
                        self.set_symbol(symbol, 'га')
                        self.__root = 'мен'
                    elif self.__word_without_punctuation.lower() == 'сага':
                        self.set_symbol(symbol, 'га')
                        self.__root = 'сен'
                elif symbol == 'acc':
                    if self.__word_without_punctuation.lower() == 'аны':
                        self.set_symbol(symbol, 'ны')
                        self.__root = 'ал'
                    elif self.__word_without_punctuation.lower() == 'мени':
                        self.set_symbol(symbol, 'ни')
                        self.__root = 'мен'
                    elif self.__word_without_punctuation.lower() == 'сени':
                        self.set_symbol(symbol, 'ни')
                        self.__root = 'сен'
                    elif self.__word_without_punctuation.lower() == 'муну':
                        self.set_symbol(symbol, 'ну')
                        self.__root = 'бул'
                elif symbol == 'loc':
                    if self.__word_without_punctuation.lower() == 'анда':
                        self.set_symbol(symbol, 'да')
                        self.__root = 'ал'
                elif symbol == 'abl':
                    if self.__word_without_punctuation.lower() == 'андан':
                        self.set_symbol(symbol, 'дан')
                        self.__root = 'ал'
            self.set_all_info()
            return self.__all_info
        elif self.__word_without_punctuation.lower() in backend.Adverb.adv_words or self.__word_without_punctuation.lower() in backend.Adverb.adv_kosh_words:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'adv'
            self.set_symbols_list('adv')
            self.set_all_info()
            return self.__all_info

        else:
            if (res := backend.file_reader.read_file(self.__word_without_punctuation.lower())) != 'none':
                self.__symbols_list = res.copy()
                self.__part_of_speech = res[0]
                self.__root = self.__word_without_punctuation
                self.set_all_info()
                return self.__all_info
            else:
                try:
                    end = self.word_analyze(self.__word_without_punctuation.lower())
                    if end == 'end':
                        self.__symbols_list.reverse()
                        self.set_all_info()
                        return self.__all_info
                    else:
                        self.__result_text = '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
                        return "I dont know this word"
                except:
                    self.__result_text = '['+str(self.__word_without_punctuation)+']' + self.__last_punctuation_mark
                    return self.__original_word





    def ending_analyze(ending):
        pass
    @property
    def original_word(self):
        return self.__original_word

    @property
    def word_without_punctuation(self):
        return self.__word_without_punctuation

    @property
    def part_of_speech(self):
        return self.__part_of_speech


    @property
    def root(self):
        return self.__root

    @property
    def first_punctuation_mark(self):
        return self.__first_punctuation_mark

    @property
    def last_punctuation_mark(self):
        return self.__last_punctuation_mark
    @property
    def result_text(self):
        return self.__result_text
    @property
    def number(self):
        return self.__number
    @property
    def negiz(self):
        return self.__negiz
    @property
    def root_from_the_end(self):
        return self.__root_from_the_end
    @property
    def all_info(self):
        return self.__all_info
    @property
    def info(self):
        return self.__info

    @property
    def change_word(self):
        return self.__change_word

    @property
    def symbols_list(self):
        return self.__symbols_list
    @property
    def symbols(self):
        self.__symbols = dict(reversed(list(self.__symbols.items())))
        return self.__symbols
    def get_symbols_list(self):
        return self.__symbols_list.reverse()
    def set_number(self, number):
        self.__number = number
    def set_negiz(self, negiz):
        self.__negiz = negiz
    def set_part_of_speech(self, part_of_speech):
        self.__part_of_speech = part_of_speech
    def set_root(self, root):
        self.__root = root
    def set_root_from_the_end(self, root):
        self.__root_from_the_end = root
    def set_change_word(self, change_word):
        self.__change_word = change_word
    def set_symbol(self, symbol, ending):
        self.__symbols[ending] = symbol
    def set_symbols_list(self, symbol):
        self.__symbols_list.append(symbol)
    def set_all_info(self):
        if 'sg' in self.__symbols_list and 'pl' in self.__symbols_list:
            self.__symbols_list.remove('sg')
        for symbol in self.__symbols_list:
            if symbol == '':
                self.__symbols_list.remove(symbol)
        self.__symbols_list = list(dict.fromkeys(self.__symbols_list))#delete duplicates symbols
        for symbol in self.__symbols_list:
            self.__symbols_list = backend.check_symbols.delete_symbols(self.__symbols_list, symbol)


        self.__symbols_list = [i for i in self.__symbols_list if i]

        self.__all_info = "Уңгу: " + str(self.__root) + ".\n" + "Сөз түркүм: " + str(self.__part_of_speech) + \
                              ".\n" + "Баардык символдор: " + str(list(dict.fromkeys(self.__symbols_list))) + ".\n" + \
                                                           "Мүчөлөр: " + str(self.__symbols) + '\n'
        symbols_text = ''
        ending_symbols =[]
        for key, value in dict(reversed(list(self.__symbols.items()))).items():
            symbols_text = symbols_text + str(key) + '<' + str(value) + '>'
            ending_symbols.append(str(value))
        for sym in list(dict.fromkeys(self.__symbols_list)):
            if sym in ending_symbols:
                self.__symbols_list.remove(sym)

        def_symbols_text = ''
        for sym in list(dict.fromkeys(self.__symbols_list)):
            def_symbols_text = def_symbols_text + '<'+str(sym)+ '>'
        self.__result_text = str(self.__first_punctuation_mark)+str(self.__word_without_punctuation) + \
                            "/" + str(self.__root) + def_symbols_text + symbols_text + str(self.__last_punctuation_mark)



    @info.setter
    def info(self, mylist):
        self.info = '_'.join(mylist)


