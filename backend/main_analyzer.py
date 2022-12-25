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
import time
import backend.file_reader

def add_char(word):
    t = ''
    for i in word:
        t += i
    return t


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1
def ending_split(words):
    syllables_of_words_all = []
    if len(words) >= 1:
        for word in words:

            ls_word = list(word)
            ls_word_orig = list(word)
            syllables_of_words = []
            if ls_word_orig[0] in backend.sourceModule.consonants_kg:
                while True:
                    if len(ls_word) == 4:
                        '''if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.consonants_kg and ls_word[
                            2] in backend.sourceModule.vowels_kg and ls_word[3] in backend.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))'''
                        if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg and ls_word[
                            2] in backend.sourceModule.vowels_kg and ls_word[3] in backend.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))

                    elif len(ls_word) == 3:
                        if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg and ls_word[2] in backend.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                        elif ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg and ls_word[2] in backend.sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))
                    elif len(ls_word) == 2:
                        if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))
                    if len(ls_word) == 0:
                        if len(ls_word_orig) <= 0:
                            break
                        else:
                            for i in range(len(syllables_of_words[-1])):
                                ls_word_orig.pop()
                            for i in ls_word_orig:
                                ls_word.append(i)
                    elif len(ls_word) != 0:
                        ls_word.remove(ls_word[0])
            elif ls_word_orig[0] in backend.sourceModule.vowels_kg:
                first_letter = ''
                if len(ls_word_orig) >= 3:
                    if ls_word_orig[0] in backend.sourceModule.vowels_kg and ls_word_orig[1] in backend.sourceModule.consonants_kg and ls_word_orig[2] in backend.sourceModule.vowels_kg:
                        first_letter = ls_word_orig[0]
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                    elif ls_word_orig[0] in backend.sourceModule.vowels_kg and ls_word_orig[1] in backend.sourceModule.consonants_kg and ls_word_orig[2] in backend.sourceModule.consonants_kg:
                        first_letter = ls_word_orig[0]+ls_word_orig[1]
                        ls_word.remove(ls_word[0])
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                        ls_word_orig.remove(ls_word_orig[0])
                    elif ls_word_orig[0] in backend.sourceModule.vowels_kg and ls_word_orig[1] in backend.sourceModule.vowels_kg and ls_word_orig[2] in backend.sourceModule.consonants_kg:
                        first_letter = ls_word_orig[0]+ls_word_orig[1]
                        ls_word.remove(ls_word[0])
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                        ls_word_orig.remove(ls_word_orig[0])
                    '''elif ls_word[0] in backend.sourceModule.vowels_kg and ls_word[1] in backend.sourceModule.consonants_kg and ls_word[
                            2] in backend.sourceModule.consonants_kg and ls_word[3] in backend.sourceModule.vowels_kg:
                        first_letter = ls_word_orig[0]+ls_word_orig[1]
                        ls_word.remove(ls_word[0])
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                        ls_word_orig.remove(ls_word_orig[0])'''



                while True:
                    if len(ls_word) == 4:
                        if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg and ls_word[
                            2] in backend.sourceModule.vowels_kg and ls_word[3] in backend.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                        '''elif ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.consonants_kg and ls_word[
                            2] in backend.sourceModule.vowels_kg and ls_word[3] in backend.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))'''
                    elif len(ls_word) == 3:
                        if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg and ls_word[2] in backend.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                        elif ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg and ls_word[2] in backend.sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))

                    elif len(ls_word) == 2:
                        if ls_word[0] in backend.sourceModule.consonants_kg and ls_word[1] in backend.sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))
                    if len(ls_word) == 0:
                        if len(ls_word_orig) <= 0:
                            syllables_of_words.append(first_letter)
                            break
                        else:
                            for i in range(len(syllables_of_words[-1])):
                                ls_word_orig.pop()
                            for i in ls_word_orig:
                                ls_word.append(i)

                    elif len(ls_word) != 0:
                        ls_word.remove(ls_word[0])

            syllables_of_words.reverse()
            syllables_of_words_all.append(syllables_of_words)
    else:
        return False
    return syllables_of_words_all[0]



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
        elif new_word in backend.sourceModule.verb:
            self.set_part_of_speech('v')
            self.set_root(new_word)
            return True
        elif new_word in backend.Numeral.num_root:
            self.set_part_of_speech('num')
            self.set_root(new_word)
            return True
        elif new_word in backend.sourceModule.adjective:
            self.set_part_of_speech('adj')
            self.set_root(new_word)
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
        elif new_word in backend.sourceModule.verb:
            self.set_part_of_speech('v')
            self.set_negiz(new_word)
            return True
        elif new_word in backend.Numeral.num_root:
            self.set_part_of_speech('num')
            self.set_negiz(new_word)
            return True
        elif new_word in backend.sourceModule.adjective:
            self.set_part_of_speech('adj')
            self.set_negiz(new_word)
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
                continue
            new_word += ch
        ending_list = syllables_of_words
        ending_list.reverse()
        new_list = list(ending_list)
        for ending in ending_list:
            str_ending = listToString(ending)
            index = new_list.index(ending)
            if self.part_of_speech == 'n':
                if (symbol := backend.Noun.get_info_noun_ending_from_noun(str_ending)) != 'none':
                    new_list.reverse()
                    new_word = listToString(new_list)
                    new_list.reverse()
                    self.set_root(new_word)
                    self.set_part_of_speech(symbol)
                    self.set_symbol('from_n_to_n',ending)
                    self.set_symbols_list(symbol)
                    new_list.pop(index)
                    new_list.reverse()

                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:

                        continue
                elif (symbol := backend.Cases.get_info_cases(ending)) != 'none':
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
                elif (symbol := backend.Adjectives_2.get_info_adj_noun_to_adj(ending)) != 'none':
                    new_list.reverse()
                    self.set_root(new_word)
                    new_list.reverse()

                    self.set_part_of_speech(symbol)
                    self.set_symbol('from_n_to_adj', ending)
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
            elif self.part_of_speech == 'v':
                if (symbol := backend.Verb.get_info_verb_verb_to_verb(str_ending)) != 'none':
                    new_list.reverse()
                    new_word = listToString(new_list)
                    new_list.reverse()
                    self.set_root(new_word)
                    self.set_part_of_speech(symbol)
                    self.set_symbol('from_v_to_v',ending)
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := backend.Verb.get_gerund(ending)) != 'none':
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
                elif (symbol := backend.Verb.get_atoochtuk(ending)) != 'none':
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
                elif (symbol := backend.Verb.get_voice(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    for sym in self.__symbols_list:
                        if sym == 'act':#
                            self.__symbols_list.remove('act')
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Verb.get_mood(ending)) != 'none':
                    self.set_symbol(symbol, ending)
                    self.set_symbols_list(symbol)
                    for sym in self.__symbols_list:
                        if sym == 'imp':#
                            self.__symbols_list.remove('imp')
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := backend.Cases.get_info_cases(ending)) != 'none':
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

                elif (symbol := backend.Faces.get_info_backend.Faces(ending)) != 'none':
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
                elif (symbol := backend.Noun.get_info_noun_ending_from_verb(ending)) != 'none':
                    new_list.reverse()
                    self.set_root(new_word)
                    new_list.reverse()
                    self.set_part_of_speech(symbol)
                    self.set_symbol('from_v_to_n', ending)
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
            self.__first_punctuation_mark = word[-1]
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
        elif self.__word_without_punctuation in backend.Pronoun.all_pronoun:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'prn'
            self.set_symbols_list('prn')
            if (symbol := backend.Pronoun.get_info_pronoun_root(self.__word_without_punctuation)) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := backend.Pronoun.is_sg_or_pl(self.__word_without_punctuation)) != 'none':
                self.set_symbols_list(symbol)
            self.set_all_info()
            return self.__all_info
        elif self.__word_without_punctuation in backend.Adverb.adv_words or self.__word_without_punctuation in backend.Adverb.adv_kosh_words:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'adv'
            self.set_symbols_list('adv')
            self.set_all_info()
            return self.__all_info
        elif self.__word_without_punctuation in backend.Numeral.num_root:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'num'
            self.set_symbols_list('num')
            self.set_symbols_list('card')
            self.set_all_info()
            return self.__all_info
        else:
            if (res := backend.file_reader.read_file(self.__word_without_punctuation)) != 'none':
                self.__symbols_list = res.copy()
                self.__part_of_speech = res[0]
                self.__root = self.__word_without_punctuation
                self.set_all_info()
                return self.__all_info
            else:
                try:
                    end = self.word_analyze(self.__word_without_punctuation)
                    if end == 'end':
                        self.__symbols_list.reverse()
                        self.set_all_info()
                        return self.__all_info
                    else:
                        return "I dont know this word"
                except:
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
        if 'sg' and 'pl' in self.__symbols_list:
            self.__symbols_list.remove('sg')
        for symbol in self.__symbols_list:
            if symbol == '':
                self.__symbols_list.remove(symbol)
            elif symbol == 'nom' in self.__symbols_list and [sym for sym in backend.sourceModule.case if (sym in self.__symbols_list)]:
                self.__symbols_list.remove('nom')
            elif symbol == 'act' in self.__symbols_list and [sym for sym in backend.sourceModule.voice if (sym in self.__symbols_list)]:
                self.__symbols_list.remove('act')
            elif symbol == 'imp' in self.__symbols_list and [sym for sym in backend.sourceModule.mood if (sym in self.__symbols_list)]:
                self.__symbols_list.remove('imp')
            elif symbol == 'p3sg' in self.__symbols_list and [sym for sym in backend.sourceModule.face if (sym in self.__symbols_list)]:
                self.__symbols_list.remove('p3sg')
        self.__symbols_list = [i for i in self.__symbols_list if i]
        if self.__negiz == '':
            self.__all_info = "Уңгу: " + str(self.__root) + ".\n" + "Сөз түркүм: " + str(self.__part_of_speech) + \
                              ".\n" + "Баардык символдор: " + str(list(dict.fromkeys(self.__symbols_list))) + ".\n" + \
                                                           "Мүчөлөр: " + str(self.__symbols) + '\n'
            symbols_text = ''
            for key, value in dict(reversed(list(self.__symbols.items()))).items():
                symbols_text = symbols_text + str(key) + '<' + str(value) + '>'

            def_symbols_text = ''
            for sym in list(dict.fromkeys(self.__symbols_list)):
                def_symbols_text = def_symbols_text + '<'+str(sym)+ '>'
            self.__result_text = str(self.__first_punctuation_mark)+str(self.__word_without_punctuation) + \
                                 "/" + str(self.__root) + def_symbols_text + symbols_text + str(self.__last_punctuation_mark)

        else:
            self.__all_info = "Негиз: " + str(self.__negiz) + "\n" + "Уңгу: " + str(self.__root) + "\n" + \
                              "Сөз түркүм: " + str(self.__part_of_speech) + \
                              "\n" + "Баардык символдор: " + str(list(dict.fromkeys(self.__symbols_list))) + "\n" + "Мүчөлөр: " + str(self.__symbols)

    @info.setter
    def info(self, mylist):
        self.info = '_'.join(mylist)

start = time.time()
'''input_string = input('Анализ учун сөз жазыныз: ').strip()
words = input_string.split(' ')
for w in words:
    word = Word(w)
    res = word.search_word_db(word.change_word)
    root = word.root
    part_of_speech = word.part_of_speech
    all_symbols = word.symbols_list
    all_endings = word.symbols

    print(res)'''
end = time.time()
print(end - start)
