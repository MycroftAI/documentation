---
ID: 46709
post_title: 'Cryptographic Backdoors and Why Policy Makers Shouldn&#8217;t Do Math'
author: Joshua Montgomery
post_excerpt: ""
layout: post
permalink: >
  https://mycroft.ai/blog/cryptographic-backdoors-and-why-policy-makers-shouldnt-do-math/
published: true
post_date: 2019-04-23 10:00:33
---
<span style="font-weight: 400;">Generally speaking, I don’t trust policymakers to do math. This isn’t a new thing. In 1894, the Indiana State Legislature <a href="https://en.wikipedia.org/wiki/Indiana_Pi_Bill" target="_blank" rel="noopener noreferrer">attempted to set the value of Pi to 3.2</a></span><span style="font-weight: 400;"> via legislative fiat. Fortunately, there was a professor from Perdue there to set them straight, but it was a close call. National governments haven’t gotten any better at math since.</span>
<h2>Cryptography is math, and it's hard</h2>
<span style="font-weight: 400;">As anyone in the world of computer science knows, cryptography is math. In its simplest form - the <a href="http://www.practicalcryptography.com/ciphers/caesar-cipher/" target="_blank" rel="noopener noreferrer">Caesar Cypher</a></span><span style="font-weight: 400;"> - cleartext can be encoded simply by adding an integer to the letter and shifting the representation by that many steps of the alphabet. Modern cyphers are made far more complex through the use of Modular Arithmetic and Matrix Algebra, but ultimately all encryption is based on math.</span>

<span style="font-weight: 400;">Getting encryption right is extremely difficult, as the Germans found out in World War II. Even though the Germans got the math right (the Enigma Cypher was unbreakable if proper procedures were followed) their cypher system was broken due to poor procedural control on behalf of operators and a <a href="https://en.wikipedia.org/wiki/Key_space_(cryptography)" target="_blank" rel="noopener noreferrer">key space</a></span><span style="font-weight: 400;"> that was small enough to be solved by 1940’s era analog computers. Small mistakes like using the same operator code at the beginning of each message, sending the same information multiple times, and other lazy practices gave allied code breakers the ability to decipher the traffic. General Dwight Eisenhower said after the war that the intelligence gathered by breaking Enigma was decisive to allied victory.</span>
<h2>Weakening security</h2>
<span style="font-weight: 400;">In the present day, two prominent countries - Australia and the United Kingdom - have undertaken efforts to create back-doors into modern cryptographic systems. Bills in both nations seek to undermine data security in favor of national security. It is hard enough to implement a cryptographic system securely, even when all of the math is done right and the system is designed to be secure. It is nearly impossible to secure a system that is intentionally designed to be vulnerable to cryptanalysis.</span>

<span style="font-weight: 400;">Efforts by governments to weaken encryption will inevitably backfire. Governments should have a vested interest in making sure their businesses are able to protect trade secrets and proprietary information. Weakening encryption just makes their industries ripe for attack by sophisticated hackers sponsored by nation states.</span>

<span style="font-weight: 400;">To say these backdoors will prevent or help solve crime is unlikely. Sophisticated criminals are just going to deploy encryption without backdoors anyway, instead of Apple or Google or whoever’s standard encryption. Often, the encryption deployed by those criminals is vulnerable enough to break regardless. Even criminal enterprises like Silk Road or Phantom Secure who tried to take encryption seriously were eventually penetrated and shut down due to poor operational security practices. There is no reason to believe that law enforcement won’t be able to do the same for other criminal enterprises regardless of whether the underlying encryption has back doors or not.</span>

<span style="font-weight: 400;">If government leaders want to regulate how math is done, they should start with their own budgets. Accounting is simply addition and subtraction - something that many governments around the world have mastered. Legislators in the UK and Australia should focus on the basics and leave the crypto to the experts.</span>