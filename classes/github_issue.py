from github import Github
from github import GithubException

class GithubIssue(object):
    def __init__(self, token):
        self.token = token

    def make_issue(self, repo_name, issue_title, issue_body='', organization=''):
        git = Github("{}".format(self.token))
        if organization == '0':
            try:
                repo = git.get_user().get_repo('{}'.format(repo_name))
                issue = repo.create_issue("{}".format(
                    issue_title), "{}".format(issue_body))
            except GithubException as error:
                print("Error: %s" % str(error))
                issue = 0
        elif organization != '0':
            try:
                organization = git.get_organization("{}".format(organization))
                repo = organization.get_repo('{}'.format(repo_name))
                issue = repo.create_issue("{}".format(
                    issue_title), "{}".format(issue_body))
            except GithubException as error:
                print("Error: %s" % str(error))
                issue = 0

        return issue
