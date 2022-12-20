import sys
import re
l = sys.stdin.readlines()
def remove_string(s, start, end):
    return s[:start] + s[end:]

for line in l:
    org = line[::] # copy
    line = re.sub('&lt;', '', line)
    line = re.sub('&gt;', '', line)
    line = re.sub('&amp;', '', line)
    def check_hex():
        global line
        for tag in re.finditer('&x[0-9|A-F|a-f]{2,};', org):
            tag = tag.group()
            if len(tag)%2==0:
                return False
            else:
                line = re.sub(tag, '', line)
        return True
        
    def check_context():
        global line
        context = []
        for tag in re.finditer('<[0-9|a-z|/]*?>', org):
            tag = tag.group()
            if tag in ['<>', '</>']:
                return False
            elif tag.count('/')>1:
                return False
            elif tag[-2:]=='/>': # <tag/>
                continue
            elif tag[:2]=='</': # </tag>
                if not context:
                    return False
                else:
                    if context[-1][1:-1] == tag[2:-1]:
                        line = remove_string(line, *(re.search(context[-1], line).span())) 
                        line = remove_string(line, *(re.search(tag, line).span())) 
                        context.pop()
            elif tag[0]=='<': # <tag>
                context.append(tag)
            # print('context:', context, tag)
            # print(line)
        # print('context:', context)
        return False if context else True

    line = re.sub('<[0-9|a-z]*?/>', '', line)
    print('valid' if check_context() and check_hex() and not re.search('<|>|&', line) else 'invalid')