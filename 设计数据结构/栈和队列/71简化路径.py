class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for c in path:
            if c == '..':
                if stack:
                    stack.pop()
            elif c and c != '.':
                stack.append(c)
        return '/' + '/'.join(stack)