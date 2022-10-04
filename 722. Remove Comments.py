class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source = '\n'.join(source)
        return filter(None, re.sub(r'//.*|/\*(.|\n)*?\*/', '', source).split('\n'))
# very wise to use '\n' to conmbine them, then use regular expression to match \\... or /*...*/
# * is special in regular expression, so use \*
# use non-greedy match, so use .*?, while . does not include \n, so use |.
# use split('\n') to make it readable. Or else it is just a char array.