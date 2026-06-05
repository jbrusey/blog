---
layout: post
title: "Data Driven Reinforcement Learning"
date: 2024-06-22 04:33:09 +0000
categories: []
tags: []
---

# Brainstorm

- We got data - now what?
  - IoT yields data
  - Sometimes there are missing values - low yield, erroneous measurements, dead sensors, malfunction
  - There is often measurement noise
    - where does it come from (e.g., electrical noise); why does it happen (interference)
  - Semantics are important - what does it mean that sensor 21 got a reading of 15 at date time 2024/6/1 12:54:01?
- Controlling a physical system is difficult
  - Why is it difficult?
    - Dynamics of real systems differ from assumed behaviour.
    - Moment to moment state of system varies from our calculated estimate of what should happen by some small amount
- How do we tackle controlling a difficult to simulate physical system?
  - Don't make too many assumptions up front about assumed behaviour
  - If we don't assume, then we must look at the data
  - This leads to data-driven simulation approaches
  - Deterministic simulation is an obvious approach but stochastic simulation also possible based on observed residuals
  - Estimating the gradient may be difficult - more advanced approaches to gradient estimation can yield better results
-
