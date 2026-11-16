<img src="assets/banner-last.svg" alt="Hi, I'm Maria Sol. Software systems reference series, edition 2026, Argentina." width="100%" />

AI engineer and full-stack developer. I build end to end: back ends in Python and FastAPI with LLMs, RAG and agents at their core, and front ends in React, Next.js and TypeScript.

**Developer reference series**: a long-term project built in the open. It grew out of appreciation for the mentors and colleagues whose work shaped my learning, and from a lesson learned in the process: mastering these fields takes hard work and time. It is meant for anyone setting out to learn them, and for colleagues looking for a clear reference when needed.

Each module has its own repository, built on the same structure: the explanation, a cheat sheet, working examples and real projects that apply it, with the reasoning behind each decision. There are 26 modules for now, a starting point rather than a limit. This profile is updated as the books and projects advance.

## Tech Stack:

<p> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&amp;logo=typescript&amp;logoColor=white" alt="TypeScript" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&amp;logo=javascript&amp;logoColor=black" alt="JavaScript" /> <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&amp;logo=nodedotjs&amp;logoColor=white" alt="Node.js" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&amp;logo=fastapi&amp;logoColor=white" alt="FastAPI" /> <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&amp;logo=pydantic&amp;logoColor=white" alt="Pydantic" /> <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&amp;logo=sqlalchemy&amp;logoColor=white" alt="SQLAlchemy" /> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&amp;logo=postgresql&amp;logoColor=white" alt="PostgreSQL" /> <img src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge" alt="SQL Server" /> <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&amp;logo=pytest&amp;logoColor=white" alt="pytest" /> <img src="https://img.shields.io/badge/NestJS-E0234E?style=for-the-badge&amp;logo=nestjs&amp;logoColor=white" alt="NestJS" /> <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&amp;logo=react&amp;logoColor=61DAFB" alt="React" /> <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&amp;logo=nextdotjs&amp;logoColor=white" alt="Next.js" /> <img src="https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&amp;logo=tailwindcss&amp;logoColor=white" alt="Tailwind CSS" /> <img src="https://img.shields.io/badge/Zod-3E67B1?style=for-the-badge&amp;logo=zod&amp;logoColor=white" alt="Zod" /> <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&amp;logo=vite&amp;logoColor=white" alt="Vite" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&amp;logo=docker&amp;logoColor=white" alt="Docker" /> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&amp;logo=git&amp;logoColor=white" alt="Git" /> <img src="https://img.shields.io/badge/GitHub-24292F?style=for-the-badge&amp;logo=github&amp;logoColor=white" alt="GitHub" /> <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&amp;logo=vercel&amp;logoColor=white" alt="Vercel" /> <img src="https://img.shields.io/badge/Railway-0B0D0E?style=for-the-badge&amp;logo=railway&amp;logoColor=white" alt="Railway" /> <img src="https://img.shields.io/badge/Resend-000000?style=for-the-badge" alt="Resend" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&amp;logo=langchain&amp;logoColor=white" alt="LangChain" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&amp;logo=langgraph&amp;logoColor=white" alt="LangGraph" /> <img src="https://img.shields.io/badge/Anthropic-D97757?style=for-the-badge&amp;logo=anthropic&amp;logoColor=white" alt="Anthropic" /> <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge" alt="OpenAI" /> <img src="https://img.shields.io/badge/Gemini-4285F4?style=for-the-badge&amp;logo=googlegemini&amp;logoColor=white" alt="Gemini" /> <img src="https://img.shields.io/badge/Groq-F55036?style=for-the-badge" alt="Groq" /> <img src="https://img.shields.io/badge/Chroma-FF6446?style=for-the-badge" alt="Chroma" /> <img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&amp;logo=n8n&amp;logoColor=white" alt="n8n" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&amp;logo=streamlit&amp;logoColor=white" alt="Streamlit" /> </p>

## Shipped.

### Featured

**[Polaris](https://polaris-fawn-two.vercel.app)** · Python · FastAPI · LangChain · Chroma · Groq<br>
A RAG assistant over Argentine Central Bank regulations. Its security review found three things worth fixing. A provider error was reaching the browser with my organization ID, plan limits and model name; clients now get a generic message instead, the full detail stays in the logs, and my bugs (500) are kept apart from provider failures (503). Each question travels inside its own tags, and the same markers are stripped from anything a user types, so nobody can fake a retrieved passage. And a 25-second timeout with one retry could take 51 seconds against the front end's 30, which is why it now waits 15 and doesn't retry. Testing also showed references sometimes arriving wrapped in 【】 brackets; normalizing them first kept the citation check from rejecting valid answers.

**[Alphecca](https://alphecca-eight.vercel.app/)** · Python · FastAPI · Pydantic · Next.js · TypeScript<br>
Describe what you need and it recommends an LLM from Google, OpenAI or Anthropic. The first version was built on Streamlit; today it's Next.js with a FastAPI back end. Next: semantic search over the providers' docs, to answer questions like "which models break if I send temperature?"

**[Ethos](https://ethos-health-bice.vercel.app)** · FastAPI · PostgreSQL · Node.js · React<br>
A clinic booking app for a fictional functional-medicine practice. The front end went live ahead of the back end: it talks to one interface with two adapters, demo and HTTP, picked by an environment variable, so the switch took a single setting. When it was ready to share, I reviewed its security: registration is off in production, the waitlist validates input without keeping any email, login has a rate limit, and the content security policy runs in report-only mode first, so nothing breaks until it's enforced. Next: capping how far ahead someone can book, memberships with Stripe, and testing the LLM layer that helps clinicians interpret patient metrics.

**[Lynx](https://lynx-site-chi.vercel.app/)** · Python · LangGraph · Gemini · FastAPI<br>
Detects fraud, scams and financial exploitation of older adults in their bank accounts. Before making it public, I reviewed the repository: nothing left from the original challenge material, and a clean dependency audit. Next, ahead of the evals: setting a timeout on the Gemini SDK.

**[Marvel Characters](https://marvel-characters-coral.vercel.app/)** · Next.js · React · TypeScript · Zod<br>
An older project of mine, rebuilt as a searchable browser of 304 characters. Its hardening pass pinned the dataset to a fixed commit, so an upstream change can't alter it silently, limited images to HTTPS from two allowed sources, and added protective headers while hiding the framework's signature. Next: a real 404 for characters that don't exist.

**[Blaze](https://github.com/mssegosende/blaze-ai-editor)** · Node.js · Hono · OpenRouter · React · TypeScript · Tiptap<br>
A Markdown editor with an AI assistant. The assistant is a single-step agent: one action and one call per request, which keeps cost and behavior predictable and leaves every change to the person. The Claude Code sessions I built it with are saved unedited in `ai-sessions/`, so anyone can see how that collaboration went.

### Built, not deployed yet

| Project | What it does | Stack | Status |
|---|---|---|---|
| **Larawag** | A support API that creates exactly one ticket per message, even when the same message arrives 50 times at once | Python, FastAPI, PostgreSQL, n8n, Docker | [Repo](https://github.com/mssegosende/larawag) · not deployed yet |
| **Helvetios** | A core banking system: accounts, balances and every money movement, with double-entry accounting | Python, FastAPI, PostgreSQL | Repo · not deployed yet |
| **Arcturus** | A multi-agent pipeline that reviews pull requests against business rules and hands them to a human when the rating is too low | Python, LangChain, LangGraph, OpenAI | Local repo, not on GitHub yet |
| **Titanium TX** | A marketplace for heavy commercial vehicles: inventory, listings and lead generation | React, Tailwind CSS | Local repo, not on GitHub yet |
| **Apsis** | A personal AI productivity app: week view, study tracking and expenses, with an LLM to ask questions | React, TypeScript, Tailwind CSS, Vite | Local repo, not on GitHub yet |

## From March to now.

<details>
<summary><b>November 2026: more projects and the series</b></summary>

- **Shipped:** Polaris, Alphecca and Ethos went from repo to deploy, Marvel Characters came back rebuilt.
- **Alphecca:** I needed a way to compare models for myself. It estimates, from the tokens you use per day, which model suits your workload and which one costs less. I built it to scale.
- **The series:** 5 of 3 books are finished and 2 more on the way.
- **The portfolio:** it's finished. From here, it simply keeps growing, with more projects and more videos as I build them.

</details>

<details>
<summary><b>October 2026: more challenges, AI engineering and data science</b></summary>

- **Lynx:** I was studying fraud cases and brought AI engineering into one of them. I didn't know it was a data science challenge until I was already doing it. I ended up investigating it about it and defending it. Now I'm testing it against new cases.
- **Polaris:** finished, ready to go live.
- **Portfolio:** finished, with the projects I chose to show.
- **The series:** I mapped 26 books and wrote the first three, Git & GitHub, Docker & Kubernetes and OOP.

</details>

<details>
<summary><b>September 2026: back to where I started</b></summary>

- **Ethos:** I started it from scratch, with FastAPI, PostgreSQL and SQLAlchemy 2.0 behind an Express gateway. I took charge of every layer, from the database to the deploy.
- **Alphard:** my friend and I kept learning the best business rules of finance as we built it. 
- **Portfolio:** I started building it.

</details>

<details>
<summary><b>August 2026: first sight of complete projects</b></summary>

- **Going deeper:** besides databases, I studied the back end and the structure behind it in depth. I made things more complex on purpose, so I could focus on the problems that matter most.
- **Alphard, Helvetios and Larawag:** all three were designed and started this month, side by side.
- **n8n finds its place:** in Larawag, it sits at the edge of the system, never at its core.
- **Data at scale:** after studying databases in July, I wanted to see how a very large integration works. I had migrated front ends and services before, but never the data layer. I like understanding the whole picture, so I set out to learn how it's done and how I would approach it.

</details>

<details>
<summary><b>July 2026: deciding to change</b></summary>

- **From features to full projects:** instead of leaving ideas as ideas, as I always had, or building isolated features, I started creating complete projects, putting them up in my lab and checking how far they could go.
- **Databases and machine learning:** how data moves with agents caught my attention, so I went back to databases and to how machine learning connects with them.
- **Titanium TX:** a marketplace for heavy commercial vehicles. I already knew how to build this kind of app, so I set myself the challenge of digging into its business rules. The front end is built and what it will do is clear, so the deploy comes next.

</details>

<details>
<summary><b>June 2026: machine learning</b></summary>

- **Machine Learning in Production (DeepLearning.AI):** I learned to see machine learning as a lifecycle, not a single step, and that improving the data often pays off more than tuning the model.
- **Apsis:** a tool for myself with an LLM inside, where I could ask anything. Building it showed me that not every question needs the same model. It also taught me that an app that makes me log everything soon becomes a chore, and looking into that led to the projects I find most useful today.

</details>

<details>
<summary><b>May 2026: back to the foundations</b></summary>

- **The fundamentals, again:** I reviewed software design, from layers and domain entities to hexagonal architecture.
- **At work:** I designed a code-review pipeline based on RAG, which later became Arcturus.

</details>

<details>
<summary><b>April 2026: systems and security</b></summary>

- **UTN-FRD:** I began the University Diploma in Linux Network Administration with a focus on Cybersecurity, to understand the parts of a system beyond my own code.
- **In practice:** every project in Shipped went through a security review based on what I learned here.

</details>

<details>
<summary><b>March 2026: automation</b></summary>

- **n8n:** I researched it through engineers' YouTube channels, which helped me understand it and decide what was worth learning. Then a full course showed me what it could automate, from webhooks to AI agents, and left me with a list of ideas still to build.
- **Next step:** I decided to take it slowly and figure out how to fit it into complete projects of my own, starting with where n8n ends and the business logic begins.

</details>

## The series, on the shelf.

The first books are out: Git & GitHub, Docker & Kubernetes, OOP, AI engineering and Python. Each one opens its repo: cheat sheet, runnable examples, exercises and a real project. Coming next: Design patterns, Async & reactive, and Cloud & scalability. The rest of the shelf fills in as I go. Scroll sideways to see all 26.

<pre><a href="https://github.com/mssegosende/01-git-github"><img src="assets/covers/01.png" alt="01 · Git &amp; GitHub cheat sheet" width="180" align="top" /></a><a href="https://github.com/mssegosende/02-docker-kubernetes"><img src="assets/covers/02.png" alt="02 · Docker &amp; Kubernetes cheat sheet" width="180" align="top" /></a><a href="https://github.com/mssegosende/04-oop"><img src="assets/covers/04.png" alt="04 · OOP cheat sheet" width="180" align="top" /></a><a href="https://github.com/mssegosende/23-ai-engineering"><img src="assets/covers/23.png" alt="23 · AI engineering cheat sheet" width="180" align="top" /></a><a href="https://github.com/mssegosende/20-python"><img src="assets/covers/20.png" alt="20 · Python cheat sheet" width="180" align="top" /></a><img src="assets/covers/03.png" alt="03 · Data structures &amp; algorithms cheat sheet" width="180" align="top" /><img src="assets/covers/05.png" alt="05 · Clean code &amp; SOLID cheat sheet" width="180" align="top" /><img src="assets/covers/06.png" alt="06 · Design patterns cheat sheet" width="180" align="top" /><img src="assets/covers/07.png" alt="07 · Testing cheat sheet" width="180" align="top" /><img src="assets/covers/08.png" alt="08 · Web &amp; APIs cheat sheet" width="180" align="top" /><img src="assets/covers/09.png" alt="09 · Architecture &amp; messaging cheat sheet" width="180" align="top" /><img src="assets/covers/10.png" alt="10 · Databases, ORMs &amp; Redis cheat sheet" width="180" align="top" /><img src="assets/covers/11.png" alt="11 · Async &amp; reactive cheat sheet" width="180" align="top" /><img src="assets/covers/12.png" alt="12 · Linux &amp; SysAdmin cheat sheet" width="180" align="top" /><img src="assets/covers/13.png" alt="13 · DevOps, DevSecOps &amp; CI/CD cheat sheet" width="180" align="top" /><img src="assets/covers/14.png" alt="14 · Cloud &amp; scalability cheat sheet" width="180" align="top" /><img src="assets/covers/15.png" alt="15 · Cybersecurity cheat sheet" width="180" align="top" /><img src="assets/covers/16.png" alt="16 · JavaScript, React &amp; Express cheat sheet" width="180" align="top" /><img src="assets/covers/17.png" alt="17 · TypeScript cheat sheet" width="180" align="top" /><img src="assets/covers/18.png" alt="18 · Node.js &amp; NestJS cheat sheet" width="180" align="top" /><img src="assets/covers/19.png" alt="19 · Mobile — React Native cheat sheet" width="180" align="top" /><img src="assets/covers/21.png" alt="21 · Java cheat sheet" width="180" align="top" /><img src="assets/covers/22.png" alt="22 · C# cheat sheet" width="180" align="top" /><img src="assets/covers/24.png" alt="24 · Data science &amp; ML cheat sheet" width="180" align="top" /><img src="assets/covers/25.png" alt="25 · MLOps cheat sheet" width="180" align="top" /><img src="assets/covers/26.png" alt="26 · Automation &amp; AI agents with n8n cheat sheet" width="180" align="top" /></pre>

## All 26 at a glance.

<img src="assets/index.svg" alt="The 26 modules in five blocks: tools, foundations and architecture, infrastructure and operations, languages and frameworks, and AI." width="100%" />

---

<p align="center"><sub>WORK IN PROGRESS · <a href="https://github.com/mssegosende">@mssegosende</a></sub></p>

