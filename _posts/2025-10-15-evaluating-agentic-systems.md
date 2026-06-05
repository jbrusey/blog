---
layout: post
title: "Evaluating Agentic Systems"
date: 2025-10-15 17:06:00 +0000
categories: ["Org2Blog", "WordPress"]
tags: ["Emacs", "Lisp"]
permalink: "/2025/10/15/evaluating-agentic-systems/"
---

# Motivation

- common use case for agentic systems - here are some guidelines or rules or things to check and here is a document that needs to be checked
- the problem is that results are quite variable - sometimes issues are flagged and sometimes not
- we could adjust temperature but that would also limit creativity and perhaps that is not desirable
- variability is not the only issue - perhaps certain sort of problems are being missed (e.g., the LLM pays attention to the beginning and the end but not so much the middle).
- absolute trust is not possible but we need to be able to increase trust and trustworthiness in agentic systems.
- we also need to be able to ensure that as development progresses or underlying language models evolve, we don't regress or reintroduce old bugs.

# Method

- we examine the use of a unit-test style architecture as an automated test mechanism for the agentic system
- in many cases, the output of the agentic system will be text and will therefore need to be evaluated by another agent (LLM-as-a-judge)
- in other situations, it is possible to use machine code (yaml or json) as output from the LLM and this can then be evaluated programmatically.
- we review a variety of different system requirements and see how they impact the design of the evaluation framework.
- we experiment with a tiny LLM and a set of grammar rules to check compliance (of an essay) with a variety of architectural elements and use ablation studies to show the need for each element of the resulting architecture.
- possible architectural elements include:
  1.  using yaml or json encoding as input to avoid ambiguity
  2.  using yam or json encoding of output to simplify automated testing
  3.  LLM augmentation of test cases to more fully explore possible inputs
  4.  Misspellings or language variations
  5.  varying temperature
  6.  using multiple runs and comparing outputs
  7.  varying order of inputs
  8.  testing the responses from vector database to ensure consistency
  9.  splitting a large problem into a set of smaller subproblems
  10. 

# Results

## Requirements that drive agentic systems

- A common requirement is the evaluation of compliance of a document according to a set of regulations.
- Retrieval Augmented Generation (RAG) is often used along with a vector database such as Pinecone to allow the integration of a body of associated documents. Chunks from these documents are retrieved based on relevance and the context of the query.
- RAG aims to expand the set of documents able to be incorporated while keeping the context of the LLM contained and within the limits of the model.
- RAG is, however, a blunt instrument as it has variability in the results it returns and it is common for the associated document database is an grab-bag of historical documents that lacks curation.
- 

## Key elements for an evaluation framework

- 

# Conclusions
