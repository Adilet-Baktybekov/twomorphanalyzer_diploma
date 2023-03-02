
from backend.common import listToString
import backend
def noun_ending_from_noun(self, index, new_list, symbol, ending):
    new_list.reverse()
    new_word = listToString(new_list)
    new_list.reverse()
    self.set_root(new_word)
    self.set_part_of_speech(symbol)
    self.set_symbol('from_n_to_n', ending)
    self.set_symbols_list(symbol)

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word
def common(self, index, new_list, symbol, ending):
    self.set_symbol(symbol, ending)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word
def faces(self, index, new_list, symbol, ending, symbols_list, symbols):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    for key in list(symbols.keys()):
        if ending in backend.Faces.face_2st_sg_politely and key in backend.Others.plural:  # сыздар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'p2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('p2pl')
        elif ending in backend.Others.negative and key in symbols:  # сыз
            symbols[ending] = 'neg'
            symbols_list.append('neg')

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols
def possessiveness(self, index, new_list, symbol, ending, symbols_list, symbols):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    for key in list(symbols.keys()):
        if ending in backend.Possessiveness.posessiveness_for_poses_2st_pl_politely and key in backend.Others.plural:  # ыңыздар итд
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'px2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list('px2pl')
        elif ending in backend.Possessiveness.posessiveness_for_face_p2pl and key in backend.Possessiveness.posessiveness_2st_pl:  # сыңар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'p2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list('p2pl')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols
def noun_to_adj(self, index, new_list, symbol, ending, new_word):
    new_list.reverse()
    self.set_root(new_word)
    new_list.reverse()
    self.set_part_of_speech(symbol)
    self.set_symbol('from_n_to_adj', ending)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word
def noun_exception_1(new_list, ending):
    new_list.reverse()
    index = new_list.index(ending)
    str = listToString(ending)
    last_letter = str[-1]
    return new_list, index, last_letter, str
def noun_exception_2(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    new_list.pop(index)
    new_list.reverse()
    return new_list, index, ending, ending_list
def noun_exception_3(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str[0]
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    return new_list, index, ending, ending_list, index2
def noun_exception_4(self, new_list, symbol, last_letter, str):
    self.set_symbol(symbol, last_letter)
    self.set_symbols_list(symbol)
    index = new_list.index(str)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, index, new_word
def noun_exception_5(index, new_list, last_letter, ending, symbols, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str[0]
    new_ending = list(symbols)[-1]
    symbols[last_letter + new_ending] = symbols.pop(new_ending)
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    new_list.pop(index)
    new_list.reverse()
    return index, new_list, last_letter, ending, symbols, ending_list
def noun_exception_6(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str[0]
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    return new_list, ending_list
def noun_exception_7(self, symbol, new_list, last_letter, str):
    self.set_symbol(symbol, last_letter)
    self.set_symbols_list(symbol)
    index = new_list.index(str)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, new_word
def noun_exception_8(index, new_list, ending, ending_list, str):
    new_list[index + 1] = new_list[index + 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index + 1]
    ending_list.pop(index2)
    return new_list, ending_list
def noun_exception_9(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    return new_list, ending_list
def noun_exception_10(self, new_list, symbol, str):
    self.set_symbol(symbol, str)
    self.set_symbols_list(symbol)
    index = new_list.index(str)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, new_word
