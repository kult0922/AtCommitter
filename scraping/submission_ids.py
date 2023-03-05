import requests
import re
from html.parser import HTMLParser

class SubmissionIdsParser(HTMLParser):
  def __init__(self, contest):
    super().__init__()
    self.submission_ids = []
    self.contest = contest

  def handle_starttag(self, tag, attrs):
    href = dict(attrs).get('href', '')
    if re.match('^\/contests\/{}\/submissions\/[0-9]+$'.format(self.contest), href):
      self.submission_ids.append(href.split('/')[-1])

def get_submission_ids(user: str, contest: str) -> list[str]:
  url = 'https://atcoder.jp/contests/{}/submissions?f.Task=&f.LanguageName=&f.Status=AC&f.User={}'.format(contest, user)
  content = requests.get(url).text
  parser = SubmissionIdsParser(contest)
  parser.feed(content)

  return parser.submission_ids
