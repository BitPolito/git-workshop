# Git & GitHub Workshop: Practice Repository

Welcome! This repository is the playground for the **BitPolito Git & GitHub workshop**.
You will go through the whole workflow, from `clone` to `merge`, by adding yourself to the list of contributors.

Nothing you do here can break anything: this repository exists to be experimented on. 🙂

## What you will practice

By the end of the exercise you will have:

1. Cloned a remote repository onto your computer
2. Created your own branch
3. Made a change and committed it
4. Pushed your branch to GitHub
5. Opened a Pull Request and had it reviewed
6. Merged it into the project

## Prerequisites

- [Git](https://git-scm.com/downloads) installed (check with `git --version`)
- A [GitHub](https://github.com/) account
- Git configured with your name and email:

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "you@example.com"
  ```

- Access to this repository (the instructors will tell you if you need to be added as a collaborator)

## The exercise

### 1. Clone

Copy the repository onto your computer and move into its folder:

```bash
git clone git@github.com:BitPolito/git-workshop.git
cd git@github.com:BitPolito/git-workshop.git
```

### 2. Branch

Create a new branch named after you, and switch to it right away:

```bash
git switch -c your-name
```

Use lowercase letters and hyphens only, for example `ada-lovelace`.

### 3. Modify

Create a new file `contributors/your-name.md` (use the same name as your branch) with this content:

```markdown
# Your Name

- **GitHub:** @your-username
- **Favorite Git command:** git something
- **Why I'm here:** a short sentence
```

Check what changed:

```bash
git status
```

### 4. Commit

Move your change into the staging area, then save a snapshot with a clear message:

```bash
git add contributors/your-name.md
git commit -m "Add Your Name to contributors"
```

A good commit message is short, written in the imperative ("Add", "Fix", "Update"), and says *what* the commit does.
You can look at the history at any time with `git log`.

### 5. Push

Send your branch to the remote repository:

```bash
git push -u origin your-name
```

### 6. Pull Request

1. Open the repository on GitHub. A banner should offer to **Compare & pull request** for your branch.
2. Make sure the **base** branch is `main` and the **compare** branch is yours.
3. Give the PR a clear title and a one-line description.
4. Click **Create pull request**.
5. Review the work of the person next to you: leave at least one comment or approve their PR.

### 7. Merge

Once your PR has been reviewed, click **Merge pull request**, then confirm.
Finally, bring the updated `main` back to your computer:

```bash
git switch main
git pull
```

You should now see your file, and everyone else's, in the `contributors/` folder. 🎉

## Bonus: provoke a conflict

A conflict happens when Git can't decide on its own which version to keep. Better to meet one here than in a real project.

1. Create a new branch from an up-to-date `main`: `git switch -c your-name-conflict`.
2. Edit the **same line** of `CONTRIBUTORS.md` as someone else, then commit and push.
3. Open a PR. When the second one is merged, GitHub will report a conflict.
4. Resolve it by hand: open the file, keep the lines you want, delete the markers (`<<<<<<<`, `=======`, `>>>>>>>`), then `git add` and `git commit`.

## Something went wrong?

| Problem | What to do |
|---|---|
| I changed a file and want to discard the change (not committed yet) | `git restore <file>` |
| I need to set my work aside for a moment | `git stash`, then `git stash pop` to get it back |
| I committed something that is already shared and it's wrong | `git revert <commit>` |
| I don't know where I am | `git status` and `git log --oneline` |
| I'm stuck | Raise your hand: it happens to everyone |

## Cheat sheet

| Command | What it does |
|---|---|
| `git clone <url>` | Copies a remote repository onto your computer |
| `git status` | Shows the state of your files |
| `git switch -c <name>` | Creates a new branch and switches to it |
| `git add <file>` | Moves changes into the staging area |
| `git commit -m "..."` | Saves a snapshot with a message |
| `git push` | Sends your commits to the remote repository |
| `git pull` | Downloads and applies the latest remote changes |
| `git log` | Lists the commit history |

---

Made with 💙 by [BitPolito](https://github.com/BitPolito)
