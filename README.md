# git tools

- `git-edit`

  Uses `git rebase` to edit a particular command. When you are
  finished editing, run `git rebase --continue`.

- `git-fixup`

  Apply changes to a particular commit.  This combines `git commmit
  --fixup` with the necessary `git rebase --autosquash ...`.

- `git-mark`/`git-unmark`

  Apply tags to the subject line of git commit messages.

  ```
  $ git log --oneline HEAD~4..
  2498130 (HEAD -> master) added routines necessary to support motion detection
  7f66db9 added set_bitfield method
  4be67fc added code to wait for stable gyros before calibrating
  c141e09 rewrote to send data via udp
  $ git mark HEAD~2..
  Rewrite 7f66db91133ad5de1f5ca023ea4f64b4067bff85 (1/2) (0 seconds passed, remaining 0 predicted
  Rewrite 249813046351ef2952e684ad183a94aafbc85580 (2/2) (0 seconds passed, remaining 0 predicted)
  Ref 'refs/heads/master' was rewritten
  $ git log --oneline HEAD~4
  1d05a35 (HEAD -> master) [WIP] added routines necessary to support motion detection
  ce6ad57 [WIP] added set_bitfield method
  4be67fc added code to wait for stable gyros before calibrating
  c141e09 rewrote to send data via udp
  ```

- `git-resume`

  Open modified files in ~~an editor~~ vim (technically, in
  `${VISUAL}`, but this relies on the `-p` flag to vim to open the
  files in tabs so it's unlikely to work with other editors without
  modification).
  
  With the `--commit` (`-c`) option, open the files modified in the
  last commit.
