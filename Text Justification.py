class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line_words = []
        line_length = 0

        for w in words:
            if line_length + len(w) + len(line_words) <= maxWidth:
                line_words.append(w)
                line_length += len(w)
            else:
                if len(line_words) == 1:
                    line = line_words[0] + ' ' * (maxWidth - line_length)
                else:
                    total_spaces = maxWidth - line_length
                    gaps = len(line_words) - 1
                    base_spaces = total_spaces // gaps
                    extra_spaces = total_spaces % gaps

                    line = line_words[0]
                    for i in range(1, len(line_words)):
                        spaces = base_spaces + (1 if i <= extra_spaces else 0)
                        line += ' ' * spaces + line_words[i]

                result.append(line)

                line_words = [w]
                line_length = len(w)

        last_line = ' '.join(line_words)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result