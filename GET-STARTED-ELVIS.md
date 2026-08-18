# Getting started with the Wepop workspace

*A setup and how-to guide for Elvis. Written to be followed top to bottom. If you get stuck, note the step number and send it to Aakash, and he can pick it up from exactly there.*

---

## What this is, in one minute

Aakash has set up a shared GitHub repo that holds all the Wepop project documentation: decisions, designs, status, meeting notes, and a running record of what is happening. You, Aakash, and Deepak each work in the same repo from your own computers, and everyone stays in sync.

You will use two apps:

- **GitHub Desktop** keeps your copy of the repo in step with everyone else's. You will click three buttons in it: Fetch, Commit, Push.
- **The Claude desktop app (Cowork)** is where you actually do the work. You open the repo folder in it, talk to Claude in plain English, and it reads and writes the project files for you.

You never touch anything technical by hand. You talk to Claude, and you press a couple of buttons in GitHub Desktop to sync. That is the whole system.

## A few words in plain language

You do not need to know Git. It helps to know these five words though:

- **Repo:** the project folder that lives on GitHub and on your computer.
- **Sync:** getting the latest changes and sending yours, so everyone sees the same thing.
- **Commit:** saving a labelled snapshot of your changes, with a short note about what you did.
- **Push / Pull:** Push sends your saved changes up to GitHub. Pull brings everyone else's down.
- **Your workspace:** your own private folder in the repo (`workspaces/elvis/`). You write freely there. The shared files are looked after by Aakash, and Claude handles that for you, so you never have to worry about stepping on anyone.

---

## Before you start, you need

- Your computer (Mac or Windows).
- Your GitHub account. Yours is **programinator-elvis**, already on file.
- The Claude desktop app, signed in with your Claude account. If you are not sure your account has Cowork, tell Aakash and he will sort it.
- The invite from Aakash to the Wepop repo (it arrives by email or as a GitHub notification).

---

## Part 1 - One-time setup

You do this once. It takes about fifteen minutes.

### Step 1 - Accept the GitHub invite
Open the invite email from GitHub (or the link Aakash sends you) and click **Accept invitation**. This gives you access to the repo. If you cannot find the invite, ask Aakash to resend it to programinator-elvis.

### Step 2 - Install GitHub Desktop and sign in
Download it from **desktop.github.com**, install it, open it, and sign in with your GitHub account (programinator-elvis). This is the app that keeps your copy in sync.

### Step 3 - Clone the repo to your computer
In GitHub Desktop, go to **File > Clone repository**. Pick the Wepop repo from the list (it shows up now that you have accepted the invite), choose a folder on your computer to keep it in, and click **Clone**. "Clone" just means download your own working copy. Remember where you put it.

### Step 4 - Install the Claude desktop app and sign in
Download and install the Claude desktop app, then sign in. This is where you will do the work.

### Step 5 - Open the repo folder in Claude
In the Claude desktop app, start a new Cowork task and choose to run it **On your computer** (not in the cloud), so Claude can see the repo folder you just cloned. Use **Add folder** and pick the Wepop repo folder from Step 3. Claude can now read and write the project files.

### Step 6 - Say hello and let Claude brief you
In that Claude session, type **"start session"** (or "good morning"). Claude will read the project rules and give you a short briefing on where things stand. That is your signal that everything is connected and working.

If Step 6 gives you a proper briefing, your setup is done. If anything looks off, note the step number and send it to Aakash.

---

## Part 2 - Five golden rules (this is the safety part)

These keep the shared record clean and make sure nothing surprising ever happens.

1. **Claude never touches GitHub for you.** It will not push, pull, or commit. You are always the one who clicks the buttons in GitHub Desktop, so nothing ever leaves your machine without you. On purpose.
2. **Work in your own space.** You write in `workspaces/elvis/`. You do not edit the shared files or anyone else's folder directly. If you want to change something shared, you ask Claude and it proposes the change for Aakash to fold in (see Part 5). Claude knows these rules and will steer you, so you cannot really get this wrong.
3. **Always start with "start session" and end with "end session".** Start pulls you up to date and briefs you. End writes a short log of what you did, so the team record stays complete.
4. **Sync at both ends.** Fetch and Pull in GitHub Desktop before you work, Commit and Push after. Details in Part 3.
5. **No app code in this repo.** This repo is for documentation and designs only. The actual app code lives in separate repos that Deepak looks after.

---

## Part 3 - Your everyday routine

Every time you sit down to work, it is the same five moves.

### Before you work
1. Open **GitHub Desktop** and click **Fetch origin**. If it offers to **Pull**, click it. You now have everyone's latest changes.
2. Open the **Claude** desktop app on the Wepop folder and type **"start session"**. Read the short briefing.

### While you work
3. Just talk to Claude in plain English. Share your latest designs, ask it to note a decision, ask what is still open. It does the filing for you. Part 4 lists the handy phrases.

### When you finish
4. In Claude, type **"end session"**. It writes your session log and suggests a commit message that starts with `[elvis]`.
5. Switch to **GitHub Desktop**. You will see the files that changed. In the Summary box, paste (or type) the `[elvis] ...` message, click **Commit to main**, then click **Push origin**. Done. Your work is now shared with the team.

That is it. Fetch and Pull, start session, work, end session, Commit and Push.

---

## Part 4 - The skills (and how to "install" them)

Here is the good news: **there is nothing to install.** The skills are small instruction files that already live inside the repo, in the `skills/` folder. Because they travel with the repo, the moment you open the folder in Claude they are available. You use one simply by saying its trigger phrase in plain English.

For example, say *"here are my latest designs"* or *"design intake"* and Claude will version and catalog your design drop into the record. Say *"propose this decision"* and it writes up the decision for Aakash to fold in.

The phrases you will use most:

| Say this | What Claude does |
|----------|------------------|
| "start session" / "good morning" | Brings you up to date and briefs you |
| "end session" / "wrap up" | Logs your session and preps your commit |
| "design intake" / "here are my latest designs" | Versions and catalogs a design drop, flags gaps |
| "propose this decision" / "log this decision" | Writes up a decision for Aakash to fold in |
| "add a risk" | Notes a project risk |
| "track this question" / "open questions" | Keeps a question from getting lost |

There are more (28 in total). For the full list with trigger phrases, open **README.md** in the repo, or **skills/TRIGGERS.md**. If Claude ever does not recognise a skill by name, just say: *"read the skill at skills/[name]/SKILL.md and follow it."*

---

## Part 5 - Changing something in the shared files

Sometimes you will want to change a shared file, like recording a decision or flagging a risk. You do not edit those files yourself. Instead you tell Claude what you want, and it writes a short *proposal* in your own workspace. Next time Aakash runs his session, he folds the clean proposals into the shared record. If two people proposed something about the same thing, it gets set aside for Aakash to decide, so nothing collides.

You do not have to remember any of this. Just say what you want ("let us record that we decided X", "add a risk about Y") and Claude routes it correctly. This is the "propose, and the owner folds it in" model that keeps everyone from overwriting each other.

---

## Part 6 - If you get stuck or need help

Two things make this painless:

- Every step in this guide is numbered. If something does not work, just tell Aakash **which step number** you are on and what you saw. He can jump in from exactly that point.
- If Claude ever seems unsure, you can always ask it plainly: *"what should I do next?"* or *"where are we in the setup?"*

Nothing you do in Claude is final until you Push in GitHub Desktop, so you can always stop, ask, and pick it back up.

---

## Part 7 - Your to-do checklist

Tick these off as you go. The numbers match the steps above, so you can point to exactly where you are.

**One-time setup**

- [ ] Step 1 - Accepted the GitHub invite
- [ ] Step 2 - Installed GitHub Desktop and signed in
- [ ] Step 3 - Cloned the Wepop repo to my computer
- [ ] Step 4 - Installed the Claude desktop app and signed in
- [ ] Step 5 - Opened the repo folder in Claude (On your computer, Add folder)
- [ ] Step 6 - Typed "start session" and got a briefing

**My first real session (a practice run)**

- [ ] A - Fetched and Pulled in GitHub Desktop
- [ ] B - Typed "start session" in Claude and read the briefing
- [ ] C - Tried one skill, for example shared a design with "design intake", or said "propose this decision"
- [ ] D - Typed "end session" in Claude
- [ ] E - In GitHub Desktop, committed with an `[elvis] ...` message and clicked Push

Once you have ticked every box, you are fully set up and running the same way Aakash and Deepak are. Welcome aboard.

---

*Questions on any step go to Aakash. Just say the step number.*
