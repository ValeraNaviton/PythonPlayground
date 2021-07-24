import collections
from typing import List
from typing import Dict


class Solution:
    def stringToKeys(self, dottedString: str) -> List[str]:
        result = []
        result.append(dottedString)

        for i in range(len(dottedString)):
            if dottedString[i] == ".":
                result.append(dottedString[i + 1:])

        return result

    def subdomainVisits(self, cpdomains: List[str]):
        domainCounts = {}
        result = []
        for j in range(len(cpdomains)):
            v, k = cpdomains[j].split()
            keylist = self.stringToKeys(k)
            for key in keylist:
                print("key = %s, value = %d" % (key, int(v)))
                if domainCounts.get(key) is None:
                    domainCounts.update({key: int(v)})
                else:
                    domainCounts.update({key: int(v) + domainCounts.get(key)})

        for s in domainCounts.keys():
            result.append(str(domainCounts.get(s)) + " " + s)
        return result



cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
dottedString = "aaa.bbb.cc"
cpdomains2 = ["11 a.b.c", "9 x.b.c", "10 d.b.c"]
print(Solution().subdomainVisits(cpdomains))
