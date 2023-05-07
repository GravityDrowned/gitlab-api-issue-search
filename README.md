# gitlab-search-without-premium

## intro
GitLab allows to search inside of issues. A useful feature.  
This is my python script to search inside issues via the API.

## installation

with python installed:  
`$ pip install -r requirements.txt`

## execution
You have to run `search_gitlab_discussions_for_string(` with your GitLab Access token, the ID of your project you want to search the discussions in and the actual query you want to search for.

Right now only complete string matches are supported....

`search_gitlab_discussions_for_string('YOUR TOKEN HERE', YOUR PROJECT ID HERE, 'YOUR SEACH QUERY HERE')`



