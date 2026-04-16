---
date: 2026-04-16T15:59:57+00:00
draft: false
title: 'Automating Your Backports'
cover:
  image: "/content/images/2026/Backport-PRs.png"
  alt: "Successfully Created Backports"
  relative: true
---

# Here's the rub

I joined npm about a little over a year ago, and never really had to deal with backporting. npm 11 was pretty well established at that point, and any dealings with npm 10 were really just dependency updates.

As we gear up for npm 12, I learned that we'll have to do quite a bit of backporting. In npm-land, that means manually cherry picking or creating commits and creating a duplicate PR, but against the other supported branches. I had little interest in doing that by hand.

# Here's the answer

This is where actions shine. In the main GitHub repository, I was familiar with using labels to trigger backports. I wrote my own for npm. Any pull request with a matching backport version label should trigger the action. Also, adding a label to an already-merged PR would do the same. Boom - done. Now we can easily get all the needed backports to the appropriate branches.

The [workflow](https://github.com/npm/cli/blob/latest/.github/workflows/backport.yml) listens for `pull_request_target` events — both `closed` and `labeled` — so you can slap the label on before or after merging:

```yaml
on:
  pull_request_target:
    types: [closed, labeled]
```

The label name maps directly to a branch — `backport:10` targets `release/10`.

# Specific Challenges

There was some tricky logic involved in the [backporting script](https://github.com/npm/cli/blob/latest/scripts/backport.js). As a result of using [`release-please`](https://github.com/googleapis/release-please) and [`conventional commits`](https://www.conventionalcommits.org/), we couldn't just grab the merge code and make one commit for all of it. Sure, in a squashed merge, that is the easy thing to do. In a PR where each commit needs to maintain its atomic commit and message - signaling to the changelog where and what each change is. The action code had to be smart about cherry-picking commits and maintaining the changelog-ability.

The script inspects the merge commit to figure out the strategy, then adjusts:

- **Merge commit** (multiple parents) → `cherry-pick -m 1`
- **Rebase merge** (commit subjects match the PR) → `cherry-pick` the full range
- **Squash merge** (everything else) → `cherry-pick` the single commit

The rebase case is the important one. Each commit carries its own conventional commit message (`fix:`, `feat:`, etc.), and `release-please` uses those to build the changelog. If we squashed them into one, we'd lose that granularity.

# Issues

We came across some quirks. First, the way it cherry-picks the commits means that they are their own commits in the other branch — if you signed the commit, you lose that validation.

Also, as a protective measure against infinite loops, workflows creating PRs don't trigger other workflows. I worked around this by calling `actions.createWorkflowDispatch` to fire `ci.yml` on the backport branch directly. The CI runs and the tests pass, but the PR status checks still don't light up green because the run isn't associated with the PR. The best workaround we have is to close and reopen the PR — that re-triggers the normal `pull_request` event and gets the checks wired up properly. Unfortunate, but we are still in a much better place.

# Conclusion

In the end, I took a whole lot of drudgery out of the backporting process. I can't believe they've been doing it manually all these years! I wouldn't be surprised if it's my greatest npm contribution.

**Authors Note** 
Yes, I did write this myself. I've grown to like emdashes.