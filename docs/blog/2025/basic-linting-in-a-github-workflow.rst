.. post:: 2025-08-22 08:00
    :tags: GitHub, Linting, CI/CD
    :category: Uncategorized

************************************
Basic linting with a GitHub workflow
************************************

The easiest way to get started with linting in a GitHub workflow is to use a pre-built action from the `GitHub Marketplace <https://github.com/marketplace>`_. These actions can be easily integrated into your workflow file and configured to run the linter of your choice. Alternatively, you can set up your own linting process using command-line tools and scripts. This way, you have more control over the linting process and can customize it to fit your specific needs.

Setting up the workflow
#######################

To get started, you'll need to create a `GitHub Actions workflow file <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>`_ in your repository. This file will define the steps to run the linters on your codebase with Python as the runtime environment for those linters. Others can be used as well, but Python has a wide range of linters available for different file types.

In the workflow file below that needs to be placed in the `.github/workflows/` directory of your repository. It will trigger on pushes and pull requests to the `master` branch. The workflow will check out the code, set up Python, install the necessary dependencies, and run the linters for yaml, markdown, and restructuredtext files as these are the file types used in this post.

.. code-block:: yaml
  :caption: Workflow file `.github/workflows/lint.yml` for linting

    ---
    name: Linting

    on:
      push:
      pull_request:
        branches:
          - master

    jobs:
      lint:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout code
            uses: actions/checkout@v5

          - name: Set up Python
            uses: actions/setup-python@v5
            with:
              python-version: '3'

          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              python -m pip install yamllint pymarkdownlnt rstcheck

Now the workflow file is in place it can run but it needs to be configured to actually do something. This is where the individual linters come into play and need to be added to the workflow as extra steps.

Validate yaml files
###################

The easiest linter is :github:repo:`yamllint <adrienverge/yamllint>` that validates YAML files and can be used to validate the GitHub workflow files themselves. This is useful as it can catch syntax errors and other issues before they cause problems in the workflow. First we will run the yamllint command on our own local machine to see what issues it finds so we know what to expect when we run it in the workflow.

.. code-block:: console
    :caption: Linting yaml files on the commandline

    $ yamllint .
    ./.github/workflows/pages-deploy.yml
      3:1       warning  truthy value should be one of [false, true]  (truthy)
      38:81     error    line too long (84 > 80 characters)  (line-length)
      53:81     error    line too long (180 > 80 characters)  (line-length)
      75:38     error    no new line character at the end of file  (new-line-at-end-of-file)

This output seems to be fine, but GitHub can't interpret it. To make it more useful we can use the `--format github` option that will format the output in a way that GitHub can understand and use to annotate the workflow run with the issues found.

.. code-block:: console
    :caption: Linting yaml files on the commandline

    $ yamllint --format github .
    ::group::./.github/workflows/pages-deploy.yml
    ::warning file=./.github/workflows/pages-deploy.yml,line=3,col=1::3:1 [truthy] truthy value should be one of [false, true]
    ::error file=./.github/workflows/pages-deploy.yml,line=38,col=81::38:81 [line-length] line too long (84 > 80 characters)
    ::error file=./.github/workflows/pages-deploy.yml,line=53,col=81::53:81 [line-length] line too long (180 > 80 characters)
    ::error file=./.github/workflows/pages-deploy.yml,line=75,col=38::75:38 [new-line-at-end-of-file] no new line character at the end of file
    ::endgroup::

Now only make sure to run the command on all relevant files that are part of the repository. In this case we want to run it on all `.yml` and `.yaml` files that are tracked by git with selecting them with `git ls-files`.

.. code-block:: console
    :caption: Linting yaml files tracked by git on the commandline

    $ yamllint --format github `git ls-files '*.yml' '*.yaml'`
    ::group::./.github/workflows/pages-deploy.yml
    ::warning file=./.github/workflows/pages-deploy.yml,line=3,col=1::3:1 [truthy] truthy value should be one of [false, true]
    ::error file=./.github/workflows/pages-deploy.yml,line=38,col=81::38:81 [line-length] line too long (84 > 80 characters)
    ::error file=./.github/workflows/pages-deploy.yml,line=53,col=81::53:81 [line-length] line too long (180 > 80 characters)
    ::error file=./.github/workflows/pages-deploy.yml,line=75,col=38::75:38 [new-line-at-end-of-file] no new line character at the end of file
    ::endgroup::

The command we want to run in the workflow is now complete and can be added as a step in the workflow file as shown below.

.. code-block:: yaml
    :caption: Adding a step to the workflow file `.github/workflows/lint.yml`

          - name: Lint with yamllint
            run: yamllint --format github `git ls-files '*.yml' '*.yaml'`

The final step is to make sure that the `.yamllint.yml` configuration file is included in the repository so that the workflow can use it as needed to not flag workflow files as having issues. The configuration file below is a good starting point and can be adjusted as needed.

.. code-block:: yaml
    :caption: Use `.yamllint.yml` to configure yamllint

    ---
    extends: default

    rules:
      braces:
        max-spaces-inside: 1
        level: error
      brackets:
        max-spaces-inside: 1
        level: error
      line-length: disable
      truthy: disable

Validate Markdown files
#######################

The second linter is :github:repo:`pymarkdownlnt <jackdewinter/pymarkdown>` that validates Markdown files. This linter is useful as it can catch a wide range of issues in Markdown files, including formatting issues, broken links, and other common problems. As with yamllint we will first run the command on our own local machine to see what issues it finds. Here we will directly go for all files tracked by git with the `git ls-files` command.

.. code-block:: console
    :caption: Linting Markdown files on the commandline

    $ pymarkdownlnt scan `git ls-files '*.md' ':!:*TEMPLATE/*md'`
    README.md:33:3: MD047: Each file should end with a single newline character. (single-trailing-newline)

.. note::

  The example command above shows how to run `pymarkdownlnt` on all Markdown files in the repository, excluding those in the `TEMPLATE` directory as those are most of the time not compliant to make them work in GitHub repositories.

As `pymarkdownlnt` doesn't have a built-in GitHub format option we need to create our own problem matcher that can interpret the output of the linter and convert it into a format that GitHub can understand. The example below shows a simple problem matcher that can be used for this purpose. This file needs to be placed in the `.github/annotations/` directory of your repository.

.. code-block:: json
    :caption: Regular expression for problem matcher in file `.github/annotations/pymarkdown-problem-matcher.json`

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

Now we need to add the problem matcher to our workflow file before the linting step for `pymarkdownlnt` and this will translate the output of the linter into a format that GitHub can understand as annotations and show in the web interface.

.. code-block:: yaml
    :caption: Adding a step to the workflow file `.github/workflows/lint.yml`

      - name: Add problem matcher
        run: echo "::add-matcher::.github/annotations/pymarkdown-problem-matcher.json"

      - name: Lint with pymarkdownlnt
        run: pymarkdownlnt scan `git ls-files '*.md' ':!:*TEMPLATE/*md'`

Similar to with yamllint we also need to make sure that the configuration file for `pymarkdownlnt` is included in the repository. The configuration file below is a good starting point and can be adjusted as needed. The example below disables the MD013 rule that checks for line length as this can be annoying when writing Markdown files.

.. code-block:: yaml
    :caption: Use `.pymarkdown.yml` to configure pymarkdownlint

    ---
    plugins:
      md013:
        enabled: false

Conclusion if linting is useful
###############################

For some linting is crucial and for others it is just nice to have. The better question is not whether to lint, but how to lint effectively as the two linters described here are just the beginning. And we may even argue about the best practices for configuring and using these tools to maximize their effectiveness that a using them directly in the workflow is the best approach as it affects the repository, but others like :github:repo:`flake8 <PyCQA/flake8>` or :github:repo:`black <psf/black>` can be used in a local development environment as well as part of :github:repo:`tox <tox-dev/tox>` or :github:repo:`pre-commit <pre-commit/pre-commit>`.
