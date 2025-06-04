from collections import abc
from functools import total_ordering

@total_ordering
class JobApplicant:
    def __init__(self, applicant_id, years_experience, is_recommended, first_interview_score, second_interview_score):
        self.applicant_id = applicant_id
        self.years_experience = years_experience
        self.is_recommended = is_recommended
        self.first_interview_score = first_interview_score
        self.second_interview_score = second_interview_score

    @property
    def score(self):
        score = self.years_experience / 2
        score += int(self.is_recommended)
        score += self.first_interview_score / 2
        score += self.second_interview_score
        return round(score, 2)
    
    def __repr__(self):
        return f"{self.__class__.__name__}(applicant_id='{self.applicant_id}', years_experience='{self.years_experience}', is_recommended='{self.is_recommended}', first_interview_score='{self.first_interview_score}', second_interview_score='{self.second_interview_score}', score='{self.score}')"
    
    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

class JobApplicantPool(abc.Sequence):
    def __init__(self):
        self._applicants = []

    def add(self, applicant):
        self._applicants.append(applicant)

    def __len__(self):
        return len(self._applicants)
    
    def __getitem__(self, item):
        return self._applicants[item]

    def __repr__(self):
        return f"Applicant Pool\n(Score | ID)\n-------------{"".join([f"\n{str(applicant.score)} - {applicant.applicant_id}" for applicant in sorted(self._applicants, reverse=True)])}"

    


ja1 = JobApplicant('1234', 5, False, 3.1, 4.6)
ja2 = JobApplicant('6799', 10, False, 3.1, 7.4)
print(ja1)
print(ja2)
jab = JobApplicantPool()
jab.add(ja1)
jab.add(ja2)
print(jab)