Development Notes
=================

.. include:: ../TODO.rst

Git workflow
------------

Example workflow::

    git checkout master # make sure you are on the local master branch
    git pull # make sure it is up to date (resolve conflicts here ...)
    git checkout develop # put me on the develop branch way down there
    git merge master # a lot happens .. look for "Fast-forward" = good sign
    git push # get develop and origin/develop in sync
    <now work on develop>        
            
            
**Background Reading**

* "Think Like (a) Git: A Guide for the Perplexed" by Sam Livingston-Gray [`link <http://think-like-a-git.net/>`__].  A graph-theory view of the git workflow.

* "Git Workflow Tutorial" at Atlassian [`link <https://www.atlassian.com/git/workflows>`__].  An overview of the possible workflows: centralized, feature branch, gitflow, forking, and pull requests.

* "Simple Git workflow is simple: A basic basic branching workflow for continuous delivery" by Nicola Paolucci at Atlassian [`link <http://blogs.atlassian.com/2014/01/simple-git-workflow-simple/>`__].  Described the ``rebase`` approach. 

Preparing for distribution
--------------------------

* "Open Sourcing the Project the Right Way" by Keff Knupp [`link <http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/>`__].