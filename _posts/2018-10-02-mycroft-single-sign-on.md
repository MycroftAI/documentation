---
ID: 40833
post_title: 'Mycroft Single Sign-On: Balancing Convenience and Privacy'
author: Chris Veilleux
post_excerpt: ""
layout: post
permalink: >
  http://mycroft.ai/blog/mycroft-single-sign-on/
published: true
post_date: 2018-10-02 18:23:04
---
<h1>Two Anniversaries</h1>
<span style="font-weight: 400;">My wife and I celebrate our 20th wedding anniversary this week. With the date falling in the middle of the week, we decided to take the day off from work. We’ll spend it together, celebrating a major milestone in our marital longevity.</span>

<span style="font-weight: 400;">A major web browser recently marked its tenth anniversary with a software update. Like my wedding anniversary, this should have been a celebrated milestone. Unfortunately, this celebration was hampered by an unpleasant surprise for the browser’s more privacy-focused users. These users would sign in to an account to check their email or calendar, but purposely avoid signing into the browser to protect their privacy. The software update circumvented this user decision by automatically signing them into the browser when they signed into their account. To make matters worse, this change was unannounced! #anniversaryfail</span>

<span style="font-weight: 400;"><a href="https://mycroft.ai/wp-content/uploads/2018/10/MycroftSSO_alt.png"><img class="alignnone wp-image-40834 size-full" src="https://mycroft.ai/wp-content/uploads/2018/10/MycroftSSO_alt.png" alt="Mycroft Single Sign-On balances usability and privacy for our Community" width="1200" height="600" /></a></span>

<span style="font-weight: 400;">User privacy is always a primary concern of Mycroft’s software engineering efforts. This includes the implementation of our user sign-in process. We wanted to share some upcoming enhancements to this process that will improve upon our privacy-focused approach to your personal data.</span>
<h1>What's New</h1>
<span style="font-weight: 400;">The first enhancement will be visible to users that sign in to Mycroft websites. Our web footprint has increased with the introduction of the </span><a href="https://market.mycroft.ai"><span style="font-weight: 400;">Mycroft Marketplace</span></a><span style="font-weight: 400;"> and </span><a href="https://translate.mycroft.ai/"><span style="font-weight: 400;">Mycroft Languages</span></a><span style="font-weight: 400;"> sites. With the addition of these sites, we thought it important to provide users with a seamless log-in experience. To this end, we will be implementing single sign-on (SSO). When implementation is complete, a login to any Mycroft site will be recognized by other Mycroft sites so that you will not need to re-authenticate. </span>

<span style="font-weight: 400;">The second enhancement will not be visible to Mycroft users but is just as important. We will be doing an audit of the user data stored on our databases to ensure that any user-identifiable personal data (email address, name, etc.) is <a href="https://en.wikipedia.org/wiki/Data_at_rest" target="_blank" rel="noopener">encrypted at rest</a>. This will ensure that your personal data will not be compromised, should any unauthorized access to Mycroft’s servers occur.</span>

<span style="font-weight: 400;">As a Software Architect at Mycroft, part of my responsibility is ensuring the security of our users' data. This is a responsibility I take very seriously. One of the reasons I enjoy working at Mycroft AI is our dedication to providing the privacy that our competitors lack. If you want to read a bit more about how we’re doing this, read on.</span>
<h1>The How</h1>
<span style="font-weight: 400;">For those of you interested in the technical details of our SSO implementation, we will be using <a href="https://jwt.io/" target="_blank" rel="noopener">JSON Web Tokens</a> (JWT) rather than the OAuth functionality used today. One of the main benefits of these tokens is that they do not need to be stored on our databases. JWTs contain the same useful information (user ID, token expiration, etc.) and can be easily encoded and decoded on the fly. Even if someone were to intercept one of these tokens, the data encrypted within them cannot be extracted without knowing the value of the secret key used at encryption time.</span>

<span style="font-weight: 400;">To prevent hackers from finding the key, we wrote it on a tiny piece of paper, cut the paper in two and hid the pieces in separate corners of our single room office. Take that, hackers!</span>

<span style="font-weight: 400;">I'm kidding, of course. We've adequately encrypted the key and stored separately from the source code.</span>

<span style="font-weight: 400;">The JWTs are generated, encoded and decoded in the API layer. The API will pass the JWTs to the browser where they will be cached in a way that allows any of our mycroft.ai sites to access them. </span>

<span style="font-weight: 400;">Just as important as a secure login is a secure logout. The logout process must be implemented in a manner that doesn’t leave any authentication breadcrumbs lying around. Once a user logs out of Mycroft’s SSO, the tokens are deleted from the cache, never to be seen again. When the user logs in again, reauthentication will result in a new token. Users do need to log out to delete the token. Otherwise, their token will remain in cache until its predetermined expiration time.</span>

<span style="font-weight: 400;">The code to support SSO is being introduced with the Marketplace. In the coming months, we will extend this functionality to other Mycroft sites. This includes, but is not limited to <a href="https://home.mycroft.ai">https://home.mycroft.ai</a> and </span><a href="https://mycroft.ai">https://mycroft.ai</a><span style="font-weight: 400;">.</span>