.. post:: Oct 31, 2025 08:00:00
   :tags: GitHub, workflow
   :category: DevOps, GitOps

Custom GitHub templates for issues
==================================

Automating workflows reduces the need to think about them, but can also guide new people in the right direction. One of these workflows is creating issues for example. One could use the default templates provided by `GitHub`_ to create an issue for a bug or a new feature. Only default templates may not fulfill all requirements needed for a smooth workflow for a project on GitHub.

Templates per organization
--------------------------

By default, GitHub has templates for issues and pull requests, but on both organization and repository levels, an override can take place. Meaning that the most specific template set will be used when creating an issue or pull request. First, we will define templates for the whole organization by creating the :file:`.github` repository within the organization.

Now that repository :file:`<organization>/.github` exists, this repository can be extended by creating the directory :file:`.github/ISSUE_TEMPLATE`. This directory will be the home for the templates for all repositories within the organization. The two template files as shown in the examples below need to be added and when to commit in the master branch of :file:`<organization>/.github` these two templates will show up for all repositories within the organization.

.. code-block::
    :caption: Template file :file:`.github/ISSUE_TEMPLATE/bug_report.yml`

    ---
    name: Bug report
    description: Create a report to help us improve
    title: ''
    labels: 'bug'
    assignees: ''

    ---

    **Describe the bug**
    A clear and concise description of what the bug is.
    ...

.. code-block::
    :caption: Template file :file:`.github/ISSUE_TEMPLATE/feature_request.yml`

    ---
    name: Feature request
    description: Suggest an idea for this project
    title: ''
    labels: 'enhancement'
    assignees: ''

    ---

    **Is your feature request related to a problem? Please describe.**
    A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]
    ...

Overriding templates
--------------------

There is always the exception that one repository within an organization requires other issue templates. GitHub does allow to override of organizational templates per repository by creating the directory :file:`.github/ISSUE_TEMPLATE` within that specific repository. From this point forward only templates found in this directory will be used. When the example template shown below is added to the repository only the template **Documentation request** is presented when creating an issue.

.. code-block::
    :caption: Template file :file:`.github/ISSUE_TEMPLATE/documentation.yml`

    ---
    name: Documentation request
    description: Suggest to improve documentation
    title: ''
    labels: 'documentation'
    assignees: ''

    ---

    **Is your documentation request related to a problem? Please describe.**
    A clear and concise description of what the problem is. Ex. The explaination is unclear for [...]

.. note::

    Creating a file in the directory :file:`.github/ISSUE_TEMPLATE` of a repository overrides all templates set by default by GitHub or in the organization. Templates from repository ``<organization>/.github`` must be copied manually if they need to be presented as an option.

Template autonomy
-----------------

The templates must be located in the :file:`.github/ISSUE_TEMPLATE` folder and can be stored in the YAML or Markdown format, but the required keys differ between formats both formats. For the Markdown format the keys ``name:`` and ``about:`` should exist as shown in the example below.

.. code-block::
    :caption: Template file :file:`.github/ISSUE_TEMPLATE/bug_report.md`

    ---
    name: Bug report
    about: Create a report to help us improve
    title: ''
    labels: 'bug'
    assignees: ''

    ---

    **Describe the bug**
    A clear and concise description of what the bug is.

Templates in the YAML format require the keys ``name:`` and ``description:`` to be used correctly, as shown in the example below.

.. code-block::
    :caption: Template file :file:`.github/ISSUE_TEMPLATE/bug_report.yml`

    ---
    name: Bug report
    description: Create a report to help us improve
    title: ''
    labels: 'bug'
    assignees: ''

    ---

    **Describe the bug**
    A clear and concise description of what the bug is.

Other **optional** keys that can be used to set a default value are:

- ``title:`` to filling the incident
- ``labels:`` to add one or more labels when creating a new issue
- ``assignees:`` to assign the new issue to one or more GitHub usernames

With this most areas are covered about templates for issues, and more :github:repo:`example templates<stevemao/github-issue-templates>` can be found on GitHub to see what other projects are using.

.. note::

    Templates are parsed as a :wikipedia:`YAML` file and will follow the structure including that colon is the separator between variable and value. Any values containing a colon must be surrounded with quotes like ``title: "bug: [short description]"``

.. _GitHub: https://github.com