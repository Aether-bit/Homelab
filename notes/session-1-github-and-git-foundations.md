# Session 1 — GitHub and git foundations

## Goal

Get an actual public-facing engineering presence going. Set up the
GitHub account, the homelab repo, learn the basic git workflow, and
start documenting the journey in public from day one.

## What I did

### GitHub account and repo

- Set up GitHub account `Aether-bit` with real name and photo
- Bio: "Aspiring Infrastructure Engineer | Learning Linux, Networking, Azure"
- Created `Homelab` public repository with README and description
- Repo URL: https://github.com/Aether-bit/Homelab

### Git identity on the host

Configured global git identity so commits are properly attributed:
git config --global user.name "Kieran Mott"
git config --global user.email "278768759+Aether-bit@users.noreply.github.com"

Used the GitHub noreply email rather than my real Gmail, so commits
don't leak my personal address into public commit history. Also
toggled "Keep my email addresses private" in GitHub settings.

### Personal access token for HTTPS pushes

GitHub doesn't accept regular passwords for git operations anymore.
Generated a personal access token (Settings → Developer Settings →
Tokens classic), scope `repo`, used it as the password when pushing.

Then enabled the credential helper so I don't have to enter it every
time:
git config --global credential.helper store

This writes the token to `~/.git-credentials` in plain text — fine
for a personal machine, not ideal in higher-trust environments where
something like libsecret would be better.

### The three-step workflow

The pattern that took a few tries to fully internalise:

1. `git add <file>` — stage the change
2. `git commit -m "message"` — record it locally as a snapshot
3. `git push` — upload commits to GitHub

Editing a file is *zero* of these steps. Just saving the file doesn't
tell git anything — the change is sitting in the working directory until
explicitly staged.

`git status` is the source of truth for "what state is everything in"
and is the most useful git command for staying oriented.

### Repo structure

Created basic directory layout I'd grow into:

- `notes/` — session notes and study notes (this file lives here)
- `README.md` — top-level overview, what the repo is, who I am

### .gitignore

Added a starter `.gitignore` covering:
- OS/editor noise (.DS_Store, *.swp, .vscode/)
- Secrets and local config patterns (.env, *.secret, secrets/, *.pem, *.key)
- Python/Terraform/Ansible cruft (for when I get there)
- Local-only notes (notes/private/, scratch/)

Even though I had nothing sensitive yet, getting the habit in early
matters. Empty `.gitignore` files signal "I haven't thought about
what's in version control." Real engineers see that.

### Editor: nano → micro

Started using `nano` because it's universal, but didn't enjoy it.
Switched to `micro` on the host:
sudo pacman -S micro

Micro has modern shortcuts (Ctrl+S, Ctrl+Q, Ctrl+C/V, mouse support,
syntax highlighting). Massive ergonomic win. Stuck with nano inside
VMs since they don't have micro pre-installed.

## Problems hit (and how I fixed them)

### Divergent branches error on push

Hit it more than once. The pattern:
- Edit a file on GitHub's web UI (creates a commit there)
- Make a commit locally without pulling first
- Try to push → rejected because local and remote diverged

Fix: `git pull --rebase`, which replays my local commit on top of the
remote's commits. Then push again, clean.

Permanent fix: `git config --global pull.rebase true` so pull defaults
to rebase rather than asking every time.

Better habit: run `git pull` at the start of every session before
doing any work. Avoids the divergence in the first place.

### "git status shows my edit but the web page doesn't update"

I edited a file in micro, ran `git push`, and the GitHub page didn't
change. Confusion until I realised: I'd skipped `git add` and `git commit`.
A modified-but-unstaged file isn't part of any commit, so push has
nothing to upload.

Internalised: editing a file is not the same as committing it. The
three steps exist for a reason.

### Capitalisation of repo name

At some point the repo got renamed from `homelab` to `Homelab`. Git
remote URL had to be updated:
git remote set-url origin https://github.com/Aether-bit/Homelab.git

Lowercase is the more common convention in the Linux/infra world, but
GitHub doesn't actually care.

## Things that finally clicked

1. **Editing ≠ committing.** I caught myself thinking "but I saved the
   file" multiple times. Saving puts content on disk. Git only knows
   about content when I explicitly tell it with `add` and `commit`.

2. **Commits are local until pushed.** I can commit dozens of times
   without GitHub knowing about any of it. `push` is the moment the
   work becomes public.

3. **GitHub contribution graphs reward consistency, not intensity.**
   Today's green square is worth more than five squares in six months,
   because the pattern over time is what's visible.

4. **Public from day one.** Even a near-empty repo on day one becomes
   "this person has been doing this for X months" by month three.
   I can't retroactively start the timeline.

## Things I'm still fuzzy on

1. **Branches.** I've only ever worked on `main`. I know `git branch`
   and `git checkout` exist but haven't needed them yet. Eventually
   I'll want to learn proper branching for "in-progress" work.

2. **What does `HEAD` actually mean?** I see it in git output but
   don't have a clean mental model. Something like "where you are
   right now in commit history" but I'd need to think about it.

3. **Removing secrets from git history** vs from the current state.
   Did the basic version when I removed the `changeme` password from
   the user-data files, but the secret is still in old commits if
   someone digs. `git-filter-repo` exists for the more thorough version
   but I haven't done it.

## Commands I now actually understand

| Command | What it does |
|---------|--------------|
| `git init` | Make a directory into a git repo |
| `git clone <url>` | Download a repo from GitHub |
| `git status` | Show working tree and staging state |
| `git add <file>` | Stage a change for the next commit |
| `git commit -m "msg"` | Snapshot staged changes with a message |
| `git push` | Upload local commits to remote |
| `git pull` | Fetch remote changes and merge/rebase them in |
| `git log --oneline -5` | Show last 5 commits in compact form |
| `git remote -v` | Show where this repo pushes/pulls from |
| `git config --global pull.rebase true` | Default pulls to rebase rather than merge |
| `git config --global credential.helper store` | Save credentials so I don't re-enter the token |

## Next session

Session 2 — actually build something on top of the repo. virt-manager,
libvirt, VMs. The repo is the foundation; now to fill it with real
work.
