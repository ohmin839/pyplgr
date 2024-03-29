from parsimonious.nodes import NodeVisitor

class Visitor(NodeVisitor):
    def calc_score(self, text):
        return self.add_score_dialesis(text,
               self.add_score_breath(text,
               self.add_score_accent(text,
               self.add_score_iota_subscriptum(text))))

    def add_score_dialesis(self, text, score=0):
        if '"' in text:
            return 4 ** 3 + score
        else:
            return score

    def add_score_breath(self, text, score=0):
        if "<" in text:
            return 4 ** 2 * 1 + score
        elif ">" in text:
            return 4 ** 2 * 2 + score
        else:
            return score

    def add_score_accent(self, text, score=0):
        if "'" in text:
            return 4 ** 1 * 1 + score
        elif "`" in text:
            return 4 ** 1 * 2 + score
        elif "~" in text:
            return 4 ** 1 * 3 + score
        else:
            return score

    def add_score_iota_subscriptum(self, text, score=0):
        if "|" in text:
            return 1 + score
        else:
            return score
    
    def visit_letters(self, node, visited_children):
        return "".join([v for v in visited_children])

    def visit_letter(self, node, visited_children):
        v, *_ = visited_children
        return v

    def visit_alphabet(self, node, visited_children):
        v, *_ = visited_children
        return v

    def visit_large_alpha(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  1: return "\u1FBC" # A|
        if s ==  4: return "\u1FBB" # 'A
        # if s ==  5: return "\uxxxx" # 'A|
        if s ==  8: return "\u1FBA" # `A
        # if s ==  9: return "\uxxxx" # `A|
        # if s == 12: return "\uxxxx" # ~A
        # if s == 13: return "\uxxxx" # ~A|
        if s == 16: return "\u1F09" # <A
        if s == 17: return "\u1F89" # <A|
        if s == 20: return "\u1F0D" # <'A
        if s == 21: return "\u1F8D" # <'A|
        if s == 24: return "\u1F0B" # <`A
        if s == 25: return "\u1F8B" # <`A|
        if s == 28: return "\u1F0F" # <~A
        if s == 29: return "\u1F8F" # <`A|
        if s == 32: return "\u1F08" # >A
        if s == 33: return "\u1F88" # >A|
        if s == 36: return "\u1F0C" # >'A
        if s == 37: return "\u1F8C" # >'A|
        if s == 40: return "\u1F0A" # >`A
        if s == 41: return "\u1F8A" # >`A|
        if s == 44: return "\u1F0E" # >~A
        if s == 45: return "\u1F8E" # >~A|
        return "\u0391" # A
    
    def visit_large_epsilon(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1FC9" # 'E
        if s ==  8: return "\u1FC8" # `E
        if s == 16: return "\u1F19" # <E
        if s == 20: return "\u1F1D" # <'E
        if s == 24: return "\u1F1B" # <`E
        if s == 32: return "\u1F18" # >E
        if s == 36: return "\u1F1C" # >'E
        if s == 40: return "\u1F1A" # >`E
        return "\u0395" # E

    def visit_large_eta(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  1: return "\u1FCC" # ^E|
        if s ==  4: return "\u1FCB" # '^E
        # if s ==  5: return "\uxxxx" # '^E|
        if s ==  8: return "\u1FCA" # `^E
        # if s ==  9: return "\uxxxx" # `^E|
        # if s == 12: return "\uxxxx" # ~^E
        # if s == 13: return "\uxxxx" # ~^E|
        if s == 16: return "\u1F29" # <^E
        if s == 17: return "\u1F99" # <^E|
        if s == 20: return "\u1F2D" # <'^E
        if s == 21: return "\u1F9D" # <'^E|
        if s == 24: return "\u1F2B" # <`^E
        if s == 25: return "\u1F9B" # <`^E|
        if s == 28: return "\u1F2F" # <~^E
        if s == 29: return "\u1F9F" # <`^E|
        if s == 32: return "\u1F28" # >^E
        if s == 33: return "\u1F98" # >^E|
        if s == 36: return "\u1F2C" # >'^E
        if s == 37: return "\u1F9C" # >'^E|
        if s == 40: return "\u1F2A" # >`^E
        if s == 41: return "\u1F9A" # >`^E|
        if s == 44: return "\u1F2E" # >~^E
        if s == 45: return "\u1F9E" # >~^E|
        return "\u0397" # ^E

    def visit_large_iota(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1FDB" # 'I
        if s ==  8: return "\u1FDA" # `I
        # if s ==  12: return "\uxxxx" # ~I
        if s == 16: return "\u1F39" # <I
        if s == 20: return "\u1F3D" # <'I
        if s == 24: return "\u1F3B" # <`I
        if s == 28: return "\u1F3F" # <~I
        if s == 32: return "\u1F38" # >I
        if s == 36: return "\u1F3C" # >'I
        if s == 40: return "\u1F3A" # >`I
        if s == 44: return "\u1F3E" # >~I
        if s == 64: return "\u03AA" # "I
        return "\u0399" # I

    def visit_large_omicron(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1FF9" # 'O
        if s ==  8: return "\u1FF8" # `O
        if s == 16: return "\u1F49" # <O
        if s == 20: return "\u1F4D" # <'O
        if s == 24: return "\u1F4B" # <`O
        if s == 32: return "\u1F48" # >O
        if s == 36: return "\u1F4C" # >'O
        if s == 40: return "\u1F4A" # >`O
        return "\u039F" # O

    def visit_large_upsilon(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1FEB" # 'Y
        if s ==  8: return "\u1FEA" # `Y
        # if s ==  12: return "\uxxxx" # ~Y
        if s == 16: return "\u1F59" # <Y
        if s == 20: return "\u1F5D" # <'Y
        if s == 24: return "\u1F5B" # <`Y
        if s == 28: return "\u1F5F" # <~Y
        if s == 64: return "\u03AB" # "Y
        return "\u03A5" # Y

    def visit_large_omega(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  1: return "\u1FFC" # ^O|
        if s ==  4: return "\u1FFB" # '^O
        # if s ==  5: return "\uxxxx" # '^O|
        if s ==  8: return "\u1FFA" # `^O
        # if s ==  9: return "\uxxxx" # `^O|
        # if s == 12: return "\uxxxx" # ~^O
        # if s == 13: return "\uxxxx" # ~^O|
        if s == 16: return "\u1F69" # <^O
        if s == 17: return "\u1FA9" # <^O|
        if s == 20: return "\u1F6D" # <'^O
        if s == 21: return "\u1FAD" # <'^O|
        if s == 24: return "\u1F6B" # <`^O
        if s == 25: return "\u1FAB" # <`^O|
        if s == 28: return "\u1F6F" # <~^O
        if s == 29: return "\u1FAF" # <`^O|
        if s == 32: return "\u1F68" # >^O
        if s == 33: return "\u1FA8" # >^O|
        if s == 36: return "\u1F6C" # >'^O
        if s == 37: return "\u1FAC" # >'^O|
        if s == 40: return "\u1F6A" # >`^O
        if s == 41: return "\u1FAA" # >`^O|
        if s == 44: return "\u1F6E" # >~^O
        if s == 45: return "\u1FAE" # >~^O|
        return "\u03A9" # ^O

    def visit_large_beta(self, node, visited_children):
        return "\u0392"

    def visit_large_gamma(self, node, visited_children):
        return "\u0393"

    def visit_large_delta(self, node, visited_children):
        return "\u0394"

    def visit_large_zeta(self, node, visited_children):
        return "\u0396"

    def visit_large_kappa(self, node, visited_children):
        if 'h' in node.text:
            return "\u03A7" # large khi
        else:
            return "\u039A" # large kappa

    def visit_large_lambda(self, node, visited_children):
        return "\u039B"

    def visit_large_mu(self, node, visited_children):
        return "\u039C"

    def visit_large_nu(self, node, visited_children):
        v, *_ = visited_children
        return v

    def visit_large_nasable_gamma_gamma(self, node, visited_children):
        *_, v = visited_children
        return "\u0393" + v

    def visit_large_nasable_gamma_kappa(self, node, visited_children):
        *_, v = visited_children
        return "\u0393" + v

    def visit_large_nasable_gamma_xi(self, node, visited_children):
        *_, v = visited_children
        return "\u0393" + v

    def visit_large_single_nu(self, node, visited_children):
        return "\u039D"

    def visit_large_xi(self, node, visited_children):
        return "\u039E"

    def visit_large_pi(self, node, visited_children):
        if "h" in node.text:
            return "\u03A6" # large phi
        elif "s" in node.text:
            return "\u03A8" # large psi
        else:
            return "\u03A0" # large pi

    def visit_large_rho(self, node, visited_children):
        s = self.calc_score(node.text)
        if s == 16 : return "\u1FEC"
        return "\u03A1"

    def visit_large_sigma(self, node, visited_children):
        return "\u03A3"

    def visit_large_tau(self, node, visited_children):
        if "h" in node.text:
            return "\u0398" # large theta
        else:
            return "\u03A4" # large tau

    def visit_small_alpha(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  1: return "\u1FB3" # a|
        if s ==  4: return "\u1F71" # 'a
        if s ==  5: return "\u1FB4" # 'a|
        if s ==  8: return "\u1F70" # `a
        if s ==  9: return "\u1FB2" # `a|
        if s == 12: return "\u1FB6" # ~a
        if s == 13: return "\u1FB7" # ~a|
        if s == 16: return "\u1F01" # <a
        if s == 17: return "\u1F81" # <a|
        if s == 20: return "\u1F05" # <'a
        if s == 21: return "\u1F85" # <'a|
        if s == 24: return "\u1F03" # <`a
        if s == 25: return "\u1F83" # <`a|
        if s == 28: return "\u1F07" # <~a
        if s == 29: return "\u1F87" # <`a|
        if s == 32: return "\u1F00" # >a
        if s == 33: return "\u1F80" # >a|
        if s == 36: return "\u1F04" # >'a
        if s == 37: return "\u1F84" # >'a|
        if s == 40: return "\u1F02" # >`a
        if s == 41: return "\u1F82" # >`a|
        if s == 44: return "\u1F06" # >~a
        if s == 45: return "\u1F86" # >~a|
        return "\u03B1"; # a

    def visit_small_epsilon(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1F73" # 'e
        if s ==  8: return "\u1F72" # `e
        if s == 16: return "\u1F11" # <e
        if s == 20: return "\u1F15" # <'e
        if s == 24: return "\u1F13" # <`e
        if s == 32: return "\u1F10" # >e
        if s == 36: return "\u1F14" # >'e
        if s == 40: return "\u1F12" # >`e
        return "\u03B5" # e

    def visit_small_eta(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  1: return "\u1FC3" # ^e|
        if s ==  4: return "\u1F75" # '^e
        if s ==  5: return "\u1FC4" # '^e|
        if s ==  8: return "\u1F74" # `^e
        if s ==  9: return "\u1FC2" # `^e|
        if s == 12: return "\u1FC6" # ~^e
        if s == 13: return "\u1FC7" # ~^e|
        if s == 16: return "\u1F21" # <^e
        if s == 17: return "\u1F91" # <^e|
        if s == 20: return "\u1F25" # <'^e
        if s == 21: return "\u1F95" # <'^e|
        if s == 24: return "\u1F23" # <`^e
        if s == 25: return "\u1F93" # <`^e|
        if s == 28: return "\u1F27" # <~^e
        if s == 29: return "\u1F97" # <`^e|
        if s == 32: return "\u1F20" # >^e
        if s == 33: return "\u1F90" # >^e|
        if s == 36: return "\u1F24" # >'^e
        if s == 37: return "\u1F94" # >'^e|
        if s == 40: return "\u1F22" # >`^e
        if s == 41: return "\u1F92" # >`^e|
        if s == 44: return "\u1F26" # >~^e
        if s == 45: return "\u1F96" # >~^e|
        return "\u03B7" # ^e

    def visit_small_iota(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1F77" # 'i
        if s ==  8: return "\u1F76" # `i
        if s == 12: return "\u1FD6" # ~i
        if s == 16: return "\u1F31" # <i
        if s == 20: return "\u1F35" # <'i
        if s == 24: return "\u1F33" # <`i
        if s == 28: return "\u1F37" # <~i
        if s == 32: return "\u1F30" # >i
        if s == 36: return "\u1F34" # >'i
        if s == 40: return "\u1F32" # >`i
        if s == 44: return "\u1F36" # >~i
        if s == 64: return "\u03CA" # "i
        if s == 68: return "\u1FD3" # "'i
        if s == 72: return "\u1FD2" # "`i
        if s == 76: return "\u1FD7" # "~i
        return "\u03B9" # i

    def visit_small_omicron(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1F79" # 'o
        if s ==  8: return "\u1F78" # `o
        if s == 16: return "\u1F41" # <o
        if s == 20: return "\u1F45" # <'o
        if s == 24: return "\u1F43" # <`o
        if s == 32: return "\u1F40" # >o
        if s == 36: return "\u1F44" # >'o
        if s == 40: return "\u1F42" # >`o
        return "\u03BF" # o

    def visit_small_upsilon(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  4: return "\u1F7B" # 'y
        if s ==  8: return "\u1F7A" # `y
        if s == 12: return "\u1FE6" # ~y
        if s == 16: return "\u1F51" # <y
        if s == 20: return "\u1F55" # <'y
        if s == 24: return "\u1F53" # <`y
        if s == 28: return "\u1F57" # <~y
        if s == 32: return "\u1F50" # >y
        if s == 36: return "\u1F54" # >'y
        if s == 40: return "\u1F52" # >`y
        if s == 44: return "\u1F56" # >~y
        if s == 64: return "\u03CB" # "y
        if s == 68: return "\u1FE3" # "'y
        if s == 72: return "\u1FE2" # "`y
        if s == 76: return "\u1FE7" # "~y
        return "\u03C5"# y

    def visit_small_omega(self, node, visited_children):
        s = self.calc_score(node.text)
        if s ==  1: return "\u1FF3" # ^o|
        if s ==  4: return "\u1F7D" # '^o
        if s ==  5: return "\u1FF4" # '^o|
        if s ==  8: return "\u1F7C" # `^o
        if s ==  9: return "\u1FF2" # `^o|
        if s == 12: return "\u1FF6" # ~^o
        if s == 13: return "\u1FF7" # ~^o|
        if s == 16: return "\u1F61" # <^o
        if s == 17: return "\u1FA1" # <^o|
        if s == 20: return "\u1F65" # <'^o
        if s == 21: return "\u1FA5" # <'^o|
        if s == 24: return "\u1F63" # <`^o
        if s == 25: return "\u1FA3" # <`^o|
        if s == 28: return "\u1F67" # <~^o
        if s == 29: return "\u1FA7" # <`^o|
        if s == 32: return "\u1F60" # >^o
        if s == 33: return "\u1FA0" # >^o|
        if s == 36: return "\u1F64" # >'^o
        if s == 37: return "\u1FA4" # >'^o|
        if s == 40: return "\u1F62" # >`^o
        if s == 41: return "\u1FA2" # >`^o|
        if s == 44: return "\u1F66" # >~^o
        if s == 45: return "\u1FA6" # >~^o|
        return "\u03C9"; # ^o
    
    def visit_small_beta(self, node, visited_children):
        return "\u03B2"

    def visit_small_gamma(self, node, visited_children):
        return "\u03B3"

    def visit_small_delta(self, node, visited_children):
        return "\u03B4"

    def visit_small_zeta(self, node, visited_children):
        return "\u03B6"

    def visit_small_kappa(self, node, visited_children):
        if 'h' in node.text:
            return "\u03C7" # small khi
        else:
            return "\u03BA" # small kappa

    def visit_small_lambda(self, node, visited_children):
        return "\u03BB"

    def visit_small_mu(self, node, visited_children):
        return "\u03BC"

    def visit_small_nu(self, node, visited_children):
        v, *_ = visited_children
        return v

    def visit_small_nasable_gamma_gamma(self, node, visited_children):
        *_, v = visited_children
        return "\u03B3" + v

    def visit_small_nasable_gamma_kappa(self, node, visited_children):
        *_, v = visited_children
        return "\u03B3" + v

    def visit_small_nasable_gamma_xi(self, node, visited_children):
        *_, v = visited_children
        return "\u03B3" + v

    def visit_small_single_nu(self, node, visited_children):
        return "\u03BD"

    def visit_small_xi(self, node, visited_children):
        return "\u03BE"

    def visit_small_pi(self, node, visited_children):
        if "h" in node.text:
            return "\u03C6" # small phi
        elif "s" in node.text:
            return "\u03C8" # small psi
        else:
            return "\u03C0" # small pi

    def visit_small_rho(self, node, visited_children):
        s = self.calc_score(node.text)
        if s == 16 : return "\u1FE5"
        if s == 32 : return "\u1FE4"
        return "\u03C1"

    def visit_small_sigma(self, node, visited_children):
        v, *_ = visited_children
        return v

    def visit_small_leading_sigma(self, node, visited_children):
        *_, v = visited_children
        return "\u03C3" + v

    def visit_small_single_sigma(self, node, visited_children):
        if node.text == "s":
            return "\u03C2" # final sigma
        else:
            return "\u03C3" # leading sigma

    def visit_small_tau(self, node, visited_children):
        if "h" in node.text:
            return "\u03B8" # small theta
        else:
            return "\u03C4" # small tau

    def visit_punctuation(self, node, visited_children):
        v, *_ = visited_children
        return v

    def visit_semicoron(self, node, visited_children):
        return "\u0387"

    def visit_question(self, node, visited_children):
        return "\u037E"
    
    def visit_new_line(self, node, visited_children):
        return node.text

    def visit_any_char(self, node, visited_children):
        return node.text

    def generic_visit(self, node, visited_children):
        return visited_children or node