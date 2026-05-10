.. post:: 2026-05-10 08:00:00
    :tags: Wikipedia, Grokipedia, summary-as-code, documentation-as-code, AI, Copilot, Sphinx
    :category: Experiments

Experimenting with Grokipedia
=============================

In the world of technology and software development, staying updated with the latest tools and trends is crucial. One of the emerging trends in recent years is the use of AI-powered tools to enhance productivity and streamline workflows. `Grokipedia <https://grokipedia.com>`_ is one such tool that has caught my attention, and I decided to experiment with it to see how it can benefit my work.

`Wikipedia <https://www.wikipedia.org>`_ is an incredible resource for information, but it is all human generated content. Grokipedia, on the other hand, is an AI-powered tool that can generate summaries and documentation based on code. It uses natural language processing and machine learning to understand the code and create meaningful summaries that can be used for documentation purposes.

This distinction between Wikipedia and Grokipedia is important in a world where new topics in technology are emerging rapidly and keep on developing. Grokipedia can help bridge the gap as it can quickly generate summaries and documentation for new technologies, making it easier for developers to understand and adopt them.

Generating the prompt
---------------------

As we already had a working codebase, we could use it to generate the prompt to migrate links from Wikipedia to Grokipedia and see if we can make a simple switch over from human to AI generated summaries about certain topics. The prompt was generated using the following steps:

1. Identify the links in the documentation that point to Wikipedia.
2. Create a mapping of Wikipedia links to their corresponding Grokipedia links.
3. Use the mapping to replace Wikipedia links with Grokipedia links in the documentation.

This resulted in an GitHub issue with the following content:

.. code-block:: text

    **The experiment**
    Can Grokipedia be used as an alternative to Wikipedia to see if we can make a simple switch over from human to AI generated summaries about certain topics.

    **Making changes**
    Steps:
    1. Add grokipedia url in extlinks configuration
    2. Validate all links with linkscheck option in Sphinx
    3. For any broken links the following options to solve it:
      a. Find a keyword that possibly leads to the same subject on both grokipedia and wikipedia and use the grokipedia option
      b. If a common keyword cannot be found the preference is to use the grokipedia keyword
      c. If no alternative can be found on grokipedia the wikipedia version must be used

After the issue was created, we proceeded to make the necessary changes in the documentation and validate the links using Sphinx's linkcheck option. This allowed us to identify any broken links and ensure that all references were correctly updated to point to Grokipedia where applicable.

.. code-block:: shell

    sphinx-build -b linkcheck . _build/linkcheck

Only a few links were found to not be migrated to Grokipedia, and for most we were able to find a suitable alternative on Grokipedia that led to the same subject on both platforms. One exception was the SBOM topic, that needed some manual work to find the right keyword on Grokipedia, but in the end we were able to successfully migrate all links from Wikipedia to Grokipedia.

Which changes were made
-----------------------

The changes made were primarily in the documentation, where we updated the links to point to Grokipedia instead of Wikipedia. This involved modifying the extlinks configuration in Sphinx to include the Grokipedia URL and then updating the documentation files to replace the Wikipedia links with their corresponding Grokipedia links.

Also `conf.py` was updated to include the new extlink for Grokipedia and to allow redirects for the linkcheck option to handle the new links correctly.

.. code-block:: python
    
    # Example of the extlinks configuration in Sphinx
    if 'sphinx.ext.extlinks' in extensions:
    extlinks = {
        'gh': ('https://github.com/%s', '%s'),
        'gp': ('https://grokipedia.com/page/%s', '%s'),
        'wiki': ('https://en.wikipedia.org/wiki/%s', '%s'),
        'yt': ('https://www.youtube.com/watch?v=%s', '%s'),
    }

    # Example of allowed redirects in conf.py to handle link checking
    linkcheck_allowed_redirects = {
        r'https://docs.github.com/[a-z]{2}/.*': r'https://docs.github.com/[a-z]{2}/.*',
        r'https://grokipedia.com/page/.*': r'https://grokipedia.com/page/.*',
        r'https://[a-z]{2}.wikipedia.org/wiki/.*': r'https://[a-z]{2}.wikipedia.org/wiki/.*',
        r'https://youtu.be/.*': r'https://www.youtube.com/watch\?v=.*',
    }

Conclusion about switching to Grokipedia
----------------------------------------

Overall, it seems that Grokipedia has the potential to be a valuable resource for developers looking for AI-generated summaries and documentation. While it may not completely replace Wikipedia, it can certainly complement it by providing quick and concise summaries that can help developers understand new technologies and concepts more efficiently. The experiment showed that it is possible to switch over from human-generated summaries to AI-generated summaries with minimal effort, and it could be a useful tool for keeping documentation up-to-date in a rapidly evolving tech landscape.

Time will tell if and how Grokipedia will evolve and whether it will become a widely adopted resource in the developer community, but it is definitely an exciting development to keep an eye on. For now, switching between Wikipedia and Grokipedia seems to be a viable option for referencing information in documentation, and it will be interesting to see how this experiment unfolds in the future. And with tools `Copilot <https://github.com/copilot>`_ and other AI assistants becoming more prevalent, the integration of AI-generated content in documentation is likely to become more common, making tools like Grokipedia even more relevant in the coming years.