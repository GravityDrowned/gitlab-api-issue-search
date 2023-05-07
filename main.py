# https://python-gitlab.readthedocs.io/en/stable/api-usage.html
import gitlab


def search_gitlab_discussions_for_string(access_token, project_id, query):
    gl = gitlab.Gitlab(url='https://gitlab.rrze.fau.de', private_token=access_token)
    project = gl.projects.get(project_id)
    statistics = project.issues_statistics.get()


    issues = project.issues.list(get_all=True)
    for issue in issues:
        discussions = issue.discussions.list()
        for discussion in discussions:
            for note in discussion.attributes['notes']:
                if query in note['body']:
                    print('#'+str( issue.attributes['iid']))
                    print(note['body'])


if __name__ == "__main__":
    # project_id is a little number under the name of your project - link-example: https://gitlab.rrze.fau.de/cdi/labs/wisski/<YOUR PROJECT NAME>
    search_gitlab_discussions_for_string('YOUR API TOKEN HERE', 1423, 'time-pad')