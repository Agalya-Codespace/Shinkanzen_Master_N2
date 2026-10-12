"""List every {漢字|かな} pair in the given files with a count, for proofreading."""
import re, sys, collections
c = collections.Counter()
for f in sys.argv[1:]:
    c.update(re.findall(r"\{([^{}|]+)\|([^{}]+)\}", open(f, encoding="utf-8").read()))
print(" ".join("%s=%s" % k for k, _ in sorted(c.items())))
