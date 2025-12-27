.. post:: 2025-12-15 00:00:00
  :tags: GitHub, GitHub Actions, GitHub Wiki, GitHub Annotations, Markdown, lint
  :category: GitOps

How to use GitHub Actions to automatically upload to GitHub Wiki
================================================================

`GitHub <https://github.com>`_ is a great platform for hosting open source projects. It provides a lot of features for free, including a wiki for documentation. However, the wiki is primarily designed to be edited through the web interface. This is not ideal for a lot of reasons as it makes it difficult to track changes from the repository. But there is a way to automatically upload to the wiki using GitHub Actions as GitHub provides a way to checkout the wiki as a separate repository.

Create a GitHub Action to upload to the wiki
--------------------------------------------

The first step is to create a GitHub Action that will upload the wiki. This can be done by creating a new file in the ``.github/workflows`` directory. The following example shows how to create a GitHub Action that will upload the wiki on every push to the master branch and on every change to the ``.github/workflows/wiki.yml`` file or the ``wiki`` directory.

.. code-block:: yaml
    :caption: Example workflow file :file:`.github/workflows/wiki.yml`

    ---
    name: GitHub Wiki upload

    on:
      push:
        branches:
          - master
        paths: [wiki/**, .github/workflows/wiki.yml]

    concurrency:
      group: wiki
      cancel-in-progress: true

    permissions:
      contents: write

    jobs:
      wiki:
        name: Publish to GitHub Wiki
        runs-on: ubuntu-latest
        steps:
          - name: Checkout Code
            uses: actions/checkout@v6
            with:
              repository: ${{github.repository}}
              path: ${{github.repository}}

          - name: Checkout Wiki
            uses: actions/checkout@v6
            with:
              repository: ${{github.repository}}.wiki
              path: ${{github.repository}}.wiki

          - name: Push to wiki
            run: |
              set -e
              cd $GITHUB_WORKSPACE/${{github.repository}}.wiki
              cp -r $GITHUB_WORKSPACE/${{github.repository}}/wiki/* .
              git config --local user.email "action@github.com"
              git config --local user.name "GitHub Action"
              git add .
              git diff-index --quiet HEAD || git commit -m "action: wiki sync" && git push

The ``concurrency`` section is used to ensure that only one instance of the GitHub Action is running at a time. This is important as the GitHub Action will be modifying the wiki repository directly. The ``permissions`` section is used to ensure that the GitHub Action has write access to the wiki repository in the last step when the changes are pushed to the wiki repository.

Validate markdown files with pymarkdownlnt
------------------------------------------

Now that the wiki is automatically updated, it is important to ensure that the markdown files are valid. This can be done using :github:repo:`pymarkdownlnt <jackdewinter/pymarkdown>`. The following example shows how to use GitHub Actions to validate markdown files in the repository.

.. code-block:: yaml
    :caption: Example workflow file :file:`.github/workflows/lint.yml`

    ---
    name: Linting

    on:
      pull_request:
      push:
        branches:
          - master

    jobs:
      lint:
        name: Lint Code Base
        runs-on: ubuntu-latest
        steps:
          - name: Checkout Code
            uses: actions/checkout@v6

          - name: Set up Python
            uses: actions/setup-python@v6

          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              python -m pip install flake8 flake8-bugbear flake8-docstrings flake8-pylint flake8-github-annotations pymarkdownlnt yamllint

          - name: Lint with yamllint
            run: |
              yamllint . --format github

          - name: Lint with flake8
            run: |
              # stop the build if there are Python syntax errors or undefined names
              flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --format github
              # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
              flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --format github

          - name: Lint with pymarkdownlnt
            run: |
              pymarkdownlnt scan `git ls-files '*.md' ':!:*TEMPLATE/*md'`

In the final step, ``pymarkdownlnt`` is used to validate all markdown files in the repository. The ``git ls-files '*.md' ':!:*TEMPLATE/*md'`` command is used to get a list of all markdown files in the repository as ``pymarkdownlnt`` doesn't scan recursively and also excludes any markdown files in the ``TEMPLATE`` directory as they aren't conformant due to their template nature for GitHub issues and pull requests. This is then passed to ``pymarkdownlnt`` to validate the files.

Enable GitHub Annotations for pymarkdownlnt
-------------------------------------------

As a final step, it is useful to enable GitHub Annotations for ``pymarkdownlnt``. This will allow GitHub to display the linting errors directly in the pull request. As described in the `GitHub Annotations documentation <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands>`_, this can be done by adding a problem matcher to the GitHub Action and then adding a problem matcher file to the repository.

.. code-block:: yaml
    :caption: Example workflow file :file:`.github/workflows/lint.yml`

    ...
          - name: Add problem matcher
            run: |
              echo "::add-matcher::.github/annotations/pymarkdown-problem-matcher.json"

          - name: Lint with pymarkdownlnt
            run: |
              pymarkdownlnt scan `git ls-files '*.md' ':!:*TEMPLATE/*md'`

The following example shows the contents of the problem matcher file for ``pymarkdownlnt`` and should be saved as ``.github/annotations/pymarkdown-problem-matcher.json`` in the repository. This will allow errors to be displayed in summary of the action run.

.. code-block:: json
    :caption: Example problem matcher file :file:`.github/annotations/pymarkdown-problem-matcher.json`

    {
      "problemMatcher": [
        {
          "owner": "pymarkdown-error",
          "severity": "error",
          "pattern": [
            {
              "regexp": "^([^:]+):(\\d+):(\\d+):\\s+([^:]+:\\s+.+)$",
              "file": 1,
              "line": 2,
              "column": 3,
              "message": 4
            }
          ]
        }
      ]
    }

With this workflow the GitHub Actions will automatically upload to the wiki and validate the markdown files. This will ensure that the wiki is always up to date and that the markdown files are valid. This can also be used to generate documentation from the repository and upload it to the wiki.

.. note::

    The documentation about GitHuub Annotations has been recently updated. The `documentation <https://github.com/actions/toolkit/blob/main/docs/problem-matchers.md>`_ about :github:repo:`actions/toolkit <actions/toolkit>` still contains the format for problem matchers and can be used as a reference.
