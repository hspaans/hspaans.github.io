.. post:: 2026-04-25 13:37:00
    :tags: GitHub, GitHub Copilot, GitHub CLI, skills
    :category: Uncategorized

Start Creating Skills for Copilot
=================================

GitHub Copilot is an AI-powered code completion tool that helps developers write code faster and more efficiently. With the introduction of skills, developers can now create custom functionalities that enhance Copilot's capabilities. In this blog post, we will explore how to start creating skills for GitHub Copilot and how to maintain them using the GitHub CLI from a central repository.

Creating Skills for Copilot
---------------------------

To create a skill for GitHub Copilot, you can follow these steps:

1. **Set Up Your Environment**: Ensure you have the GitHub CLI installed and configured on your machine. You can download it from the [GitHub CLI website](https://cli.github.com/).
2. **Create a Repository**: Create a new repository on GitHub where you will store your Copilot skills. This repository will serve as the central location for all your skills.
3. **Define Your Skill**: Decide on the functionality you want to add to Copilot. This could be anything from code snippets, templates, or even integrations with other tools.
4. **Write Your Skill**: Use your preferred programming language to write the code for your skill. Make sure to follow the guidelines provided by GitHub for creating skills, which can be found in the [GitHub Copilot documentation](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills).
5. **Test Your Skill**: Before deploying your skill, test it locally to ensure it works as expected. You can use the GitHub CLI to run your skill and check for any issues.
6. **Deploy Your Skill**: Once you are satisfied with your skill, you can deploy it to your GitHub repository. Use the GitHub CLI to push your code and make it available for use in Copilot.

Maintaining Your Skills
-----------------------

Maintaining your skills is crucial to ensure they continue to function correctly and provide value to users

Starting with the SKILL.md format
---------------------------------

.. code-block:: markdown
    :caption: Example of a SKILL.md file format

    ---
    name: skill-name
    description: Brief description of the skill
    ---

    # Skill Title

    Guidelines and instructions...

Installation
------------

From version 2.90.0 of the [GitHub CLI](https://github.com/cli/cli), you can install skills directly from this repository using the following command:

.. code-block:: bash
    :caption: Command to install a skill using GitHub CLI

    gh skill install <owner>/<repo> <skill-name>

An example to install a Python skill with GitHub CLI command:



```bash
gh skill install hspaans/skills python
```