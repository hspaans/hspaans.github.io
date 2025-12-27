.. post:: Oct 30, 2025 08:00:00
   :tags: GitHub, technical debt
   :category: DevOps

Start using GitHub Dependabot
=============================

`GitHub`_ bought a service called :github:org:`Dependabot <dependabot>` a while back and is now integrating this service as a GitHub Application into the ecosystem. This allows GitHub users to automatically do dependency management and get alerted when a security-related update has been found. For a while this service was in beta but it is now enabled for all public repositories and can be enabled for private repositories as well.

Getting started
---------------

Let's start simple and create a file ``.github/dependabot.yml`` in the repository with the content below. This will tell Dependabot to scan all your GitHub workflows daily for GitHub Actions that are defined and have a newer release available. It will also create a pull request that can be merged when approved.

.. code-block:: yaml
    :caption: Example file :file:`.github/dependabot.yml` to scan GitHub Actions

    ---
    version: 2
    updates:
      - package-ecosystem: github-actions
        directory: /
        schedule:
          interval: daily

.. note::

    Dependabot will only use ``.github/dependabot.yml`` found in the **master** branch of the repository.

In the second example, we're telling Dependabot to scan for a Dockerfile in the root of the repository with the ``directory`` option. We also tell Dependabot to scan for a Dockerfile in the ``.devcontainer`` directory as well in the second section. This is a common practice for repositories with support for Docker and development containers in `VSCode`_ or `GitHub CodeSpaces`_.

.. code-block:: yaml
    :caption: Example file :file:`.github/dependabot.yml` to scan Dockerfiles

    ---
    version: 2
    updates:
      - package-ecosystem: docker
        directory:
          - /
          - /.devcontainer
        schedule:
          interval: daily

Using different branches
------------------------

The master branch is scanned by default. You can also specify a branch to scan by adding the option ``target_branch`` per package ecosystem. The example below will let Dependabot scan and created pull requests for both the **master** and **v1** branches.

.. code-block:: yaml
    :caption: Example file :file:`.github/dependabot.yml` to scan different branches

    ---
    version: 2
    updates:
      - package-ecosystem: github-actions
        directory: /
        schedule:
          interval: daily
        target-branch: master

      - package-ecosystem: github-actions
        directory: /
        schedule:
          interval: daily
        target-branch: v1


Supported package ecosystem
---------------------------

Dependabot supports multiple package ecosystems. Besides ``github-actions`` and ``docker``, there is also support for ``Python``, ``PHP``, and ``Java``. A complete and actual list of `supported ecosystems`_ can be found in the `Dependabot documentation`_.

.. code-block:: yaml
    :caption: Example file :file:`.github/dependabot.yml` to scan Python dependencies

    ---
    version: 2
    updates:
      - package-ecosystem: github-actions
        directory: /
        schedule:
          interval: daily

      - package-ecosystem: pip
        directory: /
        schedule:
          interval: daily

      - package-ecosystem: devcontainer
        directory: /
        schedule:
          interval: daily

The example above will also scan for dependencies defined in a `devcontainer.json` file and create pull requests when updates are found for the used `devcontainer features <//containers.dev/features>`_.

The number of pull requests
---------------------------

By default, Dependabot will create a pull request for each update found and will limit this to 5 open pull requests. This can be changed by adding the option ``open-pull-requests-limit`` and setting a different value.

.. code-block:: yaml
    :caption: Example file :file:`.github/dependabot.yml` to set the number of open pull requests

    ---
    version: 2
    updates:
      - package-ecosystem: github-actions
        directory: /
        schedule:
          interval: daily

      - package-ecosystem: pip
        directory: /
        schedule:
          interval: daily
        open-pull-requests-limit: 10

.. warning::

    Dependabot will rebase open pull requests on the target branch when the target branch is updated. This will also trigger workflows that are defined in the updated branch and will consume time from your GitHub Actions budget.

Scheduling scan interval
------------------------

In all examples, we scanned the repository **daily** at a random time, but it can also be specified by setting a time and also a timezone. It can also be set to a **weekly** schedule that by default runs on a Monday, but it can be set to the day of the week. And finally, the schedule can also be set to run on a specific day of the month with a **monthly** schedule and if no day is specified, then it will run on the first day of the month.

.. code-block:: yaml
    :caption: Example file :file:`.github/dependabot.yml` to set different scan intervals

    ---
    version: 2
    updates:
      - package-ecosystem: github-actions
        directory: /
        schedule:
          interval: daily
          time: "09:00"
          timezone: "Europe/Amsterdam"

      - package-ecosystem: pip
        directory: /
        schedule:
          interval: monthly
          day: 3

      - package-ecosystem: docker
        directory: /
        schedule:
          interval: weekly
          day: friday

.. warning::

    As with the ``open-pull-requests-limit`` option, the schedule interval will influence the time consumed from your GitHub Actions budget. Picking the right interval for Dependabot to scan your dependencies is essential and for a lot of repositories, the **monthly** interval is the most efficient.

Conclusions about Dependabot
----------------------------

Dependabot is a great tool to get started with and is a great way to get alerted when a security-related update has been found. It is also a great way to get your dependencies up to date regularly. It does require a little bit of planning to come to a sane interval to scan repositories. It can both burn your GitHub Actions budget and be a burden on developers if too many pull requests are opened.

In the end, Dependabot helps developers to keep their dependencies up to date without much effort. Not all settings were covered in this post, but you can find more information on the `Dependabot documentation`_.

.. _Dependabot documentation: https://docs.github.com/en/code-security/dependabot
.. _GitHub: https://github.com/
.. _GitHub CodeSpaces: https://github.com/features/codespaces
.. _Semantic Versioning : https://semver.org/
.. _VSCode: https://code.visualstudio.com/
.. _supported ecosystems: https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference#package-ecosystem-
