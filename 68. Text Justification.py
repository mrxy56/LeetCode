class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0
        current_width = 0
        line = []
        
        while i < len(words):
            word = words[i]
            if (current_width + len(word)) <= maxWidth:
                line.append(word)
                current_width += len(word) + 1
                i += 1
            else: 
                current_line = ""
                necessary_spaces = maxWidth - current_width + len(line) 
                if len(line) == 1:
                    current_line += line[0] + " " * necessary_spaces
                else:
                    for j in range(len(line)):
                        line_word = line[j]
                        remaining_words = len(line) - (j + 1)
                        required_spaces = ceil(necessary_spaces / remaining_words) if remaining_words else 0
                        current_line += line_word + " " * required_spaces
                        necessary_spaces -= required_spaces
                lines.append(current_line)
                line = []
                current_width = 0
        if line: 
            necessary_spaces = maxWidth - current_width + 1
            current_line = ' '.join(line) + " " * necessary_spaces
            lines.append(current_line)
        return lines

# A solution from the forum. Very wise to control the necessary spaces dynamically (including using ceil function.)
# Structure is good, since you read and append, if exceed, then output, clear variables.
# Finally, if there are still some words, process it seperately.
