---
layout: post
title: "The gap in our ethical infrastructure and know-how for smart cities"
date: 2022-06-07 08:14:00 +0000
categories: ["ethics"]
tags: ["Ethics", "AI"]
permalink: "/2022/06/07/the-gap-in-our-ethical-infrastructure-and-know-how-for-smart-cities/"
wordpress_id: "61"
---

# TLDR

- Where there are laws that cover artificial intelligence (AI), they focus on more obvious, high-profile issues
- Instituting rigorous ethical review might help, but such processes are not widely adopted
- Meanwhile, commonplace embedded computer systems escape scrutiny
- Summary: there is a clear "gap" in our ethical infrastructure. Ideas for resolving that include moving away from proprietary, closed approaches to intellectual property and towards open approaches (including open / free source) that support ethical review. In addition, embedding ethical review into corporate structures may prove to be sufficient but it is not clear how they might be properly policed.

Let me go through these points in a bit more detail …

## AI laws focus on obvious problems

Mastercard recently [announced](https://www.mastercard.com/news/press/2022/may/with-a-smile-or-a-wave-paying-in-store-just-got-personal/) that they are thinking about facial recognition at the checkout. Rather than show your credit card or scan your smartphone, this system would require you simply to look at a camera and then the system would identify you and charge the purchases to your account. There is some [debate](https://theconversation.com/pay-with-a-smile-or-a-wave-why-mastercards-new-face-recognition-payment-system-raises-concerns-183447) about whether such a system poses an ethical risk from the point of view of its *accuracy* or *bias*.

To explain this further, facial recognition *accuracy* refers to the combined problems of failing to identify someone or misidentifying one person as someone else. *Bias* refers to the problem that accuracy varies depending on such things as gender or ethnicity. Since bias causes systems to behave differently to different groups of users, it raises legitimate ethical concerns about the long term effect on those groups.

From the point of view of the recent [EU AI Act](https://artificialintelligenceact.eu/), this probably falls into the category of *high risk* AI. Falling into such a category doesn't cause it to be banned but does expose it to more scrutiny. Risk arises because past AI systems, such as those used to screen CVs, have been found to replicate bias that was in the original data; the basis of screening decisions wasn't transparent and favoured white males over other categories. Similarly, facial recognition has been shown to perform less accurately for coloured than white faces. The negative consequences of bias have been well documented \[insert link\].

While the EU AI Act is clear about the risk associated with known problems (such as, facial recognition) it says little about yet to be uncovered issues. Risk assessment is subtle and should not be left to the imagination of regulators. So what other options are there apart from regulation?

## Ethical review is rare

As an academic, ethical review appears to be a given. We are taught and we teach each other that ethical review is a pillar of good science. It should never be left up to individual scientists to decide whether or not their research crosses an ethical line.

On a recent trip to a developing nation to teach a course to research managers, a striking fact emerged: ethical review processes were only observed rigorously for medical sciences. Indeed, the research managers seemed to accept this as a norm simply because the existing review processes were so bureaucratic and time consuming that to apply them to all research projects would produce a logjam and ordinary scientific endeavour would come to a halt. However, this left a situation where research projects have no form of ethical supervision merely because they are to do with engineering or computer science. Yet we know today that computer science and, particularly, artificial intelligence, has plenty of risks—to privacy, to biased decision making systems, and to the well-being of users.

Perhaps we are fortunate that much research is conducted at universities where ethical review for engineering and computer science is considered necessary. However, increasingly important AI research is coming from private companies. Some of those companies are quite large and some try to include an ethical review process. However, the dominant paradigm for the tech industry is that if it is legal to do a thing, then it is allowed.

## Commonplace systems escape scrutiny

- When elevators were first developed, people didn't trust them
- Elevators - seemingly straightforward but need to be as energy and time efficient as possible
  - Problem is one of being able to predict where demand will be taking into account some obvious factors:
    - time of day
    - what has happened in recent past
    - current state of a set of elevators
  - Modelling humans involved is also an important factor (e.g., walking speeds, group behaviour, etc)
- Exactly how such systems work and what data they obtain and store is kept secret by the manufacturer
- The decision making of elevators and many other everyday systems continues to evolve and develop without transparency, oversight, or much consideration.
- While elevators are the safest known form of transport, ethical risks do arise for commonplace systems

# Ethics-In-Practice

The discussion above draws attention to the idea that despite the growing concern with Ethics & AI, serious and consistent ethical review (compared to medical ethics) is probably missing in most corporations working with AI. Observations made in Pakistan seem likely to apply to companies world-wide. Indeed, a recent study of the Energy Sector in the UK has shown this to be the case \[SOME RESULTS FROM PAPER HERE\]. The other area of questioning in the discussion relates to what might happen if serious ethical review was embedded in corporations. What form of regulation would police the decision-making that might be undertaken in the context of any and all levels of an [AI lifecycle](https://www.infosys.com/content/dam/infosys-web/en/techcompass/ai-life-cycle-tools.html)? The new [European AI Act](https://artificialintelligenceact.eu/) is referred to along with the concern that this Act, intended to underpin future AI regulation in Europe, leaves a lot of issues uncovered. This is one of the critiques of the Act [published recently](https://www.adalovelaceinstitute.org/report/regulating-ai-in-europe/) by the Ada Lovelace Institute who question if such a "holistic instrument" for regulating AI systems is the "right way to go" as opposed to government regulation of sectors, e.g. the medical sector already mentioned.

The plenitude of complicated gaps here and, more importantly, what to do about them in any kind of applied way is difficult to grasp. Philosophical and intellectual debate in this context comes directly into conflict not only with commercial and state interests, but also falls into the difficulty of conducting effective applied research across radically different disciplines and fields, not to mention the challenges of intercultural communication.  It is widely assumed that siloed approaches to understanding and resolving the gaps cannot be successful. But there is little indication of how to effectively conduct the fundamental research being called for (e.g. by [Horizon Europe](https://tinyurl.com/26vacc2l)) that integrates the arts and humanities with computing science and engineering.

On 18 May 2022, C-DaRE Invites panel framing the arts & humanities and computer science & engineering collaboration on technology and ethics

- Ethics-in-Practice as a term. Ethical know-how (Varela)
  - [Life of Data Project](https://lifeofdata.org/site/patterns-in-practice/about/) as an example
