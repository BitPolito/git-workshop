# Contributing to Git & GitHub Workshop

Thanks for taking part in the **BitPolito Git & GitHub workshop**! 

This repository is a practice playground, so contributing here is part of the exercise: every contribution is a chance to learn the real workflow used in open source projects. Please read the rules below before opening your Pull Request (PR).

## Table of contents

- [Code of conduct](#code-of-conduct)
- [What you can contribute](#what-you-can-contribute)
- [Getting started](#getting-started)
- [Branch naming](#branch-naming)
- [Contributor file format](#contributor-file-format)
- [Commit messages](#commit-messages)
- [Opening a Pull Request](#opening-a-pull-request)
- [Reviewing someone else's PR](#reviewing-someone-elses-pr)
- [Resolving conflicts](#resolving-conflicts)
- [Need help?](#need-help)

## Code of conduct

Be kind and respectful. Everyone here is learning, and mistakes are expected and welcome.

- Be patient with beginners and give feedback constructively.
- No offensive, discriminatory or inappropriate content in files, commits, PRs or comments.
- Don't share personal information (yours or other people's) that you don't want to be public.

## What you can contribute

- **Your contributor file** in the `contributors/` folder (the main workshop exercise).
- **Fixes and improvements** to the documentation, such as typos, unclear explanations or broken commands.
- **Review comments** on other participants' PRs.

Please keep each PR focused on **one thing only**.

## Getting started

Follow the full step-by-step exercise in the [README](README.md). In short:

1. Make sure Git is installed and configured with your name and email:

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```

2. Clone the repository and move into its folder:

   ```bash
   git clone git@github.com:BitPolito/git-workshop.git
   cd git-workshop
   ```

3. Create your own branch from an up-to-date `master`:

   ```bash
   git switch master
   git pull
   git switch -c your-name
   ```

> If you don't have write access, ask the instructors to add you as a collaborator, or [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the repository and open the PR from your fork.

## Branch naming

- Use **lowercase letters and hyphens only**.
- Name your branch after yourself: `ada-lovelace`.
- For anything other than your contributor file, use a short prefix:
  - `fix/short-description` for fixes (e.g. `fix/readme-typo`)
  - `docs/short-description` for documentation changes
- Never commit directly to `master`.

## Contributor file format

Create a file named `contributors/your-name.md`, using the **same name as your branch**, with this content:

```markdown
# Your Name

- **GitHub:** @your-username
- **Favorite Git command:** git something
- **Why I'm here:** a short sentence
```

Rules:

- Only add or edit **your own file**. Don't touch other people's files.
- Keep it short, friendly and safe for work.
- Don't include private data such as phone numbers, home addresses or passwords.

## Commit messages

A good commit message is **short**, written in the **imperative mood**, and says **what** the commit does.

| ✅ Good                             | ❌ Avoid          |
|------------------------------------|------------------|
| `Add Ada Lovelace to contributors` | `stuff`          |
| `Fix typo in README`               | `fixed things!!` |
| `Update favorite command`          | `asdfgh`         |

Guidelines:

- Keep the first line under about 72 characters.
- Start with a verb: `Add`, `Fix`, `Update`, `Remove`.
- One logical change per commit.

## Opening a Pull Request

Before you open the PR, check that:

- [ ] Your branch is named correctly.
- [ ] You only changed the files you intended (check with `git status` and `git diff`).
- [ ] Your commits have clear messages.
- [ ] Your contributor file follows the [format](#contributor-file-format).

Then:

1. Push your branch:

   ```bash
   git push -u origin your-name
   ```

2. On GitHub, click **Compare & pull request**.
3. Set the **base** branch to `master` and the **compare** branch to yours.
4. Write a clear title (e.g. `Add Ada Lovelace to contributors`) and a one-line description.
5. Click **Create pull request**.

If a reviewer asks for changes, just commit and push to the same branch: the PR updates automatically.

## Reviewing someone else's PR

Reviewing is part of the exercise! Leave at least one comment or approve the PR of the person next to you.

When reviewing, check that:

- The file is in `contributors/` and named correctly.
- The content follows the template.
- The commit message is clear.

Be specific and kind. Prefer *"Could you rename the file to match your branch?"* over *"Wrong name."*

Once a PR has been reviewed, it can be merged with **Merge pull request**. Afterwards, update your local copy:

```bash
git switch master
git pull
```

## Resolving conflicts

A conflict happens when Git can't decide which version of a line to keep. If you get one:

1. Open the conflicting file and look for the markers `<<<<<<<`, `=======` and `>>>>>>>`.
2. Keep the lines you want and **delete the markers**.
3. Stage and commit the result:

   ```bash
   git add <file>
   git commit
   ```

4. Push again.

## Need help?

| Problem                                                | What to do                                       |
|--------------------------------------------------------|--------------------------------------------------|
| I changed a file and want to discard it (not committed) | `git restore <file>`                             |
| I need to set my work aside for a moment               | `git stash`, then `git stash pop` to get it back |
| I committed something already shared and it's wrong    | `git revert <commit>`                            |
| I don't know where I am                                | `git status` and `git log --oneline`             |
| I'm stuck                                              | Raise your hand or open an issue: it happens to everyone |

---

Made with 💙 by [BitPolito](https://github.com/BitPolito)
