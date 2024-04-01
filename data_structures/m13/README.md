# String Matching Algorithms

## Pattern matching algorithms (Brute Force)

- Naive approach meaning very basic and simple algorithm
- Match all possible combinations of input pattern in given string
- Algorithm is very naive and not suitable for really long text
- Time Complexity -> O(m(n - m + 1)), where m is length of pattern and n is length of text

## Rabin-Karp pattern matching algorithm

- Improves performance by reducing number of comparisons with help of hashing
- Concept: if hash values of two strings are equal, assumed that both strings are also equal
- However, it is possible that there can be two different strings whose hash values are equal
- Spurious hit: happens due to collisions in hashing
- Steps
    - preprocess pattern before starting search, compute hash value of pattern of length `m` and
      hash values of all possible substrings of text of length `m`; total number of possible
      substrings would be (n-m+1), where `n` is length of text
    - compare hash value of pattern with hash value of substrings of text one by one
    - if hash values are not matched, then we shift pattern by one position
    - if hash value of pattern and hash value of substring of text match, then compare pattern and
      substring character by character to ensure that pattern is actually matched in text
    - continue process of until we reach end of given text string
- Time Complexity -> O(m(n - m + 1)), where m is length of pattern and n is length of text

## Knuth-Morris-Pratt (KMP) algorithm

- Concept: overlapping text in pattern itself can be used to immediately know at time of any
  mismatch how much pattern should be shifted to skip unnecessary comparisons
- Precompute prefix function that indicates required number of shifts of pattern whenever we get a
  mismatch
- KMP preprocesses pattern to avoid unnecessary comparisons using prefix function
- Algorithm utilizes prefix function to estimate how much pattern should be shifted to search
  pattern in text string whenever we get a mismatch
- Efficient as it minimizes number of comparisons of given patterns with respect to text string
- Steps
    - precompute prefix function for given pattern and initialize a counter `q` that represents
      number of characters that matched
    - start by comparing first character of pattern with first character of text string, and if this
      matches, then increment counter `q` for pattern and counter for text string, and we compare
      next character
    - if there is a mismatch, then assign value of precomputed prefix function for `q` to index
      value of `q`
    - continue searching pattern in text string until we reach end of text, if we do not find any
      matches; if all characters in pattern are matched in text string, we return position where
      pattern is matched in text and continue to search for another match
- Time Complexity -> O(n + m), where n is length of text and m is length of pattern

## Boyer-Moore pattern matching algorithm

- Further improves performance of pattern matching by skipping comparisons
- Concepts to Understand
    - shift pattern in direction from left to right, similar to KMP algorithm
    - compare characters of pattern and text string from right to left, which is opposite of what we
      do in the case of KMP algorithm
    - skips unnecessary comparisons by using good suffix and bad character shift heuristics,
      heuristics find possible number of comparisons that can be skipped; slide pattern over given
      text with greatest offsets suggested by both of these heuristics
- Shift pattern accordingly for any mismatch
    - if mismatched character of text does not occur in pattern, then shift pattern next to
      mismatched character
    - if mismatched character has one occurrence in pattern, then shift pattern in such a way that
      we align with mismatched character
    - if mismatched character has more than one occurrence in pattern, then make most minimal shift
      possible to align pattern with that character
- Preprocessing Time Complexity -> O(m)
- Searching Time Complexity -> O(mn)
