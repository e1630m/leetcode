class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        clean = []
        for m in emails:
            at = m.index('@')
            try:
                front = m[:m.index('+')].replace('.', '')
            except ValueError:
                front = m[:at].replace('.', '')
            clean.append(front + m[at:])
        return len(set(clean))
