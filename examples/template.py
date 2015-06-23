from string import Template

s = Template('$who like $what')
s.substitute(who='tim', what='kung pao')
d = dict(who='tim', what='kung pao')

print Template('Give $who $$100').substitute(d)

print Template('$who like $what').substitute(d)

print Template('$who likes $what').safe_substitute(d)
