# Example 1
1. "abb" accept
2. "aba" reject
3. "baabbba" accept
4. "bbaba" reject
5. "aaabbbb"

S->aSX|bSY|b
X->b
Y->a




#Example 2
1. "aaaabbbb" reject
2. "abbb" accept
3. "ababb" accept
4. "bbbab" reject
5. "abbbab" reject

S
a,b
S-> aSA|aSC|b
A-> bB
B-> b
C-> aA



