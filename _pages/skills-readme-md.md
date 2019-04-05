---
ID: 46174
post_title: Skills README.md
author: Kris Gesling
post_excerpt: ""
layout: page
permalink: >
  http://mycroft.ai/documentation/skills/skills-readme-md/
published: true
post_date: 2019-04-04 20:27:47
---
# Skills README.md

The README.md file in each Skill repository is used to provide an overview of the Skill and its functionality. This file is used by the [Skills Marketplace](https://market.mycroft.ai/) to display the appropriate information including the [Card view](https://market.mycroft.ai/skills) and [Details view](https://market.mycroft.ai/skill/mycroft-weather).

When creating your skill, the [Mycroft Skills Kit](https://mycroft.ai/documentation/skills/msk/) will automatically generate your first README.md for you. Alternatively you can use the [Skills Meta Editor](https://mycroft.ai/skill-meta-editor) to generate a compatible README.md and ensure all the relevant information is included.

## Top tips for a great README  
- The title should not include the word Skill  
- There is limited space on the Skill Card in the Marketplace. Long titles, on-line descriptions and intent examples will be truncated (cut off). Try to keep these clear and concise.  
- Note: the one-line description is the text between the Skill title and the "About" section.  
- Only the first Example Intent will be shown on the Skills Card in the Marketplace. This should be short and make sense as a single phrase.  
- The primary category, being the category in bold, is where the Skill will be displayed in the Marketplace by default.

## Suggesting changes to an existing README  
A Github account is required, please register for an account now if needed. Then head to the Skills Github repository (repo) to get started.

### Edit and make a pull request (PR)  
This is the most direct and simplest method for Skill Authors if you have a clear idea of what changes need to be made.

README.md files are writting using the Markdown syntax, which is a way to style text on the web. If you aren't familiar with Markdown formatting, Github has an excellent [3 minute guide](https://guides.github.com/features/mastering-markdown/) to get you started.

#### How to  
**1. Edit the file**  
- Select the README.md file  
- Then the pencil icon to edit the file

**2. Review your changes using the [Skills Meta Editor](https://mycroft.ai/skill-meta-editor)**  
- Github provides the preview tab for quickly checking your formatting, however when shown in the Mycroft Marketplace, there are multiple ways a Skill may be shown.  
- Copy and paste the file contents into the README.md tab of the [Meta Editor](https://mycroft.ai/skill-meta-editor) to see a preview of the Card and Detail views.  
- Please be aware that after importing text into this tool, it may be modified to fit the standard features of a Mycroft Skills README.

**3. Propose the changes**  
- At the bottom of the edit page on Github will be a short "Propose file change form". Submitting this will automatically create a [fork](https://guides.github.com/activities/forking/) of the repo in your account as well as a [pull request](https://guides.github.com/activities/forking/#making-a-pull-request) to the main project proposing the changes.  
- This provides the Skill Author with a list of any proposed changes as well as the message you include in this form.  
- Please try to be clear and concise in your message as to what has been changed and why. Be aware that we have developers from across the world and English may not be their first language.

### Create a new 'issue'  
This is the best option if you are unsure about what the final text should look like.

#### How to  
**1. Create a 'new issue'**  
- From the Skills Github repo, select the 'Issues' tab  
- Then the green 'New issue' button on the right.

**2. Write a clear and concise issue message**  
- The title of an issue should be a very brief overview of the changes you are suggesting. If the changes are limited to a specific section or for a particular reason say that here. An example might be "Suggested changes to description for readability".  
- In the main comment area, please detail the changes you are suggesting, and try to be descriptive about which section you are referring to. Instead of "there's a typo in skill", we might write "In the first intent example there is a typo, sklil should be skill."  
- If you are proposing multiple changes consider grouping them under headings.  
- If you are proposing a block of text, consider using the 'quote' formatting to highlight this.

**3. Preview and Submit**  
- Just underneath the title field is a 'Preview' tab. This lets you check the formatting of your message.  
- Once you're happy hit submit.