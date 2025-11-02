.. post:: Nov 1, 2025 08:00:00
   :tags: GitHub, workflow, schedule
   :category: DevOps, GitOps

Create GitHub issues on a schedule
==================================

In post :ref:`Custom GitHub templates for issues`, the first step was made to automate the workflow more by defining issue templates on the organizational level and assigning labels when creating a new issue. A human still needs to create the issue manually while some issues must be created on a schedule to deploy new certificates or run an Ansible playbook to patch servers for example.

Like in post :ref:`Start using GitHub Dependabot` where merge requests were automatically created for updated dependencies, issues can also be created on a schedule. Let's create a workflow that creates an issue every month for recurring maintenance that must be done.

GitHub Actions on a schedule
----------------------------

GitHub Actions supports different triggers and one of its triggers is called ``schedule`` which allows starting a workflow at a specific time. In the example below we start the workflow every first day of the month at 8 AM sharp. The syntax to specify the time follows the implementation of :wikipedia:`cron <Cron>` in :wikipedia:`Linux`.

.. code-block:: yaml
    :caption: Example workflow file :file:`.github/workflows/patch-reminder.yml`

    ---
    name: Create patch issue

    on:
      schedule:
        - cron: "0 8 1 * *"

    permissions:
      contents: read
      issues: write

    jobs:
      create-issue:
        name: Create an issue
        runs-on: ubuntu-latest
        steps:
          - name: Checkout Code
            uses: actions/checkout@v5

          - name: Create an issue
            uses: JasonEtco/create-an-issue@v2.9.1
            env:
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
            with:
              update_existing: false
              filename: .github/patch-issue-template.md

The job to create an issue relies on a third-party action called :github:repo:`JasonEtco/create-an-issue` that needs write permissions to create or update issues. This GitHub Action can update existing issues, but also create new ones. In our example pipeline we create a new issue every month and are using file :file:`.github/patch-issue-template.md` as a template for this.

.. warning::

    The :wikipedia:`cron <Cron>` implementation used by :github:org:`GitHub Actions<actions>` doesn't support extensions like ``@daily`` or ``@weekly`` for example.

Template autonomy for create-an-issue
-------------------------------------

GitHub Action :github:repo:`JasonEtco/create-an-issue` takes a template file and supports some basic Jinja2 filters that are applied when an issue is created. This way a unique issue is generated every month and supports similar keys as in post :ref:`Custom GitHub templates for issues` to directly assign the issue and to apply labels.

.. code-block:: markdown
    :caption: Example template :file:`.github/patch-issue-template.md`

    ---
    title: Monthly maintenance for {{ date | date('MMMM YYYY') }}
    assignees: user01
    labels: infrastructure
    ---
    Monthly maintenance cycle for {{ date | date('MMMM YYYY') }}

    Actions:
    - [ ]  Install all patches
    - [ ]  Reboot all servers
    - [ ]  Deploy Ansible site.yml to validate the state
    - [ ]  Update all certificates that will expire

With this, a new issue will be created on the first day of every month, assigned to ``user01``, and will have label ``infrastructure``. The issue can be used to create new related issues as it has a checklist or to just mark tasks as done.
