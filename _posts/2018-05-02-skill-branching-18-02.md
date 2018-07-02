---
ID: 37489
post_title: 'Skill Branching &#8211; What you need to know as a Community Developer'
author: Kathy Reid
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/skill-branching-18-02/
published: true
post_date: 2018-05-02 11:30:06
---
Are you a Community Developer? Have you previously written Skills for the Mycroft ecosystem? Are you considering writing Skills? Then you should read this blog post to understand a fundamental change to the publication of Skills, and what you need to do to ensure your Skills are updated on to the new 18.02 branch.
<h2>What changes are we introducing?</h2>
The April 27th <code>mycroft-core</code> release (18.2.5b) changed the Mycroft Skills Management (<code>msm</code>) system to pull from a new branch of the <a href="https://github.com/MycroftAI/mycroft-skills"><code>mycroft-skills</code> GitHub repository</a>. Skills are now associated with a branch that corresponds to the major version of <code>mycroft-core</code> under which they were created and tested.  The MSM system will only install Skills from the Skill branch corresponding to the version of <code>mycroft-core</code> -- i.e. ‘18.02’ as of today. A new Pull Request is required to submit an existing Skill in a new branch. When Mycroft moves to version 18.08b in August 2018, Pull Requests will be required to move Skills from the ‘18.02’ branch to an ‘18.08’ branch of the <code>mycroft-skills</code> repo.

This change also introduced <strong>version locking</strong>.  This means <a href="https://mycroft.ai/documentation/msm/">Mycroft Skills Manager (MSM)</a> will not automatically update to HEAD of a Skill repo, instead the Skill will be locked to the revision submitted to the <code>mycroft-skills</code> repository, then reviewed by the Skills Team and accepted. To publish a new version of a Skill the author needs to generate a new Pull Request, verifying that the Skill still passes all tests and standards.
<h2>Why have we made this change?</h2>
Previously, all Skills were merged to the master branch of the <code>mycroft-skills</code> GitHub repository. There were both advantages and disadvantages to this approach. On the one hand, Community Developers only needed to concern themselves with one branch. On the other hand, Mycroft users had no way to determine how current a Skill was or whether it had been tested against a recent code base. Moreover, without branching, <code>mycroft-core</code> needs to be mindful of backward compatibility. This makes it nearly impossible to make foundational changes to Mycroft as we evolve the system.

For example, Mycroft has been moving towards Python 3 for some time and will be switching in the near future. Many Skills which were written in the pre-18.02 world did not consider Python 3 compatibility and may stop functioning. Similar changes will certainly occur in the future. This mechanism will provide certainty for users that the Skill they install will function, and certainty to Community Skill Developers that <code>mycroft-core</code> will not change out from underneath them unexpectedly.
<h2>What new requirements does this impose for Skill authors?</h2>
We are taking this opportunity to introduce two new Skill requirements.  Before a Skill will be accepted into the mycroft-skill repository, it must meet these requirements.
<ul>
 	<li><strong>Python 3 compatibility:</strong> This clean cut is a great opportunity for developers to make the switch with their Skills.  For most, this will be quick and painless.</li>
 	<li><strong>Automatic testing:</strong> A new <a href="https://mycroft.ai/documentation/skills/automatic-testing/">automated testing framework</a> has been built over the last few months in conjunction with several community members.  This system allows a Community Skill Developer to validate the operation of their own Skill during development.  When a Skill is submitted to the repository, the same system will validate that the Skill doesn’t interfere with core operation of default Skills.</li>
</ul>
<h2>Skill Life Cycle Examples</h2>
<h3>Submitting a new Skill to the <code>mycroft-skills</code> repository</h3>
<em>Example:</em> Sarah has a brand new Skill to submit to <code>mycroft-skills</code>, <code>sarah-awesome-skill</code>. Sarah completes the automatic testing of the Skill and creates a PR on the 18.02 Skill. The Skill Acceptance Process is used to validate that the Skill is working, and the Skill is merged into the 18.02 branch of the <code>mycroft-skills</code> repo by the Skills Team.

Now that the Skill is in the 18.02 branch, it can be automatically installed using voice commands - such as <code>"install sarah awesome”</code>, or using msm - <code>“msm install sarah-awesome-skill”</code>.

In August 2018, Sarah will need to re-test the Skill against the 18.08 branch of <code>mycroft-core</code>, and raise another Pull Request for the Skill to be merged into the 18.02 branch.
<h3>Updating an existing Skill that’s in the master branch of the <code>mycroft-skills</code> repository</h3>
<em>Example:</em> Brian has several Skills in the master branch of the <code>mycroft-skills</code> repo. He decides which ones he wishes to actively maintain, and using <a href="https://mycroft.ai/documentation/skills/automatic-testing/">Automatic Skill Testing</a>, he ensures that they work with the 18.02 branch of mycroft-core.

For each Skill he wishes to maintain, he raises a Pull Request for the Skill to be merged into the 18.02 branch of the mycroft-skills repo. The Skill Acceptance Process is used by the Skills Team to validate that the Skills are working, and the Skills are merged into the 18.02 branch by the Skills Team.
<h4>What happens to Skills that are not maintained?</h4>
A Skill that Brian does not wish to maintain will remain in the original <code>mycroft-skills</code> branch to which it was submitted -- that is, they are never deleted.  However, they are also not migrated automatically when a new major version releases. When users migrate their Mycroft to the new version they will not be able to install the abandoned Skill with either voice commands or msm commands (although advanced users can manually clone the repo, of course).

Useful but abandoned Skills can be adopted by a new maintainer. They can fork the original repo and resubmit the now-maintained Skill to the latest Skill branch.
<h3>Updating an existing Skill that’s in the 18.02 branch of the <code>mycroft-skills</code> repository</h3>
<em>Example:</em> Sergio has already submitted his Skill, <code>sergio-wonderful-skill</code>, to the 18.02 branch of <code>mycroft-skills</code>, and it has passed the Skills Acceptance Process and been merged into the 18.02 branch.

He now wishes to add some features to <code>sergio-wonderful-skill</code>. He simply raises a PR against the <code>mycroft-skills</code> repo 18.02 branch, and then the PR is reviewed.
<h2>Where can you go to get assistance?</h2>
If this all sounds a little confusing, we totally understand.

There’s a bit of a learning curve involved in becoming a Mycroft Community Developer, and we’re here to help. You can get assistance in our <a href="https://chat.mycroft.ai/community/channels/dev">Mattermost Chat - the Dev channel is going to be the most helpful</a>, or on our <a href="https://community.mycroft.ai/">Forum</a>.