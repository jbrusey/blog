---
layout: post
title: "How to do sustainable AI adoption"
date: 2026-09-25 19:37:00 +0000
permalink: "/2026/09/25/sustainable-ai-adoption/"
---

### Adoption is not the same as experimentation

What does *AI adoption* mean to you?

For many organisations, it can amount to paying an AI supplier a licence fee and hoping that this somehow changes work practice.
It is relatively easy to show that AI can do something useful.
A much harder problem is to turn that demonstration into a capability that produces lasting benefit.

In other words, it is not simply a question of whether AI can do a particular thing.
Does it work reliably, does it create measurable value, and can the organisation sustain it?

Our AI Adoption Lab at Coventry University is built on the idea that sustainability comes first.

One example is our Student Experience project.
The Student Experience team wanted to identify students who might need support before they fail or drop out.
They had experimented with a variety of solutions, but could not readily maintain or develop these themselves.

In this article, we reflect on that project and the principles we have developed for sustainable adoption of AI.

### Start with the people who will own it

As an AI expert, it is relatively easy to provide a solution that works.
But is it the right solution?
Is it meeting the needs of the people who will actually use it?

This sounds obvious, but technically adept professionals can become so absorbed in the cleverness of a solution that they forget to ask whether it genuinely meets the needs of the people involved.

The first principle, therefore, is to give the operational team ownership.
This means involving them in design decisions from the outset, embedding technical expertise with them, and deliberately transferring capability.

Ultimately, the Adoption Lab's aim is to no longer be needed.
Adoption succeeds when the operational team takes complete ownership of the solution.

For the Student Experience project, the Adoption Lab brought in a recent PhD graduate to help with development.
We embedded that person directly in the team so that knowledge and skills could be transferred through the work itself.

### Decide how you will know whether it works

The second principle is to agree at the outset how success will be measured.

A common example is using a Large Language Model to check documents against rules or regulations.
Producing a plausible answer is not enough: performance needs to be tested against a benchmark set of known cases.
That benchmark should remain part of the system so that changes to the model or prompt can be checked over time.

Where several metrics matter, the important thing is to agree the trade-offs between them in advance.
Otherwise, one measure may improve while another gets worse, leaving people arguing after the event about whether the system is actually better.

You should also establish a baseline.
Where are you now in terms of performance?
Without this, it becomes difficult later to show whether the AI has genuinely improved anything.

For the Student Experience project, our metric is how well we can predict "did not pass" at weeks 2 and 4.
We use an F2 score, deliberately giving greater weight to finding students who may need support than to avoiding unnecessary alerts.

That choice matters.
A solution might be technically better but still be useless if it produces alerts too late, overwhelms staff, or directs attention towards the wrong cases.
The metric has to reflect the real requirement.

### Constrain the problem

AI projects can easily become open-ended programmes.
Once a project shows promise, more requirements, datasets, users and possible applications tend to be added.
The finish line keeps moving.

The third principle is therefore to constrain the scope of the project at the outset.

For the Student Experience project, we constrain the initial problem to predicting student outcomes better than the existing approach.
We deliberately leave questions such as "would contacting this particular student actually improve their outcome?" outside the scope.

That is a different and much harder problem.
Predicting risk is not the same as knowing which intervention will change an individual's outcome.

Constraining the scope helps ensure that the work fits the time and resources available.

*A small AI project that reaches use is more valuable than an ambitious AI programme that remains permanently at 80% completion.*

### Put time boundaries around the work

Time boundaries may sound similar to scope control, but the problem here is momentum.

People begin enthusiastically, but their day jobs intervene.
After several months without a meeting, no clear timeline and no visible progress, it is reasonable for people to wonder whether they are even still doing an AI project.

The fourth principle is therefore to set time boundaries and agree a rhythm for the work.

For the Student Experience project, we formulated a three-month plan with milestones that act as checkpoints.
We also set up weekly informal working sessions alongside less frequent sprint reviews.

This keeps us clear about whether we are on track and what needs to happen next.

The Adoption Lab should not only bring AI expertise.
It also needs to impose a *cadence for adoption*.

### AI can now accelerate the technical work

AI itself can increasingly be used to accelerate the technical work involved in AI projects.

We are adapting an approach recently popularised by Andrej Karpathy's *autoresearch*: give an AI agent a bounded experimental problem and an objective measure of whether each change improves the result.

For this to work, the problem and the metric both have to be clear.
The agent needs to know when one solution is better than another.

In the Student Experience project, we are already using this approach to compare many different models and configurations.

The obvious consequence is speed.
The more important consequence is that it forces us to be precise about the problem we are trying to solve and how we will evaluate success.

### Sustainable adoption means leaving capability behind

The ultimate measure of success for the Adoption Lab is not how many AI systems we build, but how many teams no longer need us.

We now have more than a dozen projects in progress, several of which are already showing positive benefits, including the Student Experience project.

But the real test is not the number of projects or prototypes.
It is whether the teams involved are left with working solutions, the ability to evaluate and improve them, and the confidence and capability to continue after the Adoption Lab steps away.

That, ultimately, is what makes AI adoption sustainable.
