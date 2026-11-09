# ClassroomCast — Meeting Script (about 5 minutes)

Speak slowly. Open the 8-page PDF and turn the page when you see **[Page X]**.

---

## Opening (30 seconds)

"Good morning, teacher. Today we want to show you our ClassroomCast project plan.

We have finished the planning documents. **Nothing is built or tested yet.**

To make it easy, we put everything in one 8-page summary. At the end, we need your decision on a few points."

## [Page 1] What the project is (45 seconds)

"ClassroomCast is a web system that works on a local network, without internet.

It does three things:

1. **Screen sharing.** The teacher shares their screen and audio. 50 to 150 students watch in their browser. They don't install anything.
2. **Class control.** The teacher creates a class with a join code and QR code, then approves, removes or blocks students.
3. **Website blocking.** The admin can block AI websites, coding agents, social media and games from a dashboard, using profiles like *Exam Mode*. We use AdGuard Home to do the blocking, so nobody needs to change router settings by hand.

In total, we have 63 requirements, 68 features, 15 use cases, 18 process flows and 90 test cases."

## [Page 2–3] Scope and roles (30 seconds)

"Page 2 shows what is in scope and out of scope. For example, we will **not** record video and we will **not** control student screens.

Page 3 shows the four roles: System Admin, Teacher, Student and Network Admin. Each role can only do its own job."

## [Page 4] Architecture (30 seconds)

"Here is our system design. The teacher sends one stream to a media server called an SFU. The SFU sends a copy to each student, so the teacher's laptop does not get overloaded.

The technology, like React, NestJS and LiveKit, is our **proposal**. We will confirm it after small tests."

## [Page 5] MVP — the most important part (1 minute)

"We have about 320 hours for the three sprints, and the sprints include the holidays. This is a lot of work, so we propose an MVP, a smaller first version, in three levels:

- **Level A, build and demo:** all 31 Must requirements: screen sharing, joining, approval, website blocking, and restoring the rules when class ends.
- **Level B, design and document:** campus network mode and the full 150-student test. We will deploy on the campus network only if campus IT approves.
- **Level C, only if we have time:** extra features like file sharing, polls and scheduling.

We will build first on **our own router**, because we control it and do not need to wait for campus IT."

## [Page 6] Schedule and team (30 seconds)

"We have three sprints:

- **Sprint 1, 30 Nov to 11 Dec:** a simple demo where one teacher shares a screen with 3 laptops, and AdGuard blocks one website.
- **Sprint 2, 14 to 25 Dec:** audio, controls and website-blocking profiles.
- **Sprint 3, 28 Dec to 13 Jan:** safety features and testing, with no new features.

The final presentation is on 3 February.

We found that our documents show different task owners, so we will agree one list as a team."

## [Page 7] Testing (20 seconds)

"We have 90 test cases, but none has been run yet because nothing is built.

We cannot get 150 laptops, so we plan to test with 10 to 20 real laptops and simulate the rest. We will report those results separately, and we will not claim 150 students works until we measure it."

## [Page 8] Questions for you (1 minute)

"Finally, we need your decision on these points:

1. Do you approve our MVP: Level A build, Level B document, Level C optional?
2. Is testing with 10 to 20 real laptops plus simulation OK?
3. Can campus mode be design and documentation only, unless campus IT approves? And who should we contact in campus IT?
4. Is the deadline 25 January, with the release on 27 January and the presentation on 3 February?
5. For task owners, can our team choose one final list?

We also listed three smaller points: acceptance targets, out-of-scope items, and the technology."

## Closing (15 seconds)

"That is our plan. Thank you, teacher. Do you have any questions or feedback for us?"

---

## If the teacher asks…

| Question | Simple answer |
|---|---|
| "Why not build everything?" | "We have about 320 hours and the holidays. We want to finish the important parts well, not everything badly." |
| "Why your own router first?" | "We control it. On the campus network, we need permission from campus IT first." |
| "Can students get around the blocking?" | "Yes, with a VPN or different DNS settings. We will write this limitation down honestly. Stronger blocking needs campus IT." |
| "Have you tested anything?" | "Not yet. Nothing is built. We will run small tests in the design phase, 18 to 27 November." |
| "What is an SFU?" | "A media server. It receives the teacher's screen once and sends a copy to every student." |
| "What is AdGuard Home?" | "A free program on our server that blocks website names, like chatgpt.com, for the students." |

**Tip:** Write the teacher's answers in `ClassroomCast_Teacher_Meeting_Questions.md` during the meeting.
