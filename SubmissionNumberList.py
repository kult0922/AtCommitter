import requests
import re
from html.parser import HTMLParser

class SubmissionNumberListParser(HTMLParser):
  def __init__(self, contest):
    super().__init__()
    self.submission_number_list = []
    self.contest = contest

  def handle_starttag(self, tag, attrs):
    href = dict(attrs).get('href', '')
    if re.match('^\/contests\/{}\/submissions\/[0-9]+$'.format(self.contest), href):
      self.submission_number_list.append(href.split('/')[-1])

def getSubmissionNumberList(user: str, contest) -> str:
  url = 'https://atcoder.jp/contests/{}/submissions?f.Task=&f.LanguageName=&f.Status=&f.User={}'.format(contest, user)
  content = requests.get(url).text
  parser = SubmissionNumberListParser(contest)
  parser.feed(content)

  return parser.submission_number_list


if __name__ == '__main__':
  getSubmissionNumberList('Kurt_', 'abc290')