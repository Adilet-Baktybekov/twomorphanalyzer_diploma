import backend.sourceModule
def delete_symbols(sym_list, symbol):
    if symbol == 'nom' in sym_list and [sym for sym in backend.sourceModule.case if (sym in sym_list)]:
        sym_list.remove('nom')
    elif symbol == 'act' in sym_list and [sym for sym in backend.sourceModule.voice if (sym in sym_list)]:
        sym_list.remove('act')
    elif symbol == 'imp' in sym_list and [sym for sym in backend.sourceModule.mood if (sym in sym_list)]:
        sym_list.remove('imp')
    elif symbol == 'p3sg' in sym_list and [sym for sym in backend.sourceModule.face if (sym in sym_list)]:
        sym_list.remove('p3sg')
    elif symbol == 'card' in sym_list and [sym for sym in backend.sourceModule.num_symbols if (sym in sym_list)]:
        sym_list.remove('card')
    elif symbol == 'imp' in sym_list and [sym for sym in backend.sourceModule.non_finite_verb_forms if (sym in sym_list)]:

        sym_list.remove('imp')
    elif symbol == 'act' in sym_list and [sym for sym in backend.sourceModule.non_finite_verb_forms if
                                                     (sym in sym_list)]:
        sym_list.remove('act')
    elif symbol == 'pass' in sym_list and [sym for sym in backend.sourceModule.non_finite_verb_forms if
                                                      (sym in sym_list)]:
        sym_list.remove('pass')
    elif symbol == 'cnd' in sym_list and [sym for sym in backend.sourceModule.non_finite_verb_forms if
                                                     (sym in sym_list)]:
        sym_list.remove('cnd')
    return sym_list