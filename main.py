import os
import json
import sys

# original library
from scraping.submission_ids import get_submission_ids
from scraping.submission import get_ac_submission, Submission

def load_conf():
  # Load conf.json
  conf = json.load(open('conf.json', 'r'))

  # Get contest from args
  args = sys.argv
  contest = args[1]
  conf['contest'] = contest
  return conf

def get_latest_ac_submissions(user: str, contest: str) -> list[Submission]:
  submission_ids = get_submission_ids(user, contest)
  ac_submissions = (get_ac_submission(submission_id, contest) for submission_id in submission_ids)

  # {key: [Submission, Submission, Submission, ...], key: [Submission, Submission, Submission, ...], ...}
  submission_per_problems = {}
  for ac_submission in ac_submissions:
    print(ac_submission.fixtime)
    if (ac_submission.problem in submission_per_problems):
      submission_per_problems[ac_submission.problem].append(Submission(ac_submission.code, ac_submission.problem, ac_submission.status, ac_submission.fixtime))
    else:
      submission_per_problems[ac_submission.problem] = [Submission(ac_submission.code, ac_submission.problem, ac_submission.status, ac_submission.fixtime)]

  # sort by fixtime
  for problem in submission_per_problems:
    submission_per_problems[problem].sort(key=lambda submission: submission.fixtime)

  latest_ac_submissions = []
  for problem in submission_per_problems:
    latest_ac_submissions.append(submission_per_problems[problem][-1])
  
  return latest_ac_submissions

def commit(submissions: list[Submission], contest: str, extension: str):
  code_dir = 'codes/'
  contest_dir = os.path.join(code_dir, contest)
  os.makedirs(contest_dir, exist_ok=True)
  for submission in submissions:
    code = submission.code
    file_name = submission.problem + '.' + extension
    f = open(os.path.join(contest_dir, file_name), 'w')
    f.write(code)

  # staging
  os.chdir(code_dir)
  os.system('git add {}'.format(contest))
  # commit
  os.system('git commit -m {}'.format(contest))
  # push
  os.system('git push origin head')

def main():
  conf = load_conf()
  latest_ac_submissions = get_latest_ac_submissions(conf['user'], conf['contest'])
  commit(latest_ac_submissions, conf['contest'], conf['extension'])

if __name__ == '__main__':
  main()
