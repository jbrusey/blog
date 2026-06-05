---
layout: post
title: "IoT security and privacy should be a national concern"
date: 2023-04-19 21:02:20 +0000
categories: []
tags: []
---

# Introduction

In late October of 2016, servers at Dyn, an Internet Domain Name System (DNS) service provider, began receiving an overwhelming flood of requests. These requests did not originate from a single computer; instead, thousands of independent and seemingly unrelated systems were simultaneously sending packets in a coordinated attack.

Distributed Denial of Service (DDoS) attacks, like the one Dyn faced, are particularly challenging to mitigate because they involve multiple sources rather than a single computer. Surprisingly, the true source of the attack may not have been a foreign agent or disgruntled employee, but rather a 'script kiddie' seeking an advantage in an online game ([DDoS attacks on Dyn](https://en.wikipedia.org/w/index.php?title=DDoS_attacks_on_Dyn&oldid=1149750626), 2023).

The enabler of this massive assault was a piece of malware called Linux/Mirai, previously discovered and analysed by the MalwareMustDie group ([unixfreaxjp, 2016](https://blog.malwaremustdie.org/2016/08/mmd-0056-2016-linuxmirai-just.html)). Their key finding revealed that the malware exploited weak security in WebIP cameras and Digital Video Recorders (DVRs), specifically targeting devices with unchanged default, factory-set passwords. It was precisely these vulnerable WebIP cameras that were weaponized in the coordinated attack on Dyn.

The security of such systems should not just concern individual device users—it should concern us all.

# What is an IoT device?

It may be surprising to think of Internet connected video cameras (WebIP cameras) or network routers as Internet of Things or IoT devices. The broad definition that we are using here is a computing device that integrates itself into the home or office, and often comes with some form of Internet connection. IoT devices serve many purposes from mood lighting to baby monitoring; from temperature monitoring to turning on the heating system.

In this blog post, we aim to explore the broader implications of IoT security, with a particular focus on the potential consequences for national and international security. We will address three key questions to better understand the risks and challenges associated with IoT devices:

1.  The perceived harmlessness of IoT devices: Does it truly matter if an external party can control your lights or heating system?
2.  What are the security weak points in IoT devices and how might they be mitigated?
3.  Privacy implications associated with IoT devices: How are vendors addressing or ignoring privacy concerns?

By addressing these questions, we hope to provide a comprehensive understanding of the IoT security landscape and encourage discussions on how to create a more secure and privacy-conscious IoT environment for all users.

# Mostly harmless

Why might IoT devices be considered harmless? They offer convenience and efficiency, automating tasks and integrating into daily life. They don't store sensitive data, such as credit card numbers or bank details and have great benefits, including energy savings, accessibility, and convenience. Some would argue that any reduction in security or privacy is easily outweighed by these benefits.

Despite the apparent harmlessness of IoT devices, there are significant counterarguments to consider. IoT devices can be compromised and used in large-scale cyberattacks like DDoS attacks, as evidenced by the Dyn incident. Additionally, these devices can expose sensitive information or personal data to unauthorised access, especially if proper security measures aren't in place. Moreover, IoT devices can act as entry points for attackers to infiltrate larger networks or critical infrastructure, posing risks not only to individuals but also to national and international security. An example is the botnet of 500,000 devices over 54 countries created using the VPNFilter malware that was used to target servers in Ukraine ([William Largent, 2018](https://blog.talosintelligence.com/vpnfilter/)). The devices in question were a variety of brands of consumer network routers. Thus, it is crucial to address IoT security concerns to ensure the safety and privacy of users and systems alike.

# Security weak points

As pointed out by [Ahmad and Alsmadi (2021)](https://doi.org/10.1016/j.iot.2021.100365), there are a number of challenges that are specific to IoT, such as their low cost and small form factor. IoT devices are often intended to melt into the environment; tucked on a shelf and forgotten about. However, this runs counter to the need for security management and software updates. Similarly, convenience and ease may encourage users to put them outside firewall protection.

The key security weak points are enumerated in the following table:

| IoT Security Weak Points                     | Explanation                                                                                                                                                        |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Insecure default settings                    | Many IoT devices come with default passwords and settings that users often don't change, leaving them vulnerable to unauthorised access.                           |
| Insufficient encryption and data protection  | IoT devices may lack proper encryption for data transmission and storage, exposing sensitive data to potential interception.                                       |
| Lack of regular security updates and patches | Manufacturers may not provide timely security updates and patches for their devices, leaving them exposed to known vulnerabilities.                                |
| Inadequate authentication methods            | Weak authentication methods or lack of multi-factor authentication can make it easier for attackers to gain access to IoT devices.                                 |
| Insecure network configurations              | IoT devices may be connected to networks without proper segmentation or firewall protection, increasing the risk of unauthorised access to other critical systems. |
| Absence of built-in security features        | IoT devices may not be designed with security-by-design principles, lacking hardware or software security features that could protect them from attacks.           |
| Poor supply chain security                   | IoT devices may contain third-party components that do not meet necessary security requirements, introducing vulnerabilities into the final product.               |

While some weaknesses may seem to stem from the end user's disregard or lack of education, there are many approaches to improving security by design. For example, legislation in many countries now forbid default passwords. A further (sensible) step would be to forbid default login names, such as the \`pi' user that once existed on the Raspberry Pi ([Cunningham, 2022](https://arstechnica.com/gadgets/2022/04/raspberry-pi-os-axes-longstanding-default-user-account-in-the-name-of-security/)). Multi-factor authentication (MFA) is now well established for e-mail and other web services but is not yet standard for IoT devices.

We see steps in the right direction but there is still a way to go before all IoT devices are completely secure.

# Privacy

As with security, privacy can sometimes be seen as a luxury. More than that, the common, anti-privacy refrain "I've got nothing to hide", even suggests that privacy might be a bad thing; that if you have something to hide, then you must have done something *wrong* ([Solove, 2007](https://digital.sandiego.edu/sdlr/vol44/iss4/5/)). Even if we don't immediately fear an Orwellian dystopia arising from our use of IoT, we should nonetheless have safeguards against it.

A simple example of a cause for concern are the digital assistants that now share many living rooms and kitchens. Although Amazon has stated that they do not use recordings from their voice-activated assistant, Alexa, there are concerns that adverts are being targeted on the basis of smart-speaker interaction ([Iqbal et al., 2023](http://arxiv.org/abs/2204.10920)). Iqbal et al suggest, for example, that based on your interaction Alexa might identify your persona as being towards having a tidy home and thus provide a greater percentage of "by the way" suggestion adverts about home cleaning products. Note that it is possible to adjust privacy settings ([Newman, 2023](https://www.pcworld.com/article/1663367/4-amazon-privacy-settings-you-should-change-right-now.html)) but, as with security, many will lose some aspect of their privacy by default.

As with security, one possible path to addressing privacy concerns is through governments and regulatory bodies working together with vendors, manufacturers, and consumer advocacy groups to work out sensible guidelines and, where necessary, strict rules and penalties. This approach aims not to hinder innovation but to prevent repeating past mistakes.

In some cases, vendors are building privacy-by-design into their products. Examples include Apple's HomeKit, which has a strong focus on privacy and security. However, some users might prefer open-source projects like Mozilla's WebThings, Home Assistant, OpenHAB, and Tasmota. From a privacy and security perspective, open-source projects offer the advantage of transparency, as anyone can inspect the source code for potential flaws. Another key advantage of open-source systems is that data is stored and processed locally rather than sent to the vendor's server.

# Conclusions

Security and privacy are essential aspects of IoT technology that should not be overlooked or dismissed. Even if security of a single device seems unimportant to its owner, thousands of such compromised devices can produce significant damage. As IoT devices become increasingly integrated into our daily lives, the potential for security failures, privacy breaches, and misuse of personal data grows. As with the VPNFilter malware, the potential for such damage should be of national and international concern; failure to properly address IoT security threats may even cost lives. It is crucial for all stakeholders to collaborate and develop effective guidelines and regulations to safeguard both security and privacy in the IoT ecosystem. By embracing security and privacy-by-design principles and supporting open-source initiatives, we can strike a balance between innovation and protection, fostering a more secure and responsible IoT landscape for all users.
