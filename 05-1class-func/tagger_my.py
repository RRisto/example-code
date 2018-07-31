# BEGIN TAG_FUNC
def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
# END TAG_FUNC

print(tag('br')) # <1>
print(tag('p', 'hello')) # <2>
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33)) # <3>
print(tag('p', 'hello', 'world', cls='sidebar'))  # <4>
print(tag(content='testing', name="img"))  # <5>
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

def f(a, *,b):
    return a, b

print(f(1,b=2))

def f(*,a,b):
    return a, b

print(f(a=1,b=2))