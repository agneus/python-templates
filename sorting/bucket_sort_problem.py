from collections import defaultdict

def longest_subsequence_word(s, dictionary):
    """
    Return the longest word in `dictionary` that is a subsequence of `s`.
    Runs in O(|s| + total length of all words in dictionary).
    """
    # buckets[char] = list of (word, position_in_word)
    buckets = defaultdict(list)
    best = ""

    # Initialize: each word waits for its first character
    for word in dictionary:
        if not word:   # empty word, ignore (never longest)
            continue
        first_char = word[0]
        buckets[first_char].append((word, 0))  # pos = 0 means next needed is word[0]

    # Stream through s once
    for ch in s:
        waiting = buckets[ch]
        if not waiting:
            continue

        # We've processed this character, clear bucket
        buckets[ch] = []

        for word, pos in waiting:
            pos += 1  # we matched word[pos] with ch

            if pos == len(word):
                # whole word matched -> subsequence of s
                if len(word) > len(best):
                    best = word
                # if tie-breaking needed (lexicographically etc.), handle here
            else:
                # still more chars to match; wait on next required char
                next_char = word[pos]
                buckets[next_char].append((word, pos))

    return best
