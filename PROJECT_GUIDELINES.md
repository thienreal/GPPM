# PROJECT_GUIDELINES.md

## 🧭 Overview
This document defines the **development and evaluation criteria** for the open-source project.
It helps contributors and AI assistants (e.g., GitHub Copilot) follow consistent, competition-ready standards.

The project must comply with **Open Source Initiative (OSI)** rules and demonstrate good engineering,
usability, and sustainability practices.

---

## I. Open Source Project Requirements 

### 1. Source Availability (1.0)
- The source code and executables must be **publicly available** (e.g., GitHub, GitLab).  
- The software must be installable via:
  - Source code (`make`, `pip install .`, `npm install`)  
  - or prebuilt package (Docker image, `.exe`, `.deb`, `.rpm`)  

### 2. OSI-Approved License (1.0)

* The project must use an **OSI-approved license** (MIT, GPLv3, Apache 2.0, BSD, MPL, etc.).
* Include a `LICENSE` file in the repository root.
* Example:

### 3. Proof of Functionality (PoF ≤ 60) (1.0)

* PoF measures total functional complexity.
* Keep PoF ≤ 60 (enough to solve the challenge; avoid feature bloat).

### 4. Use of Open Source Tools (0.5)

* Use open technologies for development.

### 5. License Compatibility (0.5)

* All dependencies must be **license-compatible** with the project’s main license.

### 6. Build & Installation Guide (0.5)

* Provide a clear build and setup guide in `README.md` or `INSTALL.md`.

### 7. Public Communication Channels (0.5)

* Provide **open and transparent** channels for community communication.
* Recommended:

  * Issues: GitHub Issues / GitLab Issues
  * Chat: Discord / Telegram group
  * Docs: Wiki / ReadTheDocs

### 8. Technical Originality (1.0)

* Must show creative or technically unique aspects.
* Example: new algorithm, efficient data structure, novel UX interaction, or integration pattern.

### 9. Product Completeness (1.0)

* The software must be runnable and stable.
* All core features implemented with minimal bugs.
* Example: full CRUD, authentication, deployment-ready.

### 10. User-Friendliness (1.0)

* UI/UX should be intuitive, clean, and accessible.
* Example:

  * Web: responsive design using React or Vue
  * CLI: provide `--help` and clear error messages

### 11. Sustainability & Extendability (1.0)

* Use clean architecture and modular design.
* Provide documentation and maintainable code.
* Example:

  * Use design patterns
  * Include unit tests (`pytest`, `unittest`)
  * Setup CI/CD via GitHub Actions

### 12. Presentation & Community Appeal (1.0)

* Showcase attractively and clearly during the demo.

## Recommended Project Structure

```
project/
│
├── README.md          # Overview, setup, usage
├── LICENSE            # OSI-approved license
├── INSTALL.md         # Optional: detailed setup
├── CONTRIBUTING.md    # Contribution guidelines
├── docs/              # Documentation / diagrams
├── src/               # Source code
├── tests/             # Automated tests
└── .github/           # Issues templates / CI workflows
```

---

## Development Tips

* Commit small, readable changes with clear messages.
* Keep README minimal but informative (setup + usage).
* Add screenshots and short demo videos for presentation.
* Keep repo public and active (commits, issues, discussions).
* Prefer simple, working solutions over complex, unfinished ones.


