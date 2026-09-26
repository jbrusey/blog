---
layout: post
title: "How to do sustainable AI adoption"
date: 2026-09-25 19:37:00 +0000
permalink: "/2026/09/25/sustainable-ai-adoption/"
---

### Adoption is not the same as experimentation 

What does *AI Adoption* mean to you? 
For many organisations, it's about paying an AI supplier the licence fee and hoping it changes work practice. 
It is relatively easy to show that AI can do something useful.
A much harder problem is to turn that demonstration into a capability that produces lasting benefit. 
In other words, it is not simply a question of whether or not AI can do a particular thing, rather: does it work reliably, does it create measurable value, and can the organisation sustain it?
Our AI Adoption Lab at Coventry University is built on the idea that sustainability comes first. 

An example is the Student Experience project.
The Student Experience team wanted to be able to identify students who might need support before they fail or drop out.
While they experimented with a variety of solutions, these solutions the team could not readily maintain or develop themselves.
In this article, we reflect on the Student Experience project and the principles that we have developed for sustainable adoption of AI.

### Start with the people who will own it

As an AI expert, it is easy to provide a solution that works. 
However, is it the right solution? 
Is it meeting the needs of the people who will use it?
This sounds obvious but it is surprising how often technically adept professionals forget to check if they are meeting needs because they are so caught up with the cleverness of the solution. 

Thus the first principle is to give the client ownership. 
When we want to make the client the owner, we must involve the operational team in decisions from the outset, embed technical expertise with them, and deliberately transfer capability.

Ultimately, the Adoption Lab's aim is to no longer be needed. 
Adoption succeeds when the operational team takes complete ownership of the solution. 

For the Student Experience project, the Adoption Lab proposed bringing in a recent PhD graduate to help with development. 
We embedded that person in the team so he could transfer some of his knowledge and skills to the team directly. 

### Decide how you will know whether it works — ~150 words

The second principle is to agree on an evaluation metric. 

A common example is using an LLM to check documents against rules or regulations.
Producing a plausible answer is not enough: performance needs to be tested against a benchmark set of known cases. 
That benchmark should remain part of the system so changes to the model or prompt can be checked over time.

If you have several metrics, try to combine them into a single score. 
The problem with several metrics is that some may go up while others go down. 
If you don't make a clear decision at the start of their relative importance, it can become hard to agree on this later. 

You should also establish a baseline. 
Where are you now in terms of performance? 
This will be important later on when you want to be able to show the impact of your work. 

For the Student Experience project, the clear metric is how well we can predict "did not pass" at week 2 and week 4. 
We use an F2 score, deliberately giving greater weight to finding students who may need support than to avoiding unnecessary alerts.

The point is that a solution might be technically better but still be useless if it produces alerts too late, overwhelms staff, or directs attention towards the wrong cases. 
We can avoid this by finding a metric that truly fits requirements. 

### 4. Constrain the problem — ~120 words

AI projects can easily become open-ended programmes.
If things improve, then more is wanted. 
If things don't improve, then the project is a failure. 
Thus the third principle is to constrain the scope of the project at the outset. 

For the Student Experience project, we constrain our initial project at being able to predict the student outcome better than the existing approach. 
We leave out of scope things like being able to answer "will it help student X if we give him/her a ring". 
While this might work for an extension project, constraining the scope ensures we fit to the time and resource available.

*A small AI project that reaches use is more valuable than an ambitious AI programme that remains permanently at 80% completion.*

### 5. Put time boundaries around the work — ~110 words

It might seem like time boundaries are similar to scope creep. 
The problem here is one of momentum. 
People begin enthusiastically but their day job intervenes. 
"Are we even still doing an AI project?", one might reasonably ask after several months without a meeting and no clear timeline or plan. 
The fourth principle is to set time boundaries and agree a rhythm for the work.

For the Student Experience project, we formulated a 3 month plan with milestones that act as check points. 
We also set up weekly informal working together sessions alongside less frequent sprint review meetings. 
This allows us to come together and be able to be clear about whether we are on-track and what we need to do to meet the milestones. 

Thus the Adoption Lab should not only bring AI expertise, it also needs to impose a *cadence for adoption*.

### 6. AI can now accelerate the technical work — ~100 words

For many AI projects, AI can also be used to help with the technical work. 
The idea for this originates with Andrej Karpathy's Auto-Research.
In essence, we can ask AI to try different approaches, compare models, and test alternatives. 
For this to make sense, we must have a clear metric for success---it needs to know when one solution is better than another.

With the Student Experience project, we are already trying out Auto-Research approaches and this has already allowed us to compare many different models and configurations. 

While the obvious consequence of this is speed, the more important consequence is to force us to be clear about the problem we are trying to solve and how we will evaluate it.



### 7. Ending: sustainable adoption means leaving capability behind — ~90 words

The ultimate measure of success for the Adoption Lab is not how many AI systems we build, but how many teams no longer need us.
We have over a dozen projects in progress, several of which are already showing positive benefit, and the Student Experience project in particular is well on its way to being a success.


