from dataclasses import dataclass
import requests
import re
from html.parser import HTMLParser

@dataclass
class Submission:
  code: str
  problem: str
  status: str
  fixtime: str

class SubmissionCodeParser(HTMLParser):
  def __init__(self, contest: str):
    super().__init__()
    self.contest = contest
    self.parse_submission_code = False
    self.parse_fixtime = False
    self.parse_status = False
    self.submission_code = ''
    self.fixtime = ''
    self.problem = ''

  def handle_starttag(self, tag, attrs):
    d = dict(attrs)
    if 'submission-code' in d.get('id', ''):
      self.parse_submission_code = True

    if 'judge-status' in d.get('id', ''):
      self.parse_status = True

    if 'fixtime-second' in d.get('class', ''):
      self.parse_fixtime = True

    href = dict(attrs).get('href', '')
    if re.match('^\/contests\/{}\/tasks\/{}_*'.format(self.contest, self.contest), href):
      self.problem = href.split('/')[-1]

  def handle_data(self, data):
    if self.parse_submission_code:
      self.submission_code = data
      self.parse_submission_code = False

    if self.parse_status:
      self.status = data
      self.parse_status = False

    if self.parse_fixtime:
      self.fixtime = data
      self.parse_fixtime = False

def get_ac_submission(submission_number: str, contest: str) -> Submission:
  url = 'https://atcoder.jp/contests/{}/submissions/{}'.format(contest, submission_number)
  content = requests.get(url).text
  parser = SubmissionCodeParser(contest)
  parser.feed(content)

  return Submission(parser.submission_code, parser.problem, parser.status, parser.fixtime)
