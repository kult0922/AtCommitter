from SubmissionCode import getSubmissionCode
from SubmissionNumberList import getSubmissionNumberList
import os

def main():
  user = 'Kurt_'
  contest = 'abc290'
  extension = 'cpp'

  problem_codes = {}

  submission_number_list = getSubmissionNumberList(user, contest)
  for submission_number in submission_number_list:
    code, problem, status, fixtime = getSubmissionCode(submission_number, contest)
    if (status != 'AC'):
      continue

    if (problem in problem_codes):
      problem_codes[problem].append((code, fixtime))
    else:
      problem_codes[problem] = [(code, fixtime)]


  # sort by fixtime
  for problem in problem_codes:
    problem_codes[problem].sort(key=lambda x: x[1])

  # create files
  contest_dir = os.path.join('codes', contest)
  os.makedirs(contest_dir, exist_ok=True)
  for problem in problem_codes:
    latest_ac_code = problem_codes[problem][-1][0]
    file_name = problem + '.' + extension
    f = open(os.path.join(contest_dir, file_name), 'w')
    f.write(latest_ac_code)

if __name__ == '__main__':
  main()

